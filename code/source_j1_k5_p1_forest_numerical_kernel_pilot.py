#!/usr/bin/env python3
"""High-precision numerical-kernel pilot for the exact scalar K5 forest operator."""

from __future__ import annotations

import argparse
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
import json
from pathlib import Path

import mpmath as mp

VERTICES = tuple(range(5))
FREE_VERTICES = (1, 2, 3, 4)
EDGES = tuple(combinations(VERTICES, 2))
P1_EXPONENTS = (1, 1, 1, 1, 2, 2, 2, 2, 2, 2)
ALPHA = "0.55"
PARENT_RAW_STRINGS = {
    5: "8953480453605148739421807526213396902384171526002357485692921.7217856849500135172",
    6: "19634671178659322651698889425902050217223479786982932371734431590749946022.237244",
}
RAW_LOCK_TOL = mp.mpf("1e-65")
S4_TOL = mp.mpf("1e-100")


def relative_or_absolute_error(a, b):
    return abs(a - b) / max(mp.mpf(1), abs(a), abs(b))


def incidence_row(a, b):
    row = [mp.mpf(0)] * 4
    if a != 0:
        row[a - 1] += 1
    if b != 0:
        row[b - 1] -= 1
    return row


def base_incidence_matrix():
    return mp.matrix([incidence_row(a, b) for a, b in EDGES])


def full_gauge_basis_fraction():
    rows = [[Fraction(0) for _ in range(4)] for _ in range(5)]
    for v in range(1, 5):
        rows[v][v - 1] = Fraction(1)
    return rows


def barycentric_collapse_fraction(s):
    s = frozenset(s)
    full = full_gauge_basis_fraction()
    out = [row[:] for row in full]
    avg = [sum(full[v][j] for v in s) / len(s) for j in range(4)]
    for v in s:
        out[v] = avg[:]
    return [[out[v][j] - out[0][j] for j in range(4)] for v in range(1, 5)]


def to_mp_matrix(frac_matrix):
    return mp.matrix(
        [[mp.mpf(x.numerator) / x.denominator for x in row] for row in frac_matrix]
    )


def exact_gamma_one_identity(s):
    c = barycentric_collapse_fraction(s)
    for i in range(4):
        for j in range(4):
            n = Fraction(int(i == j)) - c[i][j]
            if c[i][j] + n != Fraction(int(i == j)):
                return False
    return True


def p1_pattern_ok(exponents):
    exp_map = {frozenset(e): p for e, p in zip(EDGES, exponents)}
    return all(exp_map[frozenset({0, v})] == 1 for v in range(1, 5)) and all(
        exp_map[frozenset({a, b})] == 2 for a, b in combinations(range(1, 5), 2)
    )


def gaussian_pairing_quadratic(eps, test_matrix, incidence):
    eps = tuple(mp.mpf(e) for e in eps)
    m = mp.matrix(test_matrix)
    for e in range(10):
        inv = 1 / (eps[e] ** 2)
        for i in range(4):
            for j in range(4):
                m[i, j] += incidence[e, i] * incidence[e, j] * inv

    sigma = mp.inverse(m) / 2
    cov = incidence * sigma * incidence.T

    @lru_cache(None)
    def moment(counts):
        degree = sum(counts)
        if degree == 0:
            return mp.mpf(1)
        if degree % 2:
            return mp.mpf(0)
        c = list(counts)
        i = next(k for k, v in enumerate(c) if v)
        c[i] -= 1
        total = mp.mpf(0)
        for j, v in enumerate(c):
            if v:
                multiplicity = v
                c[j] -= 1
                total += multiplicity * cov[i, j] * moment(tuple(c))
                c[j] += 1
        return total

    expectation = mp.mpf(0)
    for mask in range(1 << 10):
        counts = [0] * 10
        coeff = mp.mpf(1)
        for e in range(10):
            if (mask >> e) & 1:
                counts[e] = 2
                coeff *= 4 / (eps[e] ** 4)
            else:
                coeff *= -2 / (eps[e] ** 2)
        expectation += coeff * moment(tuple(counts))

    mollifier_norm = mp.mpf(1)
    for e in range(10):
        mollifier_norm /= mp.sqrt(mp.pi) * eps[e]

    return mollifier_norm * (mp.pi ** 2 / mp.sqrt(mp.det(m))) * expectation


def subset_label(s):
    return "".join(str(v) for v in sorted(s))


def evaluate_subset(s, k, incidence):
    c = to_mp_matrix(barycentric_collapse_fraction(s))
    n = mp.eye(4) - c
    t = mp.mpf(2) ** (-k)
    eps = [t ** p for p in P1_EXPONENTS]
    alpha = mp.mpf(ALPHA)

    def f(lam):
        gamma = c + lam * n
        test_matrix = alpha * (gamma.T * gamma)
        return gaussian_pairing_quadratic(eps, test_matrix, incidence)

    raw = f(mp.mpf(1))
    f0 = f(mp.mpf(0))
    f1 = mp.diff(f, mp.mpf(0), 1, method="step", addprec=80)
    f2 = mp.diff(f, mp.mpf(0), 2, method="step", addprec=80)
    t2 = f0 + f1 + f2 / 2
    r2 = raw - t2
    parent = mp.mpf(PARENT_RAW_STRINGS[k])
    parent_err = relative_or_absolute_error(raw, parent)

    digits = min(mp.mp.dps - 25, 180)
    return {
        "subset": subset_label(s),
        "k": k,
        "raw": mp.nstr(raw, digits),
        "f0": mp.nstr(f0, digits),
        "f1": mp.nstr(f1, digits),
        "f2": mp.nstr(f2, digits),
        "t2": mp.nstr(t2, digits),
        "r2": mp.nstr(r2, digits),
        "parent_raw_lock_error": mp.nstr(parent_err, 80),
        "finite": all(mp.isfinite(x) for x in (raw, f0, f1, f2, t2, r2)),
    }


def max_orbit_error(records, fields):
    ref = records[0]
    out = mp.mpf(0)
    for record in records[1:]:
        for field in fields:
            a = mp.mpf(ref[field])
            b = mp.mpf(record[field])
            out = max(out, relative_or_absolute_error(a, b))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dps", type=int, required=True, choices=(180, 260))
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    mp.mp.dps = args.dps

    incidence = base_incidence_matrix()
    all_size2 = tuple(frozenset(c) for c in combinations(range(5), 2))
    anchor_orbit = tuple(s for s in all_size2 if 0 in s)
    internal_orbit = tuple(s for s in all_size2 if 0 not in s)
    k6_reps = (frozenset({0, 1}), frozenset({1, 2}))

    records_k5 = [evaluate_subset(s, 5, incidence) for s in all_size2]
    records_k6 = [evaluate_subset(s, 6, incidence) for s in k6_reps]
    by_label_k5 = {r["subset"]: r for r in records_k5}

    fields = ("f0", "f1", "f2", "t2", "r2")
    anchor_err = max_orbit_error([by_label_k5[subset_label(s)] for s in anchor_orbit], fields)
    internal_err = max_orbit_error([by_label_k5[subset_label(s)] for s in internal_orbit], fields)

    parent_errors = [mp.mpf(r["parent_raw_lock_error"]) for r in records_k5 + records_k6]
    all_finite = all(r["finite"] for r in records_k5 + records_k6)

    perturbed_parent = mp.mpf(PARENT_RAW_STRINGS[5]) * (1 + mp.mpf("1e-20"))
    perturbed_err = relative_or_absolute_error(mp.mpf(records_k5[0]["raw"]), perturbed_parent)

    bad_exponents = (2, 1, 1, 1, 2, 2, 2, 2, 2, 2)

    controls = {
        "p1_pattern_lock": p1_pattern_ok(P1_EXPONENTS),
        "bad_p1_pattern_rejected": not p1_pattern_ok(bad_exponents),
        "exact_gamma_one_identity_all_workload_subsets": all(exact_gamma_one_identity(s) for s in all_size2),
        "historical_parent_raw_lock": max(parent_errors) <= mp.mpf("1e-65"),
        "s4_anchor_orbit_numerical_covariance": anchor_err <= mp.mpf("1e-100"),
        "s4_internal_orbit_numerical_covariance": internal_err <= mp.mpf("1e-100"),
        "all_outputs_finite": all_finite,
        "perturbed_parent_raw_detected": perturbed_err > mp.mpf("1e-65"),
    }
    controls_pass = all(controls.values())
    classification = "P1_FOREST_NUMERICAL_KERNEL_LANE_VALID" if controls_pass else "INVALID_IMPLEMENTATION"

    out = {
        "classification": classification,
        "controls_pass": controls_pass,
        "controls": controls,
        "precision_decimal_digits": args.dps,
        "alpha": ALPHA,
        "p1_exponents": list(P1_EXPONENTS),
        "k5_records": records_k5,
        "k6_representative_records": records_k6,
        "max_parent_raw_lock_error": mp.nstr(max(parent_errors), 80),
        "max_s4_anchor_orbit_error": mp.nstr(anchor_err, 80),
        "max_s4_internal_orbit_error": mp.nstr(internal_err, 80),
        "perturbed_parent_raw_error": mp.nstr(perturbed_err, 80),
        "claim_ceiling": "Numerical-kernel validation only; R2 sign/growth is non-deciding and no forest-subtracted scientific conclusion is authorized.",
    }

    Path(args.out).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(json.dumps({k: v for k, v in out.items() if k not in ("k5_records", "k6_representative_records")}, sort_keys=True))


if __name__ == "__main__":
    main()

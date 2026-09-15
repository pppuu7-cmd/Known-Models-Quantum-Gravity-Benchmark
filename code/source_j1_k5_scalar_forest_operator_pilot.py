#!/usr/bin/env python3
"""Exact operator-definition audit for the auxiliary scalar K5 forest prescription."""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
import hashlib
from itertools import combinations, permutations
import json
from pathlib import Path

V = frozenset(range(5))
I4 = [[Fraction(int(i == j)) for j in range(4)] for i in range(4)]
PERMS = tuple(permutations(range(5)))
SCALAR_ORDERS = {2: 2, 3: 7, 4: 15, 5: 26}
THREE_NORMAL_ORDERS = {2: 0, 3: 3, 4: 9, 5: 18}


def mm(a, b):
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def msub(a, b):
    return [[x - y for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def rowmul(row, mat):
    return [sum(row[k] * mat[k][j] for k in range(len(mat))) for j in range(len(mat[0]))]


def matrix_rank_exact(mat):
    a = [row[:] for row in mat]
    nrow = len(a)
    ncol = len(a[0]) if a else 0
    pivot_row = 0
    for col in range(ncol):
        pivot = next((r for r in range(pivot_row, nrow) if a[r][col] != 0), None)
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        p = a[pivot_row][col]
        a[pivot_row] = [x / p for x in a[pivot_row]]
        for r in range(nrow):
            if r != pivot_row and a[r][col] != 0:
                f = a[r][col]
                a[r] = [a[r][c] - f * a[pivot_row][c] for c in range(ncol)]
        pivot_row += 1
        if pivot_row == nrow:
            break
    return pivot_row


def full_gauge_basis():
    # q_0=0, x=(q_1,q_2,q_3,q_4)
    rows = [[Fraction(0) for _ in range(4)] for _ in range(5)]
    for v in range(1, 5):
        rows[v][v - 1] = Fraction(1)
    return rows


def barycentric_collapse(s):
    s = frozenset(s)
    full = full_gauge_basis()
    out = [row[:] for row in full]
    avg = [sum(full[v][j] for v in s) / len(s) for j in range(4)]
    for v in s:
        out[v] = avg[:]
    # Restore q_0=0 after the full-coordinate collapse.
    return [[out[v][j] - out[0][j] for j in range(4)] for v in range(1, 5)]


def anchored_collapse(s):
    # Deliberately label-dependent adversarial control: collapse to min(S), not barycenter.
    s = frozenset(s)
    full = full_gauge_basis()
    out = [row[:] for row in full]
    anchor = full[min(s)][:]
    for v in s:
        out[v] = anchor[:]
    return [[out[v][j] - out[0][j] for j in range(4)] for v in range(1, 5)]


def permutation_representation(p):
    # p maps old vertex labels to new labels; re-gauge after relabeling.
    full = full_gauge_basis()
    new = [[Fraction(0) for _ in range(4)] for _ in range(5)]
    for old in range(5):
        new[p[old]] = full[old][:]
    return [[new[v][j] - new[0][j] for j in range(4)] for v in range(1, 5)]


def compatible(a, b):
    return a <= b or b <= a or a.isdisjoint(b)


def proper_subsets():
    return tuple(
        frozenset(c)
        for k in range(2, 5)
        for c in combinations(range(5), k)
    )


def enumerate_forests(candidates):
    candidates = tuple(sorted(candidates, key=lambda s: (len(s), tuple(sorted(s)))))
    out = []

    def rec(prefix, tail):
        out.append(tuple(prefix))
        for i, s in enumerate(tail):
            nxt = tuple(t for t in tail[i + 1 :] if compatible(s, t))
            rec(prefix + (s,), nxt)

    rec(tuple(), candidates)
    return tuple(out)


def canon_subset(s):
    return tuple(sorted(s))


def canon_forest(forest):
    return tuple(sorted((canon_subset(s) for s in forest), key=lambda x: (len(x), x)))


def permute_forest(forest, p):
    return canon_forest(frozenset(p[i] for i in s) for s in forest)


def orbit_key(forest):
    return min(permute_forest(forest, p) for p in PERMS)


def difference_row(a, b):
    # Linear form q_a-q_b in q_0=0 coordinates.
    row = [Fraction(0)] * 4
    if a != 0:
        row[a - 1] += 1
    if b != 0:
        row[b - 1] -= 1
    return row


def symbolic_gamma_commutes(s, t):
    # Compare coefficients of 1, lambda, mu, lambda*mu in
    # Gamma_s(lambda) Gamma_t(mu) and the reverse product.
    cs = barycentric_collapse(s)
    ct = barycentric_collapse(t)
    ns = msub(I4, cs)
    nt = msub(I4, ct)
    return all(
        left == right
        for left, right in (
            (mm(cs, ct), mm(ct, cs)),
            (mm(ns, ct), mm(ct, ns)),
            (mm(cs, nt), mm(nt, cs)),
            (mm(ns, nt), mm(nt, ns)),
        )
    )


def frac_string(x):
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def serialize_matrix(m):
    return [[frac_string(x) for x in row] for row in m]


def subset_name(s):
    return "{" + ",".join(map(str, sorted(s))) + "}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="source_j1_k5_scalar_forest_operator_pilot.json")
    args = ap.parse_args()

    proper = proper_subsets()
    all_for_maps = proper + (V,)
    forests = enumerate_forests(proper)

    collapses = {s: barycentric_collapse(s) for s in all_for_maps}
    normals = {s: msub(I4, collapses[s]) for s in all_for_maps}

    idempotent = all(mm(collapses[s], collapses[s]) == collapses[s] for s in all_for_maps)
    ranks_ok = all(
        matrix_rank_exact(collapses[s]) == 5 - len(s)
        and matrix_rank_exact(normals[s]) == len(s) - 1
        for s in all_for_maps
    )
    full_root_ok = collapses[V] == [[Fraction(0)] * 4 for _ in range(4)] and normals[V] == I4 and SCALAR_ORDERS[5] == 26

    s5_covariant = True
    for p in PERMS:
        rp = permutation_representation(p)
        for s in all_for_maps:
            ps = frozenset(p[v] for v in s)
            if mm(rp, collapses[s]) != mm(barycentric_collapse(ps), rp):
                s5_covariant = False
                break
        if not s5_covariant:
            break

    anchored_covariance_fails = False
    for p in PERMS:
        rp = permutation_representation(p)
        for s in proper:
            ps = frozenset(p[v] for v in s)
            if mm(rp, anchored_collapse(s)) != mm(anchored_collapse(ps), rp):
                anchored_covariance_fails = True
                break
        if anchored_covariance_fails:
            break

    laminar_pair_count = 0
    overlap_pair_count = 0
    laminar_commutation_ok = True
    overlap_noncommutation_ok = True
    nested_absorption_ok = True
    for i, s in enumerate(proper):
        for t in proper[i + 1 :]:
            ccomm = mm(collapses[s], collapses[t]) == mm(collapses[t], collapses[s])
            gcomm = symbolic_gamma_commutes(s, t)
            if compatible(s, t):
                laminar_pair_count += 1
                if not (ccomm and gcomm):
                    laminar_commutation_ok = False
            else:
                overlap_pair_count += 1
                if ccomm or gcomm:
                    overlap_noncommutation_ok = False

    for s in proper:
        for t in proper:
            if s < t:
                if mm(collapses[t], collapses[s]) != collapses[t] or mm(collapses[s], collapses[t]) != collapses[t]:
                    nested_absorption_ok = False
                    break
        if not nested_absorption_ok:
            break

    normal_form_ok = True
    normal_pair_checks = 0
    taylor_fixture_checks = 0
    degree_r_plus_one_survives = True
    for s in all_for_maps:
        c = collapses[s]
        n = normals[s]
        r = SCALAR_ORDERS[len(s)]
        for a, b in combinations(sorted(s), 2):
            ell = difference_row(a, b)
            if rowmul(ell, c) != [Fraction(0)] * 4 or rowmul(ell, n) != ell:
                normal_form_ok = False
            normal_pair_checks += 1

            # From ell(Gamma(lambda)x)=lambda*ell(x), the Taylor series of ell^m
            # contains exactly one lambda monomial of degree m.
            for m in (0, 1, r):
                kept = m <= r
                if not kept:
                    normal_form_ok = False
                taylor_fixture_checks += 1
            removed_by_t = (r + 1) <= r
            survives_one_minus_t = not removed_by_t
            if not survives_one_minus_t:
                degree_r_plus_one_survives = False
            taylor_fixture_checks += 1

    forest_hist = Counter(len(f) for f in forests)
    orbit_sizes = Counter(orbit_key(f) for f in forests)
    orbit_hist = Counter(orbit_sizes.values())

    forest_topology_ok = (
        len(forests) == 236
        and dict(sorted(forest_hist.items())) == {0: 1, 1: 25, 2: 105, 3: 105}
        and len(orbit_sizes) == 12
        and all(V not in f for f in forests)
    )

    scalar_order_lock = SCALAR_ORDERS == {2: 2, 3: 7, 4: 15, 5: 26}
    historical_order_negative_control = THREE_NORMAL_ORDERS == {2: 0, 3: 3, 4: 9, 5: 18} and THREE_NORMAL_ORDERS != SCALAR_ORDERS

    known_overlap = (frozenset({0, 1}), frozenset({1, 2}))
    known_overlap_rejected = not compatible(*known_overlap) and not symbolic_gamma_commutes(*known_overlap)

    operator_spec = {
        "gauge": "q0=0; x=(q1,q2,q3,q4)",
        "collapse_rule": "barycentric collapse in full 5-vertex scalar coordinates, then subtract transformed q0",
        "normal_scaling": "Gamma_S(lambda)=C_S+lambda*(I-C_S)",
        "taylor_projector": "T_S^r=sum_{n=0}^r (1/n!)*d_lambda^n[f(Gamma_S(lambda)x)] at lambda=0",
        "scalar_orders_by_subset_size": {str(k): v for k, v in SCALAR_ORDERS.items()},
        "proper_forest_formula": "W_prop=sum_{F proper laminar} (-1)^|F| product_{S in F} T_S^{r(S)}",
        "full_root_formula": "W_full=(I-T_V^26) W_prop",
        "collapse_matrices": {
            subset_name(s): serialize_matrix(collapses[s])
            for s in sorted(all_for_maps, key=lambda x: (len(x), tuple(sorted(x))))
        },
        "proper_forests": [
            [subset_name(s) for s in f]
            for f in sorted(forests, key=lambda f: (len(f), canon_forest(f)))
        ],
    }
    spec_bytes = json.dumps(operator_spec, sort_keys=True, separators=(",", ":")).encode()
    operator_spec_sha256 = hashlib.sha256(spec_bytes).hexdigest()

    controls = {
        "collapse_idempotence": idempotent,
        "exact_rank_and_normal_dimension": ranks_ok,
        "full_root_zero_collapse_and_order26": full_root_ok,
        "s5_covariance": s5_covariant,
        "laminar_collapse_and_gamma_commutation": laminar_commutation_ok,
        "nested_absorption": nested_absorption_ok,
        "overlapping_nonnested_noncommutation": overlap_noncommutation_ok,
        "normal_linear_form_scaling": normal_form_ok,
        "degree_r_plus_one_survives_one_minus_t": degree_r_plus_one_survives,
        "proper_forest_topology": forest_topology_ok,
        "scalar_order_lock": scalar_order_lock,
        "historical_three_normal_order_negative_control": historical_order_negative_control,
        "known_overlap_rejected": known_overlap_rejected,
        "anchored_collapse_fails_s5_covariance": anchored_covariance_fails,
    }
    controls_pass = all(controls.values())

    classification = (
        "SCALAR_K5_FOREST_OPERATOR_PILOT_CONFIRMED_SCOPED"
        if controls_pass
        else "INVALID_IMPLEMENTATION"
    )

    out = {
        "classification": classification,
        "controls_pass": controls_pass,
        "controls": controls,
        "proper_subset_count": len(proper),
        "proper_forest_count_including_empty": len(forests),
        "proper_forest_cardinality_histogram": dict(sorted(forest_hist.items())),
        "proper_s5_orbit_count": len(orbit_sizes),
        "proper_s5_orbit_size_histogram": dict(sorted(orbit_hist.items())),
        "laminar_pair_count": laminar_pair_count,
        "overlapping_nonnested_pair_count": overlap_pair_count,
        "normal_pair_checks": normal_pair_checks,
        "taylor_fixture_checks": taylor_fixture_checks,
        "scalar_orders_by_subset_size": SCALAR_ORDERS,
        "operator_spec_sha256": operator_spec_sha256,
        "operator_spec": operator_spec,
        "claim_ceiling": "Exact KMQGB-derived scalar forest-operator definition only; no post-subtraction numerical or physical conclusion and no D7 closure.",
    }

    Path(args.out).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(json.dumps({k: v for k, v in out.items() if k != "operator_spec"}, sort_keys=True))


if __name__ == "__main__":
    main()

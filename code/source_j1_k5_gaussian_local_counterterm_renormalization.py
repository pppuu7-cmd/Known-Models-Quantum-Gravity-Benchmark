#!/usr/bin/env python3
"""Frozen lane evaluator for SOURCE_J1_K5_GAUSSIAN_LOCAL_COUNTERTERM_RENORMALIZATION_GATE."""

from __future__ import annotations

import argparse
from functools import lru_cache
from itertools import combinations
import json
from pathlib import Path

import mpmath as mp

mp.mp.dps = 180

VERTICES = (1, 2, 3, 4, 5)
FREE_VERTICES = (2, 3, 4, 5)
EDGES = tuple(combinations(VERTICES, 2))
EDGE_NAMES = tuple(f"{a}{b}" for a, b in EDGES)
K_USED = (5, 6, 7, 8)
PATHS = {
    "P1": (1, 1, 1, 1, 2, 2, 2, 2, 2, 2),
    "P2": (2, 2, 2, 2, 1, 1, 1, 1, 1, 1),
    "P3": (1, 2, 3, 4, 2, 3, 4, 3, 4, 4),
}
A_CAL = tuple(mp.mpf("0.50") + mp.mpf("0.10") * i for i in range(14))
A_TEST = tuple(mp.mpf(x) for x in ("0.55", "0.95", "1.35", "1.75", "1.95"))
CENTER = mp.mpf("1.15")
SCALE = mp.mpf("0.65")

# Durable parent artifact serializes these values to ~50 significant digits.
PARENT_ALPHA1 = {
    "P1": {
        5: mp.mpf("8.9510136719908333656615197048707843316562750852333e60"),
        6: mp.mpf("1.9633312684248074342314464767612631634535680997002e73"),
        7: mp.mpf("4.314651505876584945816521638588520059271053734886e85"),
        8: mp.mpf("9.4865017199109286106452809809068287930119331797525e97"),
    },
    "P2": {
        5: mp.mpf("245870337345958841759501297345495631316828202.40385"),
        6: mp.mpf("1.7011669634822373234545959023701290547789019612741e52"),
        7: mp.mpf("1.1503980263516685214704565557842195403961344723214e60"),
        8: mp.mpf("7.7349715478329779506879606195894931263878381881271e67"),
    },
    "P3": {
        5: mp.mpf("2.8504231751760102048172903131415132341424544375567e103"),
        6: mp.mpf("2.1446274351862920840626223822442457918986960673853e123"),
        7: mp.mpf("1.5902115441755380115653326873448219689430918674374e143"),
        8: mp.mpf("1.1748053789687323618824129528291495419221411873518e163"),
    },
}


def incidence_row(a: int, b: int):
    row = [mp.mpf("0")] * 4
    if a != 1:
        row[FREE_VERTICES.index(a)] += 1
    if b != 1:
        row[FREE_VERTICES.index(b)] -= 1
    return row


def build_A(mapped_vertices=None):
    if mapped_vertices is None:
        mapped_vertices = {v: v for v in VERTICES}
    rows = []
    for a, b in EDGES:
        aa, bb = mapped_vertices[a], mapped_vertices[b]
        if aa > bb:
            aa, bb = bb, aa
        rows.append(incidence_row(aa, bb))
    return mp.matrix(rows)


A = build_A()


def leading_principal_minors_positive(M):
    for n in range(1, 5):
        sub = mp.matrix([[M[i, j] for j in range(n)] for i in range(n)])
        if not (mp.det(sub) > 0):
            return False
    return True


def gaussian_pairing_alpha(eps, alpha, A_matrix=A):
    eps = tuple(mp.mpf(e) for e in eps)
    alpha = mp.mpf(alpha)
    if alpha <= 0 or len(eps) != 10 or any(e <= 0 for e in eps):
        raise ValueError("alpha and all ten epsilon values must be positive")

    M = mp.eye(4) * alpha
    for e in range(10):
        inv = 1 / (eps[e] ** 2)
        for i in range(4):
            for j in range(4):
                M[i, j] += A_matrix[e, i] * A_matrix[e, j] * inv

    if not leading_principal_minors_positive(M):
        raise ArithmeticError("precision/control failure: M not positive definite")

    Sigma = mp.inverse(M) / 2
    C = A_matrix * Sigma * A_matrix.T
    sym_err = max(abs(C[i, j] - C[j, i]) for i in range(10) for j in range(10))
    if sym_err > mp.mpf("1e-150"):
        raise ArithmeticError(f"covariance symmetry control failed: {sym_err}")

    @lru_cache(None)
    def moment(counts):
        if sum(counts) == 0:
            return mp.mpf(1)
        if sum(counts) % 2:
            return mp.mpf(0)
        c = list(counts)
        i = next(k for k, v in enumerate(c) if v)
        c[i] -= 1
        total = mp.mpf(0)
        for j, v in enumerate(c):
            if v:
                multiplicity = v
                c[j] -= 1
                total += multiplicity * C[i, j] * moment(tuple(c))
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

    value = mollifier_norm * (mp.pi ** 2 / mp.sqrt(mp.det(M))) * expectation
    return value, sym_err


def zcoord(alpha):
    return (mp.mpf(alpha) - CENTER) / SCALE


def solve_interpolant(xs, ys):
    V = mp.matrix([[zcoord(x) ** j for j in range(14)] for x in xs])
    b = mp.matrix(ys)
    return tuple(mp.lu_solve(V, b))


def polynomial_value(coeffs, alpha):
    z = zcoord(alpha)
    out = mp.mpf(0)
    for c in reversed(coeffs):
        out = out * z + c
    return out


def barycentric_value(xs, ys, alpha):
    zs = [zcoord(x) for x in xs]
    z = zcoord(alpha)
    for zi, yi in zip(zs, ys):
        if z == zi:
            return yi
    weights = []
    for i, zi in enumerate(zs):
        prod = mp.mpf(1)
        for j, zj in enumerate(zs):
            if i != j:
                prod *= zi - zj
        weights.append(1 / prod)
    num = mp.mpf(0)
    den = mp.mpf(0)
    for wi, zi, yi in zip(weights, zs, ys):
        q = wi / (z - zi)
        num += q * yi
        den += q
    return num / den


def relative_or_absolute_error(a, b):
    return abs(a - b) / max(mp.mpf(1), abs(a), abs(b))


def delta_identity_control():
    # Independent radial recurrence: Delta(s^n)=4 n(n+1) s^(n-1) in d=4.
    alpha = mp.mpf("1.37")
    checks = []
    for j in range(5):
        if j == 0:
            recurrence = mp.mpf(1)
        else:
            # coefficient of s^j in exp(-alpha s), followed by j Laplacians.
            coeff = (-alpha) ** j / mp.factorial(j)
            factor = mp.mpf(1)
            for n in range(j, 0, -1):
                factor *= 4 * n * (n + 1)
            recurrence = coeff * factor
        closed = (-4 * alpha) ** j * mp.factorial(j + 1)
        checks.append(relative_or_absolute_error(recurrence, closed))
    return max(checks) <= mp.mpf("1e-150"), checks


def degree14_adversarial_control():
    ys = [zcoord(a) ** 14 for a in A_CAL]
    coeffs = solve_interpolant(A_CAL, ys)
    errors = [abs(zcoord(a) ** 14 - polynomial_value(coeffs, a)) for a in A_TEST]
    return max(errors) > mp.mpf("1e-20"), errors


def classify_residual_sequence(residuals):
    r = [mp.mpf(v) for v in residuals]
    d56 = abs(r[1] - r[0])
    d67 = abs(r[2] - r[1])
    d78 = abs(r[3] - r[2])
    rel78 = d78 / max(mp.mpf(1), abs(r[3]), abs(r[2]))
    finite = d56 > d67 > d78 and rel78 <= mp.mpf("1e-8")

    abs_tail = [abs(r[1]), abs(r[2]), abs(r[3])]
    divergent = False
    growth = [None, None]
    if all(v > 0 for v in abs_tail) and abs_tail[0] < abs_tail[1] < abs_tail[2]:
        growth = [mp.log(abs_tail[1] / abs_tail[0], 2), mp.log(abs_tail[2] / abs_tail[1], 2)]
        divergent = (growth[0] + growth[1]) / 2 >= 2

    if finite:
        status = "FINITE_COMPATIBLE"
    elif divergent:
        status = "DIVERGENT_AFTER_LOCAL_SUBTRACTION"
    else:
        status = "INCONCLUSIVE"
    return status, {
        "d56": d56,
        "d67": d67,
        "d78": d78,
        "rel78": rel78,
        "growth_6to7": growth[0],
        "growth_7to8": growth[1],
    }


def evaluate_lane(path):
    if path not in PATHS:
        raise ValueError(path)

    controls = {
        "star_coordinate_basis": tuple(tuple(int(A[i, j]) for j in range(4)) for i in range(4))
        == ((-1, 0, 0, 0), (0, -1, 0, 0), (0, 0, -1, 0), (0, 0, 0, -1)),
    }
    delta_ok, delta_errors = delta_identity_control()
    controls["delta_identity"] = delta_ok
    degree14_ok, degree14_errors = degree14_adversarial_control()
    controls["degree14_fixture_detected"] = degree14_ok

    values = {str(a): {} for a in A_TEST}
    fit_diagnostics = {}
    parent_lock_errors = {}
    max_cov_sym = mp.mpf(0)
    max_cal_resid = mp.mpf(0)
    max_prediction_disagreement = mp.mpf(0)

    for k in K_USED:
        t = mp.mpf(2) ** (-k)
        eps = [t ** p for p in PATHS[path]]
        cal_values = []
        for alpha in A_CAL:
            v, sym = gaussian_pairing_alpha(eps, alpha)
            max_cov_sym = max(max_cov_sym, sym)
            cal_values.append(v)

        # Parent alpha=1 lock uses the calibration value at index 5.
        parent_err = relative_or_absolute_error(cal_values[5], PARENT_ALPHA1[path][k])
        parent_lock_errors[str(k)] = parent_err

        coeffs = solve_interpolant(A_CAL, cal_values)
        cal_resids = [relative_or_absolute_error(polynomial_value(coeffs, a), y) for a, y in zip(A_CAL, cal_values)]
        max_cal_resid = max(max_cal_resid, max(cal_resids))

        fit_diagnostics[str(k)] = {
            "max_calibration_relative_or_absolute_residual": mp.nstr(max(cal_resids), 50),
            "parent_alpha1_lock_error": mp.nstr(parent_err, 50),
        }

        for alpha in A_TEST:
            raw, sym = gaussian_pairing_alpha(eps, alpha)
            max_cov_sym = max(max_cov_sym, sym)
            counterterm = polynomial_value(coeffs, alpha)
            bary = barycentric_value(A_CAL, cal_values, alpha)
            pred_err = relative_or_absolute_error(counterterm, bary)
            max_prediction_disagreement = max(max_prediction_disagreement, pred_err)
            residual = raw - counterterm
            values[str(alpha)][str(k)] = {
                "raw": mp.nstr(raw, 80),
                "counterterm": mp.nstr(counterterm, 80),
                "residual": mp.nstr(residual, 80),
                "barycentric_prediction": mp.nstr(bary, 80),
                "prediction_disagreement": mp.nstr(pred_err, 50),
            }

    controls["parent_alpha1_lock"] = max(parent_lock_errors.values()) <= mp.mpf("1e-45")
    controls["covariance_symmetry"] = max_cov_sym <= mp.mpf("1e-150")
    controls["calibration_interpolation"] = max_cal_resid <= mp.mpf("1e-130")
    controls["linear_barycentric_agreement"] = max_prediction_disagreement <= mp.mpf("1e-120")

    # Frozen vertex relabel control only belongs to P3; other lanes report N/A true.
    vertex_rel_err = None
    if path == "P3":
        swap23 = {1: 1, 2: 3, 3: 2, 4: 4, 5: 5}
        A_perm = build_A(swap23)
        t = mp.mpf(2) ** -5
        eps = [t ** p for p in PATHS["P3"]]
        base, _ = gaussian_pairing_alpha(eps, mp.mpf("1.35"), A)
        perm, _ = gaussian_pairing_alpha(eps, mp.mpf("1.35"), A_perm)
        vertex_rel_err = relative_or_absolute_error(base, perm)
        controls["vertex_relabel"] = vertex_rel_err <= mp.mpf("1e-90")
    else:
        controls["vertex_relabel"] = True

    per_alpha = {}
    for alpha in A_TEST:
        residuals = [mp.mpf(values[str(alpha)][str(k)]["residual"]) for k in K_USED]
        status, diag = classify_residual_sequence(residuals)
        per_alpha[str(alpha)] = {
            "status": status,
            "diagnostics": {
                key: None if val is None else mp.nstr(val, 50) for key, val in diag.items()
            },
        }

    controls_pass = all(controls.values())
    if not controls_pass:
        lane_classification = "INVALID_IMPLEMENTATION"
    elif any(v["status"] == "DIVERGENT_AFTER_LOCAL_SUBTRACTION" for v in per_alpha.values()):
        lane_classification = "LANE_DIVERGENT_AFTER_LOCAL_SUBTRACTION"
    elif all(v["status"] == "FINITE_COMPATIBLE" for v in per_alpha.values()):
        lane_classification = "LANE_FINITE_COMPATIBLE"
    else:
        lane_classification = "LANE_INCONCLUSIVE"

    return {
        "gate": "SOURCE_J1_K5_GAUSSIAN_LOCAL_COUNTERTERM_RENORMALIZATION_GATE",
        "path": path,
        "classification": lane_classification,
        "precision_decimal_digits": mp.mp.dps,
        "k_used": list(K_USED),
        "alpha_cal": [str(a) for a in A_CAL],
        "alpha_test": [str(a) for a in A_TEST],
        "local_basis": "degree<=13 polynomial in alpha, equivalent on radial Gaussian tests to Delta^j delta_0 for j=0..13",
        "controls": controls,
        "controls_pass": controls_pass,
        "control_diagnostics": {
            "max_covariance_symmetry_error": mp.nstr(max_cov_sym, 50),
            "max_calibration_residual": mp.nstr(max_cal_resid, 50),
            "max_linear_barycentric_disagreement": mp.nstr(max_prediction_disagreement, 50),
            "parent_lock_errors": {k: mp.nstr(v, 50) for k, v in parent_lock_errors.items()},
            "delta_identity_errors": [mp.nstr(v, 50) for v in delta_errors],
            "degree14_fixture_heldout_errors": [mp.nstr(v, 50) for v in degree14_errors],
            "vertex_relabel_error": None if vertex_rel_err is None else mp.nstr(vertex_rel_err, 50),
        },
        "fit_diagnostics": fit_diagnostics,
        "heldout_values": values,
        "heldout_path_classification": per_alpha,
        "claim_ceiling": "Auxiliary scalar Gaussian aligned-K5 local-counterterm diagnostic only; not source-authorized Eq4 extension and not D7 closure.",
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--path", required=True, choices=tuple(PATHS))
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    result = evaluate_lane(args.path)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "path": result["path"],
        "classification": result["classification"],
        "controls_pass": result["controls_pass"],
        "heldout_statuses": {a: d["status"] for a, d in result["heldout_path_classification"].items()},
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

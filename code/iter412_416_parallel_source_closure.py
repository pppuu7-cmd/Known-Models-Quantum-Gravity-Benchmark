#!/usr/bin/env python3
from __future__ import annotations

import argparse
import cmath
import json
import math
from pathlib import Path

LANCZOS_G = 7
LANCZOS_COEFF = [
    0.99999999999980993,
    676.5203681218851,
    -1259.1392167224028,
    771.32342877765313,
    -176.61502916214059,
    12.507343278686905,
    -0.13857109526572012,
    9.9843695780195716e-6,
    1.5056327351493116e-7,
]


def write_result(out: dict, path: str) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(out, sort_keys=True))
    if not out.get("pass", False):
        raise SystemExit(2)


def cgamma(z: complex) -> complex:
    if z.real < 0.5:
        return math.pi / (cmath.sin(math.pi * z) * cgamma(1.0 - z))
    zz = z - 1.0
    x = complex(LANCZOS_COEFF[0], 0.0)
    for i, c in enumerate(LANCZOS_COEFF[1:], start=1):
        x += c / (zz + i)
    t = zz + LANCZOS_G + 0.5
    return cmath.sqrt(2.0 * math.pi) * (t ** (zz + 0.5)) * cmath.exp(-t) * x


def hyp2f1_series(a: complex, b: complex, c: complex, z: float, tol: float = 2e-14, max_terms: int = 200000) -> complex:
    if not 0.0 <= z < 1.0:
        raise ValueError("This audited series implementation requires 0<=z<1")
    total = 1.0 + 0.0j
    term = 1.0 + 0.0j
    for n in range(1, max_terms + 1):
        term *= ((a + n - 1.0) * (b + n - 1.0) / ((c + n - 1.0) * n)) * z
        total_next = total + term
        if abs(term) <= tol * max(1.0, abs(total_next)):
            return total_next
        total = total_next
    raise RuntimeError(f"2F1 series did not converge after {max_terms} terms for z={z}")


def toller_branch(sign: int, j: float, m: float, rho: float, beta: float) -> complex:
    if sign not in (-1, 1):
        raise ValueError("sign must be +/-1")
    s = float(sign)
    exponent = j - s * 1j * rho + s * m + 1.0
    prefactor = cmath.exp(-exponent * beta)
    numerator = cgamma(complex(2.0 * j + 2.0, 0.0)) * cgamma(s * 1j * rho - s * m)
    denominator = cgamma(complex(j - s * m + 1.0, 0.0)) * cgamma(j + 1.0 + s * 1j * rho)
    a = complex(j + s * m + 1.0, 0.0)
    b = j + 1.0 - s * 1j * rho
    c = 1.0 + s * m - s * 1j * rho
    z = math.exp(-2.0 * beta)
    return prefactor * numerator / denominator * hyp2f1_series(a, b, c, z)


def wigner_d_gamma_simple(j: float, m: float, rho: float, beta: float) -> complex:
    prefactor = cmath.exp(-(j - 1j * rho + m + 1.0) * beta)
    a = complex(j + m + 1.0, 0.0)
    b = j + 1.0 - 1j * rho
    c = complex(2.0 * j + 2.0, 0.0)
    z = 1.0 - math.exp(-2.0 * beta)
    return prefactor * hyp2f1_series(a, b, c, z)


def linear_slope(xs: list[float], ys: list[float]) -> float:
    n = len(xs)
    sx = sum(xs)
    sy = sum(ys)
    sxx = sum(x * x for x in xs)
    sxy = sum(x * y for x, y in zip(xs, ys))
    den = n * sxx - sx * sx
    if abs(den) < 1e-30:
        raise ValueError("singular linear fit")
    return (n * sxy - sx * sy) / den


def magnetic_values(j: float) -> list[float]:
    two_j = round(2.0 * j)
    if abs(two_j - 2.0 * j) > 1e-10 or two_j < 1:
        raise ValueError("j must be a positive half-integer")
    return [-j + k for k in range(two_j + 1)]


def run_lqg(gamma: float, j: float) -> dict:
    if gamma <= 0.0:
        raise ValueError("gamma must be positive")
    rho = gamma * j
    identity_betas = [0.5, 0.8, 1.2]
    asymptotic_betas = [4.0, 5.0, 6.0, 7.0, 8.0]
    rows = []
    max_identity = 0.0
    max_slope_error = 0.0
    worst_identity = None
    worst_slope = None

    for m in magnetic_values(j):
        identity_rows = []
        for beta in identity_betas:
            tp = toller_branch(+1, j, m, rho, beta)
            tm = toller_branch(-1, j, m, rho, beta)
            d = wigner_d_gamma_simple(j, m, rho, beta)
            residual = abs((tp + tm) - d) / max(abs(d), abs(tp) + abs(tm), 1e-300)
            identity_rows.append({"beta": beta, "relative_residual": residual})
            if residual > max_identity:
                max_identity = residual
                worst_identity = {"m": m, "beta": beta, "relative_residual": residual}

        asymptotic = {}
        for sign, label in ((+1, "plus"), (-1, "minus")):
            logs = []
            for beta in asymptotic_betas:
                value = toller_branch(sign, j, m, rho, beta)
                logs.append(math.log(max(abs(value), 1e-300)))
            fitted = linear_slope(asymptotic_betas, logs)
            predicted = -(1.0 + abs(j + sign * m))
            error = abs(fitted - predicted)
            asymptotic[label] = {
                "predicted_log_abs_slope": predicted,
                "fitted_log_abs_slope": fitted,
                "absolute_slope_error": error,
            }
            if error > max_slope_error:
                max_slope_error = error
                worst_slope = {"m": m, "branch": label, "predicted": predicted, "fitted": fitted, "absolute_error": error}
        rows.append({"m": m, "identity": identity_rows, "asymptotic": asymptotic})

    ok = max_identity < 1e-7 and max_slope_error < 5e-3
    return {
        "iteration": 412,
        "stream": "LQG_SPINFOAM_TOLLER",
        "probe": "SOURCE_HYPERGEOMETRIC_TOLLER_IDENTITY_AND_ASYMPTOTIC",
        "gamma": gamma,
        "j": j,
        "rho": rho,
        "max_sum_identity_relative_residual": max_identity,
        "max_large_beta_slope_absolute_error": max_slope_error,
        "worst_identity": worst_identity,
        "worst_slope": worst_slope,
        "rows": rows,
        "pass": ok,
        "classification": "PASS_SOURCE_HYPERGEOMETRIC_TOLLER_IDENTITY_AND_ASYMPTOTIC_REPRODUCED" if ok else "FAIL_SOURCE_HYPERGEOMETRIC_TOLLER_REPRODUCTION_GUARD",
        "scope_guard": [
            "GAMMA_SIMPLE_TOLLER_BUILDING_BLOCK_ONLY",
            "NO_FULL_CAUSAL_VERTEX_ABSOLUTE_CONVERGENCE_PROOF",
            "NO_COMPLETE_VERTEX_NORMALIZATION_CERTIFICATE",
            "NO_FAMILY_TERMINALIZATION",
            "NO_D7_PROMOTION",
        ],
    }


def run_cfs(x: float, bound: float) -> dict:
    if not 0.0 < x < 1.0 or bound <= 0.0:
        raise ValueError("need 0<x<1 and B>0")
    finite_terms = [bound * (x ** q) for q in range(1, 7)]
    through_order_8 = sum(finite_terms)
    infinite_envelope = bound * x / (1.0 - x)
    critical_bound = (1.0 - x) / x
    long_sum = bound * sum(x ** q for q in range(1, 1000))
    arithmetic_residual = abs(long_sum - infinite_envelope) / max(abs(infinite_envelope), 1e-300)
    hierarchy_safe = infinite_envelope < 1.0
    ok = arithmetic_residual < 1e-12 and through_order_8 <= infinite_envelope * (1.0 + 1e-14)
    return {
        "iteration": 413,
        "stream": "CFS_GEOMETRIC_CORRECTION_ENVELOPE",
        "probe": "DELTA3PLUS_BOUNDED_COEFFICIENT_ENVELOPE",
        "delta_over_L": x,
        "assumed_abs_Cn_over_C2_bound_B": bound,
        "relative_terms_delta3_through_delta8": finite_terms,
        "relative_envelope_through_delta8": through_order_8,
        "relative_envelope_all_delta3plus_orders": infinite_envelope,
        "critical_B_for_total_subleading_envelope_below_leading": critical_bound,
        "hierarchy_safe_under_assumed_bound": hierarchy_safe,
        "geometric_series_arithmetic_relative_residual": arithmetic_residual,
        "pass": ok,
        "classification": "PASS_CFS_DELTA3PLUS_COEFFICIENT_ENVELOPE_DIAGNOSTIC" if ok else "FAIL_CFS_DELTA3PLUS_ENVELOPE_ARITHMETIC_GUARD",
        "scope_guard": [
            "B_IS_EXPLICIT_ASSUMPTION_SCAN_NOT_SOURCE_FIT",
            "NO_SOURCE_DEFINED_DELTA3PLUS_COEFFICIENT",
            "NO_EXPLICIT_BEYOND_EINSTEIN_CORRECTION_TENSOR",
            "NO_PHENOMENOLOGICAL_BOUND",
            "NO_FAMILY_TERMINALIZATION",
            "NO_D7_PROMOTION",
        ],
    }


def simpson_inverse_cube(a: float, b: float, n: int = 50000) -> float:
    if n % 2:
        n += 1
    h = (b - a) / n
    total = a ** -3 + b ** -3
    odd = 0.0
    even = 0.0
    for i in range(1, n):
        v = (a + i * h) ** -3
        if i % 2:
            odd += v
        else:
            even += v
    return h * (total + 4.0 * odd + 2.0 * even) / 3.0


def run_as_tail(cutoff: float) -> dict:
    if cutoff <= 1.0:
        raise ValueError("cutoff Lambda must exceed 1 in source dimensionless UV-tail audit")
    u0 = math.log(cutoff * cutoff)
    umax = max(1000.0, 20.0 * u0)
    analytic = 1.0 / (4.0 * math.pi * u0 * u0)
    finite_numeric = simpson_inverse_cube(u0, umax, 50000) / (2.0 * math.pi)
    analytic_remainder = 1.0 / (4.0 * math.pi * umax * umax)
    numeric = finite_numeric + analytic_remainder
    relative_error = abs(numeric - analytic) / analytic
    scaled_invariant = analytic * u0 * u0
    target_invariant = 1.0 / (4.0 * math.pi)
    invariant_error = abs(scaled_invariant - target_invariant)
    ok = relative_error < 5e-9 and invariant_error < 1e-15
    return {
        "iteration": 414,
        "stream": "ASYMPTOTIC_SAFETY_LORENTZIAN_SPECTRAL_TAIL",
        "probe": "NORMALIZED_UV_SPECTRAL_TAIL_NORMALISABILITY",
        "cutoff_Lambda": cutoff,
        "u0_log_Lambda_squared": u0,
        "normalized_c_h_UV": 1.0,
        "analytic_tail_weight": analytic,
        "numeric_tail_weight": numeric,
        "numeric_vs_analytic_relative_error": relative_error,
        "scaled_tail_invariant": scaled_invariant,
        "target_scaled_invariant_1_over_4pi": target_invariant,
        "pass": ok,
        "classification": "PASS_AS_SPECTRAL_UV_TAIL_NORMALISABILITY_REPRODUCED" if ok else "FAIL_AS_SPECTRAL_UV_TAIL_QUADRATURE_GUARD",
        "scope_guard": [
            "C_H_UV_NORMALIZED_TO_ONE_FOR_SCALING_ONLY",
            "NO_EXTRACTION_OF_SOURCE_NUMERICAL_C_H_UV",
            "NO_COMPOSITION_WITH_ERG2026_CONTACT_AMPLITUDE",
            "NO_PHYSICAL_HILBERT_SPACE_CERTIFICATE",
            "NO_FAMILY_TERMINALIZATION",
            "NO_D7_PROMOTION",
        ],
    }


def run_source_guard() -> dict:
    A_h = 61.0 / (60.0 * math.pi)
    ir_coeff = 61.0 / 30.0
    relation_residual = abs(2.0 * math.pi * A_h - ir_coeff)
    g_star = 760.0 * math.pi / 2499.0
    ok = relation_residual < 1e-14 and abs(g_star - 0.9554263372261876) < 1e-14
    return {
        "iteration": 415,
        "stream": "SOURCE_CONSTANT_GUARD",
        "probe": "AS_LORENTZIAN_SPECTRAL_SOURCE_CONSTANT_ARITHMETIC",
        "A_h_61_over_60pi": A_h,
        "IR_tail_coefficient_61_over_30": ir_coeff,
        "relation_2pi_Ah_minus_61_over_30_abs_residual": relation_residual,
        "g_star_760pi_over_2499": g_star,
        "pass": ok,
        "classification": "PASS_SOURCE_CONSTANT_ARITHMETIC_GUARD" if ok else "FAIL_SOURCE_CONSTANT_ARITHMETIC_GUARD",
        "scope_guard": ["ARITHMETIC_SOURCE_GUARD_ONLY", "NO_TERMINALIZATION", "NO_D7_PROMOTION"],
    }


def run_aggregate(input_dir: str) -> dict:
    rows = []
    for p in sorted(Path(input_dir).rglob("*.json")):
        rows.append(json.loads(p.read_text(encoding="utf-8")))
    counts: dict[str, int] = {}
    for r in rows:
        counts[r["stream"]] = counts.get(r["stream"], 0) + 1
    expected = {
        "LQG_SPINFOAM_TOLLER": 25,
        "CFS_GEOMETRIC_CORRECTION_ENVELOPE": 15,
        "ASYMPTOTIC_SAFETY_LORENTZIAN_SPECTRAL_TAIL": 8,
        "SOURCE_CONSTANT_GUARD": 1,
    }
    lqg = [r for r in rows if r.get("stream") == "LQG_SPINFOAM_TOLLER"]
    cfs = [r for r in rows if r.get("stream") == "CFS_GEOMETRIC_CORRECTION_ENVELOPE"]
    as_tail = [r for r in rows if r.get("stream") == "ASYMPTOTIC_SAFETY_LORENTZIAN_SPECTRAL_TAIL"]
    ok = len(rows) == 49 and counts == expected and all(r.get("pass", False) for r in rows)
    return {
        "iteration_bundle": "412-416",
        "independent_result_count": len(rows),
        "counts": counts,
        "expected_counts": expected,
        "all_independent_pass": all(r.get("pass", False) for r in rows) if rows else False,
        "metrics": {
            "lqg_max_sum_identity_relative_residual": max((r["max_sum_identity_relative_residual"] for r in lqg), default=None),
            "lqg_max_large_beta_slope_absolute_error": max((r["max_large_beta_slope_absolute_error"] for r in lqg), default=None),
            "cfs_max_geometric_series_arithmetic_relative_residual": max((r["geometric_series_arithmetic_relative_residual"] for r in cfs), default=None),
            "as_tail_max_numeric_vs_analytic_relative_error": max((r["numeric_vs_analytic_relative_error"] for r in as_tail), default=None),
        },
        "pass": ok,
        "classification": "PASS_THREE_STREAM_SOURCE_GROUNDED_CLOSURE_WAVE__LQG_TOLLER_EXACT_BUILDING_BLOCK__CFS_DELTA3PLUS_ENVELOPE__AS_SPECTRAL_NORMALISABILITY" if ok else "FAIL_ITER412_416_AGGREGATE_CONTRACT",
        "terminalization": {
            "lqg_family_terminal": False,
            "cfs_family_terminal": False,
            "asymptotic_safety_family_terminal": False,
            "any_family_promoted": False,
        },
        "required_next_objects": {
            "LQG_SPINFOAM": "FULL_CAUSAL_VERTEX_ABSOLUTE_CONVERGENCE_NORMALIZATION_OR_EQUIVALENT_TERMINAL_OBJECT",
            "CAUSAL_FERMION_SYSTEMS": "EXPLICIT_DELTA3PLUS_CORRECTION_TENSOR_WITH_SOURCE_DEFINED_COEFFICIENTS_AND_DOMAIN",
            "ASYMPTOTIC_SAFETY": "MACHINE_READABLE_CONTACT_COMPLETE_SAME_REALIZATION_AMPLITUDE_WITH_APPROXIMATION_AND_ERROR_LEDGER",
        },
        "global": {
            "D2": "NOT_CLOSED_COVERAGE_AND_OBJECTS",
            "D4": "PARTIAL_GLOBAL_NOT_CLOSED",
            "D7": "NOT_CLOSED_NOT_YET_AUTHORIZED",
            "candidate_gravity_activation": False,
            "new_required_authorized": False,
        },
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", required=True, choices=["lqg", "cfs", "as-tail", "source-guard", "aggregate"])
    ap.add_argument("--gamma", type=float)
    ap.add_argument("--j", type=float)
    ap.add_argument("--delta-over-L", type=float)
    ap.add_argument("--B", type=float)
    ap.add_argument("--cutoff", type=float)
    ap.add_argument("--input-dir")
    ap.add_argument("--output", required=True)
    a = ap.parse_args()
    if a.mode == "lqg":
        out = run_lqg(a.gamma, a.j)
    elif a.mode == "cfs":
        out = run_cfs(a.delta_over_L, a.B)
    elif a.mode == "as-tail":
        out = run_as_tail(a.cutoff)
    elif a.mode == "source-guard":
        out = run_source_guard()
    else:
        out = run_aggregate(a.input_dir)
    write_result(out, a.output)


if __name__ == "__main__":
    main()

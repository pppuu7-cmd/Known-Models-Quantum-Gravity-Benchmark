"""Semantic/fail-closed comparator for independent RQCP evidence recomputation.

Raw JSON byte identity is too strict for floating linear-algebra results across
BLAS/platform builds, but a scientific audit must not hide meaningful drift.
This comparator therefore:

* requires exact equality for structure, strings, booleans and integers;
* compares primary finite floating values with explicit abs/relative tolerances;
* gives derived error/bound/refinement ratios a separate tolerance because they
  divide small numerical differences and are not primary observables;
* independently freezes the headline physics quantities, gate booleans and the
  explicit algorithmic acceptance inequalities used by the external artifact;
* treats the known omega=0 geometry-derivative diagnostic separately because
  the external implementation subtracts two analytically identical expressions
  and divides round-off by 1e-30 at the exact continuum point.

The special case is reported as a numerical diagnostic defect, never silently
normalised away. Any primary mismatch or failed declared threshold is a hard
failure.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any


SPECIAL_PATH = "direct_continuum_reference.geometry_derivative_remainder"
HEADLINE_PATHS = (
    "direct_continuum_reference.Newton_response_G",
    "direct_continuum_reference.dimensionless_gravity_number_G_gap2",
    "direct_continuum_reference.mass_gap",
    "direct_continuum_reference.connected_static_four_response",
    "direct_continuum_reference.mixed_geometry_matter_response",
    "direct_continuum_reference.final_scale_factor",
    "one_error_scale.fitted_power_law_order",
)
EXACT_GATE_PATHS = (
    "all_band_nonperturbative_QG_completion",
    "canonical_NP1_NP6_status",
    "domain_qualified_mainstream_comparison_benchmark_passed",
    "domain_qualified_mainstream_comparison_candidate",
    "closure_gates.U1_same_UCP_refinement_family",
    "closure_gates.U2_interacting_Lorentzian_fixed_physical_band",
    "closure_gates.U3_continuum_relational_Diff_Ward_algebra",
    "closure_gates.U4_positive_two_regulator_fixed_band_G_eff",
    "closure_gates.U5_quantum_matter_semiclassical_geometry_backreaction",
    "closure_gates.U6_one_epsilon_N_to_zero",
    "closure_gates.U7_nonfitted_dimensionless_gravity_observable",
)


def get_path(data: dict[str, Any], dotted: str) -> Any:
    cur: Any = data
    for part in dotted.split("."):
        if not isinstance(cur, dict) or part not in cur:
            raise KeyError(dotted)
        cur = cur[part]
    return cur


def flatten(value: Any, prefix: str = "") -> dict[str, Any]:
    out: dict[str, Any] = {}
    if isinstance(value, dict):
        for key in sorted(value):
            path = f"{prefix}.{key}" if prefix else key
            out.update(flatten(value[key], path))
    elif isinstance(value, list):
        for index, item in enumerate(value):
            path = f"{prefix}[{index}]"
            out.update(flatten(item, path))
    else:
        out[prefix] = value
    return out


def is_float_number(value: Any) -> bool:
    return isinstance(value, float) and not isinstance(value, bool)


def is_derived_ratio_path(path: str) -> bool:
    leaf = path.rsplit(".", 1)[-1]
    return (
        "analytic_bound_ratios." in path
        or leaf.endswith("_bound_ratio")
        or leaf.endswith("_refinement_ratio")
    )


def threshold_checks(data: dict[str, Any]) -> dict[str, dict[str, Any]]:
    """Mirror explicit algorithmic assertions visible in the external checker."""
    checks: dict[str, dict[str, Any]] = {}
    specs = (
        ("mixed_response_refinement_difference", "algorithmic_discretization_control.mixed_response_refinement_difference", "lt", 2.0e-9),
        ("backreaction_fine_difference", "algorithmic_discretization_control.backreaction_fine_difference", "lt", 1.0e-9),
        ("backreaction_refinement_ratio", "algorithmic_discretization_control.backreaction_refinement_ratio", "gt", 4.0),
    )
    for name, path, op, threshold in specs:
        value = float(get_path(data, path))
        passed = value < threshold if op == "lt" else value > threshold
        checks[name] = {
            "path": path,
            "value": value,
            "operator": op,
            "threshold": threshold,
            "pass": passed,
        }
    return checks


def compare(
    baseline: dict[str, Any],
    candidate: dict[str, Any],
    *,
    rel_tol: float,
    abs_tol: float,
    diagnostic_rel_tol: float,
    diagnostic_abs_tol: float,
    headline_rel_tol: float,
    headline_abs_tol: float,
) -> dict[str, Any]:
    base_flat = flatten(baseline)
    cand_flat = flatten(candidate)
    base_keys = set(base_flat)
    cand_keys = set(cand_flat)
    missing = sorted(base_keys - cand_keys)
    extra = sorted(cand_keys - base_keys)
    hard_mismatches: list[dict[str, Any]] = []
    float_drifts: list[dict[str, Any]] = []
    diagnostic_ratio_drifts: list[dict[str, Any]] = []

    for path in sorted(base_keys & cand_keys):
        a = base_flat[path]
        b = cand_flat[path]
        if path == SPECIAL_PATH:
            continue
        if is_float_number(a) or is_float_number(b):
            if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
                hard_mismatches.append({"path": path, "baseline": a, "candidate": b, "reason": "numeric_type_mismatch"})
                continue
            af = float(a)
            bf = float(b)
            if not (math.isfinite(af) and math.isfinite(bf)):
                if af != bf:
                    hard_mismatches.append({"path": path, "baseline": af, "candidate": bf, "reason": "nonfinite_mismatch"})
                continue
            delta = abs(bf - af)
            scale = max(abs(af), abs(bf), 1.0)
            rel = delta / scale
            derived_ratio = is_derived_ratio_path(path)
            this_rel_tol = diagnostic_rel_tol if derived_ratio else rel_tol
            this_abs_tol = diagnostic_abs_tol if derived_ratio else abs_tol
            record = {"path": path, "baseline": af, "candidate": bf, "abs_delta": delta, "scaled_rel_delta": rel}
            if not math.isclose(af, bf, rel_tol=this_rel_tol, abs_tol=this_abs_tol):
                hard_mismatches.append({**record, "reason": "derived_ratio_outside_tolerance" if derived_ratio else "float_outside_tolerance"})
            elif delta != 0.0:
                if derived_ratio:
                    diagnostic_ratio_drifts.append(record)
                else:
                    float_drifts.append(record)
        else:
            if type(a) is not type(b) or a != b:
                hard_mismatches.append({"path": path, "baseline": a, "candidate": b, "reason": "exact_mismatch"})

    headline = {}
    for path in HEADLINE_PATHS:
        a = float(get_path(baseline, path))
        b = float(get_path(candidate, path))
        ok = math.isclose(a, b, rel_tol=headline_rel_tol, abs_tol=headline_abs_tol)
        headline[path] = {"baseline": a, "candidate": b, "pass": ok, "abs_delta": abs(b - a)}
        if not ok:
            hard_mismatches.append({"path": path, "baseline": a, "candidate": b, "reason": "headline_outside_tolerance"})

    exact_gates = {}
    for path in EXACT_GATE_PATHS:
        a = get_path(baseline, path)
        b = get_path(candidate, path)
        ok = type(a) is type(b) and a == b
        exact_gates[path] = {"baseline": a, "candidate": b, "pass": ok}
        if not ok:
            hard_mismatches.append({"path": path, "baseline": a, "candidate": b, "reason": "gate_mismatch"})

    baseline_thresholds = threshold_checks(baseline)
    candidate_thresholds = threshold_checks(candidate)
    for name, result in candidate_thresholds.items():
        if not result["pass"]:
            hard_mismatches.append({
                "path": result["path"],
                "candidate": result["value"],
                "threshold": result["threshold"],
                "operator": result["operator"],
                "reason": "declared_algorithmic_threshold_failed",
            })

    omega = float(get_path(candidate, "direct_continuum_reference.declared_frequency"))
    special_baseline = float(get_path(baseline, SPECIAL_PATH))
    special_candidate = float(get_path(candidate, SPECIAL_PATH))
    bound = float(get_path(candidate, "direct_continuum_reference.geometry_derivative_remainder_bound"))
    ratio = float(get_path(candidate, "direct_continuum_reference.geometry_derivative_bound_ratio"))
    special_is_known_zero_frequency_artifact = (
        omega == 0.0
        and bound == 0.0
        and ratio == 0.0
        and special_baseline == 0.0
        and special_candidate != 0.0
    )
    if special_candidate != special_baseline and not special_is_known_zero_frequency_artifact:
        hard_mismatches.append({
            "path": SPECIAL_PATH,
            "baseline": special_baseline,
            "candidate": special_candidate,
            "reason": "unexpected_special_case_mismatch",
        })

    status = "FAIL"
    if not missing and not extra and not hard_mismatches:
        status = (
            "PASS_CORE_WITH_ZERO_FREQUENCY_DIAGNOSTIC_DEFECT"
            if special_is_known_zero_frequency_artifact
            else "PASS"
        )

    return {
        "schema_version": "1.1",
        "status": status,
        "structure": {"missing_paths": missing, "extra_paths": extra},
        "tolerances": {
            "primary_relative": rel_tol,
            "primary_absolute": abs_tol,
            "derived_ratio_relative": diagnostic_rel_tol,
            "derived_ratio_absolute": diagnostic_abs_tol,
            "headline_relative": headline_rel_tol,
            "headline_absolute": headline_abs_tol,
        },
        "headline_quantities": headline,
        "exact_gates": exact_gates,
        "declared_algorithmic_thresholds": {
            "baseline": baseline_thresholds,
            "candidate": candidate_thresholds,
        },
        "zero_frequency_geometry_derivative_diagnostic": {
            "path": SPECIAL_PATH,
            "declared_frequency": omega,
            "baseline": special_baseline,
            "candidate": special_candidate,
            "analytic_remainder_at_exact_zero_frequency": 0.0,
            "reported_bound": bound,
            "reported_ratio": ratio,
            "classified_as_roundoff_amplification_defect": special_is_known_zero_frequency_artifact,
            "explanation": "At omega=0 exact_kernel and static are algebraically identical; the external code evaluates them separately and divides their floating subtraction residual by 1e-30.",
        },
        "hard_mismatches": hard_mismatches,
        "within_tolerance_primary_float_drift_count": len(float_drifts),
        "within_tolerance_derived_ratio_drift_count": len(diagnostic_ratio_drifts),
        "largest_within_tolerance_primary_drifts": sorted(float_drifts, key=lambda x: x["abs_delta"], reverse=True)[:20],
        "largest_within_tolerance_derived_ratio_drifts": sorted(diagnostic_ratio_drifts, key=lambda x: x["scaled_rel_delta"], reverse=True)[:20],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--baseline", required=True)
    parser.add_argument("--candidate", required=True)
    parser.add_argument("--report", required=True)
    parser.add_argument("--rel-tol", type=float, default=1.0e-9)
    parser.add_argument("--abs-tol", type=float, default=1.0e-10)
    parser.add_argument("--diagnostic-rel-tol", type=float, default=1.0e-5)
    parser.add_argument("--diagnostic-abs-tol", type=float, default=1.0e-8)
    parser.add_argument("--headline-rel-tol", type=float, default=1.0e-11)
    parser.add_argument("--headline-abs-tol", type=float, default=1.0e-11)
    args = parser.parse_args()

    baseline = json.loads(Path(args.baseline).read_text(encoding="utf-8"))
    candidate = json.loads(Path(args.candidate).read_text(encoding="utf-8"))
    report = compare(
        baseline,
        candidate,
        rel_tol=args.rel_tol,
        abs_tol=args.abs_tol,
        diagnostic_rel_tol=args.diagnostic_rel_tol,
        diagnostic_abs_tol=args.diagnostic_abs_tol,
        headline_rel_tol=args.headline_rel_tol,
        headline_abs_tol=args.headline_abs_tol,
    )
    out = Path(args.report)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"RQCP semantic reproducibility status={report['status']}")
    print(
        "zero_frequency_candidate_remainder="
        f"{report['zero_frequency_geometry_derivative_diagnostic']['candidate']!r}"
    )
    print(f"hard_mismatches={len(report['hard_mismatches'])}")
    print(f"primary_float_drifts={report['within_tolerance_primary_float_drift_count']}")
    print(f"derived_ratio_drifts={report['within_tolerance_derived_ratio_drift_count']}")
    return 0 if report["status"].startswith("PASS") else 1


if __name__ == "__main__":
    raise SystemExit(main())

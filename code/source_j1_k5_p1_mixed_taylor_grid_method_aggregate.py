#!/usr/bin/env python3
"""Aggregate the prospectively frozen LOW/HIGH mixed-Taylor method lanes."""
from __future__ import annotations
import argparse, json
from pathlib import Path
import mpmath as mp

FORESTS = ("SINGLE15", "NESTED27", "DISJOINT22", "CHAIN2715")


def nerr(a, b):
    a, b = mp.mpf(a), mp.mpf(b)
    return abs(a-b) / max(mp.mpf(1), abs(a), abs(b))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--low", required=True)
    ap.add_argument("--high", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    mp.mp.dps = 1800
    low = json.loads(Path(a.low).read_text())
    high = json.loads(Path(a.high).read_text())

    invalid_keys = (
        "operator_digest_lock",
        "all_forest_structure_controls",
        "nonlaminar_pair_rejected",
        "historical_order9_rejected_for_single15",
        "historical_parent_raw_lock",
        "exact_polynomial_fixtures",
        "degree_r_plus_one_step_sensitivity_detected",
    )
    precision_keys = (
        "tensor_reduction_order_and_direct_sum",
        "all_actual_values_finite",
        "cancellation_margin_at_least_180_digits",
    )
    invalid_controls = all(bool(x["controls"].get(k, False)) for x in (low, high) for k in invalid_keys)
    lane_precision = all(bool(x["controls"].get(k, False)) for x in (low, high) for k in precision_keys)

    same_step = {}
    refine = {}
    for name in FORESTS:
        l = low["scales"]["100"]["actual"][name]["projected"]
        h100 = high["scales"]["100"]["actual"][name]["projected"]
        h140 = high["scales"]["140"]["actual"][name]["projected"]
        same_step[name] = mp.nstr(nerr(l, h100), 100)
        refine[name] = mp.nstr(nerr(h100, h140), 100)

    same_step_ok = all(mp.mpf(v) <= mp.mpf("1e-70") for v in same_step.values())
    refinement_ok = all(mp.mpf(v) <= mp.mpf("1e-18") for v in refine.values())

    if not invalid_controls:
        classification = "INVALID_IMPLEMENTATION"
    elif not (lane_precision and same_step_ok and refinement_ok):
        classification = "P1_MIXED_TAYLOR_GRID_METHOD_PRECISION_BLOCKED"
    else:
        classification = "P1_MIXED_TAYLOR_GRID_METHOD_CONFIRMED_SCOPED"

    out = {
        "gate": "SOURCE_J1_K5_P1_MIXED_TAYLOR_GRID_METHOD_PILOT",
        "classification": classification,
        "invalid_controls_pass": invalid_controls,
        "lane_precision_controls_pass": lane_precision,
        "same_step_precision_replay_errors": same_step,
        "same_step_precision_replay_pass": same_step_ok,
        "high_step_refinement_errors": refine,
        "high_step_refinement_pass": refinement_ok,
        "low_lane_classification": low["classification"],
        "high_lane_classification": high["classification"],
        "claim_ceiling": "Mixed Taylor numerical method validation only; no forest-subtracted stabilization/divergence, Eq. (4), model/family, D7, selector, or Candidate Gravity conclusion.",
    }
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(json.dumps(out, sort_keys=True))

if __name__ == "__main__":
    main()

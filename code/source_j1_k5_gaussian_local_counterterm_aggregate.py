#!/usr/bin/env python3
"""Aggregate frozen P1-P3 lanes for the Gaussian local-counterterm gate."""

from __future__ import annotations

import argparse
import glob
import json
from pathlib import Path

import mpmath as mp

mp.mp.dps = 180

PATHS = ("P1", "P2", "P3")
A_TEST = ("0.55", "0.95", "1.35", "1.75", "1.95")
K_USED = (5, 6, 7, 8)


def classify_sequence(residuals):
    r = [mp.mpf(v) for v in residuals]
    d56 = abs(r[1] - r[0])
    d67 = abs(r[2] - r[1])
    d78 = abs(r[3] - r[2])
    rel78 = d78 / max(mp.mpf(1), abs(r[3]), abs(r[2]))
    finite = d56 > d67 > d78 and rel78 <= mp.mpf("1e-8")
    abs_tail = [abs(r[1]), abs(r[2]), abs(r[3])]
    divergent = False
    if all(v > 0 for v in abs_tail) and abs_tail[0] < abs_tail[1] < abs_tail[2]:
        g1 = mp.log(abs_tail[1] / abs_tail[0], 2)
        g2 = mp.log(abs_tail[2] / abs_tail[1], 2)
        divergent = (g1 + g2) / 2 >= 2
    if finite:
        return "FINITE_COMPATIBLE"
    if divergent:
        return "DIVERGENT_AFTER_LOCAL_SUBTRACTION"
    return "INCONCLUSIVE"


def alpha_global_status(lanes, alpha):
    statuses = [lanes[p]["heldout_path_classification"][alpha]["status"] for p in PATHS]
    if not all(s == "FINITE_COMPATIBLE" for s in statuses):
        return None, None
    finals = [mp.mpf(lanes[p]["heldout_values"][alpha]["8"]["residual"]) for p in PATHS]
    scale = max(mp.mpf(1), *(abs(v) for v in finals))
    spread = max(abs(finals[i] - finals[j]) for i in range(3) for j in range(i + 1, 3)) / scale
    return ("PATH_INDEPENDENT_FINITE" if spread <= mp.mpf("1e-6") else "FINITE_PATH_DEPENDENT"), spread


def synthetic_path_dependence_control():
    # Three finite-compatible sequences converging to deliberately separated limits.
    seqs = {
        "P1": [mp.mpf("1.00001"), mp.mpf("1.0000001"), mp.mpf("1.000000001"), mp.mpf("1.00000000001")],
        "P2": [mp.mpf("2.00001"), mp.mpf("2.0000001"), mp.mpf("2.000000001"), mp.mpf("2.00000000001")],
        "P3": [mp.mpf("3.00001"), mp.mpf("3.0000001"), mp.mpf("3.000000001"), mp.mpf("3.00000000001")],
    }
    if not all(classify_sequence(v) == "FINITE_COMPATIBLE" for v in seqs.values()):
        return False
    finals = [seqs[p][-1] for p in PATHS]
    scale = max(mp.mpf(1), *(abs(v) for v in finals))
    spread = max(abs(finals[i] - finals[j]) for i in range(3) for j in range(i + 1, 3)) / scale
    return spread > mp.mpf("1e-6")


def load_lanes(root):
    lanes = {}
    for filename in glob.glob(str(Path(root) / "**" / "*.json"), recursive=True):
        try:
            data = json.loads(Path(filename).read_text())
        except Exception:
            continue
        p = data.get("path")
        if p in PATHS and data.get("gate") == "SOURCE_J1_K5_GAUSSIAN_LOCAL_COUNTERTERM_RENORMALIZATION_GATE":
            if p in lanes:
                raise RuntimeError(f"duplicate lane for {p}: {filename}")
            lanes[p] = data
    return lanes


def aggregate(root):
    lanes = load_lanes(root)
    complete = set(lanes) == set(PATHS)
    controls = {
        "all_three_lanes_present": complete,
        "all_lane_controls_pass": complete and all(lanes[p].get("controls_pass") is True for p in PATHS),
        "synthetic_path_dependence_detected": synthetic_path_dependence_control(),
        "p0_absent": complete and all(lanes[p].get("path") != "P0" for p in PATHS),
    }
    controls_pass = all(controls.values())

    alpha_results = {}
    any_divergent = False
    all_finite = complete
    for alpha in A_TEST:
        if not complete:
            alpha_results[alpha] = {"status": "INCOMPLETE", "spread": None}
            all_finite = False
            continue
        path_statuses = {p: lanes[p]["heldout_path_classification"][alpha]["status"] for p in PATHS}
        any_divergent = any_divergent or any(s == "DIVERGENT_AFTER_LOCAL_SUBTRACTION" for s in path_statuses.values())
        finite_here = all(s == "FINITE_COMPATIBLE" for s in path_statuses.values())
        all_finite = all_finite and finite_here
        global_status, spread = alpha_global_status(lanes, alpha) if finite_here else (None, None)
        alpha_results[alpha] = {
            "path_statuses": path_statuses,
            "status": global_status if global_status is not None else ("DIVERGENT_PRESENT" if any(s == "DIVERGENT_AFTER_LOCAL_SUBTRACTION" for s in path_statuses.values()) else "INCONCLUSIVE"),
            "spread": None if spread is None else mp.nstr(spread, 50),
            "final_residuals": {p: lanes[p]["heldout_values"][alpha]["8"]["residual"] for p in PATHS},
        }

    if not controls_pass:
        classification = "INVALID_IMPLEMENTATION"
    elif any_divergent:
        classification = "AUX_GAUSSIAN_LOCAL_COUNTERTERM_ANSATZ_INSUFFICIENT_SCOPED"
    elif all_finite and all(v["status"] == "PATH_INDEPENDENT_FINITE" for v in alpha_results.values()):
        classification = "AUX_GAUSSIAN_LOCAL_RENORMALIZED_EXTENSION_COMPATIBLE_SCOPED"
    elif all_finite and any(v["status"] == "FINITE_PATH_DEPENDENT" for v in alpha_results.values()):
        classification = "AUX_GAUSSIAN_LOCAL_RENORMALIZED_PATH_DEPENDENCE_WITNESS_SCOPED"
    else:
        classification = "AUX_GAUSSIAN_LOCAL_RENORMALIZATION_INCONCLUSIVE"

    return {
        "gate": "SOURCE_J1_K5_GAUSSIAN_LOCAL_COUNTERTERM_RENORMALIZATION_GATE",
        "classification": classification,
        "controls": controls,
        "controls_pass": controls_pass,
        "observed_paths": sorted(lanes),
        "alpha_results": alpha_results,
        "lane_classifications": {p: lanes[p]["classification"] for p in sorted(lanes)},
        "finite_ambiguity_dimension_before_renormalization_conditions": 14,
        "claim_ceiling": "Auxiliary scalar Gaussian aligned-K5 local-counterterm diagnostic only; insufficient rejects only the frozen order<=26 radial-test local ansatz, compatible is KMQGB-derived extension evidence only; neither is source-authorized Eq4 science or D7 closure.",
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    result = aggregate(args.root)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

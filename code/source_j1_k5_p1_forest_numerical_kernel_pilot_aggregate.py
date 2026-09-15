#!/usr/bin/env python3
"""Aggregate/cross-precision verifier for the P1 forest numerical-kernel pilot."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import mpmath as mp

CROSS_TOL = mp.mpf("1e-110")
FIELDS = ("raw", "f0", "f1", "f2", "t2", "r2")
REP_LABELS = ("01", "12")


def relative_or_absolute_error(a, b):
    return abs(a - b) / max(mp.mpf(1), abs(a), abs(b))


def index_records(data, k):
    records = data["k5_records"] if k == 5 else data["k6_representative_records"]
    return {r["subset"]: r for r in records}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    mp.mp.dps = 320

    files = sorted(Path(args.root).glob("**/source_j1_k5_p1_forest_numerical_kernel_pilot.json"))
    if len(files) != 2:
        raise SystemExit(f"expected exactly 2 lane JSON files, got {len(files)}")
    lanes = [json.loads(p.read_text()) for p in files]
    by_dps = {int(d["precision_decimal_digits"]): d for d in lanes}
    if set(by_dps) != {180, 260}:
        raise SystemExit(f"unexpected dps set: {set(by_dps)}")

    low = by_dps[180]
    high = by_dps[260]
    lane_valid = all(d.get("classification") == "P1_FOREST_NUMERICAL_KERNEL_LANE_VALID" and d.get("controls_pass") for d in lanes)
    object_lock = all(d.get("alpha") == "0.55" and tuple(d.get("p1_exponents", ())) == (1,1,1,1,2,2,2,2,2,2) for d in lanes)

    comparisons = []
    max_error = mp.mpf(0)
    for k in (5, 6):
        ilow = index_records(low, k)
        ihigh = index_records(high, k)
        for label in REP_LABELS:
            if label not in ilow or label not in ihigh:
                raise SystemExit(f"missing representative {label} at k={k}")
            for field in FIELDS:
                a = mp.mpf(ilow[label][field])
                b = mp.mpf(ihigh[label][field])
                err = relative_or_absolute_error(a, b)
                max_error = max(max_error, err)
                comparisons.append({
                    "k": k,
                    "subset": label,
                    "field": field,
                    "relative_or_absolute_error": mp.nstr(err, 100),
                })

    cross_precision_pass = max_error <= mp.mpf("1e-110")
    controls = {
        "both_lanes_valid": lane_valid,
        "object_lock": object_lock,
        "cross_precision_pass": cross_precision_pass,
    }
    controls_pass = all(controls.values())
    if not lane_valid or not object_lock:
        classification = "INVALID_IMPLEMENTATION"
    elif not cross_precision_pass:
        classification = "P1_FOREST_NUMERICAL_KERNEL_PRECISION_BLOCKED"
    else:
        classification = "P1_FOREST_NUMERICAL_KERNEL_CONFIRMED_SCOPED"

    out = {
        "classification": classification,
        "controls_pass": controls_pass,
        "controls": controls,
        "lane_precisions": sorted(by_dps),
        "max_cross_precision_relative_or_absolute_error": mp.nstr(max_error, 100),
        "cross_precision_tolerance": "1e-110",
        "comparisons": comparisons,
        "claim_ceiling": "Numerical-kernel validation only; no forest-subtracted convergence/divergence or physical conclusion.",
    }
    Path(args.out).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(json.dumps({k: v for k, v in out.items() if k != "comparisons"}, sort_keys=True))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

INVALID = "ITER504P_POINT_GRID_DRIFT_INVALID"
TERMINAL = {
    "ITER504P_POINT_GRID_DRIFT_WITHIN_FROZEN_TOLERANCE_SCOPED",
    "ITER504P_POINT_GRID_DRIFT_VIOLATION_SCOPED",
}


def load_one(root: str):
    files = sorted(Path(root).rglob("*.json"))
    if len(files) != 1:
        raise SystemExit(f"expected exactly one json under {root}, got {len(files)}")
    raw = files[0].read_bytes()
    return json.loads(raw), hashlib.sha256(raw).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--decimal", required=True)
    ap.add_argument("--float", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    d, dsha = load_one(args.decimal)
    f, fsha = load_one(args.float)

    core_keys = [
        "gate", "classification", "preregistration_commit", "upstream_iter504_run_id",
        "upstream_iter504_head", "threshold", "decisive_lanes", "known_control_lane",
        "known_control_is_decisive", "decisive_lane_count", "expected_records_per_lane",
        "expected_decisive_record_count", "decisive_record_count", "decisive_structure_ok",
        "violation_count", "max_drift_locator", "max_drift_within_threshold",
        "known_control_structure_ok", "known_control_record_count",
        "known_control_violation_count", "known_control_max_locator",
        "source_json_hashes", "known_control_json_sha256", "claim_ceiling",
        "scientific_payload_sha256",
    ]
    methods_ok = d.get("method") == "decimal" and f.get("method") == "float"
    scientific_agreement = methods_ok and all(d.get(k) == f.get(k) for k in core_keys)
    cls = d.get("classification") if scientific_agreement and d.get("classification") in TERMINAL else INVALID

    numeric_crosscheck = {
        "same_max_locator": d.get("max_drift_locator") == f.get("max_drift_locator"),
        "same_violation_count": d.get("violation_count") == f.get("violation_count"),
        "decimal_max_drift": d.get("max_drift"),
        "float_max_drift": f.get("max_drift"),
        "decimal_control_max_drift": d.get("known_control_max_drift"),
        "float_control_max_drift": f.get("known_control_max_drift"),
    }
    if not all([numeric_crosscheck["same_max_locator"], numeric_crosscheck["same_violation_count"]]):
        cls = INVALID

    out = {
        "gate": d.get("gate"),
        "classification": cls,
        "independent_methods_agree": scientific_agreement,
        "decimal_json_sha256": dsha,
        "float_json_sha256": fsha,
        "scientific_payload_sha256": d.get("scientific_payload_sha256") if scientific_agreement else None,
        "decisive_record_count": d.get("decisive_record_count"),
        "violation_count": d.get("violation_count"),
        "max_drift_locator": d.get("max_drift_locator"),
        "max_drift": d.get("max_drift"),
        "threshold": d.get("threshold"),
        "known_control_is_decisive": False,
        "known_control_max_drift": d.get("known_control_max_drift"),
        "numeric_crosscheck": numeric_crosscheck,
        "claim_ceiling": d.get("claim_ceiling"),
    }
    payload = json.dumps(out, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    out["aggregate_sha256"] = hashlib.sha256(payload).hexdigest()

    p = Path(args.out)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(out, indent=2, sort_keys=True, ensure_ascii=False) + "\n")
    print(json.dumps(out, indent=2, sort_keys=True, ensure_ascii=False))
    return 0 if cls != INVALID else 2


if __name__ == "__main__":
    raise SystemExit(main())

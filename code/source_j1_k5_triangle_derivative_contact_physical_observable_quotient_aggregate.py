#!/usr/bin/env python3
"""Aggregate exact independent lanes for the physical-observable quotient gate."""
from __future__ import annotations
import argparse, json
from pathlib import Path

EXPECTED = {
    "PHYSICAL_OBSERVABLE_QUOTIENT_ZERO_ACTION_COMPLETE_SCOPED",
    "PHYSICAL_OBSERVABLE_FINITE_FREEDOM_DISTINGUISHABLE_SCOPED",
    "PHYSICAL_OBSERVABLE_QUOTIENT_PARTIAL_SCOPED",
    "PHYSICAL_OBSERVABLE_QUOTIENT_MAP_BLOCKED_SCOPED",
    "INVALID_IMPLEMENTATION",
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lane311", required=True)
    ap.add_argument("--lane313", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    a = json.loads(Path(args.lane311).read_text())
    b = json.loads(Path(args.lane313).read_text())

    same_decision = a.get("decision_sha256") == b.get("decision_sha256")
    controls = bool(a.get("controls_pass")) and bool(b.get("controls_pass"))
    class_ok = a.get("classification") in EXPECTED and b.get("classification") in EXPECTED
    if not (same_decision and controls and class_ok):
        classification = "INVALID_IMPLEMENTATION"
    elif a["classification"] != b["classification"]:
        classification = "INVALID_IMPLEMENTATION"
    else:
        classification = a["classification"]

    out = {
        "gate": "SOURCE_J1_K5_TRIANGLE_DERIVATIVE_CONTACT_PHYSICAL_OBSERVABLE_QUOTIENT_GATE",
        "classification": classification,
        "lane_decision_agreement": same_decision,
        "lane_controls_pass": controls,
        "lane_classification_agreement": a.get("classification") == b.get("classification"),
        "decision_sha256": a.get("decision_sha256") if same_decision else None,
        "map_present": a.get("map_present") if same_decision else None,
        "observable_completeness_authority": a.get("observable_completeness_authority") if same_decision else None,
        "nullspace_action_rank": a.get("nullspace_action_rank") if same_decision else None,
        "v8_basis_count": a.get("v8_basis_count") if same_decision else None,
        "v8_affine_nullity": a.get("v8_affine_nullity") if same_decision else None,
        "claim_ceiling": a.get("claim_ceiling") if same_decision else "INVALID: lane decision mismatch",
    }
    p = Path(args.out)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(json.dumps(out, sort_keys=True))

if __name__ == "__main__":
    main()

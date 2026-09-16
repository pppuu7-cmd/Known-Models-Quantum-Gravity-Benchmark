#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

INVALID = "ITER504Q_ADAPTIVE_SUBBOX_DIAGNOSTIC_INVALID"
TERMINAL = {
    "ITER504Q_ADAPTIVE_SUBBOX_DIAGNOSTIC_NARROWED_WITHIN_TOLERANCE_SCOPED",
    "ITER504Q_ADAPTIVE_SUBBOX_DIAGNOSTIC_INCONCLUSIVE_SCOPED",
}


def load_one(root: str):
    files = sorted(Path(root).rglob("*.json"))
    if len(files) != 1:
        raise SystemExit(f"expected exactly one JSON under {root}, got {len(files)}")
    raw = files[0].read_bytes()
    return json.loads(raw), hashlib.sha256(raw).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--a", required=True)
    ap.add_argument("--b", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    a, asha = load_one(args.a)
    b, bsha = load_one(args.b)
    byte_identical = asha == bsha
    same_class = a.get("classification") == b.get("classification")
    cls = a.get("classification") if byte_identical and same_class and a.get("classification") in TERMINAL else INVALID

    out = {
        "gate": a.get("gate"),
        "classification": cls,
        "independent_environment_outputs_byte_identical": byte_identical,
        "lane_a_json_sha256": asha,
        "lane_b_json_sha256": bsha,
        "valid_cover": a.get("valid_cover"),
        "all_controls": a.get("all_controls"),
        "total_node_count": a.get("total_node_count"),
        "total_leaf_count": a.get("total_leaf_count"),
        "certified_leaf_count": a.get("certified_leaf_count"),
        "unresolved_leaf_count": a.get("unresolved_leaf_count"),
        "leaf_depth_histogram": a.get("leaf_depth_histogram"),
        "per_root_box_leaf_count": a.get("per_root_box_leaf_count"),
        "root_max_possible_counts": a.get("root_max_possible_counts"),
        "max_terminal_leaf_possible_count": a.get("max_terminal_leaf_possible_count"),
        "max_terminal_leaf_drift_upper": a.get("max_terminal_leaf_drift_upper"),
        "max_terminal_leaf_drift_witness": a.get("max_terminal_leaf_drift_witness"),
        "minimum_terminal_leaf_S_lower": a.get("minimum_terminal_leaf_S_lower"),
        "per_rho_worst": a.get("per_rho_worst"),
        "covers": a.get("covers"),
        "claim_ceiling": a.get("claim_ceiling"),
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

#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

PASS = "EQ4_TRIANGLE_WEDGE_GROUP_ARGUMENT_IDENTITY_PASS_SCOPED"
BLOCKED = "EQ4_TRIANGLE_WEDGE_GROUP_ARGUMENT_IDENTITY_BLOCKED_SCOPED"
INVALID = "INVALID_IMPLEMENTATION"


def load_one(root: Path, tag: str):
    fs = sorted(root.rglob("*.json"))
    if len(fs) != 1:
        raise SystemExit(f"{tag}: expected exactly one JSON, got {len(fs)}")
    return fs[0], json.loads(fs[0].read_text())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lane311", required=True)
    ap.add_argument("--lane313", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    p311, a = load_one(Path(args.lane311), "py311")
    p313, b = load_one(Path(args.lane313), "py313")
    keys = [
        "gate", "classification", "target_triangle", "provenance", "source_blob_checks",
        "pdf_hash_checks", "identity_controls", "literal_wedge_checks", "fixture_controls",
        "missing_identity_fields", "identity_ledger", "transverse_rank", "rank_policy",
        "downstream_authorized", "scope", "decision_sha256",
    ]
    identical = all(a.get(k) == b.get(k) for k in keys)
    lane_valid = a.get("classification") in (PASS, BLOCKED) and b.get("classification") in (PASS, BLOCKED)
    classification = a.get("classification") if identical and lane_valid else INVALID
    payload = {
        "gate": "SOURCE_J1_K5_EQ4_TRIANGLE_WEDGE_GROUP_ARGUMENT_IDENTITY_GATE",
        "classification": classification,
        "lanes_agree": identical,
        "lane_311_path": str(p311),
        "lane_313_path": str(p313),
        "lane_decision_sha256": [a.get("decision_sha256"), b.get("decision_sha256")],
        "target_triangle": a.get("target_triangle") if identical else None,
        "identity_ledger": a.get("identity_ledger") if identical else None,
        "missing_identity_fields": a.get("missing_identity_fields") if identical else None,
        "transverse_rank": None,
        "downstream_authorized": bool(identical and classification == PASS),
        "controls_all_pass": bool(identical and all(a.get("provenance", {}).values()) and all(a.get("identity_controls", {}).values()) and all(a.get("literal_wedge_checks", {}).values()) and all(a.get("fixture_controls", {}).values())),
        "scope": "source identity gate only; no rank/transversality inference",
    }
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["aggregate_decision_sha256"] = hashlib.sha256(raw).hexdigest()
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({k: v for k, v in payload.items() if k != "identity_ledger"}, sort_keys=True))
    return 0 if classification in (PASS, BLOCKED) and payload["controls_all_pass"] else 2


if __name__ == "__main__":
    raise SystemExit(main())

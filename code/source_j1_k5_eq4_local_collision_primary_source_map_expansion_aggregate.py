#!/usr/bin/env python3
"""Aggregate independent exact lanes for Eq4 local collision primary-source map expansion."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def canon_sha(obj):
    raw = json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--a", required=True)
    ap.add_argument("--b", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    a = json.loads(Path(args.a).read_text())
    b = json.loads(Path(args.b).read_text())

    keys = (
        "gate",
        "classification",
        "controls_pass",
        "new_actionable_fields",
        "remaining_missing_fields",
        "map_complete",
        "source_corpus",
        "source_pdf_sha256",
        "parent_classification",
        "nullspace_action_rank",
        "claim_ceiling",
        "decision_sha256",
    )
    same = all(a.get(k) == b.get(k) for k in keys)
    controls_pass = bool(a.get("controls_pass")) and bool(b.get("controls_pass"))
    classification = a.get("classification") if same and controls_pass else "INVALID_IMPLEMENTATION"
    out = {
        "gate": a.get("gate"),
        "classification": classification,
        "lanes_agree": same,
        "controls_pass": controls_pass,
        "lane_decision_sha256": a.get("decision_sha256") if same else None,
        "new_actionable_fields": a.get("new_actionable_fields") if same else None,
        "remaining_missing_fields": a.get("remaining_missing_fields") if same else None,
        "map_complete": a.get("map_complete") if same else False,
        "source_corpus": a.get("source_corpus") if same else None,
        "nullspace_action_rank": None,
        "claim_ceiling": a.get("claim_ceiling") if same else "Invalid aggregate; no scientific claim.",
    }
    out["aggregate_decision_sha256"] = canon_sha(out)
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(json.dumps(out, sort_keys=True))


if __name__ == "__main__":
    main()

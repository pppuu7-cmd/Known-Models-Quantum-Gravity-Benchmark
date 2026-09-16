#!/usr/bin/env python3
"""Aggregate independent V9 source-authority audit lanes."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

GATE = "SOURCE_J1_K5_TRIANGLE_DERIVATIVE_CONTACT_FINITE_RENORMALIZATION_AUTHORITY_GATE"
INVALID = "INVALID_IMPLEMENTATION"


def projection(x):
    y = dict(x)
    y.pop("runtime_python", None)
    y.pop("decision_sha256", None)
    return y


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--py311", required=True)
    ap.add_argument("--py313", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    a = json.loads(Path(args.py311).read_text())
    b = json.loads(Path(args.py313).read_text())
    pa, pb = projection(a), projection(b)
    lane_agreement = pa == pb
    lane_hashes_self_consistent = True
    for x in (a, b):
        canonical = json.dumps(projection(x), sort_keys=True, separators=(",", ":"))
        lane_hashes_self_consistent &= hashlib.sha256(canonical.encode()).hexdigest() == x.get("decision_sha256")

    gate_ok = a.get("gate") == GATE and b.get("gate") == GATE
    lane_controls = bool(a.get("controls_pass")) and bool(b.get("controls_pass"))
    same_class = a.get("classification") == b.get("classification")
    controls_pass = lane_agreement and lane_hashes_self_consistent and gate_ok and lane_controls and same_class
    classification = a.get("classification") if controls_pass else INVALID

    out = {
        "gate": GATE,
        "classification": classification,
        "controls_pass": controls_pass,
        "lane_decision_agreement": lane_agreement,
        "lane_hashes_self_consistent": lane_hashes_self_consistent,
        "lane_gate_identity": gate_ok,
        "lane_controls_pass": lane_controls,
        "lane_classification_agreement": same_class,
        "lane_runtime_python": [a.get("runtime_python"), b.get("runtime_python")],
        "authoritative_decision_projection": pa if lane_agreement else None,
        "claim_ceiling": (
            "Current durable structured-source authority audit for the local V8 delta-double-prime triangle only; "
            "no all-mollifier theorem, extension existence/nonexistence, full-K5/model/family/D7/global selector, or Candidate Gravity authority."
        ),
    }
    canonical = json.dumps(out, sort_keys=True, separators=(",", ":"))
    out["aggregate_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()
    p = Path(args.out)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "classification": classification,
        "controls_pass": controls_pass,
        "lane_decision_agreement": lane_agreement,
        "aggregate_sha256": out["aggregate_sha256"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()

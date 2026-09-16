#!/usr/bin/env python3
"""Aggregate independent Eq4 local collision test-jet map lanes."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

KEYS = (
    "gate","classification","controls_pass","required_map_fields","missing_required_fields",
    "map_complete","jet_order_7_constructed","v8_basis_count","v8_affine_nullity",
    "nullspace_action_rank","source_id","v10_open_finiteness_lock","claim_ceiling"
)

def projection(x):
    return {k:x.get(k) for k in KEYS}

def sha(x):
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":")).encode()).hexdigest()

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--a",required=True); ap.add_argument("--b",required=True); ap.add_argument("--out",required=True); args=ap.parse_args()
    a=json.loads(Path(args.a).read_text()); b=json.loads(Path(args.b).read_text())
    pa,pb=projection(a),projection(b)
    agree=pa==pb and a.get("decision_sha256")==b.get("decision_sha256")
    if not agree:
        cls="INVALID_IMPLEMENTATION"
    elif not (a.get("controls_pass") and b.get("controls_pass")):
        cls="INVALID_IMPLEMENTATION"
    else:
        cls=a["classification"]
    out={
        **pa,
        "classification":cls,
        "lane_decision_agreement":agree,
        "lane_decision_sha256":a.get("decision_sha256") if agree else None,
        "aggregate_decision_sha256":None,
        "runtime_python_versions":[a.get("runtime_python"),b.get("runtime_python")],
    }
    temp=dict(out); temp.pop("aggregate_decision_sha256",None); out["aggregate_decision_sha256"]=sha(temp)
    Path(args.out).parent.mkdir(parents=True,exist_ok=True); Path(args.out).write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print(json.dumps(out,sort_keys=True))
if __name__=="__main__": main()

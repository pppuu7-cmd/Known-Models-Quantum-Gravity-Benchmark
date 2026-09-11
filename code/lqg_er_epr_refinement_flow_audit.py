#!/usr/bin/env python3
import argparse, json
from pathlib import Path

FACTS = {
    "authority": {
        "arxiv_id": "2508.18324v2",
        "public_preprint": True,
        "peer_reviewed_located": False,
    },
    "refinement_flow": {
        "explicit_refinement_renormalization_claim": True,
        "conditional_regulator_independent_continuum_claim": True,
    },
    "equivalence": {
        "explicit_map_to_han_complete_stack": False,
        "continuous_gamma_stack_spin_transport_to_iter290": False,
    },
    "terminal_scope": {
        "normalized_same_realization_observable_comparator_error": False,
        "family_terminal": False,
        "d7_authorized": False,
    },
}

def guard(label):
    if label not in FACTS:
        raise SystemExit(f"unknown label {label}")
    data = {"label": label, **FACTS[label]}
    if label == "authority":
        data["pass"] = data["public_preprint"] and not data["peer_reviewed_located"]
    elif label == "refinement_flow":
        data["pass"] = data["explicit_refinement_renormalization_claim"] and data["conditional_regulator_independent_continuum_claim"]
    elif label == "equivalence":
        data["pass"] = (not data["explicit_map_to_han_complete_stack"] and not data["continuous_gamma_stack_spin_transport_to_iter290"])
    else:
        data["pass"] = (not data["normalized_same_realization_observable_comparator_error"] and not data["family_terminal"] and not data["d7_authorized"])
    return data

def main():
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)
    g = sub.add_parser("guard"); g.add_argument("--label", required=True); g.add_argument("--output", required=True)
    a = sub.add_parser("aggregate"); a.add_argument("--input-dir", required=True); a.add_argument("--output", required=True)
    args = p.parse_args()
    if args.cmd == "guard":
        out = guard(args.label)
    else:
        files = sorted(Path(args.input_dir).glob("*.json"))
        rows = [json.loads(f.read_text()) for f in files]
        labels = {r["label"] for r in rows}
        required = set(FACTS)
        if labels != required or not all(r.get("pass") for r in rows):
            raise SystemExit(f"fail-closed: labels={labels} required={required}")
        out = {
            "iteration": 292,
            "classification": "HIGH_VALUE_EXTERNAL_REFINEMENT_FLOW_AUTHORITY__NO_EXPLICIT_EQUIVALENCE_TO_THE_ACTIVE_COMPLETE_STACK_OR_CAUSAL_REGGE_CHAIN",
            "scoped_refinement_flow_positive": True,
            "explicit_active_stack_equivalence_ready": False,
            "complete_stack_same_realization_uv_ir_transport_ready": False,
            "family_terminal": False,
            "d7_authorized": False,
            "guards": rows,
        }
    path = Path(args.output); path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")

if __name__ == "__main__":
    main()

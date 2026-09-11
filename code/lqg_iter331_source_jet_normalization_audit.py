#!/usr/bin/env python3
import argparse, json
from pathlib import Path

SOURCES = {
    "bcg_causal_vertex_2601_23162": {
        "source": "Bianchi-Chen-Gamonal, arXiv:2601.23162",
        "facts": {
            "fixed_causal_vertex_formula": True,
            "individual_toller_iepsilon_definition": True,
            "common_multiwedge_iepsilon_limit": False,
            "partial_diagonal_extension_prescription": False,
            "forest_compatible_gluing_normalization": False,
            "k4_first_normal_jet_values_fixed": False,
            "k3_second_normal_jet_values_fixed": False,
        },
        "scope": "Eq.(3) defines individual Toller matrices; Eq.(4) forms the fixed causal vertex after those matrices are defined. No audited source passage fixes the singular-stratum normal jets required by Iter330.",
    },
    "bcg_toller_2604_24945": {
        "source": "Bianchi-Chen-Gamonal, arXiv:2604.24945",
        "facts": {
            "fixed_causal_vertex_formula": False,
            "individual_toller_iepsilon_definition": True,
            "common_multiwedge_iepsilon_limit": False,
            "partial_diagonal_extension_prescription": False,
            "forest_compatible_gluing_normalization": False,
            "k4_first_normal_jet_values_fixed": False,
            "k3_second_normal_jet_values_fixed": False,
        },
        "scope": "Audited Toller paper establishes the individual branch representation/analyticity for beta>0; it does not supply a forest-compatible extension law at the common beta=0 singular strata.",
    },
    "beltran_generalized_2603_22661_v2": {
        "source": "Beltran, arXiv:2603.22661v2",
        "facts": {
            "fixed_causal_vertex_formula": True,
            "individual_toller_iepsilon_definition": False,
            "common_multiwedge_iepsilon_limit": False,
            "partial_diagonal_extension_prescription": False,
            "forest_compatible_gluing_normalization": False,
            "k4_first_normal_jet_values_fixed": False,
            "k3_second_normal_jet_values_fixed": False,
        },
        "scope": "Generalizes causal structure/amplitudes to arbitrary 2-complexes, but the audited text does not provide the local distribution-extension or normal-jet normalization required by the explicit Iter330 K5 basis.",
    },
}

REQUIRED = [
    "partial_diagonal_extension_prescription",
    "forest_compatible_gluing_normalization",
    "k4_first_normal_jet_values_fixed",
    "k3_second_normal_jet_values_fixed",
]


def audit(name: str):
    row = SOURCES[name]
    facts = row["facts"]
    fixed = [k for k in REQUIRED if facts[k]]
    missing = [k for k in REQUIRED if not facts[k]]
    closes_iter330_gate = all(facts[k] for k in REQUIRED)
    return {
        "source_id": name,
        "source": row["source"],
        "facts": facts,
        "required_closure_fields": REQUIRED,
        "fixed_fields": fixed,
        "missing_fields": missing,
        "closes_iter330_gate": closes_iter330_gate,
        "scope": row["scope"],
        "classification": (
            "SOURCE_DEFINED_CLOSURE_FOUND" if closes_iter330_gate
            else "NOT_FOUND_IN_AUDITED_SOURCE"
        ),
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--source", choices=sorted(SOURCES), required=True)
    p.add_argument("--output", required=True)
    a = p.parse_args()
    result = audit(a.source)
    Path(a.output).parent.mkdir(parents=True, exist_ok=True)
    Path(a.output).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    # Fail closed against accidental over-promotion: current audited source rows
    # are expected NOT to close the Iter330 normalization gate.
    if result["closes_iter330_gate"]:
        raise SystemExit("Unexpected closure: manually re-audit source provenance before promotion")
    print(json.dumps(result, sort_keys=True))

if __name__ == "__main__":
    main()

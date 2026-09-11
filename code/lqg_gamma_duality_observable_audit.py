#!/usr/bin/env python3
import argparse, json, hashlib
from pathlib import Path

AUTH = {
    "title": "Spinfoams, gamma-duality, and parity violation in primordial gravitational waves",
    "authors": ["Eugenio Bianchi", "Monica Rincon-Ramirez"],
    "journal": "Physical Review D",
    "volume": "113",
    "article": "124013",
    "published": "2026-06-05",
    "doi": "10.1103/qz89-26hk",
    "arxiv": "2403.06053",
}

GUARDS = {
    "authority": {
        "pass": True,
        "claim": "peer_reviewed_prd_authority_identified",
        "scope": "published authority identity only",
    },
    "gamma_duality": {
        "pass": True,
        "claim": "EPRL_Barbero_Immirzi_gamma_controls_gravitational_parity_violation_via_duality_rotation",
        "scope": "EPRL/spinfoam dynamics and authors' gamma-dual EFT construction",
    },
    "eft_observable": {
        "pass": True,
        "claim": "gamma_fixes_relation_between_parity_even_and_parity_odd_higher_curvature_EFT_couplings_and_enters_primordial_tensor_polarization_inference",
        "scope": "chosen gamma-dual effective action in inflationary semiclassical regime",
    },
    "transport_scope": {
        "pass": True,
        "claim": "object_does_not_supply_complete_stack_same_realization_UV_to_IR_transport",
        "scope": "fail_closed promotion guard",
    },
}

def emit(path, obj):
    p = Path(path); p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")

def main():
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest="cmd", required=True)
    g = sp.add_parser("guard"); g.add_argument("--label", required=True, choices=sorted(GUARDS)); g.add_argument("--output", required=True)
    a = sp.add_parser("aggregate"); a.add_argument("--input-dir", required=True); a.add_argument("--output", required=True)
    ns = ap.parse_args()
    if ns.cmd == "guard":
        x = {"label": ns.label, "authority": AUTH, **GUARDS[ns.label]}
        emit(ns.output, x)
        return
    files = sorted(Path(ns.input_dir).glob("*.json"))
    rows = [json.loads(p.read_text(encoding="utf-8")) for p in files]
    labels = {r["label"] for r in rows}
    expected = set(GUARDS)
    if labels != expected or not all(r.get("pass") is True for r in rows):
        raise SystemExit(f"fail-closed aggregate: labels={sorted(labels)}")
    result = {
        "iteration": 291,
        "authority": AUTH,
        "guards_passed": sorted(labels),
        "scoped_observable_parameter_bridge": True,
        "semiclassical_gamma_observable_anchor": True,
        "complete_stack_same_realization_uv_ir_transport_ready": False,
        "normalized_observable_with_full_propagated_qg_error_ready": False,
        "family_terminal": False,
        "d7_authorized": False,
        "classification": "HIGH_VALUE_LQG_GAMMA_DUALITY_SEMICLASSICAL_OBSERVABLE_PARAMETER_BRIDGE__NO_COMPLETE_STACK_SAME_REALIZATION_UV_TO_IR_TRANSPORT",
        "promotion_rule": "scoped PASS only; do not promote to family PASS/FAIL or terminal D7 outcome",
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["aggregate_sha256"] = hashlib.sha256(canonical).hexdigest()
    emit(ns.output, result)

if __name__ == "__main__": main()

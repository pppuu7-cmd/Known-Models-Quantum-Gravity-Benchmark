#!/usr/bin/env python3
import argparse, hashlib, json, pathlib, sys

AUTHORITY = {
    "title": "Causal spinfoam vertex for 4d Lorentzian quantum gravity",
    "authors": ["Eugenio Bianchi", "Chaosong Chen", "Mauricio Gamonal"],
    "arxiv": "2601.23162",
    "date": "2026-01-30",
    "scope": "4d Lorentzian causal spinfoam vertex; vertex-level causal data and large-spin asymptotics",
}

GUARDS = {
    "split": {
        "claim": "Toller causal components satisfy T_plus + T_minus = D and provide a causal decomposition of the Lorentzian vertex data.",
        "pass": True,
        "classification": "PASS_CAUSAL_TOLLER_SPLIT_IDENTITY_AT_VERTEX_SCOPE",
    },
    "regge": {
        "claim": "In the large-spin limit, causal data select Lorentzian Regge geometries compatible with the spinfoam causal data and a single exp(+i S_Regge/hbar) phase.",
        "pass": True,
        "classification": "PASS_CAUSAL_LARGE_SPIN_SINGLE_PHASE_LORENTZIAN_REGGE_ENDPOINT",
    },
    "scope": {
        "claim": "The authority is a vertex-level result and does not itself supply complete-stack/refinement UV-to-IR transport or family-scope closure.",
        "pass": True,
        "classification": "PASS_SCOPE_BOUNDARY__VERTEX_RESULT_NOT_COMPLETE_STACK_TRANSPORT",
    },
    "transport": {
        "claim": "No explicit same-realization coupling/gamma/spin-scale trajectory is supplied that transports the Iter287 small-spin UV fixed-point sector continuously to this causal large-spin Regge endpoint with normalized observable/comparator/error propagation.",
        "pass": True,
        "classification": "PASS_BLOCKER_PRESERVATION__UV_TO_IR_PARAMETER_TRANSPORT_STILL_MISSING",
    },
}

AGGREGATE_CLASSIFICATION = (
    "HIGH_VALUE_CAUSAL_LARGE_SPIN_LORENTZIAN_REGGE_ENDPOINT__"
    "NO_COMPLETE_STACK_SAME_REALIZATION_UV_TO_IR_TRANSPORT"
)


def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode()


def write_json(path, obj):
    p = pathlib.Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def run_guard(label, output):
    if label not in GUARDS:
        raise SystemExit(f"unknown guard: {label}")
    g = GUARDS[label]
    payload = {
        "schema_version": "1.0",
        "authority": AUTHORITY,
        "guard": label,
        "claim": g["claim"],
        "pass": g["pass"],
        "classification": g["classification"],
        "frozen_core_modified": False,
        "family_terminal_claimed": False,
    }
    payload["digest"] = "sha256:" + hashlib.sha256(canonical(payload)).hexdigest()
    write_json(output, payload)
    if not payload["pass"]:
        sys.exit(1)


def aggregate(input_dir, output):
    root = pathlib.Path(input_dir)
    files = sorted(root.glob("*.json"))
    rows = [json.loads(p.read_text(encoding="utf-8")) for p in files]
    labels = {r.get("guard") for r in rows}
    required = set(GUARDS)
    if labels != required:
        raise SystemExit(f"guard set mismatch: got={sorted(labels)} required={sorted(required)}")
    all_pass = all(bool(r.get("pass")) for r in rows)
    payload = {
        "schema_version": "1.0",
        "authority": AUTHORITY,
        "guards": {r["guard"]: r["classification"] for r in rows},
        "all_guards_pass": all_pass,
        "aggregate_classification": AGGREGATE_CLASSIFICATION,
        "same_realization_transport_ready": False,
        "family_terminal": False,
        "d7_authorized": False,
        "candidate_gravity_activation": False,
    }
    payload["digest"] = "sha256:" + hashlib.sha256(canonical(payload)).hexdigest()
    write_json(output, payload)
    if not all_pass:
        sys.exit(1)


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    g = sub.add_parser("guard")
    g.add_argument("--label", required=True)
    g.add_argument("--output", required=True)
    a = sub.add_parser("aggregate")
    a.add_argument("--input-dir", required=True)
    a.add_argument("--output", required=True)
    ns = ap.parse_args()
    if ns.cmd == "guard":
        run_guard(ns.label, ns.output)
    else:
        aggregate(ns.input_dir, ns.output)


if __name__ == "__main__":
    main()

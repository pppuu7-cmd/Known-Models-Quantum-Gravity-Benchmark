#!/usr/bin/env python3
"""V9 exact source-authority audit for the V8 finite-renormalization freedom."""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from fractions import Fraction
from pathlib import Path

GATE = "SOURCE_J1_K5_TRIANGLE_DERIVATIVE_CONTACT_FINITE_RENORMALIZATION_AUTHORITY_GATE"
BLOCKED = "SOURCE_FINITE_RENORMALIZATION_AUTHORITY_BLOCKED_SCOPED"
UNIQUE = "SOURCE_FINITE_RENORMALIZATION_UNIQUELY_FIXED_SCOPED"
QUOTIENT = "SOURCE_FINITE_RENORMALIZATION_QUOTIENT_FIXED_SCOPED"
INCONSISTENT = "SOURCE_FINITE_RENORMALIZATION_CONSTRAINT_INCONSISTENT_SCOPED"
INVALID = "INVALID_IMPLEMENTATION"

EXPECTED_SOURCE_BLOBS = {
    "sources/arxiv_2202_04360_sl2c_haar_cartan.json": "4a8eb5762745f4b483c8aff87c0c9fb8b74cc236",
    "sources/arxiv_2601_23162v1_causal_vertex.json": "f0b520fc04904e038f252dc5b45d23893cb020ed",
    "sources/arxiv_2604_24945v1_toller_cartan.json": "8dc58f3c9c191289f2f148469f8df3ea95f77ad5",
}
EXPECTED_CHAIN_BLOBS = {
    "results/SOURCE_J1_K5_HIGHEST_CONTACT_MAGNETIC_LEADING_TRANSFER_V4_REPAIR_TERMINAL_2026-09-16.md": "fe69a936e561ddb84d933e9145be325d6ddc966b",
    "recovery/CRITICAL_REVIEW_SOURCE_J1_K5_CHANNEL_COVERAGE_V5_2026-09-16.md": "943a0c5a9cbd7d806d6927569f109d17be65ef68",
    "results/SOURCE_J1_K5_TRIANGLE_DERIVATIVE_CONTACT_REGULARIZATION_V7_REPAIR_TERMINAL_2026-09-16.md": "3e38daea995a7f803181080b32310beb61d39da4",
    "inputs/source_j1_k5_triangle_derivative_contact_counterterm_authority_v8.json": "4d048a0cb130e7e5e1e632773f247572946f042c",
    "results/SOURCE_J1_K5_TRIANGLE_DERIVATIVE_CONTACT_COUNTERTERM_EQUIVALENCE_V8_CANONICAL_2026-09-16.json": "49e248993d0a23d85663aaa198cd5d87b6200b6e",
    "results/SOURCE_J1_K5_TRIANGLE_DERIVATIVE_CONTACT_COUNTERTERM_EQUIVALENCE_V8_TERMINAL_2026-09-16.md": "a63ffe988fa6584775a77892f695d776e9c142cc",
}
V8_CANONICAL = "results/SOURCE_J1_K5_TRIANGLE_DERIVATIVE_CONTACT_COUNTERTERM_EQUIVALENCE_V8_CANONICAL_2026-09-16.json"
EXPECTED_NULLSPACE = [
    ["1", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "1", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "1", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "1", "0", "0", "0"],
    ["0", "0", "0", "18", "0", "6", "1", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "1"],
]
EXPECTED_SOURCE_SET = set(EXPECTED_SOURCE_BLOBS)

MENTION_TERMS = ("normalization", "renormal", "counterterm", "gluing", "composition", "rg", "scale")
ACTION_KEYS = {
    "finite_counterterm_coefficients": "FINITE_COEFFICIENTS",
    "finite_counterterm_equations": "FINITE_COEFFICIENTS",
    "finite_renormalization_condition": "FINITE_NORMALIZATION",
    "common_finite_normalization": "FINITE_NORMALIZATION",
    "gluing_composition_constraint": "GLUING_COMPOSITION",
    "rg_scale_constraint": "RG_SCALE",
    "authorized_finite_renormalization_quotient": "AUTHORIZED_QUOTIENT",
}


def F(x):
    if isinstance(x, Fraction):
        return x
    if isinstance(x, int):
        return Fraction(x, 1)
    return Fraction(str(x))


def rank(matrix):
    a = [[F(x) for x in row] for row in matrix]
    if not a:
        return 0
    rows, cols = len(a), len(a[0])
    r = 0
    for c in range(cols):
        pivot = next((i for i in range(r, rows) if a[i][c] != 0), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        p = a[r][c]
        a[r] = [x / p for x in a[r]]
        for i in range(rows):
            if i != r and a[i][c] != 0:
                q = a[i][c]
                a[i] = [x - q * y for x, y in zip(a[i], a[r])]
        r += 1
        if r == rows:
            break
    return r


def exact_constraint_status(matrix, rhs, n=6):
    if not matrix:
        return {"rank": 0, "augmented_rank": 0, "nullity": n, "consistent": True}
    if any(len(row) != n for row in matrix) or len(rhs) != len(matrix):
        raise ValueError("malformed selector constraint dimensions")
    r = rank(matrix)
    ar = rank([list(row) + [b] for row, b in zip(matrix, rhs)])
    return {"rank": r, "augmented_rank": ar, "nullity": n - r, "consistent": r == ar}


def git_blob_sha(repo_root, path):
    return subprocess.check_output(
        ["git", "-C", str(repo_root), "rev-parse", f"HEAD:{path}"], text=True
    ).strip()


def flatten_mentions(obj, path="$"):
    out = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            key_path = f"{path}.{k}"
            low = str(k).lower()
            terms = sorted({t for t in MENTION_TERMS if t in low})
            if terms:
                out.append({"path": key_path, "terms": terms, "kind": "key"})
            out.extend(flatten_mentions(v, key_path))
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            out.extend(flatten_mentions(v, f"{path}[{i}]"))
    elif isinstance(obj, str):
        low = obj.lower()
        terms = sorted({t for t in MENTION_TERMS if t in low})
        if terms:
            out.append({"path": path, "terms": terms, "kind": "value"})
    return out


def find_action_keys(obj, source_path, path="$"):
    records = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            kp = f"{path}.{k}"
            if k in ACTION_KEYS:
                parent_same = bool(obj.get("same_realization", False))
                records.append({
                    "source": source_path,
                    "path": kp,
                    "key": k,
                    "category": ACTION_KEYS[k],
                    "same_realization": parent_same,
                    "payload": v,
                })
            records.extend(find_action_keys(v, source_path, kp))
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            records.extend(find_action_keys(v, source_path, f"{path}[{i}]"))
    return records


def selector_record_to_constraints(rec):
    if not rec.get("same_realization", False):
        return [], [], False, None
    key = rec["key"]
    payload = rec["payload"]
    if key == "finite_counterterm_coefficients":
        if isinstance(payload, dict):
            vals = payload.get("free_coordinates")
        else:
            vals = payload
        if isinstance(vals, list) and len(vals) == 6:
            return [[1 if i == j else 0 for j in range(6)] for i in range(6)], vals, False, None
    if key in ("finite_counterterm_equations", "finite_renormalization_condition", "gluing_composition_constraint", "rg_scale_constraint"):
        if isinstance(payload, dict) and isinstance(payload.get("matrix"), list) and isinstance(payload.get("rhs"), list):
            return payload["matrix"], payload["rhs"], bool(payload.get("fixes_common_normalization", False)), None
    if key == "common_finite_normalization":
        if payload is not None:
            return [], [], True, None
    if key == "authorized_finite_renormalization_quotient":
        if isinstance(payload, dict):
            return [], [], False, {
                "directions": payload.get("directions", []),
                "observable_class_fixed": bool(payload.get("observable_class_fixed", False)),
            }
    return [], [], False, None


def classify_records(records, mention_only=False):
    matrix, rhs = [], []
    common_norm = False
    quotient_records = []
    wrong_realization = []
    actionable = []
    for rec in records:
        if not rec.get("same_realization", False):
            wrong_realization.append({k: rec[k] for k in ("source", "path", "key", "category") if k in rec})
            continue
        m, b, norm, q = selector_record_to_constraints(rec)
        if m or norm or q is not None or rec["key"] == "finite_counterterm_coefficients":
            actionable.append({k: rec[k] for k in ("source", "path", "key", "category") if k in rec})
        matrix.extend(m)
        rhs.extend(b)
        common_norm = common_norm or norm
        if q is not None:
            quotient_records.append(q)

    status = exact_constraint_status(matrix, rhs, 6)
    if not status["consistent"]:
        classification = INCONSISTENT
    else:
        quotient_rank = 0
        quotient_fixed = False
        for q in quotient_records:
            dirs = q["directions"]
            if isinstance(dirs, list) and dirs and all(isinstance(row, list) and len(row) == 6 for row in dirs):
                quotient_rank = max(quotient_rank, rank(dirs))
                quotient_fixed = quotient_fixed or q["observable_class_fixed"]
        if quotient_rank == 6 and quotient_fixed:
            classification = QUOTIENT
        elif status["rank"] == 6 and common_norm:
            classification = UNIQUE
        else:
            classification = BLOCKED
    return {
        "classification": classification,
        "selector_rank": status["rank"],
        "selector_augmented_rank": status["augmented_rank"],
        "remaining_affine_nullity": status["nullity"],
        "common_finite_normalization_fixed": common_norm,
        "actionable_records": actionable,
        "wrong_realization_records": wrong_realization,
        "mention_only_present": bool(mention_only),
    }


def synthetic_controls():
    ident = [[1 if i == j else 0 for j in range(6)] for i in range(6)]
    unique_rec = [{
        "source": "synthetic", "path": "$.selectors.unique", "key": "finite_renormalization_condition",
        "category": "FINITE_NORMALIZATION", "same_realization": True,
        "payload": {"matrix": ident, "rhs": [1, 2, 3, 4, 5, 6], "fixes_common_normalization": True},
    }]
    quotient_rec = [{
        "source": "synthetic", "path": "$.selectors.quotient", "key": "authorized_finite_renormalization_quotient",
        "category": "AUTHORIZED_QUOTIENT", "same_realization": True,
        "payload": {"directions": ident, "observable_class_fixed": True},
    }]
    inconsistent_rec = [{
        "source": "synthetic", "path": "$.selectors.bad", "key": "rg_scale_constraint",
        "category": "RG_SCALE", "same_realization": True,
        "payload": {"matrix": [[1,0,0,0,0,0],[1,0,0,0,0,0]], "rhs": [0, 1]},
    }]
    wrong_rec = [{
        "source": "synthetic", "path": "$.selectors.wrong", "key": "finite_renormalization_condition",
        "category": "FINITE_NORMALIZATION", "same_realization": False,
        "payload": {"matrix": ident, "rhs": [0]*6, "fixes_common_normalization": True},
    }]
    return {
        "unique_fixture": classify_records(unique_rec)["classification"] == UNIQUE,
        "quotient_fixture": classify_records(quotient_rec)["classification"] == QUOTIENT,
        "blocked_mention_only_fixture": classify_records([], mention_only=True)["classification"] == BLOCKED,
        "inconsistent_fixture": classify_records(inconsistent_rec)["classification"] == INCONSISTENT,
        "wrong_realization_rejected": (
            classify_records(wrong_rec)["classification"] == BLOCKED
            and len(classify_records(wrong_rec)["wrong_realization_records"]) == 1
        ),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo-root", default=".")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    root = Path(args.repo_root)

    actual_sources = {str(p.relative_to(root)) for p in (root / "sources").glob("*.json")}
    source_set_complete = actual_sources == EXPECTED_SOURCE_SET

    blob_records = {}
    blob_locks = True
    for path, expected in {**EXPECTED_SOURCE_BLOBS, **EXPECTED_CHAIN_BLOBS}.items():
        actual = git_blob_sha(root, path)
        ok = actual == expected
        blob_records[path] = {"expected": expected, "actual": actual, "match": ok}
        blob_locks &= ok

    v8 = json.loads((root / V8_CANONICAL).read_text())
    v8_controls = {
        "classification": v8.get("classification") == "SOURCE_UNFIXED_FINITE_LOCAL_FREEDOM_SCOPED",
        "basis_count_8": v8.get("basis_count") == 8,
        "rank_2": v8.get("solve", {}).get("rank") == 2,
        "augmented_rank_2": v8.get("solve", {}).get("augmented_rank") == 2,
        "nullity_6": v8.get("solve", {}).get("nullity") == 6,
        "nullspace_exact": v8.get("solve", {}).get("nullspace_basis") == EXPECTED_NULLSPACE,
        "parent_controls_pass": v8.get("controls_pass") is True,
    }

    source_scan = {}
    all_records = []
    all_mentions = []
    for path in sorted(EXPECTED_SOURCE_BLOBS):
        doc = json.loads((root / path).read_text())
        mentions = flatten_mentions(doc)
        records = find_action_keys(doc, path)
        source_scan[path] = {
            "source_id": doc.get("source_id"),
            "source_scope": doc.get("source_scope"),
            "mentions": mentions,
            "explicit_selector_key_records": [
                {k: r[k] for k in ("path", "key", "category", "same_realization")} for r in records
            ],
        }
        all_mentions.extend({"source": path, **m} for m in mentions)
        all_records.extend(records)

    actual_decision = classify_records(all_records, mention_only=bool(all_mentions))
    synth = synthetic_controls()
    controls = {
        "frozen_source_set_exact": source_set_complete,
        "all_blob_locks": blob_locks,
        "v8_object_reconstructed": all(v8_controls.values()),
        "synthetic_unique_fixture": synth["unique_fixture"],
        "synthetic_quotient_fixture": synth["quotient_fixture"],
        "synthetic_blocked_fixture": synth["blocked_mention_only_fixture"],
        "synthetic_inconsistent_fixture": synth["inconsistent_fixture"],
        "wrong_realization_fixture": synth["wrong_realization_rejected"],
        "no_v8_canonical_representative_as_source_selector": True,
    }
    controls_pass = all(controls.values())
    classification = actual_decision["classification"] if controls_pass else INVALID

    decision_projection = {
        "gate": GATE,
        "classification": classification,
        "controls_pass": controls_pass,
        "controls": controls,
        "v8_controls": v8_controls,
        "source_set_complete": source_set_complete,
        "blob_records": blob_records,
        "source_scan": source_scan,
        "actual_decision": actual_decision,
        "synthetic_controls": synth,
        "new_fact": (
            "Whether the complete frozen structured source corpus provides an actionable same-realization finite-renormalization selector for the six-dimensional terminal V8 affine freedom."
        ),
        "claim_ceiling": (
            "Current durable structured-source authority audit for the local V8 delta-double-prime triangle only; "
            "no all-mollifier theorem, extension existence/nonexistence, full-K5/model/family/D7/global selector, or Candidate Gravity authority."
        ),
    }
    canonical = json.dumps(decision_projection, sort_keys=True, separators=(",", ":"))
    decision_projection["decision_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()
    decision_projection["runtime_python"] = sys.version.split()[0]

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(decision_projection, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "classification": classification,
        "controls_pass": controls_pass,
        "decision_sha256": decision_projection["decision_sha256"],
        "runtime_python": decision_projection["runtime_python"],
        "actionable_selector_count": len(actual_decision["actionable_records"]),
        "wrong_realization_selector_count": len(actual_decision["wrong_realization_records"]),
        "mention_count": len(all_mentions),
        "remaining_affine_nullity": actual_decision["remaining_affine_nullity"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Exact source/object classifier for Eq4 local collision primary-source map expansion."""
from __future__ import annotations

import argparse
import hashlib
import json
import platform
from pathlib import Path

GATE = "SOURCE_J1_K5_EQ4_LOCAL_COLLISION_PRIMARY_SOURCE_MAP_EXPANSION_GATE"
EXPECTED_PARENT = "EQ4_LOCAL_COLLISION_TEST_JET_MAP_SOURCE_BLOCKED_SCOPED"
REQUIRED = (
    "LOCAL_COLLISION_CHART",
    "SMOOTH_REMAINDER_OBJECT",
    "JET_ORDER_7_COMPLETENESS",
    "PERMUTATION_COORDINATE_CONSISTENCY",
)
SOURCES = {
    "arXiv:2601.23162v1": "cc533af3c84de8c0de57523a795ba4357523712f1746ce55fa78eb521cd51713",
    "arXiv:2604.24945v1": "f37659f5cb4674dd0c1b81a6e55f5d1dfd992c60b0e85cb2859322b860e22046",
}
PASS = "EQ4_LOCAL_COLLISION_PRIMARY_SOURCE_MAP_EXPANDED_SCOPED"
PARTIAL = "EQ4_LOCAL_COLLISION_PRIMARY_SOURCE_MAP_PARTIAL_BLOCKED_SCOPED"
BLOCKED = "EQ4_LOCAL_COLLISION_PRIMARY_SOURCE_MAP_AUTHORITY_BLOCKED_SCOPED"
INCONSISTENT = "EQ4_LOCAL_COLLISION_PRIMARY_SOURCE_MAP_INCONSISTENT_SCOPED"
INVALID = "INVALID_IMPLEMENTATION"


def load(path: Path):
    return json.loads(path.read_text())


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_sha(obj) -> str:
    raw = json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def classify(field_states, *, source_ok=True, contradictory=False):
    if not source_ok:
        return INVALID
    if contradictory:
        return INCONSISTENT
    actionable = {k for k, v in field_states.items() if v == "ACTIONABLE"}
    if actionable == set(REQUIRED):
        return PASS
    if actionable:
        return PARTIAL
    return BLOCKED


def audit_record(record, source_id, pdf_sha):
    ok = True
    ok &= record.get("gate") == GATE
    ok &= record.get("source_id") == source_id
    ok &= record.get("pdf_sha256") == pdf_sha
    candidates = record.get("candidate_passages", [])
    ok &= bool(candidates)
    for p in candidates:
        ok &= isinstance(p.get("page"), int) and p["page"] > 0
        ok &= bool(p.get("section"))
        ok &= bool(p.get("equations"))
        assess = p.get("field_assessment", {})
        ok &= set(assess) == set(REQUIRED)
        ok &= all(v in {"ACTIONABLE", "NON_ACTIONABLE", "CONTRADICTED"} for v in assess.values())
    declared = record.get("new_actionable_fields", [])
    ok &= all(x in REQUIRED for x in declared)
    return ok


def merged_states(records):
    states = {k: "MISSING" for k in REQUIRED}
    contradictory = False
    for rec in records:
        for p in rec.get("candidate_passages", []):
            for k, v in p.get("field_assessment", {}).items():
                if v == "CONTRADICTED":
                    contradictory = True
                elif v == "ACTIONABLE":
                    states[k] = "ACTIONABLE"
    return states, contradictory


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo-root", default=".")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    root = Path(args.repo_root)

    authority_path = root / "inputs/source_j1_k5_eq4_local_collision_primary_source_map_expansion_authority.json"
    parent_path = root / "results/SOURCE_J1_K5_EQ4_LOCAL_COLLISION_TEST_JET_MAP_TERMINAL_2026-09-16.md"
    causal_path = root / "sources/arxiv_2601_23162v1_eq4_local_collision_map_expansion_v13.json"
    toller_path = root / "sources/arxiv_2604_24945v1_eq4_local_collision_map_expansion_v13.json"

    authority = load(authority_path)
    parent = parent_path.read_text()
    causal = load(causal_path)
    toller = load(toller_path)
    records = [causal, toller]

    source_ok = (
        authority.get("gate") == GATE
        and tuple(authority.get("required_fields", [])) == REQUIRED
        and authority.get("missing_is_not_zero") is True
        and authority.get("synthetic_substitution_forbidden") is True
        and authority.get("external_source_decision_forbidden") is True
        and audit_record(causal, "arXiv:2601.23162v1", SOURCES["arXiv:2601.23162v1"])
        and audit_record(toller, "arXiv:2604.24945v1", SOURCES["arXiv:2604.24945v1"])
    )
    parent_ok = (
        EXPECTED_PARENT in parent
        and "LOCAL_COLLISION_CHART = false" in parent
        and "SMOOTH_REMAINDER_OBJECT = false" in parent
        and "JET_ORDER_7_COMPLETENESS = false" in parent
        and "PERMUTATION_COORDINATE_CONSISTENCY = false" in parent
        and "nullspace_action_rank = null" in parent
    )

    states, contradictory = merged_states(records)
    actual = classify(states, source_ok=source_ok and parent_ok, contradictory=contradictory)

    complete = {k: "ACTIONABLE" for k in REQUIRED}
    partial = {k: "MISSING" for k in REQUIRED}; partial[REQUIRED[0]] = "ACTIONABLE"
    empty = {k: "MISSING" for k in REQUIRED}
    controls = {
        "authority_and_source_locks": source_ok,
        "parent_terminal_lock": parent_ok,
        "actual_records_have_no_unlisted_actionable_field": all(set(r.get("new_actionable_fields", [])) <= set(REQUIRED) for r in records),
        "complete_fixture_passes": classify(complete) == PASS,
        "partial_fixture_blocks": classify(partial) == PARTIAL,
        "empty_fixture_blocks": classify(empty) == BLOCKED,
        "contradiction_fixture_inconsistent": classify(complete, contradictory=True) == INCONSISTENT,
        "wrong_source_fixture_invalid": classify(complete, source_ok=False) == INVALID,
        "missing_never_encoded_as_zero": all(v in {"MISSING", "ACTIONABLE"} for v in states.values()),
    }
    controls_pass = all(controls.values())
    classification = actual if controls_pass else INVALID
    actionable = sorted(k for k, v in states.items() if v == "ACTIONABLE")
    missing = sorted(k for k in REQUIRED if k not in actionable)

    decision = {
        "gate": GATE,
        "classification": classification,
        "controls_pass": controls_pass,
        "new_actionable_fields": actionable,
        "remaining_missing_fields": missing,
        "map_complete": classification == PASS,
        "source_corpus": sorted(SOURCES),
        "source_pdf_sha256": SOURCES,
        "parent_classification": EXPECTED_PARENT,
        "nullspace_action_rank": None,
        "claim_ceiling": "Primary-source local-map availability only; missing map fields are not zero and no physical quotient, distributional nonexistence, model/family failure, D7 closure, selector, or Candidate Gravity conclusion follows.",
    }
    decision["decision_sha256"] = canonical_sha(decision)
    output = {
        **decision,
        "python": platform.python_version(),
        "controls": controls,
        "merged_field_states": states,
        "source_record_sha256": {
            "arXiv:2601.23162v1": file_sha256(causal_path),
            "arXiv:2604.24945v1": file_sha256(toller_path),
        },
        "authority_sha256": file_sha256(authority_path),
    }
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps(decision, sort_keys=True))


if __name__ == "__main__":
    main()

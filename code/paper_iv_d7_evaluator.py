"""Executable Paper-IV D7 evaluator.

This program does not force a terminal decision. It recomputes the D7 prerequisites
from the frozen coverage contract and comparator residual matrix, enumerates every
required family-level blocker, and verifies the stored D7 attempt artifact.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "protocol" / "PAPER_IV_MAJOR_FRAMEWORK_COVERAGE_CONTRACT.json"
MATRIX = ROOT / "paper_iv" / "PAPER_IV_COMPARATOR_RESIDUAL_MATRIX_2026-09-10.json"
ATTEMPT = ROOT / "paper_iv" / "PAPER_IV_D7_ATTEMPT_2026-09-10.json"
TERMINAL_COVERAGE = {
    "BENCHMARKED_COMPLETE_REALIZATION",
    "EQUIVALENCE_CLASS_CLOSED_BY_THEOREM",
    "MERGED_INTO_OTHER_ROW_WITH_EXPLICIT_REDUCTION_MAP",
    "OUTSIDE_PAPER_IV_TARGET_WITH_SCOPE_PROOF",
}


def compute() -> dict:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    matrix = json.loads(MATRIX.read_text(encoding="utf-8"))
    tier1 = {r["id"]: r for r in contract["tier1_required_rows"]}
    required = {r["id"]: r for r in matrix["frameworks"] if r.get("required_for_D2") is True}
    if set(tier1) != set(required):
        raise AssertionError("D7 census mismatch between contract and matrix")

    unresolved_tier2 = [r["id"] for r in contract.get("tier2_resolution_watchlist", []) if r.get("status") == "UNRESOLVED_CLASSIFICATION"]
    nonterminal_families = [rid for rid, c in tier1.items() if c.get("coverage_status") not in TERMINAL_COVERAGE]
    object_failures = [rid for rid, r in required.items() if r.get("object_complete_in_declared_domain") is not True]
    residual_failures = [rid for rid, r in required.items() if r.get("residual_defined") is not True]
    candidate_rows = [r for r in required.values() if r.get("role") != "baseline_comparator"]
    family_exclusion_gaps = [r["id"] for r in candidate_rows if r.get("counts_as_new_required_exclusion") is not True]
    globally_sufficient = [r["id"] for r in candidate_rows if r.get("global_sufficiency") is True]
    adapter_only = [r["id"] for r in candidate_rows if r.get("adapter_only_gap_proven") is True]
    hybrid_ready = [r["id"] for r in candidate_rows if r.get("hybrid_interface_certificate") is True]

    d2a = not nonterminal_families and not unresolved_tier2
    d2b = not object_failures
    d2 = d2a and d2b
    d4 = d2a and not residual_failures

    decisions = {
        "EXISTING_SUFFICIENT": bool(d2 and d4 and globally_sufficient),
        "ADAPT_EXISTING": bool(d2 and d4 and adapter_only),
        "HYBRID_REQUIRED": bool(d2 and d4 and hybrid_ready),
        "NEW_REQUIRED": bool(d2 and d4 and not family_exclusion_gaps),
    }
    authorized = [k for k, v in decisions.items() if v]
    if len(authorized) > 1:
        raise AssertionError(f"ambiguous terminal decisions: {authorized}")
    global_decision = authorized[0] if authorized else "NOT_YET_AUTHORIZED"

    blockers = []
    for rid in nonterminal_families:
        row = required[rid]
        blockers.append({
            "family": rid,
            "coverage_status": tier1[rid].get("coverage_status"),
            "object_status": row.get("object_status"),
            "missing_certificate": row.get("missing_certificate"),
            "residual_status": row.get("residual_status"),
        })

    return {
        "rqir_core": contract.get("rqir_core"),
        "tier1_total": len(tier1),
        "tier1_nonterminal": len(nonterminal_families),
        "tier2_unresolved": len(unresolved_tier2),
        "D2A_framework_family_coverage": d2a,
        "D2B_complete_objects": d2b,
        "D2": d2,
        "D4": d4,
        "D7": bool(authorized),
        "terminal_authorization": decisions,
        "global_decision": global_decision,
        "candidate_gravity_activation": global_decision == "NEW_REQUIRED",
        "object_failures": object_failures,
        "residual_failures": residual_failures,
        "family_exclusion_gaps": family_exclusion_gaps,
        "blockers": blockers,
    }


def main() -> int:
    computed = compute()
    stored = json.loads(ATTEMPT.read_text(encoding="utf-8"))
    keys = [
        "tier1_total", "tier1_nonterminal", "tier2_unresolved",
        "D2A_framework_family_coverage", "D2B_complete_objects", "D2", "D4", "D7",
        "terminal_authorization", "global_decision", "candidate_gravity_activation",
        "object_failures", "residual_failures", "family_exclusion_gaps", "blockers",
    ]
    mismatches = [k for k in keys if stored.get(k) != computed.get(k)]
    if stored.get("rqir_core") != computed.get("rqir_core"):
        mismatches.append("rqir_core")
    if mismatches:
        raise AssertionError(f"stored D7 attempt differs from executable evaluation: {mismatches}")
    print(json.dumps({"status":"PASS_D7_EVALUATED","result":computed}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

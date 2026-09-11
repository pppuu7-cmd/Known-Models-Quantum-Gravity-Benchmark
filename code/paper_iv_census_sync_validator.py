"""Fail-closed cross-artifact census consistency check for Paper IV.

This validator prevents a newly promoted or reduced Tier-1 family from being
updated in only part of the decision stack. It does not establish scientific
closure; it only requires that the coverage contract, comparator matrix, D7
attempt and D7 readiness state describe the same current Tier-1 census.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "protocol" / "PAPER_IV_MAJOR_FRAMEWORK_COVERAGE_CONTRACT.json"
MATRIX = ROOT / "paper_iv" / "PAPER_IV_COMPARATOR_RESIDUAL_MATRIX_2026-09-10.json"
ATTEMPT = ROOT / "paper_iv" / "PAPER_IV_D7_ATTEMPT_2026-09-10.json"
READINESS = ROOT / "paper_iv" / "PAPER_IV_D7_READINESS_STATE.json"
TERMINAL_COVERAGE = {
    "BENCHMARKED_COMPLETE_REALIZATION",
    "EQUIVALENCE_CLASS_CLOSED_BY_THEOREM",
    "MERGED_INTO_OTHER_ROW_WITH_EXPLICIT_REDUCTION_MAP",
    "OUTSIDE_PAPER_IV_TARGET_WITH_SCOPE_PROOF",
}


def fail(message: str) -> None:
    raise AssertionError(message)


def main() -> int:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    matrix = json.loads(MATRIX.read_text(encoding="utf-8"))
    attempt = json.loads(ATTEMPT.read_text(encoding="utf-8"))
    readiness = json.loads(READINESS.read_text(encoding="utf-8"))

    frozen = {"version": "1.0", "status": "FROZEN"}
    for name, artifact in (
        ("contract", contract),
        ("matrix", matrix),
        ("attempt", attempt),
    ):
        if artifact.get("rqir_core") != frozen:
            fail(f"{name}: RQIR Core v1.0 frozen invariant mismatch")

    tier1_rows = contract.get("tier1_required_rows", [])
    tier1_ids = [row.get("id") for row in tier1_rows]
    if not tier1_ids or any(not item for item in tier1_ids):
        fail("contract: invalid Tier-1 ids")
    if len(tier1_ids) != len(set(tier1_ids)):
        fail("contract: duplicate Tier-1 ids")
    tier1_set = set(tier1_ids)

    required_matrix = {
        row.get("id"): row
        for row in matrix.get("frameworks", [])
        if row.get("required_for_D2") is True
    }
    if set(required_matrix) != tier1_set:
        fail(
            "contract/matrix Tier-1 mismatch: "
            f"contract={sorted(tier1_set)} matrix={sorted(required_matrix)}"
        )

    nonterminal_ids = [
        row["id"] for row in tier1_rows
        if row.get("coverage_status") not in TERMINAL_COVERAGE
    ]
    terminal_count = len(tier1_rows) - len(nonterminal_ids)
    candidate_ids = [
        rid for rid in tier1_ids
        if required_matrix[rid].get("role") != "baseline_comparator"
    ]
    object_failures = [
        rid for rid in tier1_ids
        if required_matrix[rid].get("object_complete_in_declared_domain") is not True
    ]
    residual_failures = [
        rid for rid in tier1_ids
        if required_matrix[rid].get("residual_defined") is not True
    ]
    exclusion_gaps = [
        rid for rid in candidate_ids
        if required_matrix[rid].get("counts_as_new_required_exclusion") is not True
    ]

    contract_summary = contract.get("current_coverage_summary", {})
    expected_contract_summary = {
        "tier1_rows": len(tier1_rows),
        "tier1_terminal_coverage_rows": terminal_count,
        "tier1_nonterminal_rows": len(nonterminal_ids),
    }
    for key, expected in expected_contract_summary.items():
        if contract_summary.get(key) != expected:
            fail(f"contract summary {key}: {contract_summary.get(key)!r} != {expected!r}")

    matrix_summary = matrix.get("coverage_summary", {})
    if matrix_summary.get("required_tier1_rows") != len(tier1_rows):
        fail("matrix summary required_tier1_rows mismatch")
    if matrix_summary.get("required_rows_partial_or_blocked") != len(nonterminal_ids):
        fail("matrix summary required_rows_partial_or_blocked mismatch")

    expected_attempt_scalars = {
        "tier1_total": len(tier1_rows),
        "tier1_nonterminal": len(nonterminal_ids),
    }
    for key, expected in expected_attempt_scalars.items():
        if attempt.get(key) != expected:
            fail(f"D7 attempt {key}: {attempt.get(key)!r} != {expected!r}")

    expected_lists = {
        "object_failures": object_failures,
        "residual_failures": residual_failures,
        "family_exclusion_gaps": exclusion_gaps,
    }
    for key, expected in expected_lists.items():
        if attempt.get(key) != expected:
            fail(f"D7 attempt {key} differs from current matrix ordering/census")

    blocker_ids = [item.get("family") for item in attempt.get("blockers", [])]
    if blocker_ids != nonterminal_ids:
        fail(
            "D7 blocker rows differ from current nonterminal Tier-1 ordering: "
            f"blockers={blocker_ids} nonterminal={nonterminal_ids}"
        )

    snapshot = readiness.get("coverage_snapshot", {})
    expected_snapshot = {
        "tier1_total": len(tier1_rows),
        "strict_terminal_rows": terminal_count,
        "strict_nonterminal_rows": len(nonterminal_ids),
    }
    for key, expected in expected_snapshot.items():
        if snapshot.get(key) != expected:
            fail(f"readiness snapshot {key}: {snapshot.get(key)!r} != {expected!r}")

    if readiness.get("metric_separation", {}).get("d7_scientific_authorization") != "NOT_AUTHORIZED":
        fail("census remains nonterminal but readiness does not say NOT_AUTHORIZED")
    if attempt.get("global_decision") != "NOT_YET_AUTHORIZED":
        fail("current nonterminal census must retain NOT_YET_AUTHORIZED")
    if any(attempt.get("terminal_authorization", {}).values()):
        fail("current nonterminal census must not authorize a terminal outcome")

    print(json.dumps({
        "status": "PASS_CENSUS_SYNCHRONIZED",
        "tier1_total": len(tier1_rows),
        "strict_terminal": terminal_count,
        "strict_nonterminal": len(nonterminal_ids),
        "candidate_rows": len(candidate_ids),
        "object_failures": len(object_failures),
        "residual_failures": len(residual_failures),
        "family_exclusion_gaps": len(exclusion_gaps),
        "scientific_terminal": False,
    }, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

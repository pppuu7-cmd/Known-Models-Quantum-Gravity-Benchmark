"""Fail-closed validator for the Paper-IV major-framework coverage census.

A PASS means only that the declared coverage contract and residual matrix are
mutually consistent. It never means that framework coverage is scientifically
complete. Scoped child PASS/FAIL results are preserved but may not silently
be promoted into a parent-family verdict.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "protocol" / "PAPER_IV_MAJOR_FRAMEWORK_COVERAGE_CONTRACT.json"
MATRIX = ROOT / "paper_iv" / "PAPER_IV_COMPARATOR_RESIDUAL_MATRIX_2026-09-10.json"


def fail(msg: str) -> None:
    raise AssertionError(msg)


def main() -> int:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    matrix = json.loads(MATRIX.read_text(encoding="utf-8"))

    frozen = {"version": "1.0", "status": "FROZEN"}
    if contract.get("rqir_core") != frozen or matrix.get("rqir_core") != frozen:
        fail("coverage and matrix must use frozen RQIR Core v1.0")

    terminal_states = set(contract.get("terminal_coverage_states", []))
    nonterminal_states = set(contract.get("nonterminal_coverage_states", []))
    if not terminal_states or not nonterminal_states or terminal_states & nonterminal_states:
        fail("coverage-state taxonomy is malformed")

    tier1 = contract.get("tier1_required_rows", [])
    tier2 = contract.get("tier2_resolution_watchlist", [])
    if not isinstance(tier1, list) or not tier1:
        fail("Tier-1 coverage census must be non-empty")
    tier1_ids = [r.get("id") for r in tier1]
    if len(tier1_ids) != len(set(tier1_ids)) or any(not x for x in tier1_ids):
        fail("Tier-1 framework IDs must be unique and non-empty")
    tier1_set = set(tier1_ids)

    matrix_rows = matrix.get("frameworks", [])
    all_ids = [r.get("id") for r in matrix_rows]
    if len(all_ids) != len(set(all_ids)) or any(not x for x in all_ids):
        fail("matrix IDs must be unique and non-empty")

    required_matrix = {r.get("id"): r for r in matrix_rows if r.get("required_for_D2") is True}
    if set(required_matrix) != tier1_set:
        fail(f"matrix required rows do not match coverage contract: {set(required_matrix)} != {tier1_set}")

    allowed_states = terminal_states | nonterminal_states
    unresolved_tier1: list[str] = []
    for row in tier1:
        rid = row["id"]
        state = row.get("coverage_status")
        if state not in allowed_states:
            fail(f"{rid}: unknown coverage_status {state!r}")
        mrow = required_matrix[rid]
        if state in nonterminal_states:
            unresolved_tier1.append(rid)
            if mrow.get("counts_as_new_required_exclusion") is not False:
                fail(f"{rid}: nonterminal coverage cannot count as exclusion")
            if mrow.get("residual_defined") is True and state != "PARTIAL_SUBFAMILY_ONLY":
                fail(f"{rid}: nonterminal family row cannot silently claim a complete residual")
        if state == "PARTIAL_SUBFAMILY_ONLY" and mrow.get("object_complete_in_declared_domain") is True:
            fail(f"{rid}: partial family coverage cannot be marked complete at family level")

    # Scoped child results are legitimate scientific evidence but never a silent
    # family-level exclusion or sufficiency certificate.
    scoped_children = [r for r in matrix_rows if r.get("required_for_D2") is False]
    for child in scoped_children:
        cid = child["id"]
        parent = child.get("parent_family")
        if not parent or parent not in tier1_set:
            fail(f"{cid}: scoped child must name a Tier-1 parent_family")
        if child.get("role") != "scoped_subbenchmark":
            fail(f"{cid}: non-required scientific row must be scoped_subbenchmark")
        if child.get("counts_as_new_required_exclusion") is not False:
            fail(f"{cid}: scoped child cannot count as family-level NEW_REQUIRED exclusion")
        if child.get("global_sufficiency") is not False:
            fail(f"{cid}: scoped child cannot establish global sufficiency")
        if child.get("object_complete_in_declared_domain") is not True:
            fail(f"{cid}: stored scoped result must be complete in its own declared domain")
        if child.get("residual_defined") is not True:
            fail(f"{cid}: stored scoped result must have a defined result/residual status")

    unresolved_tier2 = [r.get("id") for r in tier2 if r.get("status") == "UNRESOLVED_CLASSIFICATION"]
    if any(not r.get("id") for r in tier2):
        fail("Tier-2 entries need non-empty IDs")

    rules = contract.get("rules", {})
    required_true = [
        "one_scoped_realization_does_not_exclude_entire_school",
        "new_required_requires_no_unresolved_major_school",
        "new_required_requires_family_level_exclusion_or_exhaustive_material_subfamily_resolution",
        "school_merging_requires_explicit_reduction_map",
        "rqir_core_may_not_be_changed_to_fit_a_school",
        "model_specific_adapters_are_allowed_without_core_change",
        "scoped_child_fail_cannot_be_promoted_to_parent_fail_without_family_scope_proof",
        "scoped_child_pass_cannot_be_promoted_to_parent_sufficiency_without_family_scope_proof",
    ]
    for key in required_true:
        if rules.get(key) is not True:
            fail(f"coverage guardrail {key} must be true")
    if rules.get("blocked_or_not_yet_benchmarked_counts_as_exclusion") is not False:
        fail("BLOCKED/NOT_YET_BENCHMARKED must give zero exclusion evidence")

    d2a = not unresolved_tier1 and not unresolved_tier2
    summary = contract.get("current_coverage_summary", {})
    if summary.get("tier1_rows") != len(tier1):
        fail("stored Tier-1 row count mismatch")
    if summary.get("tier1_nonterminal_rows") != len(unresolved_tier1):
        fail("stored Tier-1 nonterminal count mismatch")
    if summary.get("tier2_unresolved_rows") != len(unresolved_tier2):
        fail("stored Tier-2 unresolved count mismatch")
    if d2a and summary.get("D2_coverage_layer") != "PASS":
        fail("coverage is complete but stored D2 coverage layer is not PASS")
    if not d2a and summary.get("D2_coverage_layer") == "PASS":
        fail("coverage layer cannot PASS with unresolved schools")

    print(json.dumps({
        "status": "PASS_LOGIC_ONLY",
        "D2A_framework_set_coverage": d2a,
        "tier1_total": len(tier1),
        "tier1_unresolved": unresolved_tier1,
        "tier2_unresolved": unresolved_tier2,
        "scoped_child_rows": [r["id"] for r in scoped_children],
        "scientific_terminal": False,
    }, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

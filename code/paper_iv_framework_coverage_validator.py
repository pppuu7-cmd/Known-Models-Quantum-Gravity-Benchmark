"""Fail-closed validator for the Paper-IV major-framework coverage census.

PASS means only that the declared coverage contract and residual matrix are
mutually consistent. It never means framework coverage is scientifically
complete. Scoped child results and Tier-2 dispositions may not silently be
promoted into family-level sufficiency or exclusion.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "protocol" / "PAPER_IV_MAJOR_FRAMEWORK_COVERAGE_CONTRACT.json"
MATRIX = ROOT / "paper_iv" / "PAPER_IV_COMPARATOR_RESIDUAL_MATRIX_2026-09-10.json"
ALLOWED_CHILD_ROLES = {"scoped_subbenchmark", "scoped_boundary_control"}
ALLOWED_TIER2 = {
    "UNRESOLVED_CLASSIFICATION",
    "REDUCED_TO_TIER1_WITH_EXPLICIT_MAP",
    "PROMOTED_TO_TIER1",
    "SPLIT_CONCRETE_PARENT_PROMOTION_RULE",
}


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
            if not mrow.get("missing_certificate") or not mrow.get("minimum_payload"):
                fail(f"{rid}: nonterminal family needs explicit closure certificate/payload")
        if state == "PARTIAL_SUBFAMILY_ONLY" and mrow.get("object_complete_in_declared_domain") is True:
            fail(f"{rid}: partial family coverage cannot be marked complete at family level")

    scoped_children = [r for r in matrix_rows if r.get("required_for_D2") is False]
    for child in scoped_children:
        cid = child["id"]
        parent = child.get("parent_family")
        if not parent or parent not in tier1_set:
            fail(f"{cid}: scoped child must name a Tier-1 parent_family")
        if child.get("role") not in ALLOWED_CHILD_ROLES:
            fail(f"{cid}: non-required scientific row has invalid scoped role")
        if child.get("counts_as_new_required_exclusion") is not False:
            fail(f"{cid}: scoped child cannot count as family-level NEW_REQUIRED exclusion")
        if child.get("global_sufficiency") is not False:
            fail(f"{cid}: scoped child cannot establish global sufficiency")
        if child.get("object_complete_in_declared_domain") is not True or child.get("residual_defined") is not True:
            fail(f"{cid}: stored scoped result must be complete/defined in its own domain")

    unresolved_tier2: list[str] = []
    for row in tier2:
        tid = row.get("id")
        status = row.get("status")
        if not tid:
            fail("Tier-2 entries need non-empty IDs")
        if status not in ALLOWED_TIER2:
            fail(f"{tid}: unknown Tier-2 disposition {status!r}")
        if status == "UNRESOLVED_CLASSIFICATION":
            unresolved_tier2.append(tid)
        elif status == "PROMOTED_TO_TIER1":
            if row.get("tier1_id") not in tier1_set:
                fail(f"{tid}: promoted Tier-2 entry must name an existing Tier-1 row")
        elif status == "REDUCED_TO_TIER1_WITH_EXPLICIT_MAP":
            mapping = row.get("reduction_map")
            if not isinstance(mapping, list) or not mapping or not all(isinstance(x, str) and x.strip() for x in mapping):
                fail(f"{tid}: reduction requires a non-empty explicit reduction_map")
        elif status == "SPLIT_CONCRETE_PARENT_PROMOTION_RULE":
            promoted = row.get("promoted_tier1_ids")
            if not isinstance(promoted, list) or not promoted or not set(promoted) <= tier1_set:
                fail(f"{tid}: split disposition must promote concrete existing Tier-1 rows")
            if not str(row.get("promotion_rule", "")).strip():
                fail(f"{tid}: split disposition requires a future-parent promotion rule")

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
        "generic_program_labels_do_not_count_as_tested_physical_parents",
        "new_concrete_independent_parent_triggers_tier1_promotion",
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
    if d2a != (summary.get("D2_coverage_layer") == "PASS"):
        fail("stored D2 coverage layer inconsistent with computed coverage")

    print(json.dumps({
        "status": "PASS_LOGIC_ONLY",
        "D2A_framework_set_coverage": d2a,
        "tier1_total": len(tier1),
        "tier1_unresolved": unresolved_tier1,
        "tier2_unresolved": unresolved_tier2,
        "tier2_dispositions": {r["id"]: r["status"] for r in tier2},
        "scoped_child_rows": [r["id"] for r in scoped_children],
        "scientific_terminal": False,
    }, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

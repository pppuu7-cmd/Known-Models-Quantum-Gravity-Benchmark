"""Fail-closed validator for Paper-IV D2/D4/D7 global decision logic.

This validator consumes both the major-framework coverage contract and the
comparator residual matrix. PASS means the stored nonterminal/terminal logic is
internally consistent; it never means quantum gravity has been scientifically
closed.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "protocol" / "PAPER_IV_MAJOR_FRAMEWORK_COVERAGE_CONTRACT.json"
MATRIX = ROOT / "paper_iv" / "PAPER_IV_COMPARATOR_RESIDUAL_MATRIX_2026-09-10.json"
TERMINAL = {"EXISTING_SUFFICIENT", "ADAPT_EXISTING", "HYBRID_REQUIRED", "NEW_REQUIRED"}


def fail(msg: str) -> None:
    raise AssertionError(msg)


def main() -> int:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    data = json.loads(MATRIX.read_text(encoding="utf-8"))

    frozen = {"version": "1.0", "status": "FROZEN"}
    if data.get("rqir_core") != frozen or contract.get("rqir_core") != frozen:
        fail("RQIR frozen-core invariant violated")

    semantics = data.get("semantics", {})
    for key in ("blocked_is_zero", "blocked_counts_as_exclusion", "not_yet_benchmarked_counts_as_exclusion", "partial_subfamily_counts_as_family_exclusion"):
        if semantics.get(key) is not False:
            fail(f"{key} must be false")
    for key in ("undefined_residual_must_not_be_zero_filled", "terminal_decision_requires_D2_and_D4", "terminal_decision_requires_coverage_contract"):
        if semantics.get(key) is not True:
            fail(f"{key} must be true")

    tier1 = contract.get("tier1_required_rows", [])
    tier1_ids = {r.get("id") for r in tier1}
    if None in tier1_ids or not tier1_ids:
        fail("invalid Tier-1 census")
    terminal_cov = set(contract.get("terminal_coverage_states", []))
    nonterminal_cov = set(contract.get("nonterminal_coverage_states", []))

    rows = data.get("frameworks", [])
    required_rows = {r.get("id"): r for r in rows if r.get("required_for_D2") is True}
    if set(required_rows) != tier1_ids:
        fail(f"required matrix rows do not match Tier-1 census: {set(required_rows)!r} != {tier1_ids!r}")

    tier2 = contract.get("tier2_resolution_watchlist", [])
    unresolved_tier2 = [r.get("id") for r in tier2 if r.get("status") == "UNRESOLVED_CLASSIFICATION"]
    unresolved_tier1 = [r["id"] for r in tier1 if r.get("coverage_status") in nonterminal_cov]
    unknown_cov = [r["id"] for r in tier1 if r.get("coverage_status") not in terminal_cov | nonterminal_cov]
    if unknown_cov:
        fail(f"unknown Tier-1 coverage states: {unknown_cov}")

    d2a_coverage = not unresolved_tier1 and not unresolved_tier2

    # Current contract supports physical-object rows plus future explicit terminal
    # disposition rows. A family may avoid a standalone object only if the contract
    # itself closes it by theorem/reduction/scope proof.
    disposition_states = {"EQUIVALENCE_CLASS_CLOSED_BY_THEOREM", "MERGED_INTO_OTHER_ROW_WITH_EXPLICIT_REDUCTION_MAP", "OUTSIDE_PAPER_IV_TARGET_WITH_SCOPE_PROOF"}
    contract_by_id = {r["id"]: r for r in tier1}
    object_failures = []
    residual_failures = []
    for rid, row in required_rows.items():
        cstate = contract_by_id[rid].get("coverage_status")
        disposition = cstate in disposition_states
        if not disposition and row.get("object_complete_in_declared_domain") is not True:
            object_failures.append(rid)
        if not disposition and row.get("residual_defined") is not True:
            residual_failures.append(rid)

        status = str(row.get("object_status", ""))
        nonterminal_object = status.startswith("BLOCKED") or status in {"NOT_YET_BENCHMARKED", "PARTIAL_SUBFAMILY_ONLY"}
        if nonterminal_object:
            if row.get("counts_as_new_required_exclusion") is not False:
                fail(f"{rid}: nonterminal row cannot count as NEW_REQUIRED exclusion")
            if not row.get("missing_certificate"):
                fail(f"{rid}: nonterminal row needs an explicit missing certificate")
            if not row.get("minimum_payload"):
                fail(f"{rid}: nonterminal row needs a minimum closure payload")

    d2b_objects = not object_failures
    d2_computed = d2a_coverage and d2b_objects
    d4_computed = d2a_coverage and not residual_failures

    gates = data.get("gates", {})
    stored_d2 = gates.get("D2_major_framework_complete_object_coverage")
    stored_d4 = gates.get("D4_comparator_subtracted_residual_matrix")
    stored_d7 = gates.get("D7_global_terminal_proof_obligation")
    if d2_computed != (stored_d2 == "PASS"):
        fail(f"stored D2 inconsistent with computed state: {stored_d2}, computed={d2_computed}")
    if d4_computed != (stored_d4 == "PASS"):
        fail(f"stored D4 inconsistent with computed state: {stored_d4}, computed={d4_computed}")

    auth = data.get("terminal_authorization", {})
    if set(auth) - TERMINAL:
        fail(f"unknown terminal decisions: {set(auth) - TERMINAL}")
    any_authorized = any(auth.get(k) is True for k in TERMINAL)
    if any_authorized and not (d2_computed and d4_computed):
        fail("no terminal decision may be authorized before D2 and D4 pass")

    if auth.get("NEW_REQUIRED") is True:
        if unresolved_tier1 or unresolved_tier2:
            fail("NEW_REQUIRED forbidden while major-school coverage is unresolved")
        candidate_rows = [r for r in required_rows.values() if r.get("role") != "baseline_comparator"]
        non_exclusions = [r["id"] for r in candidate_rows if r.get("counts_as_new_required_exclusion") is not True]
        if non_exclusions:
            fail(f"NEW_REQUIRED requires family-level exclusion evidence: {non_exclusions}")

    computed_d7 = d2_computed and d4_computed and any_authorized
    if computed_d7 != (stored_d7 == "PASS"):
        fail(f"stored D7 inconsistent with computed state: {stored_d7}, computed={computed_d7}")

    global_decision = data.get("global_decision")
    if not computed_d7 and global_decision != "NOT_YET_AUTHORIZED":
        fail("nonterminal matrix must retain NOT_YET_AUTHORIZED")

    print(json.dumps({
        "status": "PASS_LOGIC_ONLY",
        "D2A_framework_set_coverage": d2a_coverage,
        "D2B_complete_objects": d2b_objects,
        "D2_computed": d2_computed,
        "D4_computed": d4_computed,
        "D7_computed": computed_d7,
        "unresolved_tier1": unresolved_tier1,
        "unresolved_tier2": unresolved_tier2,
        "object_failures": object_failures,
        "residual_failures": residual_failures,
        "global_decision": global_decision,
        "scientific_terminal": computed_d7,
    }, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

"""Fail-closed validator for Paper-IV D2/D4/D7 global decision logic.

This script validates the *logical status* of the frozen comparator residual matrix.
A PASS means the ledger is internally consistent with RQIR Core v1.0; it does not
mean that D2, D4, D7, or quantum gravity are scientifically closed.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MATRIX = ROOT / "paper_iv" / "PAPER_IV_COMPARATOR_RESIDUAL_MATRIX_2026-09-10.json"
REQUIRED_FRAMEWORKS = {"GR_EFT", "STRING_DUAL_RESONANCE", "ASYMPTOTIC_SAFETY", "LQG_SPINFOAM", "CFS"}
TERMINAL = {"EXISTING_SUFFICIENT", "ADAPT_EXISTING", "HYBRID_REQUIRED", "NEW_REQUIRED"}


def fail(msg: str) -> None:
    raise AssertionError(msg)


def main() -> int:
    data = json.loads(MATRIX.read_text(encoding="utf-8"))

    core = data.get("rqir_core", {})
    if core != {"version": "1.0", "status": "FROZEN"}:
        fail(f"RQIR frozen-core invariant violated: {core!r}")

    semantics = data.get("semantics", {})
    if semantics.get("blocked_is_zero") is not False:
        fail("BLOCKED must never be represented as zero residual")
    if semantics.get("blocked_counts_as_exclusion") is not False:
        fail("BLOCKED must contribute zero exclusion evidence")
    if semantics.get("undefined_residual_must_not_be_zero_filled") is not True:
        fail("undefined residuals must fail closed")
    if semantics.get("terminal_decision_requires_D2_and_D4") is not True:
        fail("terminal decision must require D2 and D4")

    rows = data.get("frameworks", [])
    by_id = {row.get("id"): row for row in rows if isinstance(row, dict)}
    if set(by_id) != REQUIRED_FRAMEWORKS:
        fail(f"framework coverage mismatch: {set(by_id)!r}")

    required_rows = [row for row in rows if row.get("required_for_D2") is True]
    d2_computed = all(row.get("object_complete_in_declared_domain") is True for row in required_rows)
    d4_computed = all(row.get("residual_defined") is True for row in required_rows)

    for row in required_rows:
        blocked = str(row.get("object_status", "")).startswith("BLOCKED")
        if blocked:
            if row.get("residual_defined") is not False:
                fail(f"blocked row {row['id']} cannot have a defined residual")
            if row.get("counts_as_new_required_exclusion") is not False:
                fail(f"blocked row {row['id']} cannot count as NEW_REQUIRED exclusion")
            if not row.get("missing_certificate"):
                fail(f"blocked row {row['id']} requires an explicit missing certificate")
            if not row.get("minimum_payload"):
                fail(f"blocked row {row['id']} requires a minimum closure payload")

    gates = data.get("gates", {})
    stored_d2 = gates.get("D2_major_framework_complete_object_coverage")
    stored_d4 = gates.get("D4_comparator_subtracted_residual_matrix")
    stored_d7 = gates.get("D7_global_terminal_proof_obligation")

    if d2_computed and stored_d2 != "PASS":
        fail("D2 computed PASS but ledger does not say PASS")
    if not d2_computed and stored_d2 == "PASS":
        fail("D2 cannot PASS while a required object is incomplete")
    if d4_computed and stored_d4 != "PASS":
        fail("D4 computed PASS but ledger does not say PASS")
    if not d4_computed and stored_d4 == "PASS":
        fail("D4 cannot PASS while a required residual is undefined")

    auth = data.get("terminal_authorization", {})
    unknown = set(auth) - TERMINAL
    if unknown:
        fail(f"unknown terminal decisions: {unknown}")

    any_authorized = any(auth.get(k) is True for k in TERMINAL)
    if any_authorized and not (d2_computed and d4_computed):
        fail("no terminal Paper-IV decision may be authorized before D2 and D4 pass")

    if auth.get("NEW_REQUIRED") is True:
        blocked_rows = [r["id"] for r in required_rows if str(r.get("object_status", "")).startswith("BLOCKED")]
        if blocked_rows:
            fail(f"NEW_REQUIRED forbidden with blocked rows: {blocked_rows}")
        non_exclusions = [r["id"] for r in required_rows if r.get("counts_as_new_required_exclusion") is not True]
        if non_exclusions:
            fail(f"NEW_REQUIRED requires exclusion evidence for every required row: {non_exclusions}")

    computed_d7 = d2_computed and d4_computed and any_authorized
    if computed_d7 and stored_d7 != "PASS":
        fail("D7 computed PASS but ledger does not say PASS")
    if not computed_d7 and stored_d7 == "PASS":
        fail("D7 cannot PASS without D2+D4 and a justified terminal decision")

    global_decision = data.get("global_decision")
    if not computed_d7 and global_decision != "NOT_YET_AUTHORIZED":
        fail("nonterminal matrix must retain NOT_YET_AUTHORIZED")

    print(json.dumps({
        "status": "PASS_LOGIC_ONLY",
        "D2_computed": d2_computed,
        "D4_computed": d4_computed,
        "D7_computed": computed_d7,
        "blocked_required_rows": [
            row["id"] for row in required_rows
            if str(row.get("object_status", "")).startswith("BLOCKED")
        ],
        "global_decision": global_decision,
        "scientific_terminal": False,
    }, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

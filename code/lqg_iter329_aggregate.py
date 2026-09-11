#!/usr/bin/env python3
"""Aggregate Iter329 O(3)/parity and conditional homogeneity results."""
from __future__ import annotations

import json
from pathlib import Path

EXPECTED = {"K3": (1, 1), "K4": (2, 0), "K5": (28, 16)}


def main() -> None:
    root = Path("iter329-results")
    rows = {}
    for stratum in EXPECTED:
        candidates = list(root.rglob(f"{stratum}.json"))
        assert len(candidates) == 1, (stratum, candidates)
        row = json.loads(candidates[0].read_text())
        rows[stratum] = row
        cumulative, exact = EXPECTED[stratum]
        assert row["o3_cumulative_through_omega"] == cumulative
        assert row["conditional_exact_homogeneity_dimension"] == exact
        assert row["parity_reduction"] == 0

    linked_o3_total = sum(rows[s]["o3_cumulative_through_omega"] for s in EXPECTED)
    linked_exact_total = sum(rows[s]["conditional_exact_homogeneity_dimension"] for s in EXPECTED)
    assert linked_o3_total == 31
    assert linked_exact_total == 17

    summary = {
        "iteration": 329,
        "status": "SUCCESS",
        "result": {
            "SO3_to_O3_reduction": "31 -> 31",
            "global_S5_linked_O3_bookkeeping_dimension": linked_o3_total,
            "conditional_exact_homogeneity_dimension": linked_exact_total,
            "conditional_reduction": "31 -> 17",
            "uniqueness_selected": linked_exact_total == 1,
        },
        "interpretation": (
            "Adding inversion/parity to the already-audited scalar normal sector does not "
            "reduce the 31 globally S5-linked structures. Even the additional conditional "
            "restriction to exact superficial degree leaves 17 structures, so these symmetry/"
            "homogeneity conditions alone do not select a unique extension."
        ),
        "scope": [
            "CONDITIONAL_EXACT_HOMOGENEITY_ONLY",
            "NOT_SOURCE_DEFINED_PRESCRIPTION",
            "NOT_PHYSICAL_COUNTERTERM_COUNT",
            "DOES_NOT_PROVE_NO_EXTENSION",
            "LQG_REMAINS_PARTIAL_BLOCKED",
            "D7_NOT_AUTHORIZED",
        ],
    }
    out = Path("iter329-summary.json")
    out.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

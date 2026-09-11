#!/usr/bin/env python3
"""Aggregate Iter330 exact invariant-basis and centered-face jet audits."""
from __future__ import annotations

import json
from pathlib import Path


def one(root: Path, mode: str) -> dict:
    files = list(root.rglob(f"{mode}.json"))
    assert len(files) == 1, (mode, files)
    return json.loads(files[0].read_text())


def main() -> None:
    root = Path("iter330-results")
    basis = one(root, "basis")
    k4 = one(root, "k4")
    k3 = one(root, "k3")

    assert basis["k5_exact_invariant_rank"] == 16
    assert basis["s5_orbit_count_before_relations"] == 69
    assert k4["face_value_rank"] == 11
    assert k4["face_value_kernel_dimension"] == 5
    assert k4["cumulative_normal_jet_ranks"] == {"0": 11, "1": 16}
    assert k3["face_value_rank"] == 4
    assert k3["face_value_kernel_dimension"] == 12
    assert k3["cumulative_normal_jet_ranks"] == {"0": 4, "1": 7, "2": 16}

    summary = {
        "iteration": 330,
        "status": "SUCCESS",
        "result": {
            "explicit_k5_degree8_s5_o3_rank": 16,
            "k4_value_restriction": {"rank": 11, "kernel": 5},
            "k4_value_plus_first_normal_jet_rank": 16,
            "k3_value_restriction": {"rank": 4, "kernel": 12},
            "k3_value_plus_first_normal_jet_rank": 7,
            "k3_value_plus_second_normal_jet_rank": 16,
        },
        "interpretation": (
            "The explicit characteristic-zero polynomial model confirms the 16-dimensional "
            "K5 degree-8 invariant sector. Zeroth-order centered-face matching alone cannot "
            "determine it (five K5 directions are invisible on a K4 face; twelve on K3). "
            "However, the first K4 normal jet and the second K3 normal jet make the candidate "
            "restriction maps injective. Therefore the next uniqueness question is whether a "
            "physical/source-defined forest or gluing prescription actually fixes these normal "
            "jets; detectability alone is not a normalization condition."
        ),
        "scope": [
            "EXACT_POLYNOMIAL_ALGEBRA_OVER_Q",
            "CENTERED_STRATUM_RESTRICTION_MODEL",
            "NOT_SOURCE_DEFINED_FOREST_GLUING_MAP",
            "JET_DETECTABILITY_DOES_NOT_IMPLY_JET_NORMALIZATION",
            "DOES_NOT_PROVE_UNIQUE_EXTENSION",
            "LQG_REMAINS_PARTIAL_BLOCKED",
            "D7_NOT_AUTHORIZED",
        ],
    }
    Path("iter330-summary.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Iter329: parity/O(3) and conditional exact-homogeneity audit.

Input data are the exact-order SO(3)-scalar multiplicities established by Iter323
for the normal-sector representation.  For vector normal variables inversion acts
on a degree-n homogeneous polynomial by (-1)^n.  Thus O(3)=SO(3)⋊{1,P}
retains the even-degree SO(3) scalars and removes odd-degree pseudoscalars.

The second layer is deliberately conditional: if a finite-renormalization rule
were to admit only counterterms at exactly the superficial divergence degree
omega, how much ambiguity would remain?  This is not claimed to be a
source-defined prescription and the resulting dimensions are bookkeeping, not
physical counterterm counts.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

SO3_EXACT = {
    "K3": [1],
    "K4": [1, 0, 1, 0],
    "K5": [1, 0, 1, 0, 3, 0, 7, 0, 16],
}
OMEGA = {"K3": 0, "K4": 3, "K5": 8}
EXPECTED_CUMULATIVE = {"K3": 1, "K4": 2, "K5": 28}
EXPECTED_EXACT_OMEGA = {"K3": 1, "K4": 0, "K5": 16}


def audit(stratum: str) -> dict:
    so3 = SO3_EXACT[stratum]
    o3 = [dim if degree % 2 == 0 else 0 for degree, dim in enumerate(so3)]

    # Iter323 already found zero odd-degree SO(3)-scalar multiplicities.  Hence
    # adjoining inversion/parity causes no additional reduction in this sector.
    odd_so3 = {i: d for i, d in enumerate(so3) if i % 2 and d}
    assert not odd_so3, f"unexpected odd SO3 scalar(s): {odd_so3}"
    assert o3 == so3

    cumulative = sum(o3)
    omega = OMEGA[stratum]
    exact_omega = o3[omega]
    assert cumulative == EXPECTED_CUMULATIVE[stratum]
    assert exact_omega == EXPECTED_EXACT_OMEGA[stratum]

    return {
        "iteration": 329,
        "stratum": stratum,
        "omega": omega,
        "so3_exact_by_degree": so3,
        "o3_exact_by_degree": o3,
        "parity_rule": "vector inversion acts as (-1)^degree",
        "parity_reduction": 0,
        "o3_cumulative_through_omega": cumulative,
        "conditional_exact_homogeneity_dimension": exact_omega,
        "scope": [
            "CONDITIONAL_EXACT_HOMOGENEITY_ONLY",
            "NOT_PHYSICAL_COUNTERTERM_COUNT",
            "DOES_NOT_PROVE_NO_EXTENSION",
            "DOES_NOT_AUTHORIZE_D7",
        ],
    }


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--stratum", choices=sorted(SO3_EXACT), required=True)
    p.add_argument("--output", type=Path, required=True)
    args = p.parse_args()
    result = audit(args.stratum)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Exact logical/arithmetic certificate for the frozen one-wedge-vs-joint gate.

Authority:
  research/SOURCE_J1_K5_ONE_WEDGE_UNIQUENESS_VS_JOINT_EXTENSION_PREREG_2026-09-15.md

The source theorem fixes each individual Toller factor.  This certificate keeps all
factor identities unchanged and verifies that the already frozen joint collision
counterterm witness acts only at the product-extension level while preserving the
EPRL sign sum, S5 covariance, off-collision restriction, and scaling ceiling.
"""

from itertools import combinations, permutations, product
from collections import Counter
import json

VERTICES = (1, 2, 3, 4, 5)
EDGES = tuple(combinations(VERTICES, 2))
EDGE_INDEX = {e: i for i, e in enumerate(EDGES)}
N_WEDGES = len(EDGES)

SCALING_DEGREE_JOINT = 30
DELTA_N_SCALING_DEGREE = 12

# Source-level one-wedge data are frozen and identical in E and E'.
# We use stable symbolic identifiers; no factor is modified by the joint extension.
ONE_WEDGE_FACTORS_E = {
    e: {
        "T_plus": f"Tplus_{e[0]}{e[1]}",
        "T_minus": f"Tminus_{e[0]}{e[1]}",
        "sum_rule": f"D_{e[0]}{e[1]}",
        "one_wedge_uniqueness_properties": (
            "asymptotic",
            "matching",
            "Toller_poles",
            "Tplus_plus_Tminus_equals_D",
            "Feynman_i_epsilon_branch",
        ),
    }
    for e in EDGES
}
ONE_WEDGE_FACTORS_E_PRIME = {e: dict(data) for e, data in ONE_WEDGE_FACTORS_E.items()}

assert N_WEDGES == 10
assert ONE_WEDGE_FACTORS_E == ONE_WEDGE_FACTORS_E_PRIME
assert all(
    ONE_WEDGE_FACTORS_E[e]["one_wedge_uniqueness_properties"]
    == ONE_WEDGE_FACTORS_E_PRIME[e]["one_wedge_uniqueness_properties"]
    for e in EDGES
)


def induced_kappa(sigmas):
    s = dict(zip(VERTICES, sigmas))
    return tuple(s[a] * s[b] for a, b in EDGES)


def permute_kappa(kappa, perm):
    p = dict(zip(VERTICES, perm))
    out = [None] * N_WEDGES
    for (a, b), value in zip(EDGES, kappa):
        aa, bb = p[a], p[b]
        edge = tuple(sorted((aa, bb)))
        out[EDGE_INDEX[edge]] = value
    return tuple(out)


sigma_assignments = tuple(product((-1, 1), repeat=len(VERTICES)))
preimage_counts = Counter(induced_kappa(s) for s in sigma_assignments)
CONSTRAINED = frozenset(preimage_counts)
ALL_PATTERNS = tuple(product((-1, 1), repeat=N_WEDGES))
UNCONSTRAINED = frozenset(ALL_PATTERNS) - CONSTRAINED

assert len(sigma_assignments) == 32
assert len(CONSTRAINED) == 16
assert set(preimage_counts.values()) == {2}
assert len(ALL_PATTERNS) == 1024
assert len(UNCONSTRAINED) == 1008

C_CONSTRAINED = 63
C_UNCONSTRAINED = -1


def counterterm_coeff(kappa):
    return C_CONSTRAINED if kappa in CONSTRAINED else C_UNCONSTRAINED


full_eprl_shift = sum(counterterm_coeff(k) for k in ALL_PATTERNS)
causal_distinct_shift = sum(counterterm_coeff(k) for k in CONSTRAINED)
causal_sigma_counted_shift = sum(counterterm_coeff(induced_kappa(s)) for s in sigma_assignments)

assert full_eprl_shift == 0
assert causal_distinct_shift == 1008
assert causal_sigma_counted_shift == 2016
assert DELTA_N_SCALING_DEGREE <= SCALING_DEGREE_JOINT

# Explicit S5 covariance of the joint coefficient family.
permutation_checks = 0
for perm in permutations(VERTICES):
    for kappa in ALL_PATTERNS:
        kp = permute_kappa(kappa, perm)
        assert (kappa in CONSTRAINED) == (kp in CONSTRAINED)
        assert counterterm_coeff(kappa) == counterterm_coeff(kp)
        permutation_checks += 1
assert permutation_checks == 120 * 1024

# Support statement is part of the frozen definition of the witness:
# E'_kappa - E_kappa = c(kappa) delta_N, supp(delta_N) subset N.
# Hence restriction to the punctured domain M\N is exactly unchanged.
joint_difference_support = "N_full_collision"
off_collision_restriction_identical = True
individual_factors_modified = False

assert off_collision_restriction_identical
assert not individual_factors_modified

classification = "SOURCE_J1_K5_ONE_WEDGE_TOLLER_UNIQUENESS_INSUFFICIENT_FOR_JOINT_EXTENSION_SCOPED"

result = {
    "classification": classification,
    "levels": {
        "one_wedge_factor_count": N_WEDGES,
        "all_one_wedge_factors_identical_between_E_and_Eprime": True,
        "individual_factors_modified": individual_factors_modified,
        "one_wedge_uniqueness_properties_identical": True,
        "joint_difference": "c(kappa)*delta_N",
        "joint_difference_support": joint_difference_support,
        "off_collision_restriction_identical": off_collision_restriction_identical,
    },
    "joint_witness_controls": {
        "n_independent_sign_patterns": len(ALL_PATTERNS),
        "n_distinct_constrained_patterns": len(CONSTRAINED),
        "n_unconstrained_patterns": len(UNCONSTRAINED),
        "full_eprl_shift": full_eprl_shift,
        "causal_distinct_shift": causal_distinct_shift,
        "causal_sigma_counted_shift": causal_sigma_counted_shift,
        "delta_N_scaling_degree": DELTA_N_SCALING_DEGREE,
        "joint_scaling_degree_ceiling": SCALING_DEGREE_JOINT,
        "within_scaling_ceiling": True,
        "s5_pattern_checks": permutation_checks,
        "s5_covariant": True,
    },
    "logical_conclusion": {
        "one_wedge_uniqueness_truth_values_change": False,
        "joint_extension_changes": True,
        "one_wedge_uniqueness_alone_excludes_joint_counterterm": False,
        "genuinely_joint_source_condition_required_for_uniqueness": True,
    },
    "claim_ceiling": (
        "The published one-wedge uniqueness theorem fixes the individual Toller matrices, "
        "but by itself does not eliminate the frozen joint collision-supported extension witness. "
        "This does not prove that no stronger source-level joint condition exists."
    ),
}

print(json.dumps(result, indent=2, sort_keys=True))

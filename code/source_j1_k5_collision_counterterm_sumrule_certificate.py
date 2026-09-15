#!/usr/bin/env python3
"""Exact certificate for the frozen K5 collision-counterterm / EPRL sum-rule gate.

Authority:
  research/SOURCE_J1_K5_COLLISION_COUNTERTERM_SUMRULE_PREREG_2026-09-15.md

This script verifies finite sign-combinatorics and scaling-ledger arithmetic only.
It does not construct or prove uniqueness/nonuniqueness of the full source vertex.
"""

from collections import Counter
from itertools import combinations, permutations, product
import json

VERTICES = (1, 2, 3, 4, 5)
EDGES = tuple(combinations(VERTICES, 2))
EDGE_INDEX = {e: i for i, e in enumerate(EDGES)}

N_EDGES = len(EDGES)
N_INDEPENDENT = 2 ** N_EDGES
NORMAL_CODIM = 12
FROZEN_SCALING_DEGREE = 30
DELTA_N_SCALING_DEGREE = NORMAL_CODIM

assert N_EDGES == 10
assert N_INDEPENDENT == 1024
assert DELTA_N_SCALING_DEGREE == 12
assert DELTA_N_SCALING_DEGREE <= FROZEN_SCALING_DEGREE


def induced_kappa(sigmas):
    s = dict(zip(VERTICES, sigmas))
    return tuple(s[a] * s[b] for a, b in EDGES)


def permute_kappa(kappa, perm):
    """Relabel vertices by the permutation tuple perm=(p(1),...,p(5))."""
    p = dict(zip(VERTICES, perm))
    out = [None] * N_EDGES
    for (a, b), value in zip(EDGES, kappa):
        aa, bb = p[a], p[b]
        e = tuple(sorted((aa, bb)))
        out[EDGE_INDEX[e]] = value
    assert all(v is not None for v in out)
    return tuple(out)


sigma_assignments = tuple(product((-1, 1), repeat=len(VERTICES)))
assert len(sigma_assignments) == 32

preimage_counts = Counter(induced_kappa(s) for s in sigma_assignments)
CONSTRAINED = frozenset(preimage_counts)
assert len(CONSTRAINED) == 16
assert set(preimage_counts.values()) == {2}

ALL_PATTERNS = tuple(product((-1, 1), repeat=N_EDGES))
assert len(ALL_PATTERNS) == 1024
UNCONSTRAINED = frozenset(ALL_PATTERNS) - CONSTRAINED
assert len(UNCONSTRAINED) == 1008

# Frozen counterterm coefficients.
C_CONSTRAINED = 63
C_UNCONSTRAINED = -1


def coefficient(kappa):
    return C_CONSTRAINED if kappa in CONSTRAINED else C_UNCONSTRAINED


full_sum = sum(coefficient(k) for k in ALL_PATTERNS)
constrained_distinct_sum = sum(coefficient(k) for k in CONSTRAINED)
constrained_sigma_counted_sum = sum(coefficient(induced_kappa(s)) for s in sigma_assignments)

assert full_sum == 0
assert constrained_distinct_sum == 1008
assert constrained_sigma_counted_sum == 2016

# Explicit S5 invariance of constrained membership and coefficient family.
all_permutations = tuple(permutations(VERTICES))
assert len(all_permutations) == 120
permutation_checks = 0
for perm in all_permutations:
    for kappa in ALL_PATTERNS:
        kp = permute_kappa(kappa, perm)
        assert (kappa in CONSTRAINED) == (kp in CONSTRAINED)
        assert coefficient(kappa) == coefficient(kp)
        permutation_checks += 1
assert permutation_checks == 120 * 1024

# Adversarial controls.
uniform_nonzero_full_sum = sum(1 for _ in ALL_PATTERNS)
assert uniform_nonzero_full_sum == 1024
assert uniform_nonzero_full_sum != 0

zero_constrained_causal_sum = sum(0 for _ in CONSTRAINED)
assert zero_constrained_causal_sum == 0
assert constrained_distinct_sum != 0

classification = "SOURCE_J1_K5_EPRL_SUMRULE_DOES_NOT_FIX_COLLISION_EXTENSION_SCOPED"

result = {
    "classification": classification,
    "n_vertices": len(VERTICES),
    "n_edges": N_EDGES,
    "n_independent_kappa_patterns": N_INDEPENDENT,
    "n_sigma_assignments": len(sigma_assignments),
    "n_distinct_constrained_kappa_patterns": len(CONSTRAINED),
    "constrained_preimage_multiplicity": sorted(set(preimage_counts.values())),
    "n_unconstrained_patterns": len(UNCONSTRAINED),
    "counterterm_coefficients": {
        "constrained": C_CONSTRAINED,
        "unconstrained": C_UNCONSTRAINED,
    },
    "full_independent_sign_counterterm_sum": full_sum,
    "distinct_constrained_counterterm_sum": constrained_distinct_sum,
    "sigma_counted_constrained_counterterm_sum": constrained_sigma_counted_sum,
    "s5_permutations_checked": len(all_permutations),
    "s5_pattern_checks": permutation_checks,
    "constrained_membership_s5_invariant": True,
    "counterterm_coefficient_s5_invariant": True,
    "delta_N_scaling_degree": DELTA_N_SCALING_DEGREE,
    "frozen_full_collision_scaling_degree_ceiling": FROZEN_SCALING_DEGREE,
    "delta_N_within_same_scaling_extension_window": True,
    "adversarial_uniform_nonzero_full_sum": uniform_nonzero_full_sum,
    "adversarial_zero_constrained_shift": zero_constrained_causal_sum,
    "eprl_sign_sum_preserved_by_witness": True,
    "causal_sector_shift_nonzero": True,
    "claim_ceiling": (
        "Exact coefficient/symmetry witness inside the already certified scaling-degree window only. "
        "It proves that the EPRL independent-sign sum rule by itself does not fix causal collision "
        "counterterm coefficients; it does not prove the published vertex remains nonunique after "
        "all possible source-faithful conditions are imposed."
    ),
}

print(json.dumps(result, indent=2, sort_keys=True))

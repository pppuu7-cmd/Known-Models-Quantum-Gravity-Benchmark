#!/usr/bin/env python3
"""Exact certificate for the frozen causal/co-causal conjugation ambiguity gate.

Authority:
  research/SOURCE_J1_K5_CAUSAL_COCAUSAL_CONJUGATION_AMBIGUITY_PREREG_2026-09-15.md

Complex coefficients are represented exactly as Gaussian-integer pairs (re, im).
"""

from collections import Counter
from itertools import combinations, permutations, product
import json

VERTICES = (1, 2, 3, 4, 5)
EDGES = tuple(combinations(VERTICES, 2))
EDGE_INDEX = {e: i for i, e in enumerate(EDGES)}
N_EDGES = len(EDGES)
ALL_PATTERNS = tuple(product((-1, 1), repeat=N_EDGES))
SIGMAS = tuple(product((-1, 1), repeat=len(VERTICES)))

assert N_EDGES == 10
assert len(ALL_PATTERNS) == 1024
assert len(SIGMAS) == 32


def induced_kappa(sigmas):
    s = dict(zip(VERTICES, sigmas))
    return tuple(s[a] * s[b] for a, b in EDGES)


def negate(kappa):
    return tuple(-x for x in kappa)


def permute_kappa(kappa, perm):
    p = dict(zip(VERTICES, perm))
    out = [None] * N_EDGES
    for (a, b), value in zip(EDGES, kappa):
        aa, bb = p[a], p[b]
        edge = tuple(sorted((aa, bb)))
        out[EDGE_INDEX[edge]] = value
    return tuple(out)


preimage_counts_plus = Counter(induced_kappa(s) for s in SIGMAS)
C_PLUS = frozenset(preimage_counts_plus)
C_MINUS = frozenset(negate(k) for k in C_PLUS)
NONCAUSAL = frozenset(ALL_PATTERNS) - C_PLUS - C_MINUS

assert len(C_PLUS) == 16
assert set(preimage_counts_plus.values()) == {2}
assert len(C_MINUS) == 16
assert C_PLUS.isdisjoint(C_MINUS)
assert len(NONCAUSAL) == 992

# Exact Gaussian-integer operations.
def gadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def gconj(a):
    return (a[0], -a[1])


ZERO = (0, 0)
PLUS_I = (0, 1)
MINUS_I = (0, -1)
ONE = (1, 0)


def coeff(kappa):
    if kappa in C_PLUS:
        return PLUS_I
    if kappa in C_MINUS:
        return MINUS_I
    return ZERO


# Full sign reversal / complex-conjugation covariance.
conjugation_checks = 0
for kappa in ALL_PATTERNS:
    assert coeff(negate(kappa)) == gconj(coeff(kappa))
    conjugation_checks += 1
assert conjugation_checks == 1024


def gsum(values):
    out = ZERO
    for v in values:
        out = gadd(out, v)
    return out


full_eprl_sum = gsum(coeff(k) for k in ALL_PATTERNS)
causal_distinct_sum = gsum(coeff(k) for k in C_PLUS)
cocausal_distinct_sum = gsum(coeff(k) for k in C_MINUS)
causal_sigma_counted_sum = gsum(coeff(induced_kappa(s)) for s in SIGMAS)
cocausal_sigma_counted_sum = gsum(coeff(negate(induced_kappa(s))) for s in SIGMAS)

assert full_eprl_sum == ZERO
assert causal_distinct_sum == (0, 16)
assert cocausal_distinct_sum == (0, -16)
assert causal_sigma_counted_sum == (0, 32)
assert cocausal_sigma_counted_sum == (0, -32)

# S5 covariance.
permutation_checks = 0
for perm in permutations(VERTICES):
    for kappa in ALL_PATTERNS:
        kp = permute_kappa(kappa, perm)
        assert coeff(kp) == coeff(kappa)
        permutation_checks += 1
assert permutation_checks == 120 * 1024

# Frozen scaling ledger.
DELTA_N_SCALING_DEGREE = 12
JOINT_SCALING_CEILING = 30
assert DELTA_N_SCALING_DEGREE <= JOINT_SCALING_CEILING

# Adversarial control 1: +1 only on C+ violates conjugation covariance.
def bad_causal_only_coeff(kappa):
    return ONE if kappa in C_PLUS else ZERO

bad_conjugation_failures = 0
for kappa in ALL_PATTERNS:
    if bad_causal_only_coeff(negate(kappa)) != gconj(bad_causal_only_coeff(kappa)):
        bad_conjugation_failures += 1
assert bad_conjugation_failures > 0

# Adversarial control 2: uniform +1 violates EPRL zero-sum.
uniform_full_sum = gsum(ONE for _ in ALL_PATTERNS)
assert uniform_full_sum == (1024, 0)
assert uniform_full_sum != ZERO

classification = "SOURCE_J1_K5_CAUSAL_COCAUSAL_CONJUGATION_STILL_LEAVES_COLLISION_AMBIGUITY_SCOPED"

result = {
    "classification": classification,
    "counts": {
        "n_independent_patterns": len(ALL_PATTERNS),
        "n_sigma_assignments": len(SIGMAS),
        "n_distinct_causal_patterns": len(C_PLUS),
        "causal_preimage_multiplicity": sorted(set(preimage_counts_plus.values())),
        "n_distinct_cocausal_patterns": len(C_MINUS),
        "causal_cocausal_disjoint": C_PLUS.isdisjoint(C_MINUS),
        "n_noncausal_patterns": len(NONCAUSAL),
    },
    "exact_gaussian_integer_sums": {
        "full_eprl_sum_re_im": list(full_eprl_sum),
        "causal_distinct_sum_re_im": list(causal_distinct_sum),
        "cocausal_distinct_sum_re_im": list(cocausal_distinct_sum),
        "causal_sigma_counted_sum_re_im": list(causal_sigma_counted_sum),
        "cocausal_sigma_counted_sum_re_im": list(cocausal_sigma_counted_sum),
    },
    "symmetry_controls": {
        "sign_reversal_conjugation_checks": conjugation_checks,
        "c_minus_equals_global_sign_reversal_of_c_plus": True,
        "coefficient_sign_reversal_conjugation_covariant": True,
        "s5_pattern_checks": permutation_checks,
        "s5_covariant": True,
    },
    "scaling_controls": {
        "delta_N_scaling_degree": DELTA_N_SCALING_DEGREE,
        "joint_scaling_ceiling": JOINT_SCALING_CEILING,
        "within_scaling_ceiling": True,
    },
    "adversarial_controls": {
        "causal_only_real_family_conjugation_failures": bad_conjugation_failures,
        "uniform_nonzero_full_sum_re_im": list(uniform_full_sum),
    },
    "logical_conclusion": {
        "eprl_sum_preserved": True,
        "causal_shift_nonzero": causal_distinct_sum != ZERO,
        "cocausal_shift_nonzero": cocausal_distinct_sum != ZERO,
        "causal_cocausal_shifts_are_conjugate": cocausal_distinct_sum == gconj(causal_distinct_sum),
        "coefficient_level_conjugation_eliminates_collision_ambiguity": False,
    },
    "claim_ceiling": (
        "Exact coefficient-level ambiguity witness compatible with EPRL zero sum, S5 covariance, "
        "same-scaling extension and global sign-reversal/complex-conjugation covariance. It does not "
        "prove compatibility with every representation-index transformation of the full vertex."
    ),
}

print(json.dumps(result, indent=2, sort_keys=True))

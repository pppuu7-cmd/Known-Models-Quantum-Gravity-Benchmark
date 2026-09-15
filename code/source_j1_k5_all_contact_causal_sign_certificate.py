#!/usr/bin/env python3
"""Exact exhaustive certificate for the frozen K5 all-contact causal-sign gate.

Authority:
  research/SOURCE_J1_K5_ALL_CONTACT_CAUSAL_SIGN_PREREG_2026-09-15.md

No numerical tolerance and no external dependency are used.
"""

from collections import Counter
from itertools import combinations, product
import json

VERTICES = (1, 2, 3, 4, 5)
EDGES = tuple(combinations(VERTICES, 2))

assert len(EDGES) == 10

degrees = {v: sum(v in e for e in EDGES) for v in VERTICES}
assert degrees == {1: 4, 2: 4, 3: 4, 4: 4, 5: 4}


def induced_kappa(sigmas):
    s = dict(zip(VERTICES, sigmas))
    return tuple(s[a] * s[b] for a, b in EDGES)


def sign_product(signs):
    out = 1
    for s in signs:
        out *= s
    return out


# Exhaustive constrained causal structures.
constrained = []
for sigmas in product((-1, 1), repeat=len(VERTICES)):
    kappas = induced_kappa(sigmas)
    p = sign_product(kappas)
    constrained.append((sigmas, kappas, p))
    assert p == 1

assert len(constrained) == 32
assert all(p == 1 for _, _, p in constrained)

# Exact degree-count identity: prod_edges sigma_a sigma_b = prod_v sigma_v^deg(v).
for sigmas, _, p in constrained:
    s = dict(zip(VERTICES, sigmas))
    rhs = 1
    for v in VERTICES:
        rhs *= s[v] ** degrees[v]
    assert rhs == 1
    assert p == rhs

# Global reversal leaves all induced edge signs unchanged.
for sigmas, kappas, _ in constrained:
    reversed_sigmas = tuple(-x for x in sigmas)
    assert induced_kappa(reversed_sigmas) == kappas

pattern_multiplicity = Counter(kappas for _, kappas, _ in constrained)
assert len(pattern_multiplicity) == 16
assert set(pattern_multiplicity.values()) == {2}
assert all(sign_product(k) == 1 for k in pattern_multiplicity)

constrained_signed_sum_over_32_sigma = sum(p for _, _, p in constrained)
constrained_signed_sum_over_16_distinct_kappa = sum(sign_product(k) for k in pattern_multiplicity)
assert constrained_signed_sum_over_32_sigma == 32
assert constrained_signed_sum_over_16_distinct_kappa == 16

# Adversarial control: unconstrained independent wedge signs.
independent_products = Counter()
independent_signed_sum = 0
for kappas in product((-1, 1), repeat=len(EDGES)):
    p = sign_product(kappas)
    independent_products[p] += 1
    independent_signed_sum += p

assert sum(independent_products.values()) == 1024
assert independent_products == Counter({-1: 512, 1: 512})
assert independent_signed_sum == 0

# Frozen j=1 source-control statement from the prior exact certificate.
# We do not evaluate rho here; for every real rho != 0, rho*(1+rho^2) != 0.
j1_delta2_coefficient = "i/(rho*(1+rho^2))"
j1_delta2_nonzero_for_real_rho_ne_0 = True
assert j1_delta2_nonzero_for_real_rho_ne_0

classification = "SOURCE_J1_K5_ALL_CONTACT_CAUSAL_SIGN_NONCANCELLATION_SCOPED"

result = {
    "classification": classification,
    "k5_vertices": list(VERTICES),
    "k5_edges": [list(e) for e in EDGES],
    "n_edges": len(EDGES),
    "vertex_degrees": {str(k): v for k, v in degrees.items()},
    "constrained": {
        "n_sigma_assignments": len(constrained),
        "n_distinct_kappa_patterns": len(pattern_multiplicity),
        "global_reversal_multiplicity": 2,
        "all_edge_sign_products_plus_one": True,
        "signed_sum_over_32_sigma_assignments": constrained_signed_sum_over_32_sigma,
        "signed_sum_over_16_distinct_kappa_patterns": constrained_signed_sum_over_16_distinct_kappa,
    },
    "unconstrained_independent_kappa_control": {
        "n_patterns": 1024,
        "product_plus_one_count": independent_products[1],
        "product_minus_one_count": independent_products[-1],
        "signed_sum": independent_signed_sum,
    },
    "j1_source_contact_control": {
        "delta2_coefficient": j1_delta2_coefficient,
        "nonzero_for_real_rho_ne_0": j1_delta2_nonzero_for_real_rho_ne_0,
    },
    "formal_all_contact_causal_sign_cancellation": False,
    "claim_ceiling": (
        "Exact causal-sign combinatorics of the formal all-delta'' j=1 contact monomial only. "
        "This does not define the ten-fold distribution product, prove divergence of that product, "
        "or close D7-S2."
    ),
}

print(json.dumps(result, indent=2, sort_keys=True))

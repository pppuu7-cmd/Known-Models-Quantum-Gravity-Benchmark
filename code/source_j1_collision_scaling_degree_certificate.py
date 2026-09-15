#!/usr/bin/env python3
"""Exact arithmetic certificate for the scoped j=1 K5 full-collision scaling ledger.

This script does not prove the microlocal extension theorem. It certifies the finite
arithmetic inputs used by research/SOURCE_J1_FULL_COLLISION_SCALING_EXTENSION_AUDIT_2026-09-15.md.
"""

from math import comb
import json

DIM_G = 6          # dim_R SL(2,C)
DIM_K = 3          # dim_R SU(2)
GAUGE_FIXED_GROUPS = 4
K5_EDGES = 10
J1_EDGE_POLE_ORDER = 3

normal_codimension = GAUGE_FIXED_GROUPS * (DIM_G - DIM_K)
total_pole_order = K5_EDGES * J1_EDGE_POLE_ORDER
scaling_degree = total_pole_order
singular_order = scaling_degree - normal_codimension
radial_measure_power = normal_codimension - 1
radial_integrand_power = radial_measure_power - total_pole_order

# On a fixed tangential slice, the unrestricted normal delta-jet space through
# total derivative order singular_order contains this many multiindices. This is
# bookkeeping only; source symmetries may reduce it substantially.
normal_multiindex_count = comb(normal_codimension + singular_order, singular_order)

assert normal_codimension == 12
assert total_pole_order == 30
assert scaling_degree == 30
assert singular_order == 18
assert radial_measure_power == 11
assert radial_integrand_power == -19
assert normal_multiindex_count == 86493225
assert scaling_degree > normal_codimension
assert radial_integrand_power <= -1

result = {
    "classification": "SOURCE_J1_FULL_COLLISION_SCALING_DEGREE_CERTIFIED_SCOPED",
    "dim_G": DIM_G,
    "dim_K": DIM_K,
    "gauge_fixed_groups": GAUGE_FIXED_GROUPS,
    "normal_codimension": normal_codimension,
    "k5_edges": K5_EDGES,
    "j1_edge_pole_order": J1_EDGE_POLE_ORDER,
    "total_pole_order": total_pole_order,
    "scaling_degree": scaling_degree,
    "singular_order": singular_order,
    "radial_measure_power": radial_measure_power,
    "radial_integrand_power": radial_integrand_power,
    "fixed_tangential_slice_normal_multiindices_leq_18": normal_multiindex_count,
    "absolute_radial_integrability": False,
    "same_scaling_extension_unique_from_off_stratum_data": False,
    "claim_ceiling": (
        "Exact arithmetic bookkeeping only. The distribution-extension statement "
        "uses the separately cited scaling-degree theorem; this certificate does not "
        "close D7-S2 and does not establish a unique source Feynman extension."
    ),
}

print(json.dumps(result, indent=2, sort_keys=True))

#!/usr/bin/env python3
"""Exact premise certificate for the frozen Eq.(4) local-extension existence gate.

This script certifies only the finite arithmetic/logical premises already proved in
repository authority.  The mathematical existence implication itself is supplied by
the cited finite-scaling-degree extension theorem, not by this Python program.
"""

import json

SCALING_DEGREE = 30
NORMAL_CODIM = 12
SINGULAR_ORDER = SCALING_DEGREE - NORMAL_CODIM
RADIAL_MEASURE_POWER = NORMAL_CODIM - 1
TOTAL_POLE_ORDER = 30
RADIAL_INTEGRAND_POWER = RADIAL_MEASURE_POWER - TOTAL_POLE_ORDER
DELTA_N_SCALING_DEGREE = NORMAL_CODIM

N_CONSTRAINED = 16
N_UNCONSTRAINED = 1008
C_CONSTRAINED = 63
C_UNCONSTRAINED = -1
FULL_SIGN_SUM_SHIFT = N_CONSTRAINED * C_CONSTRAINED + N_UNCONSTRAINED * C_UNCONSTRAINED
CAUSAL_SHIFT = N_CONSTRAINED * C_CONSTRAINED

assert SCALING_DEGREE == 30
assert NORMAL_CODIM == 12
assert SINGULAR_ORDER == 18
assert RADIAL_INTEGRAND_POWER == -19
assert DELTA_N_SCALING_DEGREE == 12
assert DELTA_N_SCALING_DEGREE <= SCALING_DEGREE
assert SCALING_DEGREE >= NORMAL_CODIM
assert FULL_SIGN_SUM_SHIFT == 0
assert CAUSAL_SHIFT == 1008
assert CAUSAL_SHIFT != 0

result = {
    "classification": "SOURCE_J1_K5_EQ4_LOCAL_EXTENSION_EXISTS_UNIQUENESS_OPEN_SCOPED",
    "premises": {
        "finite_scaling_degree": True,
        "scaling_degree": SCALING_DEGREE,
        "normal_codimension": NORMAL_CODIM,
        "singular_order": SINGULAR_ORDER,
        "radial_integrand_power": RADIAL_INTEGRAND_POWER,
        "ordinary_absolute_radial_integrability": False,
        "delta_N_scaling_degree": DELTA_N_SCALING_DEGREE,
        "delta_N_within_scaling_ceiling": True,
        "eprl_preserving_counterterm_full_sum_shift": FULL_SIGN_SUM_SHIFT,
        "causal_counterterm_shift": CAUSAL_SHIFT,
        "eprl_sumrule_alone_fixes_extension": False,
    },
    "theorem_application": {
        "finite_scaling_degree_implies_local_extension_exists": True,
        "automatic_uniqueness_condition_sd_lt_codim": SCALING_DEGREE < NORMAL_CODIM,
        "automatic_uniqueness_from_scaling_theorem": False,
        "max_normal_ambiguity_order": SINGULAR_ORDER,
    },
    "scope": {
        "j": 1,
        "channel": "00000",
        "full_collision_conic_patch_away_from_lower_pair_collisions": True,
        "lower_collision_strata_consumed": False,
        "global_vertex_defined": False,
    },
    "claim_ceiling": (
        "Local existence with uniqueness open on the frozen conic full-collision patch only. "
        "This is not a global Eq.(4) definition, not an all-channel/spin theorem, and not D7-S2 closure."
    ),
}

print(json.dumps(result, indent=2, sort_keys=True))

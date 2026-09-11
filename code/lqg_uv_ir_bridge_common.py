#!/usr/bin/env python3
"""Iter283 source-contract facts for the Han 2017 -> 2026 LQG bridge audit."""
import json
from pathlib import Path

SOURCES = {
  "ir_gr": {
    "title": "Einstein Equation from Covariant Loop Quantum Gravity in Semiclassical Continuum Limit",
    "year": 2017,
    "doi": "10.1103/PhysRevD.96.024047",
    "arxiv": "1705.09030",
    "family": "EPRL_FK_COVARIANT_LQG",
    "amplitude_scope": "spinfoam amplitude on refining triangulations",
    "spin_regime": "large_spin",
    "limits": ["triangulation_refinement", "lambda_to_infinity", "delta_to_zero"],
    "running_scale_direction": "mu_to_zero_IR",
    "hierarchy": "lambda >> 1/delta >> 1",
    "target": "continuum_Einstein_equation",
    "normalized_operational_gravity_observable": False
  },
  "uv_fixed_point": {
    "title": "Ultraviolet Fixed Point in Covariant Loop Quantum Gravity",
    "year": 2026,
    "doi": "10.1103/d8s7-jqfl",
    "arxiv": "2602.18665",
    "family": "LORENTZIAN_COVARIANT_LQG_SPINFOAM_STACK",
    "amplitude_scope": "complete LQG amplitude summed over two-complexes partitioned into spinfoam-stack families",
    "spin_regime": "small_spin_UV_condensation",
    "leading_fixed_point_regime": "topological",
    "target": "fundamental_continuum_UV_fixed_point",
    "normalized_operational_gravity_observable": False
  },
  "stack_cutoff": {
    "title": "Summation and triangulation independence of Lorentzian spinfoam amplitudes for all LQG",
    "year": 2026,
    "doi": "10.1103/n76f-31gf",
    "arxiv": "2510.26926",
    "internal_area_cutoff_limit": "cutoff_to_infinity",
    "limit_regime": "topological_SU2_flat_connection_localization",
    "bulk_triangulation_independence_scope": "topologically_trivial_manifolds_after_renormalization"
  }
}

BRIDGE = {
  "explicit_same_realization_identification_between_2017_and_2026_amplitudes": False,
  "explicit_lambda_delta_mu_to_stack_cutoff_parameter_map": False,
  "explicit_small_spin_UV_to_large_spin_semiclassical_trajectory": False,
  "explicit_normalized_observable_transport_across_bridge": False,
  "shared_broad_parent_family": True,
  "both_have_material_positive_endpoints": True
}

def write_json(path, payload):
    p=Path(path); p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n",encoding="utf-8")

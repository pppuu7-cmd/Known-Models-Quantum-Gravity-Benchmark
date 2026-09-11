#!/usr/bin/env python3
"""Iter294 source-contract facts: Finster–Krpoun geometric Einstein derivation."""
import json
from pathlib import Path

CFS_GEOMETRIC_2026 = {
    "title": "A Geometric Derivation of the Einstein Equations from the Causal Action Principle",
    "authors": ["Felix Finster", "Christoph Krpoun"],
    "arxiv": "2607.13871v1",
    "date": "2026-07-15",
    "authority": "public_preprint",
    "lorentzian_four_dimensional_main_theorem": True,
    "einstein_equations_explicit": True,
    "energy_momentum_explicit": True,
    "energy_momentum_symmetric": True,
    "energy_momentum_divergence_free": True,
    "leading_energy_momentum_scaling_delta_power": 2,
    "gravitational_coupling_regularization_length_squared": True,
    "systematic_correction_procedure": True,
    "planck_scale_higher_delta_corrections_listed": True,
    "osculation_torsion_corrections_listed": True,
    "regularizing_vector_corrections_listed": True,
    "modified_measure_corrections_listed": True,
    "explicit_evaluated_beyond_einstein_correction_tensor": False,
    "normalized_beyond_einstein_observable": False,
    "same_domain_comparator_residual": False,
    "propagated_correction_uncertainty": False,
    "corrections_worked_out_in_detail": False,
}

FROZEN_CFS = {
    "status": "BLOCKED_MISSING_REQUIRED_OBJECT",
    "required": "FIRST_EXPLICIT_NORMALIZED_CFS_GRAVITY_CORRECTION_TENSOR_PLUS_COMPARATOR",
    "reopen_condition": "causal-action-derived beyond-continuum gravity observable with fixed state/regularization and robust same-domain comparator-orthogonal residual",
}

def write_json(path, payload):
    p=Path(path); p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(payload, indent=2, sort_keys=True)+"\n", encoding="utf-8")

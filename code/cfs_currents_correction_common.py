#!/usr/bin/env python3
"""Iter289 source-contract facts for CFS current / correction-tensor pathway audit."""
import json
from pathlib import Path

CURRENTS2025 = {
  "title":"Construction of Currents in Causal Fermion Systems",
  "authors":["Felix Finster","Patrick Fischer"],
  "arxiv":"2507.09633",
  "date":"2025-07-13",
  "systematic_linearized_field_equation_formalism":True,
  "explicit_higher_order_quantum_and_discreteness_corrections_in_scope":True,
  "generalizes_to_nonabelian_and_gravitation":True,
  "tensor_hierarchy_increasing_rank":True,
  "rank_one_maxwell_explicit":True,
  "rank_two_einstein_explicit":False,
  "rank_two_einstein_expected":True,
  "higher_rank_new_physics_corrections_explicitly_computed":False,
  "higher_rank_corrections_prospective":True,
  "normalized_gravity_correction_tensor":False,
  "gravity_same_domain_comparator_quotient":False
}

FROZEN_CFS = {
  "status":"BLOCKED_MISSING_REQUIRED_OBJECT",
  "required":"FIRST_EXPLICIT_NORMALIZED_CFS_GRAVITY_CORRECTION_TENSOR_PLUS_COMPARATOR",
  "reopen_condition":"causal-action-derived beyond-continuum gravity observable with fixed state/regularization and robust same-domain comparator-orthogonal residual"
}

def write_json(path,payload):
    p=Path(path); p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n",encoding="utf-8")

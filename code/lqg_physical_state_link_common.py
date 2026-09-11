#!/usr/bin/env python3
"""Iter284 source-contract facts for the EPRL canonical/covariant physical-state link audit."""
import json
from pathlib import Path

YANG2021 = {
  "title":"Relating spin-foam to canonical loop quantum gravity by graphical calculus",
  "journal":"Physical Review D 104, 044025 (2021)",
  "doi":"10.1103/PhysRevD.104.044025",
  "arxiv":"2102.05881",
  "model":"generalized_Euclidean_EPRL",
  "constraint":"Euclidean_Hamiltonian_constraint",
  "physical_state_scope":"certain_spin_network_states",
  "implied_rigging_map":True,
  "constraint_satisfaction":"weak",
  "immmirzi_beta":1.0,
  "full_state_space_certificate":False,
  "lorentzian_same_realization_certificate":False,
  "normalized_gravity_observable":False
}

CHAIN = {
  "iter283_shared_lqg_parent":True,
  "iter283_uv_endpoint":"small_spin_Lorentzian_complete_stack_UV_fixed_point_topological_leading_regime",
  "iter283_gr_endpoint":"large_spin_refinement_continuum_Einstein_equation",
  "iter283_same_realization_transport_ready":False,
  "explicit_2021_to_2017_2026_state_parameter_signature_map":False,
  "explicit_2021_rigging_map_transport_across_uv_ir_chain":False
}

def write_json(path,payload):
    p=Path(path);p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n",encoding="utf-8")

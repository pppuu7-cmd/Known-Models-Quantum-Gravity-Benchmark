#!/usr/bin/env python3
"""Iter286 source-contract facts for Euclidean/Lorentzian EPRL Wick-rotation compatibility audit."""
import json
from pathlib import Path

WICK2021 = {
  "title":"Wick rotation for spin foam quantum gravity",
  "journal":"Physical Review D 104, 126008 (2021)",
  "doi":"10.1103/PhysRevD.104.126008",
  "arxiv":"2106.14672",
  "maps_euclidean_lorentzian_vertex_amplitudes":True,
  "map_type":"analytic_continuation_of_gauge_groups_representations_and_group_elements",
  "euclidean_group":"Spin(4)",
  "lorentzian_group":"SL(2,C)",
  "immmirzi_map":"gamma_real_to_i_gamma",
  "same_real_gamma_identity":False,
  "vertex_level_relation":True,
  "fixed_triangulation_context":True,
  "full_rigging_map_transport":False,
  "complete_stack_transport":False,
  "physical_state_space_transport":False
}

CHAIN = {
  "iter284_model":"generalized_Euclidean_EPRL_beta1_certain_states",
  "iter284_rigging_map_scoped":True,
  "iter283_285_target_signature":"Lorentzian",
  "iter283_285_real_gamma_sector":True,
  "explicit_yang_to_han_state_map":False,
  "explicit_real_gamma_preserving_transport":False,
  "explicit_vertex_to_complete_stack_transport":False
}

def write_json(path,payload):
    p=Path(path); p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n",encoding="utf-8")

#!/usr/bin/env python3
"""Iter287 facts for same-stack UV/entropy/IR transport audit."""
import json
from pathlib import Path

UV = {
  'paper':'Han PRD 114 044040 (2026)',
  'signature':'Lorentzian','complete_amplitude_sum_over_2complexes':True,
  'spinfoam_stack':True,'root_face_couplings':True,'uv_small_spin':True,
  'entropy_paper_explicitly_cited_in_stack_sections':True,
  'gr_ir_large_spin_transport_explicit':False
}
ENTROPY = {
  'paper':'Han PRD 113 084044 (2026)',
  'signature':'Lorentzian','sum_over_family_of_2complexes':True,
  'dynamically_generated_state':True,'coupling_related_to_gamma_for_bh':True,
  'lorentzian_observable_anchor':True,'bh_normalized_after_selection':True,
  'semiclassical_root_complex_direction_reported':True,
  'full_uv_fixed_point_to_gr_observable_flow_computed':False
}
ITER283 = {'uv_endpoint':True,'gr_endpoint':True,'same_realization_transport_ready':False}

def write_json(path,payload):
    p=Path(path); p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n',encoding='utf-8')

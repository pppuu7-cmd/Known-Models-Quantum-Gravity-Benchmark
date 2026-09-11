#!/usr/bin/env python3
"""Iter285 source-contract facts for Lorentzian spinfoam entanglement-entropy observable audit."""
import json, math
from pathlib import Path

HAN_ENTROPY_2026 = {
  "title":"Lorentzian spinfoam gravity path integral and geometrical area-law entanglement entropy",
  "journal":"Physical Review D 113, 084044 (2026)",
  "doi":"10.1103/kbw3-m49g",
  "arxiv":"2510.26925",
  "signature":"Lorentzian",
  "dimension":"3+1",
  "state_origin":"dynamically_generated_by_spinfoam_path_integral_sum_over_family_of_2_complexes",
  "area_spectrum":"Ar=4*pi*gamma*lP^2*a",
  "entropy_large_area":"S=beta*a+c*log(a)+O(1)",
  "beta_positive":True,
  "leading_beta_2complex_independent":True,
  "log_coefficient_may_depend_on_boundary_graph":True,
  "bh_formula_reproduced_with_coupling_gamma_relation":True,
  "bh_gamma_range":[0.0,0.5],
  "parameter_free_bh_normalization":False,
  "explicit_uv_to_gr_observable_transport":False,
  "same_realization_normalized_comparator_error_certificate":False
}

ITER283 = {
  "material_uv_endpoint":True,
  "material_gr_endpoint":True,
  "same_realization_transport_ready":False,
  "missing_parameter_transport":True,
  "missing_normalized_observable_transport":True
}

def bh_ratio(gamma,beta):
    # S/(Ar/lP^2) = beta/(4*pi*gamma); Bekenstein-Hawking requires 1/4.
    return beta/(4.0*math.pi*gamma)

def write_json(path,payload):
    p=Path(path); p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n",encoding="utf-8")

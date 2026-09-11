#!/usr/bin/env python3
import json
out={
 "iteration":359,
 "source":"Ambjorn-Loll arXiv:2604.05641 (2026)",
 "source_defined_strengths":[
  "four-dimensional finite-size collapse in C_dS",
  "UV product-scaling estimate delta=0.54 +/- 0.04",
  "de Sitter volume-profile and fluctuation observables",
  "scale-dependent spectral dimension",
  "quantum Ricci curvature compatible with classical de Sitter at coarse scales"
 ],
 "remaining_source_level_gaps":[
  "separate omega and Gamma critical scaling sufficient to certify diverging de Sitter time extension",
  "sharpened UV exponent/continuum trajectory from additional Monte Carlo data",
  "complete lattice-spacing map with propagated finite-size/discretization/numerical errors on the same trajectory",
  "terminal invariant physical observable plus same-domain comparator/error ledger"
 ],
 "regge_curvature_terminal_substitute":False,
 "spectral_dimension_terminal_substitute":False,
 "family_status":"PARTIAL_SUBFAMILY_ONLY",
 "family_terminal":False,
 "d7_promotion_authorized":False,
 "scope_guard":[
  "NO_ONE_SIGMA_COMPATIBILITY_TO_EXACT_CONTINUUM_CERTIFICATE",
  "NO_PRODUCT_SCALING_TO_SEPARATE_OMEGA_GAMMA_IDENTIFICATION",
  "NO_CHILD_OBSERVABLE_TO_PARENT_TERMINALIZATION",
  "NO_BLOCKED_TO_FAIL_CONVERSION",
  "NO_D7_PROMOTION"
 ]
}
with open("iter359-cdt-scope-guard.json","w") as f: json.dump(out,f,indent=2,sort_keys=True)
print(json.dumps(out,sort_keys=True))

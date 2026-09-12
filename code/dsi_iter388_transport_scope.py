#!/usr/bin/env python3
import json
from pathlib import Path
out={
  'record_type':'transport_scope_guard',
  'source_formula_chain_present':True,
  'table4_numeric_target_present':True,
  'quoted_ns_central':0.9634,
  'quoted_ns_sigma':0.0048,
  'quoted_ks_Mpc_inv':7e-5,
  'cutoff_fractions':[0.04,0.025,0.02],
  'reported_masked_smica_R_TT_approx':0.79,
  'direct_formula_R_TT_is_not_masked_map_R_TT':True,
  'healpix_synfast_mask_beam_pipeline_reproduced':False,
  'raw_planck_map_reproduced':False,
  'raw_author_mc_ensemble_reproduced':False,
  'formal_bayes_factor_reproduced':False,
  'family_terminal':False,
  'd7_promotion_authorized':False,
  'classification':'PASS_SCOPE_GUARD_THEORY_TO_CL_TRANSPORT_ONLY'
}
Path('iter388-transport-scope.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,sort_keys=True))

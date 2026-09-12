#!/usr/bin/env python3
import json
from pathlib import Path

out={
  'record_type':'semantics_guard',
  'empirical_tail_ratio_reproducible':True,
  'bayes_factor_reproduced':False,
  'posterior_odds_reproduced':False,
  'source_prior_model_probabilities_present':False,
  'explicit_marginal_likelihood_normalization_payload_present':False,
  'raw_joint_likelihood_payload_present':False,
  'source_covariance_formula_present':True,
  'raw_covariance_matrix_present':False,
  'd7_promotion_authorized':False,
  'classification':'PASS_SEMANTICS_BOUNDARY_TAIL_RATIO_NOT_PROMOTED_TO_FORMAL_BAYES_FACTOR',
  'scientific_boundary':'A ratio of empirical Monte-Carlo tail probabilities is reproducible from the published table but is not promoted to a formal Bayes factor or posterior odds unless an explicit marginal-evidence construction, model priors/normalization and underlying likelihood payload are supplied.'
}
Path('iter381-semantics-guard.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,sort_keys=True))

#!/usr/bin/env python3
import json
from pathlib import Path

out={
  'record_type':'covariance_scope',
  'cross_correlation_upper_bound_reported':0.15,
  'likelihood_ratio_impact_upper_bound_reported':0.15,
  'reported_cumulative_cl_likelihood_ratio':150.0,
  'covariance_formula_present':True,
  'svd_pseudoinverse_reported':True,
  'raw_covariance_matrix_present':False,
  'raw_mc_realizations_present':False,
  'd7_promotion_authorized':False,
  'classification':'REPORTED_COVARIANCE_STRUCTURE_WITHOUT_RAW_MATRIX_REPRODUCTION',
  'scientific_boundary':'The source describes covariance construction and SVD inversion and reports bounded correlations, but the raw covariance matrix and underlying Monte-Carlo realizations are not present in the current machine-auditable payload.'
}
Path('iter382-covariance-scope.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,sort_keys=True))

#!/usr/bin/env python3
import hashlib, json, pathlib
root=pathlib.Path('build/lqg-iter309-results')
rows=[json.loads(p.read_text()) for p in sorted(root.glob('*.json'))]
expected={'generic_rank','collinear_rank','conormal_nullspace','source_limit_scope','transversality_guard','scope_guard'}
seen={r.get('probe') for r in rows}
if seen!=expected or not all(r.get('pass') is True for r in rows):
    raise SystemExit(f'probe barrier failed: seen={seen}, expected={expected}')
contract=json.load(open('benchmarks/lqg_iter309_distribution_transversality.json'))
out={
  'iteration':309,'family':'LQG_SPINFOAM','classification':contract['frozen_classification_target'],
  'independent_probes':sorted(seen),
  'source_distribution':'Theta=theta(sigma B)+sigma delta^(rho,j)(B), with delta derivatives through order 2j',
  'joint_constraint_shape':'10 B constraints over 12 gauge-fixed noncompact boost directions plus independent spinors',
  'generic_exact_rank':10,'collinear_exact_rank':4,'collinear_left_nullity':6,
  'standard_sufficient_transversality_global':'FAIL_ON_EXPLICIT_COMMON_SUPPORT_STRATUM',
  'joint_multiwedge_epsilon_limit_explicit_in_eq4':False,
  'distributional_extension_or_renormalized_product_nonexistence_proven':False,
  'unregularized_absolute_integrability_restored':False,
  'd7_s2_status':'NOT_CLOSED_DISTRIBUTION_PRODUCT_EXTENSION_REQUIRED',
  'family_terminal':False,'d7_authorized':False,'terminal_count':'1/15',
  'next_required_object':'a source-grounded or newly proved joint ten-wedge distribution product/common-epsilon extension with existence, uniqueness or scheme control, plus compatibility with gluing/normalization; then complete-stack cutoff control and same-realization UV-to-Regge/GR transport'
}
raw=json.dumps(out,indent=2,sort_keys=True)+'\n'
pathlib.Path('build/lqg-iter309-summary.json').write_text(raw)
digest=hashlib.sha256(raw.encode()).hexdigest()
pathlib.Path('build/lqg-iter309-summary.sha256').write_text(digest+'  lqg-iter309-summary.json\n')

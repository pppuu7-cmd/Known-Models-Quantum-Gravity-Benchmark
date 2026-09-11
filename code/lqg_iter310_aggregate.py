#!/usr/bin/env python3
import hashlib, json, pathlib
root=pathlib.Path('build/lqg-iter310-results')
rows=[json.loads(p.read_text()) for p in sorted(root.glob('*.json'))]
expected={'scaling_degree','extension_threshold','counterterm_count','nonzero_coefficient','scope_guard'}
seen={r.get('probe') for r in rows}
if seen!=expected or not all(r.get('pass') is True for r in rows):
    raise SystemExit(f'probe barrier failed: seen={seen}, expected={expected}')
contract=json.load(open('benchmarks/lqg_iter310_scaling_degree_extension.json'))
out={
  'iteration':310,'family':'LQG_SPINFOAM','classification':contract['frozen_classification_target'],
  'independent_probes':sorted(seen),'local_scaling_degree':20,'relative_dimension':12,
  'degree_of_divergence':8,'same_scaling_degree_extension_exists':True,'same_scaling_degree_extension_unique':False,
  'max_local_delta_derivative_order':8,'raw_12d_multiindex_ambiguity_count':125970,
  'source_eq4_alone_fixes_all_extension_coefficients':False,
  'global_causal_vertex_distribution_constructed':False,
  'd7_s2_status':'LOCAL_EXTENSION_EXISTS_BUT_RENORMALIZATION_NORMALIZATION_SCHEME_NOT_FIXED',
  'complete_stack_control_proven':False,'family_terminal':False,'d7_authorized':False,'terminal_count':'1/15',
  'next_required_object':'impose Lorentz/SU2 covariance, boundary permutation/orientation structure, gluing and normalization constraints on the order<=8 local extension ambiguity; test existence and uniqueness of a globally compatible causal-vertex distribution, then complete-stack cutoff control'
}
raw=json.dumps(out,indent=2,sort_keys=True)+'\n'
pathlib.Path('build/lqg-iter310-summary.json').write_text(raw)
digest=hashlib.sha256(raw.encode()).hexdigest()
pathlib.Path('build/lqg-iter310-summary.sha256').write_text(digest+'  lqg-iter310-summary.json\n')

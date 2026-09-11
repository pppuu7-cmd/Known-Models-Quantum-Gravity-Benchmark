#!/usr/bin/env python3
import hashlib, json, pathlib
root=pathlib.Path('build/lqg-iter303-results')
files=sorted(root.glob('*.json'))
rows=[json.loads(x.read_text()) for x in files]
expected={'source_covariance_contract','exact_schur_haar_contraction','mismatched_spin_orthogonality','branch_bilinearity','scope_guard'}
seen={x['probe'] for x in rows}
if len(rows)!=5 or seen!=expected or not all(x['pass'] for x in rows): raise SystemExit(1)
p=json.load(open('benchmarks/lqg_iter303_toller_su2_haar_glue.json'))
out={
  'iteration':303,
  'independent_probes':5,
  'all_probes_pass':True,
  'classification':p['frozen_classification_target'],
  'fixed_spin_toller_su2_haar_half_link_glue_compatible':True,
  'exact_schur_dimensions_tested':[1,2,3,4,5,6],
  'spin_channels_checked':49,
  'mismatched_spin_channels_zero':42,
  'branch_bilinearity_dimensions_tested':[2,3,4,5],
  'fixed_toller_branch_sl2c_representation':False,
  'causal_vertex_finiteness_proven':False,
  'lambda_f_weighted_causal_stack_finiteness_normalization_cutoff_control_proven':False,
  'same_realization_uv_to_causal_regge_gr_transport_proven':False,
  'family_terminal':False,
  'd7_authorized':False,
  'probe_files':[x.name for x in files]
}
payload=json.dumps(out,indent=2,sort_keys=True)+'\n'
pathlib.Path('build/lqg-iter303-summary.json').write_text(payload)
pathlib.Path('build/lqg-iter303-summary.sha256').write_text(hashlib.sha256(payload.encode()).hexdigest()+'\n')

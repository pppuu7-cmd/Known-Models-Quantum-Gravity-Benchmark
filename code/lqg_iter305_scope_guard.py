#!/usr/bin/env python3
import json, pathlib

p=json.load(open('benchmarks/lqg_iter305_toller_tail_local_integrability_split.json'))
c=p['prospectively_frozen_claims']
ok=(c['radial_tail_decay_exponent_strictly_exceeds_kaminski_comparison_exponent'] and
    c['explicit_fixed_branch_identity_neighborhood_singularity_exists'] and
    (not c['radial_tail_control_alone_proves_full_causal_vertex_integrability']) and
    (not c['local_identity_neighborhood_integrability_closed']) and
    (not c['causal_vertex_finiteness_proven']) and
    (not c['causal_vertex_divergence_proven']) and
    (not c['lambda_f_weighted_causal_stack_finiteness_normalization_cutoff_control_proven']) and
    (not c['same_realization_uv_to_causal_regge_gr_transport_proven']) and
    (not c['family_terminal']) and (not c['d7_authorized']))
out={
  'probe':'scope_guard','pass':bool(ok),'iteration':305,
  'tail_subproblem_closed':True,
  'local_identity_integrability_closed':False,
  'causal_vertex_finiteness_proven':False,
  'causal_vertex_divergence_proven':False,
  'family_terminal':False,
  'd7_authorized':False,
  'tested_claim':'tail closure must not be promoted into full vertex, stack, family, or D7 closure'
}
pathlib.Path('build/lqg-iter305').mkdir(parents=True,exist_ok=True)
pathlib.Path('build/lqg-iter305/scope_guard.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if not ok: raise SystemExit(1)

#!/usr/bin/env python3
import json, pathlib
p=json.load(open('benchmarks/lqg_iter303_toller_su2_haar_glue.json'))
c=p['prospectively_frozen_claims']
ok=(c['fixed_spin_toller_half_link_su2_haar_glue_compatibility_target'] and
    c['fixed_toller_branch_is_not_sl2c_representation'] and
    not c['causal_vertex_finiteness_proven'] and
    not c['lambda_f_weighted_causal_stack_finiteness_normalization_cutoff_control_proven'] and
    not c['same_realization_uv_to_causal_regge_gr_transport_proven'] and
    not c['family_terminal'] and not c['d7_authorized'])
out={'probe':'scope_guard','pass':bool(ok),'iteration':303,
     'sl2c_branch_representation':False,
     'causal_vertex_finiteness_proven':False,
     'causal_stack_cutoff_control_proven':False,
     'uv_ir_transport_proven':False,
     'family_terminal':False,'d7_authorized':False}
pathlib.Path('build/lqg-iter303').mkdir(parents=True,exist_ok=True)
pathlib.Path('build/lqg-iter303/scope_guard.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if not ok: raise SystemExit(1)

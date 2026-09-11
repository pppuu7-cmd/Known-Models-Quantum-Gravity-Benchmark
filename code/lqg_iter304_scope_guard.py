#!/usr/bin/env python3
import json, pathlib
p=json.load(open('benchmarks/lqg_iter304_toller_finiteness_transfer.json'))
c=p['prospectively_frozen_claims']
ok=(not c['family_terminal'] and not c['d7_authorized'] and
    not c['lambda_f_weighted_causal_stack_finiteness_normalization_cutoff_control_proven'] and
    not c['same_realization_uv_to_causal_regge_gr_transport_proven'])
out={'probe':'scope_guard','pass':bool(ok),'iteration':304,
     'family_terminal':False,'d7_authorized':False,
     'stack_cutoff_closed':False,'uv_ir_transport_closed':False,
     'forbidden_promotions':['causal_vertex_divergence','family_FAIL','family_PASS','D7 terminal classifier authorization'],
     'tested_claim':'Iter304 remains a scoped theorem-applicability audit only'}
pathlib.Path('build/lqg-iter304').mkdir(parents=True,exist_ok=True)
pathlib.Path('build/lqg-iter304/scope_guard.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if not ok: raise SystemExit(1)

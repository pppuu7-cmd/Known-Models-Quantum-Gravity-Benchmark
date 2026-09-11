#!/usr/bin/env python3
import json, pathlib

p=json.load(open('benchmarks/lqg_iter306_toller_local_power_count.json'))
c=p['prospectively_frozen_claims']
ok=(c['component_level_power_count_risk_established'] and
    (not c['full_intertwiner_contracted_leading_coefficient_nonzero_proven']) and
    (not c['full_causal_vertex_divergence_proven']) and
    (not c['full_causal_vertex_finiteness_proven']) and
    (not c['family_terminal']) and (not c['d7_authorized']))
out={'probe':'scope_guard','pass':bool(ok),'iteration':306,
     'component_level_power_count_risk':True,
     'full_contracted_leading_coefficient_resolved':False,
     'full_causal_vertex_divergence_proven':False,
     'family_terminal':False,'d7_authorized':False,
     'next_decisive_object':'leading fixed-branch K5 tensor after SU(2)-invariant intertwiner/magnetic contraction'}
pathlib.Path('build/lqg-iter306').mkdir(parents=True,exist_ok=True)
pathlib.Path('build/lqg-iter306/scope_guard.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if not ok: raise SystemExit(1)

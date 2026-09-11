#!/usr/bin/env python3
import json, pathlib

p=json.load(open('benchmarks/lqg_iter306_toller_local_power_count.json'))
# Minimal nonzero spin j=1/2 has component-level candidate singular order q=2.
# If s K5 vertices collapse in H3, there are s(s-1)/2 internal edges and
# 3(s-1) relative noncompact dimensions. Superficial degree delta=P-D.
q=2
rows=[]
for s in range(2,6):
    internal_edges=s*(s-1)//2
    P=internal_edges*q
    D=3*(s-1)
    delta=P-D
    status='safe' if delta<0 else ('marginal' if delta==0 else 'risk')
    rows.append({'collapsed_vertices':s,'internal_edges':internal_edges,'singular_power':P,
                 'relative_h3_dimension':D,'superficial_degree':delta,'status':status})
ok=(rows[0]['superficial_degree']==-1 and rows[1]['superficial_degree']==0 and
    rows[2]['superficial_degree']==3 and rows[3]['superficial_degree']==8 and
    p['prospectively_frozen_claims']['uniform_minimal_spin_component_power_count_has_marginal_or_positive_degree_subcollapses'])
out={'probe':'k5_subset_power_count','pass':bool(ok),'iteration':306,
     'uniform_spin':'1/2','component_singularity_order_per_edge':q,'rows':rows,
     'boundary':'component-level superficial degree only; contraction cancellations not tested'}
pathlib.Path('build/lqg-iter306').mkdir(parents=True,exist_ok=True)
pathlib.Path('build/lqg-iter306/k5_subset_power_count.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if not ok: raise SystemExit(1)

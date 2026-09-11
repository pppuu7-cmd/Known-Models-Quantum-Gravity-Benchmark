#!/usr/bin/env python3
import itertools, json, pathlib
p=json.load(open('benchmarks/lqg_iter312_partial_diagonal_causal_sign_cancellation.json'))
nodes=range(5); sectors=[(1,)+tail for tail in itertools.product((-1,1),repeat=4)]
def factor(sig,S):
    z=1
    for a,b in itertools.combinations(S,2): z*=-(sig[a]*sig[b])
    return z
rows=[]; ok=True
expected={3:-16,4:0,5:16}
for s in (3,4,5):
  for S in itertools.combinations(nodes,s):
    total=sum(factor(sig,S) for sig in sectors)
    good=(total==expected[s]); ok &= good
    rows.append({'s':s,'S':list(S),'unit_weight_sum':total,'pass':good})
ok &= p['prospectively_frozen_claims']['unit_weight_triangle_sum_each_of_10']==-16
ok &= p['prospectively_frozen_claims']['unit_weight_k4_sum_each_of_5']==0
ok &= p['prospectively_frozen_claims']['unit_weight_full_k5_sum']==16
out={'probe':'unit_sum_census','pass':bool(ok),'iteration':312,'rows':rows,
     'summary':{'K3':'10/10 sums = -16','K4':'5/5 sums = 0','K5':'sum = +16'}}
pathlib.Path('build/lqg-iter312').mkdir(parents=True,exist_ok=True)
pathlib.Path('build/lqg-iter312/unit_sum_census.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if not ok: raise SystemExit(1)

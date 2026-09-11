#!/usr/bin/env python3
import itertools, json, pathlib
p=json.load(open('benchmarks/lqg_iter312_partial_diagonal_causal_sign_cancellation.json'))
nodes=range(5); sectors=[(1,)+tail for tail in itertools.product((-1,1),repeat=4)]
def cls(sig):
    n=sum(x<0 for x in sig); return min(n,5-n)
def factor(sig,S):
    z=1
    for a,b in itertools.combinations(S,2): z*=-(sig[a]*sig[b])
    return z
expected={3:[-1,-5,-10],4:[1,-3,2],5:[1,5,10]}
rows=[]; ok=True
for s in (3,4,5):
  vals=[]
  for S in itertools.combinations(nodes,s):
    sums=[0,0,0]
    for sig in sectors: sums[cls(sig)]+=factor(sig,S)
    vals.append(sums); ok &= sums==expected[s]
  rows.append({'s':s,'distinct_class_sum_vectors':sorted({tuple(v) for v in vals})})
ok &= p['prospectively_frozen_claims']['triangle_class_sums']==[-1,-5,-10]
ok &= p['prospectively_frozen_claims']['k4_class_sums']==[1,-3,2]
ok &= p['prospectively_frozen_claims']['k5_class_sums']==[1,5,10]
out={'probe':'class_weight_coefficients','pass':bool(ok),'iteration':312,
     'class_order':['0_5','1_4','2_3'],'class_multiplicities':[1,5,10],
     'coefficient_vectors':{'K3':[-1,-5,-10],'K4':[1,-3,2],'K5':[1,5,10]},
     'weighted_forms':{'K3':'-(w0+5 w1+10 w2)','K4':'w0-3 w1+2 w2','K5':'w0+5 w1+10 w2'},
     'rows':rows}
pathlib.Path('build/lqg-iter312').mkdir(parents=True,exist_ok=True)
pathlib.Path('build/lqg-iter312/class_weight_coefficients.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if not ok: raise SystemExit(1)

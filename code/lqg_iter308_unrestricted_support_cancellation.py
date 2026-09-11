#!/usr/bin/env python3
import itertools, json, pathlib

p=json.load(open('benchmarks/lqg_iter308_causal_support_pole_cancellation.json'))
edges=list(itertools.combinations(range(5),2))
pos=neg=0; total=0
for kappas in itertools.product((-1,1),repeat=len(edges)):
    factor=1
    for k in kappas: factor*=(-k)
    total+=factor
    if factor==1: pos+=1
    elif factor==-1: neg+=1
    else: raise SystemExit('non-binary factor')
ok=(len(edges)==10 and pos==512 and neg==512 and total==0 and
    p['prospectively_frozen_claims']['unrestricted_sector_count']==1024 and
    p['prospectively_frozen_claims']['unrestricted_unit_weight_leading_factor_sum']==0)
out={'probe':'unrestricted_support_cancellation','pass':bool(ok),'iteration':308,
     'edge_count':len(edges),'sector_count':2**len(edges),'positive_factor_count':pos,
     'negative_factor_count':neg,'unit_weight_leading_factor_sum':total,
     'identity':'sum_{independent kappa_ab=+/-1} prod_ab(-kappa_ab)=0'}
pathlib.Path('build/lqg-iter308').mkdir(parents=True,exist_ok=True)
pathlib.Path('build/lqg-iter308/unrestricted_support_cancellation.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if not ok: raise SystemExit(1)

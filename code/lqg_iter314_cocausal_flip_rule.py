#!/usr/bin/env python3
import itertools, json, math, pathlib
p=json.load(open('benchmarks/lqg_iter314_cplus_cminus_noncausal_cancellation.json'))
nodes=range(5); edges=list(itertools.combinations(nodes,2)); idx={e:i for i,e in enumerate(edges)}
sectors=[]
for sig in itertools.product((-1,1),repeat=5):
    sectors.append(tuple(sig[a]*sig[b] for a,b in edges))
sectors=set(sectors)
def factor(k,S):
    z=1
    for e in itertools.combinations(S,2): z*= -k[idx[e]]
    return z
rows=[]; ok=True
for s in (3,4,5):
  ratio_expected=(-1)**math.comb(s,2)
  for S in itertools.combinations(nodes,s):
    for k in sectors:
      km=tuple(-x for x in k)
      a=factor(k,S); b=factor(km,S)
      good=(b==ratio_expected*a); ok &= good
  rows.append({'s':s,'relative_factor':ratio_expected})
ok &= p['prospectively_frozen_claims']['cminus_relative_subset_factor']=='(-1)^C(s,2)'
out={'probe':'cocausal_flip_rule','pass':bool(ok),'iteration':314,'rows':rows,
     'interpretation':'C- flips K3 leading sign relative to C+, but leaves K4 and K5 leading sign unchanged'}
pathlib.Path('build/lqg-iter314').mkdir(parents=True,exist_ok=True)
pathlib.Path('build/lqg-iter314/cocausal_flip_rule.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if not ok: raise SystemExit(1)

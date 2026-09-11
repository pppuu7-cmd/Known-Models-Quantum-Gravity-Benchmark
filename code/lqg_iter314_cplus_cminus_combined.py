#!/usr/bin/env python3
import itertools, json, pathlib
p=json.load(open('benchmarks/lqg_iter314_cplus_cminus_noncausal_cancellation.json'))
nodes=range(5); edges=list(itertools.combinations(nodes,2)); idx={e:i for i,e in enumerate(edges)}
cplus=set(tuple(sig[a]*sig[b] for a,b in edges) for sig in itertools.product((-1,1),repeat=5))
cminus={tuple(-x for x in k) for k in cplus}
def factor(k,S):
    z=1
    for e in itertools.combinations(S,2): z*= -k[idx[e]]
    return z
expected={3:0,4:0,5:32}; rows=[]; ok=True
for s in (3,4,5):
  vals=[]
  for S in itertools.combinations(nodes,s):
    total=sum(factor(k,S) for k in cplus)+sum(factor(k,S) for k in cminus)
    vals.append(total); ok &= total==expected[s]
  rows.append({'s':s,'distinct_combined_sums':sorted(set(vals)),'subset_count':len(vals)})
ok &= p['prospectively_frozen_claims']['cplus_plus_cminus_k3_sum']==0 and p['prospectively_frozen_claims']['cplus_plus_cminus_k4_sum']==0 and p['prospectively_frozen_claims']['cplus_plus_cminus_k5_sum']==32
out={'probe':'cplus_cminus_combined','pass':bool(ok),'iteration':314,'rows':rows,
     'conclusion':'C+ plus C- cancels the K3 scalar leading sign and K4 remains zero, but the full K5 leading sign adds constructively to +32'}
pathlib.Path('build/lqg-iter314').mkdir(parents=True,exist_ok=True)
pathlib.Path('build/lqg-iter314/cplus_cminus_combined.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if not ok: raise SystemExit(1)

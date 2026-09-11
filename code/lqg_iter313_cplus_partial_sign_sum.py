#!/usr/bin/env python3
import itertools, json, pathlib
p=json.load(open('benchmarks/lqg_iter313_source_cplus_unit_sum.json'))
nodes=range(5); edges=list(itertools.combinations(nodes,2)); idx={e:i for i,e in enumerate(edges)}
cplus=set()
for sig in itertools.product((-1,1),repeat=5): cplus.add(tuple(sig[a]*sig[b] for a,b in edges))
def factor(k,S):
    z=1
    for e in itertools.combinations(S,2): z*= -k[idx[e]]
    return z
expected={3:-16,4:0,5:16}; rows=[]; ok=True
for s in (3,4,5):
    vals=[]
    for S in itertools.combinations(nodes,s):
        total=sum(factor(k,S) for k in cplus)
        vals.append(total); ok &= total==expected[s]
    rows.append({'s':s,'distinct_sums':sorted(set(vals)),'subset_count':len(vals)})
ok &= p['prospectively_frozen_claims']['cplus_distinct_support_triangle_leading_sum']==-16
ok &= p['prospectively_frozen_claims']['cplus_distinct_support_k4_leading_sum']==0
ok &= p['prospectively_frozen_claims']['cplus_distinct_support_k5_leading_sum']==16
out={'probe':'cplus_partial_sign_sum','pass':bool(ok),'iteration':313,'distinct_Cplus_patterns':len(cplus),'rows':rows,
     'conclusion':'published unit C+ support does not cancel the minimal-spin K3 or K5 scalar leading sign; K4 sign sum cancels'}
pathlib.Path('build/lqg-iter313').mkdir(parents=True,exist_ok=True)
pathlib.Path('build/lqg-iter313/cplus_partial_sign_sum.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if not ok: raise SystemExit(1)

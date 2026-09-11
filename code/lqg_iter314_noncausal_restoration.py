#!/usr/bin/env python3
import itertools, json, pathlib
p=json.load(open('benchmarks/lqg_iter314_cplus_cminus_noncausal_cancellation.json'))
nodes=range(5); edges=list(itertools.combinations(nodes,2)); idx={e:i for i,e in enumerate(edges)}
cplus=set(tuple(sig[a]*sig[b] for a,b in edges) for sig in itertools.product((-1,1),repeat=5))
cminus={tuple(-x for x in k) for k in cplus}
allp=set(itertools.product((-1,1),repeat=len(edges))); non=allp-cplus-cminus
def factor(k,S):
    z=1
    for e in itertools.combinations(S,2): z*= -k[idx[e]]
    return z
expected_non={3:0,4:0,5:-32}; expected_all={3:0,4:0,5:0}; rows=[]; ok=True
for s in (3,4,5):
  nvals=[]; avals=[]
  for S in itertools.combinations(nodes,s):
    ns=sum(factor(k,S) for k in non); alls=sum(factor(k,S) for k in allp)
    nvals.append(ns); avals.append(alls); ok &= ns==expected_non[s] and alls==expected_all[s]
  rows.append({'s':s,'noncausal_distinct_sums':sorted(set(nvals)),'unrestricted_distinct_sums':sorted(set(avals))})
ok &= len(non)==992 and p['prospectively_frozen_claims']['noncausal_k5_sum']==-32 and p['prospectively_frozen_claims']['noncausal_sector_is_required_for_full_k5_scalar_sign_cancellation']
out={'probe':'noncausal_restoration','pass':bool(ok),'iteration':314,'noncausal_patterns':len(non),'rows':rows,
     'K5_identity':'C+ (+16) + C- (+16) + noncausal (-32) = unrestricted EPRL 0',
     'interpretation':'the scalar leading K5 cancellation of the full EPRL wedge-sign expansion uses the noncausal sector'}
pathlib.Path('build/lqg-iter314').mkdir(parents=True,exist_ok=True)
pathlib.Path('build/lqg-iter314/noncausal_restoration.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if not ok: raise SystemExit(1)

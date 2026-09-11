#!/usr/bin/env python3
import itertools, json, pathlib
p=json.load(open('benchmarks/lqg_iter313_source_cplus_unit_sum.json'))
edges=list(itertools.combinations(range(5),2))
cplus=set()
for sig in itertools.product((-1,1),repeat=5):
    cplus.add(tuple(sig[a]*sig[b] for a,b in edges))
cminus={tuple(-x for x in k) for k in cplus}
all_patterns=set(itertools.product((-1,1),repeat=len(edges)))
noncausal=all_patterns-cplus-cminus
ok=(len(cplus)==16 and len(cminus)==16 and len(cplus&cminus)==0 and len(noncausal)==992 and len(all_patterns)==1024 and
    p['prospectively_frozen_claims']['distinct_cplus_wedge_patterns']==16 and
    p['prospectively_frozen_claims']['distinct_cminus_wedge_patterns']==16 and
    p['prospectively_frozen_claims']['cplus_cminus_support_overlap']==0 and
    p['prospectively_frozen_claims']['noncausal_wedge_patterns']==992)
out={'probe':'source_decomposition_count','pass':bool(ok),'iteration':313,
     'all_wedge_sign_patterns':len(all_patterns),'Cplus':len(cplus),'Cminus':len(cminus),'overlap':len(cplus&cminus),'noncausal':len(noncausal),
     'identity':'1024 = 16 C+ + 16 C- + 992 noncausal'}
pathlib.Path('build/lqg-iter313').mkdir(parents=True,exist_ok=True)
pathlib.Path('build/lqg-iter313/source_decomposition_count.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if not ok: raise SystemExit(1)

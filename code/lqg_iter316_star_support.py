#!/usr/bin/env python3
import itertools, json, pathlib
p=json.load(open('benchmarks/lqg_iter316_k4_full_branch_residue.json'))
nodes=range(5); edges=list(itertools.combinations(nodes,2)); idx={e:i for i,e in enumerate(edges)}
cplus=set(tuple(sig[u]*sig[v] for u,v in edges) for sig in itertools.product((-1,1),repeat=5))
rows=[]; ok=True
for S in itertools.combinations(nodes,4):
    SS=set(S); o=next(u for u in nodes if u not in SS)
    external=sorted(tuple(sorted((a,o))) for a in S)
    patterns={tuple(k[idx[e]] for e in external) for k in cplus}
    all4=set(itertools.product((-1,1),repeat=4))
    # For K4, the internal leading sign equals product sigma_a over S,
    # which equals product of four external kappa_ao because sigma_o^4=1.
    identity_ok=True
    for sig in itertools.product((-1,1),repeat=5):
        ext=[sig[e[0]]*sig[e[1]] for e in external]
        internal_sign=1
        for a in S: internal_sign*=sig[a]
        identity_ok &= internal_sign==__import__('math').prod(ext)
    good=(patterns==all4 and identity_ok); ok &= good
    rows.append({'subset':''.join(map(str,S)),'complement':o,'external_edges':[list(e) for e in external],
                 'pattern_count':len(patterns),'all_16_patterns':patterns==all4,'internal_sign_equals_product_external_signs':identity_ok})
ok &= p['prospectively_frozen_claims']['cplus_external_star_patterns_each']==16
out={'probe':'star_support','pass':bool(ok),'iteration':316,'rows':rows,
     'conclusion':'for every K4, C+ restricts bijectively to all 16 sign patterns on the four external star edges'}
pathlib.Path('build/lqg-iter316-guards').mkdir(parents=True,exist_ok=True)
pathlib.Path('build/lqg-iter316-guards/star_support.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if not ok: raise SystemExit(1)

#!/usr/bin/env python3
import itertools, json, pathlib

p=json.load(open('benchmarks/lqg_iter307_minspin_contracted_local_witness.json'))
edges=list(itertools.combinations(range(5),2))
rows=[]; ok=True
# Fix sigma_0=+1 because global reversal is equivalent: 16 inequivalent structures.
for tail in itertools.product((-1,1),repeat=4):
    sig=(1,)+tail
    factors=[]
    for a,b in edges:
        kappa=sig[a]*sig[b]
        factors.append(-kappa)  # j=1/2 leading branch scalar
    prod=1
    for x in factors: prod*=x
    good=(prod==1)
    ok &= good
    rows.append({'sigma':list(sig),'leading_branch_scalar_product':prod})
ok &= (len(edges)==10 and p['prospectively_frozen_claims']['k5_causal_branch_scalar_product_independent_of_sigma'])
out={'probe':'k5_causal_sign_product','pass':bool(ok),'iteration':307,'edge_count':len(edges),
     'identity':'prod_{a<b}[-sigma_a sigma_b]=(+1) because |E|=10 and each sigma_a occurs four times',
     'inequivalent_structures_checked':len(rows),'rows':rows}
pathlib.Path('build/lqg-iter307').mkdir(parents=True,exist_ok=True)
pathlib.Path('build/lqg-iter307/k5_causal_sign_product.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if not ok: raise SystemExit(1)

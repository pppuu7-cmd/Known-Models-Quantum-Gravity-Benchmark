#!/usr/bin/env python3
import itertools, json, pathlib

p=json.load(open('benchmarks/lqg_iter309_distribution_transversality.json'))
nodes=range(5)
edges=[(a,b) for a in nodes for b in nodes if a<b]
edge_index={e:i for i,e in enumerate(edges)}
# With every n_ab=z, dB_ab is the oriented graph-incidence covector in the
# four gauge-fixed z-boost coordinates. Every triangle cycle supplies a left-null relation.
witnesses=[]
for tri in [(0,1,2),(0,1,3),(0,1,4),(0,2,3),(0,2,4),(0,3,4)]:
    a,b,c=tri
    lam=[0]*10
    # oriented cycle a->b, b->c, c->a; stored edges use low<high.
    for u,v,sgn in ((a,b,1),(b,c,1),(c,a,1)):
        e=tuple(sorted((u,v)))
        lam[edge_index[e]] += sgn if u<v else -sgn
    # Verify sum lambda_e*(v_a-v_b)=0 in gauge-fixed node coordinates.
    coeff=[0]*4
    for (u,v),q in zip(edges,lam):
        if q==0: continue
        if u!=0: coeff[u-1]+=q
        if v!=0: coeff[v-1]-=q
    good=(coeff==[0,0,0,0] and any(lam))
    witnesses.append({'triangle':tri,'lambda':lam,'node_coefficients':coeff,'pass':good})
ok=(all(w['pass'] for w in witnesses) and len(witnesses)==6 and p['prospectively_frozen_claims']['collinear_left_nullity']==6)
out={'probe':'conormal_nullspace','pass':bool(ok),'iteration':309,'edge_order':edges,
     'independent_cycle_witness_count':len(witnesses),'witnesses':witnesses,
     'interpretation':'nonzero conormal coefficients can sum to zero, so the standard wavefront/transversality sufficient condition fails at this support point'}
pathlib.Path('build/lqg-iter309').mkdir(parents=True,exist_ok=True)
pathlib.Path('build/lqg-iter309/conormal_nullspace.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if not ok: raise SystemExit(1)

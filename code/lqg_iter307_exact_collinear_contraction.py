#!/usr/bin/env python3
import itertools, json, pathlib
from fractions import Fraction

p=json.load(open('benchmarks/lqg_iter307_minspin_contracted_local_witness.json'))
nodes=range(5)
edges=list(itertools.combinations(nodes,2))
neigh={a:sorted(b for b in nodes if b!=a) for a in nodes}
pos=(0,1,2,3,4)

def eps(i,j):
    return 1 if (i,j)==(0,1) else (-1 if (i,j)==(1,0) else 0)

def intertwiner(a,vals,kind):
    ns=neigh[a]
    if kind=='A': pairs=((0,1),(2,3))
    elif kind=='B': pairs=((0,2),(1,3))
    else: raise ValueError(kind)
    return eps(vals[ns[pairs[0][0]]],vals[ns[pairs[0][1]]])*eps(vals[ns[pairs[1][0]]],vals[ns[pairs[1][1]]])

choices=('A','A','B','A','A')
total=Fraction(0,1)
nonzero_terms=0
for bits in itertools.product((0,1),repeat=len(edges)):
    bmap=dict(zip(edges,bits)); term=Fraction(1,1)
    for a,kind in enumerate(choices):
        vals={b:bmap[tuple(sorted((a,b)))] for b in neigh[a]}
        term*=intertwiner(a,vals,kind)
        if term==0: break
    if term==0: continue
    for (a,b),bit in bmap.items():
        distance=abs(pos[a]-pos[b])
        direction=1 if pos[a]-pos[b]>0 else -1
        sigma_z=1 if bit==0 else -1
        term*=Fraction(direction*sigma_z,distance*distance)
    if term:
        nonzero_terms+=1
        total+=term
unnormalized=total
normalized=total/Fraction(2**5,1)  # each A/B tensor carries factor 1/2
# C^10=[2/(1+gamma^2)]^10.  Strip the common (1+gamma^2)^-10.
full_numerator=normalized*(2**10)
ok=(unnormalized==Fraction(-1,20736) and normalized==Fraction(-1,663552) and
    full_numerator==Fraction(-1,648) and
    p['prospectively_frozen_claims']['unnormalized_collinear_geometric_contraction']=='-1/20736' and
    p['prospectively_frozen_claims']['normalized_collinear_geometric_contraction']=='-1/663552')
out={'probe':'exact_collinear_contraction','pass':bool(ok),'iteration':307,
     'positions_z':list(pos),'node_intertwiners':list(choices),'nonzero_bit_assignments':nonzero_terms,
     'unnormalized_geometric_contraction':str(unnormalized),
     'normalized_geometric_contraction':str(normalized),
     'after_multiplying_2^10_from_C^10':str(full_numerator),
     'full_leading_coefficient':'-1/[648*(1+gamma^2)^10] * delta^-20'}
pathlib.Path('build/lqg-iter307').mkdir(parents=True,exist_ok=True)
pathlib.Path('build/lqg-iter307/exact_collinear_contraction.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if not ok: raise SystemExit(1)

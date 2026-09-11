#!/usr/bin/env python3
import argparse, itertools, json, pathlib
from fractions import Fraction

ap=argparse.ArgumentParser()
ap.add_argument('--triangle',required=True,help='three node digits, e.g. 012')
a=ap.parse_args()
S=tuple(int(x) for x in a.triangle)
if len(S)!=3 or len(set(S))!=3 or any(x not in range(5) for x in S): raise SystemExit('bad triangle')
S=tuple(sorted(S)); tag=''.join(map(str,S))

p=json.load(open('benchmarks/lqg_iter315_k3_contracted_residue_tensor.json'))
nodes=range(5); edges=list(itertools.combinations(nodes,2)); neigh={x:sorted(y for y in nodes if y!=x) for x in nodes}
choices=('A','A','B','A','A')

def eps(i,j):
    return 1 if (i,j)==(0,1) else (-1 if (i,j)==(1,0) else 0)

def I(node, vals):
    ns=neigh[node]; q=[vals[b] for b in ns]
    if choices[node]=='A': return eps(q[0],q[1])*eps(q[2],q[3])
    return eps(q[0],q[2])*eps(q[1],q[3])

SS=set(S)
internal=[e for e in edges if e[0] in SS and e[1] in SS]
external=[e for e in edges if e not in internal]
slots=[(e,u) for e in external for u in e]
pos=neg=nonzero=0; norm2_unnorm=0
# Internal leading Pauli-z kernels are taken with unit nonzero geometric scalar;
# changing internal ray distances/orientation multiplies the whole tensor by a
# common nonzero scalar and cannot change tensor nonvanishing.
for extbits in itertools.product((0,1), repeat=len(slots)):
    local={u:{} for u in nodes}
    for bit,(e,u) in zip(extbits,slots):
        v=e[1] if u==e[0] else e[0]
        local[u][v]=bit
    total=0
    for ibits in itertools.product((0,1), repeat=3):
        loc={u:dict(local[u]) for u in nodes}; term=1
        for (u,v),bit in zip(internal,ibits):
            loc[u][v]=bit; loc[v][u]=bit
            term *= (1 if bit==0 else -1)  # sigma_z diagonal
        for u in nodes:
            term *= I(u,loc[u])
            if term==0: break
        total += term
    if total:
        nonzero+=1; norm2_unnorm+=total*total
        if total>0: pos+=1
        if total<0: neg+=1

# Five normalized intertwiners each contribute 1/2.
norm_factor=Fraction(1,32)
norm2=Fraction(norm2_unnorm,1)*norm_factor*norm_factor

# Source C+ distinct wedge-sign support restricted to the seven external edges.
cplus=set()
for sig in itertools.product((-1,1),repeat=5):
    cplus.add(tuple(sig[u]*sig[v] for u,v in edges))
edge_index={e:i for i,e in enumerate(edges)}
ext_patterns={tuple(k[edge_index[e]] for e in external) for k in cplus}

ok=(len(internal)==3 and len(external)==7 and len(slots)==14 and
    nonzero==128 and pos==64 and neg==64 and norm2==Fraction(1,8) and len(ext_patterns)==16 and
    p['prospectively_frozen_claims']['fixed_sector_internal_k3_residue_tensor_nonzero_for_all_10_triangles'] and
    p['prospectively_frozen_claims']['cplus_restricted_external_branch_pattern_count_each_triangle']==16)
out={
 'probe':'triangle_residue_tensor','triangle':tag,'pass':bool(ok),'iteration':315,
 'internal_edges':[list(e) for e in internal],'external_edges':[list(e) for e in external],
 'open_external_endpoint_indices':len(slots),'tensor_component_count':2**len(slots),
 'nonzero_unnormalized_components':nonzero,'positive_components':pos,'negative_components':neg,
 'unnormalized_squared_norm':norm2_unnorm,'normalized_nonzero_component_magnitude':'1/32',
 'normalized_squared_tensor_norm':str(norm2),'distinct_Cplus_external_branch_patterns':len(ext_patterns),
 'interpretation':'the leading K3 internal residue tensor is not annihilated by the chosen boundary intertwiner contraction; C+ restrictions remain 16 distinct formal external branch monomials'
}
pathlib.Path('build/lqg-iter315').mkdir(parents=True,exist_ok=True)
pathlib.Path(f'build/lqg-iter315/triangle_{tag}.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if not ok: raise SystemExit(1)

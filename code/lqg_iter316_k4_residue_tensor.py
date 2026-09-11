#!/usr/bin/env python3
import argparse, itertools, json, pathlib
from fractions import Fraction

ap=argparse.ArgumentParser(); ap.add_argument('--subset',required=True); a=ap.parse_args()
S=tuple(sorted(int(x) for x in a.subset)); tag=''.join(map(str,S))
if len(S)!=4 or len(set(S))!=4 or any(x not in range(5) for x in S): raise SystemExit('bad K4 subset')
p=json.load(open('benchmarks/lqg_iter316_k4_full_branch_residue.json'))
nodes=range(5); edges=list(itertools.combinations(nodes,2)); neigh={x:sorted(y for y in nodes if y!=x) for x in nodes}; choices=('A','A','B','A','A')

def eps(i,j): return 1 if (i,j)==(0,1) else (-1 if (i,j)==(1,0) else 0)
def I(node,vals):
    q=[vals[b] for b in neigh[node]]
    if choices[node]=='A': return eps(q[0],q[1])*eps(q[2],q[3])
    return eps(q[0],q[2])*eps(q[1],q[3])
SS=set(S); internal=[e for e in edges if e[0] in SS and e[1] in SS]; external=[e for e in edges if e not in internal]
slots=[(e,u) for e in external for u in e]
vals=[]
for extbits in itertools.product((0,1),repeat=len(slots)):
    local={u:{} for u in nodes}
    for bit,(e,u) in zip(extbits,slots):
        v=e[1] if u==e[0] else e[0]; local[u][v]=bit
    total=0
    for ibits in itertools.product((0,1),repeat=len(internal)):
        loc={u:dict(local[u]) for u in nodes}; term=1
        for (u,v),bit in zip(internal,ibits):
            loc[u][v]=bit; loc[v][u]=bit; term *= (1 if bit==0 else -1)
        for u in nodes:
            term*=I(u,loc[u])
            if term==0: break
        total+=term
    if total: vals.append(total)
nonzero=len(vals); pos=sum(v>0 for v in vals); neg=sum(v<0 for v in vals); norm2u=sum(v*v for v in vals)
norm_factor=Fraction(1,32); norm2=Fraction(norm2u)*norm_factor*norm_factor
magnitude=Fraction(abs(vals[0]),32) if vals else Fraction(0)
expected_mag={'0123':Fraction(1,32),'0124':Fraction(1,32),'0134':Fraction(1,16),'0234':Fraction(1,32),'1234':Fraction(1,32)}[tag]
expected_norm={'0123':Fraction(1,64),'0124':Fraction(1,64),'0134':Fraction(1,16),'0234':Fraction(1,64),'1234':Fraction(1,64)}[tag]
# The four external edges form a star from complement node to each K4 node.
complement=next(u for u in nodes if u not in SS)
cplus=set(tuple(sig[u]*sig[v] for u,v in edges) for sig in itertools.product((-1,1),repeat=5)); idx={e:i for i,e in enumerate(edges)}
ext_patterns={tuple(k[idx[e]] for e in external) for k in cplus}
ok=(len(internal)==6 and len(external)==4 and len(slots)==8 and nonzero==16 and pos==8 and neg==8 and
    magnitude==expected_mag and norm2==expected_norm and len(ext_patterns)==16 and
    p['prospectively_frozen_claims']['internal_k4_residue_tensor_nonzero_all_5'])
out={'probe':'k4_residue_tensor','subset':tag,'pass':bool(ok),'iteration':316,'complement_node':complement,
     'internal_edges':[list(e) for e in internal],'external_edges':[list(e) for e in external],
     'open_external_endpoint_indices':len(slots),'tensor_component_count':2**len(slots),
     'nonzero_unnormalized_components':nonzero,'positive_components':pos,'negative_components':neg,
     'unnormalized_component_magnitudes':sorted(set(abs(v) for v in vals)),
     'normalized_component_magnitude':str(magnitude),'normalized_squared_tensor_norm':str(norm2),
     'distinct_Cplus_external_star_patterns':len(ext_patterns)}
pathlib.Path('build/lqg-iter316').mkdir(parents=True,exist_ok=True)
pathlib.Path(f'build/lqg-iter316/k4_{tag}.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if not ok: raise SystemExit(1)

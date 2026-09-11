#!/usr/bin/env python3
import argparse, itertools, json, pathlib
from fractions import Fraction

ap=argparse.ArgumentParser(); ap.add_argument('--subset',required=True); a=ap.parse_args()
S=tuple(sorted(int(x) for x in a.subset)); tag=''.join(map(str,S))
if len(S) not in (3,4) or len(set(S))!=len(S) or any(x not in range(5) for x in S): raise SystemExit('bad subset')
p=json.load(open('benchmarks/lqg_iter317_nested_physical_residue_witness.json'))
nodes=range(5); edges=list(itertools.combinations(nodes,2)); neigh={u:sorted(v for v in nodes if v!=u) for u in nodes}; choices=('A','A','B','A','A')

def eps(i,j): return 1 if (i,j)==(0,1) else (-1 if (i,j)==(1,0) else 0)
def I(u,vals):
    q=[vals[v] for v in neigh[u]]
    if choices[u]=='A': return eps(q[0],q[1])*eps(q[2],q[3])
    return eps(q[0],q[2])*eps(q[1],q[3])

def spin_contraction(direction):
    total=0
    for bits in itertools.product((0,1),repeat=10):
        bm=dict(zip(edges,bits)); term=1
        for u in nodes:
            term*=I(u,{v:bm[tuple(sorted((u,v)))] for v in neigh[u]})
            if term==0: break
        if term==0: continue
        for e,bit in bm.items(): term*=direction[e]*(1 if bit==0 else -1)
        total+=term
    return total

SS=set(S); outside=[u for u in nodes if u not in SS]
# x_cluster=delta*r, r=1..s; x_outside=epsilon*q, q=1..(5-s), delta/epsilon->0.
r={u:i+1 for i,u in enumerate(S)}; q={u:i+1 for i,u in enumerate(outside)}
direction={}; dint=dext=1; ni=ne=0
for e in edges:
    u,v=e
    if u in SS and v in SS:
        diff=r[u]-r[v]; ni+=1; dint*=diff*diff
    else:
        eu=0 if u in SS else q[u]; ev=0 if v in SS else q[v]
        diff=eu-ev; ne+=1; dext*=diff*diff
    if diff==0: raise SystemExit('degenerate hierarchy')
    direction[e]=1 if diff>0 else -1
G=spin_contraction(direction)
# Five normalized intertwiners give 1/32.  C+ has 16 distinct sectors and
# prod_edges[-kappa_ab]=+1 on K5, hence coefficient = 16*(G/32)/(dint*dext).
cplus_pref=Fraction(G,2*dint*dext)
cc_pref=2*cplus_pref
expected_abs=Fraction(1,128) if len(S)==3 else Fraction(1,72)
expected_ni=3 if len(S)==3 else 6; expected_ne=7 if len(S)==3 else 4
expected_scaling='delta^-6 epsilon^-14' if len(S)==3 else 'delta^-12 epsilon^-8'
# Independently enumerate the 16 distinct source C+ sectors and verify their full leading branch scalar.
cplus=set()
for sig in itertools.product((-1,1),repeat=5): cplus.add(tuple(sig[u]*sig[v] for u,v in edges))
branch_products=[]
for k in cplus:
    z=1
    for kap in k: z*=(-kap)
    branch_products.append(z)
ok=(len(cplus)==16 and set(branch_products)=={1} and abs(G)==4 and ni==expected_ni and ne==expected_ne and
    abs(cplus_pref)==expected_abs and cc_pref==2*cplus_pref and cplus_pref!=0 and
    p['prospectively_frozen_claims']['cplus_nested_coefficient_nonzero_all_15'] and
    p['prospectively_frozen_claims']['physical_external_evaluation_exists_for_each_k3_k4_residue'])
out={'probe':'nested_subset_witness','subset':tag,'subset_size':len(S),'pass':bool(ok),'iteration':317,
     'outside_nodes':outside,'cluster_integer_rapidities':r,'outside_epsilon_rapidities':q,
     'internal_edges':ni,'external_edges':ne,'internal_distance_square_product':dint,'external_distance_square_product':dext,
     'unnormalized_oriented_pauli_network_contraction':G,'normalized_pauli_network_contraction':str(Fraction(G,32)),
     'distinct_Cplus_sectors':len(cplus),'Cplus_full_branch_product_values':sorted(set(branch_products)),
     'Cplus_prefactor_without_Cgamma10':str(cplus_pref),'Cplus_plus_Cminus_prefactor_without_Cgamma10':str(cc_pref),
     'scaling':expected_scaling,'Cgamma':'2/(1+gamma^2)',
     'conclusion':'nonzero sequential two-scale asymptotic coefficient; therefore the corresponding internal K3/K4 residue is nonzero for sufficiently small physically consistent nonzero external epsilon'}
pathlib.Path('build/lqg-iter317').mkdir(parents=True,exist_ok=True)
pathlib.Path(f'build/lqg-iter317/subset_{tag}.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if not ok: raise SystemExit(1)

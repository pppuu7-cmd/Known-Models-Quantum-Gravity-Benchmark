#!/usr/bin/env python3
import itertools, json, pathlib

p=json.load(open('benchmarks/lqg_iter307_minspin_contracted_local_witness.json'))

eps=((0,1),(-1,0))
def A(idx):
    i,j,k,l=idx
    return 0.5*eps[i][j]*eps[k][l]
def B(idx):
    i,j,k,l=idx
    return 0.5*eps[i][k]*eps[j][l]
# Fundamental su(2) generators sigma_i/2.  Exact zeros are represented by
# ordinary complex arithmetic; tolerance guards only floating representation.
J=[
 ((0,0.5),(0.5,0)),
 ((0,-0.5j),(0.5j,0)),
 ((0.5,0),(0,-0.5)),
]

def total_action(tensor,gen,out_idx):
    total=0j
    for slot in range(4):
        for q in (0,1):
            src=list(out_idx); src[slot]=q
            total += gen[out_idx[slot]][q]*tensor(tuple(src))
    return total

rows=[]; ok=True
for name,tensor in [('A',A),('B',B)]:
    max_abs=0.0
    for gen in J:
        for idx in itertools.product((0,1),repeat=4):
            max_abs=max(max_abs,abs(total_action(tensor,gen,idx)))
    good=max_abs<1e-14
    ok &= good
    rows.append({'tensor':name,'max_total_su2_generator_residual':max_abs,'pass':good})
ok &= p['prospectively_frozen_claims']['chosen_boundary_tensors_are_su2_invariant']
out={'probe':'intertwiner_invariance','pass':bool(ok),'iteration':307,
     'A':'epsilon_12 epsilon_34 / 2','B':'epsilon_13 epsilon_24 / 2','rows':rows}
pathlib.Path('build/lqg-iter307').mkdir(parents=True,exist_ok=True)
pathlib.Path('build/lqg-iter307/intertwiner_invariance.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if not ok: raise SystemExit(1)

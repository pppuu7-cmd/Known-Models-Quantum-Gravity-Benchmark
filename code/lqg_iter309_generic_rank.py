#!/usr/bin/env python3
import json, pathlib
from fractions import Fraction

p=json.load(open('benchmarks/lqg_iter309_distribution_transversality.json'))
nodes=range(5)
edges=[(a,b) for a in nodes for b in nodes if a<b]
dirs=[(1,0,0),(0,1,0),(0,0,1),(1,1,0),(1,0,1),(0,1,1),(1,-1,0),(1,0,-1),(0,1,-1),(1,1,1)]

def mat_rank(A):
    A=[[Fraction(x) for x in row] for row in A]
    m=len(A); n=len(A[0]); r=0
    for c in range(n):
        pivot=next((i for i in range(r,m) if A[i][c]),None)
        if pivot is None: continue
        A[r],A[pivot]=A[pivot],A[r]
        q=A[r][c]
        A[r]=[x/q for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                q=A[i][c]; A[i]=[x-q*y for x,y in zip(A[i],A[r])]
        r+=1
        if r==m: break
    return r

M=[]
for (a,b),nvec in zip(edges,dirs):
    row=[0]*12
    for node,sgn in ((a,1),(b,-1)):
        if node==0: continue
        base=(node-1)*3
        for k in range(3): row[base+k]+=sgn*nvec[k]
    M.append(row)
rank=mat_rank(M)
ok=(len(edges)==10 and rank==10 and p['prospectively_frozen_claims']['generic_exact_direction_rank']==10)
out={'probe':'generic_rank','pass':bool(ok),'iteration':309,'edge_order':edges,'direction_vectors':dirs,
     'matrix_shape':[10,12],'exact_rank':rank,'interpretation':'full row rank is attainable; obstruction is not generic everywhere'}
pathlib.Path('build/lqg-iter309').mkdir(parents=True,exist_ok=True)
pathlib.Path('build/lqg-iter309/generic_rank.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if not ok: raise SystemExit(1)

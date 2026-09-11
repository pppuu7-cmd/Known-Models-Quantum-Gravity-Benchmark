#!/usr/bin/env python3
import json, pathlib
from fractions import Fraction

p=json.load(open('benchmarks/lqg_iter309_distribution_transversality.json'))
nodes=range(5)
edges=[(a,b) for a in nodes for b in nodes if a<b]

def rref_rank_left_nullity(A):
    A=[[Fraction(x) for x in row] for row in A]
    m=len(A); n=len(A[0]); r=0
    for c in range(n):
        pivot=next((i for i in range(r,m) if A[i][c]),None)
        if pivot is None: continue
        A[r],A[pivot]=A[pivot],A[r]
        q=A[r][c]; A[r]=[x/q for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                q=A[i][c]; A[i]=[x-q*y for x,y in zip(A[i],A[r])]
        r+=1
    return r,m-r

nvec=(0,0,1)
M=[]
for a,b in edges:
    row=[0]*12
    for node,sgn in ((a,1),(b,-1)):
        if node==0: continue
        base=(node-1)*3
        for k in range(3): row[base+k]+=sgn*nvec[k]
    M.append(row)
rank,left_nullity=rref_rank_left_nullity(M)
ok=(rank==4 and left_nullity==6 and p['prospectively_frozen_claims']['collinear_direction_rank']==4 and p['prospectively_frozen_claims']['collinear_left_nullity']==6)
out={'probe':'collinear_rank','pass':bool(ok),'iteration':309,'edge_count':len(edges),
     'all_direction_vectors':[0,0,1],'matrix_shape':[10,12],'exact_rank':rank,'left_nullity':left_nullity,
     'interpretation':'on an admissible common-support collinear spinor configuration the ten B differentials obey six exact linear dependencies'}
pathlib.Path('build/lqg-iter309').mkdir(parents=True,exist_ok=True)
pathlib.Path('build/lqg-iter309/collinear_rank.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if not ok: raise SystemExit(1)

#!/usr/bin/env python3
import hashlib,itertools,json,sys
from fractions import Fraction
V=tuple(range(1,6)); E=tuple((a,b) for a in V for b in V if a<b)

def matrix(root):
    cols=[v for v in V if v!=root]; ci={v:i for i,v in enumerate(cols)}; M=[]
    for a,b in E:
        row=[0]*4
        if a!=root: row[ci[a]]+=1
        if b!=root: row[ci[b]]-=1
        M.append(row)
    return M,cols

def rank(A):
    A=[[Fraction(x) for x in row] for row in A]; m=len(A); n=len(A[0]); r=0
    for c in range(n):
        p=next((i for i in range(r,m) if A[i][c]),None)
        if p is None: continue
        A[r],A[p]=A[p],A[r]; q=A[r][c]; A[r]=[x/q for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                q=A[i][c]; A[i]=[A[i][j]-q*A[r][j] for j in range(n)]
        r+=1
    return r

def transport(root,p):
    M,cols=matrix(root); nr=p[root]; newcols=[v for v in V if v!=nr]
    old_for_new={p[v]:i for i,v in enumerate(cols)}; cp=[old_for_new[v] for v in newcols]
    idx={e:i for i,e in enumerate(E)}; out=[[0]*4 for _ in E]
    for i,(a,b) in enumerate(E):
        pa,pb=p[a],p[b]; e=(pa,pb) if pa<pb else (pb,pa); s=1 if pa<pb else -1
        out[idx[e]]=[s*M[i][j] for j in cp]
    return out,nr

def sha(x): return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
roots={}
for r in V:
    M,_=matrix(r); q=rank(M); roots[str(r)]={'rank':q,'domain_nullity':4-q,'left_nullity':10-q}
M,c=matrix(1); ei={e:i for i,e in enumerate(E)}; ci={v:i for i,v in enumerate(c)}
tri=[[M[ei[e]][ci[v]] for v in (2,3)] for e in ((1,2),(2,3),(1,3))]
expected=[[-1,0],[1,-1],[0,-1]]
s5=True; cases=0
for vals in itertools.permutations(V):
    p={v:vals[v-1] for v in V}
    for r in V:
        T,nr=transport(r,p); s5 = s5 and (T==matrix(nr)[0]); cases+=1
scientific={'gate':'D7_S2_EQ4_FULL_K5_GROUP_TANGENT_PUSHFORWARD_GATE','lane':'RREF_S5','roots':roots,'triangle_match':tri==expected,'triangle_restriction':tri,'s5_exact_transport':s5,'s5_root_transport_cases_checked':cases,'iter466_consistency':all(x['rank']==4 and x['left_nullity']==6 for x in roots.values()),'full_real_sl2c':{'domain_dimension':24,'codomain_dimension':60,'rank':24,'domain_nullity':0,'left_nullity':36}}
valid=all(x=={'rank':4,'domain_nullity':0,'left_nullity':6} for x in roots.values()) and tri==expected and s5 and scientific['iter466_consistency']
out={'classification':'PASS_SCOPED' if valid else 'FAIL_SCOPED','scientific':scientific,'scientific_sha256':sha(scientific)}
json.dump(out,sys.stdout,sort_keys=True,indent=2); print(); sys.exit(0 if valid else 2)

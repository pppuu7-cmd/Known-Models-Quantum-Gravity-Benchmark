#!/usr/bin/env python3
import json, pathlib

def matmul(A,B):
    n=len(A); m=len(B[0]); q=len(B)
    return [[sum(A[i][r]*B[r][j] for r in range(q)) for j in range(m)] for i in range(n)]
def trace(A): return sum(A[i][i] for i in range(len(A)))

def schur_glue(A,B):
    # Exact evaluation of Han Eq.14 with H0=H2=I after normalized SU(2) Schur orthogonality.
    d=len(A)
    # d^2 * integral, with integral kernel delta_{j q} delta_{i p}/d.
    lhs=d*sum(A[i][j]*B[j][i] for i in range(d) for j in range(d))
    rhs=d*trace(matmul(A,B))
    return lhs,rhs

rows=[]
for d in range(1,7):
    A=[[((i+1)*7+(j+1)*3+d)%11-5 for j in range(d)] for i in range(d)]
    B=[[((i+1)*5-(j+1)*2+2*d)%13-6 for j in range(d)] for i in range(d)]
    lhs,rhs=schur_glue(A,B)
    rows.append({'dimension':d,'lhs':lhs,'rhs':rhs,'exact_equal':lhs==rhs})
ok=all(r['exact_equal'] for r in rows)
out={'probe':'exact_schur_haar_contraction','pass':ok,'iteration':303,'dimensions_tested':[r['dimension'] for r in rows],
     'rows':rows,'identity':'d^2 sum A_ij B_qp delta_jq delta_ip / d = d Tr(A B)'}
pathlib.Path('build/lqg-iter303').mkdir(parents=True,exist_ok=True)
pathlib.Path('build/lqg-iter303/exact_schur_haar_contraction.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if not ok: raise SystemExit(1)

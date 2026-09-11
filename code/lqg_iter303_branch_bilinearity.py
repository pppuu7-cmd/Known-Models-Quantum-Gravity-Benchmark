#!/usr/bin/env python3
import json, pathlib

def add(A,B): return [[A[i][j]+B[i][j] for j in range(len(A))] for i in range(len(A))]
def mm(A,B):
    d=len(A); return [[sum(A[i][r]*B[r][j] for r in range(d)) for j in range(d)] for i in range(d)]
def tr(A): return sum(A[i][i] for i in range(len(A)))
def G(A,B): return len(A)*tr(mm(A,B))

rows=[]
for d in (2,3,4,5):
    Ap=[[((i+2)*(j+3)+d)%7-3 for j in range(d)] for i in range(d)]
    Am=[[((2*i-j+3*d)%9)-4 for j in range(d)] for i in range(d)]
    Bp=[[((3*i+2*j+d)%11)-5 for j in range(d)] for i in range(d)]
    Bm=[[((i-4*j+2*d)%13)-6 for j in range(d)] for i in range(d)]
    full=G(add(Ap,Am),add(Bp,Bm))
    branches={s:G(A,B) for s,A,B in [
        ('++',Ap,Bp),('+-',Ap,Bm),('-+',Am,Bp),('--',Am,Bm)]}
    branch_sum=sum(branches.values())
    rows.append({'dimension':d,'full_completed_glue':full,'sum_four_branch_glues':branch_sum,
                 'branch_glues':branches,'exact_equal':full==branch_sum})
ok=all(x['exact_equal'] for x in rows)
out={'probe':'branch_bilinearity','pass':ok,'iteration':303,'rows':rows,
     'interpretation':'SU2 Schur/Haar gluing is bilinear in boundary matrices; branchwise gluing is algebraically defined even though a fixed Toller branch is not an SL2C representation.'}
pathlib.Path('build/lqg-iter303').mkdir(parents=True,exist_ok=True)
pathlib.Path('build/lqg-iter303/branch_bilinearity.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if not ok: raise SystemExit(1)

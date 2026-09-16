#!/usr/bin/env python3
import hashlib,itertools,json,sys
V=tuple(range(1,6)); E=tuple((a,b) for a in V for b in V if a<b)

def matrix(root):
    cols=[v for v in V if v!=root]; ci={v:i for i,v in enumerate(cols)}; M=[]
    for a,b in E:
        row=[0]*4
        if a!=root: row[ci[a]]+=1
        if b!=root: row[ci[b]]-=1
        M.append(row)
    return M

def det(A):
    A=[r[:] for r in A]; n=len(A); sign=1; prev=1
    for k in range(n-1):
        p=next((i for i in range(k,n) if A[i][k]),None)
        if p is None:return 0
        if p!=k:A[k],A[p]=A[p],A[k];sign*=-1
        pivot=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n): A[i][j]=(A[i][j]*pivot-A[i][k]*A[k][j])//prev
        prev=pivot
        for i in range(k+1,n):A[i][k]=0
    return sign*A[-1][-1]

def tree(es):
    parent={v:v for v in V}
    def f(x):
        while parent[x]!=x: parent[x]=parent[parent[x]];x=parent[x]
        return x
    for a,b in es:
        a,b=f(a),f(b)
        if a==b:return False
        parent[b]=a
    return len(es)==4 and len({f(v) for v in V})==1

def sha(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
roots={}; all_dets=[]
for r in V:
    M=matrix(r); ds=[]; count=0
    for inds in itertools.combinations(range(10),4):
        if tree([E[i] for i in inds]):
            count+=1; ds.append(det([M[i] for i in inds]))
    roots[str(r)]={'tree_count':count,'minor_values':sorted(set(ds)),'all_unimodular':all(abs(x)==1 for x in ds),'rank_from_nonzero_4minor':4 if any(ds) else None,'cycle_dimension_from_rank':10-4 if any(ds) else None}
    all_dets.extend(ds)
valid=all(x['tree_count']==125 and x['all_unimodular'] and x['rank_from_nonzero_4minor']==4 and x['cycle_dimension_from_rank']==6 for x in roots.values())
scientific={'gate':'D7_S2_EQ4_FULL_K5_GROUP_TANGENT_PUSHFORWARD_GATE','lane':'TREE_MINORS','roots':roots,'total_tree_root_minors':len(all_dets),'global_minor_values':sorted(set(all_dets)),'iter466_consistency':all(x['rank_from_nonzero_4minor']==4 and x['cycle_dimension_from_rank']==6 for x in roots.values()),'unimodular_tree_coordinate_charts':valid}
out={'classification':'PASS_SCOPED' if valid else 'FAIL_SCOPED','scientific':scientific,'scientific_sha256':sha(scientific)}
json.dump(out,sys.stdout,sort_keys=True,indent=2);print();sys.exit(0 if valid else 2)

#!/usr/bin/env python3
import argparse, itertools, json
from fractions import Fraction

V=5
EDGES=[(i,j) for i in range(V) for j in range(i+1,V)]

def incidence(edges=EDGES, corrupt=None):
    B=[[Fraction(0) for _ in edges] for _ in range(V)]
    for k,(i,j) in enumerate(edges):
        B[i][k]=Fraction(-1)
        B[j][k]=Fraction(1)
    if corrupt is not None:
        i,j=edges[corrupt]
        B[i][corrupt]=Fraction(1)
        B[j][corrupt]=Fraction(1)
    return B

def transpose(A): return [list(x) for x in zip(*A)]

def matmul(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))), Fraction(0)) for j in range(len(B[0]))] for i in range(len(A))]

def det(A):
    A=[row[:] for row in A]; n=len(A); out=Fraction(1)
    for c in range(n):
        p=next((r for r in range(c,n) if A[r][c]),None)
        if p is None: return Fraction(0)
        if p!=c: A[c],A[p]=A[p],A[c]; out=-out
        piv=A[c][c]; out*=piv
        for j in range(c,n): A[c][j]/=piv
        for r in range(c+1,n):
            q=A[r][c]
            if q:
                for j in range(c,n): A[r][j]-=q*A[c][j]
    return out

def rank(A):
    A=[row[:] for row in A]; m=len(A); n=len(A[0]); r=0
    for c in range(n):
        p=next((i for i in range(r,m) if A[i][c]),None)
        if p is None: continue
        A[r],A[p]=A[p],A[r]; piv=A[r][c]
        for j in range(c,n): A[r][j]/=piv
        for i in range(m):
            if i!=r and A[i][c]:
                q=A[i][c]
                for j in range(c,n): A[i][j]-=q*A[r][j]
        r+=1
        if r==m: break
    return r

def inv(A):
    n=len(A); M=[A[i][:]+[Fraction(int(i==j)) for j in range(n)] for i in range(n)]
    for c in range(n):
        p=next((r for r in range(c,n) if M[r][c]),None)
        if p is None: raise ValueError('singular')
        M[c],M[p]=M[p],M[c]; q=M[c][c]
        M[c]=[x/q for x in M[c]]
        for r in range(n):
            if r!=c and M[r][c]:
                q=M[r][c]; M[r]=[M[r][j]-q*M[c][j] for j in range(2*n)]
    return [row[n:] for row in M]

def subcols(A, cols): return [[row[c] for c in cols] for row in A]

def is_tree(edge_indices, edges=EDGES):
    parent=list(range(V))
    def f(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]; x=parent[x]
        return x
    for k in edge_indices:
        a,b=edges[k]; ra,rb=f(a),f(b)
        if ra==rb: return False
        parent[ra]=rb
    return len(edge_indices)==V-1 and len({f(i) for i in range(V)})==1

def cycle_basis(Br, tree):
    tree=list(tree); chords=[e for e in range(10) if e not in tree]
    T=subcols(Br,tree); Ti=inv(T); R=subcols(Br,chords)
    X=matmul(Ti,R)
    C=[[Fraction(0) for _ in range(6)] for __ in range(10)]
    for j,e in enumerate(chords): C[e][j]=Fraction(1)
    for i,e in enumerate(tree):
        for j in range(6): C[e][j]=-X[i][j]
    return C,chords

def determinant6(A): return det(A)

def minor_signature(Br):
    vals=[]; nonzero=0; mismatch=0
    for s in itertools.combinations(range(10),4):
        d=det(subcols(Br,s)); tree=is_tree(s)
        if d: nonzero+=1
        vals.append(abs(d))
        if bool(d)!=tree: mismatch+=1
    return nonzero,mismatch,tuple(sorted(vals))

def permuted_edges(p):
    es=[]
    for a,b in EDGES:
        x,y=p[a],p[b]
        if x>y: x,y=y,x
        es.append((x,y))
    return sorted(es)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--root',type=int,required=True); ap.add_argument('--out',required=True); args=ap.parse_args()
    root=args.root
    B=incidence(); Br=[row for i,row in enumerate(B) if i!=root]
    r=rank(Br); nullity=10-r
    nz,mismatch,sig=minor_signature(Br)
    tree_sets=[s for s in itertools.combinations(range(10),4) if det(subcols(Br,s))]
    dets=[det(subcols(Br,s)) for s in tree_sets]
    canonical=tree_sets[0]; C0,ch0=cycle_basis(Br,canonical)
    kernel_ok=True; integer_ok=True; unimod_ok=True; basis_recon_ok=True
    for t in tree_sets:
        C,ch=cycle_basis(Br,t)
        if any(x for row in matmul(B,C) for x in row): kernel_ok=False
        if any(x.denominator!=1 for row in C for x in row): integer_ok=False
        M=[[C[e][j] for j in range(6)] for e in ch0]
        if matmul(C0,M)!=C: basis_recon_ok=False
        dm=determinant6(M)
        if abs(dm)!=1 or any(x.denominator!=1 for row in M for x in row): unimod_ok=False
    # permutation robustness; relabeling K5 must preserve minor signature
    perm_ok=True
    for p in itertools.permutations(range(V)):
        Bp=incidence(permuted_edges(p)); Brp=[row for i,row in enumerate(Bp) if i!=root]
        nzp,mmp,sigp=minor_signature(Brp)
        if rank(Brp)!=4 or 10-rank(Brp)!=6 or nzp!=125 or mmp!=0 or sigp!=sig:
            perm_ok=False; break
    # controls
    del_edges=EDGES[:-1]; Bd=incidence(del_edges); Brd=[row for i,row in enumerate(Bd) if i!=root]
    deletion_detected=(rank(Brd)==4 and len(del_edges)-rank(Brd)==5)
    dup_edges=EDGES[:-1]+[EDGES[0]]; Bdup=incidence(dup_edges); Brdup=[row for i,row in enumerate(Bdup) if i!=root]
    nzd,mmd,sigd=minor_signature(Brdup)
    duplicate_detected=(mmd>0 or sigd!=sig or nzd!=125)
    Bbad=incidence(corrupt=0); Brbad=[row for i,row in enumerate(Bbad) if i!=root]
    column_sum_bad=sum(Bbad[i][0] for i in range(V))!=0
    bad_root_sigs=[]
    for rr in range(V):
        Brx=[row for i,row in enumerate(Bbad) if i!=rr]
        bad_root_sigs.append((rank(Brx),minor_signature(Brx)[0]))
    corruption_detected=column_sum_bad and len(set(bad_root_sigs))>1
    qualified=(r==4 and nullity==6 and nz==125 and mismatch==0 and all(abs(d)==1 for d in dets)
               and kernel_ok and integer_ok and unimod_ok and basis_recon_ok and perm_ok
               and deletion_detected and duplicate_detected and corruption_detected)
    out={
      'iteration':467,'root':root,'rank':r,'nullity':nullity,'nonzero_maximal_minors':nz,
      'tree_minor_mismatch':mismatch,'all_nonzero_minors_unimodular':all(abs(d)==1 for d in dets),
      'kernel_ok':kernel_ok,'integer_cycle_bases':integer_ok,'cycle_basis_unimodular':unimod_ok,
      'basis_reconstruction_ok':basis_recon_ok,'permutation_invariant':perm_ok,
      'deletion_control_detected':deletion_detected,'duplicate_control_detected':duplicate_detected,
      'corrupt_incidence_control_detected':corruption_detected,'qualified':qualified,
      'classification':'ITER467_EQ4_TANGENT_GROUP_DIFFERENCE_PUSHFORWARD_LATTICE_QUALIFIED_SCOPED' if qualified else 'SCIENTIFIC_FAIL_ITER467_TANGENT_GROUP_PUSHFORWARD_LATTICE',
      'scope':'tangent group-difference integer-lattice/conservation geometry only; no full nonlinear SL(2,C) integral, no convergence theorem, no D7-S2 closure'
    }
    with open(args.out,'w') as f: json.dump(out,f,indent=2,sort_keys=True); f.write('\n')
    print(json.dumps(out,sort_keys=True))
    if not qualified: raise SystemExit(2)
if __name__=='__main__': main()

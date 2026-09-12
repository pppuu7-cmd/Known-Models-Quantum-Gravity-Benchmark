#!/usr/bin/env python3
import argparse, json, math, os, random

R=4; Z=6; M=10

def transpose(A): return [list(x) for x in zip(*A)]
def matmul(A,B): return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def eye(n): return [[1.0 if i==j else 0.0 for j in range(n)] for i in range(n)]
def vecdot(a,b): return sum(x*y for x,y in zip(a,b))
def matvec(A,x): return [sum(a*b for a,b in zip(row,x)) for row in A]

def chol(A):
    n=len(A); L=[[0.0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1):
            v=A[i][j]-sum(L[i][k]*L[j][k] for k in range(j))
            if i==j:
                if v<=0: raise RuntimeError('not SPD')
                L[i][j]=math.sqrt(v)
            else: L[i][j]=v/L[j][j]
    return L

def solve_spd(A,b):
    L=chol(A); n=len(A)
    y=[0.0]*n
    for i in range(n): y[i]=(b[i]-sum(L[i][k]*y[k] for k in range(i)))/L[i][i]
    x=[0.0]*n
    for i in range(n-1,-1,-1): x[i]=(y[i]-sum(L[k][i]*x[k] for k in range(i+1,n)))/L[i][i]
    return x

def logdet_spd(A):
    L=chol(A); return 2.0*sum(math.log(L[i][i]) for i in range(len(A)))

def inv_spd(A):
    n=len(A); E=eye(n); cols=[solve_spd(A,[E[i][j] for i in range(n)]) for j in range(n)]
    return transpose(cols)

def add(A,B): return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def scale(A,c): return [[c*v for v in row] for row in A]

def make_spd(n,rng,span,offdiag):
    L=[[0.0]*n for _ in range(n)]
    for i in range(n):
        expo=-span+2*span*i/max(1,n-1)
        L[i][i]=math.exp(expo)
        for j in range(i): L[i][j]=offdiag*rng.uniform(-0.7,0.7)
    return matmul(L,transpose(L))

def unitdet(A):
    ld=logdet_spd(A); c=math.exp(-ld/len(A)); return scale(A,c)

def block_H(A,C,S):
    Ai=inv_spd(A)
    Ct=transpose(C)
    K=add(S,matmul(matmul(Ct,Ai),C))
    H=[[0.0]*M for _ in range(M)]
    for i in range(R):
        for j in range(R): H[i][j]=A[i][j]
        for j in range(Z): H[i][R+j]=C[i][j]; H[R+j][i]=C[i][j]
    for i in range(Z):
        for j in range(Z): H[R+i][R+j]=K[i][j]
    return H

def sigma_from_H(H,eta):
    d=[1.0]*R+[eta]*Z
    return [[d[i]*H[i][j]*d[j] for j in range(M)] for i in range(M)]

def profile_from_sigma(Sigma,eta,z):
    x=[0.0]*R+[eta*v for v in z]
    q=vecdot(x,solve_spd(Sigma,x))
    return math.exp(-0.5*q)

def relerr(a,b): return abs(a-b)/max(abs(b),1e-300)

def probes():
    out=[]
    for k in range(Z):
        v=[0.0]*Z; v[k]=1.0; out.append(v)
    return out

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--index',type=int,required=True); a=ap.parse_args(); idx=a.index
    if not 0<=idx<24: raise SystemExit('index 0..23')
    rng=random.Random(423000+idx)
    span=[0.15,0.35,0.60,0.90,1.20,1.50][idx%6]
    mix=[0.0,0.15,0.35,0.70][(idx//6)%4]
    A=make_spd(R,rng,0.35+0.05*(idx%3),0.25)
    S=unitdet(make_spd(Z,rng,span,0.30+0.08*(idx%4)))
    C=[[mix*rng.uniform(-0.35,0.35) for _ in range(Z)] for __ in range(R)]
    H=block_H(A,C,S)
    logdetS=logdet_spd(S)
    Si=inv_spd(S)
    zs=probes(); etas=[0.1,0.03,0.01,0.003]
    probe_rows=[]; max_full_err=0.0; max_eta_spread=0.0
    factors=[]
    for p,z in enumerate(zs):
        pred=math.exp(-0.5*vecdot(z,matvec(Si,z)))
        vals=[profile_from_sigma(sigma_from_H(H,e),e,z) for e in etas]
        err=max(relerr(v,pred) for v in vals); spread=(max(vals)-min(vals))/max(abs(pred),1e-300)
        max_full_err=max(max_full_err,err); max_eta_spread=max(max_eta_spread,spread); factors.append(pred)
        probe_rows.append({'probe':p,'prediction':pred,'observed':vals,'max_relative_error':err,'relative_spread_over_eta':spread})
    within_ratio=max(factors)/min(factors)
    passed=(abs(logdetS)<1e-10 and max_full_err<2e-8 and max_eta_spread<2e-7)
    out={
      'iteration':423,'profile_index':idx,'support_rank':R,'cycle_rank':Z,'shape_span':span,'mixing_strength':mix,
      'logdet_S':logdetS,'det_S':math.exp(logdetS),'max_full_vs_schur_relative_error':max_full_err,
      'max_eta_profile_relative_spread':max_eta_spread,'fixed_probe0_factor':factors[0],
      'within_profile_probe_ratio':within_ratio,'pass':passed,'probes':probe_rows,
      'classification':'PASS_UNITDET_VOLUME_FIXED_BUT_CONDITIONAL_SHAPE_REMAINS' if passed else 'FAIL_NUMERICAL_OR_CONSTRUCTION_GATE',
      'scope_guard':'linearized Gaussian K5 surrogate only; residual off-support conditional-metric shape dependence after det(S)=1 does not by itself establish ambiguity of the physical spin-foam amplitude'
    }
    os.makedirs('build/lqg-iter423',exist_ok=True)
    with open(f'build/lqg-iter423/profile_{idx}.json','w') as f: json.dump(out,f,indent=2,sort_keys=True)
    print(json.dumps(out,indent=2,sort_keys=True))
    if not passed: raise SystemExit(2)
if __name__=='__main__': main()

#!/usr/bin/env python3
import argparse, json, math, os, random

RANK=4; CYCLE=6; DIM=10

def transpose(A): return [list(x) for x in zip(*A)]
def matmul(A,B): return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def eye(n): return [[1.0 if i==j else 0.0 for j in range(n)] for i in range(n)]
def matvec(A,x): return [sum(a*b for a,b in zip(row,x)) for row in A]
def vecdot(a,b): return sum(x*y for x,y in zip(a,b))
def add(A,B): return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def diag(v): return [[v[i] if i==j else 0.0 for j in range(len(v))] for i in range(len(v))]
def trace(A): return sum(A[i][i] for i in range(len(A)))

def chol(A):
    n=len(A); L=[[0.0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1):
            v=A[i][j]-sum(L[i][k]*L[j][k] for k in range(j))
            if i==j:
                if v <= 0: raise RuntimeError('not SPD')
                L[i][j]=math.sqrt(v)
            else:
                L[i][j]=v/L[j][j]
    return L

def solve_spd(A,b):
    L=chol(A); n=len(A); y=[0.0]*n
    for i in range(n): y[i]=(b[i]-sum(L[i][k]*y[k] for k in range(i)))/L[i][i]
    x=[0.0]*n
    for i in range(n-1,-1,-1): x[i]=(y[i]-sum(L[k][i]*x[k] for k in range(i+1,n)))/L[i][i]
    return x

def inv_spd(A):
    n=len(A); I=eye(n)
    return transpose([solve_spd(A,[I[i][j] for i in range(n)]) for j in range(n)])

def logdet_spd(A):
    L=chol(A); return 2.0*sum(math.log(L[i][i]) for i in range(len(A)))

def make_spd(n,rng,span=0.4,offdiag=0.2):
    L=[[0.0]*n for _ in range(n)]
    for i in range(n):
        L[i][i]=math.exp(-span+2*span*i/max(1,n-1))
        for j in range(i): L[i][j]=offdiag*rng.uniform(-0.6,0.6)
    return matmul(L,transpose(L))

def givens(n,i,j,theta):
    G=eye(n); c=math.cos(theta); s=math.sin(theta)
    G[i][i]=c; G[j][j]=c; G[i][j]=-s; G[j][i]=s
    return G

def rotation(idx):
    pairs=[(0,1),(1,2),(2,3),(3,4),(4,5),(0,5),(1,4),(0,3)]
    bases=[0.19,0.31,0.43,0.57,0.71,0.83,0.37,0.49]
    Q=eye(CYCLE)
    phase=1.0+0.035*idx
    for k,((i,j),b) in enumerate(zip(pairs,bases)):
        sign=-1.0 if ((idx+k)%3==0) else 1.0
        Q=matmul(givens(CYCLE,i,j,sign*b*phase),Q)
    return Q

def orth_error(Q):
    E=matmul(transpose(Q),Q); I=eye(len(Q))
    return max(abs(E[i][j]-I[i][j]) for i in range(len(Q)) for j in range(len(Q)))

def spectrum_invariant_error(A,B):
    # For real symmetric 6x6 matrices, equality of power sums tr(S^k), k=1..6,
    # determines the characteristic polynomial via Newton identities.
    PA=eye(len(A)); PB=eye(len(B)); worst=0.0
    for _ in range(1,len(A)+1):
        PA=matmul(PA,A); PB=matmul(PB,B)
        a=trace(PA); b=trace(PB)
        worst=max(worst,abs(a-b)/max(1.0,abs(a),abs(b)))
    return worst

def block_H(A,C,S):
    Ai=inv_spd(A); Ct=transpose(C)
    K=add(S,matmul(matmul(Ct,Ai),C))
    H=[[0.0]*DIM for _ in range(DIM)]
    for i in range(RANK):
        for j in range(RANK): H[i][j]=A[i][j]
        for j in range(CYCLE): H[i][RANK+j]=C[i][j]; H[RANK+j][i]=C[i][j]
    for i in range(CYCLE):
        for j in range(CYCLE): H[RANK+i][RANK+j]=K[i][j]
    return H

def sigma(H,eta):
    d=[1.0]*RANK+[eta]*CYCLE
    return [[d[i]*H[i][j]*d[j] for j in range(DIM)] for i in range(DIM)]

def profile_full(H,eta,z):
    x=[0.0]*RANK+[eta*v for v in z]
    q=vecdot(x,solve_spd(sigma(H,eta),x))
    return math.exp(-0.5*q)

def relerr(a,b): return abs(a-b)/max(abs(b),1e-300)

def probes():
    out=[]
    for k in range(CYCLE):
        z=[0.0]*CYCLE; z[k]=1.0; out.append(z)
    return out

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--index',type=int,required=True); args=ap.parse_args(); idx=args.index
    if not 0 <= idx < 24: raise SystemExit('index 0..23')
    rng=random.Random(424000+idx)
    spans=[0.30,0.50,0.75,1.00,1.30,1.65]
    span=spans[idx%6]
    exps=[-span+2*span*i/(CYCLE-1) for i in range(CYCLE)]
    mean=sum(exps)/CYCLE; lambdas=[math.exp(x-mean) for x in exps]
    S0=diag(lambdas)
    Q=rotation(idx); S=matmul(matmul(Q,S0),transpose(Q))
    A=make_spd(RANK,rng,0.30+0.04*(idx%4),0.22)
    mix=[0.0,0.15,0.35,0.65][(idx//6)%4]
    C=[[mix*rng.uniform(-0.35,0.35) for _ in range(CYCLE)] for __ in range(RANK)]
    H=block_H(A,C,S)
    S0i=inv_spd(S0); Si=inv_spd(S)
    etas=[0.1,0.03,0.01,0.003]
    rows=[]; max_full=0.0; max_spread=0.0; max_corot=0.0; orientation_ratios=[]
    for p,z in enumerate(probes()):
        ref=math.exp(-0.5*vecdot(z,matvec(S0i,z)))
        rotated=math.exp(-0.5*vecdot(z,matvec(Si,z)))
        vals=[profile_full(H,e,z) for e in etas]
        ferr=max(relerr(v,rotated) for v in vals)
        spread=(max(vals)-min(vals))/max(abs(rotated),1e-300)
        zrot=matvec(Q,z)
        corot=math.exp(-0.5*vecdot(zrot,matvec(Si,zrot)))
        cerr=relerr(corot,ref)
        oratio=max(ref/rotated,rotated/ref)
        orientation_ratios.append(oratio)
        max_full=max(max_full,ferr); max_spread=max(max_spread,spread); max_corot=max(max_corot,cerr)
        rows.append({'probe':p,'reference_factor':ref,'fixed_probe_rotated_factor':rotated,
                     'orientation_effect_ratio':oratio,'co_rotated_factor':corot,
                     'co_rotation_relative_error':cerr,'full_observed':vals,
                     'max_full_relative_error':ferr,'eta_relative_spread':spread})
    ldet=logdet_spd(S); serr=spectrum_invariant_error(S0,S); oerr=orth_error(Q)
    profile_pass=(abs(ldet)<1e-10 and serr<2e-10 and oerr<2e-12 and
                  max_full<3e-8 and max_spread<3e-7 and max_corot<3e-10)
    effect=max(orientation_ratios)
    out={'iteration':424,'profile_index':idx,'support_rank':RANK,'cycle_rank':CYCLE,
         'spectrum_span':span,'mixing_strength':mix,'logdet_S':ldet,
         'spectrum_power_sum_relative_error':serr,'orthogonality_error':oerr,
         'max_full_vs_schur_relative_error':max_full,'max_eta_profile_relative_spread':max_spread,
         'max_corotation_relative_error':max_corot,'max_fixed_probe_orientation_effect_ratio':effect,
         'orientation_effect_detected':effect>=1.05,'pass':profile_pass,'probes':rows,
         'classification':'PASS_FIXED_SPECTRUM_RELATIVE_ORIENTATION_AUDIT' if profile_pass else 'FAIL_NUMERICAL_OR_CONSTRUCTION_GATE',
         'scope_guard':'Gaussian K5 surrogate only. Fixed-probe orientation dependence is meaningful only if the probe frame is physically identified; exact co-rotation is the basis-change control.'}
    os.makedirs('build/lqg-iter424',exist_ok=True)
    with open(f'build/lqg-iter424/profile_{idx}.json','w') as f: json.dump(out,f,indent=2,sort_keys=True)
    print(json.dumps(out,indent=2,sort_keys=True))
    if not profile_pass: raise SystemExit(2)

if __name__=='__main__': main()

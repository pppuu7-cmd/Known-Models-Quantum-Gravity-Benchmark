#!/usr/bin/env python3
import argparse, json, math, os, random

N=6

def T(A): return [list(x) for x in zip(*A)]
def mm(A,B): return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def eye(n): return [[1.0 if i==j else 0.0 for j in range(n)] for i in range(n)]
def diag(v): return [[v[i] if i==j else 0.0 for j in range(len(v))] for i in range(len(v))]
def add(A,B): return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def tr(A): return sum(A[i][i] for i in range(len(A)))

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

def logdet(A):
    L=chol(A); return 2*sum(math.log(L[i][i]) for i in range(len(A)))

def solve(A,b):
    L=chol(A); n=len(A); y=[0.0]*n
    for i in range(n): y[i]=(b[i]-sum(L[i][k]*y[k] for k in range(i)))/L[i][i]
    x=[0.0]*n
    for i in range(n-1,-1,-1): x[i]=(y[i]-sum(L[k][i]*x[k] for k in range(i+1,n)))/L[i][i]
    return x

def inv(A):
    I=eye(len(A)); return T([solve(A,[I[i][j] for i in range(len(A))]) for j in range(len(A))])

def givens(n,i,j,a):
    G=eye(n); c=math.cos(a); s=math.sin(a)
    G[i][i]=G[j][j]=c; G[i][j]=-s; G[j][i]=s
    return G

def rotation(idx):
    pairs=[(0,1),(1,2),(2,3),(3,4),(4,5),(0,5),(1,4),(0,3)]
    base=[0.17,0.29,0.41,0.53,0.67,0.79,0.37,0.47]
    Q=eye(N); phase=1+0.041*idx
    for k,((i,j),b) in enumerate(zip(pairs,base)):
        a=b*phase*(-1 if (idx+k)%4==0 else 1)
        Q=mm(givens(N,i,j,a),Q)
    return Q

def specerr(A,B):
    PA=eye(N); PB=eye(N); w=0.0
    for _ in range(N):
        PA=mm(PA,A); PB=mm(PB,B)
        a=tr(PA); b=tr(PB); w=max(w,abs(a-b)/max(1.0,abs(a),abs(b)))
    return w

def ensemble_factor(S,W):
    # z~N(0,W): E exp[-1/2 z^T S^{-1} z] = det(I + W S^{-1})^{-1/2}
    M=add(eye(N),mm(W,inv(S)))
    return math.exp(-0.5*logdet(M))

def rel(a,b): return abs(a-b)/max(abs(b),1e-300)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--index',type=int,required=True); a=ap.parse_args(); idx=a.index
    if not 0<=idx<24: raise SystemExit('index 0..23')
    spans=[0.28,0.45,0.65,0.90,1.20,1.55]
    span=spans[idx%6]
    ex=[-span+2*span*i/(N-1) for i in range(N)]; mu=sum(ex)/N
    lam=[math.exp(x-mu) for x in ex]
    S0=diag(lam); Q=rotation(idx); S=mm(mm(Q,S0),T(Q))

    # Four anisotropic physical probe covariances, each normalized to det(W)=1.
    strength=[0.20,0.45,0.80,1.20][(idx//6)%4]
    raw=[-strength+2*strength*i/(N-1) for i in range(N)]
    # permute principal probe directions so lanes do not share one accidental alignment
    shift=idx%N; raw=raw[shift:]+raw[:shift]
    W=diag([math.exp(x-sum(raw)/N) for x in raw])
    Wrot=mm(mm(Q,W),T(Q))
    I=eye(N)

    iso0=ensemble_factor(S0,I); iso1=ensemble_factor(S,I)
    an0=ensemble_factor(S0,W); an1=ensemble_factor(S,W)
    corot=ensemble_factor(S,Wrot)
    iso_err=rel(iso1,iso0); corot_err=rel(corot,an0)
    effect=max(an0/an1,an1/an0)
    se=specerr(S0,S); ld=logdet(S)
    ok=(abs(ld)<1e-10 and se<2e-10 and iso_err<3e-10 and corot_err<3e-10)
    out={
      'iteration':425,'profile_index':idx,'spectrum_span':span,'probe_anisotropy_strength':strength,
      'logdet_S':ld,'spectrum_power_sum_relative_error':se,
      'isotropic_reference_factor':iso0,'isotropic_rotated_factor':iso1,'isotropic_relative_error':iso_err,
      'anisotropic_reference_factor':an0,'anisotropic_fixed_probe_factor':an1,
      'anisotropic_effect_ratio':effect,'anisotropic_effect_detected':effect>=1.03,
      'corotated_probe_factor':corot,'corotation_relative_error':corot_err,
      'pass':ok,
      'classification':'PASS_PROBE_COVARIANCE_ORIENTATION_AUDIT' if ok else 'FAIL_NUMERICAL_OR_CONSTRUCTION_GATE',
      'scope_guard':'Gaussian K5 surrogate only. Isotropic ensemble invariance is spectral; anisotropic sensitivity requires a physically identified probe covariance.'
    }
    os.makedirs('build/lqg-iter425',exist_ok=True)
    with open(f'build/lqg-iter425/profile_{idx}.json','w') as f: json.dump(out,f,indent=2,sort_keys=True)
    print(json.dumps(out,indent=2,sort_keys=True))
    if not ok: raise SystemExit(2)

if __name__=='__main__': main()

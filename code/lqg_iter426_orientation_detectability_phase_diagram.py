#!/usr/bin/env python3
import argparse, json, math, os

N=6

def T(A): return [list(x) for x in zip(*A)]
def mm(A,B): return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def eye(n): return [[1.0 if i==j else 0.0 for j in range(n)] for i in range(n)]
def diag(v): return [[v[i] if i==j else 0.0 for j in range(len(v))] for i in range(len(v))]
def add(A,B): return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

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

def rotation(seed):
    pairs=[(0,1),(1,2),(2,3),(3,4),(4,5),(0,5),(1,4),(0,3),(2,5),(0,4)]
    Q=eye(N)
    for k,(i,j) in enumerate(pairs):
        # deterministic irrational-like phase sweep; seed=0 includes a nontrivial orientation
        a=(0.137*(seed+1)*(k+1)+0.071*(k+2)) % 1.41 - 0.705
        Q=mm(givens(N,i,j,a),Q)
    return Q

def ensemble_factor(S,W):
    # det(I + W S^{-1}) = det((S+W) S^{-1}) = det(S+W)/det(S).
    # I + W S^{-1} is generally non-symmetric when S and W do not commute,
    # so applying Cholesky directly to that product is invalid even though the
    # determinant is positive. Evaluate the exactly equivalent SPD ratio instead.
    return math.exp(-0.5*(logdet(add(S,W))-logdet(S)))

def quantile(xs,q):
    ys=sorted(xs); pos=q*(len(ys)-1); lo=int(math.floor(pos)); hi=int(math.ceil(pos))
    if lo==hi: return ys[lo]
    f=pos-lo; return ys[lo]*(1-f)+ys[hi]*f

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--index',type=int,required=True); a=ap.parse_args(); idx=a.index
    if not 0<=idx<24: raise SystemExit('index 0..23')
    spans=[0.28,0.45,0.65,0.90,1.20,1.55]
    strengths=[0.20,0.45,0.80,1.20]
    span=spans[idx%6]; strength=strengths[idx//6]
    ex=[-span+2*span*i/(N-1) for i in range(N)]; ex=[x-sum(ex)/N for x in ex]
    S0=diag([math.exp(x) for x in ex])
    raw=[-strength+2*strength*i/(N-1) for i in range(N)]; raw=[x-sum(raw)/N for x in raw]
    W=diag([math.exp(x) for x in raw])
    ref=ensemble_factor(S0,W)

    effects=[]; iso_errors=[]; corot_errors=[]
    I=eye(N); iso_ref=ensemble_factor(S0,I)
    for seed in range(96):
        Q=rotation(seed)
        S=mm(mm(Q,S0),T(Q))
        Wrot=mm(mm(Q,W),T(Q))
        f=ensemble_factor(S,W)
        corot=ensemble_factor(S,Wrot)
        iso=ensemble_factor(S,I)
        effects.append(max(ref/f,f/ref))
        corot_errors.append(abs(corot-ref)/max(abs(ref),1e-300))
        iso_errors.append(abs(iso-iso_ref)/max(abs(iso_ref),1e-300))

    p50=quantile(effects,0.50); p90=quantile(effects,0.90); p95=quantile(effects,0.95); mx=max(effects)
    frac=sum(x>=1.03 for x in effects)/len(effects)
    numerical_ok=max(iso_errors)<5e-10 and max(corot_errors)<5e-10
    # Scientific discriminator only; job success is reserved for construction/numerical integrity.
    out={
      'iteration':426,'profile_index':idx,'spectrum_span':span,'probe_anisotropy_strength':strength,
      'orientation_samples':len(effects),'effect_ratio_p50':p50,'effect_ratio_p90':p90,
      'effect_ratio_p95':p95,'effect_ratio_max':mx,'fraction_effect_ge_1p03':frac,
      'max_isotropic_relative_error':max(iso_errors),'max_corotation_relative_error':max(corot_errors),
      'numerical_pass':numerical_ok,
      'scientific_flags':{
        'typical_detectable':p50>=1.03,
        'upper_tail_detectable':p90>=1.03,
        'robustly_detectable':frac>=0.75
      },
      'classification':'PASS_NUMERICAL_PHASE_DIAGRAM_PROFILE' if numerical_ok else 'FAIL_NUMERICAL_OR_CONSTRUCTION_GATE',
      'scope_guard':'Gaussian K5 surrogate. This maps detectability over relative orientations; it does not identify the physical probe covariance or close D7.'
    }
    os.makedirs('build/lqg-iter426',exist_ok=True)
    with open(f'build/lqg-iter426/profile_{idx}.json','w') as f: json.dump(out,f,indent=2,sort_keys=True)
    print(json.dumps(out,indent=2,sort_keys=True))
    if not numerical_ok: raise SystemExit(2)

if __name__=='__main__': main()

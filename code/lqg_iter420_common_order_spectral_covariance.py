#!/usr/bin/env python3
import argparse, json, math, os, random

N=5
EDGES=[(i,j) for i in range(N) for j in range(i+1,N)]
M=len(EDGES)
R=N-1

def transpose(A): return [list(x) for x in zip(*A)]
def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def add(A,B,sa=1.0,sb=1.0):
    return [[sa*A[i][j]+sb*B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def eye(n): return [[1.0 if i==j else 0.0 for j in range(n)] for i in range(n)]
def inv(A):
    n=len(A); X=[row[:] + eye(n)[i] for i,row in enumerate(A)]
    for c in range(n):
        p=max(range(c,n), key=lambda r: abs(X[r][c]))
        X[c],X[p]=X[p],X[c]
        d=X[c][c]
        if abs(d)<1e-14: raise RuntimeError('singular')
        X[c]=[v/d for v in X[c]]
        for r in range(n):
            if r==c: continue
            f=X[r][c]
            X[r]=[X[r][j]-f*X[c][j] for j in range(2*n)]
    return [row[n:] for row in X]
def logdet_spd(A):
    n=len(A); L=[[0.0]*n for _ in range(n)]
    s=0.0
    for i in range(n):
        for j in range(i+1):
            v=A[i][j]-sum(L[i][k]*L[j][k] for k in range(j))
            if i==j:
                if v<=1e-18: raise RuntimeError(f'non-positive pivot {v}')
                L[i][j]=math.sqrt(v); s += 2.0*math.log(L[i][j])
            else:
                L[i][j]=v/L[j][j]
    return s
def linfit(xs,ys):
    mx=sum(xs)/len(xs); my=sum(ys)/len(ys)
    den=sum((x-mx)**2 for x in xs)
    slope=sum((x-mx)*(y-my) for x,y in zip(xs,ys))/den
    intercept=my-slope*mx
    rss=sum((y-(intercept+slope*x))**2 for x,y in zip(xs,ys))
    return slope, math.sqrt(rss/len(xs))

def incidence():
    B=[]
    for i,j in EDGES:
        row=[0.0]*R
        if i<R: row[i]+=1.0
        if j<R: row[j]-=1.0
        B.append(row)
    return B

def spd(n,rng,diag):
    A=[[rng.uniform(-1,1) for _ in range(n)] for __ in range(n)]
    AT=transpose(A); K=matmul(A,AT)
    for i in range(n): K[i][i]+=diag
    return K

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--index',type=int,required=True); a=ap.parse_args()
    idx=a.index
    if not 0 <= idx < 16: raise SystemExit('index 0..15')
    rng=random.Random(420000+idx)
    B=incidence(); BT=transpose(B)
    G=matmul(BT,B); Ps=matmul(matmul(B,inv(G)),BT); Pc=add(eye(M),Ps,1.0,-1.0)
    V=spd(R,rng,0.35+0.05*(idx%4))
    K=spd(M,rng,0.20+0.03*(idx%5))
    S=matmul(matmul(B,V),BT)
    C=matmul(matmul(Pc,K),Pc)
    etas=[10.0**(-x/2.0) for x in range(2,11)]
    xs=[]; ys=[]; rows=[]
    for eta in etas:
        Sigma=add(S,C,1.0,eta*eta)
        ld=logdet_spd(Sigma)
        log_density=-0.5*ld
        x=math.log(1.0/eta)
        xs.append(x); ys.append(log_density); rows.append({'eta':eta,'logdet':ld,'log_density_unnormalized':log_density})
    slope,rmse=linfit(xs,ys)
    tail_slope,tail_rmse=linfit(xs[-5:],ys[-5:])
    passed=abs(slope-6.0)<2e-6 and abs(tail_slope-6.0)<2e-6 and rmse<2e-6
    out={
      'iteration':420,'profile_index':idx,'edge_count':M,'support_rank':R,'cycle_rank':M-R,
      'regulator':'Sigma_eta = B V B^T + eta^2 P_cycle K P_cycle',
      'common_cycle_spectral_order':1.0,'predicted_density_exponent':6.0,
      'fitted_density_exponent':slope,'tail_fitted_density_exponent':tail_slope,
      'fit_rmse':rmse,'tail_fit_rmse':tail_rmse,'pass':passed,'samples':rows,
      'scope_guard':'linearized Gaussian K5 surrogate; tests universality inside a common-order correlated spectral class only; does not identify a source-backed causal EPRL/Toller prescription'
    }
    os.makedirs('build/lqg-iter420',exist_ok=True)
    path=f'build/lqg-iter420/profile_{idx}.json'
    with open(path,'w') as f: json.dump(out,f,indent=2,sort_keys=True)
    print(json.dumps(out,indent=2,sort_keys=True))
    if not passed: raise SystemExit(2)
if __name__=='__main__': main()

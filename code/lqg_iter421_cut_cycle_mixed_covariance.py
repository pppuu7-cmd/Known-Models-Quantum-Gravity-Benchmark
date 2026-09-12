#!/usr/bin/env python3
import argparse, json, math, os, random

N=5
EDGES=[(i,j) for i in range(N) for j in range(i+1,N)]
M=len(EDGES)
R=N-1
Z=M-R

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def norm(a): return math.sqrt(dot(a,a))
def transpose(A): return [list(x) for x in zip(*A)]
def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def linfit(xs,ys):
    mx=sum(xs)/len(xs); my=sum(ys)/len(ys)
    den=sum((x-mx)**2 for x in xs)
    slope=sum((x-mx)*(y-my) for x,y in zip(xs,ys))/den
    intercept=my-slope*mx
    rss=sum((y-(intercept+slope*x))**2 for x,y in zip(xs,ys))
    return slope, math.sqrt(rss/len(xs))
def logdet_spd(A):
    n=len(A); L=[[0.0]*n for _ in range(n)]; s=0.0; minpivot=float('inf')
    scale=max(max(abs(v) for v in row) for row in A)
    tol=max(1e-30,1e-15*scale)
    for i in range(n):
        for j in range(i+1):
            v=A[i][j]-sum(L[i][k]*L[j][k] for k in range(j))
            if i==j:
                if v<=tol: raise RuntimeError(f'non-positive pivot {v} <= {tol}')
                minpivot=min(minpivot,v)
                L[i][j]=math.sqrt(v); s += 2.0*math.log(L[i][j])
            else:
                L[i][j]=v/L[j][j]
    return s,minpivot

def incidence_columns():
    cols=[[0.0]*M for _ in range(R)]
    for e,(i,j) in enumerate(EDGES):
        if i<R: cols[i][e]+=1.0
        if j<R: cols[j][e]-=1.0
    return cols

def orthonormal_basis():
    q=[]
    candidates=incidence_columns()+[[1.0 if i==j else 0.0 for i in range(M)] for j in range(M)]
    for v0 in candidates:
        v=v0[:]
        for u in q:
            c=dot(v,u); v=[x-c*y for x,y in zip(v,u)]
        nv=norm(v)
        if nv>1e-11:
            q.append([x/nv for x in v])
        if len(q)==M: break
    if len(q)!=M: raise RuntimeError('failed orthogonal completion')
    return q[:R],q[R:]

def seed_factor(idx,rng):
    # Deterministic variation of conditioning and cut-cycle coupling.
    span=[0.0,0.35,0.70,1.05][idx%4]
    mix=[0.10,0.30,0.55,0.80,1.05,1.30][(idx//4)%6]
    L=[[0.0]*M for _ in range(M)]
    for i in range(M):
        expo=(-span + 2.0*span*i/(M-1)) if span else 0.0
        L[i][i]=math.exp(expo)
        for j in range(i):
            cross=(i<R and j>=R) or (i>=R and j<R)
            # Lower triangular means only the second cross case is reachable,
            # but retain symmetric semantic labeling.
            amp=mix if cross else 0.35
            L[i][j]=amp*rng.uniform(-0.45,0.45)
    H=matmul(L,transpose(L))
    return H,span,mix

def build_sigma(Q,H,eta):
    scales=[1.0]*R+[eta]*Z
    HD=[[scales[i]*H[i][j]*scales[j] for j in range(M)] for i in range(M)]
    return matmul(matmul(Q,HD),transpose(Q))

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--index',type=int,required=True); a=ap.parse_args()
    idx=a.index
    if not 0 <= idx < 24: raise SystemExit('index 0..23')
    rng=random.Random(421000+idx)
    qc,qz=orthonormal_basis()
    # Q is 10x10 with basis vectors as columns.
    Q=transpose(qc+qz)
    H,span,mix=seed_factor(idx,rng)
    etas=[10.0**(-x/2.0) for x in range(2,11)]
    xs=[]; ydens=[]; yld=[]; rows=[]
    all_spd=True
    for eta in etas:
        Sigma=build_sigma(Q,H,eta)
        try:
            ld,minpivot=logdet_spd(Sigma)
        except RuntimeError:
            all_spd=False
            raise
        x=math.log(1.0/eta); dens=-0.5*ld
        xs.append(x); ydens.append(dens); yld.append(ld)
        rows.append({'eta':eta,'logdet':ld,'log_density_unnormalized':dens,'min_cholesky_pivot':minpivot})
    p,prmse=linfit(xs,ydens); pt,ptrmse=linfit(xs[-5:],ydens[-5:])
    lds,ldrmse=linfit(xs,yld); ldst,ldtrmse=linfit(xs[-5:],yld[-5:])
    det_exp=-lds; det_exp_tail=-ldst
    passed=(all_spd and abs(p-6.0)<2e-5 and abs(pt-6.0)<2e-5
            and abs(det_exp-12.0)<4e-5 and abs(det_exp_tail-12.0)<4e-5)
    out={
      'iteration':421,'profile_index':idx,'edge_count':M,'support_rank':R,'cycle_rank':Z,
      'construction':'Sigma_eta = Q D_eta H D_eta Q^T, D_eta=diag(I4, eta I6)',
      'conditioning_span_parameter':span,'cut_cycle_mixing_parameter':mix,
      'predicted_density_exponent':6.0,'predicted_determinant_exponent':12.0,
      'fitted_density_exponent':p,'tail_fitted_density_exponent':pt,
      'fitted_determinant_exponent':det_exp,'tail_fitted_determinant_exponent':det_exp_tail,
      'fit_rmse':prmse,'tail_fit_rmse':ptrmse,'logdet_fit_rmse':ldrmse,'tail_logdet_fit_rmse':ldtrmse,
      'all_samples_spd':all_spd,'pass':passed,'samples':rows,
      'scope_guard':'linearized Gaussian K5 surrogate; broad mixed cut/cycle common-order congruence class only; does not derive a source-backed causal EPRL/Toller i-epsilon prescription and does not close D7'
    }
    os.makedirs('build/lqg-iter421',exist_ok=True)
    path=f'build/lqg-iter421/profile_{idx}.json'
    with open(path,'w') as f: json.dump(out,f,indent=2,sort_keys=True)
    print(json.dumps(out,indent=2,sort_keys=True))
    if not passed: raise SystemExit(2)
if __name__=='__main__': main()

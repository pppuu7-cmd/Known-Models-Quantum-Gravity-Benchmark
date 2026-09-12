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
        if nv>1e-11: q.append([x/nv for x in v])
        if len(q)==M: break
    if len(q)!=M: raise RuntimeError('failed orthogonal completion')
    return q[:R],q[R:]

def seed_factor(idx,rng):
    span=[0.0,0.35,0.70,1.05][idx%4]
    mix=[0.10,0.30,0.55,0.80,1.05,1.30][(idx//4)%6]
    # Add a frozen profile-volume scale so the finite coefficient is deliberately nontrivial.
    volume_scale=[0.70,0.85,1.00,1.20,1.45,1.75][(idx//4)%6]
    L=[[0.0]*M for _ in range(M)]
    for i in range(M):
        expo=(-span + 2.0*span*i/(M-1)) if span else 0.0
        L[i][i]=math.sqrt(volume_scale)*math.exp(expo)
        for j in range(i):
            cross=(i<R and j>=R) or (i>=R and j<R)
            amp=mix if cross else 0.35
            L[i][j]=math.sqrt(volume_scale)*amp*rng.uniform(-0.45,0.45)
    H=matmul(L,transpose(L))
    return H,span,mix,volume_scale

def build_sigma(Q,H,eta):
    scales=[1.0]*R+[eta]*Z
    HD=[[scales[i]*H[i][j]*scales[j] for j in range(M)] for i in range(M)]
    return matmul(matmul(Q,HD),transpose(Q))

def rescale_matrix(H,scale):
    return [[v*scale for v in row] for row in H]

def relerr(a,b): return abs(a-b)/max(abs(b),1e-300)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--index',type=int,required=True); a=ap.parse_args()
    idx=a.index
    if not 0 <= idx < 24: raise SystemExit('index 0..23')
    rng=random.Random(422000+idx)
    qc,qz=orthonormal_basis(); Q=transpose(qc+qz)
    H,span,mix,volume_scale=seed_factor(idx,rng)
    logdetH,_=logdet_spd(H)
    predicted=math.exp(-0.5*logdetH)
    # Scalar c makes det(c H)=1 in dimension M.
    c=math.exp(-logdetH/M)
    Hbar=rescale_matrix(H,c)
    logdetHbar,_=logdet_spd(Hbar)
    predicted_bar=math.exp(-0.5*logdetHbar)
    etas=[10.0**(-x/2.0) for x in range(2,11)]
    raw=[]; ctl=[]; rows=[]; all_spd=True
    for eta in etas:
        try:
            ld,piv=logdet_spd(build_sigma(Q,H,eta))
            ldb,pivb=logdet_spd(build_sigma(Q,Hbar,eta))
        except RuntimeError:
            all_spd=False
            raise
        # Compute in log form to suppress overflow/underflow and expose exact finite part.
        rr=math.exp(Z*math.log(eta)-0.5*ld)
        rb=math.exp(Z*math.log(eta)-0.5*ldb)
        raw.append(rr); ctl.append(rb)
        rows.append({'eta':eta,'raw_renormalized_factor':rr,'unitdet_control_factor':rb,
                     'raw_min_cholesky_pivot':piv,'control_min_cholesky_pivot':pivb})
    raw_err=max(relerr(v,predicted) for v in raw)
    raw_spread=(max(raw)-min(raw))/max(abs(predicted),1e-300)
    ctl_err=max(relerr(v,1.0) for v in ctl)
    ctl_spread=max(ctl)-min(ctl)
    passed=(all_spd and raw_err<1e-6 and raw_spread<1e-6 and ctl_err<1e-6 and ctl_spread<1e-6)
    out={
      'iteration':422,'profile_index':idx,'edge_count':M,'support_rank':R,'cycle_rank':Z,
      'construction':'Sigma_eta = Q D_eta H D_eta Q^T; finite factor eta^6 det(Sigma_eta)^(-1/2)',
      'conditioning_span_parameter':span,'cut_cycle_mixing_parameter':mix,'seed_volume_scale':volume_scale,
      'logdet_H':logdetH,'predicted_raw_finite_factor':predicted,
      'observed_raw_factor_min':min(raw),'observed_raw_factor_max':max(raw),
      'max_relative_error_raw_factor':raw_err,'relative_spread_over_eta':raw_spread,
      'logdet_unitdet_H':logdetHbar,'predicted_unitdet_factor':predicted_bar,
      'observed_unitdet_factor_min':min(ctl),'observed_unitdet_factor_max':max(ctl),
      'max_relative_error_unitdet_control':ctl_err,'unitdet_spread_over_eta':ctl_spread,
      'all_samples_spd':all_spd,'pass':passed,'samples':rows,
      'scope_guard':'linearized Gaussian K5 surrogate only; finite-part ambiguity within the common-order mixed covariance regulator class; no physical EPRL/Toller prescription is derived'
    }
    os.makedirs('build/lqg-iter422',exist_ok=True)
    path=f'build/lqg-iter422/profile_{idx}.json'
    with open(path,'w') as f: json.dump(out,f,indent=2,sort_keys=True)
    print(json.dumps(out,indent=2,sort_keys=True))
    if not passed: raise SystemExit(2)
if __name__=='__main__': main()

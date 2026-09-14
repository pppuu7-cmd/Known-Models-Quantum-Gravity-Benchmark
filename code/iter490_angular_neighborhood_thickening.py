#!/usr/bin/env python3
import argparse, itertools, json, math, os
import numpy as np
import iter486_shared_node_haar_escape as base
import iter488_kak_high_precision_revalidation as hp

EPS=[0.0025,0.005,0.01,0.02]
RHOS=base.RHOS
CENTER={
 '0to5':[4.0013215485181615,4.000662592689377,4.001415012139243,4.000286533668415],
 '1to4':[4.001427390393364,4.000445747952862,3.999775078860818,3.9998298869259363],
 '2to3':[3.9991928877857013,3.999683838247393,3.99996834238084,4.000166577259772],
}


def rx(t):
    c=np.cos(t/2); s=np.sin(t/2)
    return np.array([[c,-1j*s],[-1j*s,c]],dtype=np.complex128)
def ry(t):
    c=np.cos(t/2); s=np.sin(t/2)
    return np.array([[c,-s],[s,c]],dtype=np.complex128)
def rz(t):
    return np.diag([np.exp(-.5j*t),np.exp(.5j*t)]).astype(np.complex128)

def vec20(radius_index,sample):
    rng=np.random.default_rng(490000+1000*radius_index+sample)
    return rng.choice([-1.0,1.0],20) if sample<8 else rng.uniform(-1.0,1.0,20)

def perturb(gs,v,eps):
    out=[g.copy() for g in gs]
    for a in range(1,5):
        q=v[(a-1)*5:a*5]*eps
        L=rx(q[0])@ry(q[1])@rz(q[2]); R=rx(q[3])@ry(q[4])
        out[a]=L@out[a]@R
    return out

def flatten(g):
    return np.r_[g.real.ravel(),g.imag.ravel()]

def chart_ranks():
    gs=base.escaped_nodes('C',4,10.0); h=1e-7; ranks=[]
    for a in range(1,5):
        cols=[]
        for j in range(5):
            v=np.zeros(20); v[(a-1)*5+j]=1.0
            gp=perturb(gs,v,h)[a]
            cols.append((flatten(gp)-flatten(gs[a]))/h)
        M=np.column_stack(cols); s=np.linalg.svd(M,compute_uv=False)
        tol=max(s[0]*1e-7,1e-10); ranks.append(int(np.sum(s>tol)))
    return ranks

def high_precision_recon(h):
    return float(hp.mp_kak(h)[0])

def sample_eval(causal,v,eps):
    sig=base.SIGMAS[causal]; ts=[base.intertwiner(i) for i in range(3)]
    path=base.contraction_path(ts); channels=list(itertools.product(range(3),repeat=5))
    logH=[]; logC={i:[] for i in range(len(RHOS))}; cyclemax=0.; kak_double=0.; kak_hp=0.; addmax=0.; allpos=True
    for R in base.R_GRID:
        gs=perturb(base.escaped_nodes('C',4,float(R)),v,eps); rs=base.relatives(gs)
        cyclemax=max(cyclemax,base.cycle_residual(rs)); lh,_=base.measure_log(gs,4); logH.append(lh)
        for ir,rho in enumerate(RHOS):
            mats,ln,add,kres=base.edge_data(rs,rho,sig); addmax=max(addmax,add); kak_double=max(kak_double,kres)
            if kres>=base.KAK_TOL:
                for hmat in rs.values(): kak_hp=max(kak_hp,high_precision_recon(hmat))
            vals=np.asarray([base.contract(ch,ts,mats,path) for ch in channels],dtype=np.complex128)
            m=float(np.max(np.abs(vals))) if np.all(np.isfinite(vals)) else float('nan')
            allpos=allpos and bool(np.isfinite(m) and m>0)
            logC[ir].append(ln+math.log(m) if m>0 and np.isfinite(m) else float('nan'))
    hs=base.slope(base.R_GRID[-3:],logH[-3:]); results=[]; bookmax=0.
    for ir,rho in enumerate(RHOS):
        le=[logC[ir][k]+logH[k] for k in range(4)]
        ns=base.slope(base.R_GRID[-3:],logC[ir][-3:]); ac=base.slope(base.R_GRID[-3:],le[-3:]); early=base.slope(base.R_GRID[:3],le[:3]); drift=abs(ac-early); book=abs((ac-ns)-hs); bookmax=max(bookmax,book)
        results.append({'rho':float(rho),'actual_slope':ac,'slope_drift':drift,'nondecay':bool(ac>=0 and drift<=0.05),'robust':bool(ac>=1.0 and drift<=0.05)})
    kak_ok=(kak_double<base.KAK_TOL) or (kak_hp>0 and kak_hp<base.KAK_TOL)
    controls={'cycle':cyclemax<1e-8,'kak_two_tier':bool(kak_ok),'finite_positive':bool(allpos),'haar_slope':abs(hs-8.0)<0.05,'haar_bookkeeping':bookmax<1e-8,'source_additive':addmax<1e-9}
    return {'results':results,'controls':controls,'cycle_max':cyclemax,'kak_double_max':kak_double,'kak_hp_max_if_used':kak_hp,'haar_slope':hs,'bookkeeping_max':bookmax,'additive_max':addmax}

def evaluate(causal,radius_index):
    eps=EPS[radius_index]; ranks=chart_ranks(); center=sample_eval(causal,np.zeros(20),0.0)
    center_slopes=[r['actual_slope'] for r in center['results']]; center_reg=max(abs(a-b) for a,b in zip(center_slopes,CENTER[causal]))
    samples=[]
    for i in range(16): samples.append(sample_eval(causal,vec20(radius_index,i),eps))
    valid=all(r==5 for r in ranks) and center_reg<5e-3 and all(all(s['controls'].values()) for s in samples) and all(center['controls'].values())
    all_nondecay=valid and all(r['nondecay'] for s in samples for r in s['results'])
    all_robust=valid and all(r['robust'] for s in samples for r in s['results'])
    if not valid: cls='INFRASTRUCTURE_OR_NUMERICAL_FAIL_ITER490'
    elif all_robust: cls='ITER490_SAMPLED_ROBUST_THICKENING_LANE'
    elif all_nondecay: cls='ITER490_SAMPLED_NONDECAY_THICKENING_LANE'
    else: cls='SCIENTIFIC_FAIL_ITER490_ANGULAR_THICKENING'
    mins=min(r['actual_slope'] for s in samples for r in s['results']); maxdr=max(r['slope_drift'] for s in samples for r in s['results'])
    return {'iteration':490,'causal':causal,'eps':eps,'radius_index':radius_index,'chart_ranks':ranks,'center_regression_max_abs':center_reg,'valid':valid,'classification':cls,'all_sampled_nondecay':all_nondecay,'all_sampled_robust':all_robust,'sampled_min_actual_slope':mins,'sampled_max_slope_drift':maxdr,'center':center,'samples':samples,'scope':'finite deterministic sampled robustness in a locally full-rank 20-D angular chart only; not a uniform-neighborhood or Haar-divergence theorem'}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--causal',required=True,choices=base.CAUSALS); ap.add_argument('--radius-index',required=True,type=int,choices=range(4)); ap.add_argument('--out',required=True); a=ap.parse_args()
    try: out=evaluate(a.causal,a.radius_index)
    except Exception as e: out={'iteration':490,'causal':a.causal,'radius_index':a.radius_index,'valid':False,'classification':'INFRASTRUCTURE_OR_NUMERICAL_FAIL_ITER490','error':repr(e)}
    os.makedirs(os.path.dirname(a.out) or '.',exist_ok=True); json.dump(out,open(a.out,'w'),indent=2,sort_keys=True); print(json.dumps(out,indent=2,sort_keys=True)); raise SystemExit(0)
if __name__=='__main__': main()

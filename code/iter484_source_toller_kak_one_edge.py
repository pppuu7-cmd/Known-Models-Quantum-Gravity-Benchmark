#!/usr/bin/env python3
import argparse, json, math, os
import numpy as np
import mpmath as mp

from iter483_common_node_sl2c_polar import nodes, relatives, polar, boost
from iter456_reduced_toller_appendixb import source

mp.mp.dps = 80
RHOS = [mp.mpf('0.35'), mp.mpf('0.9'), mp.mpf('1.6'), mp.mpf('2.7')]
MS = [-1,0,1]
I2 = np.eye(2,dtype=np.complex128)
W = np.array([[0,-1],[1,0]],dtype=np.complex128)
THETA = 0.731

def maxabs(a): return float(np.max(np.abs(a)))

def rz(theta):
    return np.diag([np.exp(-0.5j*theta),np.exp(0.5j*theta)]).astype(np.complex128)

def spin1(U):
    # Canonical symmetric square. Fundamental order is (+1/2,-1/2).
    # Project first in (+1,0,-1), then reorder to (-1,0,+1).
    S=np.array([[1,0,0],[0,1/math.sqrt(2),0],[0,1/math.sqrt(2),0],[0,0,1]],dtype=np.complex128)
    Dp=S.conj().T@np.kron(U,U)@S
    q=[2,1,0]
    return Dp[np.ix_(q,q)]

def kak(h):
    u,s,vh=np.linalg.svd(h)
    # det(h)=1 and prod(s)=1. Split the U(1) phase so both factors are SU(2).
    detu=np.linalg.det(u)
    alpha=np.sqrt(detu)
    U1=u/alpha
    U2=alpha*vh
    beta=float(np.log(s[0]/s[1]))
    A=boost(beta)
    return U1,beta,U2,A

def reduced(rho,beta):
    ds=[]; ps=[]; ns=[]
    b=mp.mpf(str(beta))
    for m in MS:
        d,tp,tm=source(m,rho,b)
        ds.append(complex(d)); ps.append(complex(tp)); ns.append(complex(tm))
    return np.diag(ds),np.diag(ps),np.diag(ns)

def full_from_kak(U1,beta,U2,rho):
    d,p,n=reduced(rho,beta)
    L=spin1(U1); R=spin1(U2)
    return L@d@R,L@p@R,L@n@R

def su2_metrics(U):
    return maxabs(U.conj().T@U-I2), float(abs(np.linalg.det(U)-1))

def full_direct(h,rho):
    U1,b,U2,_=kak(h)
    return full_from_kak(U1,b,U2,rho)

def evaluate(panel,regime):
    gs=nodes(panel,regime)
    rs=relatives(gs)
    h=rs[(0,1)]
    h2=rs[(0,2)]
    U1,beta,U2,A=kak(h)
    u1u,u1d=su2_metrics(U1); u2u,u2d=su2_metrics(U2)
    recon=maxabs(U1@A@U2-h)
    _,_,_,eta_polar=polar(h)
    eta_res=abs(beta-eta_polar)

    add_max=0.0; axial_max=0.0; conj_max=mp.mpf('0')
    inv_recon=maxabs((np.linalg.inv(U2)@W)@A@(np.linalg.inv(W)@np.linalg.inv(U1))-np.linalg.inv(h))
    inv_t_max=0.0; nonrep_max=[]
    Rz=rz(THETA)
    for rho in RHOS:
        D,Tp,Tm=full_from_kak(U1,beta,U2,rho)
        add_max=max(add_max,maxabs(Tp+Tm-D))
        Dg,Tpg,Tmg=full_from_kak(U1@Rz,beta,np.linalg.inv(Rz)@U2,rho)
        axial_max=max(axial_max,maxabs(Dg-D),maxabs(Tpg-Tp),maxabs(Tmg-Tm))
        b_mp=mp.mpf(str(beta))
        for m in MS:
            _,p,_=source(m,rho,b_mp); _,_,nm=source(-m,rho,b_mp)
            denom=max(mp.mpf('1'),abs(p),abs(nm))
            conj_max=max(conj_max,abs(mp.conj(p)-nm)/denom)
        Up1=np.linalg.inv(U2)@W; Up2=np.linalg.inv(W)@np.linalg.inv(U1)
        Dp,Pp,Np=full_from_kak(Up1,beta,Up2,rho)
        Dd,Pd,Nd=full_direct(np.linalg.inv(h),rho)
        inv_t_max=max(inv_t_max,maxabs(Dp-Dd),maxabs(Pp-Pd),maxabs(Np-Nd))
        # Frozen nonrepresentation control uses h2*h in the same source convention.
        _,P21,_=full_direct(h2@h,rho)
        _,P2,_=full_direct(h2,rho)
        _,P1,_=full_direct(h,rho)
        nonrep_max.append(maxabs(P21-P2@P1))

    H,Up,_,_=polar(h)
    h_bad=A@Up
    polar_bad=maxabs(h_bad-h)
    beta_valid=bool(beta>1e-8 and np.isfinite(beta))
    finite=all(np.isfinite(x) for x in [recon,eta_res,add_max,axial_max,inv_recon,inv_t_max,polar_bad]+nonrep_max)
    tests={
      'cartan_reconstruction': recon<1e-10 and u1u<1e-10 and u1d<1e-10 and u2u<1e-10 and u2d<1e-10,
      'rapidity_continuity': eta_res<1e-10,
      'full_additive_identity': add_max<=1e-11,
      'axial_gauge_invariance': axial_max<1e-10,
      'reduced_conjugation_reversal': conj_max<=mp.mpf('1e-35'),
      'inversion_kak': inv_recon<1e-10 and inv_t_max<1e-9,
      'naive_polar_negative': polar_bad>1e-4,
      'nonrepresentation_negative': max(nonrep_max)>1e-5,
    }
    valid=beta_valid and finite
    passed=valid and all(bool(v) for v in tests.values())
    cls=('ITER484_SOURCE_TOLLER_KAK_ONE_EDGE_RECONSTRUCTION_QUALIFIED_SCOPED' if passed
         else 'SCIENTIFIC_FAIL_ITER484_SOURCE_TOLLER_KAK_ONE_EDGE' if valid
         else 'BLOCKED_OR_INFRASTRUCTURE_ITER484')
    return {
      'iteration':484,'lane':f'{panel}-{regime}','panel':panel,'regime':regime,'edge':[0,1],
      'valid':valid,'pass':passed,'classification':cls,'tests':tests,
      'beta':beta,'cartan_reconstruction_residual':recon,'u1_unitarity':u1u,'u1_det':u1d,'u2_unitarity':u2u,'u2_det':u2d,
      'polar_rapidity_residual':eta_res,'full_additive_residual':add_max,'axial_gauge_residual':axial_max,
      'reduced_conjugation_relative_residual':float(conj_max),'inverse_reconstruction_residual':inv_recon,
      'inverse_toller_kak_residual':inv_t_max,'naive_polar_reconstruction_error':polar_bad,
      'nonrepresentation_mismatches':nonrep_max,'nonrepresentation_max':max(nonrep_max),
      'rho_panel':[float(r) for r in RHOS],
      'scope':'one-edge source Eq.(7)/(13) full magnetic reconstruction in frozen j=1 witness sector only; no ten-edge/Haar/D7-S2 closure'
    }

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--panel',required=True,choices=list('ABCD')); ap.add_argument('--regime',required=True,choices=['mild','strong']); ap.add_argument('--out',required=True); args=ap.parse_args()
    try: payload=evaluate(args.panel,args.regime)
    except Exception as e:
        payload={'iteration':484,'lane':f'{args.panel}-{args.regime}','valid':False,'pass':False,'classification':'BLOCKED_OR_INFRASTRUCTURE_ITER484','error':repr(e)}
    os.makedirs(os.path.dirname(args.out) or '.',exist_ok=True)
    with open(args.out,'w') as f: json.dump(payload,f,indent=2,sort_keys=True)
    print(json.dumps(payload,indent=2,sort_keys=True))
    raise SystemExit(0 if payload.get('pass') else 2)

if __name__=='__main__': main()

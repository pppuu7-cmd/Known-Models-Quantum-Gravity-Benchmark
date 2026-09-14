#!/usr/bin/env python3
import argparse, itertools, json, math, os
import numpy as np
import mpmath as mp

import iter486_shared_node_haar_escape as base
import iter490_angular_neighborhood_thickening as parent
from iter483_common_node_sl2c_polar import PANELS, BOOSTS

mp.mp.dps = 130
PRIMARY_DPS = 100
EDGE_ID_REL_TOL = mp.mpf('1e-9')
HP_GROUP_TOL = mp.mpf('1e-50')
PRECISION_TOL = mp.mpf('1e-20')

TS = [base.intertwiner(i) for i in range(3)]
PATH = base.contraction_path(TS)
CHANNELS = list(itertools.product(range(3), repeat=5))
EDGES = list(base.EDGES)


def M2(a,b,c,d):
    return mp.matrix([[a,b],[c,d]])


def diag2(a,b):
    return M2(a,0,0,b)


def mpf_float(x):
    return mp.mpf(repr(float(x)))


def det2(a):
    return a[0,0]*a[1,1]-a[0,1]*a[1,0]


def inv2(a):
    d=det2(a)
    return M2(a[1,1]/d,-a[0,1]/d,-a[1,0]/d,a[0,0]/d)


def maxabs_mp(a):
    return max(abs(a[i,j]) for i in range(a.rows) for j in range(a.cols))


def mp_su2(a,t,g):
    # a,t,g are already the exact frozen double parameter values.
    a=mpf_float(a); t=mpf_float(t); g=mpf_float(g)
    c=mp.cos(t/2); s=mp.sin(t/2)
    return diag2(mp.e**(-mp.j*a/2),mp.e**(mp.j*a/2))*M2(c,-s,s,c)*diag2(mp.e**(-mp.j*g/2),mp.e**(mp.j*g/2))


def mp_boost(x):
    x=mpf_float(x)
    return diag2(mp.e**(x/2),mp.e**(-x/2))


def mp_rx(x):
    x=mpf_float(x); c=mp.cos(x/2); s=mp.sin(x/2)
    return M2(c,-mp.j*s,-mp.j*s,c)


def mp_ry(x):
    x=mpf_float(x); c=mp.cos(x/2); s=mp.sin(x/2)
    return M2(c,-s,s,c)


def mp_rz(x):
    x=mpf_float(x)
    return diag2(mp.e**(-mp.j*x/2),mp.e**(mp.j*x/2))


def hp_nodes(R, v, eps, dps=PRIMARY_DPS):
    with mp.workdps(dps):
        out=[mp.eye(2)]
        B=mp_boost(float(R))
        etas=BOOSTS['strong']
        for i in range(1,5):
            a,t,g=PANELS['C'][i]
            # Preserve the exact original double composite parameters before lifting.
            ur_a=float(-0.37*g); ur_t=float(0.73*t); ur_g=float(0.41*a)
            g0=mp_su2(a,t,g)*mp_boost(etas[i])*mp_su2(ur_a,ur_t,ur_g)
            out.append(B*g0)
        for a in range(1,5):
            q=[float(v[(a-1)*5+j]*eps) for j in range(5)]
            out[a]=mp_rx(q[0])*mp_ry(q[1])*mp_rz(q[2])*out[a]*mp_rx(q[3])*mp_ry(q[4])
        return out


def hp_relatives(gs):
    return {(a,b):inv2(gs[b])*gs[a] for a,b in EDGES}


def hp_kak(h, dps=PRIMARY_DPS):
    with mp.workdps(dps):
        U,S,V=mp.svd_c(h)
        alpha=mp.sqrt(det2(U))
        U1=U/alpha
        U2=V*alpha
        beta=mp.log(S[0]/S[1])
        A=diag2(mp.e**(beta/2),mp.e**(-beta/2))
        recon=maxabs_mp(U1*A*U2-h)
        eye=mp.eye(2)
        u1u=maxabs_mp(U1.H*U1-eye); u2u=maxabs_mp(U2.H*U2-eye)
        u1d=abs(det2(U1)-1); u2d=abs(det2(U2)-1)
        return U1,beta,U2,recon,max(u1u,u2u),max(u1d,u2d)


def to_np(a):
    return np.array([[complex(float(mp.re(a[i,j])),float(mp.im(a[i,j]))) for j in range(a.cols)] for i in range(a.rows)],dtype=np.complex128)


def hp_cycle_residual(rs):
    out=mp.mpf('0')
    for a,b,c in itertools.combinations(range(5),3):
        out=max(out,maxabs_mp(rs[(b,c)]*rs[(a,b)]-rs[(a,c)]))
    return out


def source_identity_residual(h_hp,h_double):
    h=to_np(h_hp)
    den=max(1.0,float(np.max(np.abs(h))))
    return float(np.max(np.abs(h-h_double))/den)


def geometry_bundle(R,v,eps,dps=PRIMARY_DPS):
    gs=hp_nodes(float(R),v,float(eps),dps=dps)
    rs=hp_relatives(gs)
    return gs,rs


def precision_anchor(radius_index):
    eps=parent.EPS[radius_index]
    v=parent.vec20(radius_index,0)
    gs80,rs80=geometry_bundle(12.0,v,eps,dps=80)
    gs120,rs120=geometry_bundle(12.0,v,eps,dps=120)
    edge_rel=mp.mpf('0'); beta_abs=mp.mpf('0')
    with mp.workdps(130):
        for e in EDGES:
            den=max(mp.mpf('1'),maxabs_mp(rs120[e]))
            edge_rel=max(edge_rel,maxabs_mp(rs80[e]-rs120[e])/den)
            b80=hp_kak(rs80[e],dps=80)[1]
            b120=hp_kak(rs120[e],dps=120)[1]
            beta_abs=max(beta_abs,abs(b80-b120))
    return {
      'edge_relative_difference_max':float(edge_rel),
      'beta_absolute_difference_max':float(beta_abs),
      'pass':bool(edge_rel<PRECISION_TOL and beta_abs<PRECISION_TOL),
    }


def sample_eval(causal,v,eps):
    sig=base.SIGMAS[causal]
    logH=[]; logC={i:[] for i in range(len(base.RHOS))}
    node_det=mp.mpf('0'); edge_det=mp.mpf('0'); cycle=mp.mpf('0')
    kak_recon=mp.mpf('0'); kak_unit=mp.mpf('0'); kak_det=mp.mpf('0')
    identity=0.0; additive=0.0; allpos=True

    for R in base.R_GRID:
        gs,rs=geometry_bundle(float(R),v,float(eps),dps=PRIMARY_DPS)
        node_det=max(node_det,max(abs(det2(g)-1) for g in gs))
        edge_det=max(edge_det,max(abs(det2(h)-1) for h in rs.values()))
        cycle=max(cycle,hp_cycle_residual(rs))

        # Frozen source-object identity against the original Iter490 double construction.
        old_gs=parent.perturb(base.escaped_nodes('C',4,float(R)),v,float(eps))
        old_rs=base.relatives(old_gs)
        for e in EDGES:
            identity=max(identity,source_identity_residual(rs[e],old_rs[e]))

        # Actual node rapidities for the source Haar factor.
        lh=mp.mpf('0')
        for a in range(1,5):
            _,beta_node,_,rec,uu,dd=hp_kak(gs[a],dps=PRIMARY_DPS)
            kak_recon=max(kak_recon,rec); kak_unit=max(kak_unit,uu); kak_det=max(kak_det,dd)
            lh += 2*mp.log(mp.sinh(beta_node))
        logH.append(float(lh))

        edge_kak={}
        for e in EDGES:
            U1,beta,U2,rec,uu,dd=hp_kak(rs[e],dps=PRIMARY_DPS)
            kak_recon=max(kak_recon,rec); kak_unit=max(kak_unit,uu); kak_det=max(kak_det,dd)
            edge_kak[e]=(to_np(U1),float(beta),to_np(U2))

        for ir,rho in enumerate(base.RHOS):
            mats=[]; lognorm=0.0
            for e in EDGES:
                U1,beta,U2=edge_kak[e]
                D,Tp,Tm=base.full_from_kak(U1,beta,U2,rho)
                additive=max(additive,base.maxabs(Tp+Tm-D))
                M=Tp if sig[e[0]]*sig[e[1]]>0 else Tm
                n=base.maxabs(M)
                if not np.isfinite(n) or n<=0:
                    allpos=False
                    mats.append(M)
                else:
                    mats.append(M/n); lognorm += math.log(n)
            vals=np.asarray([base.contract(ch,TS,mats,PATH) for ch in CHANNELS],dtype=np.complex128)
            finite=bool(np.all(np.isfinite(vals.real)) and np.all(np.isfinite(vals.imag)))
            m=float(np.max(np.abs(vals))) if finite else float('nan')
            positive=bool(finite and np.isfinite(m) and m>0)
            allpos=allpos and positive
            logC[ir].append(lognorm+math.log(m) if positive else float('nan'))

    hs=base.slope(base.R_GRID[-3:],logH[-3:])
    bookmax=0.0; results=[]
    for ir,rho in enumerate(base.RHOS):
        le=[logC[ir][k]+logH[k] for k in range(4)]
        ns=base.slope(base.R_GRID[-3:],logC[ir][-3:])
        ac=base.slope(base.R_GRID[-3:],le[-3:])
        early=base.slope(base.R_GRID[:3],le[:3])
        drift=abs(ac-early)
        book=abs((ac-ns)-hs); bookmax=max(bookmax,book)
        results.append({
          'rho':float(rho),'actual_slope':ac,'slope_drift':drift,
          'nondecay':bool(ac>=0.0 and drift<=0.05),
          'robust':bool(ac>=1.0 and drift<=0.05),
        })

    controls={
      'hp_node_det':bool(node_det<HP_GROUP_TOL),
      'hp_edge_det':bool(edge_det<HP_GROUP_TOL),
      'hp_kak_reconstruction':bool(kak_recon<HP_GROUP_TOL),
      'hp_kak_su2_unitarity':bool(kak_unit<HP_GROUP_TOL),
      'hp_kak_su2_det':bool(kak_det<HP_GROUP_TOL),
      'hp_cycle':bool(cycle<HP_GROUP_TOL),
      'source_object_identity':bool(identity<float(EDGE_ID_REL_TOL)),
      'finite_positive':bool(allpos),
      'haar_slope':bool(abs(hs-8.0)<0.05),
      'haar_bookkeeping':bool(bookmax<1e-8),
      'source_additive':bool(additive<1e-9),
    }
    return {
      'results':results,'controls':controls,
      'hp_node_det_max':float(node_det),'hp_edge_det_max':float(edge_det),'hp_cycle_max':float(cycle),
      'hp_kak_reconstruction_max':float(kak_recon),'hp_kak_unitarity_max':float(kak_unit),'hp_kak_det_max':float(kak_det),
      'source_object_identity_relative_max':identity,'haar_slope':hs,'bookkeeping_max':bookmax,'additive_max':additive,
    }


def evaluate(causal,radius_index):
    eps=parent.EPS[radius_index]
    ranks=parent.chart_ranks()
    anchor=precision_anchor(radius_index)
    center=sample_eval(causal,np.zeros(20,dtype=float),0.0)
    center_slopes=[r['actual_slope'] for r in center['results']]
    center_reg=max(abs(a-b) for a,b in zip(center_slopes,parent.CENTER[causal]))
    samples=[sample_eval(causal,parent.vec20(radius_index,i),eps) for i in range(16)]

    valid=(all(r==5 for r in ranks) and anchor['pass'] and center_reg<5e-3
           and all(center['controls'].values()) and all(all(s['controls'].values()) for s in samples))
    all_nondecay=valid and all(r['nondecay'] for s in samples for r in s['results'])
    all_robust=valid and all(r['robust'] for s in samples for r in s['results'])
    if not valid:
        cls='INFRASTRUCTURE_OR_NUMERICAL_FAIL_ITER491'
    elif all_robust:
        cls='ITER491_SAMPLED_ROBUST_THICKENING_LANE'
    elif all_nondecay:
        cls='ITER491_SAMPLED_NONDECAY_THICKENING_LANE'
    else:
        cls='SCIENTIFIC_FAIL_ITER491_ANGULAR_THICKENING_HP'

    slopes=[r['actual_slope'] for s in samples for r in s['results']]
    drifts=[r['slope_drift'] for s in samples for r in s['results']]
    return {
      'iteration':491,'lane':f'{causal}-r{radius_index}','causal':causal,'radius_index':radius_index,'eps':eps,
      'chart_ranks':ranks,'precision_anchor':anchor,'center_regression_max_abs':center_reg,
      'valid':bool(valid),'classification':cls,'all_sampled_nondecay':bool(all_nondecay),'all_sampled_robust':bool(all_robust),
      'sampled_min_actual_slope':min(slopes),'sampled_max_actual_slope':max(slopes),'sampled_max_slope_drift':max(drifts),
      'center':center,'samples':samples,
      'scope':'same frozen Iter490 sampled 20-D angular thickening, source group matrices built before KAK at 100 digits; finite sampled result only'
    }


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--causal',required=True,choices=base.CAUSALS); ap.add_argument('--radius-index',required=True,type=int,choices=range(4)); ap.add_argument('--out',required=True); a=ap.parse_args()
    try:
        out=evaluate(a.causal,a.radius_index)
    except Exception as e:
        out={'iteration':491,'lane':f'{a.causal}-r{a.radius_index}','causal':a.causal,'radius_index':a.radius_index,'valid':False,'classification':'INFRASTRUCTURE_OR_NUMERICAL_FAIL_ITER491','error':repr(e)}
    os.makedirs(os.path.dirname(a.out) or '.',exist_ok=True)
    with open(a.out,'w') as f: json.dump(out,f,indent=2,sort_keys=True)
    print(json.dumps(out,indent=2,sort_keys=True))
    # Scientific FAIL is a valid production result. Aggregate owns workflow terminalization.
    raise SystemExit(0)

if __name__=='__main__':
    main()

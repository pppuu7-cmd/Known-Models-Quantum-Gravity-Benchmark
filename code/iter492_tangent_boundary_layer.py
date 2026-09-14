#!/usr/bin/env python3
import argparse, itertools, json, math, os
import numpy as np
import mpmath as mp

import iter486_shared_node_haar_escape as base
import iter490_angular_neighborhood_thickening as parent
import iter491_high_precision_angular_thickening as hp

mp.mp.dps = 130
KAPPA = 0.02
Q_VALUES = [0.50, 0.75, 1.00, 1.25, 1.50]
DIRS_INT = [
 [1,1,1,1,1, 1,1,1,1,1, 1,1,1,1,1, 1,1,1,1,1],
 [1,-1,1,-1,1, -1,1,-1,1,-1, 1,-1,1,-1,1, -1,1,-1,1,-1],
 [1,1,-1,-1,1, 1,-1,-1,1,1, -1,-1,1,1,-1, -1,1,1,-1,-1],
 [1,-1,-1,1,1, -1,-1,1,1,-1, -1,1,1,-1,-1, 1,1,-1,-1,1],
 [1,-1,1,1,-1, 1,1,-1,1,-1, 1,-1,1,-1,1, -1,1,-1,1,1],
 [1,1,-1,1,-1, -1,1,1,-1,1, 1,-1,1,1,-1, -1,1,-1,1,1],
 [1,-1,-1,-1,1, 1,1,-1,-1,-1, -1,1,1,-1,-1, -1,-1,1,1,-1],
 [1,1,1,-1,-1, -1,1,1,1,-1, -1,-1,1,1,1, 1,-1,-1,1,1],
]
DIRS = [np.asarray(v,dtype=float)/np.linalg.norm(v) for v in DIRS_INT]
TS = hp.TS
PATH = hp.PATH
CHANNELS = hp.CHANNELS
EDGES = hp.EDGES


def dynamic_eval(causal, direction, sign, q):
    sig = base.SIGMAS[causal]
    logH=[]; logC={i:[] for i in range(len(base.RHOS))}
    node_det=mp.mpf('0'); edge_det=mp.mpf('0'); cycle=mp.mpf('0')
    kak_recon=mp.mpf('0'); kak_unit=mp.mpf('0'); kak_det=mp.mpf('0')
    identity=0.0; additive=0.0; allpos=True
    eps_by_R=[]

    for R in base.R_GRID:
        eps = float(KAPPA * math.exp(-float(q)*float(R)))
        eps_by_R.append(eps)
        v = float(sign) * direction
        gs,rs = hp.geometry_bundle(float(R),v,eps,dps=hp.PRIMARY_DPS)
        node_det=max(node_det,max(abs(hp.det2(g)-1) for g in gs))
        edge_det=max(edge_det,max(abs(hp.det2(h)-1) for h in rs.values()))
        cycle=max(cycle,hp.hp_cycle_residual(rs))

        old_gs=parent.perturb(base.escaped_nodes('C',4,float(R)),v,eps)
        old_rs=base.relatives(old_gs)
        for e in EDGES:
            identity=max(identity,hp.source_identity_residual(rs[e],old_rs[e]))

        lh=mp.mpf('0')
        for a in range(1,5):
            _,beta_node,_,rec,uu,dd=hp.hp_kak(gs[a],dps=hp.PRIMARY_DPS)
            kak_recon=max(kak_recon,rec); kak_unit=max(kak_unit,uu); kak_det=max(kak_det,dd)
            lh += 2*mp.log(mp.sinh(beta_node))
        logH.append(float(lh))

        edge_kak={}
        for e in EDGES:
            U1,beta,U2,rec,uu,dd=hp.hp_kak(rs[e],dps=hp.PRIMARY_DPS)
            kak_recon=max(kak_recon,rec); kak_unit=max(kak_unit,uu); kak_det=max(kak_det,dd)
            edge_kak[e]=(hp.to_np(U1),float(beta),hp.to_np(U2))

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
            'rho':float(rho),'actual_slope':ac,'early_actual_slope':early,
            'slope_drift':drift,
            'nondecay':bool(ac>=0.0 and drift<=0.05),
            'robust':bool(ac>=1.0 and drift<=0.05),
        })

    controls={
        'hp_node_det':bool(node_det<hp.HP_GROUP_TOL),
        'hp_edge_det':bool(edge_det<hp.HP_GROUP_TOL),
        'hp_kak_reconstruction':bool(kak_recon<hp.HP_GROUP_TOL),
        'hp_kak_su2_unitarity':bool(kak_unit<hp.HP_GROUP_TOL),
        'hp_kak_su2_det':bool(kak_det<hp.HP_GROUP_TOL),
        'hp_cycle':bool(cycle<hp.HP_GROUP_TOL),
        'source_object_identity':bool(identity<float(hp.EDGE_ID_REL_TOL)),
        'finite_positive':bool(allpos),
        'haar_bookkeeping':bool(bookmax<1e-8),
        'source_additive':bool(additive<1e-9),
    }
    return {
        'eps_by_R':eps_by_R,'results':results,'controls':controls,
        'hp_node_det_max':float(node_det),'hp_edge_det_max':float(edge_det),
        'hp_cycle_max':float(cycle),'hp_kak_reconstruction_max':float(kak_recon),
        'hp_kak_unitarity_max':float(kak_unit),'hp_kak_det_max':float(kak_det),
        'source_object_identity_relative_max':identity,'haar_slope':hs,
        'bookkeeping_max':bookmax,'additive_max':additive,
    }


def evaluate(causal, q_index):
    q=Q_VALUES[q_index]
    ranks=parent.chart_ranks()
    center=hp.sample_eval(causal,np.zeros(20,dtype=float),0.0)
    center_slopes=[r['actual_slope'] for r in center['results']]
    center_reg=max(abs(a-b) for a,b in zip(center_slopes,parent.CENTER[causal]))
    center_valid=all(r==5 for r in ranks) and center_reg<5e-3 and all(center['controls'].values())

    lanes=[]
    for di,d in enumerate(DIRS):
        signed=[]
        for sign in (-1,1):
            s=dynamic_eval(causal,d,sign,q)
            signed.append({'sign':sign,**s})
        valid=bool(center_valid and all(all(x['controls'].values()) for x in signed))
        states=[r for x in signed for r in x['results']]
        all_nondecay=bool(valid and all(r['nondecay'] for r in states))
        all_robust=bool(valid and all(r['robust'] for r in states))
        if not valid:
            cls='INFRASTRUCTURE_OR_NUMERICAL_FAIL_ITER492'
        elif all_robust:
            cls='ITER492_TANGENT_ROBUST_LANE'
        elif all_nondecay:
            cls='ITER492_TANGENT_NONDECAY_LANE'
        else:
            cls='SCIENTIFIC_FAIL_ITER492_TANGENT_LANE'
        lanes.append({
            'direction_index':di,'direction':DIRS_INT[di],
            'valid':valid,'classification':cls,
            'all_nondecay':all_nondecay,'all_robust':all_robust,
            'signed':signed,
        })

    return {
        'iteration':492,'job':f'{causal}-q{q_index}','causal':causal,
        'q_index':q_index,'q':q,'kappa':KAPPA,
        'chart_ranks':ranks,'center_regression_max_abs':center_reg,
        'center_valid':bool(center_valid),'center':center,
        'lanes':lanes,
        'all_lanes_valid':bool(all(x['valid'] for x in lanes)),
        'all_lanes_nondecay':bool(all(x['all_nondecay'] for x in lanes)),
        'all_lanes_robust':bool(all(x['all_robust'] for x in lanes)),
        'scope':'prospectively frozen R-dependent tangent boundary-layer eps=0.02*exp(-qR), finite directions/R only; not a positive-measure theorem',
    }


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--causal',required=True,choices=base.CAUSALS)
    ap.add_argument('--q-index',required=True,type=int,choices=range(len(Q_VALUES)))
    ap.add_argument('--out',required=True)
    a=ap.parse_args()
    try:
        out=evaluate(a.causal,a.q_index)
    except Exception as e:
        out={'iteration':492,'job':f'{a.causal}-q{a.q_index}','causal':a.causal,
             'q_index':a.q_index,'valid':False,
             'classification':'INFRASTRUCTURE_OR_NUMERICAL_FAIL_ITER492','error':repr(e)}
    os.makedirs(os.path.dirname(a.out) or '.',exist_ok=True)
    with open(a.out,'w') as f: json.dump(out,f,indent=2,sort_keys=True)
    print(json.dumps(out,indent=2,sort_keys=True))
    raise SystemExit(0)

if __name__=='__main__':
    main()

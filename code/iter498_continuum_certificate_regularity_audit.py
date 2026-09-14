#!/usr/bin/env python3
import argparse, itertools, json, math, os
import numpy as np

import iter486_shared_node_haar_escape as base
import iter490_angular_neighborhood_thickening as parent
import iter491_high_precision_angular_thickening as hp
import iter492_tangent_boundary_layer as it
import iter495_multivariate_taylor_stress as geom

AMPS=[0.00125,0.00140625,0.0015625,0.00171875,0.001875,0.00203125,0.0021875,0.00234375,0.00250]
COORDS=geom.COORDS
BLOCKS=geom.BLOCKS
Q=1.0
GAP_TOL=1e-6
BETA_TOL=1e-6
EDGES=hp.EDGES
TS=hp.TS
PATH=hp.PATH
CHANNELS=hp.CHANNELS


def diag_at(causal, vec6, amp):
    sig=base.SIGMAS[causal]
    d=np.zeros(20,dtype=float)
    for k,c in enumerate(COORDS): d[c]=float(vec6[k])
    states=[]
    valid=True
    max_identity=0.0; max_add=0.0
    max_node_det=0.0; max_edge_det=0.0; max_cycle=0.0
    max_rec=0.0; max_unit=0.0; max_kdet=0.0
    for R in base.R_GRID:
        eps=float(amp*math.exp(-Q*float(R)))
        gs,rs=hp.geometry_bundle(float(R),d,eps,dps=hp.PRIMARY_DPS)
        node_betas=[]; edge_betas={}
        max_node_det=max(max_node_det,float(max(abs(hp.det2(g)-1) for g in gs)))
        max_edge_det=max(max_edge_det,float(max(abs(hp.det2(h)-1) for h in rs.values())))
        max_cycle=max(max_cycle,float(hp.hp_cycle_residual(rs)))
        old_gs=parent.perturb(base.escaped_nodes('C',4,float(R)),d,eps)
        old_rs=base.relatives(old_gs)
        for e in EDGES:
            max_identity=max(max_identity,float(hp.source_identity_residual(rs[e],old_rs[e])))
        for a in range(1,5):
            _,beta,_,rec,uu,dd=hp.hp_kak(gs[a],dps=hp.PRIMARY_DPS)
            node_betas.append(float(beta)); max_rec=max(max_rec,float(rec)); max_unit=max(max_unit,float(uu)); max_kdet=max(max_kdet,float(dd))
        edge_kak={}
        for e in EDGES:
            U1,beta,U2,rec,uu,dd=hp.hp_kak(rs[e],dps=hp.PRIMARY_DPS)
            edge_betas[e]=float(beta); edge_kak[e]=(hp.to_np(U1),float(beta),hp.to_np(U2))
            max_rec=max(max_rec,float(rec)); max_unit=max(max_unit,float(uu)); max_kdet=max(max_kdet,float(dd))
        for ir,rho in enumerate(base.RHOS):
            mats=[]
            for e in EDGES:
                U1,beta,U2=edge_kak[e]
                D,Tp,Tm=base.full_from_kak(U1,beta,U2,rho)
                max_add=max(max_add,base.maxabs(Tp+Tm-D))
                M=Tp if sig[e[0]]*sig[e[1]]>0 else Tm
                n=base.maxabs(M)
                if (not np.isfinite(n)) or n<=0:
                    valid=False
                    mats.append(M)
                else:
                    mats.append(M/n)
            vals=np.asarray([base.contract(ch,TS,mats,PATH) for ch in CHANNELS],dtype=np.complex128)
            mags=np.abs(vals)
            finite=bool(np.all(np.isfinite(mags)))
            valid=valid and finite
            if not finite:
                idx=-1; m1=float('nan'); m2=float('nan'); gap=float('nan')
            else:
                order=np.argsort(mags)
                idx=int(order[-1]); m1=float(mags[order[-1]]); m2=float(mags[order[-2]])
                gap=float((m1-m2)/max(m1,1e-300))
            states.append({'R':float(R),'rho':float(rho),'argmax':idx,'m1':m1,'m2':m2,'relative_gap':gap,
                           'min_edge_beta':float(min(edge_betas.values())),'min_node_beta':float(min(node_betas))})
    controls={
      'hp_node_det':bool(max_node_det<float(hp.HP_GROUP_TOL)),
      'hp_edge_det':bool(max_edge_det<float(hp.HP_GROUP_TOL)),
      'hp_cycle':bool(max_cycle<float(hp.HP_GROUP_TOL)),
      'hp_kak_reconstruction':bool(max_rec<float(hp.HP_GROUP_TOL)),
      'hp_kak_su2_unitarity':bool(max_unit<float(hp.HP_GROUP_TOL)),
      'hp_kak_su2_det':bool(max_kdet<float(hp.HP_GROUP_TOL)),
      'source_object_identity':bool(max_identity<float(hp.EDGE_ID_REL_TOL)),
      'source_additive':bool(max_add<1e-9),
      'finite_channels':bool(valid),
    }
    valid=bool(valid and all(controls.values()))
    return {'amplitude':float(amp),'states':states,'controls':controls,'valid':valid,
            'max_source_identity':max_identity,'max_additive':max_add,'max_kak_reconstruction':max_rec}


def evaluate(causal,block):
    paths=[]; all_valid=True; switches=0; min_gap=float('inf'); min_beta=float('inf')
    for direction in BLOCKS[block]:
        for sign in (1,-1):
            v=[float(sign*x) for x in direction]
            samples=[diag_at(causal,v,a) for a in AMPS]
            all_valid=all_valid and all(s['valid'] for s in samples)
            # fixed state order = 4 R x 4 rho
            local_switch=0
            for j in range(len(samples[0]['states'])):
                seq=[s['states'][j] for s in samples]
                ids=[z['argmax'] for z in seq]
                local_switch += sum(int(ids[k]!=ids[k-1]) for k in range(1,len(ids)))
                min_gap=min(min_gap,min(z['relative_gap'] for z in seq))
                min_beta=min(min_beta,min(min(z['min_edge_beta'],z['min_node_beta']) for z in seq))
            switches += local_switch
            paths.append({'direction':direction,'sign':sign,'argmax_switches':local_switch,'samples':samples})
    if not all_valid:
        cls='INFRASTRUCTURE_OR_NUMERICAL_FAIL_ITER498'
    else:
        gap_bad=bool(min_gap<GAP_TOL or switches>0)
        beta_bad=bool(min_beta<BETA_TOL)
        if gap_bad and beta_bad: cls='ITER498_MAX_AND_KAK_REGULARITY_BLOCKERS_IDENTIFIED_SCOPED'
        elif gap_bad: cls='ITER498_MAX_ENVELOPE_NONSMOOTH_BLOCKER_IDENTIFIED_SCOPED'
        elif beta_bad: cls='ITER498_KAK_BRANCH_MARGIN_BLOCKER_IDENTIFIED_SCOPED'
        else: cls='ITER498_REGULAR_SAMPLED_PATH_QUALIFIED_SCOPED'
    return {'iteration':498,'job':f'{causal}-b{block}','causal':causal,'block':block,'amplitudes':AMPS,
            'gap_tol':GAP_TOL,'beta_tol':BETA_TOL,'argmax_switches':int(switches),'min_relative_top2_gap':float(min_gap),
            'min_positive_kak_beta':float(min_beta),'valid':bool(all_valid),'classification':cls,'paths':paths,
            'scope':'diagnostic sampled regularity audit for selecting a rigorous interval method; not a continuum/interval certificate'}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--causal',required=True,choices=base.CAUSALS); ap.add_argument('--block',required=True,type=int,choices=range(4)); ap.add_argument('--out',required=True); a=ap.parse_args()
    try: out=evaluate(a.causal,a.block)
    except Exception as e: out={'iteration':498,'job':f'{a.causal}-b{a.block}','valid':False,'classification':'INFRASTRUCTURE_OR_NUMERICAL_FAIL_ITER498','error':repr(e)}
    os.makedirs(os.path.dirname(a.out) or '.',exist_ok=True)
    with open(a.out,'w') as f: json.dump(out,f,indent=2,sort_keys=True)
    print(json.dumps({k:v for k,v in out.items() if k!='paths'},indent=2,sort_keys=True))
    raise SystemExit(0)
if __name__=='__main__': main()

#!/usr/bin/env python3
import argparse, itertools, json, os
import numpy as np

from iter483_common_node_sl2c_polar import nodes, relatives, boost
from iter484_source_toller_kak_one_edge import kak, full_from_kak, full_direct, su2_metrics, maxabs, RHOS
from iter482_common_node_su2_control import EDGES, SIGMAS, intertwiner, tensor_controls, contraction_path, contract

THRESH=1e-14
REINDEX_TOL=1e-10


def cycle_residual(rs):
    r=0.0
    for a,b,c in itertools.combinations(range(5),3):
        r=max(r,maxabs(rs[(b,c)]@rs[(a,b)]-rs[(a,c)]))
    return float(r)


def causal_counts(sig):
    same=sum(1 for a,b in EDGES if sig[a]*sig[b]>0)
    return same,10-same


def evaluate(panel,regime,causal):
    sig=SIGMAS[causal]
    gs=nodes(panel,regime)
    rs=relatives(gs)
    cyc=cycle_residual(rs)

    ts=[intertwiner(i) for i in range(3)]
    int_ok,gramres=tensor_controls(ts)
    path=contraction_path(ts)

    # Freeze KAK data once for every shared-node edge.
    edge_kak={}
    kak_recon=0.0; su2_res=0.0
    for e in EDGES:
        h=rs[e]
        U1,b,U2,A=kak(h)
        edge_kak[e]=(U1,b,U2,A)
        kak_recon=max(kak_recon,maxabs(U1@A@U2-h))
        for U in (U1,U2):
            uu,dd=su2_metrics(U); su2_res=max(su2_res,uu,dd)

    same,opp=causal_counts(sig)
    expected={'0to5':(10,0),'1to4':(6,4),'2to3':(4,6)}[causal]

    rho_rows=[]; all_finite=True; all_nonzero=True; add_max=0.0; reindex_max=0.0; zero_max=0.0
    for rho in RHOS:
        mats=[]; norms=[]
        for e in EDGES:
            U1,b,U2,_=edge_kak[e]
            D,Tp,Tm=full_from_kak(U1,b,U2,rho)
            add_max=max(add_max,maxabs(Tp+Tm-D))
            M=Tp if sig[e[0]]*sig[e[1]]>0 else Tm
            mats.append(M)
            norms.append(maxabs(M))
        scale=float(np.prod(norms))
        finite_scale=bool(np.isfinite(scale) and scale>0)
        vals=np.array([contract(ch,ts,mats,path) for ch in itertools.product(range(3),repeat=5)],dtype=np.complex128)
        finite_vals=bool(np.all(np.isfinite(vals.real)) and np.all(np.isfinite(vals.imag)))
        ratios=np.abs(vals)/scale if finite_scale else np.full(vals.shape,np.nan)
        max_ratio=float(np.max(ratios)) if finite_scale and finite_vals else float('nan')
        nonzero=bool(finite_scale and finite_vals and max_ratio>THRESH)
        all_finite=all_finite and finite_scale and finite_vals
        all_nonzero=all_nonzero and nonzero

        # Simultaneous magnetic-basis reversal is a pure relabeling control.
        rts=[T[::-1,::-1,::-1,::-1].copy() for T in ts]
        rmats=[M[::-1,::-1].copy() for M in mats]
        rvals=np.array([contract(ch,rts,rmats,path) for ch in itertools.product(range(3),repeat=5)],dtype=np.complex128)
        sm=np.sort(np.abs(vals)); sr=np.sort(np.abs(rvals)); denom=max(float(np.max(sm)),float(np.max(sr)),1e-300)
        reindex=float(np.max(np.abs(sm-sr))/denom)
        reindex_max=max(reindex_max,reindex)

        zmats=[M.copy() for M in mats]; zmats[0]=np.zeros((3,3),dtype=np.complex128)
        zvals=np.array([contract(ch,ts,zmats,path) for ch in itertools.product(range(3),repeat=5)],dtype=np.complex128)
        zratio=float(np.max(np.abs(zvals))/scale) if finite_scale else float('inf')
        zero_max=max(zero_max,zratio)
        rho_rows.append({'rho':float(rho),'scale':scale,'max_normalized_witness':max_ratio,'nonzero_witness':nonzero,'reindex_residual':reindex,'zero_edge_normalized_max':zratio})

    # Independent-edge surrogate: corrupt only h_01, leaving the other nine shared-edge elements fixed.
    bad=dict(rs)
    bad[(0,1)]=boost(0.417)@bad[(0,1)]
    independent_cycle=cycle_residual(bad)

    # Frozen false-representation negative control inherited from Iter484.
    h=rs[(0,1)]; h2=rs[(0,2)]; nonrep=[]
    for rho in RHOS:
        _,P21,_=full_direct(h2@h,rho); _,P2,_=full_direct(h2,rho); _,P1,_=full_direct(h,rho)
        nonrep.append(maxabs(P21-P2@P1))
    nonrep_max=max(nonrep)

    finite_beta=all(np.isfinite(edge_kak[e][1]) for e in EDGES)
    valid=bool(finite_beta and all_finite)
    tests={
      'shared_node_cycle': cyc<1e-10,
      'per_edge_kak_inheritance': kak_recon<1e-10 and su2_res<1e-10,
      'per_edge_additive_identity': add_max<=1e-11,
      'causal_branch_determinism': (same,opp)==expected,
      'intertwiner_controls': bool(int_ok and gramres<1e-12),
      'finite_normalized_contraction': bool(all_finite),
      'nonzero_witness_all_rho': bool(all_nonzero),
      'magnetic_reindex_covariance': reindex_max<REINDEX_TOL,
      'zero_edge_negative': zero_max<THRESH,
      'independent_edge_negative': independent_cycle>1e-5,
      'false_toller_composition_negative': nonrep_max>1e-5,
    }
    passed=bool(valid and all(tests.values()))
    cls=('ITER485_SHARED_NODE_TEN_EDGE_TOLLER_MAGNETIC_NETWORK_QUALIFIED_SCOPED' if passed else
         'SCIENTIFIC_FAIL_ITER485_TEN_EDGE_TOLLER_NETWORK' if valid else 'BLOCKED_OR_INFRASTRUCTURE_ITER485')
    return {
      'iteration':485,'lane':f'{panel}-{regime}-{causal}','panel':panel,'regime':regime,'causal':causal,
      'valid':valid,'pass':passed,'classification':cls,'tests':tests,
      'cycle_residual':cyc,'kak_reconstruction_max':kak_recon,'su2_factor_residual_max':su2_res,
      'additive_identity_max':add_max,'causal_same_edges':same,'causal_opposite_edges':opp,
      'intertwiner_gram_residual':float(gramres),'reindex_residual_max':reindex_max,'zero_edge_normalized_max':zero_max,
      'independent_edge_cycle_residual':independent_cycle,'nonrepresentation_max':nonrep_max,
      'rho_rows':rho_rows,'rho_panel':[float(r) for r in RHOS],
      'scope':'finite j=1 shared-node ten-edge source Toller magnetic contraction only; pre-Haar/pre-spectral; no D7-S2 closure'
    }


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--panel',required=True,choices=list('ABCD')); ap.add_argument('--regime',required=True,choices=['mild','strong']); ap.add_argument('--causal',required=True,choices=['0to5','1to4','2to3']); ap.add_argument('--out',required=True); args=ap.parse_args()
    try: payload=evaluate(args.panel,args.regime,args.causal)
    except Exception as e: payload={'iteration':485,'lane':f'{args.panel}-{args.regime}-{args.causal}','valid':False,'pass':False,'classification':'BLOCKED_OR_INFRASTRUCTURE_ITER485','error':repr(e)}
    os.makedirs(os.path.dirname(args.out) or '.',exist_ok=True)
    with open(args.out,'w') as f: json.dump(payload,f,indent=2,sort_keys=True)
    print(json.dumps(payload,indent=2,sort_keys=True))
    raise SystemExit(0 if payload.get('pass') else 2)

if __name__=='__main__': main()

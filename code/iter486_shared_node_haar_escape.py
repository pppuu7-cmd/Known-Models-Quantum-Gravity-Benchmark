#!/usr/bin/env python3
import argparse, itertools, json, math, os
import numpy as np

from iter483_common_node_sl2c_polar import nodes, relatives, boost
from iter484_source_toller_kak_one_edge import kak, full_from_kak, full_direct, maxabs, RHOS
from iter482_common_node_su2_control import EDGES, SIGMAS, intertwiner, tensor_controls, contraction_path, contract

R_GRID=np.array([6.0,8.0,10.0,12.0],dtype=float)
PANELS=('A','C')
CAUSALS=('0to5','1to4','2to3')
CYCLE_TOL=1e-8
KAK_TOL=1e-8
HAAR_SLOPE_TOL=0.05
DRIFT_TOL=0.05
DECAY_CEIL=-0.10
NONDECAY_FLOOR=0.0


def cycle_residual(rs):
    out=0.0
    for a,b,c in itertools.combinations(range(5),3):
        out=max(out,maxabs(rs[(b,c)]@rs[(a,b)]-rs[(a,c)]))
    return float(out)


def slope(xs,ys):
    return float(np.polyfit(np.asarray(xs,dtype=float),np.asarray(ys,dtype=float),1)[0])


def escaped_nodes(panel,cluster_size,R):
    gs=[g.copy() for g in nodes(panel,'strong')]
    B=boost(float(R))
    for a in range(1,cluster_size+1):
        gs[a]=B@gs[a]
    return gs


def measure_log(gs,cluster_size):
    etas=[]
    for a in range(1,cluster_size+1):
        _,eta,_,_=kak(gs[a])
        etas.append(float(eta))
    if not all(np.isfinite(x) and x>0 for x in etas):
        raise FloatingPointError('invalid escaped-node Cartan rapidity')
    return float(sum(2.0*math.log(math.sinh(x)) for x in etas)),etas


def edge_data(rs,rho,sig):
    mats=[]; lognorm=0.0; addmax=0.0; kakmax=0.0
    for e in EDGES:
        h=rs[e]
        U1,b,U2,A=kak(h)
        kakmax=max(kakmax,maxabs(U1@A@U2-h))
        D,Tp,Tm=full_from_kak(U1,b,U2,rho)
        addmax=max(addmax,maxabs(Tp+Tm-D))
        M=Tp if sig[e[0]]*sig[e[1]]>0 else Tm
        n=maxabs(M)
        if not np.isfinite(n) or n<=0:
            raise FloatingPointError(f'invalid edge norm {e}: {n}')
        mats.append(M/n)
        lognorm += math.log(n)
    return mats,float(lognorm),float(addmax),float(kakmax)


def evaluate(panel,cluster_size,causal):
    sig=SIGMAS[causal]
    ts=[intertwiner(i) for i in range(3)]
    int_ok,gramres=tensor_controls(ts)
    path=contraction_path(ts)
    channels=list(itertools.product(range(3),repeat=5))

    per_R={}
    cycle_max=0.0; kak_max=0.0; add_max=0.0
    all_finite=True; all_positive=True
    for R in R_GRID:
        gs=escaped_nodes(panel,cluster_size,R)
        rs=relatives(gs)
        cyc=cycle_residual(rs); cycle_max=max(cycle_max,cyc)
        logH,etas=measure_log(gs,cluster_size)
        rho_rows=[]
        for rho in RHOS:
            mats,lognorm,add,kres=edge_data(rs,rho,sig)
            add_max=max(add_max,add); kak_max=max(kak_max,kres)
            vals=np.asarray([contract(ch,ts,mats,path) for ch in channels],dtype=np.complex128)
            finite=bool(np.all(np.isfinite(vals.real)) and np.all(np.isfinite(vals.imag)))
            maxratio=float(np.max(np.abs(vals))) if finite else float('nan')
            positive=bool(finite and np.isfinite(maxratio) and maxratio>0)
            all_finite=all_finite and finite
            all_positive=all_positive and positive
            logC=(lognorm+math.log(maxratio)) if positive else float('nan')
            logE=(logC+logH) if positive else float('nan')
            rho_rows.append({'rho':float(rho),'log_network_max':logC,'log_haar_density':logH,'log_actual_envelope':logE,'max_normalized_contraction':maxratio})
        per_R[float(R)]={'R':float(R),'cycle_residual':cyc,'escaped_node_etas':etas,'log_haar_density':logH,'rho_rows':rho_rows}

    # Frozen slopes for every rho.
    rho_results=[]; bookkeeping_max=0.0
    logH=[per_R[float(R)]['log_haar_density'] for R in R_GRID]
    h_slope=slope(R_GRID[-3:],logH[-3:])
    for ir,rho in enumerate(RHOS):
        logC=[per_R[float(R)]['rho_rows'][ir]['log_network_max'] for R in R_GRID]
        logE=[per_R[float(R)]['rho_rows'][ir]['log_actual_envelope'] for R in R_GRID]
        ns=slope(R_GRID[-3:],logC[-3:]); ac=slope(R_GRID[-3:],logE[-3:])
        early=slope(R_GRID[:3],logE[:3]); drift=abs(ac-early)
        book=abs((ac-ns)-h_slope); bookkeeping_max=max(bookkeeping_max,book)
        if ac<=DECAY_CEIL and drift<=DRIFT_TOL: state='DECAY'
        elif ac>=NONDECAY_FLOOR and drift<=DRIFT_TOL: state='NONDECAY'
        else: state='ASYMPTOTIC_INCONCLUSIVE'
        rho_results.append({'rho':float(rho),'network_slope':ns,'haar_slope':h_slope,'actual_slope':ac,'early_actual_slope':early,'slope_drift':drift,'haar_bookkeeping_residual':book,'state':state})

    # Independent-edge corruption at R=10. Edge (0,1) is always a cluster crossing edge.
    gs10=escaped_nodes(panel,cluster_size,10.0); rs10=relatives(gs10)
    bad=dict(rs10); bad[(0,1)]=boost(0.417)@bad[(0,1)]
    bad_cycle=cycle_residual(bad)

    # Frozen false-representation control at R=10, inherited from Iter484/485.
    h=rs10[(0,1)]; h2=rs10[(0,2)]; nonrep=[]
    for rho in RHOS:
        _,P21,_=full_direct(h2@h,rho); _,P2,_=full_direct(h2,rho); _,P1,_=full_direct(h,rho)
        nonrep.append(maxabs(P21-P2@P1))
    nonrep_max=max(nonrep)

    controls={
      'shared_node_cycle': cycle_max<CYCLE_TOL,
      'per_edge_kak_reconstruction': kak_max<KAK_TOL,
      'finite_positive_contractions': bool(all_finite and all_positive),
      'haar_radial_slope': abs(h_slope-2.0*cluster_size)<HAAR_SLOPE_TOL,
      'haar_bookkeeping': bookkeeping_max<1e-8,
      'independent_edge_negative': bad_cycle>1e-5,
      'false_toller_composition_negative': nonrep_max>1e-5,
      'intertwiner_controls': bool(int_ok and gramres<1e-12),
      'source_additive_regression': add_max<1e-9,
    }
    valid=bool(all(controls.values()))
    states=[x['state'] for x in rho_results]
    if not valid: cls='INFRASTRUCTURE_OR_SOURCE_FAIL_ITER486'
    elif 'NONDECAY' in states: cls='SCIENTIFIC_FAIL_ITER486_HAAR_ESCAPE_ACTUAL_ENVELOPE'
    elif all(x=='DECAY' for x in states): cls='ITER486_LANE_HAAR_ESCAPE_DECAY'
    else: cls='INCONCLUSIVE_ITER486_HAAR_ESCAPE_ASYMPTOTIC'

    return {
      'iteration':486,'lane':f'{panel}-s{cluster_size}-{causal}','panel':panel,'base_regime':'strong','cluster_size':cluster_size,
      'cluster_nodes':list(range(1,cluster_size+1)),'causal':causal,'valid':valid,'classification':cls,'controls':controls,
      'R_grid':R_GRID.tolist(),'rho_panel':[float(r) for r in RHOS],
      'cycle_residual_max':cycle_max,'kak_reconstruction_max':kak_max,'source_additive_residual_max':add_max,
      'intertwiner_gram_residual':float(gramres),'haar_slope':h_slope,'haar_target_slope':2.0*cluster_size,
      'haar_bookkeeping_residual_max':bookkeeping_max,'independent_edge_cycle_residual':bad_cycle,
      'nonrepresentation_max':nonrep_max,'rho_results':rho_results,
      'per_R':[per_R[float(R)] for R in R_GRID],
      'scope':'full j=1 shared-node ten-edge/intertwiner radial Haar escape diagnostic only; no full Haar/spectral/physical-vertex theorem'
    }


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--panel',required=True,choices=PANELS); ap.add_argument('--cluster',required=True,type=int,choices=[1,2,3,4]); ap.add_argument('--causal',required=True,choices=CAUSALS); ap.add_argument('--out',required=True); args=ap.parse_args()
    try: payload=evaluate(args.panel,args.cluster,args.causal)
    except Exception as e: payload={'iteration':486,'lane':f'{args.panel}-s{args.cluster}-{args.causal}','valid':False,'classification':'INFRASTRUCTURE_OR_SOURCE_FAIL_ITER486','error':repr(e)}
    os.makedirs(os.path.dirname(args.out) or '.',exist_ok=True)
    with open(args.out,'w') as f: json.dump(payload,f,indent=2,sort_keys=True)
    print(json.dumps(payload,indent=2,sort_keys=True))
    # Scientific FAIL/INCONCLUSIVE are valid outputs; aggregate owns the terminal workflow verdict.
    raise SystemExit(0)

if __name__=='__main__': main()

#!/usr/bin/env python3
import argparse, json, os
import numpy as np
import iter486_shared_node_haar_escape as base

REL_NONREP_MIN=1e-6
BASE_ABS_NONREP_MIN=1e-5


def nonrep_metrics(rs):
    h=rs[(0,1)]; h2=rs[(0,2)]
    rel=[]; absolute=[]
    for rho in base.RHOS:
        _,P21,_=base.full_direct(h2@h,rho)
        _,P2,_=base.full_direct(h2,rho)
        _,P1,_=base.full_direct(h,rho)
        prod=P2@P1
        num=base.maxabs(P21-prod)
        den=max(base.maxabs(P21),base.maxabs(prod),1e-300)
        rel.append(float(num/den))
        absolute.append(float(num))
    return rel,absolute


def evaluate(panel,cluster_size,causal):
    # Exact Iter486 scientific object/observables. We discard only its known
    # scale-nonuniform absolute nonrepresentation validity bit.
    x=base.evaluate(panel,cluster_size,causal)

    rs10=base.relatives(base.escaped_nodes(panel,cluster_size,10.0))
    rel10,abs10=nonrep_metrics(rs10)

    rs0=base.relatives(base.nodes(panel,'strong'))
    rel0,abs0=nonrep_metrics(rs0)

    finite_rel=bool(np.all(np.isfinite(rel10)))
    finite_base=bool(np.all(np.isfinite(abs0)))
    controls=dict(x['controls'])
    controls.pop('false_toller_composition_negative',None)
    controls['escaped_relative_nonrepresentation']=bool(finite_rel and max(rel10)>REL_NONREP_MIN)
    controls['base_absolute_nonrepresentation_regression']=bool(finite_base and max(abs0)>BASE_ABS_NONREP_MIN)

    valid=bool(all(controls.values()))
    states=[r['state'] for r in x['rho_results']]
    if not valid:
        cls='INFRASTRUCTURE_OR_SOURCE_FAIL_ITER487'
    elif 'NONDECAY' in states:
        cls='SCIENTIFIC_FAIL_ITER487_HAAR_ESCAPE_ACTUAL_ENVELOPE'
    elif all(s=='DECAY' for s in states):
        cls='ITER487_LANE_HAAR_ESCAPE_DECAY'
    else:
        cls='INCONCLUSIVE_ITER487_HAAR_ESCAPE_ASYMPTOTIC'

    x['iteration']=487
    x['valid']=valid
    x['classification']=cls
    x['controls']=controls
    x['escaped_relative_nonrepresentation_by_rho']=rel10
    x['escaped_relative_nonrepresentation_max']=max(rel10)
    x['escaped_absolute_nonrepresentation_by_rho']=abs10
    x['base_absolute_nonrepresentation_by_rho']=abs0
    x['base_absolute_nonrepresentation_max']=max(abs0)
    x['base_relative_nonrepresentation_by_rho']=rel0
    x['scope']='Iter487 exact Iter486 full j=1 shared-node/intertwiner Haar escape science object with scale-normalized validation only; no full Haar/spectral/physical-vertex theorem'
    return x


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--panel',required=True,choices=base.PANELS)
    ap.add_argument('--cluster',required=True,type=int,choices=[1,2,3,4])
    ap.add_argument('--causal',required=True,choices=base.CAUSALS)
    ap.add_argument('--out',required=True)
    args=ap.parse_args()
    try:
        payload=evaluate(args.panel,args.cluster,args.causal)
    except Exception as e:
        payload={'iteration':487,'lane':f'{args.panel}-s{args.cluster}-{args.causal}','valid':False,'classification':'INFRASTRUCTURE_OR_SOURCE_FAIL_ITER487','error':repr(e)}
    os.makedirs(os.path.dirname(args.out) or '.',exist_ok=True)
    with open(args.out,'w') as f: json.dump(payload,f,indent=2,sort_keys=True)
    print(json.dumps(payload,indent=2,sort_keys=True))
    raise SystemExit(0)

if __name__=='__main__':
    main()

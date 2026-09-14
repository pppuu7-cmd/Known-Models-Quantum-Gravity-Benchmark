#!/usr/bin/env python3
import argparse, json, math, os
import numpy as np

import iter492_tangent_boundary_layer as it
import iter491_high_precision_angular_thickening as hp
import iter490_angular_neighborhood_thickening as parent
import iter486_shared_node_haar_escape as base

H_VALUES=[0.005,0.010]
BLOCKS=[list(range(0,5)),list(range(5,10)),list(range(10,15)),list(range(15,20))]
Q=1.0


def one_eval(causal, coord, sign, h):
    d=np.zeros(20,dtype=float); d[coord]=1.0
    old=it.KAPPA
    try:
        it.KAPPA=float(h)
        out=it.dynamic_eval(causal,d,int(sign),Q)
    finally:
        it.KAPPA=old
    valid=bool(all(out['controls'].values()))
    slopes=[float(r['actual_slope']) for r in out['results']]
    finite=bool(all(math.isfinite(x) for x in slopes))
    return {'coord':coord,'sign':int(sign),'h':float(h),'valid':bool(valid and finite),'slopes':slopes,'raw':out}


def evaluate(causal, block):
    coords=BLOCKS[block]
    center=hp.sample_eval(causal,np.zeros(20,dtype=float),0.0)
    center_slopes=[float(r['actual_slope']) for r in center['results']]
    center_reg=max(abs(a-b) for a,b in zip(center_slopes,parent.CENTER[causal]))
    center_valid=bool(center_reg<5e-3 and all(center['controls'].values()) and all(math.isfinite(x) for x in center_slopes))
    records=[]
    all_valid=center_valid
    for c in coords:
        by_h={}
        for h in H_VALUES:
            minus=one_eval(causal,c,-1,h)
            plus=one_eval(causal,c,+1,h)
            all_valid=all_valid and minus['valid'] and plus['valid']
            D=[]; Q2=[]
            for ir in range(len(base.RHOS)):
                sm=minus['slopes'][ir]; sp=plus['slopes'][ir]; s0=center_slopes[ir]
                D.append((sp-sm)/(2*h))
                Q2.append((sp+sm-2*s0)/(h*h))
            by_h[str(h)]={'minus':minus,'plus':plus,'D':D,'Q':Q2}
        per_rho=[]
        for ir,rho in enumerate(base.RHOS):
            d0=by_h[str(H_VALUES[0])]['D'][ir]; d1=by_h[str(H_VALUES[1])]['D'][ir]
            q0=by_h[str(H_VALUES[0])]['Q'][ir]; q1=by_h[str(H_VALUES[1])]['Q'][ir]
            vals=[d0,d1,q0,q1]
            finite=all(math.isfinite(x) for x in vals)
            all_valid=all_valid and finite
            per_rho.append({
                'rho':float(rho),
                'D_h005':d0,'D_h010':d1,
                'Q_h005':q0,'Q_h010':q1,
                'D_abs_discrepancy':abs(d0-d1),
                'D_scaled_discrepancy':abs(d0-d1)/max(1.0,abs(d0),abs(d1)),
                'Q_abs_discrepancy':abs(q0-q1),
                'Q_scaled_discrepancy':abs(q0-q1)/max(1.0,abs(q0),abs(q1)),
                'D_sign_stable':bool(d0==0.0 or d1==0.0 or (d0>0)==(d1>0)),
                'finite':bool(finite),
            })
        records.append({'coord':c,'by_h':by_h,'per_rho':per_rho})
    cls='ITER493_CRITICAL_Q1_LOCAL_VARIATION_QUALIFIED_SCOPED' if all_valid else 'INFRASTRUCTURE_OR_NUMERICAL_FAIL_ITER493'
    return {
        'iteration':493,'job':f'{causal}-b{block}','causal':causal,'block':block,'coords':coords,
        'q':Q,'h_values':H_VALUES,'center_valid':center_valid,'center_regression_max_abs':center_reg,
        'center_slopes':center_slopes,'records':records,'valid':bool(all_valid),'classification':cls,
        'scope':'finite-grid critical-q1 local first/second angular variation only; not an analytic/uniform or positive-measure theorem'
    }


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--causal',required=True,choices=base.CAUSALS); ap.add_argument('--block',required=True,type=int,choices=range(4)); ap.add_argument('--out',required=True); a=ap.parse_args()
    try: out=evaluate(a.causal,a.block)
    except Exception as e: out={'iteration':493,'job':f'{a.causal}-b{a.block}','causal':a.causal,'block':a.block,'valid':False,'classification':'INFRASTRUCTURE_OR_NUMERICAL_FAIL_ITER493','error':repr(e)}
    os.makedirs(os.path.dirname(a.out) or '.',exist_ok=True)
    with open(a.out,'w') as f: json.dump(out,f,indent=2,sort_keys=True)
    print(json.dumps(out,indent=2,sort_keys=True))
    raise SystemExit(0)

if __name__=='__main__': main()

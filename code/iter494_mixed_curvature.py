#!/usr/bin/env python3
import argparse, json, math, os
import numpy as np

import iter492_tangent_boundary_layer as it
import iter486_shared_node_haar_escape as base

COORDS=[0,1,3,5,6,11]
PAIRS=[(COORDS[i],COORDS[j]) for i in range(len(COORDS)) for j in range(i+1,len(COORDS))]
BLOCKS=[PAIRS[0:5],PAIRS[5:10],PAIRS[10:15]]
H_VALUES=[0.005,0.010]
Q=1.0


def corner_eval(causal,i,j,si,sj,h):
    d=np.zeros(20,dtype=float)
    d[i]=float(si); d[j]=float(sj)
    old=it.KAPPA
    try:
        it.KAPPA=float(h)
        out=it.dynamic_eval(causal,d,1,Q)
    finally:
        it.KAPPA=old
    slopes=[float(r['actual_slope']) for r in out['results']]
    valid=bool(all(out['controls'].values()) and all(math.isfinite(x) for x in slopes))
    return {'i':i,'j':j,'si':si,'sj':sj,'h':float(h),'valid':valid,'slopes':slopes,'raw':out}


def evaluate(causal,block):
    records=[]; all_valid=True
    for i,j in BLOCKS[block]:
        by_h={}
        for h in H_VALUES:
            pp=corner_eval(causal,i,j,+1,+1,h)
            pm=corner_eval(causal,i,j,+1,-1,h)
            mp=corner_eval(causal,i,j,-1,+1,h)
            mm=corner_eval(causal,i,j,-1,-1,h)
            all_valid = all_valid and pp['valid'] and pm['valid'] and mp['valid'] and mm['valid']
            M=[]
            for ir in range(len(base.RHOS)):
                val=(pp['slopes'][ir]-pm['slopes'][ir]-mp['slopes'][ir]+mm['slopes'][ir])/(4*h*h)
                M.append(float(val))
                all_valid = all_valid and math.isfinite(val)
            by_h[str(h)]={'pp':pp,'pm':pm,'mp':mp,'mm':mm,'M':M}
        per_rho=[]
        for ir,rho in enumerate(base.RHOS):
            m0=by_h[str(H_VALUES[0])]['M'][ir]
            m1=by_h[str(H_VALUES[1])]['M'][ir]
            per_rho.append({
                'rho':float(rho),'M_h005':m0,'M_h010':m1,
                'abs_discrepancy':abs(m0-m1),
                'scaled_discrepancy':abs(m0-m1)/max(1.0,abs(m0),abs(m1)),
                'sign_stable':bool(m0==0.0 or m1==0.0 or (m0>0)==(m1>0))
            })
        records.append({'pair':[i,j],'by_h':by_h,'per_rho':per_rho})
    cls='ITER494_CRITICAL_Q1_MIXED_CURVATURE_QUALIFIED_SCOPED' if all_valid else 'INFRASTRUCTURE_OR_NUMERICAL_FAIL_ITER494'
    return {'iteration':494,'job':f'{causal}-b{block}','causal':causal,'block':block,'pairs':BLOCKS[block],
            'q':Q,'h_values':H_VALUES,'records':records,'valid':bool(all_valid),'classification':cls,
            'scope':'finite-grid q1 mixed-curvature prerequisite only; not an interval/uniform or positive-measure theorem'}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--causal',required=True,choices=base.CAUSALS); ap.add_argument('--block',required=True,type=int,choices=range(3)); ap.add_argument('--out',required=True); a=ap.parse_args()
    try: out=evaluate(a.causal,a.block)
    except Exception as e: out={'iteration':494,'job':f'{a.causal}-b{a.block}','causal':a.causal,'block':a.block,'valid':False,'classification':'INFRASTRUCTURE_OR_NUMERICAL_FAIL_ITER494','error':repr(e)}
    os.makedirs(os.path.dirname(a.out) or '.',exist_ok=True)
    with open(a.out,'w') as f: json.dump(out,f,indent=2,sort_keys=True)
    print(json.dumps(out,indent=2,sort_keys=True))
    raise SystemExit(0)

if __name__=='__main__': main()

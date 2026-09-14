#!/usr/bin/env python3
import argparse, json, math, os
import numpy as np
import iter495_multivariate_taylor_stress as prev
import iter486_shared_node_haar_escape as base

HS=[0.0050,0.0025,0.00125]
AMPS=[0.00125,0.0025]
COORDS=prev.COORDS
BLOCKS=prev.BLOCKS


def coeff_at(causal,h):
    old=prev.H0
    try:
        prev.H0=float(h)
        c=prev.coefficients(causal)
    finally:
        prev.H0=old
    return c


def richardson(c1,c2):
    # c1 = h=0.0025, c2 = h=0.00125
    out={'valid':bool(c1['valid'] and c2['valid']), 's0':[float(x) for x in c2['s0']]}
    out['D']=((4*np.array(c2['D'],float)-np.array(c1['D'],float))/3.0).tolist()
    out['Qii']=((4*np.array(c2['Qii'],float)-np.array(c1['Qii'],float))/3.0).tolist()
    out['M']=((4*np.array(c2['M'],float)-np.array(c1['M'],float))/3.0).tolist()
    return out


def t2(c,ir,x):
    val=float(c['s0'][ir])
    val += sum(float(c['D'][ir][k])*x[k] for k in range(len(COORDS)))
    val += 0.5*sum(float(c['Qii'][ir][k])*x[k]*x[k] for k in range(len(COORDS)))
    for a in range(len(COORDS)):
        for b in range(a+1,len(COORDS)):
            val += float(c['M'][ir][a][b])*x[a]*x[b]
    return float(val)


def flat(c,key):
    a=np.array(c[key],float)
    if key=='M':
        vals=[]
        for ir in range(a.shape[0]):
            for i in range(a.shape[1]):
                for j in range(i+1,a.shape[2]): vals.append(a[ir,i,j])
        return np.array(vals,float)
    return a.reshape(-1)


def evaluate(causal,block):
    coeffs={str(h):coeff_at(causal,h) for h in HS}
    cr=richardson(coeffs[str(HS[1])],coeffs[str(HS[2])])
    valid=all(c['valid'] for c in coeffs.values()) and cr['valid']
    convergence={}
    for key in ['D','Qii','M']:
        a0,a1,a2=[flat(coeffs[str(h)],key) for h in HS]
        d01=np.abs(a1-a0); d12=np.abs(a2-a1)
        ratio=d12/np.maximum(d01,1e-300)
        convergence[key]={
            'delta_h0_h1_max':float(np.max(d01)),'delta_h0_h1_median':float(np.median(d01)),
            'delta_h1_h2_max':float(np.max(d12)),'delta_h1_h2_median':float(np.median(d12)),
            'halving_ratio_max':float(np.max(ratio)),'halving_ratio_median':float(np.median(ratio))}
    records=[]
    labels=[str(h) for h in HS]+['richardson']
    cset={str(h):coeffs[str(h)] for h in HS}; cset['richardson']=cr
    for d in BLOCKS[block]:
        for sg in [1,-1]:
            ds=[float(sg*x) for x in d]
            by_amp={}
            for amp in AMPS:
                act=prev.eval_vec(causal,ds,amp); valid=valid and act['valid']
                x=[amp*v for v in ds]
                rows=[]
                for ir,rho in enumerate(base.RHOS):
                    preds={lab:t2(cset[lab],ir,x) for lab in labels}
                    actual=float(act['slopes'][ir])
                    rr={lab:float(actual-preds[lab]) for lab in labels}
                    base_abs=abs(rr[str(HS[0])]); rich_abs=abs(rr['richardson'])
                    rows.append({'rho':float(rho),'actual':actual,'predictions':preds,'remainders':rr,
                                 'abs_remainders':{k:abs(v) for k,v in rr.items()},
                                 'richardson_suppression_ratio':float(rich_abs/max(base_abs,1e-300))})
                    valid=valid and math.isfinite(actual) and all(math.isfinite(v) for v in preds.values()) and all(math.isfinite(v) for v in rr.values())
                by_amp[str(amp)]={'per_rho':rows}
            ratios=[]
            for ir,rho in enumerate(base.RHOS):
                row={}
                for lab in labels:
                    rs=abs(by_amp[str(AMPS[0])]['per_rho'][ir]['remainders'][lab])
                    rl=abs(by_amp[str(AMPS[1])]['per_rho'][ir]['remainders'][lab])
                    row[lab]=float(rs/max(rl,1e-300))
                ratios.append({'rho':float(rho),'small_over_large':row,'cubic_expected_ratio':0.125})
            records.append({'direction':d,'sign':sg,'by_amp':by_amp,'remainder_ratios':ratios})
    cls='ITER496_COEFFICIENT_STENCIL_CONVERGENCE_QUALIFIED_SCOPED' if valid else 'INFRASTRUCTURE_OR_NUMERICAL_FAIL_ITER496'
    return {'iteration':496,'job':f'{causal}-b{block}','causal':causal,'block':block,'h_levels':HS,'amps':AMPS,
            'convergence':convergence,'records':records,'valid':bool(valid),'classification':cls,
            'scope':'finite-set coefficient-stencil convergence and Richardson diagnostic only; not interval/uniform or positive-measure theorem'}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--causal',required=True,choices=base.CAUSALS); ap.add_argument('--block',required=True,type=int,choices=range(4)); ap.add_argument('--out',required=True); a=ap.parse_args()
    try: out=evaluate(a.causal,a.block)
    except Exception as e: out={'iteration':496,'job':f'{a.causal}-b{a.block}','valid':False,'classification':'INFRASTRUCTURE_OR_NUMERICAL_FAIL_ITER496','error':repr(e)}
    os.makedirs(os.path.dirname(a.out) or '.',exist_ok=True)
    with open(a.out,'w') as f: json.dump(out,f,indent=2,sort_keys=True)
    print(json.dumps(out,indent=2,sort_keys=True)); raise SystemExit(0)
if __name__=='__main__': main()

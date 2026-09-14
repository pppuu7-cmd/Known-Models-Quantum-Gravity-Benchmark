#!/usr/bin/env python3
import argparse, json, math, os
import numpy as np

import iter492_tangent_boundary_layer as it
import iter486_shared_node_haar_escape as base

COORDS=[0,1,3,5,6,11]
DIRS=[
 [1,1,1,1,1,1], [1,1,1,-1,-1,-1], [1,-1,-1,1,1,-1], [1,-1,1,-1,1,-1],
 [1,1,-1,1,-1,-1], [1,-1,1,1,-1,1], [1,1,-1,-1,1,1], [1,-1,-1,-1,-1,1]
]
BLOCKS=[DIRS[0:2],DIRS[2:4],DIRS[4:6],DIRS[6:8]]
H0=0.005
AMPS=[0.0025,0.0050]
Q=1.0


def eval_vec(causal, vec, amp):
    d=np.zeros(20,dtype=float)
    for k,c in enumerate(COORDS): d[c]=float(vec[k])
    old=it.KAPPA
    try:
        it.KAPPA=float(amp)
        out=it.dynamic_eval(causal,d,1,Q)
    finally:
        it.KAPPA=old
    slopes=[float(r['actual_slope']) for r in out['results']]
    valid=bool(all(out['controls'].values()) and all(math.isfinite(x) for x in slopes))
    return {'amp':float(amp),'vec':[float(x) for x in vec],'slopes':slopes,'valid':valid,'controls':out['controls']}


def coefficients(causal):
    z=[0.0]*len(COORDS)
    cen=eval_vec(causal,z,H0)
    s0=cen['slopes']
    D=[[0.0]*len(COORDS) for _ in base.RHOS]
    Qii=[[0.0]*len(COORDS) for _ in base.RHOS]
    valid=cen['valid']
    one={}
    for k,c in enumerate(COORDS):
        vp=[0.0]*len(COORDS); vm=[0.0]*len(COORDS); vp[k]=1.0; vm[k]=-1.0
        p=eval_vec(causal,vp,H0); m=eval_vec(causal,vm,H0); valid=valid and p['valid'] and m['valid']
        one[str(c)]={'p':p,'m':m}
        for ir in range(len(base.RHOS)):
            D[ir][k]=(p['slopes'][ir]-m['slopes'][ir])/(2*H0)
            Qii[ir][k]=(p['slopes'][ir]-2*s0[ir]+m['slopes'][ir])/(H0*H0)
    M=[[[0.0]*len(COORDS) for _ in COORDS] for __ in base.RHOS]
    pairs={}
    for a in range(len(COORDS)):
        for b in range(a+1,len(COORDS)):
            vals={}
            for sa,sb,key in [(1,1,'pp'),(1,-1,'pm'),(-1,1,'mp'),(-1,-1,'mm')]:
                v=[0.0]*len(COORDS); v[a]=float(sa); v[b]=float(sb)
                vals[key]=eval_vec(causal,v,H0); valid=valid and vals[key]['valid']
            pairs[f'{COORDS[a]}-{COORDS[b]}']=vals
            for ir in range(len(base.RHOS)):
                mij=(vals['pp']['slopes'][ir]-vals['pm']['slopes'][ir]-vals['mp']['slopes'][ir]+vals['mm']['slopes'][ir])/(4*H0*H0)
                M[ir][a][b]=M[ir][b][a]=float(mij)
    return {'valid':bool(valid),'center':cen,'s0':s0,'D':D,'Qii':Qii,'M':M}


def t2(coeff, ir, x):
    val=float(coeff['s0'][ir])
    val += sum(float(coeff['D'][ir][k])*x[k] for k in range(len(COORDS)))
    val += 0.5*sum(float(coeff['Qii'][ir][k])*x[k]*x[k] for k in range(len(COORDS)))
    for a in range(len(COORDS)):
        for b in range(a+1,len(COORDS)):
            val += float(coeff['M'][ir][a][b])*x[a]*x[b]
    return float(val)


def evaluate(causal,block):
    coeff=coefficients(causal); valid=coeff['valid']; records=[]
    for d in BLOCKS[block]:
        for sg in [1,-1]:
            ds=[float(sg*x) for x in d]
            by_amp={}
            for amp in AMPS:
                act=eval_vec(causal,ds,amp); valid=valid and act['valid']
                per=[]
                x=[amp*v for v in ds]
                for ir,rho in enumerate(base.RHOS):
                    pred=t2(coeff,ir,x); actual=float(act['slopes'][ir]); r=actual-pred
                    per.append({'rho':float(rho),'actual':actual,'T2':pred,'remainder':float(r),'abs_remainder':abs(r),
                                'r_over_a2':abs(r)/(amp**2),'r_over_a3':abs(r)/(amp**3)})
                    valid=valid and all(math.isfinite(v) for v in [pred,actual,r])
                by_amp[str(amp)]={'actual':act,'per_rho':per}
            ratio=[]
            for ir,rho in enumerate(base.RHOS):
                rsmall=by_amp[str(AMPS[0])]['per_rho'][ir]['abs_remainder']
                rlarge=by_amp[str(AMPS[1])]['per_rho'][ir]['abs_remainder']
                ratio.append({'rho':float(rho),'small_over_large':float(rsmall/max(rlarge,1e-300)),
                              'cubic_expected_ratio':float((AMPS[0]/AMPS[1])**3)})
            records.append({'direction':d,'sign':sg,'by_amp':by_amp,'remainder_ratio':ratio})
    cls='ITER495_MULTIVARIATE_TAYLOR_STRESS_QUALIFIED_SCOPED' if valid else 'INFRASTRUCTURE_OR_NUMERICAL_FAIL_ITER495'
    return {'iteration':495,'job':f'{causal}-b{block}','causal':causal,'block':block,'coords':COORDS,'directions':BLOCKS[block],
            'h0':H0,'amps':AMPS,'q':Q,'coefficients':coeff,'records':records,'valid':bool(valid),'classification':cls,
            'scope':'prospectively frozen finite-set multivariate q1 Taylor stress only; not interval/uniform or positive-measure theorem'}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--causal',required=True,choices=base.CAUSALS); ap.add_argument('--block',required=True,type=int,choices=range(4)); ap.add_argument('--out',required=True); a=ap.parse_args()
    try: out=evaluate(a.causal,a.block)
    except Exception as e: out={'iteration':495,'job':f'{a.causal}-b{a.block}','causal':a.causal,'block':a.block,'valid':False,'classification':'INFRASTRUCTURE_OR_NUMERICAL_FAIL_ITER495','error':repr(e)}
    os.makedirs(os.path.dirname(a.out) or '.',exist_ok=True)
    with open(a.out,'w') as f: json.dump(out,f,indent=2,sort_keys=True)
    print(json.dumps(out,indent=2,sort_keys=True))
    raise SystemExit(0)

if __name__=='__main__': main()

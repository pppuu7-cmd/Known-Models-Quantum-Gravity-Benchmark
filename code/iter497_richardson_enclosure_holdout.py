#!/usr/bin/env python3
import argparse, json, math, os
import numpy as np
import iter496_coefficient_stencil_convergence as prev
import iter486_shared_node_haar_escape as base

TRAIN=[0.00125,0.0025]
HOLD=[0.00150,0.00175,0.00200,0.00225]
COORDS=prev.COORDS
BLOCKS=prev.BLOCKS
SAFETY=2.0


def coeff_uncertainty(cmid,cfine):
    out={}
    for key in ['D','Qii','M']:
        out[key]=(4.0/3.0)*np.abs(np.array(cfine[key],float)-np.array(cmid[key],float))
    return out


def ec_bound(ec,ir,x):
    x=np.array(x,float)
    val=float(np.sum(ec['D'][ir]*np.abs(x)))
    val += 0.5*float(np.sum(ec['Qii'][ir]*(x*x)))
    M=ec['M'][ir]
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            val += float(M[i,j]*abs(x[i]*x[j]))
    return float(val)


def evaluate(causal,block):
    cmid=prev.coeff_at(causal,0.0025)
    cfine=prev.coeff_at(causal,0.00125)
    cr=prev.richardson(cmid,cfine)
    ec=coeff_uncertainty(cmid,cfine)
    valid=bool(cmid['valid'] and cfine['valid'] and cr['valid'])
    rows=[]; covered=0; total=0
    for d in BLOCKS[block]:
        for sg in [1,-1]:
            ds=[float(sg*v) for v in d]
            train_actual={a:prev.prev.eval_vec(causal,ds,a) for a in TRAIN}
            hold_actual={a:prev.prev.eval_vec(causal,ds,a) for a in HOLD}
            valid = valid and all(z['valid'] for z in train_actual.values()) and all(z['valid'] for z in hold_actual.values())
            for ir,rho in enumerate(base.RHOS):
                kres=[]
                train_detail=[]
                for a in TRAIN:
                    x=[a*v for v in ds]
                    pred=prev.t2(cr,ir,x)
                    actual=float(train_actual[a]['slopes'][ir])
                    r=abs(actual-pred)
                    k=float(r/(a**3))
                    kres.append(k)
                    train_detail.append({'amplitude':a,'actual':actual,'prediction':pred,'abs_remainder':r,'cubic_normalized':k})
                K3=max(kres)
                holds=[]
                for a in HOLD:
                    x=[a*v for v in ds]
                    pred=prev.t2(cr,ir,x)
                    actual=float(hold_actual[a]['slopes'][ir])
                    resid=abs(actual-pred)
                    e3=float(SAFETY*K3*(a**3))
                    ecoef=ec_bound(ec,ir,x)
                    etot=float(e3+ecoef)
                    slack=1e-12*max(1.0,etot,abs(actual),abs(pred))
                    ok=bool(resid <= etot+slack)
                    ratio=float(resid/max(etot,1e-300))
                    holds.append({'amplitude':a,'actual':actual,'prediction':pred,'abs_remainder':resid,'E3':e3,'EC':ecoef,'E_total':etot,'coverage_ratio':ratio,'covered':ok})
                    total+=1; covered+=int(ok)
                    valid = valid and all(math.isfinite(v) for v in [pred,actual,resid,e3,ecoef,etot,ratio])
                rows.append({'direction':d,'sign':sg,'rho':float(rho),'K3':float(K3),'training':train_detail,'holdouts':holds})
    all_covered=bool(covered==total)
    if not valid:
        cls='INFRASTRUCTURE_OR_NUMERICAL_FAIL_ITER497'
    elif all_covered:
        cls='ITER497_RICHARDSON_ENCLOSURE_HOLDOUT_QUALIFIED_SCOPED'
    else:
        cls='SCIENTIFIC_FAIL_ITER497_RICHARDSON_ENCLOSURE_HOLDOUT'
    return {'iteration':497,'job':f'{causal}-b{block}','causal':causal,'block':block,
            'training_amplitudes':TRAIN,'holdout_amplitudes':HOLD,'safety_factor':SAFETY,
            'n_holdouts':total,'n_covered':covered,'all_covered':all_covered,'records':rows,
            'valid':bool(valid),'classification':cls,
            'scope':'finite preregistered holdout validation only; not a continuous interval/uniform or positive-measure theorem'}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--causal',required=True,choices=base.CAUSALS); ap.add_argument('--block',required=True,type=int,choices=range(4)); ap.add_argument('--out',required=True); a=ap.parse_args()
    try: out=evaluate(a.causal,a.block)
    except Exception as e: out={'iteration':497,'job':f'{a.causal}-b{a.block}','valid':False,'classification':'INFRASTRUCTURE_OR_NUMERICAL_FAIL_ITER497','error':repr(e)}
    os.makedirs(os.path.dirname(a.out) or '.',exist_ok=True)
    with open(a.out,'w') as f: json.dump(out,f,indent=2,sort_keys=True)
    print(json.dumps(out,indent=2,sort_keys=True)); raise SystemExit(0)
if __name__=='__main__': main()

#!/usr/bin/env python3
import argparse, json, math, pathlib
import mpmath as mp

mp.mp.dps = 60
Z_DEFAULT = [0.005,0.01,0.02,0.05,0.1,0.25,0.5,1.0]

def kernel(z, h):
    z = mp.mpf(str(z)); h = mp.mpf(str(h)); nu = mp.mpf('1.5')
    H = mp.hankel1(nu, z)
    dH = (mp.hankel1(nu+h, z)-mp.hankel1(nu-h, z))/(2*h)
    return mp.re(2*dH/H)

def converged_kernel(z):
    a = kernel(z, mp.mpf('1e-4'))
    b = kernel(z, mp.mpf('5e-5'))
    rel = abs(a-b)/max(mp.mpf('1.0'), abs(b))
    if not rel < mp.mpf('1e-6'):
        raise RuntimeError(f'order-derivative convergence failed z={z}: {rel}')
    return float(b), float(rel)

def write(path, obj):
    pathlib.Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path,'w') as f: json.dump(obj,f,indent=2,sort_keys=True)
    print(json.dumps(obj,sort_keys=True))

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--mode',choices=['kernel','scalar','tensor','evidence'],required=True)
    p.add_argument('--z',type=float)
    p.add_argument('--N',type=float)
    p.add_argument('--x',type=float,default=0.0,help='beta/(12 alpha)')
    p.add_argument('--output',required=True)
    a=p.parse_args()
    if a.mode=='kernel':
        assert a.z and a.z>0
        K, rel=converged_kernel(a.z)
        out={'iteration':374,'z_k_over_kstar':a.z,'kernel_K':K,'finite_difference_relative_change':rel,
             'classification':'PASS_SOURCE_DEFINED_HANKEL_KERNEL_NUMERICAL_CONVERGENCE'}
    elif a.mode=='scalar':
        assert a.N and a.N>0
        ns=1.0-2.0/a.N
        pts=[]
        for z in Z_DEFAULT:
            K,rel=converged_kernel(z)
            dp=(1.0-ns)*K
            pts.append({'z':z,'K':K,'DeltaP_v':dp,'fd_rel':rel})
        out={'iteration':375,'N':a.N,'n_s_from_eq_7_17':ns,'points':pts,
             'parity_symmetric_baseline_DeltaP_v':0.0,
             'classification':'PASS_SCOPED_SOURCE_DEFINED_SCALAR_PARITY_SHAPE'}
    elif a.mode=='tensor':
        assert a.N and a.N>0 and 0.0<=a.x<1.0
        r=(12.0/(a.N*a.N))/(1.0-a.x)
        pts=[]
        for z in Z_DEFAULT:
            K,rel=converged_kernel(z)
            dpu=(r/8.0)*K
            pts.append({'z':z,'K':K,'DeltaP_u':dpu,'fd_rel':rel})
        out={'iteration':376,'N':a.N,'x_beta_over_12alpha':a.x,'r_from_eq_7_39':r,'points':pts,
             'parity_symmetric_baseline_DeltaP_u':0.0,
             'classification':'PASS_SCOPED_SOURCE_DEFINED_TENSOR_PARITY_SHAPE'}
    else:
        out={'iteration':377,'reported_R_TT':0.79,'reported_ellmax_domain':'approximately <=20-30',
             'reported_posterior_odds_DSI_over_SI':650.0,
             'likelihood_or_covariance_payload_present_in_current_source':False,
             'posterior_odds_recomputed_here':False,
             'classification':'PASS_SOURCE_EVIDENCE_POINTER__REPRODUCIBLE_LIKELIHOOD_OBJECT_STILL_OPEN'}
    write(a.output,out)

if __name__=='__main__': main()

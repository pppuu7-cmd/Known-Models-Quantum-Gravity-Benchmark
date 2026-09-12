#!/usr/bin/env python3
import argparse, json, math
from pathlib import Path
import mpmath as mp
import numpy as np
from scipy.special import spherical_jn

mp.mp.dps = 50
KSTAR = 0.05
KS = 7.0e-5
TABLE = {
  0.04:[0.582,1.385,0.641,1.339,0.678,1.305,0.708,1.277,0.734,1.254,0.759,1.233,0.781,1.208,0.799,1.188,0.825,1.169,0.840],
  0.025:[0.589,1.373,0.657,1.320,0.705,1.278,0.743,1.235,0.776,1.203,0.824,1.165,0.845,1.126,0.916,1.045,0.980,1.007,0.998],
  0.02:[0.594,1.363,0.667,1.305,0.725,1.258,0.770,1.199,0.814,1.168,0.875,1.073,0.967,1.012,0.996,1.001,1.000,1.000,1.000]
}

def hankel_kernel(z, h=5e-5):
    z=mp.mpf(str(z)); h=mp.mpf(str(h)); nu=mp.mpf('1.5')
    H=mp.hankel1(nu,z)
    dH=(mp.hankel1(nu+h,z)-mp.hankel1(nu-h,z))/(2*h)
    return float(mp.re(2*dH/H))

def kernel_grid(x, ns):
    z=np.maximum(x*KS/KSTAR, 1e-14)
    K=np.array([hankel_kernel(v) for v in z], dtype=float)
    return (1.0-ns)*K

def compute(ns, cutoff, num_grid=1400, den_grid=90000, den_xmax=5000.0):
    assert cutoff in TABLE and 0 < ns < 1
    xmin=1e-6
    xc=cutoff*KSTAR/KS
    xn=np.geomspace(xmin,xc,num_grid)
    dp=kernel_grid(xn,ns)
    xd=np.geomspace(xmin,den_xmax,den_grid)
    target=TABLE[cutoff]
    rows=[]
    si_even=si_odd=dsi_even=dsi_odd=0.0
    for ell in range(2,21):
        jd=spherical_jn(ell,xd)
        den=float(np.trapezoid((xd**(ns-2.0))*jd*jd,xd))
        jn=spherical_jn(ell,xn)
        num=float(np.trapezoid((xn**(ns-2.0))*jn*jn*dp,xn))
        delta=num/den
        modulation=1.0+delta if ell%2 else 1.0-delta
        tgt=target[ell-2]
        rows.append({'ell':ell,'C_SI_reduced':den,'DeltaC':delta,'modulation':modulation,'table4_target':tgt,'residual':modulation-tgt})
        w=ell*(ell+1.0)*den
        if ell%2:
            si_odd += w; dsi_odd += w*modulation
        else:
            si_even += w; dsi_even += w*modulation
    residuals=np.array([r['residual'] for r in rows])
    mods=np.array([r['modulation'] for r in rows])
    tgts=np.array([r['table4_target'] for r in rows])
    # Independent order-derivative step test at representative source-domain points.
    zchecks=np.geomspace(1e-5,cutoff,12)
    fd=[]
    for z in zchecks:
        a=hankel_kernel(z,1e-4); b=hankel_kernel(z,5e-5)
        fd.append(abs(a-b)/max(1.0,abs(b)))
    parity_ok=all((r['modulation']<1.0 if r['ell']%2==0 else r['modulation']>1.0) for r in rows[:8])
    out={
      'record_type':'cmb_transport','ns':ns,'cutoff_fraction':cutoff,'kstar':KSTAR,'ks':KS,'xc_k_over_ks':xc,
      'num_grid':num_grid,'den_grid':den_grid,'den_xmax':den_xmax,'ell_min':2,'ell_max':20,
      'rows':rows,'rmse_to_table4':float(np.sqrt(np.mean(residuals**2))),
      'max_abs_residual_to_table4':float(np.max(np.abs(residuals))),
      'mean_abs_residual_to_table4':float(np.mean(np.abs(residuals))),
      'table4_correlation':float(np.corrcoef(mods,tgts)[0,1]),
      'max_hankel_fd_relative_change':float(max(fd)),
      'low_l_even_odd_sign_pattern_correct':parity_ok,
      'R_TT_SI_reduced_l2_l20':si_even/si_odd,
      'R_TT_DSI_reduced_l2_l20':dsi_even/dsi_odd,
      'R_TT_shift_DSI_minus_SI':dsi_even/dsi_odd-si_even/si_odd,
      'classification':'SOURCE_FORMULA_TRANSPORT_NUMERIC_AUDIT'
    }
    return out

def convergence(ns, cutoff):
    coarse=compute(ns,cutoff,700,45000,2500.0)
    fine=compute(ns,cutoff,1400,90000,5000.0)
    cm={r['ell']:r['modulation'] for r in coarse['rows']}; fm={r['ell']:r['modulation'] for r in fine['rows']}
    diffs=[abs(cm[l]-fm[l]) for l in cm]
    return {
      'record_type':'transport_convergence','ns':ns,'cutoff_fraction':cutoff,
      'coarse':{'num_grid':700,'den_grid':45000,'den_xmax':2500.0},
      'fine':{'num_grid':1400,'den_grid':90000,'den_xmax':5000.0},
      'max_abs_modulation_change':max(diffs),'mean_abs_modulation_change':sum(diffs)/len(diffs),
      'rmse_table4_coarse':coarse['rmse_to_table4'],'rmse_table4_fine':fine['rmse_to_table4'],
      'classification':'PASS_NUMERICAL_TRANSPORT_CONVERGENCE' if max(diffs)<2e-4 else 'FAIL_NUMERICAL_TRANSPORT_CONVERGENCE'
    }

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--mode',choices=['transport','convergence'],required=True)
    p.add_argument('--ns',type=float,required=True)
    p.add_argument('--cutoff',type=float,required=True)
    p.add_argument('--output',required=True)
    a=p.parse_args()
    obj=compute(a.ns,a.cutoff) if a.mode=='transport' else convergence(a.ns,a.cutoff)
    Path(a.output).parent.mkdir(parents=True,exist_ok=True)
    Path(a.output).write_text(json.dumps(obj,indent=2,sort_keys=True)+'\n')
    print(json.dumps(obj,sort_keys=True))
    if obj.get('record_type')=='transport':
        if not obj['low_l_even_odd_sign_pattern_correct'] or obj['max_hankel_fd_relative_change']>=1e-6:
            raise SystemExit(2)
    else:
        if not obj['classification'].startswith('PASS'):
            raise SystemExit(2)

if __name__=='__main__': main()

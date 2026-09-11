#!/usr/bin/env python3
import argparse, math
from as_spectral_common import SOURCE,A,GSTAR,beta,trajectory,write_json

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); a=ap.parse_args()
 exact_res=abs(2*GSTAR-A*GSTAR*GSTAR)
 ks=[1e-3,1e-2,1e-1,1,10,100,1000]
 rows=[]; maxrel=0.0
 for k in ks:
  h=1e-5
  gp=trajectory(k*math.exp(h)); gm=trajectory(k*math.exp(-h)); g=trajectory(k)
  dlog=(gp-gm)/(2*h); b=beta(g)
  rel=abs(dlog-b)/max(abs(dlog),abs(b),1e-300); maxrel=max(maxrel,rel)
  rows.append({'k_over_Mpl':k,'g':g,'d_g_d_logk_numeric':dlog,'beta':b,'relative_residual':rel})
 write_json(a.output,{'probe':'as_spectral_rg_trajectory','source':SOURCE,'gstar_exact':GSTAR,'gstar_vs_reported_0p955_abs':abs(GSTAR-0.955),'fixed_point_beta_abs':exact_res,'rows':rows,'max_trajectory_relative_residual':maxrel,'boundary':'Checks Eq.23-25 internal consistency only; not an independent spectral-flow reproduction.'})
if __name__=='__main__': main()

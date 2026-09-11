#!/usr/bin/env python3
import argparse, math
from as_spectral_common import SOURCE,write_json

def tail_integral_p3(l0,linf):
 u0=math.log(l0*l0); u1=math.log(linf*linf)
 return 0.25*(1.0/(u0*u0)-1.0/(u1*u1))

def tail_integral_p3_to_inf(l0):
 u0=math.log(l0*l0); return 0.25/(u0*u0)

def tail_integral_p1(l0,linf):
 u0=math.log(l0*l0); u1=math.log(linf*linf)
 return 0.5*math.log(u1/u0)

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); a=ap.parse_args()
 l0=10.0; uppers=[1e2,1e4,1e8,1e16,1e32]
 limit=tail_integral_p3_to_inf(l0)
 rows=[]
 for hi in uppers:
  v3=tail_integral_p3(l0,hi); v1=tail_integral_p1(l0,hi)
  rows.append({'upper':hi,'p3_integral':v3,'p3_fraction_of_infinite_limit':v3/limit,'p3_remaining_fraction':1-v3/limit,'p1_integral':v1})
 write_json(a.output,{'probe':'as_spectral_uv_tail_integrability','source':SOURCE,'lower':l0,'p3_infinite_limit_unit_prefactor':limit,'rows':rows,'result':'PUBLISHED_1_OVER_LAMBDA2_LOG3_TAIL_IS_SUM_RULE_INTEGRABLE__SIMPLE_LOG_POWER1_IS_NOT','boundary':'Checks the analytic asymptotic tail and integration measure only; the numerical UV prefactor and full spectral curve are not reproduced.'})
if __name__=='__main__': main()

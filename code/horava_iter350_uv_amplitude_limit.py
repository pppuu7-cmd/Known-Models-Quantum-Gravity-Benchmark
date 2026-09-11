#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path
import mpmath as mp

# Source: Radkovski & Sibiryakov, arXiv:2306.00102, Appendix D Eq. (D.9),
# special case u_s=1 for f_{++,+s}. Evaluate the published rational
# expression and its exact lambda->infinity leading-coefficient limit.
mp.mp.dps=80
COUPLINGS={'zero':(mp.mpf('0'),mp.mpf('0')),'v2p1':(mp.mpf('1'),mp.mpf('0')),'v3p1':(mp.mpf('0'),mp.mpf('1')),'mixedA':(mp.mpf('1'),mp.mpf('-1')),'mixedB':(mp.mpf('-1'),mp.mpf('2')),'mixedC':(mp.mpf('2'),mp.mpf('0.5'))}

def f_d9(L,v2,v3,x):
    b6=(81+80*v2**2*(1-L)**2-245*L+230*L**2+18*v3**2*(5-8*L+3*L**2)-3*v3*(31-21*L-8*L**2)-4*v2*(1-L)*(49-80*L-v3*(48-51*L)))
    b4=(447+240*v2**2*(1-L)**2-1175*L+402*L**2+18*v3**2*(17-38*L+21*L**2)-3*v3*(111-165*L+76*L**2)-4*v2*(1-L)*(85-60*L-3*v3*(48-59*L)))
    b2=(-1221+112*v2**2*(1-L)**2+5729*L-5870*L**2+54*v3**2*(5-16*L+11*L**2)+3*v3*(159-821*L+608*L**2)+4*v2*(1-L)*(121-536*L+3*v3*(32-59*L)))
    b0=(1587+48*v2**2*(1-L)**2-6851*L+6426*L**2-4*v2*(1-L)*(253-(708+51*v3)*L)-54*v3**2*(1-6*L+5*L**2)-3*v3*(335-1253*L+884*L**2))
    den=128*mp.sqrt(2*(1-L)*(1-3*L)**3)*(1-x*x)**2
    return (x**6*b6-x**4*b4+x*x*b2+b0)/den

def f_limit(v2,v3,x):
    a6=80*v2**2+230+54*v3**2+24*v3-320*v2+204*v2*v3
    a4=240*v2**2+402+378*v3**2-228*v3-240*v2+708*v2*v3
    a2=112*v2**2-5870+594*v3**2+1824*v3+2144*v2+708*v2*v3
    a0=48*v2**2+6426-2832*v2-204*v2*v3-270*v3**2-2652*v3
    return (x**6*a6-x**4*a4+x*x*a2+a0)/(384*mp.sqrt(6)*(1-x*x)**2)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--case',choices=sorted(COUPLINGS),required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
    v2,v3=COUPLINGS[a.case]; xs=[mp.mpf('-0.75'),mp.mpf('-0.25'),mp.mpf('0.25'),mp.mpf('0.75')]; lambdas=[mp.mpf('10'),mp.mpf('100'),mp.mpf('1e3'),mp.mpf('1e4'),mp.mpf('1e5'),mp.mpf('1e6')]
    rows=[]; worst=mp.mpf('0')
    for x in xs:
      lim=f_limit(v2,v3,x); seq=[]
      for L in lambdas:
        val=f_d9(L,v2,v3,x); assert mp.isfinite(val); seq.append({'lambda':float(L),'amplitude':float(val)})
      err=abs(f_d9(lambdas[-1],v2,v3,x)-lim)/(1+abs(lim)); worst=max(worst,err); assert err < mp.mpf('2e-6'),(a.case,x,err,lim)
      rows.append({'x':float(x),'analytic_lambda_infinity_limit':float(lim),'scaled_error_at_1e6':float(err),'sequence':seq})
    out={'iteration':350,'case':a.case,'v2':float(v2),'v3':float(v3),'u_s':1.0,'x_values':[float(x) for x in xs],'worst_scaled_error_at_lambda_1e6':float(worst),'classification':'PASS_SCOPED_PROJECTABLE_HORAVA_PUBLISHED_HEADON_ONE_SCALAR_AMPLITUDE_D9_CONVERGES_TO_FINITE_ANALYTIC_LAMBDA_INFINITY_LIMIT','source_equation':'arXiv:2306.00102 Eq.(D.9), u_s=1','scope_guard':['TREE_LEVEL_HEADON_AMPLITUDE_ONLY','FIXED_MARGINAL_COUPLINGS','AWAY_FROM_COLLINEAR_X_PM1','NOT_AN_IR_OBSERVABLE','NO_PARENT_FAMILY_TERMINALIZATION','NO_D7_PROMOTION'],'rows':rows}
    Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps({k:v for k,v in out.items() if k!='rows'},sort_keys=True))
if __name__=='__main__': main()

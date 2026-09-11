#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path
import mpmath as mp

# Source: Barvinsky, Kurov, Sibiryakov, arXiv:2411.13574v1,
# Eqs. (11b),(12).  Around flat space in projectable Hořava gravity,
# omega_s^2 = A[-eta k^2 + B k^4] + C k^6,
# A=(1-lambda)/(1-3lambda), B=(8 mu1+3 mu2), C=u_s^2 nu5.
mp.mp.dps = 80

def main() -> None:
    ap=argparse.ArgumentParser()
    ap.add_argument('--epsilon', required=True, help='lambda-1 > 0')
    ap.add_argument('--output', required=True)
    a=ap.parse_args()
    eps=mp.mpf(a.epsilon); lam=1+eps
    A=(1-lam)/(1-3*lam)
    assert A>0
    etas=[mp.mpf('0.1'),mp.mpf('1'),mp.mpf('10')]
    Bs=[mp.mpf('-1e6'),mp.mpf('-100'),mp.mpf('-1'),mp.mpf('0'),mp.mpf('1'),mp.mpf('100'),mp.mpf('1e6')]
    Cs=[mp.mpf('1e-6'),mp.mpf('1e-3'),mp.mpf('1'),mp.mpf('1e3'),mp.mpf('1e6')]
    rows=[]; kmin=mp.inf; kmax=mp.mpf('0')
    for eta in etas:
      low_coeff=-A*eta
      assert low_coeff<0
      for B in Bs:
        for C in Cs:
          disc=(A*B)**2+4*C*A*eta
          xroot=(-A*B+mp.sqrt(disc))/(2*C)
          assert xroot>0
          kc=mp.sqrt(xroot); klo=kc/2; khi=kc*2
          def w2(k): return A*(-eta*k*k+B*k**4)+C*k**6
          wl=w2(klo); wh=w2(khi)
          assert wl<0,(eps,eta,B,C,kc,wl)
          assert wh>0,(eps,eta,B,C,kc,wh)
          kmin=min(kmin,kc); kmax=max(kmax,kc)
          rows.append({'eta':float(eta),'B_8mu1_plus_3mu2':float(B),'C_us2_nu5':float(C),'k_crossover':float(kc),'omega2_below':float(wl),'omega2_above':float(wh)})
    out={
      'iteration':349,'lambda':float(lam),'epsilon_lambda_minus_1':float(eps),'A':float(A),
      'case_count':len(rows),'minimum_crossover_k':float(kmin),'maximum_crossover_k':float(kmax),
      'analytic_low_k_coefficient_sign':'STRICTLY_NEGATIVE_FOR_ALL_ETA_GT_0',
      'classification':'PASS_SCOPED_PROJECTABLE_HORAVA_IR_SCALAR_DISPERSION_HAS_UNAVOIDABLE_NEGATIVE_LOW_K_WINDOW_FOR_LAMBDA_GT_1_ETA_GT_0_AND_FINITE_HIGHER_DERIVATIVE_COEFFICIENTS',
      'source_equations':['arXiv:2411.13574v1 Eq.(11b)','arXiv:2411.13574v1 Eq.(12)'],
      'scope_guard':['DIMENSIONLESS_REDUCED_COEFFICIENT_STRESS_NOT_A_PHYSICAL_PRIOR','FINITE_B_AND_POSITIVE_C_ONLY','PROJECTABLE_FLAT_BACKGROUND_LINEAR_SCALAR_MODE','NO_CLAIM_ABOUT_TIME_DEPENDENT_STABILIZATION','NO_PARENT_FAMILY_TERMINALIZATION','NO_D7_PROMOTION'],
      'rows':rows
    }
    Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='rows'},sort_keys=True))
if __name__=='__main__': main()

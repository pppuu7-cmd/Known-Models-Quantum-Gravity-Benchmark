#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, math
from pathlib import Path

# Source: D. Anselmi, arXiv:2010.04739v2, eqs. (4.27), (5.52), (6.3).
# xi = m_phi^2/m_chi^2, zeta=(1+xi/2)^-1, gamma_M=gamma_E+ln2.
# Eq. (6.3):
# r+8 n_T = -192 zeta alpha^3
#   + 8(202 zeta +65 xi zeta -144 gamma_M -8 pi^2 +3 xi F_s) zeta alpha^4
#   + O(alpha^5).
GAMMA_M = 0.577215664901532860606512090082402431 + math.log(2.0)

# Explicit source uncertainty bands quoted after eq. (6.3).
def fs_source_band(xi: float) -> tuple[float,float,str]:
    if not (0.0 <= xi <= 16.0):
        raise ValueError("source consistency range is 0<=xi<=16")
    if xi > 4.0:
        return 0.0, 2.0, "Fs=1+-1 for 4<xi<16"
    if xi > 2.0:
        c=1.0+xi/4.0; e=xi/8.0
        return c-e,c+e,"Fs=1+xi/4 +- xi/8 for 2<xi<4"
    if xi > 1.0:
        c=1.0+xi/4.0+xi**2/8.0; e=xi**2/16.0
        return c-e,c+e,"Fs=1+xi/4+xi^2/8 +- xi^2/16 for 1<xi<2"
    if xi > 4.0/7.0:
        c=1.0+xi/4.0+xi**2/8.0+xi**3/8.0; e=xi**3/16.0
        return c-e,c+e,"published asymptotic truncation for 4/7<xi<1"
    if xi > 7.0/19.0:
        c=1.0+xi/4.0+xi**2/8.0+xi**3/8.0+7.0*xi**4/32.0
        e=7.0*xi**4/64.0
        return c-e,c+e,"published asymptotic truncation for 7/19<xi<4/7"
    # The paper says 'and so on' and gives coefficients through xi^8.  For the
    # lower-xi stress region we deliberately use a MUCH WIDER envelope than the
    # displayed asymptotic series requires.  This is KMQGB stress data, not a
    # source claim about a formal Fs error bar.
    return 0.0, 2.5, "KMQGB conservative stress envelope for 0<=xi<=7/19"

def zeta(xi: float) -> float:
    return 1.0/(1.0+xi/2.0)

def bracket(xi: float, fs: float) -> float:
    z=zeta(xi)
    return 202.0*z+65.0*xi*z-144.0*GAMMA_M-8.0*math.pi**2+3.0*xi*fs

def nnll(xi: float, alpha: float, fs: float) -> tuple[float,float,float]:
    z=zeta(xi)
    leading=-192.0*z*alpha**3
    correction=8.0*bracket(xi,fs)*z*alpha**4
    return leading,correction,leading+correction

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--xi',type=float,required=True)
    ap.add_argument('--alpha',type=float,required=True)
    ap.add_argument('--output',required=True)
    a=ap.parse_args()
    if not (0.0 <= a.xi <= 16.0): raise ValueError('xi outside source consistency range')
    if not (0.0 < a.alpha < 0.1): raise ValueError('alpha stress domain')
    lo,hi,band=fs_source_band(a.xi)
    vals=[]
    for fs in (lo,hi):
        lead,corr,total=nnll(a.xi,a.alpha,fs)
        vals.append({'Fs':fs,'leading_alpha3':lead,'nnll_alpha4_correction':corr,'through_alpha4':total,'bracket':bracket(a.xi,fs),'relative_abs_correction_to_alpha3':abs(corr/lead)})
    assert all(v['leading_alpha3'] < 0.0 for v in vals)
    assert all(v['bracket'] < 0.0 for v in vals)
    assert all(v['nnll_alpha4_correction'] < 0.0 for v in vals)
    assert all(v['through_alpha4'] < 0.0 for v in vals)
    out={
      'iteration':344,
      'source':'Anselmi arXiv:2010.04739v2 eqs. (4.27),(5.52),(6.3)',
      'xi':a.xi,'alpha':a.alpha,'zeta':zeta(a.xi),'gamma_M':GAMMA_M,
      'Fs_band':[lo,hi],'Fs_band_basis':band,'endpoint_results':vals,
      'classification':'PASS_SCOPED_FAKEON_NNLL_BREAKS_LEADING_CONSISTENCY_DEGENERACY_WITH_SIGN_STABLE_NONZERO_R_PLUS_8NT_THROUGH_ALPHA4',
      'scope_guard':['SOURCE_DEFINED_NNLL_FORMULA','INTERVAL_STRESS_ON_FS','NOT_A_CAUSAL_RESPONSE_CERTIFICATE','NOT_ALL_HIGHER_DERIVATIVE_BRANCHES','NO_PARENT_FAMILY_TERMINALIZATION','NO_D7_PROMOTION']
    }
    Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,sort_keys=True))
if __name__=='__main__': main()

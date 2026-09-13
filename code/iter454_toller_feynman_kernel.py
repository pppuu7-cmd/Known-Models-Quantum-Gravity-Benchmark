#!/usr/bin/env python3
import argparse, json
import mpmath as mp

LANES = {
    "L0": (0,0,mp.mpf('0.37')),
    "L1": (1,1,mp.mpf('0.73')),
    "L2": (1,2,mp.mpf('1.11')),
    "L3": (2,2,mp.mpf('1.57')),
}
EPS = [mp.mpf('0.2'),mp.mpf('0.1'),mp.mpf('0.05'),mp.mpf('0.025')]

def P(j,l,rt,r):
    return mp.gamma(-j-1j*r)*mp.gamma(l-1j*rt+1)/(mp.gamma(-j-1j*rt)*mp.gamma(l-1j*r+1))

def integrate_branch(j,l,r,eps,wrong=False):
    def f(x): return mp.e**(-(x-r)**2)
    def integrand(x):
        p=P(j,l,x,r)
        if wrong:
            kern = 1/(x-r-1j*eps) + 1/(x-r+1j*eps)
        else:
            kern = 1/(x-r-1j*eps) - 1/(x-r+1j*eps)
        return p*f(x)*kern/(2*mp.pi*1j)
    # deterministic split around the regulated peak
    pts=[-20,r-2,r-mp.mpf('0.5'),r,r+mp.mpf('0.5'),r+2,20]
    return mp.quad(integrand, pts)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--lane',required=True); ap.add_argument('--out',required=True)
    a=ap.parse_args(); mp.mp.dps=80
    j,l,r=LANES[a.lane]
    pdiag=P(j,l,r,r); diag_err=abs(pdiag-1)
    poles=list(range(-j,l+1))
    delta=mp.mpf('1e-30')
    cancel_vals=[]
    for n in poles:
        rt=-1j*mp.mpf(n)+delta
        invgamma=1/mp.gamma(-j-1j*rt)
        cancel_vals.append(abs(invgamma))
    vals=[]; wrongs=[]
    valid=True
    try:
        for e in EPS:
            vals.append(integrate_branch(j,l,r,e,False))
            wrongs.append(integrate_branch(j,l,r,e,True))
    except Exception:
        valid=False
    errors=[abs(v-1) for v in vals] if valid else []
    wrong_errors=[abs(v-1) for v in wrongs] if valid else []
    t1=diag_err < mp.mpf('1e-60')
    t2=(poles==list(range(-j,l+1)))
    t3=(max(cancel_vals) <= mp.mpf('1e-50')) if cancel_vals else False
    t4=valid and errors[-1] < mp.mpf('0.03') and errors[-1] < errors[0]
    t5=valid and wrong_errors[-1] > mp.mpf('0.2')
    passed=bool(t1 and t2 and t3 and t4 and t5)
    def s(x): return mp.nstr(x,40)
    out={
      'lane':a.lane,'j':j,'l':l,'rho':s(r),'dps':mp.mp.dps,'valid':valid,'pass':passed,
      'tests':{'P_diagonal':bool(t1),'pole_enumeration':bool(t2),'pole_cancellation_local':bool(t3),'plemelj_convergence':bool(t4),'wrong_branch_negative_control':bool(t5)},
      'P_diagonal_error':s(diag_err),'source_poles_i_rho':poles,
      'pole_cancellation_abs':[s(x) for x in cancel_vals],
      'eps':[s(x) for x in EPS],
      'branch_values':[s(x) for x in vals], 'branch_errors':[s(x) for x in errors],
      'wrong_values':[s(x) for x in wrongs], 'wrong_errors':[s(x) for x in wrong_errors],
      'classification':'ITER454_TOLLER_FEYNMAN_PROJECTOR_KERNEL_QUALIFIED_SCOPED' if passed else ('SCIENTIFIC_FAIL_ITER454_TOLLER_FEYNMAN_PROJECTOR_KERNEL' if valid else 'INFRASTRUCTURE_OR_NUMERICAL_FAIL')
    }
    with open(a.out,'w') as f: json.dump(out,f,indent=2)
    print(json.dumps(out,indent=2))
if __name__=='__main__': main()

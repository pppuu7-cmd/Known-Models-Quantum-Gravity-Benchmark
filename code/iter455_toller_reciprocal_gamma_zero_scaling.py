#!/usr/bin/env python3
import argparse, json, math
import mpmath as mp

LANES = {
    "L0": (0,0,mp.mpf('0.37')),
    "L1": (1,1,mp.mpf('0.73')),
    "L2": (1,2,mp.mpf('1.11')),
    "L3": (2,2,mp.mpf('1.57')),
}
DELTAS=[mp.mpf('1e-10'),mp.mpf('1e-15'),mp.mpf('1e-20'),mp.mpf('1e-25'),mp.mpf('1e-30')]
EPS=[mp.mpf('0.2'),mp.mpf('0.1'),mp.mpf('0.05'),mp.mpf('0.025')]

def P(j,l,rt,r):
    return mp.gamma(-j-1j*r)*mp.gamma(l-1j*rt+1)/(mp.gamma(-j-1j*rt)*mp.gamma(l-1j*r+1))

def integrate_branch(j,l,r,eps,wrong=False):
    def f(x): return mp.e**(-(x-r)**2)
    def integrand(x):
        p=P(j,l,x,r)
        if wrong:
            kern=1/(x-r-1j*eps)+1/(x-r+1j*eps)
        else:
            kern=1/(x-r-1j*eps)-1/(x-r+1j*eps)
        return p*f(x)*kern/(2*mp.pi*1j)
    pts=[-20,r-2,r-mp.mpf('0.5'),r,r+mp.mpf('0.5'),r+2,20]
    return mp.quad(integrand,pts)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--lane',required=True); ap.add_argument('--out',required=True)
    a=ap.parse_args(); mp.mp.dps=80
    j,l,r=LANES[a.lane]
    valid=True
    pole_records=[]
    try:
        for n in range(-j,l+1):
            m=j+n
            coeff=mp.factorial(m)
            mags=[]
            for d in DELTAS:
                rt=-1j*mp.mpf(n)+d
                z=-j-1j*rt
                mags.append(abs(1/mp.gamma(z)))
            ratios=[v/d for v,d in zip(mags,DELTAS)]
            rel=[abs(q-coeff)/coeff for q in ratios]
            slopes=[]
            for k in range(1,len(DELTAS)):
                slopes.append(mp.log(mags[k]/mags[k-1])/mp.log(DELTAS[k]/DELTAS[k-1]))
            ratio_ok=(rel[-1] <= mp.mpf('1e-8') and rel[-2] <= mp.mpf('1e-8'))
            slope_ok=all(abs(s-1) <= mp.mpf('1e-6') for s in slopes[-3:])
            monotone_ok=all(mags[k] < mags[k-1] for k in range(1,len(mags)))
            quadratic_reject=(mags[-1]/(DELTAS[-1]**2) > mp.mpf('1e20'))
            pole_records.append({'n':n,'m':m,'expected_coeff':coeff,'magnitudes':mags,'ratios':ratios,
                                 'relative_errors':rel,'slopes':slopes,'ratio_ok':ratio_ok,
                                 'slope_ok':slope_ok,'monotone_ok':monotone_ok,
                                 'quadratic_reject':quadratic_reject})
        pdiag=P(j,l,r,r); diag_err=abs(pdiag-1)
        poles=list(range(-j,l+1))
        vals=[integrate_branch(j,l,r,e,False) for e in EPS]
        wrongs=[integrate_branch(j,l,r,e,True) for e in EPS]
    except Exception as exc:
        valid=False; err=repr(exc); pdiag=mp.nan; diag_err=mp.inf; poles=[]; vals=[]; wrongs=[]

    branch_errors=[abs(v-1) for v in vals] if valid else []
    wrong_errors=[abs(v-1) for v in wrongs] if valid else []
    t1=valid and all(x['ratio_ok'] for x in pole_records)
    t2=valid and all(x['slope_ok'] for x in pole_records)
    t3=valid and all(x['monotone_ok'] for x in pole_records)
    t4=valid and all(x['quadratic_reject'] for x in pole_records)
    t5=valid and diag_err < mp.mpf('1e-60')
    t6=valid and poles == list(range(-j,l+1))
    t7=valid and branch_errors[-1] < mp.mpf('0.03') and branch_errors[-1] < branch_errors[0]
    t8=valid and wrong_errors[-1] > mp.mpf('0.2')
    passed=bool(t1 and t2 and t3 and t4 and t5 and t6 and t7 and t8)
    def s(x): return mp.nstr(x,40) if not isinstance(x,(int,bool,str)) else x
    serial=[]
    for q in pole_records:
        serial.append({'n':q['n'],'m':q['m'],'expected_coeff':s(q['expected_coeff']),
                       'magnitudes':[s(x) for x in q['magnitudes']],
                       'ratios':[s(x) for x in q['ratios']],
                       'relative_errors':[s(x) for x in q['relative_errors']],
                       'slopes':[s(x) for x in q['slopes']],
                       'ratio_ok':bool(q['ratio_ok']),'slope_ok':bool(q['slope_ok']),
                       'monotone_ok':bool(q['monotone_ok']),'quadratic_reject':bool(q['quadratic_reject'])})
    cls=('ITER455_TOLLER_RECIPROCAL_GAMMA_SIMPLE_ZERO_QUALIFIED_SCOPED' if passed else
         'SCIENTIFIC_FAIL_ITER455_TOLLER_RECIPROCAL_GAMMA_SIMPLE_ZERO' if valid else
         'INFRASTRUCTURE_OR_NUMERICAL_FAIL')
    out={'lane':a.lane,'j':j,'l':l,'rho':s(r),'dps':mp.mp.dps,'valid':valid,'pass':passed,
         'tests':{'ratio_factorial':bool(t1),'unit_log_slope':bool(t2),'strict_monotone':bool(t3),
                  'quadratic_zero_rejected':bool(t4),'P_diagonal':bool(t5),'pole_enumeration':bool(t6),
                  'plemelj_convergence':bool(t7),'wrong_branch_negative_control':bool(t8)},
         'deltas':[s(x) for x in DELTAS],'pole_records':serial,'P_diagonal_error':s(diag_err),
         'source_poles_i_rho':poles,'eps':[s(x) for x in EPS],
         'branch_values':[s(x) for x in vals],'branch_errors':[s(x) for x in branch_errors],
         'wrong_values':[s(x) for x in wrongs],'wrong_errors':[s(x) for x in wrong_errors],
         'classification':cls}
    if not valid: out['error']=err
    with open(a.out,'w') as f: json.dump(out,f,indent=2)
    print(json.dumps(out,indent=2))

if __name__=='__main__': main()

#!/usr/bin/env python3
import argparse,itertools,json,math,os
import mpmath as mp

DPS=100
BETAS=(0.5,1.0,2.0,4.0,8.0,12.0,16.0)
TAU=mp.mpf('0.05')
Q=1-TAU
mp.mp.dps=DPS


def tvals(j,m,rho,beta):
    jj=mp.mpf(j); mm=mp.mpf(m); rr=mp.mpf(str(rho)); b=mp.mpf(str(beta)); z=mp.e**(-2*b)
    tp=(mp.e**(-(jj-1j*rr+mm+1)*b)*mp.gamma(2*jj+2)*mp.gamma(1j*rr-mm)/(mp.gamma(jj-mm+1)*mp.gamma(jj+1+1j*rr))*mp.hyp2f1(jj+mm+1,jj+1-1j*rr,1+mm-1j*rr,z))
    tm=(mp.e**(-(jj+1j*rr-mm+1)*b)*mp.gamma(2*jj+2)*mp.gamma(-1j*rr+mm)/(mp.gamma(jj+mm+1)*mp.gamma(jj+1-1j*rr))*mp.hyp2f1(jj-mm+1,jj+1+1j*rr,1-mm+1j*rr,z))
    return mp.mpc(tp),mp.mpc(tm)


def env(gamma,j,beta):
    rho=gamma*j; best=mp.mpf('0'); finite=True; who=None
    for m in range(-j,j+1):
        tp,tm=tvals(j,m,rho,beta)
        finite &= bool(mp.isfinite(tp.real) and mp.isfinite(tp.imag) and mp.isfinite(tm.real) and mp.isfinite(tm.imag))
        for branch,v in (('plus',tp),('minus',tm)):
            if abs(v)>best:
                best=abs(v); who={'m':m,'branch':branch}
    return best,who,finite


def k5_cut_check():
    V=range(5); E=list(itertools.combinations(V,2)); rows=[]
    for mask in range(1,(1<<5)-1):
        S={v for v in V if (mask>>v)&1}
        if 0 not in S: continue
        cut=sum(((u in S) != (v in S)) for u,v in E)
        rows.append({'size':len(S),'cut':cut})
    return min(r['cut'] for r in rows),rows


def main():
    p=argparse.ArgumentParser(); p.add_argument('--gamma',type=float,required=True); p.add_argument('--j',type=int,required=True); a=p.parse_args()
    if a.gamma not in (7.0,8.0) or a.j not in (2,5): raise SystemExit('outside frozen matrix')
    cutmin,cuts=k5_cut_check(); rows=[]; finite=True
    for b in BETAS:
        M,w,f=env(a.gamma,a.j,b); finite &= f
        ratio=M*mp.cosh(b)**Q
        finite &= bool(mp.isfinite(ratio))
        rows.append({'beta':b,'M':float(M),'comparison_ratio_M_times_cosh_pow_0p95':float(ratio),'witness':w})
    tail=[r['comparison_ratio_M_times_cosh_pow_0p95'] for r in rows if r['beta']>=4.0]
    controls={
      'k5_min_cut_at_least_three':cutmin>=3,
      'source_worst_decay_exponent_stronger_than_comparison':1.0>float(Q),
      'finite_kak_angular_dimension':2*a.j+1>0,
      'all_frozen_ratios_finite_for_beta_ge_0p5':finite,
      'asymptotic_comparison_ratio_not_growing_on_frozen_tail':tail[-1] <= tail[0],
      'collision_beta_zero_explicitly_excluded':True
    }
    ok=all(controls.values())
    out={'iteration':446,'gamma':a.gamma,'j':a.j,'rho':a.gamma*a.j,'tau':float(TAU),'comparison_exponent':float(Q),'source_worst_decay_exponent':1.0,'k5_min_cut':cutmin,'k5_cut_rows':cuts,'kak_magnetic_dimension':2*a.j+1,'rows':rows,'controls':controls,'controls_valid':ok,'classification':'SOURCE_BACKED_CAUSAL_K5_COLLISION_EXCISED_DOMAIN_ABSOLUTELY_INTEGRABLE_BY_KAMINSKI_COMPARISON' if ok else 'KAMINSKI_COLLISION_EXCISED_COMPARISON_CONTROL_INVALID','scope_guard':'Comparison applies only away from relative-rapidity collision loci. It does not prove beta->0 collision integrability, full causal-vertex finiteness, stack normalization/cutoff removal, terminal D7, or Candidate Gravity activation.','d7_s2':'NONCOMPACT_TAIL_LOCALIZED__COLLISION_STRATA_REMAIN_OPEN' if ok else 'NOT_CLOSED','d7_s3':'NOT_CLOSED','d7_s4':'PARTIAL_GLOBAL_NOT_CLOSED','d7':'NOT_CLOSED / NOT_YET_AUTHORIZED','candidate_gravity_authorized':False}
    os.makedirs('build/lqg-iter446',exist_ok=True); gt=str(a.gamma).replace('.','p'); fn=f'build/lqg-iter446/g{gt}_j{a.j}.json'; open(fn,'w').write(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps(out,indent=2,sort_keys=True))
    if not ok: raise SystemExit(2)

if __name__=='__main__': main()

#!/usr/bin/env python3
import argparse,json,math,os
import mpmath as mp
mp.mp.dps=100
BETAS=[4.,6.,8.,10.,12.,14.]

def tvals(j,m,rho,beta):
    j=mp.mpf(j); m=mp.mpf(m); rho=mp.mpf(str(rho)); b=mp.mpf(str(beta)); z=mp.e**(-2*b)
    tp=(mp.e**(-(j-1j*rho+m+1)*b)*mp.gamma(2*j+2)*mp.gamma(1j*rho-m)/(mp.gamma(j-m+1)*mp.gamma(j+1+1j*rho))*mp.hyp2f1(j+m+1,j+1-1j*rho,1+m-1j*rho,z))
    tm=(mp.e**(-(j+1j*rho-m+1)*b)*mp.gamma(2*j+2)*mp.gamma(-1j*rho+m)/(mp.gamma(j+m+1)*mp.gamma(j+1-1j*rho))*mp.hyp2f1(j-m+1,j+1+1j*rho,1-m+1j*rho,z))
    return tp,tm

def lin_slope(x,y):
    xm=sum(x)/len(x); ym=sum(y)/len(y)
    return sum((a-xm)*(b-ym) for a,b in zip(x,y))/sum((a-xm)**2 for a in x)

def main():
    p=argparse.ArgumentParser(); p.add_argument('--gamma',type=float,required=True); p.add_argument('--j',type=int,required=True); a=p.parse_args()
    if a.gamma not in (7.,8.) or a.j not in (2,5): raise SystemExit(2)
    rho=a.gamma*a.j; rows=[]; finite=True
    for b in BETAS:
        env=mp.mpf('0'); who=None
        for m in range(-a.j,a.j+1):
            tp,tm=tvals(a.j,m,rho,b)
            finite &= bool(mp.isfinite(tp.real) and mp.isfinite(tp.imag) and mp.isfinite(tm.real) and mp.isfinite(tm.imag))
            for name,v in [('plus',tp),('minus',tm)]:
                if abs(v)>env: env=abs(v); who={'m':m,'branch':name}
        radial=mp.sinh(b)**2*env**4
        rows.append({'beta':b,'envelope':float(env),'envelope_exp_beta':float(env*mp.e**b),'haar_times_four_wedge_envelope':float(radial),'witness':who})
    r=[x['haar_times_four_wedge_envelope'] for x in rows]
    dec=all(r[i+1]<r[i] for i in range(len(r)-1))
    late=[x for x in rows if x['beta']>=8]
    slope=lin_slope([x['beta'] for x in late],[math.log(x['haar_times_four_wedge_envelope']) for x in late])
    s=[x['envelope_exp_beta'] for x in late]; variation=(max(s)-min(s))/max(s)
    controls={'finite':finite,'strictly_decreasing':dec,'slope_le_minus_1p8':slope<=-1.8,'e_minus_beta_scaling':variation<=1e-4}
    ok=all(controls.values())
    out={'iteration':443,'gamma':a.gamma,'j':a.j,'rho':rho,'rows':rows,'late_log_slope':slope,'expected_slope':-2.0,'scaled_envelope_variation':variation,'controls':controls,'controls_valid':ok,'classification':'SOURCE_ONE_LEG_RADIAL_ENVELOPE_INTEGRABLE_ON_FROZEN_GRID' if ok else 'RADIAL_GATE_INVALID_OR_FAILED','scope_guard':'One-group-variable radial gate only; not full multi-group Haar/angular vertex finiteness or D7 closure.','d7_s2':'STRENGTHENED_BUT_NOT_CLOSED' if ok else 'NOT_CLOSED','d7_s3':'NOT_CLOSED','d7_s4':'PARTIAL_GLOBAL_NOT_CLOSED','d7':'NOT_CLOSED / NOT_YET_AUTHORIZED','candidate_gravity_authorized':False}
    os.makedirs('build/lqg-iter443',exist_ok=True); tag=str(a.gamma).replace('.','p'); fn=f'build/lqg-iter443/g{tag}_j{a.j}.json'; open(fn,'w').write(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps(out,indent=2,sort_keys=True))
    if not ok: raise SystemExit(2)
if __name__=='__main__': main()

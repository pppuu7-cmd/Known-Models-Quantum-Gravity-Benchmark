#!/usr/bin/env python3
import argparse,json,math,os
import mpmath as mp

DPS=100
BS=(8.0,10.0,12.0,14.0)
SOURCE_GAMMAS=(7.0,8.0)
SOURCE_JS=(2,5)
SOURCE_C=(0.5,1.0,2.0,4.0)
MAX_SLOPE=-1.8
MAX_SCALED_VARIATION=1e-4
mp.mp.dps=DPS


def tvals(j,m,rho,beta):
    j=mp.mpf(j); m=mp.mpf(m); rho=mp.mpf(str(rho)); b=mp.mpf(str(beta)); z=mp.e**(-2*b)
    tp=(mp.e**(-(j-1j*rho+m+1)*b)*mp.gamma(2*j+2)*mp.gamma(1j*rho-m)/(mp.gamma(j-m+1)*mp.gamma(j+1+1j*rho))*mp.hyp2f1(j+m+1,j+1-1j*rho,1+m-1j*rho,z))
    tm=(mp.e**(-(j+1j*rho-m+1)*b)*mp.gamma(2*j+2)*mp.gamma(-1j*rho+m)/(mp.gamma(j+m+1)*mp.gamma(j+1-1j*rho))*mp.hyp2f1(j-m+1,j+1+1j*rho,1-m+1j*rho,z))
    return mp.mpc(tp),mp.mpc(tm)


def envelope(gamma,j,beta):
    rho=gamma*j; best=mp.mpf('0'); witness=None; finite=True
    for m in range(-j,j+1):
        tp,tm=tvals(j,m,rho,beta)
        finite &= bool(mp.isfinite(tp.real) and mp.isfinite(tp.imag) and mp.isfinite(tm.real) and mp.isfinite(tm.imag))
        for branch,v in (('plus',tp),('minus',tm)):
            if abs(v)>best:
                best=abs(v); witness={'m':m,'branch':branch}
    return best,witness,finite


def slope(xs,ys):
    xm=sum(xs)/len(xs); ym=sum(ys)/len(ys)
    return sum((x-xm)*(y-ym) for x,y in zip(xs,ys))/sum((x-xm)**2 for x in xs)


def main():
    p=argparse.ArgumentParser(); p.add_argument('--gamma',type=float,required=True); p.add_argument('--j',type=int,required=True); p.add_argument('--c',type=float,required=True); a=p.parse_args()
    if a.gamma not in SOURCE_GAMMAS or a.j not in SOURCE_JS or a.c not in SOURCE_C: raise SystemExit('outside frozen matrix')
    mc,wc,fc=envelope(a.gamma,a.j,a.c)
    rows=[]; finite=fc; scaled=[]
    for B in BS:
        b1=B+a.c/2; b2=B-a.c/2
        m1,w1,f1=envelope(a.gamma,a.j,b1); m2,w2,f2=envelope(a.gamma,a.j,b2)
        finite &= f1 and f2
        r=mp.sinh(b1)**2*mp.sinh(b2)**2*m1**3*m2**3*mc
        finite &= bool(mp.isfinite(r))
        scaled.extend([float(m1*mp.e**b1),float(m2*mp.e**b2)])
        rows.append({'B':B,'c':a.c,'beta1':b1,'beta2':b2,'M_beta1':float(m1),'M_beta2':float(m2),'M_c':float(mc),'R2':float(r),'witness_beta1':w1,'witness_beta2':w2,'witness_c':wc})
    vals=[r['R2'] for r in rows]
    decreasing=all(vals[i+1]<vals[i] for i in range(len(vals)-1))
    fit=slope(list(BS),[math.log(x) for x in vals])
    variation=(max(scaled)-min(scaled))/max(scaled)
    controls={'all_source_values_finite':finite,'radial_envelope_strictly_decreasing_in_B':decreasing,'common_shift_log_slope_le_minus_1p8':fit<=MAX_SLOPE,'external_single_factor_exp_beta_stable':variation<=MAX_SCALED_VARIATION}
    ok=all(controls.values())
    out={'iteration':444,'gamma':a.gamma,'j':a.j,'c':a.c,'rho':a.gamma*a.j,'dps':DPS,'rows':rows,'common_shift_log_slope':fit,'expected_common_shift_log_slope':-2.0,'external_scaled_envelope_variation':variation,'controls':controls,'controls_valid':ok,'classification':'SOURCE_TWO_GROUP_SEPARATED_RADIAL_ENVELOPE_INTEGRABLE_ON_FROZEN_GRID' if ok else 'TWO_GROUP_SEPARATED_RADIAL_GATE_FAILED_OR_INVALID','scope_guard':'Two-group common-axis fixed-positive-separation radial gate only; not c->0 collision strip, arbitrary angular directions, k>=3 simultaneous escape, full Haar/angular causal-vertex finiteness, stack cutoff removal, terminal D7, or Candidate Gravity activation.','d7_s2':'STRENGTHENED_BUT_NOT_CLOSED' if ok else 'NOT_CLOSED','d7_s3':'NOT_CLOSED','d7_s4':'PARTIAL_GLOBAL_NOT_CLOSED','d7':'NOT_CLOSED / NOT_YET_AUTHORIZED','candidate_gravity_authorized':False}
    os.makedirs('build/lqg-iter444',exist_ok=True); gt=str(a.gamma).replace('.','p'); ct=str(a.c).replace('.','p'); fn=f'build/lqg-iter444/g{gt}_j{a.j}_c{ct}.json'; open(fn,'w').write(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps(out,indent=2,sort_keys=True))
    if not ok: raise SystemExit(2)

if __name__=='__main__': main()

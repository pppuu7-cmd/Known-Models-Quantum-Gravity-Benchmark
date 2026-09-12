#!/usr/bin/env python3
# Production trigger after frozen preregistration in status/ITERATION_447.md.
import argparse,json,math,os,statistics
import mpmath as mp

mp.mp.dps=100
NS=tuple(range(4,11))
BETAS=tuple(mp.power(2,-n) for n in NS)
SAFETY=mp.mpf('0.10')
SPREAD_MAX=mp.mpf('0.20')


def hyp2f1_euler(a,b,c,z):
    # Exact Euler transformation. Here c-b is a non-positive integer, so the
    # transformed hypergeometric terminates and avoids mpmath's near-z=1
    # analytic-continuation comparison bug without changing the source object.
    return mp.power(1-z,c-a-b)*mp.hyp2f1(c-a,c-b,c,z)


def tvals(j,m,rho,beta):
    jj=mp.mpf(j); mm=mp.mpf(m); rr=mp.mpf(str(rho)); b=mp.mpf(beta); z=mp.e**(-2*b)
    ap=jj+mm+1; bp=jj+1-1j*rr; cp=1+mm-1j*rr
    am=jj-mm+1; bm=jj+1+1j*rr; cm=1-mm+1j*rr
    tp=(mp.e**(-(jj-1j*rr+mm+1)*b)*mp.gamma(2*jj+2)*mp.gamma(1j*rr-mm)/(mp.gamma(jj-mm+1)*mp.gamma(jj+1+1j*rr))*hyp2f1_euler(ap,bp,cp,z))
    tm=(mp.e**(-(jj+1j*rr-mm+1)*b)*mp.gamma(2*jj+2)*mp.gamma(-1j*rr+mm)/(mp.gamma(jj+mm+1)*mp.gamma(jj+1-1j*rr))*hyp2f1_euler(am,bm,cm,z))
    return mp.mpc(tp),mp.mpc(tm)


def finite_complex(z):
    return bool(mp.isfinite(z.real) and mp.isfinite(z.imag))


def main():
    p=argparse.ArgumentParser(); p.add_argument('--gamma',type=float,required=True); p.add_argument('--j',type=int,required=True); a=p.parse_args()
    if a.gamma not in (7.0,8.0) or a.j not in (2,5): raise SystemExit('outside frozen matrix')
    rho=a.gamma*a.j
    records=[]; all_valid=True
    for m in range(-a.j,a.j+1):
        vals={'plus':[],'minus':[]}
        for beta in BETAS:
            tp,tm=tvals(a.j,m,rho,beta)
            all_valid &= finite_complex(tp) and finite_complex(tm)
            vals['plus'].append(abs(tp)); vals['minus'].append(abs(tm))
        for branch in ('plus','minus'):
            xs=vals[branch]; powers=[]
            for i in range(len(BETAS)-1):
                if xs[i] <= 0 or xs[i+1] <= 0:
                    all_valid=False; powers.append(mp.nan); continue
                slope=(mp.log(xs[i+1])-mp.log(xs[i]))/(mp.log(BETAS[i+1])-mp.log(BETAS[i]))
                powers.append(-slope)
            all_valid &= all(bool(mp.isfinite(q)) for q in powers)
            tail=powers[-3:]
            p_local=mp.mpf(str(statistics.median([float(q) for q in tail])))
            spread=max(tail)-min(tail)
            records.append({'m':m,'branch':branch,'abs_values':[float(v) for v in xs],'effective_powers':[float(q) for q in powers],'p_local':float(p_local),'stability_spread':float(spread)})
    worst=max(records,key=lambda r:r['p_local'])
    scientific_pass=bool(all_valid and mp.mpf(str(worst['p_local'])) < 3-SAFETY and mp.mpf(str(worst['stability_spread'])) <= SPREAD_MAX)
    if not all_valid: classification='COLLISION_LOCAL_POWER_NUMERICAL_INVALID'
    elif scientific_pass: classification='SOURCE_TOLLER_PAIR_COLLISION_LOCAL_POWER_INTEGRABLE_ON_FROZEN_GRID'
    else: classification='SOURCE_TOLLER_PAIR_COLLISION_LOCAL_POWER_OBSTRUCTION_ON_FROZEN_GRID'
    out={'iteration':447,'gamma':a.gamma,'j':a.j,'rho':rho,'precision_dps':100,'beta_exponents_n':list(NS),'beta_values':[float(b) for b in BETAS],'radial_measure_power':2.0,'frozen_integrability_threshold_p_less_than':2.9,'frozen_stability_spread_max':0.20,'records':records,'worst_witness':worst,'numerically_valid':all_valid,'scientific_lane_pass':scientific_pass,'classification':classification,'scope_guard':'Isolated source-Toller pair-collision local-power audit only; no simultaneous multi-pair theorem, no full causal-vertex finiteness/divergence theorem, no PV/finite-part/distributional equivalence, no terminal D7, no Candidate Gravity authorization.','d7_s2':'PAIR_COLLISION_LOCAL_POWER_SUPPORTED__MULTI_PAIR_REMAINS_OPEN' if scientific_pass else 'PAIR_COLLISION_LOCAL_POWER_OBSTRUCTION_OR_INVALID__NOT_CLOSED','d7_s3':'NOT_CLOSED','d7_s4':'PARTIAL_GLOBAL_NOT_CLOSED','d7':'NOT_CLOSED / NOT_YET_AUTHORIZED','candidate_gravity_authorized':False}
    os.makedirs('build/lqg-iter447',exist_ok=True); gt=str(a.gamma).replace('.','p'); fn=f'build/lqg-iter447/g{gt}_j{a.j}.json'; open(fn,'w').write(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps(out,indent=2,sort_keys=True))
    if not all_valid: raise SystemExit(3)

if __name__=='__main__': main()

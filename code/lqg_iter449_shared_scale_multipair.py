#!/usr/bin/env python3
# Implementation after prospective freeze in status/ITERATION_449.md.
# Production trigger after workflow installation; frozen science unchanged.
import argparse,json,os,statistics
import mpmath as mp

NS=tuple(range(4,11))
SPREAD_MAX=mp.mpf('0.20')
POWER_MAX=mp.mpf('2.90')
RECHECK_MAX=mp.mpf('0.02')
FACTORIZATION_MAX=mp.mpf('0.02')


def hyp2f1_euler(a,b,c,z):
    return mp.power(1-z,c-a-b)*mp.hyp2f1(c-a,c-b,c,z)


def tvals(j,m,rho,beta):
    jj=mp.mpf(j); mm=mp.mpf(m); rr=mp.mpf(str(rho)); b=mp.mpf(beta); z=mp.e**(-2*b)
    ap=jj+mm+1; bp=jj+1-1j*rr; cp=1+mm-1j*rr
    am=jj-mm+1; bm=jj+1+1j*rr; cm=1-mm+1j*rr
    tp=(mp.e**(-(jj-1j*rr+mm+1)*b)*mp.gamma(2*jj+2)*mp.gamma(1j*rr-mm)/(mp.gamma(jj-mm+1)*mp.gamma(jj+1+1j*rr))*hyp2f1_euler(ap,bp,cp,z))
    tm=(mp.e**(-(jj+1j*rr-mm+1)*b)*mp.gamma(2*jj+2)*mp.gamma(-1j*rr+mm)/(mp.gamma(jj+mm+1)*mp.gamma(jj+1-1j*rr))*hyp2f1_euler(am,bm,cm,z))
    return mp.mpc(tp),mp.mpc(tm)


def finite(z):
    return bool(mp.isfinite(z.real) and mp.isfinite(z.imag))


def effective_powers(values,betas):
    out=[]
    for i in range(len(values)-1):
        if values[i] <= 0 or values[i+1] <= 0:
            out.append(mp.nan); continue
        slope=(mp.log(values[i+1])-mp.log(values[i]))/(mp.log(betas[i+1])-mp.log(betas[i]))
        out.append(-slope)
    return out


def tail_stats(powers):
    tail=powers[-3:]
    if not all(mp.isfinite(x) for x in tail): return mp.nan,mp.inf
    med=mp.mpf(str(statistics.median([float(x) for x in tail])))
    return med,max(tail)-min(tail)


def compute_lane(gamma,j,k,dps):
    with mp.workdps(dps):
        betas=tuple(mp.power(2,-n) for n in NS)
        rho=gamma*j
        rows=[]; valid=True
        for m in range(-j,j+1):
            single=[]; product=[]; envelope=[]
            for beta in betas:
                tp,tm=tvals(j,m,rho,beta)
                valid &= finite(tp) and finite(tm)
                s=tp+tm; e=abs(tp)+abs(tm)
                valid &= finite(s)
                single.append(abs(s)); product.append(abs(s**k)); envelope.append(e**k)
            ps=effective_powers(single,betas)
            pp=effective_powers(product,betas)
            pe=effective_powers(envelope,betas)
            sm,_=tail_stats(ps); pm,spread=tail_stats(pp); em,_=tail_stats(pe)
            factor_delta=abs(pm-k*sm) if mp.isfinite(pm) and mp.isfinite(sm) else mp.inf
            valid &= bool(mp.isfinite(pm) and mp.isfinite(spread) and mp.isfinite(factor_delta) and mp.isfinite(em))
            rows.append({
                'm':m,'single_abs':[float(x) for x in single],'product_abs':[float(x) for x in product],
                'envelope_abs':[float(x) for x in envelope],
                'single_effective_powers':[float(x) if mp.isfinite(x) else None for x in ps],
                'product_effective_powers':[float(x) if mp.isfinite(x) else None for x in pp],
                'envelope_effective_powers':[float(x) if mp.isfinite(x) else None for x in pe],
                'single_p_local':float(sm) if mp.isfinite(sm) else None,
                'product_p_local':float(pm) if mp.isfinite(pm) else None,
                'product_stability_spread':float(spread) if mp.isfinite(spread) else None,
                'factorization_power_delta':float(factor_delta) if mp.isfinite(factor_delta) else None,
                'envelope_p_local':float(em) if mp.isfinite(em) else None,
            })
        return valid,rows


def main():
    p=argparse.ArgumentParser(); p.add_argument('--gamma',type=int,required=True); p.add_argument('--j',type=int,required=True); p.add_argument('--k',type=int,required=True); a=p.parse_args()
    if a.gamma not in (7,8) or a.j not in (2,5) or a.k not in (2,3): raise SystemExit('outside frozen matrix')
    valid,rows=compute_lane(a.gamma,a.j,a.k,100)
    worst=max(rows,key=lambda r: float('inf') if r['product_p_local'] is None else r['product_p_local'])
    _,rows130=compute_lane(a.gamma,a.j,a.k,130)
    w130=next(r for r in rows130 if r['m']==worst['m'])
    recheck=abs(mp.mpf(str(worst['product_p_local']))-mp.mpf(str(w130['product_p_local']))) if worst['product_p_local'] is not None and w130['product_p_local'] is not None else mp.inf
    factor=max((mp.mpf(str(r['factorization_power_delta'])) for r in rows if r['factorization_power_delta'] is not None),default=mp.inf)
    scientific_pass=bool(valid and mp.mpf(str(worst['product_p_local'])) < POWER_MAX and mp.mpf(str(worst['product_stability_spread'])) <= SPREAD_MAX and recheck <= RECHECK_MAX and factor <= FACTORIZATION_MAX)
    if not valid: cls='MULTIPAIR_COHERENT_COLLISION_NUMERICAL_INVALID'
    elif scientific_pass: cls='SOURCE_TOLLER_COHERENT_SHARED_SCALE_MULTI_PAIR_LANE_INTEGRABLE'
    else: cls='SOURCE_TOLLER_COHERENT_SHARED_SCALE_MULTI_PAIR_LANE_OBSTRUCTION'
    out={
      'iteration':449,'gamma':a.gamma,'j':a.j,'multiplicity_k':a.k,'rho':a.gamma*a.j,
      'precision_dps':100,'recheck_dps':130,'beta_exponents_n':list(NS),
      'frozen_power_threshold_less_than':2.90,'frozen_stability_spread_max':0.20,
      'frozen_recheck_delta_max':0.02,'frozen_factorization_power_delta_max':0.02,
      'records':rows,'worst_witness':worst,'worst_witness_recheck_130dps':w130,
      'worst_power_recheck_abs_delta':float(recheck),'worst_factorization_power_delta':float(factor) if mp.isfinite(factor) else None,
      'numerically_valid':valid,'scientific_lane_pass':scientific_pass,'classification':cls,
      'scope_guard':'Shared common-scale no-fit product of coherent Toller branch sums only; not the complete source-defined magnetic/intertwiner invariant contraction, not all collision strata, not a full causal-vertex theorem, no D7 terminal classification and no Candidate Gravity authorization.'
    }
    os.makedirs('build/lqg-iter449',exist_ok=True); fn=f'build/lqg-iter449/g{a.gamma}_j{a.j}_k{a.k}.json'; open(fn,'w').write(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps(out,indent=2,sort_keys=True))
    if not valid: raise SystemExit(3)

if __name__=='__main__': main()

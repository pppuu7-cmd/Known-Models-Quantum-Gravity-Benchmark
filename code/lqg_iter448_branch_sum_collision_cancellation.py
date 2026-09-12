#!/usr/bin/env python3
# Implementation after prospective freeze in status/ITERATION_448.md.
import argparse,json,os,statistics
import mpmath as mp

NS=tuple(range(4,11))
SPREAD_MAX=mp.mpf('0.20')
POWER_MAX=mp.mpf('2.90')
RECHECK_MAX=mp.mpf('0.02')


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


def compute_lane(gamma,j,dps):
    with mp.workdps(dps):
        betas=tuple(mp.power(2,-n) for n in NS)
        rho=gamma*j
        rows=[]; valid=True
        for m in range(-j,j+1):
            plus=[]; minus=[]; coherent=[]; envelope=[]; ratios=[]
            for beta in betas:
                tp,tm=tvals(j,m,rho,beta)
                valid &= finite(tp) and finite(tm)
                ap=abs(tp); am=abs(tm); s=tp+tm; aa=ap+am
                plus.append(ap); minus.append(am); coherent.append(abs(s)); envelope.append(aa)
                ratios.append(abs(s)/aa if aa>0 else mp.nan)
            pp=effective_powers(plus,betas); pm=effective_powers(minus,betas)
            ps=effective_powers(coherent,betas); pa=effective_powers(envelope,betas)
            psm,pspread=tail_stats(ps); pam,_=tail_stats(pa)
            valid &= bool(mp.isfinite(psm) and mp.isfinite(pspread) and mp.isfinite(pam))
            rows.append({
                'm':m,
                'coherent_abs':[float(x) for x in coherent],
                'envelope_abs':[float(x) for x in envelope],
                'cancellation_ratio':[float(x) if mp.isfinite(x) else None for x in ratios],
                'coherent_effective_powers':[float(x) if mp.isfinite(x) else None for x in ps],
                'envelope_effective_powers':[float(x) if mp.isfinite(x) else None for x in pa],
                'plus_effective_powers':[float(x) if mp.isfinite(x) else None for x in pp],
                'minus_effective_powers':[float(x) if mp.isfinite(x) else None for x in pm],
                'coherent_p_local':float(psm) if mp.isfinite(psm) else None,
                'coherent_stability_spread':float(pspread) if mp.isfinite(pspread) else None,
                'envelope_p_local':float(pam) if mp.isfinite(pam) else None,
            })
        return valid,rows


def main():
    p=argparse.ArgumentParser(); p.add_argument('--gamma',type=int,required=True); p.add_argument('--j',type=int,required=True); a=p.parse_args()
    if a.gamma not in (7,8) or a.j not in (2,5): raise SystemExit('outside frozen matrix')
    valid,rows=compute_lane(a.gamma,a.j,100)
    worst=max(rows,key=lambda r: float('inf') if r['coherent_p_local'] is None else r['coherent_p_local'])
    _,rows130=compute_lane(a.gamma,a.j,130)
    match130=next(r for r in rows130 if r['m']==worst['m'])
    recheck=abs(mp.mpf(str(worst['coherent_p_local']))-mp.mpf(str(match130['coherent_p_local']))) if worst['coherent_p_local'] is not None and match130['coherent_p_local'] is not None else mp.inf
    min_ratio=min((x for r in rows for x in r['cancellation_ratio'] if x is not None),default=None)
    isolated=max([x for r in rows for x in (r['plus_effective_powers'][-3:]+r['minus_effective_powers'][-3:]) if x is not None],default=None)
    scientific_pass=bool(valid and mp.mpf(str(worst['coherent_p_local'])) < POWER_MAX and mp.mpf(str(worst['coherent_stability_spread'])) <= SPREAD_MAX and recheck <= RECHECK_MAX)
    if not valid: cls='BRANCH_SUM_COLLISION_CANCELLATION_NUMERICAL_INVALID'
    elif scientific_pass: cls='SOURCE_TOLLER_BRANCH_SUM_PAIR_COLLISION_POWER_INTEGRABLE_ON_FROZEN_GRID'
    else: cls='SOURCE_TOLLER_BRANCH_SUM_PAIR_COLLISION_OBSTRUCTION_ON_FROZEN_GRID'
    out={
      'iteration':448,'gamma':a.gamma,'j':a.j,'rho':a.gamma*a.j,'precision_dps':100,'recheck_dps':130,
      'beta_exponents_n':list(NS),'frozen_power_threshold_less_than':2.90,'frozen_stability_spread_max':0.20,'frozen_recheck_delta_max':0.02,
      'records':rows,'worst_witness':worst,'worst_witness_recheck_130dps':match130,'worst_power_recheck_abs_delta':float(recheck),
      'minimum_cancellation_ratio':min_ratio,'isolated_branch_tail_power_max':isolated,'numerically_valid':valid,'scientific_lane_pass':scientific_pass,'classification':cls,
      'scope_guard':'Coherent Toller two-branch pair-collision diagnostic only; not the full source-defined causal-vertex invariant contraction, not a simultaneous multi-pair theorem, not an absolute-integrability/PV/distributional equivalence theorem, no terminal D7 and no Candidate Gravity authorization.'
    }
    os.makedirs('build/lqg-iter448',exist_ok=True); fn=f'build/lqg-iter448/g{a.gamma}_j{a.j}.json'; open(fn,'w').write(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps(out,indent=2,sort_keys=True))
    if not valid: raise SystemExit(3)

if __name__=='__main__': main()

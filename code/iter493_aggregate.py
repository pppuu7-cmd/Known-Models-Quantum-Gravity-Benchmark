#!/usr/bin/env python3
import argparse, glob, json, math, os, statistics

EXPECTED={(c,b) for c in ('0to5','1to4','2to3') for b in range(4)}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--root',required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    jobs=[]
    for f in glob.glob(os.path.join(a.root,'**','*.json'),recursive=True):
        try:
            j=json.load(open(f))
            if j.get('iteration')==493 and 'causal' in j and 'block' in j: jobs.append(j)
        except Exception: pass
    keyed={(j['causal'],int(j['block'])):j for j in jobs}
    missing=sorted(EXPECTED-set(keyed)); invalid=sorted(k for k,j in keyed.items() if not j.get('valid',False))
    Ds=[]; Qs=[]; ddisc=[]; qdisc=[]; stable=0; nstates=0; coord_norm={}
    extrema={'D':None,'Q':None}
    for (causal,b),j in keyed.items():
        for rec in j.get('records',[]):
            c=int(rec['coord']); acc=[]
            for r in rec.get('per_rho',[]):
                for key in ('D_h005','D_h010'):
                    x=float(r[key]); Ds.append(abs(x)); acc.append(x)
                    if extrema['D'] is None or abs(x)>extrema['D']['abs_value']: extrema['D']={'abs_value':abs(x),'value':x,'causal':causal,'coord':c,'rho':r['rho'],'step':key}
                for key in ('Q_h005','Q_h010'):
                    x=float(r[key]); Qs.append(abs(x))
                    if extrema['Q'] is None or abs(x)>extrema['Q']['abs_value']: extrema['Q']={'abs_value':abs(x),'value':x,'causal':causal,'coord':c,'rho':r['rho'],'step':key}
                ddisc.append(float(r['D_scaled_discrepancy'])); qdisc.append(float(r['Q_scaled_discrepancy']))
                stable += int(bool(r['D_sign_stable'])); nstates += 1
            coord_norm.setdefault(c,0.0); coord_norm[c]+=sum(x*x for x in acc)
    valid=(not missing and not invalid and len(keyed)==12 and all(math.isfinite(x) for x in Ds+Qs+ddisc+qdisc))
    cls='ITER493_CRITICAL_Q1_LOCAL_VARIATION_QUALIFIED_SCOPED' if valid else 'INFRASTRUCTURE_OR_NUMERICAL_FAIL_ITER493'
    out={'iteration':493,'classification':cls,'valid':bool(valid),'job_count':len(keyed),'missing_jobs':[list(x) for x in missing],'invalid_jobs':[list(x) for x in invalid],
         'D_abs_max':max(Ds) if Ds else None,'D_abs_median':statistics.median(Ds) if Ds else None,'Q_abs_max':max(Qs) if Qs else None,'Q_abs_median':statistics.median(Qs) if Qs else None,
         'D_scaled_discrepancy_max':max(ddisc) if ddisc else None,'Q_scaled_discrepancy_max':max(qdisc) if qdisc else None,'D_sign_stable_count':stable,'state_count':nstates,
         'D_extremum':extrema['D'],'Q_extremum':extrema['Q'],'coordinate_response_norm':{str(k):math.sqrt(v) for k,v in sorted(coord_norm.items())},
         'interpretation_ceiling':'finite-grid critical-q1 local first/second variation diagnostic only; no analytic/uniform open-neighborhood, positive-measure Haar, D7-S2 closure, terminal label, or Candidate Gravity authorization'}
    os.makedirs(os.path.dirname(a.out) or '.',exist_ok=True); json.dump(out,open(a.out,'w'),indent=2,sort_keys=True); print(json.dumps(out,indent=2,sort_keys=True))

if __name__=='__main__': main()

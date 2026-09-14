#!/usr/bin/env python3
import argparse, glob, json, math, os, statistics

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--root',required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    files=glob.glob(os.path.join(a.root,'**','*.json'),recursive=True)
    jobs=[]
    for p in files:
        try:
            with open(p) as f: d=json.load(f)
            if d.get('iteration')==494: jobs.append(d)
        except Exception: pass
    missing=max(0,9-len(jobs)); invalid=[j.get('job') for j in jobs if not j.get('valid',False)]
    vals=[]; discrepancies=[]; signs=0; total_signs=0; coord_norm={str(c):0.0 for c in [0,1,3,5,6,11]}; extremum=None
    for j in jobs:
        for r in j.get('records',[]):
            i,k=r['pair']
            for x in r['per_rho']:
                for key in ('M_h005','M_h010'):
                    v=float(x[key]); vals.append(abs(v)); coord_norm[str(i)]+=v*v; coord_norm[str(k)]+=v*v
                    if extremum is None or abs(v)>extremum['abs_value']:
                        extremum={'abs_value':abs(v),'value':v,'causal':j['causal'],'pair':[i,k],'rho':x['rho'],'step':key}
                discrepancies.append(float(x['scaled_discrepancy'])); total_signs+=1; signs+=int(bool(x['sign_stable']))
    for c in coord_norm: coord_norm[c]=math.sqrt(coord_norm[c])
    valid=(len(jobs)==9 and not invalid)
    out={'iteration':494,'job_count':len(jobs),'missing_jobs':missing,'invalid_jobs':invalid,'valid':valid,
         'classification':'ITER494_CRITICAL_Q1_MIXED_CURVATURE_QUALIFIED_SCOPED' if valid else 'INFRASTRUCTURE_OR_NUMERICAL_FAIL_ITER494',
         'M_abs_max':max(vals) if vals else None,'M_abs_median':statistics.median(vals) if vals else None,
         'M_extremum':extremum,'M_scaled_discrepancy_max':max(discrepancies) if discrepancies else None,
         'M_sign_stable_count':signs,'M_sign_total':total_signs,'coordinate_mixed_response_norm':coord_norm,
         'interpretation_ceiling':'finite-grid q1 mixed-curvature prerequisite only; no interval/uniform open-neighborhood, positive-measure Haar, D7-S2 closure, terminal label, or Candidate Gravity authorization'}
    os.makedirs(os.path.dirname(a.out) or '.',exist_ok=True)
    with open(a.out,'w') as f: json.dump(out,f,indent=2,sort_keys=True)
    print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__': main()

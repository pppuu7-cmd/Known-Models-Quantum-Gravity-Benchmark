#!/usr/bin/env python3
import argparse, glob, json, math, os, statistics

EXPECTED=12

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--root',required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    files=sorted(glob.glob(os.path.join(a.root,'iter495-*','*.json')))
    jobs=[]; invalid=[]; rema=[]; r2=[]; r3=[]; ratios=[]
    for p in files:
        try:
            x=json.load(open(p)); jobs.append(x)
            if not x.get('valid',False): invalid.append(x.get('job',p))
            for rec in x.get('records',[]):
                for amp,pack in rec.get('by_amp',{}).items():
                    for q in pack.get('per_rho',[]):
                        rema.append(float(q['abs_remainder'])); r2.append(float(q['r_over_a2'])); r3.append(float(q['r_over_a3']))
                for q in rec.get('remainder_ratio',[]): ratios.append(float(q['small_over_large']))
        except Exception as e:
            invalid.append(f'{p}:{e!r}')
    valid=(len(jobs)==EXPECTED and not invalid and all(math.isfinite(v) for v in rema+r2+r3+ratios))
    out={
      'iteration':495,'job_count':len(jobs),'missing_jobs':max(0,EXPECTED-len(jobs)),'invalid_jobs':invalid,'valid':bool(valid),
      'classification':'ITER495_MULTIVARIATE_TAYLOR_STRESS_QUALIFIED_SCOPED' if valid else 'INFRASTRUCTURE_OR_NUMERICAL_FAIL_ITER495',
      'abs_remainder_max':max(rema) if rema else None,'abs_remainder_median':statistics.median(rema) if rema else None,
      'r_over_a2_max':max(r2) if r2 else None,'r_over_a3_max':max(r3) if r3 else None,
      'small_over_large_median':statistics.median(ratios) if ratios else None,
      'small_over_large_max':max(ratios) if ratios else None,
      'cubic_expected_ratio':0.125,
      'interpretation_ceiling':'finite-set multivariate q1 Taylor stress only; no interval/uniform open-neighborhood, positive-measure Haar, D7-S2 closure, terminal label, or Candidate Gravity authorization'
    }
    os.makedirs(os.path.dirname(a.out) or '.',exist_ok=True)
    json.dump(out,open(a.out,'w'),indent=2,sort_keys=True); print(json.dumps(out,indent=2,sort_keys=True))

if __name__=='__main__': main()

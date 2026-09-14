#!/usr/bin/env python3
import argparse, collections, glob, json, math, os
EXPECTED=[f'{c}-b{b}' for c in ['0to5','1to4','2to3'] for b in range(4)]

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--root',required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    rows=[]
    for p in sorted(glob.glob(os.path.join(a.root,'**','*.json'),recursive=True)):
        with open(p) as f: x=json.load(f)
        if x.get('iteration')==502: rows.append(x)
    ids=[x.get('job') for x in rows]; cnt=collections.Counter(ids)
    missing=sorted(set(EXPECTED)-set(ids)); dup=sorted(k for k,v in cnt.items() if v!=1)
    blocker=[x.get('job') for x in rows if x.get('method_blocker') or not x.get('valid',False)]
    point_fail=[x.get('job') for x in rows if not x.get('point_regression_all_pass',False)]
    structure=bool(len(rows)==12 and not missing and not dup)
    classes=[]; min_s=math.inf; max_s=-math.inf; max_d=-math.inf; min_beta=math.inf; nsub=0
    for x in rows:
        if x.get('min_beta_lower') is not None: min_beta=min(min_beta,float(x['min_beta_lower']))
        for p in x.get('paths',[]):
            for b in p.get('subboxes',[]):
                if b.get('error'): continue
                nsub+=1
                for q in b.get('per_rho',[]):
                    classes.append(q['classification']); min_s=min(min_s,float(q['S_lower'])); max_s=max(max_s,float(q['S_upper'])); max_d=max(max_d,float(q['drift_upper']))
    method=bool((not structure) or blocker or point_fail)
    if method: cls='ITER502_NUMERICAL_METHOD_BLOCKER'
    elif classes and all(c=='INTERVAL_ROBUST_NONDECAY' for c in classes): cls='ITER502_DYADIC_DIRECT_MAX_ENVELOPE_INTERVAL_ROBUST_QUALIFIED_SCOPED'
    elif classes and all(c in ('INTERVAL_ROBUST_NONDECAY','INTERVAL_NONDECAY') for c in classes): cls='ITER502_DYADIC_DIRECT_MAX_ENVELOPE_INTERVAL_NONDECAY_QUALIFIED_SCOPED'
    elif any(c=='INTERVAL_UNIFORM_DECAY_WITNESS' for c in classes): cls='SCIENTIFIC_FAIL_ITER502_UNIFORM_NONDECAY_INTERVAL'
    else: cls='ITER502_VALIDATED_INTERVAL_INCONCLUSIVE_SCOPED'
    out={'iteration':502,'classification':cls,'valid_structure':structure,'method_blocker':method,'n_jobs':len(rows),'job_ids':ids,
         'missing_job_ids':missing,'duplicate_job_ids':dup,'blocker_job_ids':blocker,'point_regression_fail_job_ids':point_fail,
         'n_valid_subboxes':nsub,'n_rho_subbox_states':len(classes),'class_counts':dict(collections.Counter(classes)),
         'global_min_S_lower':None if not classes else min_s,'global_max_S_upper':None if not classes else max_s,
         'global_max_drift_upper':None if not classes else max_d,'global_min_beta_lower':None if min_beta is math.inf else min_beta,
         'jobs':[{'job':x.get('job'),'classification':x.get('classification'),'valid':x.get('valid'),'method_blocker':x.get('method_blocker'),'point_regression':x.get('point_regression_all_pass')} for x in rows],
         'scope':'prospectively frozen 8-way exact cover repair of each Iter501 amplitude box; unchanged 243-channel max-envelope science thresholds; no multidimensional neighborhood, Haar or spectral theorem'}
    os.makedirs(os.path.dirname(a.out) or '.',exist_ok=True)
    with open(a.out,'w') as f: json.dump(out,f,indent=2,sort_keys=True)
    print(json.dumps(out,indent=2,sort_keys=True)); raise SystemExit(0)
if __name__=='__main__': main()

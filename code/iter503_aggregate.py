#!/usr/bin/env python3
import argparse, glob, json, os

EXPECTED=['0to5-b0','1to4-b0','2to3-b0']


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--root',required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    rows=[]
    for p in sorted(glob.glob(os.path.join(a.root,'**','*.json'),recursive=True)):
        with open(p) as f: x=json.load(f)
        if x.get('iteration')==503: rows.append(x)
    ids=[x.get('job') for x in rows]
    missing=sorted(set(EXPECTED)-set(ids)); dup=sorted({x for x in ids if ids.count(x)>1})
    invalid=[x.get('job') for x in rows if x.get('classification')=='INFRASTRUCTURE_OR_VALIDATION_FAIL_ITER503' or not x.get('valid',False)]
    insufficient=[x.get('job') for x in rows if x.get('classification')=='ITER503_CENTERED_MULTILINEAR_METHOD_INSUFFICIENT_SCOPED']
    qualified=[x.get('job') for x in rows if x.get('classification')=='ITER503_CENTERED_MULTILINEAR_METHOD_QUALIFIED_SCOPED']
    structure=bool(len(rows)==3 and not missing and not dup)
    if not structure or invalid:
        cls='INFRASTRUCTURE_OR_VALIDATION_FAIL_ITER503'
    elif insufficient or len(qualified)!=3:
        cls='ITER503_CENTERED_MULTILINEAR_METHOD_INSUFFICIENT_SCOPED'
    else:
        cls='ITER503_CENTERED_MULTILINEAR_METHOD_QUALIFIED_SCOPED'
    total_states=sum(int(x.get('total_envelope_states',0)) for x in rows)
    positive=sum(int(x.get('positive_envelope_states',0)) for x in rows)
    out={'iteration':503,'classification':cls,'valid_structure':structure,'n_jobs':len(rows),
         'missing_job_ids':missing,'duplicate_job_ids':dup,'invalid_job_ids':invalid,
         'insufficient_job_ids':insufficient,'qualified_job_ids':qualified,
         'positive_envelope_states':positive,'total_envelope_states':total_states,
         'all_point_regressions_pass':bool(structure and not invalid and not insufficient and all(x.get('point_regression_all_pass',False) for x in rows)),
         'max_midpoint_channel_relative_residual':max([float(x.get('max_midpoint_channel_relative_residual',0.0)) for x in rows],default=None),
         'jobs':[{'job':x.get('job'),'classification':x.get('classification'),'positive_states':x.get('positive_envelope_states'),
                  'total_states':x.get('total_envelope_states'),'point_pass':x.get('point_regression_all_pass'),
                  'min_beta':x.get('min_beta_lower'),'midpoint_channel_rel':x.get('max_midpoint_channel_relative_residual')} for x in rows],
         'scope':'centered multilinear enclosure method diagnostic on frozen block 0 only; no science NONDECAY/DECAY or D7 closure'}
    os.makedirs(os.path.dirname(a.out) or '.',exist_ok=True)
    with open(a.out,'w') as f: json.dump(out,f,indent=2,sort_keys=True)
    print(json.dumps(out,indent=2,sort_keys=True)); raise SystemExit(0)

if __name__=='__main__': main()

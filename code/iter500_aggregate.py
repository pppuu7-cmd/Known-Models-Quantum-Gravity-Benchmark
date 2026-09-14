#!/usr/bin/env python3
import argparse, collections, glob, json, math, os

EXPECTED=[0,1,2,3]


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--root',required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    rows=[]
    for p in sorted(glob.glob(os.path.join(a.root,'**','*.json'),recursive=True)):
        with open(p) as f: x=json.load(f)
        if x.get('iteration')==500: rows.append(x)
    ids=[x.get('block') for x in rows]; counts=collections.Counter(ids)
    missing=sorted(set(EXPECTED)-set(ids)); dup=sorted(k for k,v in counts.items() if v!=1)
    structure=bool(len(rows)==4 and not missing and not dup)
    blockers=[x.get('block') for x in rows if x.get('method_blocker') or x.get('classification')=='ITER500_NUMERICAL_METHOD_BLOCKER']
    science=[x.get('block') for x in rows if x.get('classification')=='SCIENTIFIC_FAIL_ITER500_COMPACT_KAK_COVARIANCE']
    qualified=[x.get('block') for x in rows if x.get('classification')=='ITER500_COMPACT_SANDWICH_FACTORIZED_KAK_LANE_QUALIFIED_SCOPED']
    block0=next((x for x in rows if x.get('block')==0),None)
    neg=bool(block0 and block0.get('negative_control',{}).get('reproduces_old_limitation'))
    if not structure or blockers or not neg:
        cls='ITER500_NUMERICAL_METHOD_BLOCKER'
    elif science:
        cls='SCIENTIFIC_FAIL_ITER500_COMPACT_KAK_COVARIANCE'
    elif len(qualified)==4:
        cls='ITER500_COMPACT_SANDWICH_FACTORIZED_KAK_QUALIFIED_SCOPED'
    else:
        cls='ITER500_NUMERICAL_METHOD_BLOCKER'
    mins=[x.get('min_beta_lower') for x in rows if x.get('min_beta_lower') is not None]
    out={'iteration':500,'classification':cls,'valid_structure':structure,'n_jobs':len(rows),'block_ids':ids,'missing_blocks':missing,'duplicate_blocks':dup,
         'blocker_blocks':blockers,'scientific_fail_blocks':science,'qualified_blocks':qualified,'old_method_negative_control_pass':neg,
         'global_min_beta_lower':min(mins) if mins else None,
         'global_max_midpoint_matrix_relative_error':max([x.get('max_midpoint_matrix_relative_error',0.0) for x in rows],default=None),
         'global_max_midpoint_beta_absolute_error':max([x.get('max_midpoint_beta_absolute_error',0.0) for x in rows],default=None),
         'global_max_midpoint_toller_relative_error':max([x.get('max_midpoint_toller_relative_error',0.0) for x in rows],default=None),
         'jobs':[{'block':x.get('block'),'classification':x.get('classification'),'valid':x.get('valid'),'method_blocker':x.get('method_blocker'),'covariance_fail':x.get('covariance_fail'),'regression_fail':x.get('regression_fail'),'states_evaluated':x.get('states_evaluated')} for x in rows],
         'scope':'validated compact-sandwich/factorized KAK/Toller enabling gate only; no NONDECAY, max-envelope, Haar or spectral-integration claim'}
    os.makedirs(os.path.dirname(a.out) or '.',exist_ok=True)
    with open(a.out,'w') as f: json.dump(out,f,indent=2,sort_keys=True)
    print(json.dumps(out,indent=2,sort_keys=True)); raise SystemExit(0)
if __name__=='__main__': main()

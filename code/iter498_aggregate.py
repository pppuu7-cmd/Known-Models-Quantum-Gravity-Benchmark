#!/usr/bin/env python3
import argparse, glob, json, math, os

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--root',required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    files=sorted(glob.glob(os.path.join(a.root,'**','*.json'),recursive=True))
    rows=[]
    for p in files:
        with open(p) as f: x=json.load(f)
        if x.get('iteration')==498: rows.append(x)
    ids=[x.get('job') for x in rows]
    expected=[f'{c}-b{b}' for c in ['0to5','1to4','2to3'] for b in range(4)]
    missing=sorted(set(expected)-set(ids)); invalid=[x.get('job') for x in rows if not x.get('valid',False)]
    valid=bool(len(rows)==12 and not missing and not invalid)
    switches=sum(int(x.get('argmax_switches',0)) for x in rows) if rows else 0
    mingap=min([float(x.get('min_relative_top2_gap',float('inf'))) for x in rows],default=float('nan'))
    minbeta=min([float(x.get('min_positive_kak_beta',float('inf'))) for x in rows],default=float('nan'))
    gap_bad=bool(valid and (switches>0 or mingap<1e-6)); beta_bad=bool(valid and minbeta<1e-6)
    if not valid: cls='INFRASTRUCTURE_OR_NUMERICAL_FAIL_ITER498'
    elif gap_bad and beta_bad: cls='ITER498_MAX_AND_KAK_REGULARITY_BLOCKERS_IDENTIFIED_SCOPED'
    elif gap_bad: cls='ITER498_MAX_ENVELOPE_NONSMOOTH_BLOCKER_IDENTIFIED_SCOPED'
    elif beta_bad: cls='ITER498_KAK_BRANCH_MARGIN_BLOCKER_IDENTIFIED_SCOPED'
    else: cls='ITER498_REGULAR_SAMPLED_PATH_QUALIFIED_SCOPED'
    out={'iteration':498,'classification':cls,'valid':valid,'n_jobs':len(rows),'missing_job_ids':missing,'invalid_job_ids':invalid,
         'argmax_switches_total':switches,'min_relative_top2_gap':mingap,'min_positive_kak_beta':minbeta,
         'all_frozen_predicates_pass':valid,'jobs':[{'job':x.get('job'),'classification':x.get('classification'),'switches':x.get('argmax_switches'),'min_gap':x.get('min_relative_top2_gap'),'min_beta':x.get('min_positive_kak_beta')} for x in rows],
         'scope':'sampled regularity audit only; selects rigorous interval method but is not a continuum/interval or positive-measure certificate'}
    os.makedirs(os.path.dirname(a.out) or '.',exist_ok=True)
    with open(a.out,'w') as f: json.dump(out,f,indent=2,sort_keys=True)
    print(json.dumps(out,indent=2,sort_keys=True)); raise SystemExit(0)
if __name__=='__main__': main()

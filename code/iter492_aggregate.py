#!/usr/bin/env python3
import argparse, glob, json, os

Q_VALUES=[0.50,0.75,1.00,1.25,1.50]
CAUSALS=['0to5','1to4','2to3']


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--root',required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    files=sorted(glob.glob(os.path.join(a.root,'**','*.json'),recursive=True))
    jobs=[]
    for p in files:
        try:
            x=json.load(open(p))
        except Exception:
            continue
        if x.get('iteration')==492 and 'causal' in x and 'q_index' in x:
            jobs.append(x)

    by={(x.get('causal'),x.get('q_index')):x for x in jobs}
    expected=[(c,qi) for c in CAUSALS for qi in range(5)]
    missing=[f'{c}-q{qi}' for c,qi in expected if (c,qi) not in by]
    invalid_jobs=[]; q_states=[]
    all_slopes=[]; all_drifts=[]; max_kak=0.0; max_identity=0.0

    for qi,q in enumerate(Q_VALUES):
        lane_rows=[]
        for c in CAUSALS:
            x=by.get((c,qi))
            if not x:
                continue
            if not x.get('all_lanes_valid',False): invalid_jobs.append(f'{c}-q{qi}')
            for lane in x.get('lanes',[]):
                lane_rows.append((c,lane))
                for s in lane.get('signed',[]):
                    max_kak=max(max_kak,float(s.get('hp_kak_reconstruction_max',0.0)))
                    max_identity=max(max_identity,float(s.get('source_object_identity_relative_max',0.0)))
                    for r in s.get('results',[]):
                        all_slopes.append(float(r['actual_slope']))
                        all_drifts.append(float(r['slope_drift']))
        full_valid=(len(lane_rows)==24 and all(l['valid'] for _,l in lane_rows))
        full_nondecay=bool(full_valid and all(l['all_nondecay'] for _,l in lane_rows))
        full_robust=bool(full_valid and all(l['all_robust'] for _,l in lane_rows))
        q_states.append({'q_index':qi,'q':q,'lane_count':len(lane_rows),'full_valid':full_valid,
                         'full_nondecay':full_nondecay,'full_robust':full_robust,
                         'failed_lane_count':sum(1 for _,l in lane_rows if l.get('valid') and not l.get('all_nondecay'))})

    all_valid=(not missing and not invalid_jobs and len(jobs)==15 and all(s['full_valid'] for s in q_states))
    if not all_valid:
        cls='INFRASTRUCTURE_OR_NUMERICAL_FAIL_ITER492'
    else:
        full=[s for s in q_states if s['full_nondecay']]
        if len(full)==len(q_states):
            cls='ITER492_TANGENT_ALL_Q_NONDECAY_QUALIFIED_SCOPED'
        elif full and any((not s['full_nondecay']) and s['q']<min(x['q'] for x in full) for s in q_states):
            cls='ITER492_TANGENT_BOUNDARY_LAYER_BRACKET_QUALIFIED_SCOPED'
        elif not full:
            cls='SCIENTIFIC_FAIL_ITER492_TANGENT_BOUNDARY_LAYER'
        else:
            # Valid but non-monotone/no lower-q bracket: report without interpolation.
            cls='ITER492_TANGENT_NONMONOTONE_DIAGNOSTIC_SCOPED'

    out={
        'iteration':492,'classification':cls,'valid':bool(all_valid),
        'job_count':len(jobs),'missing_jobs':missing,'invalid_jobs':sorted(set(invalid_jobs)),
        'q_states':q_states,
        'smallest_full_nondecay_q':min([s['q'] for s in q_states if s['full_nondecay']],default=None),
        'actual_slope_min':min(all_slopes) if all_slopes else None,
        'actual_slope_max':max(all_slopes) if all_slopes else None,
        'slope_drift_max':max(all_drifts) if all_drifts else None,
        'hp_kak_reconstruction_max':max_kak,
        'source_object_identity_relative_max':max_identity,
        'interpretation_ceiling':'finite frozen tangent directions and finite R boundary-layer diagnostic only; no fixed open angular neighborhood, positive-measure Haar claim, D7-S2 closure, terminal D7 label or Candidate Gravity authorization',
    }
    os.makedirs(os.path.dirname(a.out) or '.',exist_ok=True)
    with open(a.out,'w') as f: json.dump(out,f,indent=2,sort_keys=True)
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=='__main__': main()

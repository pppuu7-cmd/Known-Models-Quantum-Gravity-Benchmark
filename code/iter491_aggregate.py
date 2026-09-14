#!/usr/bin/env python3
import argparse, glob, json, os

CAUSALS=('0to5','1to4','2to3')
RADII=(0,1,2,3)
EPS=(0.0025,0.005,0.01,0.02)
EXPECTED={f'{c}-r{r}' for c in CAUSALS for r in RADII}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--root',required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    rows=[]
    for fn in glob.glob(os.path.join(a.root,'**','*.json'),recursive=True):
        try:
            with open(fn) as f: x=json.load(f)
            if x.get('iteration')==491 and x.get('lane') in EXPECTED: rows.append(x)
        except Exception:
            pass
    by={x['lane']:x for x in rows}
    missing=sorted(EXPECTED-set(by))
    invalid=sorted(k for k,v in by.items() if not v.get('valid',False))

    robust_radii=[]; nondecay_radii=[]
    for r in RADII:
        vals=[by.get(f'{c}-r{r}') for c in CAUSALS]
        if all(v is not None and v.get('valid') for v in vals):
            if all(v.get('classification')=='ITER491_SAMPLED_ROBUST_THICKENING_LANE' for v in vals): robust_radii.append(r)
            if all(v.get('classification') in ('ITER491_SAMPLED_ROBUST_THICKENING_LANE','ITER491_SAMPLED_NONDECAY_THICKENING_LANE') for v in vals): nondecay_radii.append(r)

    if missing or invalid:
        cls='INFRASTRUCTURE_OR_NUMERICAL_FAIL_ITER491'; passed=False
    elif robust_radii:
        cls='ITER491_FULL_ANGULAR_SAMPLED_ROBUST_THICKENING_QUALIFIED_SCOPED'; passed=True
    elif nondecay_radii:
        cls='ITER491_FULL_ANGULAR_SAMPLED_NONDECAY_THICKENING_QUALIFIED_SCOPED'; passed=True
    else:
        cls='SCIENTIFIC_FAIL_ITER491_ANGULAR_THICKENING_HP'; passed=False

    slopes=[r.get('actual_slope') for v in by.values() for s in v.get('samples',[]) for r in s.get('results',[]) if isinstance(r.get('actual_slope'),(int,float))]
    drifts=[r.get('slope_drift') for v in by.values() for s in v.get('samples',[]) for r in s.get('results',[]) if isinstance(r.get('slope_drift'),(int,float))]
    identity=[s.get('source_object_identity_relative_max') for v in by.values() for s in v.get('samples',[]) if isinstance(s.get('source_object_identity_relative_max'),(int,float))]
    hp_rec=[s.get('hp_kak_reconstruction_max') for v in by.values() for s in v.get('samples',[]) if isinstance(s.get('hp_kak_reconstruction_max'),(int,float))]
    anchor_edge=[v.get('precision_anchor',{}).get('edge_relative_difference_max') for v in by.values() if isinstance(v.get('precision_anchor',{}).get('edge_relative_difference_max'),(int,float))]
    anchor_beta=[v.get('precision_anchor',{}).get('beta_absolute_difference_max') for v in by.values() if isinstance(v.get('precision_anchor',{}).get('beta_absolute_difference_max'),(int,float))]

    out={
      'iteration':491,'classification':cls,'pass':passed,'expected_lanes':12,'present_lanes':len(by),
      'missing_lanes':missing,'invalid_lanes':invalid,
      'robust_radius_indices':robust_radii,'robust_radii':[EPS[r] for r in robust_radii],
      'sampled_nondecay_radius_indices':nondecay_radii,'sampled_nondecay_radii':[EPS[r] for r in nondecay_radii],
      'largest_robust_radius':EPS[max(robust_radii)] if robust_radii else None,
      'largest_sampled_nondecay_radius':EPS[max(nondecay_radii)] if nondecay_radii else None,
      'sampled_actual_slope_min':min(slopes) if slopes else None,'sampled_actual_slope_max':max(slopes) if slopes else None,
      'sampled_slope_drift_max':max(drifts) if drifts else None,
      'source_object_identity_relative_max':max(identity) if identity else None,
      'hp_kak_reconstruction_max':max(hp_rec) if hp_rec else None,
      'precision_anchor_edge_relative_max':max(anchor_edge) if anchor_edge else None,
      'precision_anchor_beta_abs_max':max(anchor_beta) if anchor_beta else None,
      'lane_classifications':{k:v.get('classification') for k,v in sorted(by.items())},
      'lane_results':[by[k] for k in sorted(by)],
      'scope':'same frozen Iter490 finite sampled 20-D angular thickening re-evaluated from 100-digit source group construction; no uniform-neighborhood/Haar-divergence theorem'
    }
    os.makedirs(os.path.dirname(a.out) or '.',exist_ok=True)
    with open(a.out,'w') as f: json.dump(out,f,indent=2,sort_keys=True)
    print(json.dumps(out,indent=2,sort_keys=True))
    # Scientific FAIL is terminal science, not infrastructure failure.
    raise SystemExit(3 if cls=='INFRASTRUCTURE_OR_NUMERICAL_FAIL_ITER491' else 0)

if __name__=='__main__': main()

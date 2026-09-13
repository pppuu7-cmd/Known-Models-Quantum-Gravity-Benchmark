#!/usr/bin/env python3
import argparse, glob, json, os

PANELS=('A','C')
CLUSTERS=(1,2,3,4)
CAUSALS=('0to5','1to4','2to3')
EXPECTED={f'{p}-s{s}-{c}' for p in PANELS for s in CLUSTERS for c in CAUSALS}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--root',required=True); ap.add_argument('--out',required=True); args=ap.parse_args()
    files=glob.glob(os.path.join(args.root,'**','*.json'),recursive=True)
    rows=[]
    for fn in files:
        try:
            with open(fn) as f: x=json.load(f)
            if x.get('iteration')==486 and x.get('lane') in EXPECTED: rows.append(x)
        except Exception:
            pass
    by={x['lane']:x for x in rows}
    missing=sorted(EXPECTED-set(by))
    invalid=sorted(k for k,v in by.items() if not v.get('valid',False))
    scientific_fail=sorted(k for k,v in by.items() if v.get('classification')=='SCIENTIFIC_FAIL_ITER486_HAAR_ESCAPE_ACTUAL_ENVELOPE')
    inconclusive=sorted(k for k,v in by.items() if v.get('classification')=='INCONCLUSIVE_ITER486_HAAR_ESCAPE_ASYMPTOTIC')
    decay=sorted(k for k,v in by.items() if v.get('classification')=='ITER486_LANE_HAAR_ESCAPE_DECAY')

    points=[]
    for v in by.values():
        for r in v.get('rho_results',[]): points.append((v['lane'],r))
    nondecay_points=[{'lane':l,**r} for l,r in points if r.get('state')=='NONDECAY']
    inconclusive_points=[{'lane':l,**r} for l,r in points if r.get('state')=='ASYMPTOTIC_INCONCLUSIVE']
    decay_points=[{'lane':l,**r} for l,r in points if r.get('state')=='DECAY']

    if missing or invalid:
        cls='INFRASTRUCTURE_OR_SOURCE_FAIL_ITER486'; passed=False
    elif scientific_fail or nondecay_points:
        cls='SCIENTIFIC_FAIL_ITER486_HAAR_ESCAPE_ACTUAL_ENVELOPE'; passed=False
    elif inconclusive or inconclusive_points:
        cls='INCONCLUSIVE_ITER486_HAAR_ESCAPE_ASYMPTOTIC'; passed=False
    elif len(decay)==24 and len(decay_points)==96:
        cls='ITER486_HAAR_ESCAPE_ACTUAL_ENVELOPE_DECAY_QUALIFIED_SCOPED'; passed=True
    else:
        cls='INFRASTRUCTURE_OR_SOURCE_FAIL_ITER486'; passed=False

    actual=[r.get('actual_slope') for _,r in points if isinstance(r.get('actual_slope'),(int,float))]
    drift=[r.get('slope_drift') for _,r in points if isinstance(r.get('slope_drift'),(int,float))]
    out={
      'iteration':486,'classification':cls,'pass':passed,'expected_lanes':24,'present_lanes':len(by),
      'missing':missing,'invalid':invalid,'scientific_fail_lanes':scientific_fail,'inconclusive_lanes':inconclusive,'decay_lanes':decay,
      'nondecay_point_count':len(nondecay_points),'inconclusive_point_count':len(inconclusive_points),'decay_point_count':len(decay_points),
      'actual_slope_min':min(actual) if actual else None,'actual_slope_max':max(actual) if actual else None,
      'slope_drift_max':max(drift) if drift else None,
      'nondecay_points':nondecay_points,'inconclusive_points':inconclusive_points,
      'scope':'Iter486 full j=1 shared-node/intertwiner radial Haar escape envelope only; no full Haar/spectral/physical-vertex theorem'
    }
    os.makedirs(os.path.dirname(args.out) or '.',exist_ok=True)
    with open(args.out,'w') as f: json.dump(out,f,indent=2,sort_keys=True)
    print(json.dumps(out,indent=2,sort_keys=True))
    # Aggregate artifact must exist for every scientific label; only infrastructure is a workflow failure.
    raise SystemExit(3 if cls=='INFRASTRUCTURE_OR_SOURCE_FAIL_ITER486' else 0)

if __name__=='__main__': main()

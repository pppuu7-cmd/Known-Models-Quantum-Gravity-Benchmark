#!/usr/bin/env python3
import argparse, glob, json, os

PANELS=('A','C'); CLUSTERS=(1,2,3,4); CAUSALS=('0to5','1to4','2to3')
EXPECTED={f'{p}-s{s}-{c}' for p in PANELS for s in CLUSTERS for c in CAUSALS}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--root',required=True); ap.add_argument('--out',required=True); args=ap.parse_args()
    rows=[]
    for fn in glob.glob(os.path.join(args.root,'**','*.json'),recursive=True):
        try:
            with open(fn) as f: x=json.load(f)
            if x.get('iteration')==487 and x.get('lane') in EXPECTED: rows.append(x)
        except Exception: pass
    by={x['lane']:x for x in rows}
    missing=sorted(EXPECTED-set(by)); invalid=sorted(k for k,v in by.items() if not v.get('valid',False))
    points=[(v['lane'],r) for v in by.values() for r in v.get('rho_results',[])]
    nd=[{'lane':l,**r} for l,r in points if r.get('state')=='NONDECAY']
    inc=[{'lane':l,**r} for l,r in points if r.get('state')=='ASYMPTOTIC_INCONCLUSIVE']
    dec=[{'lane':l,**r} for l,r in points if r.get('state')=='DECAY']
    fail_lanes=sorted(k for k,v in by.items() if v.get('classification')=='SCIENTIFIC_FAIL_ITER487_HAAR_ESCAPE_ACTUAL_ENVELOPE')
    inconclusive_lanes=sorted(k for k,v in by.items() if v.get('classification')=='INCONCLUSIVE_ITER487_HAAR_ESCAPE_ASYMPTOTIC')
    decay_lanes=sorted(k for k,v in by.items() if v.get('classification')=='ITER487_LANE_HAAR_ESCAPE_DECAY')

    if missing or invalid:
        cls='INFRASTRUCTURE_OR_SOURCE_FAIL_ITER487'; passed=False
    elif nd or fail_lanes:
        cls='SCIENTIFIC_FAIL_ITER487_HAAR_ESCAPE_ACTUAL_ENVELOPE'; passed=False
    elif inc or inconclusive_lanes:
        cls='INCONCLUSIVE_ITER487_HAAR_ESCAPE_ASYMPTOTIC'; passed=False
    elif len(dec)==96 and len(decay_lanes)==24:
        cls='ITER487_HAAR_ESCAPE_ACTUAL_ENVELOPE_DECAY_QUALIFIED_SCOPED'; passed=True
    else:
        cls='INFRASTRUCTURE_OR_SOURCE_FAIL_ITER487'; passed=False

    slopes=[r.get('actual_slope') for _,r in points if isinstance(r.get('actual_slope'),(int,float))]
    rel=[v.get('escaped_relative_nonrepresentation_max') for v in by.values() if isinstance(v.get('escaped_relative_nonrepresentation_max'),(int,float))]
    baseabs=[v.get('base_absolute_nonrepresentation_max') for v in by.values() if isinstance(v.get('base_absolute_nonrepresentation_max'),(int,float))]
    out={'iteration':487,'classification':cls,'pass':passed,'expected_lanes':24,'present_lanes':len(by),
         'missing':missing,'invalid':invalid,'scientific_fail_lanes':fail_lanes,'inconclusive_lanes':inconclusive_lanes,'decay_lanes':decay_lanes,
         'nondecay_point_count':len(nd),'inconclusive_point_count':len(inc),'decay_point_count':len(dec),
         'actual_slope_min':min(slopes) if slopes else None,'actual_slope_max':max(slopes) if slopes else None,
         'escaped_relative_nonrepresentation_min_of_lane_maxima':min(rel) if rel else None,
         'base_absolute_nonrepresentation_min_of_lane_maxima':min(baseabs) if baseabs else None,
         'nondecay_points':nd,'inconclusive_points':inc,
         'scope':'Iter487 exact Iter486 Haar escape science object with scale-normalized validation; no full Haar/spectral/physical-vertex theorem'}
    os.makedirs(os.path.dirname(args.out) or '.',exist_ok=True)
    with open(args.out,'w') as f: json.dump(out,f,indent=2,sort_keys=True)
    print(json.dumps(out,indent=2,sort_keys=True))
    raise SystemExit(3 if cls=='INFRASTRUCTURE_OR_SOURCE_FAIL_ITER487' else 0)

if __name__=='__main__': main()

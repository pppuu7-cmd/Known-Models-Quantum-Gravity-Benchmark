#!/usr/bin/env python3
import argparse, glob, json, os

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--root',required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    rows=[]
    for p in glob.glob(os.path.join(a.root,'**','*.json'),recursive=True):
        with open(p) as f: rows.append(json.load(f))
    keys={r.get('geometry_key') for r in rows}; expected={'C-s2','C-s3'}
    passed=(keys==expected and len(rows)==2 and all(bool(r.get('pass')) for r in rows))
    lanes=sorted({x for r in rows for x in r.get('revalidates_lanes',[])})
    out={'iteration':489,'expected_geometries':2,'present_geometries':len(keys),'revalidated_lanes':lanes,'pass':passed,
         'classification':'ITER489_FIVE_ITER487_LANES_KAK_REVALIDATED_SCOPED' if passed else 'NUMERICAL_OR_SOURCE_FAIL_ITER489_KAK_REVALIDATION',
         'promoted_iter487_classification':'SCIENTIFIC_FAIL_ITER487_HAAR_ESCAPE_ACTUAL_ENVELOPE_REVALIDATED_BY_ITER489' if passed else None,
         'geometry_results':rows,
         'scope':'validation-only composite decision; original Iter487 96 slope states remain unchanged'}
    os.makedirs(os.path.dirname(a.out) or '.',exist_ok=True)
    with open(a.out,'w') as f: json.dump(out,f,indent=2,sort_keys=True)
    print(json.dumps(out,indent=2,sort_keys=True)); raise SystemExit(0)
if __name__=='__main__': main()

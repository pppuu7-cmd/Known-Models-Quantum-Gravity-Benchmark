#!/usr/bin/env python3
import argparse, glob, json, os

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--root',required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    rows=[]
    for p in glob.glob(os.path.join(a.root,'**','*.json'),recursive=True):
        with open(p) as f: rows.append(json.load(f))
    keys={r.get('geometry_key') for r in rows}
    expected={'C-s2','C-s3'}
    complete=(keys==expected and len(rows)==2)
    passed=complete and all(bool(r.get('pass')) for r in rows)
    lanes=sorted({x for r in rows for x in r.get('revalidates_lanes',[])})
    out={'iteration':488,'expected_geometries':2,'present_geometries':len(keys),'revalidated_lanes':lanes,
         'pass':passed,'classification':'ITER488_FIVE_LANES_KAK_HIGH_PRECISION_REVALIDATED_SCOPED' if passed else 'NUMERICAL_OR_SOURCE_FAIL_ITER488_KAK_REVALIDATION',
         'geometry_results':rows,
         'scope':'validation-only numerical recheck; Iter487 raw slope states are not recomputed or modified'}
    os.makedirs(os.path.dirname(a.out) or '.',exist_ok=True)
    with open(a.out,'w') as f: json.dump(out,f,indent=2,sort_keys=True)
    print(json.dumps(out,indent=2,sort_keys=True))
    raise SystemExit(0)
if __name__=='__main__': main()

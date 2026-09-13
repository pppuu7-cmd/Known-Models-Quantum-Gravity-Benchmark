#!/usr/bin/env python3
import glob, json, os, pathlib

EXPECTED={f'{p}-{r}' for p in 'ABCD' for r in ('mild','strong')}
PASS='ITER484_SOURCE_TOLLER_KAK_ONE_EDGE_RECONSTRUCTION_QUALIFIED_SCOPED'
FAIL='SCIENTIFIC_FAIL_ITER484_SOURCE_TOLLER_KAK_ONE_EDGE'
BLOCK='BLOCKED_OR_INFRASTRUCTURE_ITER484'

records=[]
for fn in sorted(glob.glob('artifacts/iter484-*.json')):
    if fn.endswith('summary.json'):
        continue
    try:
        x=json.load(open(fn))
        x['_file']=fn
        records.append(x)
    except Exception as e:
        records.append({'lane':pathlib.Path(fn).stem.replace('iter484-',''),'valid':False,'pass':False,'classification':BLOCK,'_file':fn,'_parse_error':repr(e)})

by_lane={r.get('lane'):r for r in records if r.get('lane') in EXPECTED}
missing=sorted(EXPECTED-set(by_lane))
extra=sorted(set(r.get('lane') for r in records if r.get('lane'))-EXPECTED)
valid_count=sum(bool(by_lane[k].get('valid')) for k in by_lane)
pass_count=sum(bool(by_lane[k].get('pass')) for k in by_lane)
scientific_fail_lanes=sorted(k for k,v in by_lane.items() if v.get('valid') and not v.get('pass'))
invalid_lanes=sorted(k for k,v in by_lane.items() if not v.get('valid'))

if missing or invalid_lanes or len(by_lane)!=8:
    cls=BLOCK
    ok=False
elif scientific_fail_lanes:
    cls=FAIL
    ok=False
elif pass_count==8:
    cls=PASS
    ok=True
else:
    cls=BLOCK
    ok=False

summary={
  'iteration':484,
  'expected_lanes':sorted(EXPECTED),
  'lane_count':len(by_lane),
  'valid_count':valid_count,
  'pass_count':pass_count,
  'missing_lanes':missing,
  'extra_lanes':extra,
  'scientific_fail_lanes':scientific_fail_lanes,
  'invalid_lanes':invalid_lanes,
  'scientific_pass':ok,
  'classification':cls,
  'lane_metrics':{k:{
      'classification':v.get('classification'),
      'valid':v.get('valid'),
      'pass':v.get('pass'),
      'beta':v.get('beta'),
      'cartan_reconstruction_residual':v.get('cartan_reconstruction_residual'),
      'polar_rapidity_residual':v.get('polar_rapidity_residual'),
      'full_additive_residual':v.get('full_additive_residual'),
      'axial_gauge_residual':v.get('axial_gauge_residual'),
      'reduced_conjugation_relative_residual':v.get('reduced_conjugation_relative_residual'),
      'inverse_reconstruction_residual':v.get('inverse_reconstruction_residual'),
      'inverse_toller_kak_residual':v.get('inverse_toller_kak_residual'),
      'naive_polar_reconstruction_error':v.get('naive_polar_reconstruction_error'),
      'nonrepresentation_max':v.get('nonrepresentation_max'),
      'tests':v.get('tests'),
    } for k,v in sorted(by_lane.items())},
  'scope':'aggregate of the 8 prospectively frozen Iter484 one-edge lanes only; no ten-edge/Haar/D7-S2 closure'
}
os.makedirs('artifacts',exist_ok=True)
with open('artifacts/iter484-summary.json','w') as f:
    json.dump(summary,f,indent=2,sort_keys=True)
print(json.dumps(summary,indent=2,sort_keys=True))
# Always exit zero: classification is scientific payload, not CI plumbing.

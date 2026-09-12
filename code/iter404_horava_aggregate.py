#!/usr/bin/env python3
from __future__ import annotations
import glob, json
from pathlib import Path

rows=[]
for fn in sorted(glob.glob('iter404-results/**/*.json',recursive=True)):
    rows.append(json.loads(Path(fn).read_text()))
lanes={r['lane']:r for r in rows if 'lane' in r}
expected={'projectable_dictionary','projectable_trajectory','projectable_observable','nonprojectable_3p1'}
complete=set(lanes)==expected
all_blocked=complete and all((not r['pass']) and (not r['scientific_fail']) and (not r['terminal']) for r in lanes.values())
out={
  'iteration':404,
  'family':'HORAVA_LIFSHITZ',
  'lane_count':len(lanes),
  'expected_lane_count':4,
  'complete':complete,
  'all_missing_objects_classified_as_blocked_not_fail':all_blocked,
  'family_terminal':False,
  'coverage_status_after':'PARTIAL_SUBFAMILY_ONLY',
  'classification':'PASS_HORAVA_FRONTIER_DISCRIMINATOR__FOUR_BLOCKERS_LOCALIZED__NO_FALSE_TERMINAL_PROMOTION' if all_blocked else 'INCOMPLETE_OR_CONTRACT_VIOLATION',
  'next_permitted_objects':[
    'same-realization projectable UV/IR parameter-and-scale stitching map with relevant couplings',
    'projectable normalized extra-mode/tensor observable plus same-domain GR comparator and errors',
    'independent non-projectable 3+1 quantum closure/disposition authority'
  ],
  'D2':'NOT_CLOSED_COVERAGE_AND_OBJECTS',
  'D4':'PARTIAL_GLOBAL_NOT_CLOSED',
  'D7':'NOT_CLOSED_NOT_YET_AUTHORIZED',
  'candidate_gravity_activation':False,
  'lanes':lanes
}
Path('iter404-summary.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,sort_keys=True))
if not all_blocked: raise SystemExit(2)

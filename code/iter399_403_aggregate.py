#!/usr/bin/env python3
import json
from pathlib import Path
root=Path('iter399-403-results')
objs=[]
for p in root.rglob('*.json'):
    try: objs.append(json.loads(p.read_text()))
    except Exception: pass
bm=[o for o in objs if o.get('mode')=='branch_map_v2']
fam=[o for o in objs if o.get('mode')=='source_family']
expected={'HORAVA_LIFSHITZ','CDT_EDT','GFT_TENSOR_MODELS','STRING_MTHEORY_HOLOGRAPHY'}
coverage=(len(bm)==1 and len(fam)==4 and {o['family'] for o in fam}==expected)
all_pass=coverage and all(o.get('pass') for o in bm+fam)
route_priority={
 'HORAVA_LIFSHITZ':1,
 'GFT_TENSOR_MODELS':2,
 'CDT_EDT':3,
 'STRING_MTHEORY_HOLOGRAPHY':4
}
frontier=sorted([{'family':o['family'],'next_route':o['next_route'],'priority':route_priority[o['family']]} for o in fam],key=lambda x:x['priority'])
out={
 'iteration_bundle':'399-403','coverage_complete':coverage,'all_jobs_pass':all_pass,
 'branch_map_jobs':len(bm),'source_family_jobs':len(fam),
 'higher_derivative_branch_map_v2_valid':bool(bm and bm[0].get('pass')),
 'families_reaudited':sorted([o['family'] for o in fam]),
 'new_terminal_families':sorted([o['family'] for o in fam if o.get('terminal_after') and not o.get('terminal_before')]),
 'terminal_denominator_change':0,
 'next_frontier_order':frontier,
 'D2':'NOT_CLOSED_COVERAGE_AND_OBJECTS','D4':'PARTIAL_GLOBAL_NOT_CLOSED','D7':'NOT_CLOSED_NOT_YET_AUTHORIZED',
 'candidate_gravity_activation':False,
 'classification':'PASS_PARALLEL_SOURCE_CLOSURE_WAVE__HIGHER_DERIVATIVE_BRANCH_CENSUS_REPAIRED__FOUR_ADDITIONAL_TIER1_BLOCKERS_REAUDITED__NO_FALSE_TERMINAL_PROMOTION' if all_pass else 'INCOMPLETE_OR_FAILED_PARALLEL_SOURCE_CLOSURE_WAVE',
 'scientific_boundary':'No new terminal family is inferred from source progress alone. Hořava remains split projectable/non-projectable; CDT remains data/continuum-capsule limited; GFT retains independent TGFT remainder; string/M-theory retains compactification/subfamily exhaustion freedom.'
}
Path('iter399-403-summary.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,sort_keys=True))
if not all_pass: raise SystemExit(2)

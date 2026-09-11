#!/usr/bin/env python3
import json
from pathlib import Path

files = sorted(Path('iter334-337-results').rglob('*.json'))
rows = [json.loads(p.read_text()) for p in files]
by_lane = {r['lane']: r for r in rows}
required = {
 'LQG_MULTISCALE_AND_LOCAL_NORMALIZATION_AUTHORITY',
 'ASYMPTOTIC_SAFETY_CONTACT_COMPLETE_AUTHORITY',
 'CFS_NORMALIZED_CORRECTION_COMPARATOR_AUTHORITY',
 'GLOBAL_D7_TERMINAL_COVERAGE_GUARD',
}
assert set(by_lane) == required, (set(by_lane), required)
assert by_lane['LQG_MULTISCALE_AND_LOCAL_NORMALIZATION_AUTHORITY']['classification'].startswith('BLOCKED_')
assert by_lane['ASYMPTOTIC_SAFETY_CONTACT_COMPLETE_AUTHORITY']['classification'].startswith('BLOCKED_')
assert by_lane['CFS_NORMALIZED_CORRECTION_COMPARATOR_AUTHORITY']['classification'].startswith('BLOCKED_')
g = by_lane['GLOBAL_D7_TERMINAL_COVERAGE_GUARD']
assert g['strict_terminal_rows'] == 1 and g['tier1_total'] == 15
assert g['authorized_outcome'] == 'NOT_AUTHORIZED'
summary = {
 'iteration_bundle': '334-337',
 'parallel_lanes': 4,
 'lane_classifications': {k:v['classification'] for k,v in sorted(by_lane.items())},
 'cw2_terminal_promotions_authorized': 0,
 'global_status_change_authorized': False,
 'd7_output': 'NOT_AUTHORIZED',
 'scientific_interpretation': 'Three high-value CW2 fronts remain blocked by distinct missing source-defined objects; the global D7 lock remains valid. These blockers are not family FAIL evidence.',
 'next_high_information_actions': [
   'LQG: new published source-defined forest/Haar jet normalization or same-realization EPRL-to-area-metric/RG bridge',
   'AS: stable public same-realization contact-complete s+t+u+A4 package with error/comparator certificate',
   'CFS: explicit normalized beyond-GR gravity correction tensor/coefficient vector plus comparator',
   'GLOBAL: terminalize additional Tier-1 rows only with family-scope evidence/reduction maps; do not infer NEW_REQUIRED from BLOCKED rows'
 ]
}
Path('iter334-337-summary.json').write_text(json.dumps(summary, indent=2, sort_keys=True)+'\n')
print(json.dumps(summary, sort_keys=True))

#!/usr/bin/env python3
import json
from pathlib import Path

root=Path('build/lqg-iter326-results')
files=sorted(root.glob('orbit_*.json'))
if len(files)!=12:
    raise SystemExit(f'expected 12 orbit artifacts, got {len(files)}')
rows=[json.loads(p.read_text()) for p in files]
assert sorted(r['orbit_index'] for r in rows)==list(range(12))
forest=[r for r in rows if r['case_kind']=='forest']
overlap=[r for r in rows if r['case_kind']=='overlap']
assert len(forest)==8 and len(overlap)==4
assert sum(r['orbit_size'] for r in forest)==72
assert sum(r['orbit_size'] for r in overlap)==85
assert sum(1 for r in rows if not r['requires_distributional_extension'])==1
nonempty=[r for r in rows if r['requires_distributional_extension']]
assert len(nonempty)==11
assert all(r['audited_source_joint_ten_wedge_forest_extension_status']=='NOT_FOUND_IN_AUDITED_SOURCE' for r in rows)
assert all(all(s['bf_extension_nonunique_without_extra_normalization'] for s in r['strata']) for r in nonempty)
assert all(all(s['finite_source_spectral_epsilon_softens_leading_beta_pole'] is False for s in r['strata']) for r in nonempty)
max_cancel=max(r['max_projector_denominator_cancellation_error'] for r in rows)
assert max_cancel < 1e-11

summary={
    'iteration':326,
    'raw_compatible_forests':72,
    'forest_S5_orbits':8,
    'raw_overlapping_incomparable_pairs':85,
    'overlap_S5_orbits':4,
    'total_inequivalent_cases':12,
    'nonempty_orbits_requiring_extension':11,
    'finite_source_spectral_epsilon_closes_any_nonempty_orbit':False,
    'audited_source_joint_ten_wedge_forest_extension_status':'NOT_FOUND_IN_AUDITED_SOURCE',
    'max_projector_denominator_cancellation_error':max_cancel,
    'classification':'Across the complete S5 quotient of compatible forests and overlapping incomparable partial diagonals, every non-empty case contains non-safe strata with epsilon-independent leading residues and nonunique scaling-degree extensions. The audited source formulas define individual spectral i-epsilon branches but do not document a unique joint ten-wedge forest-compatible extension/normalization.',
    'implication':'For KMQGB resource closure, causal spinfoam now needs an explicit source-defined joint distributional/renormalized prescription with forest/overlap consistency; individual branch i-epsilon is insufficient by itself.',
    'scope_guard':'This is a complete orbit-level closure/provenance audit of the identified K3/K4/K5 singular strata, not a proof that no joint extension can be constructed, not a terminal family FAIL, and not D7/NEW_REQUIRED authorization.'
}
out=Path('build/lqg-iter326-summary.json')
out.write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n')
print(json.dumps(summary,sort_keys=True))

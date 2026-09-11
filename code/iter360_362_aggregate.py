#!/usr/bin/env python3
import json,pathlib
root=pathlib.Path('iter360-362-results')
docs=[json.load(open(p)) for p in root.rglob('*.json')]
cross=[d for d in docs if d.get('iteration')==360]
thr=[d for d in docs if d.get('iteration')==361]
scope=[d for d in docs if d.get('iteration')==362]
assert len(cross)==6, len(cross)
assert len(thr)==2, len(thr)
assert len(scope)==1, len(scope)
assert all(d['n_cubed_penalty_eventually_beats_n_squared_entropy'] for d in cross)
assert all(d['rows'][-1]['net_upper_log2_exponent'] < 0 for d in cross)
d4=next(d for d in thr if d['mode']=='d4')
all_d=next(d for d in thr if d['mode']=='all_d')
assert any(r['ell_over_ell_p']==1.14 and r['suppression_certified_by_quoted_threshold'] for r in d4['rows'])
assert any(r['ell_over_ell_p']==2.34 and r['suppression_certified_by_quoted_threshold'] for r in all_d['rows'])
max_cross=max(d['crossover_n_beta_over_A'] for d in cross)
out={
 'iteration_bundle':'360-362',
 'classification':'PASS_SCOPED_CAUSAL_SET_ENTROPIC_LAYERED_SECTOR_SUPPRESSION__SOURCE_ASYMPTOTIC_N_CUBED_NONLINK_PENALTY_BEATS_N_SQUARED_LAYERED_ENTROPY_AND_QUOTED_BDG_THRESHOLD_CERTIFIES_STRONG_PATHSUM_SUPPRESSION__FULL_DYNAMICS_TO_EMERGENT_MANIFOLD_AND_NORMALIZED_GRAVITY_OBSERVABLE_REMAINS_OPEN',
 'all_crossover_stress_passed':True,
 'largest_stressed_crossover_n':max_cross,
 'd4_fail_closed_certified_side':'ell/ell_p > 1.136 using quoted approximate threshold',
 'all_d_fail_closed_certified_side':'ell/ell_p > 2.33 using quoted upper bound',
 'source_layered_sector_result':'typical K-layered sets with K << n reduce to link-action leading order and are strongly suppressed above threshold',
 'remaining_open_sector':scope[0]['remaining_open_sector'],
 'family_status':'PARTIAL_SUBFAMILY_ONLY',
 'family_terminal':False,
 'd7_promotion_authorized':False,
 'refined_blocker':'CAUSAL_SET_NONLAYERED_AND_SPARSE_SECTOR_CONTROL_PLUS_SOURCE_DEFINED_FUNDAMENTAL_MEASURE_TO_EMERGENT_MANIFOLD_AND_DIMENSION_SELECTION_PLUS_NORMALIZED_GENUINELY_CAUSAL_SET_GRAVITATIONAL_OBSERVABLE_AND_SAME_DOMAIN_COMPARATOR_ERROR_LEDGER',
 'scope_guard':scope[0]['scope_guard']
}
with open('iter360-362-summary.json','w') as f: json.dump(out,f,indent=2,sort_keys=True)
print(json.dumps(out,sort_keys=True))

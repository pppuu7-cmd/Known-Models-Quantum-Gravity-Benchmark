#!/usr/bin/env python3
import json,pathlib
root=pathlib.Path('iter363-365-results')
docs=[json.load(open(p)) for p in root.rglob('*.json')]
th=[d for d in docs if d.get('iteration')==363]
ct=[d for d in docs if d.get('iteration')==364]
sg=[d for d in docs if d.get('iteration')==365]
assert len(th)==6, len(th)
assert len(ct)==5, len(ct)
assert len(sg)==1, len(sg)
assert all(any(r['p0_over_ReM']==0.0 and r['complex_delta_inactive_by_source_window'] for r in d['rows']) for d in th)
assert all(any(r['p0_over_ReM']==2.0 and not r['complex_delta_inactive_by_source_window'] for r in d['rows']) for d in th)
assert all(d['sign_change_at_x_half'] and d['contour_residue_sensitivity_present'] for d in ct)
out={
 'iteration_bundle':'363-365',
 'classification':'PASS_SCOPED_LEE_COMPLEX_GHOST_BOUND_STATE_THRESHOLD_AND_CONTOUR_SENSITIVITY__SOURCE_STATIONARY_WINDOW_IS_EXACTLY_SET_BY_2_RE_M_AND_COMPLEX_MASS_WICK_ROTATION_REQUIRES_CONTOUR_RESIDUES__POSITIVE_NORM_BOUND_STATE_DOES_NOT_ESTABLISH_PERMANENT_GHOST_CONFINEMENT_AND_UNITARITY_AUTHORITY_CONFLICT_REMAINS_BLOCKED',
 'threshold_cases_passed':len(th),
 'contour_cases_passed':len(ct),
 'positive_pair_norm':sg[0]['pair_state_norm_from_source_eq_4_25'],
 'permanent_confinement_established':False,
 'same_realization_unitarity_conflict_resolved':False,
 'branch_status':sg[0]['branch_status'],
 'family_status':'PARTIAL_SUBFAMILY_ONLY',
 'family_terminal':False,
 'd7_promotion_authorized':False,
 'refined_blocker':'LEE_WICK_FIXED_PRESCRIPTION_SAME_REALIZATION_PHYSICAL_UNITARITY_CUT_CERTIFICATE_PLUS_PERMANENT_GHOST_CONFINEMENT_OR_OTHER_PHYSICAL_ASYMPTOTIC_STATE_RULE_PLUS_NORMALIZED_GRAVITY_OBSERVABLE_COMPARATOR_AND_ERROR_LEDGER',
 'scope_guard':sg[0]['scope_guard']
}
with open('iter363-365-summary.json','w') as f: json.dump(out,f,indent=2,sort_keys=True)
print(json.dumps(out,sort_keys=True))

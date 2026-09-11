#!/usr/bin/env python3
import json,pathlib
root=pathlib.Path('iter366-369-results')
docs=[json.load(open(p)) for p in root.rglob('*.json')]
pos=[d for d in docs if d.get('iteration')==366 and d.get('branch')=='IHO_DQFT_SPACELIKE_PV']
neg=[d for d in docs if d.get('iteration')==366 and d.get('branch')=='FEYNMAN_TIMELIKE_CONTROL']
lan=[d for d in docs if d.get('iteration')==367]
uv=[d for d in docs if d.get('iteration')==368]
sg=[d for d in docs if d.get('iteration')==369]
assert len(pos)==6, len(pos)
assert len(neg)==3, len(neg)
assert len(lan)==5, len(lan)
assert len(uv)==6, len(uv)
assert len(sg)==1, len(sg)
assert all(d['pole_class']=='SPACELIKE' and not d['pole_inside_KL_physical_support'] and d['source_rho_zero_condition_supported'] for d in pos)
assert all(d['pole_class']=='TIMELIKE' and d['pole_inside_KL_physical_support'] for d in neg)
assert all(d['two_dIHO_branch_point_class']=='SPACELIKE' and not d['mixed_has_real_nonnegative_feynman_ratio'] and not d['physical_timelike_samples_hit_branch_point'] for d in lan)
assert all(d['monotone_convergence_to_minus_one'] for d in uv)
worst=max(d['worst_highest_scale_error'] for d in uv)
out={
 'iteration_bundle':'366-369',
 'classification':'PASS_SCOPED_IHO_DQFT_SPECTRAL_SUPPORT_LANDAU_AND_UV_LOCALITY__BETA_POSITIVE_SPIN2_POLE_IS_SPACELIKE_AND_OUTSIDE_KL_SUPPORT_WHILE_BETA_NEGATIVE_CONTROL_IS_TIMELIKE_AND_INSIDE_SUPPORT__STATED_PHYSICAL_TIMELIKE_LANDAU_PINCH_ABSENT_AND_FULL_SPIN2_KERNEL_RETAINS_1_OVER_K4_FALLOFF__BRANCH_NORMALIZED_GRAVITY_OBSERVABLE_COMPARATOR_STILL_REQUIRED',
 'positive_beta_spectral_cases':len(pos),
 'negative_beta_timelike_controls':len(neg),
 'landau_ratio_cases':len(lan),
 'uv_cases':len(uv),
 'worst_uv_scaled_error_at_k2_over_mu2_1e8':worst,
 'source_all_loop_unitarity_axis':sg[0]['source_defined_unitarity_axis'],
 'source_all_loop_unitarity_theorem_reproved_here':False,
 'branch_status':sg[0]['branch_status'],
 'branch_materially_distinct':True,
 'family_status':'PARTIAL_SUBFAMILY_ONLY',
 'family_terminal':False,
 'd7_promotion_authorized':False,
 'branch_refined_blocker':'IHO_DQFT_NORMALIZED_GRAVITATIONAL_OBSERVABLE_PLUS_SAME_DOMAIN_GR_EFT_COMPARATOR_AND_PROPAGATED_ERROR_LEDGER_PLUS_NON_MINKOWSKI_OR_STATED_DOMAIN_SCOPE_CERTIFICATE',
 'family_refined_blocker':'HIGHER_DERIVATIVE_MATERIAL_QUANTIZATION_BRANCH_TERMINAL_DISPOSITION_PLUS_SAME_REALIZATION_CAUSALITY_OBSERVABLE_COMPARATOR_CERTIFICATE',
 'scope_guard':sg[0]['scope_guard']
}
with open('iter366-369-summary.json','w') as f: json.dump(out,f,indent=2,sort_keys=True)
print(json.dumps(out,sort_keys=True))

#!/usr/bin/env python3
import json
out={
 'iteration':369,
 'branch_id':'IHO_DQFT_SPACELIKE_PV',
 'materially_distinct_from':['FAKEON_AVERAGE_CONTINUATION','LEE_WICK_UNSTABLE_RESONANCE','PT_SYMMETRIC_MODIFIED_INNER_PRODUCT','EUCLIDEAN_OS_RECONSTRUCTION'],
 'source_defined_unitarity_axis':'SOURCE_CLAIMS_ALL_LOOP_OPTICAL_THEOREM_WITH_WIGHTMAN_KL_ZERO_SPECTRAL_WEIGHT_AND_PV_DQFT_REALIZATION',
 'source_defined_locality_uv_axis':'SOURCE_RETAINS_STELLE_1_OVER_K4_SPIN2_FALLOFF',
 'kinematic_certificates_recomputed':['SPACELIKE_POLE_OUTSIDE_KL_SUPPORT','NO_PHYSICAL_TIMELIKE_LANDAU_PINCH_IN_STATED_CHANNELS','1_OVER_K4_UV_FALLOFF'],
 'source_all_loop_unitarity_theorem_reproved_here':False,
 'normalized_gravitational_observable_present_in_this_gate':False,
 'same_domain_GR_EFT_comparator_present_in_this_gate':False,
 'propagated_error_ledger_present_in_this_gate':False,
 'non_Minkowski_scope_terminalized':False,
 'branch_status':'PASS_SCOPED_SOURCE_DEFINED_UNITARITY_AND_LOCALITY_CERTIFICATE__KMQGB_OBSERVABLE_COMPARATOR_CLOSURE_OPEN',
 'family_status':'PARTIAL_SUBFAMILY_ONLY',
 'family_terminal':False,
 'd7_promotion_authorized':False,
 'scope_guard':['NO_SOURCE_THEOREM_TO_NUMERICAL_REPROOF_CLAIM','NO_KINEMATIC_CERTIFICATE_TO_FULL_OBSERVABLE_CLOSURE','NO_NEW_BRANCH_TO_PARENT_TERMINALIZATION','NO_MINKOWSKI_TO_ALL_BACKGROUND_PROMOTION','NO_D7_PROMOTION']
}
with open('iter369-iho-dqft-scope.json','w') as f: json.dump(out,f,indent=2,sort_keys=True)
print(json.dumps(out,sort_keys=True))

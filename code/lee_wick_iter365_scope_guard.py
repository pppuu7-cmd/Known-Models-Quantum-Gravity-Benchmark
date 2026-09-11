#!/usr/bin/env python3
import json
out={
 'iteration':365,
 'pair_state_norm_from_source_eq_4_25':1.0,
 'positive_norm_bound_state_possible_below_threshold':True,
 'permanent_confinement_established':False,
 'massive_ghost_problem_resolved':False,
 'same_realization_unitarity_conflict_resolved':False,
 'prescription_independence_established':False,
 'branch_status':'BLOCKED_CONTESTED_UNITARITY_AUTHORITY__SAME_REALIZATION_CUT_AND_PRESCRIPTION_CERTIFICATE_REQUIRED',
 'family_status':'PARTIAL_SUBFAMILY_ONLY',
 'family_terminal':False,
 'd7_promotion_authorized':False,
 'scope_guard':['NO_BOUND_STATE_POSITIVITY_TO_PERMANENT_CONFINEMENT','NO_THRESHOLD_TO_GLOBAL_UNITARITY','NO_CROSS_PRESCRIPTION_MERGE','NO_CONTESTED_AUTHORITY_TO_FAIL','NO_PARENT_TERMINALIZATION','NO_D7_PROMOTION']
}
with open('iter365-lee-wick-scope.json','w') as f: json.dump(out,f,indent=2,sort_keys=True)
print(json.dumps(out,sort_keys=True))

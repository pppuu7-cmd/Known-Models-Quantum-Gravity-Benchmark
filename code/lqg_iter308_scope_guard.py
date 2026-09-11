#!/usr/bin/env python3
import json, pathlib

p=json.load(open('benchmarks/lqg_iter308_causal_support_pole_cancellation.json'))
c=p['prospectively_frozen_claims']
ok=(c['leading_branch_factor_each_causal_sector']==1 and
    c['unit_weight_causal_sum_leading_factor']==16 and
    (not c['positive_weight_causal_sum_can_cancel_common_nonzero_leading_term']) and
    c['unrestricted_unit_weight_leading_factor_sum']==0 and
    (not c['causal_support_restores_eprl_local_pole_cancellation']) and
    (not c['distributional_or_regularized_causal_sum_nonexistence_proven']) and
    (not c['family_terminal']) and (not c['d7_authorized']))
out={'probe':'scope_guard','pass':bool(ok),'iteration':308,
     'proven_scope':'unit-weight and any nontrivial nonnegative sigma-induced causal-sector sum preserves the Iter307 leading local pole',
     'contrast':'unrestricted 1024-sector wedge-sign sum cancels the leading branch-sign factor',
     'not_proven':['no signed/complex causal weighting can cancel','no distributional/regularized prescription exists','family no-go','D7 authorization'],
     'next_required_object':'source-grounded signed/complex weighting or local distributional/renormalized prescription compatible with causal interpretation, gluing and normalization; absent that, the causal sum retains the absolute-integrability obstruction'}
pathlib.Path('build/lqg-iter308').mkdir(parents=True,exist_ok=True)
pathlib.Path('build/lqg-iter308/scope_guard.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if not ok: raise SystemExit(1)

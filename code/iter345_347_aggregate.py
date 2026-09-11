#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

root=Path('iter345-347-results')
des=[json.loads(p.read_text()) for p in root.rglob('desitter-*.json')]
flat=[json.loads(p.read_text()) for p in root.rglob('flat-*.json')]
guards=[json.loads(p.read_text()) for p in root.rglob('iter347-rqcp-saturation-guard.json')]
assert len(des)==4,len(des)
assert sorted(round(x['m_chi_over_H'],6) for x in des)==[0.6,1.0,2.0,4.0]
assert len(flat)==5,len(flat)
assert sorted(round(x['omega'],6) for x in flat)==[0.5,1.0,2.0,5.0,10.0]
assert len(guards)==1,len(guards)
assert all(x['minimum_future_support_abs']>1e-8 for x in des)
assert all(x['maximum_imaginary_fraction']<1e-40 for x in des)
assert all(x['minimum_fakeon_future_abs']>1e-8 for x in flat)
assert all(x['maximum_average_identity_residual']<1e-15 for x in flat)
assert 'SATURATED' in guards[0]['classification']
summary={
 'iteration_bundle':'345-347',
 'fakeon_desitter_mass_ratios':sorted(x['m_chi_over_H'] for x in des),
 'fakeon_desitter_total_probes':sum(x['probe_count'] for x in des),
 'fakeon_desitter_global_minimum_future_support_abs':min(x['minimum_future_support_abs'] for x in des),
 'flat_control_omegas':sorted(x['omega'] for x in flat),
 'flat_control_total_probes':sum(x['probe_count'] for x in flat),
 'rqcp_cutoff_only_compute_saturated':True,
 'classification':'PASS_SCOPED_FAKEON_RESPONSE_LEVEL_CONTROLLED_NONLOCALITY_CERTIFICATE__DESITTER_SOURCE_KERNEL_AND_INDEPENDENT_FLAT_AVERAGE_CONTROL_SHOW_NONZERO_FUTURE_SUPPORT__RQCP_DUPLICATE_CUTOFF_COMPUTE_GUARDED',
 'higher_derivative_family_status':'PARTIAL_SUBFAMILY_ONLY',
 'fakeon_branch_terminal':False,
 'd7_promotion_authorized':False,
 'next_fakeon_gate':'NORMALIZED_PHYSICAL_GRAVITY_OBSERVABLE_USING_THE_SAME_FAKEON_RESPONSE_PRESCRIPTION_PLUS_IDENTICAL_DOMAIN_GR_OR_HIGHER_DERIVATIVE_COMPARATOR_AND_ERROR_LEDGER',
 'scope_guard':[
   'RESPONSE_LEVEL_CERTIFICATE_DOES_NOT_EQUAL_FULL_PHYSICAL_OBSERVABLE_PACKAGE',
   'FAKEON_CONTROLLED_NONLOCALITY_IS_SOURCE_DEFINED_NOT_COUNTED_AS FAMILY_FAIL',
   'OTHER_FOUR_HIGHER_DERIVATIVE_QUANTIZATION_BRANCHES_REMAIN_UNRESOLVED',
   'RQCP_GUARD_IS_PROCESS_ONLY',
   'NO_PARENT_FAMILY_TERMINALIZATION','NO_D7_PROMOTION'
 ]
}
Path('iter345-347-summary.json').write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n')
print(json.dumps(summary,sort_keys=True))

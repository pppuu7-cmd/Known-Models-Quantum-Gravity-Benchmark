#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
root=Path('iter349-352-results')
ir=[json.loads(p.read_text()) for p in root.rglob('ir-*.json')]
uv=[json.loads(p.read_text()) for p in root.rglob('uv-*.json')]
tr=[json.loads(p.read_text()) for p in root.rglob('iter351-horava-transport-guard.json')]
np=[json.loads(p.read_text()) for p in root.rglob('iter352-horava-nonprojectable-scope-guard.json')]
assert len(ir)==6,len(ir); assert len(uv)==6,len(uv); assert len(tr)==1,len(tr); assert len(np)==1,len(np)
assert all(x['case_count']==105 for x in ir)
assert all('UNAVOIDABLE_NEGATIVE_LOW_K_WINDOW' in x['classification'] for x in ir)
assert all(x['worst_scaled_error_at_lambda_1e6']<2e-6 for x in uv)
assert 'BLOCKED_SCOPED' in tr[0]['classification']; assert np[0]['three_plus_one_terminal_certificate'] is False
summary={'iteration_bundle':'349-352','ir_lambda_values':sorted(x['lambda'] for x in ir),'ir_total_stress_cases':sum(x['case_count'] for x in ir),'ir_all_low_k_sign_certificates_passed':True,'uv_amplitude_coupling_cases':sorted(x['case'] for x in uv),'uv_d9_all_finite_lambda_infinity_limit_checks_passed':True,'uv_worst_scaled_error_at_lambda_1e6':max(x['worst_scaled_error_at_lambda_1e6'] for x in uv),'projectable_uv_to_ir_transport_status':'BLOCKED_MISSING_SOURCE_DEFINED_RELEVANT_SECTOR_AND_TIME_DEPENDENT_IR_RESOLUTION_TRANSPORT','nonprojectable_3p1_terminal_certificate':False,'classification':'PASS_SCOPED_HORAVA_PROJECTABLE_UV_REGULARITY_PLUS_IR_OBSTRUCTION_CROSS_AUDIT__PUBLISHED_UV_SCATTERING_LIMIT_IS_REGULAR_WHILE_PROJECTABLE_NEAR_GR_IR_SCALAR_DISPERSION_HAS_UNAVOIDABLE_LOW_K_INSTABILITY_AND_2026_STATIC_ENDPOINT_ROUTE_IS_NOT_AVAILABLE__FULL_UV_TO_IR_TRANSPORT_REMAINS_BLOCKED','family_status':'PARTIAL_SUBFAMILY_ONLY','family_terminal':False,'d7_promotion_authorized':False,'refined_blocker':'HORAVA_PROJECTABLE_TIME_DEPENDENT_IR_STABILITY_RESOLUTION_PLUS_SOURCE_DEFINED_RELEVANT_COUPLING_UV_TO_IR_TRANSPORT_AND_NORMALIZED_PHYSICAL_OBSERVABLE_COMPARATOR_CERTIFICATE_PLUS_NONPROJECTABLE_3P1_TERMINAL_DISPOSITION','scope_guard':['IR_OBSTRUCTION_IS_PROJECTABLE_FLAT_BACKGROUND_LINEAR_SCALAR_SECTOR','UV_AMPLITUDE_IS_TREE_LEVEL_HEADON_SCOPED_CONTROL','NO_BLOCKED_TO_FAIL_CONVERSION','NONPROJECTABLE_NOT_SUBSTITUTED_FOR_PROJECTABLE','NO_PARENT_FAMILY_TERMINALIZATION','NO_D7_PROMOTION']}
Path('iter349-352-summary.json').write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n'); print(json.dumps(summary,sort_keys=True))

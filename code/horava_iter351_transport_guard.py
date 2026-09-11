#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

a=json.loads(Path('paper_iv/HORAVA_SOURCE_AUTHORITY_ITER349_352.json').read_text())
f=a['frozen_interpretation']
assert a['family']=='HORAVA_LIFSHITZ_GRAVITY'
assert f['projectable_same_family_identity'] is True
assert f['full_source_defined_uv_to_ir_same_realization_transport'] is False
assert f['family_terminalization_authorized'] is False
rg=' '.join(a['projectable_rg_authority']['facts']).lower(); ir=' '.join(a['projectable_ir_2026_authority']['facts']).lower(); sc=' '.join(a['projectable_scattering_authority']['facts']).lower()
assert 'marginal' in rg and 'relevant' in rg and 'instability' in rg
assert 'time-dependent' in ir and 'no static' in ir
assert 'finite at lambda->infinity' in sc and 'low-energy' in sc
out={'iteration':351,'classification':'BLOCKED_SCOPED_PROJECTABLE_HORAVA_UV_TO_IR_SAME_REALIZATION_TRANSPORT__UV_MARGINAL_RG_AND_LAMBDA_INFINITY_SCATTERING_EXIST_BUT_RELEVANT_IR_COEFFICIENTS_AND_TIME_DEPENDENT_STABILITY_RESOLUTION_ARE_NOT_JOINTLY_SOURCE_TRANSPORTED','same_projectable_family_identity':True,'uv_scattering_authority':True,'near_gr_kinetic_rg_trajectory_authority':True,'ir_scalar_instability_authority':True,'static_higher_derivative_endpoint_rescue_authority':False,'time_dependent_ir_resolution_authority':False,'normalized_same_realization_uv_to_ir_observable_comparator':False,'scope_guard':['BLOCKED_IS_NOT_FAIL','SAME_FAMILY_DOES_NOT_IMPLY_SAME_REALIZATION_TRANSPORT','NO_PARAMETER_ZERO_FILL','NO_PARENT_FAMILY_TERMINALIZATION','NO_D7_PROMOTION']}
Path('iter351-horava-transport-guard.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps(out,sort_keys=True))

#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
root=Path('iter353-355-results')
coupled=[json.loads(p.read_text()) for p in root.rglob('coupled-*.json')]
controls=[json.loads(p.read_text()) for p in root.rglob('control-*.json')]
guards=[json.loads(p.read_text()) for p in root.rglob('iter355-gft-scope-guard.json')]
assert len(coupled)==4,len(coupled); assert len(controls)==4,len(controls); assert len(guards)==1,len(guards)
assert sorted(round(x['alpha_i'],6) for x in coupled)==[0.01,0.1,0.3,1.0]
assert all('FUNCTIONAL_RIGIDITY' in x['classification'] for x in coupled)
assert all(x['maximum_identity_scaled_residual']<1e-13 for x in coupled)
assert all(x['minimum_joint_nonstandard_norm']>1e-12 for x in coupled)
assert all('RELATIVISTIC_SHAPE_CONTROL' in x['classification'] for x in controls)
assert all(x['maximum_gamma_k_dependence']<1e-15 and x['maximum_affine_slope_residual']<1e-13 for x in controls)
assert 'BLOCKED_SCOPED' in guards[0]['classification']
summary={
 'iteration_bundle':'353-355',
 'coupled_alpha_i_values':sorted(x['alpha_i'] for x in coupled),
 'coupled_total_algebraic_cases':sum(x['case_count'] for x in coupled),
 'coupled_global_minimum_joint_nonstandard_norm':min(x['minimum_joint_nonstandard_norm'] for x in coupled),
 'coupled_maximum_source_identity_scaled_residual':max(x['maximum_identity_scaled_residual'] for x in coupled),
 'decoupled_control_cases':sorted(x['case'] for x in controls),
 'decoupled_all_k_independent_damping_and_affine_radicand':True,
 'source_scope_status':'BLOCKED_INTENSIVE_SECTOR_PLUS_SOURCE_TERM_PLUS_OBSERVABLE_SPECTRUM_PLUS_FULL_GRAVITY_COMPARATOR_AND_REDUCTION_MAP',
 'classification':'PASS_SCOPED_GFT_CONDENSATE_MATTER_PROPAGATION_FUNCTIONAL_RIGIDITY__COUPLED_SOURCE_RELATIONS_FORCE_K_DEPENDENT_DAMPING_OR_NONAFFINE_K2_RADICAND_WHILE_DECOUPLED_CONTROL_RECOVERS_RELATIVISTIC_SHAPE__FAMILY_CLOSURE_REMAINS_BLOCKED',
 'family_status':'PARTIAL_SUBFAMILY_ONLY',
 'family_terminal':False,
 'd7_promotion_authorized':False,
 'refined_blocker':'GFT_INTENSIVE_PHYSICAL_SECTOR_SELECTION_PLUS_SOURCE_TERM_AND_OBSERVABLE_SPECTRUM_BRIDGE_PLUS_FULL_GRAVITY_OBSERVABLE_COMPARATOR_OUTSIDE_CONDENSATE_COSMOLOGY_PLUS_EXPLICIT_SPINFOAM_REDUCTION_OR_INDEPENDENCE_DISPOSITION',
 'scope_guard':['CONDENSATE_MATTER_PROPAGATION_CHILD_ONLY','NO_PARENT_EXHAUSTION','NO_IMPLICIT_GFT_TO_SPINFOAM_MERGE','NO_BLOCKED_TO_FAIL_CONVERSION','NO_D7_PROMOTION']
}
Path('iter353-355-summary.json').write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n'); print(json.dumps(summary,sort_keys=True))

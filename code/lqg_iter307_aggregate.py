#!/usr/bin/env python3
import hashlib, json, pathlib

root=pathlib.Path('build/lqg-iter307-results')
rows=[json.loads(p.read_text()) for p in sorted(root.glob('*.json'))]
expected={'jhalf_leading_kernel','k5_causal_sign_product','intertwiner_invariance','exact_collinear_contraction','absolute_integrability_power','scope_guard'}
seen={r.get('probe') for r in rows}
if seen!=expected or not all(r.get('pass') is True for r in rows):
    raise SystemExit(f'probe barrier failed: seen={seen}, expected={expected}')
contract=json.load(open('benchmarks/lqg_iter307_minspin_contracted_local_witness.json'))
out={
  'iteration':307,
  'family':'LQG_SPINFOAM',
  'classification':contract['frozen_classification_target'],
  'independent_probes':sorted(seen),
  'boundary_spins':'all ten j_ab=1/2',
  'boundary_intertwiners':['A','A','B','A','A'],
  'exact_leading_coefficient':'-1/[648*(1+gamma^2)^10]',
  'local_integrand_scaling':'delta^-20',
  'local_reduced_noncompact_dimension':12,
  'absolute_radial_scaling':'delta^-9 ddelta',
  'local_absolute_integrability_for_witness_component':False,
  'fixed_causal_vertex_unqualified_absolute_finiteness_gate':'FAIL_FOR_EXPLICIT_BOUNDARY_COMPONENT',
  'conditional_or_distributional_vertex_nonexistence_proven':False,
  'all_boundary_components_diverge_proven':False,
  'lambda_f_weighted_complete_stack_control_proven':False,
  'same_realization_uv_to_causal_regge_gr_transport_proven':False,
  'family_terminal':False,
  'd7_authorized':False,
  'terminal_count':'1/15',
  'next_required_object':'source-grounded regularization/distributional prescription for the fixed causal vertex, with proof of compatibility with boundary contraction, gluing, normalization and cutoff removal; absent that, D7_S2 absolute-finiteness route is blocked'
}
raw=json.dumps(out,indent=2,sort_keys=True)+'\n'
pathlib.Path('build/lqg-iter307-summary.json').write_text(raw)
digest=hashlib.sha256(raw.encode()).hexdigest()
pathlib.Path('build/lqg-iter307-summary.sha256').write_text(digest+'  lqg-iter307-summary.json\n')

#!/usr/bin/env python3
import json, pathlib

p=json.load(open('benchmarks/lqg_iter307_minspin_contracted_local_witness.json'))
c=p['prospectively_frozen_claims']
ok=(c['j_half_branch_leading_kernel_exact'] and
    c['k5_causal_branch_scalar_product_independent_of_sigma'] and
    c['chosen_boundary_tensors_are_su2_invariant'] and
    (not c['local_absolute_integrability_for_witness_component']) and
    (not c['conditional_or_distributional_vertex_nonexistence_proven']) and
    (not c['all_boundary_components_diverge_proven']) and
    (not c['lambda_f_weighted_complete_stack_control_proven']) and
    (not c['same_realization_uv_to_causal_regge_gr_transport_proven']) and
    (not c['family_terminal']) and (not c['d7_authorized']))
out={'probe':'scope_guard','pass':bool(ok),'iteration':307,
     'refuted_claim':'unqualified local absolute convergence/finiteness for every fixed-causal vertex boundary component',
     'proven_scope':'one explicit legitimate j=1/2 boundary-intertwiner component fails local absolute integrability',
     'not_proven':['nonexistence of conditional/principal-value/distributional/regularized vertex','divergence of every boundary component','complete-stack failure','family no-go','D7 authorization'],
     'next_required_object':'determine whether the causal proposal specifies a mathematically controlled regularization/distributional prescription compatible with gluing and normalization; otherwise absolute-finiteness gate fails'}
pathlib.Path('build/lqg-iter307').mkdir(parents=True,exist_ok=True)
pathlib.Path('build/lqg-iter307/scope_guard.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if not ok: raise SystemExit(1)

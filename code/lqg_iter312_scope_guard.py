#!/usr/bin/env python3
import json, pathlib
p=json.load(open('benchmarks/lqg_iter312_partial_diagonal_causal_sign_cancellation.json'))
c=p['prospectively_frozen_claims']
ok=(c['triangle_factor_each_causal_sector']==-1 and c['full_k5_factor_each_causal_sector']==1 and
    c['unit_weight_triangle_sum_each_of_10']==-16 and c['unit_weight_k4_sum_each_of_5']==0 and c['unit_weight_full_k5_sum']==16 and
    not c['nontrivial_nonnegative_class_weights_cancel_triangle_and_k5'] and
    c['signed_class_weight_null_direction']==[-5,-1,1] and
    not c['signed_class_weight_null_direction_source_grounded_or_physically_admissible'] and
    not c['leading_sign_cancellation_implies_full_tensor_residue_cancellation'] and
    not c['family_terminal'] and not c['d7_authorized'])
out={'probe':'scope_guard','pass':bool(ok),'iteration':312,
     'proven_scope':'exact leading causal-sign factors and class-weight cancellation equations on K3/K4/K5 collapse strata',
     'robust_obstruction':'unit and all nontrivial nonnegative class weights preserve K3 and K5 leading sign factors',
     'algebraic_loophole':'signed class weights proportional to (-5,-1,+1) cancel the scalar leading sign equations',
     'not_proven':['signed weights are physically admissible/source-grounded','full angular/intertwiner residues cancel under that weighting','all K3/K4 residues are nonzero for every boundary component','family terminality','D7 authorization'],
     'next_required':'audit source causal-structure weights and explicit contracted K3 residues; reject or retain the signed-weight loophole before defining the forest extension problem'}
pathlib.Path('build/lqg-iter312').mkdir(parents=True,exist_ok=True)
pathlib.Path('build/lqg-iter312/scope_guard.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if not ok: raise SystemExit(1)

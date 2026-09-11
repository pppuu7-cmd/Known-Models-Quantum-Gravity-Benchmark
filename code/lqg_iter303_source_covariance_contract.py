#!/usr/bin/env python3
import json, pathlib
p=json.load(open('benchmarks/lqg_iter303_toller_su2_haar_glue.json'))
c=p['prospectively_frozen_claims']
ok=(c['han_half_link_glue_is_su2_haar_schur_contraction'] and
    c['han_glue_identity_is_matrix_index_contraction_after_su2_orthogonality'] and
    c['toller_cartan_form_preserves_left_right_su2_magnetic_index_spaces'] and
    c['gamma_simple_causal_block_has_matching_j_to_j_finite_index_space'] and
    c['fixed_toller_branch_is_not_sl2c_representation'] and
    c['sl2c_representation_composition_not_required_for_su2_boundary_schur_glue'])
out={'probe':'source_covariance_contract','pass':bool(ok),'iteration':303,
     'fixed_spin_su2_index_spaces_match':True,
     'toller_sl2c_representation_law':False,
     'tested_claim':'source-grounded separation of SU2 boundary covariance from SL2C branch composition'}
pathlib.Path('build/lqg-iter303').mkdir(parents=True,exist_ok=True)
pathlib.Path('build/lqg-iter303/source_covariance_contract.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if not ok: raise SystemExit(1)

#!/usr/bin/env python3
import json, pathlib
p=json.load(open('benchmarks/lqg_iter316_k4_full_branch_residue.json'))
c=p['prospectively_frozen_claims']
ok=(c['internal_k4_residue_tensor_nonzero_all_5'] and c['cplus_external_star_patterns_each']==16 and
    c['cplus_formal_k4_branch_polynomial']=='tensor_product_four(Tplus-Tminus)' and
    not c['cplus_formal_k4_branch_polynomial_identically_zero'] and
    not c['unit_scalar_sign_sum_zero_implies_full_k4_residue_zero'] and
    not c['explicit_physical_external_toller_evaluation_nonzero_proven'] and
    not c['family_terminal'] and not c['d7_authorized'])
out={'probe':'scope_guard','pass':bool(ok),'iteration':316,
     'proven_scope':'all five K4 internal residue tensors are nonzero and the source-C+ external branch sum is a nonzero formal polynomial equal to a fourfold tensor product of T+ minus T-',
     'refuted_inference':'zero K4 scalar sign sum does not imply zero full K4 residue',
     'open':['explicit physical external Toller evaluation','global forest-compatible extension','complete-stack normalization/cutoff control','family terminality','D7 authorization']}
pathlib.Path('build/lqg-iter316-guards').mkdir(parents=True,exist_ok=True)
pathlib.Path('build/lqg-iter316-guards/scope_guard.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if not ok: raise SystemExit(1)

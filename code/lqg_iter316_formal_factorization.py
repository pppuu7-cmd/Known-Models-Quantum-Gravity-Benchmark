#!/usr/bin/env python3
import itertools, json, pathlib, math
p=json.load(open('benchmarks/lqg_iter316_k4_full_branch_residue.json'))
# Encode a formal monomial by its four branch signs k_i in {+1,-1}.
# Source-C+ coefficient is product k_i.  Expansion of tensor_i(T_i^+ - T_i^-)
# has exactly the same coefficient: +1 for a + branch choice and -1 for a - choice.
source={k:math.prod(k) for k in itertools.product((-1,1),repeat=4)}
factorized={k:math.prod(1 if q==1 else -1 for q in k) for k in itertools.product((-1,1),repeat=4)}
identical=(source==factorized)
unit_scalar_specialization=sum(source.values())
nonzero_coeffs=sum(v!=0 for v in source.values())
ok=(identical and nonzero_coeffs==16 and unit_scalar_specialization==0 and
    p['prospectively_frozen_claims']['cplus_formal_k4_branch_polynomial']=='tensor_product_four(Tplus-Tminus)' and
    p['prospectively_frozen_claims']['cplus_formal_k4_branch_polynomial_identically_zero'] is False and
    p['prospectively_frozen_claims']['unit_scalar_sign_sum_zero_implies_full_k4_residue_zero'] is False)
out={'probe':'formal_factorization','pass':bool(ok),'iteration':316,
     'formal_monomial_count':16,'nonzero_coefficients':nonzero_coeffs,
     'coefficient_histogram':{'plus':sum(v==1 for v in source.values()),'minus':sum(v==-1 for v in source.values())},
     'exact_factorization':'tensor_product_{i=1..4}(T_i^+ - T_i^-)',
     'unit_scalar_specialization':unit_scalar_specialization,
     'interpretation':'the scalar sum vanishes only after setting every T_i^+=T_i^-=1; the full formal branch polynomial has 16 nonzero monomials'}
pathlib.Path('build/lqg-iter316-guards').mkdir(parents=True,exist_ok=True)
pathlib.Path('build/lqg-iter316-guards/formal_factorization.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if not ok: raise SystemExit(1)

#!/usr/bin/env python3
import json, pathlib
p=json.load(open('benchmarks/lqg_iter311_partial_diagonal_subdivergence_census.json'))
c=p['prospectively_frozen_claims']
ok=(c['proper_marginal_or_divergent_partial_diagonals']==15 and
    c['including_total_diagonal_non_safe_subsets']==16 and
    c['global_distribution_extension_requires_partial_diagonal_control'] and
    not c['all_partial_diagonal_leading_coefficients_nonzero_proven'] and
    not c['family_terminal'] and not c['d7_authorized'])
out={'probe':'scope_guard','pass':bool(ok),'iteration':311,
     'proven_scope':'exact minimal-spin power-count and overlap geometry of K3, K4 and K5 collapse strata',
     'not_proven':['nonzero residue for every boundary component on every stratum','unique forest renormalization','complete-stack control','family terminality','D7 authorization'],
     'next_required':'test which partial-diagonal leading residues survive causal-sector summation and boundary contraction, then impose compatible extension conditions on all surviving strata'}
pathlib.Path('build/lqg-iter311').mkdir(parents=True,exist_ok=True)
pathlib.Path('build/lqg-iter311/scope_guard.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if not ok: raise SystemExit(1)

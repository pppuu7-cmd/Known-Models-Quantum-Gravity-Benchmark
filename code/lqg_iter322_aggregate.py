#!/usr/bin/env python3
import json
from pathlib import Path

root=Path('build/lqg-iter322-results')
files=sorted(root.glob('K*.json'))
if len(files)!=3:
    raise SystemExit(f'expected K3/K4/K5 artifacts, got {len(files)}')
rows={r['collapse_size']:r for r in (json.loads(p.read_text()) for p in files)}
assert set(rows)=={3,4,5}
assert rows[3]['invariant_basis_dimension_leq_omega']==1
assert rows[4]['invariant_basis_dimension_leq_omega']==17
assert rows[5]['invariant_basis_dimension_leq_omega']==1757
raw_weighted=10*rows[3]['raw_derivative_multiindices_leq_omega']+5*rows[4]['raw_derivative_multiindices_leq_omega']+rows[5]['raw_derivative_multiindices_leq_omega']
inv_weighted=10*rows[3]['invariant_basis_dimension_leq_omega']+5*rows[4]['invariant_basis_dimension_leq_omega']+rows[5]['invariant_basis_dimension_leq_omega']
assert raw_weighted==127080
assert inv_weighted==1852
summary={
 'iteration':322,
 'per_stratum_internal_Ss_invariant_basis':{
   'K3':1,'K4':17,'K5':1757
 },
 'raw_weighted_local_multiindex_slots':raw_weighted,
 'weighted_internal_permutation_invariant_scalar_basis_slots':inv_weighted,
 'formal_reduction_factor':raw_weighted/inv_weighted,
 'derivative_order_dimensions':{
   'K3':rows[3]['invariant_dimensions_by_exact_derivative_order'],
   'K4':rows[4]['invariant_dimensions_by_exact_derivative_order'],
   'K5':rows[5]['invariant_dimensions_by_exact_derivative_order']
 },
 'classification':'internal vertex-permutation symmetry alone strongly reduces the scalar local normal-derivative basis, but leaves a nontrivial extension space, especially on K5; uniqueness is not supplied by S_s symmetry alone',
 'scope_guard':'1852 is a multiplicity-weighted scalar invariant-basis bookkeeping count under internal S_s only, not a number of physical counterterms. It ignores/does not settle external tensor structure, Lorentz/SU2 covariance, orientation, gluing, forest overlaps, normalization and any source-defined joint boundary-value prescription.'
}
out=Path('build/lqg-iter322-summary.json')
out.write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n')
print(json.dumps(summary,sort_keys=True))

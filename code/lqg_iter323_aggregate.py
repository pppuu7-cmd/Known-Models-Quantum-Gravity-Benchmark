#!/usr/bin/env python3
import json
from pathlib import Path

root=Path('build/lqg-iter323-results')
files=sorted(root.glob('K*.json'))
if len(files)!=3: raise SystemExit(f'expected 3 artifacts, got {len(files)}')
rows={r['collapse_size']:r for r in (json.loads(p.read_text()) for p in files)}
assert set(rows)=={3,4,5}
assert [rows[s]['invariant_basis_dimension_leq_omega'] for s in (3,4,5)]==[1,2,28]
weighted=10*rows[3]['invariant_basis_dimension_leq_omega']+5*rows[4]['invariant_basis_dimension_leq_omega']+rows[5]['invariant_basis_dimension_leq_omega']
assert weighted==48
assert all(rows[s]['constant_delta_mode_survives'] for s in rows)
summary={
 'iteration':323,
 'per_stratum_Ss_x_SO3_scalar_invariant_basis':{'K3':1,'K4':2,'K5':28},
 'weighted_across_10K3_5K4_1K5':weighted,
 'previous_weighted_Ss_only':1852,
 'raw_weighted_multiindices':127080,
 'formal_reduction_vs_Ss_only':1852/weighted,
 'formal_reduction_vs_raw':127080/weighted,
 'constant_delta_mode_survives_on_all_sizes':True,
 'classification':'even after simultaneous internal vertex-permutation and SO3 scalar normal-sector symmetry, the allowed local extension space does not collapse to a unique structure; K5 alone retains 28 invariant derivative structures through order 8',
 'scope_guard':'48 is conditional scalar normal-sector symmetry bookkeeping, not physical counterterm count. Full tensor covariance, gluing, overlap/forest consistency, orientation, normalization and a possible source-defined joint boundary-value prescription may further reduce or fix the space.'
}
out=Path('build/lqg-iter323-summary.json')
out.write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n')
print(json.dumps(summary,sort_keys=True))

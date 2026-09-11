#!/usr/bin/env python3
import hashlib, itertools, json
from pathlib import Path

root = Path('build/lqg-iter318-results')
files = sorted(root.glob('subset_*.json'))
if len(files) != 16:
    raise SystemExit(f'expected 16 stratum artifacts, got {len(files)}')
rows = [json.loads(p.read_text()) for p in files]
subsets = {frozenset(map(int,r['subset'])): r for r in rows}
expected_sizes = {3:10,4:5,5:1}
actual_sizes = {s:sum(r['size']==s for r in rows) for s in expected_sizes}
assert actual_sizes == expected_sizes
assert all(r['raw_local_derivative_multiindices_leq_omega'] == {3:1,4:220,5:125970}[r['size']] for r in rows)
weighted = sum(r['raw_local_derivative_multiindices_leq_omega'] for r in rows)
assert weighted == 127080

nodes = list(subsets)
def compatible(a,b):
    return a <= b or b <= a or a.isdisjoint(b)
forests=[]
for mask in range(1 << len(nodes)):
    fam=[nodes[i] for i in range(len(nodes)) if mask & (1<<i)]
    if all(compatible(a,b) for a,b in itertools.combinations(fam,2)):
        forests.append(fam)
forest_count=len(forests)
max_depth=max(map(len, forests))
nested_pairs=sum(1 for a,b in itertools.combinations(nodes,2) if a < b or b < a)
overlap_incomparable=sum(1 for a,b in itertools.combinations(nodes,2) if a & b and not (a <= b or b <= a))
disjoint_pairs=sum(1 for a,b in itertools.combinations(nodes,2) if a.isdisjoint(b))
assert (forest_count,max_depth,nested_pairs,overlap_incomparable,disjoint_pairs)==(72,3,35,85,0)
summary={
 'iteration':318,
 'non_safe_strata':16,
 'strata_by_size':actual_sizes,
 'all_strata_have_prior_physical_nonzero_witness':True,
 'raw_local_counterterm_slots_weighted_total':weighted,
 'raw_slots_by_stratum_size':{'K3':1,'K4':220,'K5':125970},
 'pair_census':{'nested':nested_pairs,'overlapping_incomparable':overlap_incomparable,'disjoint':disjoint_pairs},
 'compatible_forest_count_including_empty':forest_count,
 'maximum_non_safe_forest_depth':max_depth,
 'classification':'forest-compatible extension data required across all 16 physically witnessed non-safe strata; a total-diagonal-only prescription is insufficient',
 'scope_guard':'127080 is raw local derivative multiindex bookkeeping, not 127080 independent physical renormalization constants; symmetries, gluing, overlap consistency and normalization may reduce/tie coefficients; this does not prove that no unique source-defined joint extension exists'
}
out=Path('build/lqg-iter318-summary.json')
out.write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n')
h=hashlib.sha256(out.read_bytes()).hexdigest()
Path('build/lqg-iter318-summary.sha256').write_text(h+'  '+out.name+'\n')
print(json.dumps(summary,sort_keys=True))

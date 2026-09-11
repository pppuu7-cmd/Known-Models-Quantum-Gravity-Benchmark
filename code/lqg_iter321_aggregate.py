#!/usr/bin/env python3
import itertools, json
from pathlib import Path

root=Path('build/lqg-iter321-results')
files=sorted(root.glob('*.json'))
if len(files)!=12:
    raise SystemExit(f'expected 12 orbit artifacts, got {len(files)}')
rows=[json.loads(p.read_text()) for p in files]
forest=[r for r in rows if r['kind']=='forest']
overlap=[r for r in rows if r['kind']=='overlap']
assert len(forest)==8 and len(overlap)==4
assert sum(r['orbit_size'] for r in forest)==72
assert sum(r['orbit_size'] for r in overlap)==85
assert all(r['orbit_size']*r['stabilizer_order']==120 for r in rows)

def fs(s): return frozenset(int(c) for c in s)
def enc_fam(F):
    z=tuple(sorted((tuple(sorted(S)) for S in F), key=lambda x:(len(x),x)))
    return '|'.join(''.join(map(str,S)) for S in z) if z else 'EMPTY'
def compatible(a,b): return a<=b or b<=a or a.isdisjoint(b)

nodes=[]
for s in (3,4,5):
    nodes += [frozenset(c) for c in itertools.combinations(range(5),s)]
raw_forests=set()
for mask in range(1<<len(nodes)):
    fam=[nodes[i] for i in range(len(nodes)) if mask&(1<<i)]
    if all(compatible(a,b) for a,b in itertools.combinations(fam,2)):
        raw_forests.add(enc_fam(fam))
assert len(raw_forests)==72
raw_overlap=set()
for a,b in itertools.combinations(nodes,2):
    if a&b and not (a<=b or b<=a):
        raw_overlap.add(enc_fam((a,b)))
assert len(raw_overlap)==85

union_f=set().union(*(set(r['members']) for r in forest))
union_o=set().union(*(set(r['members']) for r in overlap))
assert union_f==raw_forests
assert union_o==raw_overlap
assert sum(len(set(r['members'])) for r in forest)==len(union_f)
assert sum(len(set(r['members'])) for r in overlap)==len(union_o)

summary={
 'iteration':321,
 's5_order':120,
 'raw_compatible_forests':72,
 'forest_orbits':8,
 'raw_overlapping_incomparable_pairs':85,
 'overlap_orbits':4,
 'raw_combinatorial_consistency_cases':157,
 's5_orbit_classes_total':12,
 'reduction_factor_raw_to_orbits':157/12,
 'forest_orbit_sizes':sorted(r['orbit_size'] for r in forest),
 'overlap_orbit_sizes':sorted(r['orbit_size'] for r in overlap),
 'exact_partition_verified':True,
 'classification':'S5 vertex relabeling reduces 157 raw forest/overlap support-consistency cases to 12 exact orbit classes, allowing subsequent extension-consistency work to target one representative per class plus stabilizer constraints',
 'scope_guard':'12 is a count of combinatorial orbit classes only, not physical renormalization constants and not a quotient of the 127080 raw derivative multiindices by itself.'
}
out=Path('build/lqg-iter321-summary.json')
out.write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n')
print(json.dumps(summary,sort_keys=True))

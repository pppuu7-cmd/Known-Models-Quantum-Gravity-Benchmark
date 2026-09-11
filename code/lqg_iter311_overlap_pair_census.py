#!/usr/bin/env python3
import itertools, json, pathlib
p=json.load(open('benchmarks/lqg_iter311_partial_diagonal_subdivergence_census.json'))
subs=[frozenset(S) for s in (3,4,5) for S in itertools.combinations(range(5),s)]
nested=overlap=disjoint=0
rows=[]
for A,B in itertools.combinations(subs,2):
    if A<=B or B<=A:
        kind='nested'; nested+=1
    elif A.isdisjoint(B):
        kind='disjoint'; disjoint+=1
    else:
        kind='overlapping_incomparable'; overlap+=1
    rows.append({'A':sorted(A),'B':sorted(B),'kind':kind})
ok=(len(rows)==120 and nested==35 and overlap==85 and disjoint==0 and
    p['prospectively_frozen_claims']['nested_pairs_among_non_safe_subsets']==35 and
    p['prospectively_frozen_claims']['overlapping_incomparable_pairs_among_non_safe_subsets']==85)
out={'probe':'overlap_pair_census','pass':bool(ok),'iteration':311,'pair_count':len(rows),
     'nested_pairs':nested,'overlapping_incomparable_pairs':overlap,'disjoint_pairs':disjoint}
pathlib.Path('build/lqg-iter311').mkdir(parents=True,exist_ok=True)
pathlib.Path('build/lqg-iter311/overlap_pair_census.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if not ok: raise SystemExit(1)

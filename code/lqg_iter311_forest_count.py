#!/usr/bin/env python3
import itertools, json, pathlib
p=json.load(open('benchmarks/lqg_iter311_partial_diagonal_subdivergence_census.json'))
subs=[frozenset(S) for s in (3,4,5) for S in itertools.combinations(range(5),s)]
def compatible(A,B):
    return A<=B or B<=A or A.isdisjoint(B)
forests=[]
for r in range(len(subs)+1):
    if r>3: break
    for fam in itertools.combinations(subs,r):
        if all(compatible(A,B) for A,B in itertools.combinations(fam,2)):
            forests.append(fam)
counts={r:sum(len(f)==r for f in forests) for r in range(4)}
ok=(counts=={0:1,1:16,2:35,3:20} and len(forests)==72 and
    p['prospectively_frozen_claims']['compatible_nested_forests_including_empty']==72)
out={'probe':'forest_count','pass':bool(ok),'iteration':311,'forest_count':len(forests),
     'counts_by_size':{str(k):v for k,v in counts.items()},
     'interpretation':'with five vertices all compatible non-safe collections are inclusion chains; maximum forest depth is 3 (K3 subset K4 subset K5)'}
pathlib.Path('build/lqg-iter311').mkdir(parents=True,exist_ok=True)
pathlib.Path('build/lqg-iter311/forest_count.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if not ok: raise SystemExit(1)

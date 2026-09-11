#!/usr/bin/env python3
import itertools, json, pathlib
p=json.load(open('benchmarks/lqg_iter311_partial_diagonal_subdivergence_census.json'))
nodes=range(5)
non_safe=[]; proper=[]
for s in (3,4,5):
    for S in itertools.combinations(nodes,s):
        non_safe.append(S)
        if s<5: proper.append(S)
ok=(len(proper)==15 and len(non_safe)==16 and
    sum(len(S)==3 for S in non_safe)==10 and sum(len(S)==4 for S in non_safe)==5 and sum(len(S)==5 for S in non_safe)==1 and
    p['prospectively_frozen_claims']['proper_marginal_or_divergent_partial_diagonals']==15 and
    p['prospectively_frozen_claims']['including_total_diagonal_non_safe_subsets']==16)
out={'probe':'non_safe_subset_count','pass':bool(ok),'iteration':311,
     'proper_partial_diagonals':len(proper),'all_non_safe_subsets':len(non_safe),
     'counts_by_size':{'3':10,'4':5,'5':1},'subsets':[list(S) for S in non_safe]}
pathlib.Path('build/lqg-iter311').mkdir(parents=True,exist_ok=True)
pathlib.Path('build/lqg-iter311/non_safe_subset_count.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if not ok: raise SystemExit(1)

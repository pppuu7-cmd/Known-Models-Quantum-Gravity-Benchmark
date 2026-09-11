#!/usr/bin/env python3
import itertools, json, pathlib
from fractions import Fraction

contract=json.load(open('benchmarks/lqg_iter305_toller_tail_local_integrability_split.json'))
nodes=range(5)
edges=list(itertools.combinations(nodes,2))
cut_sizes=[]
for r in range(1,5):
    for subset in itertools.combinations(nodes,r):
        s=set(subset)
        if 0 not in s:
            continue
        cut=sum(((a in s) != (b in s)) for a,b in edges)
        cut_sizes.append(cut)
edge_connectivity=min(cut_sizes)
tau=Fraction(1,2*len(edges))
comparison=Fraction(1,1)-tau
decay=Fraction(1,1)
margin=decay-comparison
ok=(len(edges)==10 and edge_connectivity>=3 and tau==Fraction(1,20) and
    comparison==Fraction(19,20) and margin==Fraction(1,20) and
    contract['prospectively_frozen_claims']['radial_tail_decay_exponent_strictly_exceeds_kaminski_comparison_exponent'])
out={
  'probe':'k5_kaminski_margin',
  'pass':bool(ok),
  'iteration':305,
  'graph':'K5',
  'edge_count':len(edges),
  'edge_connectivity':edge_connectivity,
  'three_edge_connected':edge_connectivity>=3,
  'tau':'1/20',
  'comparison_exponent':'19/20',
  'toller_worst_gamma_simple_tail_exponent':'1',
  'strict_exponent_margin':'1/20'
}
pathlib.Path('build/lqg-iter305').mkdir(parents=True,exist_ok=True)
pathlib.Path('build/lqg-iter305/k5_kaminski_margin.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if not ok: raise SystemExit(1)

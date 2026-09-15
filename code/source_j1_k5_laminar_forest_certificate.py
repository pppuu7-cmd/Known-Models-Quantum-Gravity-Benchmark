import itertools,json,math
from collections import Counter
V=tuple(range(5))
subs=[frozenset(c) for k in range(2,6) for c in itertools.combinations(V,k)]

def lam(a,b): return a<=b or b<=a or a.isdisjoint(b)
def valid(f): return all(lam(a,b) for a,b in itertools.combinations(f,2))
def omega(s,edge=3):
 k=len(s); return edge*(k*(k-1)//2)-3*(k-1)
def depth(f):
 if not f:return 0
 return max(sum(1 for t in f if t<=s) for s in f)
def canon(f):
 reps=[]
 for p in itertools.permutations(V):
  mp={i:p[i] for i in V}
  ff=sorted(tuple(sorted(mp[x] for x in s)) for s in f)
  reps.append(tuple(ff))
 return min(reps)
forests=[]
# Backtracking enumerates each laminar family once.
def rec(i,cur):
 if i==len(subs): forests.append(tuple(cur)); return
 rec(i+1,cur)
 s=subs[i]
 if all(lam(s,t) for t in cur): rec(i+1,cur+[s])
rec(0,[])
assert valid([frozenset((0,1))])
assert valid([frozenset((0,1)),frozenset((0,1,2)),frozenset((0,1,2,3)),frozenset(V)])
assert not valid([frozenset((0,1)),frozenset((1,2))])
assert valid([frozenset((0,1)),frozenset((2,3))])
orders={''.join(map(str,sorted(s))):max(0,math.floor(omega(s))) for s in subs}
orders2={''.join(map(str,sorted(s))):max(0,math.floor(omega(s,2))) for s in subs}
assert orders!=orders2
orbits=Counter(canon(f) for f in forests)
# direct invariance spot-complete: every permutation of every forest remains valid
for f in forests:
 for p in itertools.permutations(V):
  mp={i:p[i] for i in V}; assert valid([frozenset(mp[x] for x in s) for s in f])
out={
 'classifier':'FOREST_CERTIFIED_SCOPED',
 'connected_subset_count':len(subs),
 'subset_size_census':dict(Counter(map(len,subs))),
 'forest_count_including_empty':len(forests),
 'forest_cardinality_histogram':dict(sorted(Counter(map(len,forests)).items())),
 'max_forest_cardinality':max(map(len,forests)),
 'max_nested_chain_depth':max(depth(f) for f in forests),
 's5_orbit_count':len(orbits),
 's5_orbit_size_histogram':dict(sorted(Counter(orbits.values()).items())),
 'subtraction_order_by_subset_size':{k:max(0,math.floor(3*(k*(k-1)//2)-3*(k-1))) for k in range(2,6)},
 'omega_by_subset_size':{k:3*(k*(k-1)//2)-3*(k-1) for k in range(2,6)},
 'changed_scaling_control':orders!=orders2,
 'scope':'auxiliary scalar K5 collision forest only; no Eq4/channel00000/physical transfer; no terminal D7 classifier'
}
print(json.dumps(out,indent=2,sort_keys=True))
open('source_j1_k5_laminar_forest_certificate.json','w').write(json.dumps(out,indent=2,sort_keys=True))
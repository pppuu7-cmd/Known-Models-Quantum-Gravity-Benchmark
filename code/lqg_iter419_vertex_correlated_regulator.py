#!/usr/bin/env python3
import argparse, itertools, json, math, os

EDGES=[(i,j) for i in range(5) for j in range(i+1,5)]

def is_tree(edge_subset):
    parent=list(range(5))
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]; x=parent[x]
        return x
    def union(a,b):
        ra,rb=find(a),find(b)
        if ra==rb: return False
        parent[rb]=ra; return True
    for e in edge_subset:
        if not union(*e): return False
    r=find(0)
    return len(edge_subset)==4 and all(find(i)==r for i in range(5))

TREES=[tuple(c) for c in itertools.combinations(EDGES,4) if is_tree(c)]
assert len(TREES)==125

def exponent(vertex_profile):
    raw={e:(vertex_profile[e[0]]+vertex_profile[e[1]])/2.0 for e in EDGES}
    mean=sum(raw.values())/len(raw)
    a={e:v/mean for e,v in raw.items()}
    s=sum(a.values())
    best=max(sum(a[e] for e in T) for T in TREES)
    return s-best, a, best

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--index',type=int,required=True); ns=ap.parse_args()
    gate=json.load(open('benchmarks/lqg_iter419_vertex_correlated_regulator_gate.json'))
    profiles=gate['vertex_profiles']; v=profiles[ns.index]
    p,a,best=exponent(v)
    out={
      'iteration':419,'profile_index':ns.index,'vertex_profile':v,
      'normalized_edge_mean':sum(a.values())/len(a),
      'predicted_singular_exponent':p,
      'max_tree_weight':best,
      'edge_exponents':{f'{i}{j}':a[(i,j)] for i,j in EDGES},
      'spanning_tree_count':len(TREES),
      'scope_guard':gate['scope_guard']
    }
    os.makedirs('build/lqg-iter419',exist_ok=True)
    path=f'build/lqg-iter419/profile_{ns.index:02d}.json'
    with open(path,'w') as f: json.dump(out,f,indent=2,sort_keys=True); f.write('\n')
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=='__main__': main()

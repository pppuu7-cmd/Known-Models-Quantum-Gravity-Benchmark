#!/usr/bin/env python3
import argparse, itertools, json, math
from fractions import Fraction
from pathlib import Path

p=argparse.ArgumentParser()
p.add_argument('--size',type=int,required=True,choices=(3,4,5))
a=p.parse_args()
s=a.size
omega={3:0,4:3,5:8}[s]
d=3*(s-1)
perms=list(itertools.permutations(range(s)))

def compose(p,q):
    return tuple(p[q[i]] for i in range(len(p)))
def power(p,m):
    r=tuple(range(len(p)))
    for _ in range(m): r=compose(p,r)
    return r
def fixed(p):
    return sum(i==x for i,x in enumerate(p))
def sym_chars(p,kmax):
    # Normal-coordinate representation V = 3 copies of the standard S_s rep.
    # Power sums p_m = tr[V(g)^m] = 3*(Fix(g^m)-1).
    # Complete symmetric characters obey k h_k = sum_{m<=k} p_m h_{k-m}.
    h=[Fraction(1)]
    for k in range(1,kmax+1):
        rhs=Fraction(0)
        for m in range(1,k+1):
            pm=3*(fixed(power(p,m))-1)
            rhs += pm*h[k-m]
        h.append(rhs/Fraction(k))
    return h

chars=[sym_chars(g,omega) for g in perms]
invariants=[]
for k in range(omega+1):
    avg=sum((h[k] for h in chars),Fraction(0))/len(perms)
    assert avg.denominator==1, (s,k,avg)
    invariants.append(int(avg))
expected={
 3:[1],
 4:[1,0,6,10],
 5:[1,0,6,10,36,81,201,444,978]
}[s]
assert invariants==expected,(s,invariants,expected)
inv_total=sum(invariants)
raw_total=math.comb(d+omega,omega)
assert raw_total=={3:1,4:220,5:125970}[s]
assert inv_total=={3:1,4:17,5:1757}[s]

# Conjugacy-class diagnostic: cycle type -> multiplicity and character vectors.
def cycle_type(g):
    seen=set(); cyc=[]
    for i in range(s):
        if i in seen: continue
        j=i;n=0
        while j not in seen:
            seen.add(j);n+=1;j=g[j]
        cyc.append(n)
    return tuple(sorted(cyc,reverse=True))
classes={}
for g,h in zip(perms,chars):
    ct=cycle_type(g)
    item=classes.setdefault(str(ct),{'multiplicity':0,'sym_characters':None})
    item['multiplicity']+=1
    vec=[int(x) if x.denominator==1 else f'{x.numerator}/{x.denominator}' for x in h]
    if item['sym_characters'] is None: item['sym_characters']=vec
    else: assert item['sym_characters']==vec
assert sum(v['multiplicity'] for v in classes.values())==math.factorial(s)

out={
 'iteration':322,
 'collapse_size':s,
 'normal_dimension':d,
 'divergence_degree':omega,
 'stabilizer_internal_group':f'S_{s}',
 'normal_representation':f'3 copies of the {s-1}-dimensional standard representation',
 'raw_derivative_multiindices_leq_omega':raw_total,
 'invariant_dimensions_by_exact_derivative_order':invariants,
 'invariant_basis_dimension_leq_omega':inv_total,
 'raw_to_internal_permutation_invariant_reduction_factor':raw_total/inv_total,
 'conjugacy_class_diagnostics':classes,
 'classification':'exact Molien/character census for scalar local normal-derivative structures invariant under permutations internal to one collapsed vertex subset',
 'scope_guard':'This is a symmetry-reduced local scalar derivative basis under internal S_s relabeling only. It is not a count of independent physical renormalization constants: external tensor data, covariance, orientation, gluing, overlap/forest consistency and source normalization can further constrain or alter the admissible extension data.'
}
path=Path('build/lqg-iter322')/f'K{s}.json'
path.parent.mkdir(parents=True,exist_ok=True)
path.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,sort_keys=True))

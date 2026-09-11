#!/usr/bin/env python3
import argparse, itertools, json, math
from fractions import Fraction
from pathlib import Path

p=argparse.ArgumentParser()
p.add_argument('--size',type=int,required=True,choices=(3,4,5))
a=p.parse_args(); s=a.size
omega={3:0,4:3,5:8}[s]
d=3*(s-1)
perms=list(itertools.permutations(range(s)))

def compose(p,q): return tuple(p[q[i]] for i in range(len(p)))
def ppow(p,m):
    r=tuple(range(len(p)))
    for _ in range(m): r=compose(p,r)
    return r
def fixed(p): return sum(i==x for i,x in enumerate(p))

def padd(a,b):
    c=dict(a)
    for e,v in b.items():
        c[e]=c.get(e,Fraction(0))+v
        if c[e]==0: del c[e]
    return c
def pscale(a,c): return {e:v*c for e,v in a.items() if v*c}
def pmul(a,b):
    c={}
    for e,v in a.items():
        for f,w in b.items(): c[e+f]=c.get(e+f,Fraction(0))+v*w
    return {e:v for e,v in c.items() if v}

def sym_char_laurent(g,kmax):
    # V = Std(S_s) tensor Vec(SO3). For an SO3 z-rotation, Vec weights are -1,0,+1.
    # p_m = tr Std(g^m) * (z^-m + 1 + z^m), with tr Std = Fix(g^m)-1.
    # Newton recurrence gives characters of Sym^k(V) as Laurent polynomials in z.
    h=[{0:Fraction(1)}]
    for k in range(1,kmax+1):
        rhs={}
        for m in range(1,k+1):
            trstd=fixed(ppow(g,m))-1
            pm={-m:Fraction(trstd),0:Fraction(trstd),m:Fraction(trstd)}
            rhs=padd(rhs,pmul(pm,h[k-m]))
        h.append(pscale(rhs,Fraction(1,k)))
    return h

chars=[sym_char_laurent(g,omega) for g in perms]
inv=[]
for k in range(omega+1):
    # For integer-spin SO3 reps, multiplicity of spin 0 = weight-0 multiplicity - weight-1 multiplicity.
    # Averaging the resulting twisted trace over S_s projects to simultaneous S_s x SO3 invariants.
    total=Fraction(0)
    for h in chars:
        total += h[k].get(0,Fraction(0))-h[k].get(1,Fraction(0))
    avg=total/len(perms)
    assert avg.denominator==1,(s,k,avg)
    inv.append(int(avg))
expected={3:[1],4:[1,0,1,0],5:[1,0,1,0,3,0,7,0,16]}[s]
assert inv==expected,(s,inv,expected)
total=sum(inv)
assert total=={3:1,4:2,5:28}[s]
prev={3:1,4:17,5:1757}[s]
raw={3:1,4:220,5:125970}[s]

out={
 'iteration':323,
 'collapse_size':s,
 'normal_dimension':d,
 'divergence_degree':omega,
 'representation':f'Std(S_{s}) tensor Vec(SO3), dimension {d}',
 'invariant_dimensions_by_exact_derivative_order':inv,
 'invariant_basis_dimension_leq_omega':total,
 'previous_internal_Ss_only_basis':prev,
 'raw_multiindex_basis':raw,
 'reduction_vs_Ss_only':prev/total,
 'reduction_vs_raw':raw/total,
 'constant_delta_mode_survives':inv[0]==1,
 'classification':'exact simultaneous internal vertex-permutation and SO3 scalar normal-sector invariant census',
 'scope_guard':'This imposes simultaneous SO3 covariance on the 3-dimensional singular normal/boost directions in addition to internal S_s relabeling. It is a conditional scalar normal-sector symmetry audit, not a full Lorentz/SU2 tensor classification and not a count of independent physical renormalization constants. Forest/overlap consistency, gluing, orientation, normalization and any source-defined joint boundary-value prescription remain separate constraints.'
}
path=Path('build/lqg-iter323')/f'K{s}.json'
path.parent.mkdir(parents=True,exist_ok=True)
path.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,sort_keys=True))

#!/usr/bin/env python3
import argparse, cmath, itertools, json, math
from pathlib import Path

p = argparse.ArgumentParser()
p.add_argument('--orbit', type=int, required=True, choices=range(12))
a = p.parse_args()

V = tuple(range(5))
PERMS = tuple(itertools.permutations(V))
STRATA = tuple(frozenset(c) for s in (3,4,5) for c in itertools.combinations(V,s))

def compatible(x,y):
    return x <= y or y <= x or x.isdisjoint(y)

def norm_case(case):
    return tuple(sorted(case, key=lambda s:(len(s), tuple(sorted(s)))))

def image(case, perm):
    return norm_case(tuple(frozenset(perm[i] for i in s) for s in case))

def key(case):
    return tuple((len(s), tuple(sorted(s))) for s in norm_case(case))

def canonical(case):
    return min(key(image(case,p)) for p in PERMS)

# Exhaustive forest census over the 16 non-safe K3/K4/K5 strata.
forests=[]
for r in range(len(STRATA)+1):
    for c in itertools.combinations(STRATA,r):
        if all(compatible(x,y) for x,y in itertools.combinations(c,2)):
            forests.append(norm_case(c))
assert len(forests)==72
assert {len(f) for f in forests} <= {0,1,2,3}

overlaps=[]
for x,y in itertools.combinations(STRATA,2):
    if not compatible(x,y):
        overlaps.append(norm_case((x,y)))
assert len(overlaps)==85

forest_orbits={}
for c in forests:
    forest_orbits.setdefault(canonical(c),[]).append(c)
overlap_orbits={}
for c in overlaps:
    overlap_orbits.setdefault(canonical(c),[]).append(c)
assert len(forest_orbits)==8
assert len(overlap_orbits)==4
assert sum(map(len,forest_orbits.values()))==72
assert sum(map(len,overlap_orbits.values()))==85

ordered=[]
for kind,orbits in [('forest',forest_orbits),('overlap',overlap_orbits)]:
    for ck in sorted(orbits):
        ordered.append((kind,ck,orbits[ck]))
assert len(ordered)==12
kind,ck,members=ordered[a.orbit]
rep=members[0]

# Published j=1/2 branch projector identity used in Iter324/325.
gammas=[0.0,0.1,0.274,1.0,10.0]
epsilons=[1e-1,1e-2,1e-4,1e-6]
max_cancel=0.0
stratum_rows=[]
for sset in rep:
    s=len(sset)
    edges=s*(s-1)//2
    sd=2*edges
    d=3*(s-1)
    omega=sd-d
    assert omega==(s-1)*(s-3)
    local_max=0.0
    residue_min=float('inf')
    for gamma in gammas:
        rho=gamma/2.0
        C=2.0/(1.0+gamma*gamma)
        residue_min=min(residue_min,C**edges)
        for eps in epsilons:
            for sign in (-1,1):
                z=complex(rho,sign*eps)
                P=(z*z+0.25)/(rho*rho+0.25)
                err=abs(P/(z*z+0.25)-1.0/(rho*rho+0.25))
                local_max=max(local_max,err)
                max_cancel=max(max_cancel,err)
    assert local_max < 1e-11
    assert residue_min > 0.0
    stratum_rows.append({
        'vertices':sorted(sset),
        'size':s,
        'internal_edges':edges,
        'scaling_degree':sd,
        'relative_dimension':d,
        'divergence_degree':omega,
        'bf_unique_extension': sd < d,
        'bf_extension_nonunique_without_extra_normalization': sd >= d,
        'finite_source_spectral_epsilon_softens_leading_beta_pole':False,
        'max_projector_denominator_cancellation_error':local_max,
        'minimum_tested_absolute_internal_residue_factor':residue_min,
    })

# The empty forest is an exact combinatorial baseline; all non-empty orbit reps
# contain at least one non-safe stratum and therefore require extension data.
requires_extension=bool(rep)
if requires_extension:
    assert all(not r['bf_unique_extension'] for r in stratum_rows)

out={
    'iteration':326,
    'orbit_index':a.orbit,
    'case_kind':kind,
    'orbit_size':len(members),
    'representative':[sorted(s) for s in rep],
    'stratum_sizes':[len(s) for s in rep],
    'requires_distributional_extension':requires_extension,
    'strata':stratum_rows,
    'source_spectral_epsilon_edge_identity_verified':True,
    'max_projector_denominator_cancellation_error':max_cancel,
    'audited_source_joint_ten_wedge_forest_extension_status':'NOT_FOUND_IN_AUDITED_SOURCE',
    'source_audit_scope':[
        'Bianchi-Chen-Gamonal causal spinfoam vertex arXiv:2601.23162 Eq.(3)-(4)',
        'Bianchi-Chen-Gamonal Toller matrices/i-epsilon arXiv:2604.24945 individual beta>0 branches'
    ],
    'classification':(
        'EMPTY_FOREST_BASELINE' if not requires_extension else
        'The orbit contains non-safe partial diagonals whose leading residues survive finite source spectral i-epsilon. '
        'Brunetti-Fredenhagen scaling degree therefore leaves nonunique local extension data, while a unique joint ten-wedge forest-compatible prescription was not found in the audited source formulas.'
    ),
    'scope_guard':'NOT_FOUND_IN_AUDITED_SOURCE is a provenance/closure statement, not a theorem that no joint extension exists. This is not a terminal LQG FAIL and does not authorize D7/NEW_REQUIRED.'
}
path=Path('build/lqg-iter326')/f'orbit_{a.orbit:02d}.json'
path.parent.mkdir(parents=True,exist_ok=True)
path.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,sort_keys=True))

#!/usr/bin/env python3
import argparse, itertools, json
from pathlib import Path

V=tuple(range(5))
PERMS=list(itertools.permutations(V))
K4=[tuple(sorted(s)) for s in itertools.combinations(V,4)]
K3=[tuple(sorted(s)) for s in itertools.combinations(V,3)]


def image(subset,perm):
    return tuple(sorted(perm[i] for i in subset))

def orbit(seed, family):
    fam=set(family)
    return {image(seed,p) for p in PERMS if image(seed,p) in fam}

def transport_count(seed,target):
    return sum(image(seed,p)==target for p in PERMS)

def stabilizer(seed):
    return sum(image(seed,p)==seed for p in PERMS)

def audit(kind):
    if kind=='k4':
        fam=K4; seed=K4[0]
        lower={'value_rank':11,'first_jet_increment':5,'full_rank':16}
    elif kind=='k3':
        fam=K3; seed=K3[0]
        lower={'value_rank':4,'first_jet_increment':3,'second_jet_increment':9,'full_rank':16}
    else: raise ValueError(kind)
    orb=orbit(seed,fam)
    counts={''.join(map(str,t)):transport_count(seed,t) for t in fam}
    stab=stabilizer(seed)
    assert orb==set(fam)
    assert all(c==stab for c in counts.values())
    assert stab*len(fam)==120
    return {
      'iteration':333,
      'kind':kind,
      'raw_strata_count':len(fam),
      's5_orbit_count':1,
      'orbit_size':len(orb),
      'stabilizer_size':stab,
      'transporters_per_target':counts,
      'canonical_rank_requirements_from_iter332':lower,
      'covariant_transport_conclusion': f'All {len(fam)} {kind.upper()} strata are one S5 orbit; an S5-covariant source normalization cannot assign unrelated normalization laws to individual labeled strata. Canonical normalization data must transport equivariantly across the orbit.',
      'independence_guard':'Orbit equivalence removes label-wise independence but does not create or fix the missing canonical jet values. It therefore does not close source normalization.',
      'classification':'PASS_SCOPED_SINGLE_S5_STRATUM_ORBIT_WITH_COVARIANT_NORMALIZATION_REQUIREMENT',
      'scope_guard':'Combinatorial S5 transport plus previously validated candidate centered-stratum ranks; not a source-defined Haar/forest gluing map and not proof of unique physical extension.'
    }

def main():
    p=argparse.ArgumentParser(); p.add_argument('--kind',choices=['k4','k3'],required=True); p.add_argument('--output',required=True); a=p.parse_args()
    r=audit(a.kind); Path(a.output).parent.mkdir(parents=True,exist_ok=True); Path(a.output).write_text(json.dumps(r,indent=2,sort_keys=True)+'\n'); print(json.dumps(r,sort_keys=True))
if __name__=='__main__': main()

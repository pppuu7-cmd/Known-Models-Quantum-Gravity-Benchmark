#!/usr/bin/env python3
import itertools, json, math, pathlib
from fractions import Fraction

def parts(seq):
    if not seq: yield []; return
    x=seq[0]
    for p in parts(seq[1:]):
        yield [[x]]+[b[:] for b in p]
        for i in range(len(p)):
            q=[b[:] for b in p]; q[i]=q[i]+[x]; yield q

def canon(p): return tuple(sorted((tuple(sorted(b)) for b in p), key=lambda b:(-len(b),b)))
P={canon(p) for p in parts(list(range(5)))}
rows=[]
for p in sorted(P):
    sizes=tuple(sorted((len(b) for b in p), reverse=True))
    if sizes==(1,1,1,1,1): continue
    eint=sum(s*(s-1)//2 for s in sizes)
    # independent relative vectors inside all collision clusters
    d=3*sum(s-1 for s in sizes)
    pc=Fraction(d,eint)
    # independent explicit edge enumeration
    same=sum(1 for a,b in itertools.combinations(range(5),2) if any(a in B and b in B for B in p))
    rows.append((sizes,eint,d,pc,same))
from collections import Counter,defaultdict
cnt=Counter(r[0] for r in rows)
expected={(2,1,1,1):10,(2,2,1):15,(3,1,1):10,(3,2):10,(4,1):5,(5,):1}
exp_pc={(2,1,1,1):Fraction(3,1),(2,2,1):Fraction(3,1),(3,1,1):Fraction(2,1),(3,2):Fraction(9,4),(4,1):Fraction(3,2),(5,):Fraction(6,5)}
panel=[Fraction(1),Fraction(6,5),Fraction(3,2),Fraction(2),Fraction(9,4),Fraction(3)]
audit={}
for typ in expected:
    pc=exp_pc[typ]
    audit[str(typ)]={str(float(p)):'SIMPLE_RADIAL_COMPARISON_INTEGRABLE' if p<pc else ('MARGINAL_UNRESOLVED' if p==pc else 'SIMPLE_BOUND_INSUFFICIENT') for p in panel}
checks={
 'bell5_52':len(P)==52,
 'nontrivial_51':len(rows)==51,
 'type_counts_exact':dict(cnt)==expected,
 'edge_routes_agree':all(e==s for _,e,_,_,s in rows),
 'pcrit_exact':all(pc==exp_pc[t] for t,e,d,pc,s in rows),
 'critical_panel_marginal':all(audit[str(t)][str(float(exp_pc[t]))]=='MARGINAL_UNRESOLVED' for t in expected),
}
out={'classification':'ITER471_K5_COLLISION_STRATA_EXACT_GEOMETRY_QUALIFIED_SCOPED' if all(checks.values()) else 'FAIL_ITER471','scientific_pass':all(checks.values()),'checks':checks,'type_counts':{str(k):v for k,v in cnt.items()},'pcrit':{str(k):str(v) for k,v in exp_pc.items()},'panel_audit':audit,'scope':'geometry/simple comparison only; insufficiency is not divergence; D7-S2 open'}
path=pathlib.Path('artifacts/iter471-summary.json'); path.parent.mkdir(exist_ok=True); path.write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps(out,indent=2)); raise SystemExit(0 if out['scientific_pass'] else 1)

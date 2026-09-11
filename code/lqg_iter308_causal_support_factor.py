#!/usr/bin/env python3
import itertools, json, pathlib

p=json.load(open('benchmarks/lqg_iter308_causal_support_pole_cancellation.json'))
edges=list(itertools.combinations(range(5),2))
rows=[]; class_counts={'0_5':0,'1_4':0,'2_3':0}; ok=True
for tail in itertools.product((-1,1), repeat=4):
    sig=(1,)+tail
    nminus=sum(1 for s in sig if s<0)
    minority=min(nminus,5-nminus)
    cls={0:'0_5',1:'1_4',2:'2_3'}[minority]
    class_counts[cls]+=1
    prod=1
    for a,b in edges:
        prod*=-(sig[a]*sig[b])
    ok &= (prod==1)
    rows.append({'sigma':list(sig),'class':cls,'leading_factor':prod})
ok &= (len(rows)==16 and class_counts=={'0_5':1,'1_4':5,'2_3':10} and
       p['prospectively_frozen_claims']['unit_weight_causal_sum_leading_factor']==16)
out={'probe':'causal_support_factor','pass':bool(ok),'iteration':308,
     'inequivalent_causal_sectors':len(rows),'class_counts':class_counts,
     'leading_factor_values':sorted(set(r['leading_factor'] for r in rows)),
     'unit_weight_sum':sum(r['leading_factor'] for r in rows),'rows':rows}
pathlib.Path('build/lqg-iter308').mkdir(parents=True,exist_ok=True)
pathlib.Path('build/lqg-iter308/causal_support_factor.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if not ok: raise SystemExit(1)

#!/usr/bin/env python3
import itertools, json, math, pathlib
p=json.load(open('benchmarks/lqg_iter312_partial_diagonal_causal_sign_cancellation.json'))
nodes=range(5)
sectors=[(1,)+tail for tail in itertools.product((-1,1),repeat=4)]
rows=[]; ok=True
for s in (3,4,5):
  for S in itertools.combinations(nodes,s):
    for sig in sectors:
      direct=1
      for a,b in itertools.combinations(S,2): direct*=-(sig[a]*sig[b])
      formula=(-1)**math.comb(s,2)
      for a in S: formula*=sig[a]**(s-1)
      good=(direct==formula)
      ok &= good
      rows.append({'s':s,'S':list(S),'sigma':list(sig),'factor':direct,'pass':good})
ok &= p['prospectively_frozen_claims']['subset_sign_formula']=='F_S=(-1)^C(s,2)*product_{a in S} sigma_a^(s-1)'
out={'probe':'subset_sign_identity','pass':bool(ok),'iteration':312,'checked_rows':len(rows),
     'formula':'F_S=(-1)^C(s,2) product_a sigma_a^(s-1)',
     'consequences':{'s3':'-1 independent of sigma','s4':'product sigma_a over S','s5':'+1 independent of sigma'}}
pathlib.Path('build/lqg-iter312').mkdir(parents=True,exist_ok=True)
pathlib.Path('build/lqg-iter312/subset_sign_identity.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if not ok: raise SystemExit(1)

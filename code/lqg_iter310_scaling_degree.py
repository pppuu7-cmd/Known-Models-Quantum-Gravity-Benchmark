#!/usr/bin/env python3
import json, pathlib
p=json.load(open('benchmarks/lqg_iter310_scaling_degree_extension.json'))
homogeneous_power=p['prospectively_frozen_claims']['leading_homogeneous_power']
sd=-homogeneous_power
d=p['prospectively_frozen_claims']['relative_dimension']
div=sd-d
ok=(homogeneous_power==-20 and sd==20 and d==12 and div==8 and
    p['prospectively_frozen_claims']['local_scaling_degree']==20 and
    p['prospectively_frozen_claims']['degree_of_divergence']==8)
out={'probe':'scaling_degree','pass':bool(ok),'iteration':310,
     'leading_homogeneity':homogeneous_power,'scaling_degree':sd,'relative_dimension':d,
     'degree_of_divergence':div,'rule':'homogeneous degree -p implies scaling degree p'}
pathlib.Path('build/lqg-iter310').mkdir(parents=True,exist_ok=True)
pathlib.Path('build/lqg-iter310/scaling_degree.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if not ok: raise SystemExit(1)

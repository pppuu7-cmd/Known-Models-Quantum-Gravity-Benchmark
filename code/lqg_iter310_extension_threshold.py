#!/usr/bin/env python3
import json, pathlib
p=json.load(open('benchmarks/lqg_iter310_scaling_degree_extension.json'))
c=p['prospectively_frozen_claims']
sd=c['local_scaling_degree']; d=c['relative_dimension']; degree=sd-d
exists=(sd<10**9)
unique=(sd<d)
max_order=max(0,int(degree))
ok=(exists and not unique and max_order==8 and c['same_scaling_degree_extension_exists'] and
    not c['same_scaling_degree_extension_unique'] and c['max_local_delta_derivative_order']==8)
out={'probe':'extension_threshold','pass':bool(ok),'iteration':310,'scaling_degree':sd,'dimension':d,
     'extension_exists':exists,'extension_unique':unique,'max_delta_derivative_order':max_order,
     'theorem_branch':'finite sd >= d: same-scaling-degree extensions exist but are nonunique'}
pathlib.Path('build/lqg-iter310').mkdir(parents=True,exist_ok=True)
pathlib.Path('build/lqg-iter310/extension_threshold.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if not ok: raise SystemExit(1)

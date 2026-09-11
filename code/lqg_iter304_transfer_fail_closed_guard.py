#!/usr/bin/env python3
import json, pathlib
p=json.load(open('benchmarks/lqg_iter304_toller_finiteness_transfer.json'))
c=p['prospectively_frozen_claims']
ok=((not c['automatic_standard_theorem_transfer_ready']) and
    (not c['causal_vertex_divergence_proven']) and
    (not c['causal_vertex_finiteness_proven']))
out={'probe':'transfer_fail_closed_guard','pass':bool(ok),'iteration':304,
     'automatic_transfer_ready':False,
     'causal_vertex_finiteness_proven':False,
     'causal_vertex_divergence_proven':False,
     'required_next_object':'explicit Toller-kernel integrability/decay bound or theorem extending the applicable EPRL finiteness class',
     'tested_claim':'applicability gap remains BLOCKED/undefined rather than PASS-finite or FAIL-divergent'}
pathlib.Path('build/lqg-iter304').mkdir(parents=True,exist_ok=True)
pathlib.Path('build/lqg-iter304/transfer_fail_closed_guard.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if not ok: raise SystemExit(1)

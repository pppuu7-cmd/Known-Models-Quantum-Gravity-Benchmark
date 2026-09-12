#!/usr/bin/env python3
from __future__ import annotations
import glob,json
from pathlib import Path
rows=[]
for fn in sorted(glob.glob('iter405-results/**/*.json',recursive=True)): rows.append(json.loads(Path(fn).read_text()))
lanes={r['lane']:r for r in rows if 'lane' in r}; expected={'reduction_scope','identity_doublecount','tgft_gravity_observable','continuum_transfer'}
ok=set(lanes)==expected and all((not r['pass']) and (not r['terminal']) and (not r['scientific_fail']) for r in lanes.values())
out={'iteration':405,'family':'GFT_TENSOR_MODELS','complete':set(lanes)==expected,'lane_count':len(lanes),'family_terminal':False,'coverage_status_after':'PARTIAL_SUBFAMILY_ONLY','classification':'PASS_GFT_FRONTIER_DISCRIMINATOR__INDEPENDENT_TGFT_REMAINDER_LOCALIZED__NO_FALSE_REDUCTION' if ok else 'INCOMPLETE_OR_CONTRACT_VIOLATION','D2':'NOT_CLOSED_COVERAGE_AND_OBJECTS','D4':'PARTIAL_GLOBAL_NOT_CLOSED','D7':'NOT_CLOSED_NOT_YET_AUTHORIZED','candidate_gravity_activation':False,'lanes':lanes}
Path('iter405-summary.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,sort_keys=True))
if not ok: raise SystemExit(2)

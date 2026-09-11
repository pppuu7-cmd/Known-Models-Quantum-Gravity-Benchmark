#!/usr/bin/env python3
import json
from pathlib import Path
files=sorted(Path('iter333-results').glob('**/*.json'))
if len(files)!=2: raise SystemExit(f'expected 2 files, got {len(files)}')
rows=[json.loads(p.read_text()) for p in files]
by={r['kind']:r for r in rows}
if set(by)!={'k4','k3'}: raise SystemExit(f'coverage mismatch {set(by)}')
assert by['k4']['raw_strata_count']==5 and by['k4']['s5_orbit_count']==1 and by['k4']['stabilizer_size']==24
assert by['k3']['raw_strata_count']==10 and by['k3']['s5_orbit_count']==1 and by['k3']['stabilizer_size']==12
summary={
 'iteration':333,
 'classification':'PASS_SCOPED_CROSS_FACE_S5_TRANSPORT_REDUCES_15_LABELED_STRATA_TO_TWO_NORMALIZATION_ORBITS',
 'raw_labeled_strata':15,
 'stratum_type_orbits':2,
 'k4':{'labeled':5,'orbit_count':1,'canonical_missing_new_first_jet_rank':5},
 'k3':{'labeled':10,'orbit_count':1,'canonical_missing_new_first_jet_rank':3,'canonical_missing_new_second_jet_rank':9},
 'interpretation':'S5 covariance forbids treating all 15 labeled lower strata as unrelated normalization laws. The unresolved burden is instead canonical orbit-level jet data transported equivariantly: K4 needs the five new first-jet directions from Iter332; K3 needs three new first-jet plus nine new second-jet directions. This symmetry reduction does not supply their values.',
 'source_closure':False,
 'scope_guard':'Candidate centered-stratum/S5 consistency result only. No source-defined forest/Haar glue was constructed, no unique extension proved, LQG remains partial/blocked and D7 remains unauthorized.',
 'rows':rows,
}
Path('iter333-summary.json').write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n'); print(json.dumps(summary,sort_keys=True))

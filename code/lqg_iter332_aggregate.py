#!/usr/bin/env python3
import json
from pathlib import Path

files=sorted(Path('iter332-results').glob('**/*.json'))
if len(files)!=2:
    raise SystemExit(f'expected 2 result files, found {len(files)}')
rows=[json.loads(p.read_text()) for p in files]
by={r['kind']:r for r in rows}
if set(by)!={'k4','k3'}:
    raise SystemExit(f'coverage mismatch: {set(by)}')
if by['k4']['value_only_rank']!=11 or by['k4']['value_plus_first_jet_rank']!=16:
    raise SystemExit('K4 rank regression')
if by['k3']['value_only_rank']!=4 or by['k3']['value_plus_first_jet_rank']!=7 or by['k3']['value_plus_first_plus_second_jet_rank']!=16:
    raise SystemExit('K3 rank regression')
summary={
    'iteration':332,
    'classification':'PASS_SCOPED_MINIMUM_NORMALIZATION_INFORMATION_LOWER_BOUNDS',
    'k4_minimum_new_rank_after_values':5,
    'k3_minimum_new_rank_first_jet_after_values':3,
    'k3_minimum_new_rank_second_jet_after_lower_layers':9,
    'interpretation':'Any source-defined prescription that claims to uniquely fix the explicit 16D K5 candidate ambiguity through these centered-stratum channels must supply enough independent normalization information to realize these rank increments.',
    'scope_guard':'Necessary rank information in the Iter330 candidate restriction model; not sufficient for a physical forest-compatible extension, not a counterterm count, no LQG terminal promotion, D7 remains unauthorized.',
    'rows':rows,
}
Path('iter332-summary.json').write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n')
print(json.dumps(summary,sort_keys=True))

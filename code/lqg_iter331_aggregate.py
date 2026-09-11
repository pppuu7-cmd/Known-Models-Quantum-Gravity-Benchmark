#!/usr/bin/env python3
import json
from pathlib import Path

files = sorted(Path('iter331-results').glob('**/*.json'))
if len(files) != 3:
    raise SystemExit(f'expected 3 source audit JSON files, found {len(files)}')
rows = [json.loads(p.read_text()) for p in files]
ids = {r['source_id'] for r in rows}
expected = {
    'bcg_causal_vertex_2601_23162',
    'bcg_toller_2604_24945',
    'beltran_generalized_2603_22661_v2',
}
if ids != expected:
    raise SystemExit(f'source coverage mismatch: {ids} != {expected}')
if any(r['closes_iter330_gate'] for r in rows):
    raise SystemExit('unexpected source-defined closure; manual scientific review required')
summary = {
    'iteration': 331,
    'audited_sources': sorted(ids),
    'source_count': len(rows),
    'iter330_required_jet_detectability': {
        'k4_first_normal_jet': 'rank-16 injective detector from Iter330',
        'k3_second_normal_jet': 'rank-16 injective detector from Iter330',
    },
    'source_defined_normalization_found': False,
    'source_defined_forest_glue_found': False,
    'classification': 'BLOCKED_SOURCE_NORMALIZATION_NOT_FOUND_IN_AUDITED_CAUSAL_SPINFOAM_SOURCES',
    'scope_guard': 'Absence in the audited sources is not a theorem that no distributional extension or normalization can exist. No LQG terminal FAIL and no D7 promotion is authorized.',
    'next_gate': 'Obtain a published/source-defined causal forest or Haar-gluing normalization that fixes the required K4-first and/or K3-second normal jets on the explicit 16D K5 invariant basis; only then test finite normalized causal vertex and full lambda_f-weighted stack cutoff control.',
    'rows': rows,
}
Path('iter331-summary.json').write_text(json.dumps(summary, indent=2, sort_keys=True) + '\n')
print(json.dumps(summary, sort_keys=True))

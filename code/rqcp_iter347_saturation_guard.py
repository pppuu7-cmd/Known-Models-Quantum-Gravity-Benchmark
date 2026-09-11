#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

STATE=Path('paper_iv/PAPER_IV_D7_READINESS_STATE.json')
COVERAGE=Path('protocol/PAPER_IV_MAJOR_FRAMEWORK_COVERAGE_CONTRACT.json')
s=json.loads(STATE.read_text())
c=json.loads(COVERAGE.read_text())
r=s['stages']['D7-S2']['latest_reopen']
q=r['quantified_resource_axis']
assert r['family']=='RELATIONAL_QUANTUM_CAUSAL_PROCESSES'
assert q['cutoff24_to28_G_relative_change'] < 2e-8
assert q['cutoff24_to28_gap_relative_change'] < 2e-9
assert q['cutoff24_to28_G_gap2_relative_change'] < 2e-8
blocker=r['refined_blocker']
assert 'ALL_BAND' in blocker and 'BACKGROUND_INDEPENDENT' in blocker and 'HILBERT_CUTOFF' in blocker
row=next(x for x in c['tier1_required_rows'] if x['id']=='RELATIONAL_QUANTUM_CAUSAL_PROCESSES')
mr=row['minimum_resolution']
assert 'all-band' in mr.lower() and 'background-independent' in mr.lower()
out={
 'iteration':347,
 'classification':'PASS_PROCESS_GUARD__RQCP_HIGH_CUTOFF_NUMERICAL_AXIS_ALREADY_SATURATED__FURTHER_CUTOFF_ONLY_COMPUTE_NOT_AUTHORIZED_WITHOUT_NEW_SOURCE_OR_MODEL_IDENTITY',
 'canonical_high_cutoff_evidence':q,
 'current_family_status':row['coverage_status'],
 'remaining_blocker':blocker,
 'compute_policy':'Do not launch another RQCP oscillator-cutoff-only extension. Reopen only for a source-defined all-band/background-independent autonomous gravity parent or a genuinely independent resource axis with frozen authority.',
 'scope_guard':['PROCESS_SATURATION_GUARD_NOT_SCIENTIFIC_FAMILY_RESULT','NO_BLOCKED_TO_FAIL_CONVERSION','NO_D7_PROMOTION']
}
Path('iter347-rqcp-saturation-guard.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,sort_keys=True))

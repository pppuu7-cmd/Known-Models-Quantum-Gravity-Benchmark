#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

PUBLISHED={
 "ground_energy":0.8092650762452466,
 "mass_gap":0.4863395672466658,
 "connected_static_four_response":-3.3257587842732006,
 "mixed_geometry_matter_response":13.102173996407302,
 "geometry_kinetic_coefficient_B":2.5524530086081993,
 "Newton_response_G":23.200280752211107,
 "dimensionless_gravity_number_G_gap2":5.487473657582965,
}
rows=[json.loads(p.read_text()) for p in sorted(Path('iter342b-343-results').rglob('cutoff-*.json'))]
rows.sort(key=lambda r:r['cutoff'])
assert [r['cutoff'] for r in rows]==[6,8,10,12,14,16,18,20]
receipts=list(Path('iter342b-343-results').rglob('portability-receipt.json'))
assert len(receipts)==1,receipts
receipt=json.loads(receipts[0].read_text())
assert receipt['scientific_closure_checker_success'] is True
assert receipt['upstream_release_integrity_exit_code'] != 0
assert receipt['max_relative_drift'] < 5e-13
cut8=next(r for r in rows if r['cutoff']==8)
cut8_errors={}
for k,v in PUBLISHED.items():
    got=float(cut8['metrics'][k]); rel=abs(got-v)/max(abs(v),1e-30)
    cut8_errors[k]=rel
    assert rel < 5e-13,(k,got,v,rel)
metrics=list(PUBLISHED)
changes=[]
for a,b in zip(rows[:-1],rows[1:]):
    rec={'from':a['cutoff'],'to':b['cutoff'],'relative_changes':{}}
    for k in metrics:
        x=float(a['metrics'][k]); y=float(b['metrics'][k])
        rec['relative_changes'][k]=abs(y-x)/max(abs(y),1e-30)
    changes.append(rec)
last=changes[-1]
prev=changes[-2]
summary={
 'iteration_bundle':'342b-343',
 'external_repository':'Amordia/rqcp-toward-quantum-gravity',
 'external_scientific_payload_sha':'7c749f5f0aeefe07a897123295f3647fdc56d868',
 'scientific_closure_checker_reproduced':True,
 'upstream_release_integrity_strict_pass':False,
 'upstream_strict_fail_keys':receipt['strict_tolerance_fail_keys'],
 'max_platform_relative_drift':receipt['max_relative_drift'],
 'cutoff8_published_headlines_reproduced_within_rel_5e_13':True,
 'cutoff8_relative_errors':cut8_errors,
 'cutoff_matrix':[r['cutoff'] for r in rows],
 'hilbert_dimensions':[r['hilbert_dimension'] for r in rows],
 'consecutive_relative_changes':changes,
 'last_step_18_to_20_relative_changes':last['relative_changes'],
 'previous_step_16_to_18_relative_changes':prev['relative_changes'],
 'maximum_last_step_relative_change':max(last['relative_changes'].values()),
 'classification':'PASS_SCOPED_RQCP_SCIENTIFIC_REPRODUCTION_WITH_QUANTIFIED_PLATFORM_DRIFT_PLUS_OSCILLATOR_CUTOFF_STRESS__UPSTREAM_ABS_5E_15_RELEASE_CHECK_NOT_PORTABLE_ON_THIS_RUNNER',
 'family_status':'PARTIAL_SUBFAMILY_ONLY',
 'd7_promotion_authorized':False,
 'scope_guard':[
   'DO_NOT_LABEL_UPSTREAM_MAKE_VALIDATE_AS_PASS',
   'SCIENTIFIC_CHECKER_PASSED_AT_EXACT_FROZEN_SHA',
   'UPSTREAM_RELEASE_INTEGRITY_FAILURE_IS_RECORDED',
   'CUTOFF_STRESS_REMOVES_ONLY_LOCAL_OSCILLATOR_TRUNCATION_WITH_FIXED_TWO_MODE_SPATIAL_BAND',
   'NO_ALL_BAND_QFT_CLAIM','NO_AUTONOMOUS_GRAVITY_SECTOR_CLAIM','NO_PARENT_FAMILY_TERMINALIZATION','NO_D7_PROMOTION'
 ]
}
Path('iter342b-343-summary.json').write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n')
print(json.dumps(summary,sort_keys=True))

#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path

KEYS = [
    "ground_energy",
    "mass_gap",
    "connected_static_four_response",
    "mixed_geometry_matter_response",
    "geometry_kinetic_coefficient_B",
    "Newton_response_G",
    "dimensionless_gravity_number_G_gap2",
    "final_scale_factor",
]

ap=argparse.ArgumentParser()
ap.add_argument('--frozen',required=True)
ap.add_argument('--regenerated',required=True)
ap.add_argument('--release-exit',required=True,type=int)
ap.add_argument('--output',required=True)
a=ap.parse_args()
f=json.loads(Path(a.frozen).read_text())['direct_continuum_reference']
r=json.loads(Path(a.regenerated).read_text())['direct_continuum_reference']
rows={}
max_abs=max_rel=0.0
strict_fail=[]
for k in KEYS:
    fv=float(f[k]); rv=float(r[k])
    ae=abs(rv-fv); re=ae/max(abs(fv),1e-30)
    rows[k]={"frozen":fv,"regenerated":rv,"absolute_error":ae,"relative_error":re,"passes_upstream_abs_5e_15":ae<=5e-15}
    max_abs=max(max_abs,ae); max_rel=max(max_rel,re)
    if ae>5e-15: strict_fail.append(k)
assert a.release_exit != 0, "portability audit expected upstream strict release checker to expose platform drift"
assert strict_fail, "expected at least one upstream 5e-15 headline mismatch"
assert max_rel < 5e-13, max_rel
out={
  "iteration":"342b",
  "external_repository":"Amordia/rqcp-toward-quantum-gravity",
  "external_scientific_payload_sha":"7c749f5f0aeefe07a897123295f3647fdc56d868",
  "scientific_closure_checker_success":True,
  "upstream_release_integrity_exit_code":a.release_exit,
  "upstream_abs_tolerance":5e-15,
  "strict_tolerance_fail_keys":strict_fail,
  "headline_drift":rows,
  "max_absolute_drift":max_abs,
  "max_relative_drift":max_rel,
  "classification":"PASS_SCOPED_SCIENTIFIC_CHECK_REPRODUCED__UPSTREAM_RELEASE_INTEGRITY_NOT_PLATFORM_PORTABLE_AT_ABS_5E_15__DRIFT_QUANTIFIED",
  "scope_guard":[
    "UPSTREAM_TOLERANCE_UNCHANGED",
    "EXTERNAL_SHA_UNCHANGED",
    "SCIENTIFIC_CHECKER_MUST_PASS",
    "STRICT_RELEASE_CHECKER_FAILURE_RECORDED_NOT_SUPPRESSED",
    "KMQGB_PORTABILITY_ACCEPTANCE_ONLY_REQUIRES_RELATIVE_DRIFT_LT_5E_13_FOR_THIS_AUDIT",
    "NO_ALL_BAND_QFT_CLAIM",
    "NO_PARENT_FAMILY_TERMINALIZATION",
    "NO_D7_PROMOTION"
  ]
}
Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,sort_keys=True))

#!/usr/bin/env python3
from __future__ import annotations
import json, math
from pathlib import Path

PINNED_SHA = "7c749f5f0aeefe07a897123295f3647fdc56d868"
PUBLISHED = {
    "ground_energy": 0.8092650762452466,
    "mass_gap": 0.4863395672466658,
    "connected_static_four_response": -3.3257587842732006,
    "mixed_geometry_matter_response": 13.102173996407302,
    "geometry_kinetic_coefficient_B": 2.5524530086081993,
    "Newton_response_G": 23.200280752211107,
    "dimensionless_gravity_number_G_gap2": 5.487473657582965,
}

rows=[]
for p in sorted(Path("iter342-343-results").rglob("cutoff-*.json")):
    rows.append(json.loads(p.read_text()))
rows.sort(key=lambda x:x["cutoff"])
assert [r["cutoff"] for r in rows] == [6,8,10,12,14,16,18,20]
assert all(r["external_scientific_payload_sha"] == PINNED_SHA for r in rows)

receipt_files=list(Path("iter342-343-results").rglob("replication-receipt.json"))
assert len(receipt_files)==1
receipt=json.loads(receipt_files[0].read_text())
assert receipt["external_head"] == PINNED_SHA
assert receipt["make_validate_success"] is True
assert receipt["evidence_sha256_before"] == receipt["evidence_sha256_after"]

cut8=next(r for r in rows if r["cutoff"]==8)
cut8_errors={}
for k, ref in PUBLISHED.items():
    got=float(cut8["metrics"][k])
    err=abs(got-ref)
    rel=err/max(abs(ref),1e-30)
    cut8_errors[k]={"absolute":err,"relative":rel}
    assert rel < 5e-13, (k,got,ref,rel)

metrics=list(PUBLISHED)
steps=[]
for lo,hi in zip(rows[:-1],rows[1:]):
    rec={"from_cutoff":lo["cutoff"],"to_cutoff":hi["cutoff"],"relative_changes":{}}
    for k in metrics:
        a=float(lo["metrics"][k]); b=float(hi["metrics"][k])
        rec["relative_changes"][k]=abs(b-a)/max(abs(b),1e-30)
    steps.append(rec)
last=steps[-1]
penultimate=steps[-2]
summary={
    "iteration_bundle":"342-343",
    "external_repository":"Amordia/rqcp-toward-quantum-gravity",
    "external_scientific_payload_sha":PINNED_SHA,
    "exact_external_make_validate_reproduced":True,
    "evidence_byte_stable_under_validation":True,
    "published_cutoff8_headlines_reproduced":True,
    "cutoff_matrix":[r["cutoff"] for r in rows],
    "hilbert_dimensions":[r["hilbert_dimension"] for r in rows],
    "cutoff8_relative_errors":cut8_errors,
    "consecutive_relative_changes":steps,
    "last_step_18_to_20_relative_changes":last["relative_changes"],
    "previous_step_16_to_18_relative_changes":penultimate["relative_changes"],
    "classification":"PASS_SCOPED_INDEPENDENT_RQCP_FIXED_BAND_REPRODUCTION_PLUS_OSCILLATOR_CUTOFF_STRESS__DOES_NOT_REMOVE_FIXED_BAND_OR_DERIVE_GRAVITY_SECTOR",
    "family_status":"PARTIAL_SUBFAMILY_ONLY",
    "d7_promotion_authorized":False,
    "scope_guard":[
        "AUTHOR_FROZEN_PAYLOAD_REPRODUCED_IN_KMQGB_CI",
        "CUTOFF_STRESS_USES_SAME_FIXED_TWO_MODE_BAND_AND_SAME_HAMILTONIAN_PARAMETERS",
        "NO_ALL_BAND_QFT_CLAIM",
        "NO_QUANTUM_METRIC_CLAIM",
        "NO_AUTONOMOUS_GRAVITY_SECTOR_SELECTION_CLAIM",
        "NO_PARENT_FAMILY_TERMINALIZATION"
    ]
}
Path("iter342-343-summary.json").write_text(json.dumps(summary,indent=2,sort_keys=True)+"\n")
print(json.dumps(summary,sort_keys=True))

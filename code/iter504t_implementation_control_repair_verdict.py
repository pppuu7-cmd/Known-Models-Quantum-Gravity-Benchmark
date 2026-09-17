#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path
REPAIR_GATE='ITER504T_IMPLEMENTATION_CONTROL_REPAIR_RERUN_GATE'
REPAIR_PREREG='adc7bfb9df77a90455cac1b0f0cb7255d80c44d5'
ORIGINAL_GATE='ITER504T_LOCAL_DERIVATIVE_ENCLOSURE_CONTRACTION'
SCIENCE_ALLOWED={'ITER504T_LOCAL_D_CERTIFIES_THREE_ROOT_CONTINUOUS_DRIFT_SCOPED','ITER504T_LOCAL_D_INCONCLUSIVE_SCOPED'}
PASS='ITER504T_IMPLEMENTATION_CONTROLS_REPAIRED_AND_RERUN_VALID_SCOPED'
FAIL='ITER504T_IMPLEMENTATION_CONTROL_REPAIR_FAILED_SCOPED'
def load(p):
 raw=Path(p).read_bytes();return json.loads(raw),hashlib.sha256(raw).hexdigest()
def main():
 p=argparse.ArgumentParser();p.add_argument('--aggregate',required=True);p.add_argument('--critic',required=True);p.add_argument('--out',required=True);a=p.parse_args()
 agg,ah=load(a.aggregate);crit,ch=load(a.critic);checks={
  'aggregate_original_gate':agg.get('gate')==ORIGINAL_GATE,
  'critic_original_gate':crit.get('gate')==ORIGINAL_GATE,
  'aggregate_repair_prereg':agg.get('repair_preregistration_commit')==REPAIR_PREREG,
  'critic_repair_prereg':crit.get('repair_preregistration_commit')==REPAIR_PREREG,
  'scientific_classification_original_allowed':agg.get('classification') in SCIENCE_ALLOWED,
  'critic_matches_science':crit.get('classification')==agg.get('classification'),
  'critic_errors_empty':crit.get('critic_errors')==[],
  'cross_environment_exact_decision_agreement':crit.get('cross_environment_exact_decision_agreement') is True,
  'componentwise_parent_inclusion_control_implemented':crit.get('componentwise_parent_inclusion_control_implemented') is True and agg.get('componentwise_parent_inclusion_control_implemented') is True,
  'r_cohort_binding_implemented':crit.get('r_cohort_binding_implemented') is True and agg.get('r_cohort_binding_implemented') is True,
  'all_repair_negative_controls_pass':bool(crit.get('negative_controls')) and all(crit.get('negative_controls',{}).values()),
  'dyadic_validation_retained':crit.get('partition_identity_verified')=='exact_rational_dyadic_cells' and agg.get('partition_identity_verified')=='exact_rational_dyadic_cells',
  'threshold_unchanged':crit.get('threshold_exact')=='1/20' and agg.get('threshold_exact')=='1/20',
  'floor_unchanged':crit.get('robust_floor_exact')=='1' and agg.get('robust_floor_exact')=='1',
  'max_depth_unchanged':crit.get('max_depth')==3,
 }
 classification=PASS if all(checks.values()) else FAIL
 out={'gate':REPAIR_GATE,'repair_preregistration_commit':REPAIR_PREREG,'classification':classification,'scientific_gate':ORIGINAL_GATE,'scientific_classification':agg.get('classification'),'checks':checks,'aggregate_sha256':ah,'critic_sha256':ch,'lane_a_parent_inclusion_stats':crit.get('lane_a_parent_inclusion_stats'),'lane_b_parent_inclusion_stats':crit.get('lane_b_parent_inclusion_stats'),'claim_ceiling':'Implementation validity plus original Iter504T three-root bounded local-D claim ceiling only'}
 payload=json.dumps(out,sort_keys=True,separators=(',',':')).encode();out['repair_payload_sha256']=hashlib.sha256(payload).hexdigest();q=Path(a.out);q.parent.mkdir(parents=True,exist_ok=True);q.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True));return 0 if classification==PASS else 2
if __name__=='__main__':raise SystemExit(main())

#!/usr/bin/env python3
import argparse
from cfs_currents_correction_common import CURRENTS2025,FROZEN_CFS,write_json

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); a=ap.parse_args()
    blocker_open=(not CURRENTS2025['normalized_gravity_correction_tensor'] and not CURRENTS2025['gravity_same_domain_comparator_quotient'])
    pathway=(CURRENTS2025['tensor_hierarchy_increasing_rank'] and CURRENTS2025['generalizes_to_nonabelian_and_gravitation'])
    ok=pathway and blocker_open and FROZEN_CFS['status']=='BLOCKED_MISSING_REQUIRED_OBJECT'
    write_json(a.output,{
      'probe':'cfs_currents_blocker_guard','pass':ok,
      'blocker_still_open':blocker_open,
      'classification':'PASS_HIGH_VALUE_PATHWAY_TOWARD_CFS_CORRECTION_TENSOR__FROZEN_NORMALIZED_GRAVITY_RESIDUAL_OBJECT_STILL_MISSING' if ok else 'FAIL_CFS_BLOCKER_COMPATIBILITY_CONTRACT',
      'boundary':'The paper materially clarifies how a future correction tensor could be constructed, but does not satisfy the frozen reopen condition by itself.'})
    if not ok: raise SystemExit(1)
if __name__=='__main__': main()

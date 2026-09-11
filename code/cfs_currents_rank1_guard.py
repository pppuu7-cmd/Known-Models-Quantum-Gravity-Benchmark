#!/usr/bin/env python3
import argparse
from cfs_currents_correction_common import CURRENTS2025,write_json

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); a=ap.parse_args()
    ok=(CURRENTS2025['systematic_linearized_field_equation_formalism'] and CURRENTS2025['tensor_hierarchy_increasing_rank'] and CURRENTS2025['rank_one_maxwell_explicit'])
    write_json(a.output,{
      'probe':'cfs_currents_rank1_guard','pass':ok,
      'classification':'PASS_EXPLICIT_CFS_CURRENT_FORMALISM_AND_RANK_ONE_MAXWELL_CONTROL' if ok else 'FAIL_CFS_RANK1_CONTROL_CONTRACT',
      'boundary':'The explicit worked control is rank one / electrodynamic, not the gravity correction tensor required by the frozen CFS blocker.'})
    if not ok: raise SystemExit(1)
if __name__=='__main__': main()

#!/usr/bin/env python3
import argparse
from cfs_currents_correction_common import CURRENTS2025,write_json

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); a=ap.parse_args()
    ok=(not CURRENTS2025['rank_two_einstein_explicit'] and CURRENTS2025['rank_two_einstein_expected'] and not CURRENTS2025['higher_rank_new_physics_corrections_explicitly_computed'] and CURRENTS2025['higher_rank_corrections_prospective'])
    write_json(a.output,{
      'probe':'cfs_currents_maturity_guard','pass':ok,
      'classification':'PASS_RANK_TWO_AND_HIGHER_RANK_BOUNDARY__GRAVITY_AND_CORRECTIONS_REMAIN_PROSPECTIVE' if ok else 'FAIL_CFS_MATURITY_SCOPE_CONTRACT',
      'boundary':'Do not promote expected rank-two Einstein structure or prospective higher-rank corrections into an explicit calculated gravity correction tensor.'})
    if not ok: raise SystemExit(1)
if __name__=='__main__': main()

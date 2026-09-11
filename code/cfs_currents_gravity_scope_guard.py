#!/usr/bin/env python3
import argparse
from cfs_currents_correction_common import CURRENTS2025,write_json

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); a=ap.parse_args()
    ok=(CURRENTS2025['generalizes_to_nonabelian_and_gravitation'] and CURRENTS2025['explicit_higher_order_quantum_and_discreteness_corrections_in_scope'])
    write_json(a.output,{
      'probe':'cfs_currents_gravity_scope_guard','pass':ok,
      'classification':'PASS_SYSTEMATIC_CURRENT_FORMALISM_EXTENDS_IN_SCOPE_TO_GRAVITATION_AND_HIGHER_ORDER_CORRECTIONS' if ok else 'FAIL_CFS_GRAVITY_SCOPE_CONTRACT',
      'boundary':'Generality of the method is a pathway result; it is not evidence that a gravity-specific higher-rank correction tensor has already been evaluated.'})
    if not ok: raise SystemExit(1)
if __name__=='__main__': main()

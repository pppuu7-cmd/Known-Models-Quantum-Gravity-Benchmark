#!/usr/bin/env python3
import argparse
from lqg_physical_state_link_common import YANG2021,CHAIN,write_json

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); a=ap.parse_args()
    scoped=(YANG2021['model']=='generalized_Euclidean_EPRL' and not YANG2021['lorentzian_same_realization_certificate'])
    write_json(a.output,{
      'probe':'lqg_physical_state_signature_guard','pass':scoped,
      'model_signature_scope':YANG2021['model'],
      'lorentzian_same_realization_certificate':YANG2021['lorentzian_same_realization_certificate'],
      'classification':'PASS_EUCLIDEAN_PHYSICAL_STATE_LINK__LORENTZIAN_SAME_REALIZATION_MAP_MISSING' if scoped else 'FAIL_SIGNATURE_SCOPE_CONTRACT',
      'boundary':'The Euclidean EPRL rigging-map result cannot be silently promoted to the Lorentzian 2026 complete-stack realization.'})
    if not scoped: raise SystemExit(1)
if __name__=='__main__': main()

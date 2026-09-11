#!/usr/bin/env python3
import argparse
from lqg_entropy_observable_common import HAN_ENTROPY_2026,ITER283,write_json

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); a=ap.parse_args()
    anchor=(HAN_ENTROPY_2026['signature']=='Lorentzian' and HAN_ENTROPY_2026['state_origin'].startswith('dynamically_generated'))
    transport_missing=(not HAN_ENTROPY_2026['explicit_uv_to_gr_observable_transport'] and ITER283['missing_normalized_observable_transport'])
    ok=anchor and transport_missing
    write_json(a.output,{
      'probe':'lqg_entropy_uv_ir_transport_guard','pass':ok,
      'observable_anchor':anchor,'same_realization_transport_ready':False,
      'classification':'PASS_HIGH_VALUE_LORENTZIAN_GRAVITATIONAL_OBSERVABLE_ANCHOR__UV_IR_TRANSPORT_STILL_MISSING' if ok else 'FAIL_OBSERVABLE_TRANSPORT_SCOPE_CONTRACT',
      'boundary':'The entropy is a material Lorentzian dynamical gravity observable in the stack sector, but no published normalized observable transport through the Iter283 small-spin UV to large-spin Einstein endpoint is established.'})
    if not ok: raise SystemExit(1)
if __name__=='__main__': main()

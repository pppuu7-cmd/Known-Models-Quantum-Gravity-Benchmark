#!/usr/bin/env python3
import argparse
from lqg_stack_uv_entropy_common import UV,ENTROPY,ITER283,write_json

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); a=ap.parse_args()
    anchor=(ENTROPY['lorentzian_observable_anchor'] and ENTROPY['bh_normalized_after_selection'] and UV['spinfoam_stack'])
    ready=ENTROPY['full_uv_fixed_point_to_gr_observable_flow_computed'] and ITER283['same_realization_transport_ready']
    ok=anchor and not ready
    write_json(a.output,{'probe':'same_stack_observable_transport_guard','pass':ok,
      'same_stack_observable_anchor':anchor,'terminal_transport_ready':False,
      'classification':'PASS_OBSERVABLE_ANCHOR_INSIDE_SHARED_STACK_ARCHITECTURE__UV_TO_GR_OBSERVABLE_TRANSPORT_STILL_OPEN' if ok else 'FAIL_SAME_STACK_OBSERVABLE_TRANSPORT_CONTRACT',
      'boundary':'The entropy observable is closer to the UV realization than a generic external observable, but has not been propagated through the UV-to-Einstein trajectory.'})
    if not ok: raise SystemExit(1)
if __name__=='__main__': main()

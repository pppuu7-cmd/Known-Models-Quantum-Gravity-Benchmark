#!/usr/bin/env python3
import argparse
from lqg_physical_state_link_common import YANG2021,CHAIN,write_json

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); a=ap.parse_args()
    positive=(YANG2021['implied_rigging_map'] and CHAIN['iter283_shared_lqg_parent'])
    missing=(not CHAIN['explicit_2021_to_2017_2026_state_parameter_signature_map'] and not CHAIN['explicit_2021_rigging_map_transport_across_uv_ir_chain'] and not YANG2021['normalized_gravity_observable'])
    ok=positive and missing
    write_json(a.output,{
      'probe':'lqg_physical_state_chain_guard','pass':ok,
      'physical_state_component_positive':positive,
      'explicit_state_parameter_signature_map':CHAIN['explicit_2021_to_2017_2026_state_parameter_signature_map'],
      'explicit_rigging_map_transport_across_uv_ir_chain':CHAIN['explicit_2021_rigging_map_transport_across_uv_ir_chain'],
      'normalized_gravity_observable':YANG2021['normalized_gravity_observable'],
      'classification':'PASS_HIGH_VALUE_PHYSICAL_STATE_COMPONENT__NOT_YET_COMPATIBLE_SAME_REALIZATION_UV_IR_CHAIN' if ok else 'FAIL_CHAIN_SCOPE_CONTRACT',
      'boundary':'The 2021 rigging-map result adds a valuable physical-state component but does not close the Iter283 amplitude/signature/parameter/observable transport gaps.'})
    if not ok: raise SystemExit(1)
if __name__=='__main__': main()

#!/usr/bin/env python3
import argparse
from lqg_wick_bridge_common import WICK2021,CHAIN,write_json

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); a=ap.parse_args()
    structural=(WICK2021['maps_euclidean_lorentzian_vertex_amplitudes'] and WICK2021['vertex_level_relation'])
    terminal_ready=(CHAIN['explicit_yang_to_han_state_map'] and CHAIN['explicit_real_gamma_preserving_transport'] and CHAIN['explicit_vertex_to_complete_stack_transport'])
    ok=structural and not terminal_ready
    write_json(a.output,{
      'probe':'lqg_wick_chain_compatibility_guard','pass':ok,
      'structural_signature_bridge':structural,'same_realization_chain_ready':False,
      'classification':'PASS_HIGH_VALUE_SIGNATURE_BRIDGE_COMPONENT__NO_YANG_TO_HAN_REAL_GAMMA_STATE_AND_STACK_TRANSPORT' if ok else 'FAIL_WICK_CHAIN_COMPATIBILITY_CONTRACT',
      'boundary':'The Wick map narrows the signature gap but does not close the Iter284→Iter283/285 physical-state, real-gamma, complete-stack transport gap.'})
    if not ok: raise SystemExit(1)
if __name__=='__main__': main()

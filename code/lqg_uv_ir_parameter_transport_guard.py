#!/usr/bin/env python3
import argparse
from lqg_uv_ir_bridge_common import SOURCES,BRIDGE,write_json

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); a=ap.parse_args()
    ir=SOURCES['ir_gr']; st=SOURCES['stack_cutoff']
    has_ir_parameters=all(x in ir['limits'] for x in ['lambda_to_infinity','delta_to_zero']) and ir['running_scale_direction']=='mu_to_zero_IR'
    has_uv_cutoff=(st['internal_area_cutoff_limit']=='cutoff_to_infinity')
    explicit_map=BRIDGE['explicit_lambda_delta_mu_to_stack_cutoff_parameter_map']
    ok=has_ir_parameters and has_uv_cutoff and not explicit_map
    write_json(a.output,{
      'probe':'lqg_uv_ir_parameter_transport_guard','pass':ok,
      'ir_parameters_and_hierarchy':{'limits':ir['limits'],'running_scale':ir['running_scale_direction'],'hierarchy':ir['hierarchy']},
      'uv_stack_cutoff':st['internal_area_cutoff_limit'],
      'explicit_parameter_map':explicit_map,
      'classification':'PASS_DISTINCT_REGULATOR_LIMITS_IDENTIFIED__PARAMETER_TRANSPORT_MAP_MISSING' if ok else 'FAIL_PARAMETER_TRANSPORT_CONTRACT',
      'boundary':'The published 2017 lambda/delta/mu limit cannot be silently identified with the 2026 internal-area cutoff or UV fixed-point coordinates without an explicit transport map.'})
    if not ok: raise SystemExit(1)
if __name__=='__main__': main()

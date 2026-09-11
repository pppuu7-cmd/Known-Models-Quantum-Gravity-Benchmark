#!/usr/bin/env python3
import argparse
from lqg_uv_ir_bridge_common import SOURCES,BRIDGE,write_json

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); a=ap.parse_args()
    ir=SOURCES['ir_gr']; uv=SOURCES['uv_fixed_point']
    endpoints=(ir['target']=='continuum_Einstein_equation' and uv['target']=='fundamental_continuum_UV_fixed_point')
    normalized=(ir['normalized_operational_gravity_observable'] or uv['normalized_operational_gravity_observable'] or BRIDGE['explicit_normalized_observable_transport_across_bridge'])
    ok=endpoints and not normalized
    write_json(a.output,{
      'probe':'lqg_uv_ir_observable_target_guard','pass':ok,
      'ir_target':ir['target'],'uv_target':uv['target'],
      'normalized_operational_observable_bridge_available':normalized,
      'classification':'PASS_MATERIAL_UV_AND_GR_ENDPOINTS_IDENTIFIED__NORMALIZED_OBSERVABLE_TRANSPORT_MISSING' if ok else 'FAIL_OBSERVABLE_TARGET_CONTRACT',
      'boundary':'Derivation of the continuum Einstein equation is a material GR-limit endpoint, but it is not itself the normalized same-domain operational observable/comparator certificate required for KMQGB family terminalization.'})
    if not ok: raise SystemExit(1)
if __name__=='__main__': main()

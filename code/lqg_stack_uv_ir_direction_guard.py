#!/usr/bin/env python3
import argparse
from lqg_stack_uv_entropy_common import UV,ENTROPY,ITER283,write_json

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); a=ap.parse_args()
    directional=(UV['uv_small_spin'] and ENTROPY['semiclassical_root_complex_direction_reported'] and ITER283['gr_endpoint'])
    ready=(UV['gr_ir_large_spin_transport_explicit'] and ENTROPY['full_uv_fixed_point_to_gr_observable_flow_computed'])
    ok=directional and not ready
    write_json(a.output,{'probe':'uv_ir_regime_direction_guard','pass':ok,
      'directional_uv_ir_structure':directional,'continuous_transport_ready':False,
      'classification':'PASS_UV_SMALL_SPIN_AND_SEMICLASSICAL_IR_DIRECTION_IDENTIFIED__CONTINUOUS_TRAJECTORY_NOT_COMPUTED' if ok else 'FAIL_UV_IR_DIRECTION_CONTRACT',
      'boundary':'Endpoint/regime orientation is stronger than before, but an explicit controlled trajectory with common parameters and propagated errors is still absent.'})
    if not ok: raise SystemExit(1)
if __name__=='__main__': main()

#!/usr/bin/env python3
import argparse
from lqg_uv_ir_bridge_common import SOURCES,BRIDGE,write_json

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); a=ap.parse_args()
    ir=SOURCES['ir_gr']; uv=SOURCES['uv_fixed_point']
    opposite=(ir['spin_regime']=='large_spin' and uv['spin_regime']=='small_spin_UV_condensation')
    explicit=BRIDGE['explicit_small_spin_UV_to_large_spin_semiclassical_trajectory']
    ok=opposite and not explicit
    write_json(a.output,{
      'probe':'lqg_uv_ir_limit_orientation_guard','pass':ok,
      'ir_spin_regime':ir['spin_regime'],'uv_spin_regime':uv['spin_regime'],
      'ir_running_scale_direction':ir['running_scale_direction'],'uv_leading_fixed_point_regime':uv['leading_fixed_point_regime'],
      'explicit_uv_to_ir_trajectory':explicit,
      'classification':'PASS_ENDPOINTS_IN_DISTINCT_SPIN_REGIMES__EXPLICIT_UV_TO_IR_TRAJECTORY_MISSING' if ok else 'FAIL_LIMIT_ORIENTATION_CONTRACT',
      'boundary':'A UV small-spin/topological endpoint and an IR-refinement large-spin Einstein endpoint are not a trajectory merely because they occur in one broad theory family.'})
    if not ok: raise SystemExit(1)
if __name__=='__main__': main()

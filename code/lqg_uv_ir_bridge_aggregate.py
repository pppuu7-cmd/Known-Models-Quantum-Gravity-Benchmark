#!/usr/bin/env python3
import argparse,json
from pathlib import Path
from lqg_uv_ir_bridge_common import SOURCES,BRIDGE,write_json
EXPECTED={
 'family':'lqg_uv_ir_family_identity_guard',
 'limits':'lqg_uv_ir_limit_orientation_guard',
 'parameters':'lqg_uv_ir_parameter_transport_guard',
 'observable':'lqg_uv_ir_observable_target_guard'
}
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--input-dir',required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
    root=Path(a.input_dir); rows={}
    for label,probe in EXPECTED.items():
        r=json.loads((root/f'{label}.json').read_text())
        if r.get('probe')!=probe or not r.get('pass'): raise SystemExit(f'bad probe {label}')
        rows[label]=r
    bridge_ready=all([
      BRIDGE['explicit_same_realization_identification_between_2017_and_2026_amplitudes'],
      BRIDGE['explicit_lambda_delta_mu_to_stack_cutoff_parameter_map'],
      BRIDGE['explicit_small_spin_UV_to_large_spin_semiclassical_trajectory'],
      BRIDGE['explicit_normalized_observable_transport_across_bridge']
    ])
    write_json(a.output,{
      'probe':'lqg_uv_ir_bridge_iter283_aggregate',
      'all_four_independent_guards_pass':True,
      'shared_parent_family':BRIDGE['shared_broad_parent_family'],
      'material_positive_endpoints':BRIDGE['both_have_material_positive_endpoints'],
      'same_realization_terminal_bridge_ready':bridge_ready,
      'family_identity_result':rows['family']['classification'],
      'limit_orientation_result':rows['limits']['classification'],
      'parameter_transport_result':rows['parameters']['classification'],
      'observable_target_result':rows['observable']['classification'],
      'classification':'HIGH_VALUE_UV_AND_GR_ENDPOINTS_IN_SHARED_LQG_PARENT__NO_EXPLICIT_SAME_REALIZATION_PARAMETER_AND_OBSERVABLE_TRANSPORT_BRIDGE',
      'scientific_boundary':[
        'The 2017 semiclassical continuum construction supplies a material Einstein-equation endpoint in a large-spin/refinement regime.',
        'The 2026 complete-amplitude construction supplies a material small-spin UV fixed-point/topological endpoint.',
        'The sources do not provide an explicit equality/reduction map between the amplitudes, a parameter transport map between lambda/delta/mu and the stack/UV variables, or a demonstrated trajectory connecting the small-spin UV regime to the large-spin semiclassical regime.',
        'No normalized same-domain gravity observable is transported across both endpoints; therefore KMQGB family terminalization remains blocked.'
      ],
      'sources':SOURCES
    })
if __name__=='__main__': main()

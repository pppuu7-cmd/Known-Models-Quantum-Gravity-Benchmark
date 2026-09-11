#!/usr/bin/env python3
import argparse
from lqg_uv_ir_bridge_common import SOURCES,BRIDGE,write_json

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); a=ap.parse_args()
    shared=BRIDGE['shared_broad_parent_family']
    same=BRIDGE['explicit_same_realization_identification_between_2017_and_2026_amplitudes']
    ok=shared and not same
    write_json(a.output,{
      'probe':'lqg_uv_ir_family_identity_guard','pass':ok,
      'shared_parent_family':shared,'explicit_same_realization_identity':same,
      'ir_object':SOURCES['ir_gr']['amplitude_scope'],'uv_object':SOURCES['uv_fixed_point']['amplitude_scope'],
      'classification':'PASS_SHARED_LQG_PARENT__SAME_REALIZATION_IDENTITY_NOT_EXPLICIT' if ok else 'FAIL_IDENTITY_CONTRACT',
      'boundary':'Common covariant-LQG ancestry is positive adjacency evidence but is not an explicit equality/reduction map between the 2017 refining-triangulation amplitude and the 2026 complete stack-summed amplitude.'})
    if not ok: raise SystemExit(1)
if __name__=='__main__': main()

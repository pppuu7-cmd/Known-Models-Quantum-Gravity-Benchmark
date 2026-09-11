#!/usr/bin/env python3
import argparse
from lqg_stack_uv_entropy_common import UV,ENTROPY,write_json

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); a=ap.parse_args()
    ok=(UV['root_face_couplings'] and ENTROPY['coupling_related_to_gamma_for_bh'] and ENTROPY['bh_normalized_after_selection'])
    write_json(a.output,{'probe':'stack_coupling_gamma_guard','pass':ok,
      'classification':'PASS_SHARED_STACK_COUPLING_STRUCTURE_WITH_ENTROPY_GAMMA_SELECTION__NO_FULL_PARAMETER_FLOW_CERTIFICATE' if ok else 'FAIL_STACK_COUPLING_GAMMA_CONTRACT',
      'boundary':'The coupling/gamma relation supplies a directional parameter anchor, but no complete map from UV fixed-point coupling variables to the semiclassical transport variables is established.'})
    if not ok: raise SystemExit(1)
if __name__=='__main__': main()

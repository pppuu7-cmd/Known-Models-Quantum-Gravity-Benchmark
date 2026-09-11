#!/usr/bin/env python3
import argparse
from lqg_wick_bridge_common import WICK2021,write_json

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); a=ap.parse_args()
    ok=(WICK2021['vertex_level_relation'] and WICK2021['fixed_triangulation_context'] and not WICK2021['full_rigging_map_transport'] and not WICK2021['complete_stack_transport'])
    write_json(a.output,{
      'probe':'lqg_wick_object_scope_guard','pass':ok,
      'classification':'PASS_VERTEX_LEVEL_SIGNATURE_RELATION__RIGGING_MAP_AND_COMPLETE_STACK_TRANSPORT_NOT_ESTABLISHED' if ok else 'FAIL_WICK_OBJECT_SCOPE_CONTRACT',
      'boundary':'The mapped object is the EPRL vertex-amplitude structure; the audit does not identify a transported Yang rigging map or Han complete-stack amplitude.'})
    if not ok: raise SystemExit(1)
if __name__=='__main__': main()

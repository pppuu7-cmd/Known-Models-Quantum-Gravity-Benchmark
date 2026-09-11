#!/usr/bin/env python3
import argparse
from lqg_wick_bridge_common import WICK2021,write_json

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); a=ap.parse_args()
    ok=(WICK2021['maps_euclidean_lorentzian_vertex_amplitudes'] and WICK2021['map_type'].startswith('analytic_continuation'))
    write_json(a.output,{
      'probe':'lqg_wick_vertex_map_guard','pass':ok,
      'classification':'PASS_EXPLICIT_EUCLIDEAN_LORENTZIAN_EPRL_VERTEX_ANALYTIC_CONTINUATION' if ok else 'FAIL_VERTEX_ANALYTIC_CONTINUATION_CONTRACT',
      'boundary':'This establishes a structural vertex-amplitude relation, not by itself a physical-state or complete-stack transport certificate.'})
    if not ok: raise SystemExit(1)
if __name__=='__main__': main()

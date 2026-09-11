#!/usr/bin/env python3
import argparse
from lqg_wick_bridge_common import WICK2021,CHAIN,write_json

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); a=ap.parse_args()
    ok=(WICK2021['immmirzi_map']=='gamma_real_to_i_gamma' and not WICK2021['same_real_gamma_identity'] and not CHAIN['explicit_real_gamma_preserving_transport'])
    write_json(a.output,{
      'probe':'lqg_wick_imMirzi_domain_guard','pass':ok,
      'classification':'PASS_SIGNATURE_MAP_REQUIRES_IMMIRZI_ANALYTIC_CONTINUATION__NO_SAME_REAL_GAMMA_IDENTITY' if ok else 'FAIL_IMMIRZI_DOMAIN_CONTRACT',
      'boundary':'A Euclidean real-gamma result cannot be silently promoted to the Lorentzian real-gamma Han chain; the published map rotates the Immirzi parameter into the complex domain.'})
    if not ok: raise SystemExit(1)
if __name__=='__main__': main()

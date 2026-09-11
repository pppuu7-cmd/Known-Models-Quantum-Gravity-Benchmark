#!/usr/bin/env python3
import argparse
from lqg_entropy_observable_common import HAN_ENTROPY_2026,write_json

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); a=ap.parse_args()
    ok=(HAN_ENTROPY_2026['bh_formula_reproduced_with_coupling_gamma_relation'] and not HAN_ENTROPY_2026['parameter_free_bh_normalization'])
    write_json(a.output,{
      'probe':'lqg_entropy_coupling_gamma_guard','pass':ok,
      'classification':'PASS_SCOPED_BH_MATCH_REQUIRES_EXPLICIT_COUPLING_GAMMA_SELECTION' if ok else 'FAIL_COUPLING_GAMMA_SCOPE_CONTRACT',
      'boundary':'The Bekenstein-Hawking match is a high-value scoped positive, but not parameter-free closure because the stack coupling must be related to gamma.'})
    if not ok: raise SystemExit(1)
if __name__=='__main__': main()

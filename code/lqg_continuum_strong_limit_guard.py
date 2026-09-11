#!/usr/bin/env python3
import argparse
from lqg_continuum_contract_common import SOURCE,CLAIMS,write_json

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output', required=True); a=ap.parse_args()
    t=CLAIMS['theorem_5_1']
    ok=('inductive boundary Hilbert space' in t['hypothesis'] and t['consequence']=='the continuum map defines a TQFT' and 'non-topological 4D gravity' in t['gravity_boundary'])
    write_json(a.output, {
      'probe':'lqg_continuum_strong_limit_guard','source':SOURCE,'pass':ok,
      'classification':'PASS_CONTRACT_STRONG_HILBERT_LIMIT_IMPLIES_TOPOLOGICAL_NO_GO' if ok else 'FAIL_CONTRACT_MISMATCH',
      'boundary':'This validates the KMQGB interpretation of Theorem 5.1; it does not independently re-prove the theorem.'})
    if not ok: raise SystemExit(1)
if __name__=='__main__': main()

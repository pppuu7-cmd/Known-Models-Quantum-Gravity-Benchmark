#!/usr/bin/env python3
import argparse
from cfs_geometric_einstein_common import CFS_GEOMETRIC_2026 as S, write_json

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); a=ap.parse_args()
    ok=(S['authority']=='public_preprint' and S['lorentzian_four_dimensional_main_theorem'] and S['einstein_equations_explicit'] and S['energy_momentum_explicit'])
    write_json(a.output,{'probe':'cfs_geometric_einstein_scope_guard','pass':ok,'explicit_lorentzian_einstein_endpoint':ok,'classification':'PASS_SCOPED_EXPLICIT_LORENTZIAN_4D_EINSTEIN_EQUATIONS_FROM_CAUSAL_ACTION' if ok else 'FAIL_SOURCE_SCOPE_CONTRACT','boundary':'Scoped public-preprint result; do not infer evaluated beyond-Einstein corrections.'})
    if not ok: raise SystemExit(1)
if __name__=='__main__': main()

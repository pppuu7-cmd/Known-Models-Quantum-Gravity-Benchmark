#!/usr/bin/env python3
import argparse
from cfs_geometric_einstein_common import CFS_GEOMETRIC_2026 as S, FROZEN_CFS, write_json

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); a=ap.parse_args()
    endpoint=S['einstein_equations_explicit'] and S['energy_momentum_explicit']
    missing=(not S['explicit_evaluated_beyond_einstein_correction_tensor'] and not S['normalized_beyond_einstein_observable'] and not S['same_domain_comparator_residual'] and not S['propagated_correction_uncertainty'])
    ok=endpoint and missing and FROZEN_CFS['status']=='BLOCKED_MISSING_REQUIRED_OBJECT'
    write_json(a.output,{'probe':'cfs_geometric_blocker_guard','pass':ok,'explicit_rank_two_einstein_endpoint':endpoint,'frozen_beyond_einstein_object_still_missing':missing,'family_terminal':False,'classification':'PASS_EINSTEIN_ENDPOINT_UPGRADED__FROZEN_BEYOND_EINSTEIN_RESIDUAL_COMPARATOR_BLOCKER_REMAINS' if ok else 'FAIL_CFS_BLOCKER_CONTRACT','required_next_object':FROZEN_CFS['required']})
    if not ok: raise SystemExit(1)
if __name__=='__main__': main()

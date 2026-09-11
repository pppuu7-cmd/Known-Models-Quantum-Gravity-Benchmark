#!/usr/bin/env python3
import argparse
from cfs_geometric_einstein_common import CFS_GEOMETRIC_2026 as S, write_json

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); a=ap.parse_args()
    listed=all(S[k] for k in ['systematic_correction_procedure','planck_scale_higher_delta_corrections_listed','osculation_torsion_corrections_listed','regularizing_vector_corrections_listed','modified_measure_corrections_listed'])
    not_evaluated=(not S['explicit_evaluated_beyond_einstein_correction_tensor'] and not S['corrections_worked_out_in_detail'])
    ok=listed and not_evaluated
    write_json(a.output,{'probe':'cfs_geometric_corrections_maturity_guard','pass':ok,'systematic_correction_hierarchy':listed,'concrete_beyond_einstein_tensor_evaluated':S['explicit_evaluated_beyond_einstein_correction_tensor'],'corrections_worked_out_in_detail':S['corrections_worked_out_in_detail'],'classification':'PASS_SYSTEMATIC_CORRECTION_HIERARCHY_PRESENT__CONCRETE_CORRECTIONS_STILL_PROSPECTIVE' if ok else 'FAIL_CORRECTION_MATURITY_CONTRACT','boundary':'A systematic route and named correction classes are not the frozen normalized beyond-Einstein residual object.'})
    if not ok: raise SystemExit(1)
if __name__=='__main__': main()

#!/usr/bin/env python3
import argparse
from lqg_entropy_observable_common import HAN_ENTROPY_2026,write_json

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); a=ap.parse_args()
    ok=(HAN_ENTROPY_2026['beta_positive'] and HAN_ENTROPY_2026['leading_beta_2complex_independent'] and HAN_ENTROPY_2026['log_coefficient_may_depend_on_boundary_graph'])
    write_json(a.output,{
      'probe':'lqg_entropy_discretization_guard','pass':ok,
      'classification':'PASS_LEADING_AREA_COEFFICIENT_2COMPLEX_INDEPENDENT__SUBLEADING_GRAPH_DEPENDENCE_REMAINS' if ok else 'FAIL_DISCRETIZATION_SCOPE_CONTRACT',
      'boundary':'Leading area-law coefficient independence is not full discretization independence; logarithmic corrections may retain boundary-graph dependence.'})
    if not ok: raise SystemExit(1)
if __name__=='__main__': main()

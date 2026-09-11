#!/usr/bin/env python3
import argparse
from lqg_continuum_contract_common import SOURCE,CLAIMS,write_json

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output', required=True); a=ap.parse_args()
    b=CLAIMS['model_specificity_boundary']
    ok=(CLAIMS['model_independent_framework'] and not b['explicit_constraint_relation_available'] and not b['specified_physical_observable_algebra_available'])
    write_json(a.output, {
      'probe':'lqg_continuum_model_specificity_guard','source':SOURCE,'pass':ok,
      'classification':'PASS_BOUNDARY_MODEL_INDEPENDENT_CONTINUUM_FRAMEWORK_NOT_MODEL_SPECIFIC_COMPLETION' if ok else 'FAIL_BOUNDARY_OVERPROMOTION_RISK',
      'required_kmqgb_objects_still_external':['specific constraints/state map','specified physical observable algebra','same-realization normalized gravity observable','UV-to-IR/GR transport','propagated uncertainty/comparator'],
      'boundary':'The generic rigging-map construction cannot by itself close a concrete LQG/spinfoam family-level observable certificate.'})
    if not ok: raise SystemExit(1)
if __name__=='__main__': main()

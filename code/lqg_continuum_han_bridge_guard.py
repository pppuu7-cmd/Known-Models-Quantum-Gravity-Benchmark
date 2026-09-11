#!/usr/bin/env python3
import argparse
from lqg_continuum_contract_common import SOURCE,CLAIMS,write_json

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output', required=True); a=ap.parse_args()
    h=CLAIMS['han_stack']; t=CLAIMS['theorem_5_1']
    compatible=(h['infinite_internal_area_cutoff_regime']=='topological_scale_invariant' and t['consequence']=='the continuum map defines a TQFT')
    bridge_open=(h['semiclassical_regge_gr_regime']=='finite_large_cutoff_small_gamma' and not h['same_realization_physical_uv_ir_bridge_explicit'])
    ok=compatible and bridge_open
    write_json(a.output, {
      'probe':'lqg_continuum_han_bridge_guard','source':SOURCE,'pass':ok,
      'han_topological_limit_compatible_with_no_go':compatible,
      'physical_uv_ir_gr_bridge_still_open':bridge_open,
      'classification':'PASS_COMPATIBILITY_HAN_TOPOLOGICAL_LIMIT_CONSISTENT_WITH_NO_GO__PHYSICAL_BRIDGE_STILL_MISSING' if ok else 'FAIL_COMPATIBILITY_CONTRACT',
      'boundary':'Compatibility is not equivalence of the two constructions and is not a same-realization UV-to-IR/GR trajectory.'})
    if not ok: raise SystemExit(1)
if __name__=='__main__': main()

#!/usr/bin/env python3
import argparse
from lqg_continuum_contract_common import SOURCE,CLAIMS,write_json

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output', required=True); a=ap.parse_args()
    d=CLAIMS['distributional_path']
    required=['uses_gelfand_triple','limit_in_algebraic_dual','cylinder_defines_rigging_map','rigging_antilinear','rigging_reality','rigging_positive_semidefinite','physical_hilbert_quotient_completion']
    missing=[k for k in required if not d.get(k)]
    ok=not missing
    write_json(a.output, {
      'probe':'lqg_continuum_rigging_map_guard','source':SOURCE,'pass':ok,'missing':missing,
      'classification':'PASS_CONTRACT_DISTRIBUTIONAL_LIMIT_RIGGING_MAP_AND_PHYSICAL_HILBERT_PATH' if ok else 'FAIL_CONTRACT_MISSING_RIGGING_PROPERTY',
      'boundary':'This validates the published structural route to a physical Hilbert space under the paper assumptions; it is not a model-specific LQG observable or GR-limit certificate.'})
    if not ok: raise SystemExit(1)
if __name__=='__main__': main()

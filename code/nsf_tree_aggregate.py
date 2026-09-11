#!/usr/bin/env python3
import argparse, json
from pathlib import Path
from nsf_tree_common import SOURCE, write_json
EXPECTED={'normalization':'nsf_tree_normalization','tu-symmetry':'nsf_tree_tu_symmetry','fixed-angle':'nsf_tree_fixed_angle_scaling','collinear':'nsf_tree_collinear_scaling'}
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--input-dir',required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
    root=Path(a.input_dir); data={}
    for label,probe in EXPECTED.items():
        p=json.loads((root/f'{label}.json').read_text())
        if p.get('probe')!=probe: raise SystemExit(f'bad probe {label}')
        data[label]=p
    out={
      'probe':'nsf_iter279_claim_boundary_aggregate','source':SOURCE,'all_four_independent_probes_present':True,
      'normalization_max_relative_error':data['normalization']['max_relative_error'],
      'tu_symmetry_max_relative_error':data['tu-symmetry']['max_relative_error'],
      'fixed_angle_exponents':[x['loglog_scaling_exponent'] for x in data['fixed-angle']['rows']],
      'collinear_epsilon_exponent':data['collinear']['loglog_epsilon_exponent'],
      'classification_boundary':[
        'NSF is explicitly a null-surface formulation/quantization of general relativity in the cited lineage and reproduces the standard tree amplitude; this supplies a positive reduction-map signal rather than evidence for a new independent Tier-1 parent.',
        'The algebraic checks do not establish all-order equivalence or validate the all-loop UV-finiteness proof.',
        'UV-finite integration/renormalization behavior is not the same claim as bounded fixed-angle high-energy amplitude or forward-limit regularity.',
        'No Tier-1 census change or family-level terminal promotion is authorized by these checks.'
      ]}
    write_json(a.output,out)
if __name__=='__main__': main()

#!/usr/bin/env python3
import argparse,json
from pathlib import Path
from lqg_stack_hessian_common import SOURCE,write_json
EXPECTED={
 'definiteness':'lqg_stack_exact_definiteness',
 'incidence':'lqg_stack_incidence_factorization',
 'kron18':'lqg_stack_kron18_consistency',
 'coefficients':'lqg_stack_C012_convergence'
}
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--input-dir',required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
 root=Path(a.input_dir); d={}
 for label,probe in EXPECTED.items():
  x=json.loads((root/f'{label}.json').read_text())
  if x.get('probe')!=probe: raise SystemExit(f'bad probe {label}: {x.get("probe")}')
  d[label]=x
 out={
  'probe':'lqg_spinfoam_stack_iter281_aggregate','source':SOURCE,
  'all_four_independent_probes_present':True,
  'exact_6x6':{
   'determinant':d['definiteness']['determinant_6x6'],
   'strict_negative_definite_by_sylvester':d['definiteness']['strict_negative_definite_by_sylvester'],
   'nondegenerate':d['definiteness']['nondegenerate']},
  'incidence_topology':{
   'M_equals_minus_BtB_exact':d['incidence']['exact_factorization_M_equals_minus_BtB'],
   'rank_B':d['incidence']['rank_B'],'kernel_dimension':d['incidence']['kernel_dimension_projected_non_tree_cochains']},
  'kron18':{
   'rank':d['kron18']['rank_18x18'],'determinant_identity_exact':d['kron18']['determinant_identity_exact'],
   'nondegenerate':d['kron18']['nondegenerate']},
  'coefficient_sums':{
   'all_beta_final_coefficients_positive':d['coefficients']['all_beta_final_coefficients_positive'],
   'max_relative_256_to_512':d['coefficients']['max_relative_256_to_512']},
  'scientific_boundary':[
   'This independently checks the explicit trivial-topology 1-5 Pachner Hessian example and representative positive-beta coefficient sums.',
   'It supports the source nondegeneracy/localization machinery in that explicit example; it does not independently reproduce the full stack amplitude or prove the generic theorem for all complexes.',
   'The source large-internal-area-cutoff limit is a topological/scale-invariant regime, whereas the semiclassical GR/Regge regime is argued for finite large cutoffs and small Barbero-Immirzi parameter; these are distinct regimes.',
   'Therefore this result strengthens LQG triangulation/refinement control but does not close the existing same-realization physical UV-to-IR/GR trajectory and normalized-observable blocker.'
  ]}
 write_json(a.output,out)
if __name__=='__main__': main()

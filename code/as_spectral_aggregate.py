#!/usr/bin/env python3
import argparse,json
from pathlib import Path
from as_spectral_common import SOURCE,write_json
EXPECTED={'rg':'as_spectral_rg_trajectory','uv':'as_spectral_uv_tail_integrability','weight':'as_spectral_weight_decomposition','ir':'as_spectral_ir_coefficient'}
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--input-dir',required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
 root=Path(a.input_dir); d={}
 for label,probe in EXPECTED.items():
  x=json.loads((root/f'{label}.json').read_text())
  if x.get('probe')!=probe: raise SystemExit(f'bad probe {label}: {x.get("probe")}')
  d[label]=x
 out={
  'probe':'as_spectral_iter280_aggregate','source':SOURCE,'all_four_independent_probes_present':True,
  'rg':{'gstar_exact':d['rg']['gstar_exact'],'fixed_point_beta_abs':d['rg']['fixed_point_beta_abs'],'max_trajectory_relative_residual':d['rg']['max_trajectory_relative_residual']},
  'uv':{'p3_infinite_limit_unit_prefactor':d['uv']['p3_infinite_limit_unit_prefactor'],'last_row':d['uv']['rows'][-1]},
  'weight':{'z_spec_reported':d['weight']['z_spec_reported'],'physical_pole_weight_fraction':d['weight']['physical_pole_weight_fraction'],'physical_continuum_weight_fraction':d['weight']['physical_continuum_weight_fraction'],'physical_total':d['weight']['physical_total']},
  'ir':{'A_h':d['ir']['A_h_61_over_60pi'],'tail_onset':d['ir']['tail_onset_reported_61_over_30'],'relative_difference':d['ir']['relative_difference']},
  'public_reproducibility_boundary':{
    'full_numerical_spectral_curve_recomputed':False,
    'reason':'Publisher states data available on request; no public numerical spectral dataset or article-specific source-code repository was located in this audit. The paper gives equations and numerical tolerances, but reconstructing the full Julia spectral-flow implementation is a separate task.',
    'classification':'BLOCKED_PUBLIC_NUMERICAL_DATA_OR_REFERENCE_IMPLEMENTATION_FOR_FULL_CURVE_REPRODUCTION'
  },
  'scientific_boundary':[
    'The peer-reviewed work supplies a strong scoped positive result for a positive normalisable Lorentzian graviton spectral function in the stated on-shell TT fluctuation-graviton setup.',
    'The authors explicitly state that these fluctuation-graviton states are not diffeomorphism invariant and are not members of the physical Hilbert space.',
    'The unit spectral-weight statement after physical rescaling is not by itself a family-level proof of unitarity for Asymptotic Safety.',
    'The existing contact-complete s+t+u+A4 scattering blocker remains independent and unresolved.'
  ]}
 write_json(a.output,out)
if __name__=='__main__': main()

#!/usr/bin/env python3
import argparse
from as_spectral_common import SOURCE,ZSPEC,write_json

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); a=ap.parse_args()
 pole=1.0/ZSPEC; continuum=(ZSPEC-1.0)/ZSPEC
 lo=1.4855; hi=1.4865
 bounds={
  'pole_fraction_if_rounding_half_unit_last_digit':[1/hi,1/lo],
  'continuum_fraction_if_rounding_half_unit_last_digit':[(lo-1)/lo,(hi-1)/hi]
 }
 write_json(a.output,{'probe':'as_spectral_weight_decomposition','source':SOURCE,'z_spec_reported':ZSPEC,'unnormalized_continuum_weight_from_reported_z':ZSPEC-1.0,'physical_pole_weight_fraction':pole,'physical_continuum_weight_fraction':continuum,'physical_total':pole+continuum,'rounding_bounds':bounds,'boundary':'Algebraically propagates the published z_spec≈1.486; it does not independently recompute the spectral integral that produced z_spec.'})
if __name__=='__main__': main()

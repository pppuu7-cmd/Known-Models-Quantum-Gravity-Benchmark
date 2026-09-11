#!/usr/bin/env python3
import argparse
from cfs_geometric_einstein_common import CFS_GEOMETRIC_2026 as S, write_json

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); a=ap.parse_args()
    ok=(S['energy_momentum_symmetric'] and S['energy_momentum_divergence_free'] and S['leading_energy_momentum_scaling_delta_power']==2 and S['gravitational_coupling_regularization_length_squared'])
    write_json(a.output,{'probe':'cfs_geometric_conservation_scaling_guard','pass':ok,'symmetric':S['energy_momentum_symmetric'],'divergence_free':S['energy_momentum_divergence_free'],'leading_delta_power':S['leading_energy_momentum_scaling_delta_power'],'gravity_coupling_regularization_length_squared':S['gravitational_coupling_regularization_length_squared'],'classification':'PASS_EXPLICIT_CONSERVATION_AND_REGULARIZATION_SCALING' if ok else 'FAIL_CONSERVATION_SCALING_CONTRACT'})
    if not ok: raise SystemExit(1)
if __name__=='__main__': main()

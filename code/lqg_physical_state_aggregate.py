#!/usr/bin/env python3
import argparse,json
from pathlib import Path
from lqg_physical_state_link_common import YANG2021,CHAIN,write_json
EXPECTED={
 'content':'lqg_physical_state_content_guard',
 'signature':'lqg_physical_state_signature_guard',
 'scope':'lqg_physical_state_beta_scope_guard',
 'chain':'lqg_physical_state_chain_guard'
}
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--input-dir',required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
    root=Path(a.input_dir); rows={}
    for label,probe in EXPECTED.items():
        r=json.loads((root/f'{label}.json').read_text())
        if r.get('probe')!=probe or not r.get('pass'): raise SystemExit(f'bad probe {label}')
        rows[label]=r
    write_json(a.output,{
      'probe':'lqg_physical_state_iter284_aggregate',
      'all_four_independent_guards_pass':True,
      'physical_state_component':'HIGH_VALUE_SCOPED_POSITIVE',
      'same_realization_chain_ready':False,
      'content_result':rows['content']['classification'],
      'signature_result':rows['signature']['classification'],
      'beta_state_scope_result':rows['scope']['classification'],
      'chain_result':rows['chain']['classification'],
      'classification':'HIGH_VALUE_EUCLIDEAN_BETA1_RIGGING_MAP_COMPONENT__NO_EXPLICIT_COMPATIBLE_TRANSPORT_INTO_LORENTZIAN_UV_IR_CHAIN',
      'scientific_boundary':[
        'The 2021 generalized Euclidean EPRL calculation supplies a genuine scoped canonical/covariant consistency result via a rigging map and weak Hamiltonian-constraint satisfaction on certain states at beta=1.',
        'It is not a full-state-space or generic-Immirzi certificate.',
        'No explicit same-realization state/signature/parameter map to the Lorentzian complete-stack UV endpoint and Iter283 UV-to-IR chain is supplied by this source.',
        'No normalized gravity observable is transported through the complete chain; LQG family terminalization therefore remains blocked.'
      ],
      'source':YANG2021,'chain_context':CHAIN
    })
if __name__=='__main__': main()

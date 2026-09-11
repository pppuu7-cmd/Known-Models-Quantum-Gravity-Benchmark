#!/usr/bin/env python3
import argparse
from lqg_physical_state_link_common import YANG2021,CHAIN,write_json

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); a=ap.parse_args()
    scoped=(YANG2021['immmirzi_beta']==1.0 and YANG2021['physical_state_scope']=='certain_spin_network_states' and not YANG2021['full_state_space_certificate'])
    write_json(a.output,{
      'probe':'lqg_physical_state_beta_scope_guard','pass':scoped,
      'immmirzi_beta':YANG2021['immmirzi_beta'],
      'state_scope':YANG2021['physical_state_scope'],
      'full_state_space_certificate':YANG2021['full_state_space_certificate'],
      'classification':'PASS_SCOPED_BETA1_CERTAIN_STATES__NO_GENERIC_BETA_OR_FULL_STATE_SPACE_CERTIFICATE' if scoped else 'FAIL_BETA_STATE_SCOPE_CONTRACT',
      'boundary':'A beta=1 result on certain states cannot establish parameter-independent or full-state-space canonical/covariant equivalence.'})
    if not scoped: raise SystemExit(1)
if __name__=='__main__': main()

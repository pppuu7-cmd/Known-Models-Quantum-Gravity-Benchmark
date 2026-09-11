#!/usr/bin/env python3
import argparse
from lqg_physical_state_link_common import YANG2021,CHAIN,write_json

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); a=ap.parse_args()
    ok=(YANG2021['implied_rigging_map'] and YANG2021['constraint_satisfaction']=='weak' and YANG2021['physical_state_scope']=='certain_spin_network_states')
    write_json(a.output,{
      'probe':'lqg_physical_state_content_guard','pass':ok,
      'classification':'PASS_SCOPED_EPRL_RIGGING_MAP_WITH_WEAK_CONSTRAINT_SATISFACTION_ON_CERTAIN_STATES' if ok else 'FAIL_PHYSICAL_STATE_CONTENT_CONTRACT',
      'boundary':'This is a genuine scoped physical-state/canonical-covariant consistency result, not a full physical-state-space certificate.'})
    if not ok: raise SystemExit(1)
if __name__=='__main__': main()

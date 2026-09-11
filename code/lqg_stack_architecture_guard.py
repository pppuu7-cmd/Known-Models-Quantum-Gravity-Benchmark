#!/usr/bin/env python3
import argparse
from lqg_stack_uv_entropy_common import UV,ENTROPY,write_json

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); a=ap.parse_args()
    ok=(UV['signature']==ENTROPY['signature']=='Lorentzian' and UV['complete_amplitude_sum_over_2complexes'] and UV['spinfoam_stack'] and ENTROPY['sum_over_family_of_2complexes'] and UV['entropy_paper_explicitly_cited_in_stack_sections'])
    write_json(a.output,{'probe':'same_stack_architecture_guard','pass':ok,
      'classification':'PASS_HIGH_VALUE_SHARED_LORENTZIAN_STACK_ARCHITECTURE_UV_AND_ENTROPY' if ok else 'FAIL_SHARED_STACK_ARCHITECTURE_CONTRACT',
      'boundary':'Shared architecture materially reduces the realization-identity gap but does not by itself prove a continuous UV-to-IR trajectory.'})
    if not ok: raise SystemExit(1)
if __name__=='__main__': main()

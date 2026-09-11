#!/usr/bin/env python3
import argparse
from lqg_stack_hessian_common import M,SOURCE,det_bareiss,kron_identity3,rank_fraction,write_json

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); a=ap.parse_args()
 K=kron_identity3(M); d6=det_bareiss(M); d18=det_bareiss(K)
 expected=d6**3
 write_json(a.output,{
  'probe':'lqg_stack_kron18_consistency','source':SOURCE,
  'shape':[18,18],'rank_18x18':rank_fraction(K),'determinant_18x18':d18,
  'determinant_expected_det6_cubed':expected,'determinant_identity_exact':d18==expected,
  'nondegenerate':d18!=0,
  'boundary':'Exact Kronecker consistency of the published 18x18 t-t block structure; C2 is factored out and assumed positive as in the source.'})
if __name__=='__main__': main()

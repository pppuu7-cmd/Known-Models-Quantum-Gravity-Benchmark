#!/usr/bin/env python3
import argparse
from lqg_stack_hessian_common import M,B,SOURCE,transpose,matmul,scalar,rank_fraction,write_json

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); a=ap.parse_args()
 reconstructed=scalar(matmul(transpose(B),B),-1)
 delta=[[reconstructed[i][j]-M[i][j] for j in range(6)] for i in range(6)]
 max_abs=max(abs(x) for row in delta for x in row)
 write_json(a.output,{
  'probe':'lqg_stack_incidence_factorization','source':SOURCE,
  'rank_B':rank_fraction(B),'rank_M':rank_fraction(M),
  'exact_factorization_M_equals_minus_BtB':max_abs==0,
  'max_absolute_entry_difference':max_abs,
  'kernel_dimension_projected_non_tree_cochains':6-rank_fraction(B),
  'boundary':'Verifies Eq.75 for the explicit 1-5 Pachner example and chosen tree/orientations; it is not a general numerical proof for arbitrary topology.'})
if __name__=='__main__': main()

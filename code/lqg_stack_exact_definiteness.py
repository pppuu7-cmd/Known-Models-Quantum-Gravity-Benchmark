#!/usr/bin/env python3
import argparse
from lqg_stack_hessian_common import M,SOURCE,det_bareiss,write_json

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); a=ap.parse_args()
 minors=[]
 for k in range(1,len(M)+1):
  d=det_bareiss([row[:k] for row in M[:k]])
  minors.append({'k':k,'det':d,'negative_definite_sylvester_quantity':((-1)**k)*d})
 neg=all(x['negative_definite_sylvester_quantity']>0 for x in minors)
 write_json(a.output,{
  'probe':'lqg_stack_exact_definiteness','source':SOURCE,
  'determinant_6x6':det_bareiss(M),'leading_principal_minors':minors,
  'strict_negative_definite_by_sylvester':neg,
  'nondegenerate':det_bareiss(M)!=0,
  'boundary':'Exact audit of the published finite Hessian example only; it does not prove generic-complex nondegeneracy beyond the source theorem.'})
if __name__=='__main__': main()

#!/usr/bin/env python3
import argparse,math
from lqg_stack_hessian_common import SOURCE,write_json

def coeffs(beta,kmax):
 c0=n1=n2=0.0
 for k in range(1,kmax+1):
  d=k+1.0; area=math.sqrt(k*(k+2.0)); w=math.exp(-beta*area)
  c0 += d*d*area*w
  n1 += (d*d*(d+1.0)/6.0)*w
  n2 += (d*d*(d-1.0)*(d+1.0)/12.0)*w
 return c0,n1/c0,n2/c0

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); a=ap.parse_args()
 betas=[0.25,0.5,1.0,2.0]; truncs=[32,64,128,256,512]
 rows=[]
 for beta in betas:
  vals=[]
  for K in truncs:
   c0,c1,c2=coeffs(beta,K); vals.append({'kmax':K,'C0':c0,'C1':c1,'C2':c2})
  last,prev=vals[-1],vals[-2]
  rel={x:abs(last[x]-prev[x])/max(abs(last[x]),1e-300) for x in ('C0','C1','C2')}
  rows.append({'beta':beta,'truncations':vals,'relative_256_to_512':rel,'all_final_positive':all(last[x]>0 for x in ('C0','C1','C2'))})
 write_json(a.output,{
  'probe':'lqg_stack_C012_convergence','source':SOURCE,'rows':rows,
  'all_beta_final_coefficients_positive':all(r['all_final_positive'] for r in rows),
  'max_relative_256_to_512':max(v for r in rows for v in r['relative_256_to_512'].values()),
  'boundary':'Numerically checks positivity and truncation convergence of the published coefficient sums for a representative positive-beta grid; it does not scan all beta or finite-gamma corrections.'})
if __name__=='__main__': main()

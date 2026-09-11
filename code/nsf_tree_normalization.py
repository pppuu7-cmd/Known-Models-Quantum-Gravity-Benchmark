#!/usr/bin/env python3
import argparse, math
from nsf_tree_common import SOURCE, amplitude, amplitude_G_form, write_json

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); a=ap.parse_args()
    samples=[(1.0,-0.3,-0.7,0.2),(10.0,-4.0,-6.0,1.0),(1e3,-250.0,-750.0,0.7)]
    errs=[]; rows=[]
    for s,t,u,G in samples:
        x=amplitude(s,t,u,G); y=amplitude_G_form(s,t,u,G)
        rel=abs(x-y)/max(abs(x),abs(y),1e-300); errs.append(rel)
        rows.append({'s':s,'t':t,'u':u,'G':G,'kappa_form':x,'G_form':y,'relative_error':rel})
    write_json(a.output,{'probe':'nsf_tree_normalization','source':SOURCE,'rows':rows,'max_relative_error':max(errs),
      'boundary':'Algebraic normalization consistency only; does not establish quantum equivalence beyond the source formula.'})
if __name__=='__main__': main()

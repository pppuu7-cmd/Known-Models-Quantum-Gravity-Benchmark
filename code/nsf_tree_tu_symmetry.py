#!/usr/bin/env python3
import argparse
from nsf_tree_common import SOURCE, amplitude, write_json

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); a=ap.parse_args()
    samples=[(1.0,-0.2,-0.8),(5.0,-1.5,-3.5),(100.0,-33.0,-67.0)]
    rows=[]; errs=[]
    for s,t,u in samples:
        x=amplitude(s,t,u); y=amplitude(s,u,t)
        rel=abs(x-y)/max(abs(x),abs(y),1e-300); errs.append(rel)
        rows.append({'s':s,'t':t,'u':u,'M_tu':x,'M_ut':y,'relative_error':rel})
    write_json(a.output,{'probe':'nsf_tree_tu_symmetry','source':SOURCE,'rows':rows,'max_relative_error':max(errs),
      'boundary':'Checks only the t<->u symmetry of the quoted complete tree formula, not full crossing for arbitrary helicity amplitudes.'})
if __name__=='__main__': main()

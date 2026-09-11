#!/usr/bin/env python3
import argparse, math
from nsf_tree_common import SOURCE, amplitude, write_json

def slope(xs, ys):
    lx=[math.log(x) for x in xs]; ly=[math.log(abs(y)) for y in ys]
    mx=sum(lx)/len(lx); my=sum(ly)/len(ly)
    return sum((x-mx)*(y-my) for x,y in zip(lx,ly))/sum((x-mx)**2 for x in lx)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); a=ap.parse_args()
    alphas=[0.2,0.35,0.5]
    scales=[1.0,10.0,100.0,1000.0]
    rows=[]
    for alpha in alphas:
        vals=[amplitude(s,-alpha*s,-(1-alpha)*s) for s in scales]
        rows.append({'alpha':alpha,'loglog_scaling_exponent':slope(scales,vals),'values':vals})
    write_json(a.output,{'probe':'nsf_tree_fixed_angle_scaling','source':SOURCE,'rows':rows,
      'boundary':'The quoted tree amplitude scales linearly with s at fixed angle. UV-finite loop/integration claims must not be rephrased as a bounded high-energy tree amplitude.'})
if __name__=='__main__': main()

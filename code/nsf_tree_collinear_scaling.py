#!/usr/bin/env python3
import argparse, math
from nsf_tree_common import SOURCE, amplitude, write_json

def slope(xs, ys):
    lx=[math.log(x) for x in xs]; ly=[math.log(abs(y)) for y in ys]
    mx=sum(lx)/len(lx); my=sum(ly)/len(ly)
    return sum((x-mx)*(y-my) for x,y in zip(lx,ly))/sum((x-mx)**2 for x in lx)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); a=ap.parse_args()
    eps=[1e-1,3e-2,1e-2,3e-3,1e-3]
    s=1.0
    vals=[]
    for e in eps:
        t=-e*s; u=-s-t
        vals.append(amplitude(s,t,u))
    p=slope(eps,vals)
    write_json(a.output,{'probe':'nsf_tree_collinear_scaling','source':SOURCE,'epsilon':eps,'absolute_amplitude':[abs(x) for x in vals],
      'loglog_epsilon_exponent':p,
      'boundary':'Forward/collinear t->0 behavior remains pole-like; perturbative UV finiteness is not infrared/forward-limit closure.'})
if __name__=='__main__': main()

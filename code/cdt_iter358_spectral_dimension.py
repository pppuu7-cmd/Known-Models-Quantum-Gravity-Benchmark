#!/usr/bin/env python3
import argparse,json
p=argparse.ArgumentParser()
p.add_argument("--case",required=True,choices=["short","meso","long","asymptotic"])
p.add_argument("--output",required=True)
a=p.parse_args()
grids={
 "short":[0,1,5,10,20],
 "meso":[0,10,50,100,200],
 "long":[0,50,200,500,1000],
 "asymptotic":[0,100,1000,10000,1000000]
}
sigmas=grids[a.case]
def ds(s): return 4.02-119.0/(54.0+s)
vals=[{"sigma":s,"D_S":ds(s)} for s in sigmas]
out={
 "iteration":358,
 "case":a.case,
 "fit":"D_S(sigma)=4.02-119/(54+sigma)",
 "D_S_at_zero":ds(0.0),
 "large_sigma_limit":4.02,
 "reported_short_distance_measurement":"1.80 +/- 0.25",
 "samples":vals,
 "monotone_increasing_on_nonnegative_sigma":True,
 "scoped_child_observable_only":True
}
with open(a.output,"w") as f: json.dump(out,f,indent=2,sort_keys=True)
print(json.dumps(out,sort_keys=True))

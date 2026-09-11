#!/usr/bin/env python3
import argparse,json
p=argparse.ArgumentParser()
p.add_argument('--case',required=True,choices=['m01','m05','m1a','m1b','m2','m5'])
p.add_argument('--output',required=True)
a=p.parse_args()
params={
 'm01':(0.1,0.01),'m05':(0.5,0.05),'m1a':(1.0,0.1),
 'm1b':(1.0,0.5),'m2':(2.0,0.2),'m5':(5.0,2.5)
}
reM,imM=params[a.case]
thr=2.0*reM
fractions=[-2.5,-2.0,-1.999,-1.0,0.0,1.0,1.999,2.0,2.5]
rows=[]
for f in fractions:
 p0=f*reM
 inactive=(-thr < p0 < thr)
 rows.append({'p0_over_ReM':f,'p0':p0,'complex_delta_inactive_by_source_window':inactive})
out={
 'iteration':363,
 'case':a.case,
 'ReM':reM,'ImM':imM,'ImM_over_ReM':imM/reM,
 'threshold_2ReM':thr,
 'rows':rows,
 'threshold_independent_of_ImM_in_stationary_source_relation':True,
 'strict_open_interval_used':True,
 'scope':'stationary p-vector=0 source threshold audit; not a scattering unitarity certificate'
}
with open(a.output,'w') as f: json.dump(out,f,indent=2,sort_keys=True)
print(json.dumps(out,sort_keys=True))

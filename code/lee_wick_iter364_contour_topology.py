#!/usr/bin/env python3
import argparse,json
p=argparse.ArgumentParser()
p.add_argument('--im-m2',type=float,required=True)
p.add_argument('--output',required=True)
a=p.parse_args()
xs=[0.0,0.1,0.25,0.49,0.5,0.51,0.75,0.9,1.0]
rows=[]
for x in xs:
 v=(2*x-1)*a.im_m2
 sign='ZERO' if abs(v)<1e-15 else ('POSITIVE' if v>0 else 'NEGATIVE')
 rows.append({'x':x,'ImDelta':v,'sign':sign})
out={
 'iteration':364,
 'ImM2':a.im_m2,
 'source_relation':'Im Delta = (2x-1) Im M^2',
 'rows':rows,
 'sign_change_at_x_half': a.im_m2>0,
 'first_quadrant_pole_region_for_positive_ImM2':'x>1/2 under source assumptions',
 'contour_residue_sensitivity_present':a.im_m2>0,
 'scope':'Feynman-parameter contour-topology audit; not a prescription-selection theorem'
}
with open(a.output,'w') as f: json.dump(out,f,indent=2,sort_keys=True)
print(json.dumps(out,sort_keys=True))

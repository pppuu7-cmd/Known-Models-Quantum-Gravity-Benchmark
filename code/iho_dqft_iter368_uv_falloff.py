#!/usr/bin/env python3
import argparse,json
p=argparse.ArgumentParser()
p.add_argument('--mu2-sq',type=float,required=True)
p.add_argument('--output',required=True)
a=p.parse_args()
assert a.mu2_sq>0
xs=[1e2,1e4,1e6,1e8]
rows=[]
for x in xs:
    k2=x*a.mu2_sq
    K=1.0/k2-1.0/(k2-a.mu2_sq)
    scaled=K*(k2**2)/a.mu2_sq
    rows.append({'k2_over_mu2_sq':x,'kernel':K,'scaled_k4_kernel_over_mu2_sq':scaled,'abs_error_to_minus_one':abs(scaled+1.0)})
out={
 'iteration':368,
 'mu2_sq':a.mu2_sq,
 'kernel':'1/k^2 - 1/(k^2-mu2^2)',
 'expected_UV':'-mu2^2/k^4',
 'rows':rows,
 'monotone_convergence_to_minus_one':all(rows[i+1]['abs_error_to_minus_one']<rows[i]['abs_error_to_minus_one'] for i in range(len(rows)-1)),
 'worst_highest_scale_error':rows[-1]['abs_error_to_minus_one'],
 'scope':'exact rational asymptotic control away from the spacelike shell; not a loop renormalization computation'
}
with open(a.output,'w') as f: json.dump(out,f,indent=2,sort_keys=True)
print(json.dumps(out,sort_keys=True))

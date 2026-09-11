#!/usr/bin/env python3
import argparse, json, math
p=argparse.ArgumentParser()
p.add_argument('--preset', required=True, choices=['strong','mid','weak','veryweak','alphaclose1','thinlayer'])
p.add_argument('--output', required=True)
a=p.parse_args()
params={
 'strong':(0.1,0.5,0.1),
 'mid':(0.5,0.2,0.01),
 'weak':(0.9,0.1,0.001),
 'veryweak':(0.99,0.05,0.0001),
 'alphaclose1':(0.999,0.2,0.01),
 'thinlayer':(0.5,0.01,0.01),
}
alpha,gamma2,kappa=params[a.preset]
A=kappa*gamma2*abs(math.log(alpha,2))
beta_prime_worst=0.5
n_cross=beta_prime_worst/A
multipliers=[0.1,1.0,2.0,10.0,100.0]
rows=[]
for m in multipliers:
 n=max(1.0,m*n_cross)
 entropy=beta_prime_worst*n*n
 suppression=A*n*n*n
 net=entropy-suppression
 rows.append({'multiple_of_crossover':m,'n':n,'entropy_log2_exponent':entropy,'nonlink_penalty_log2_exponent':suppression,'net_upper_log2_exponent':net})
out={
 'iteration':360,
 'preset':a.preset,
 'alpha':alpha,'gamma2':gamma2,'kappa':kappa,
 'A_kappa_gamma2_abs_log2_alpha':A,
 'beta_prime_worst_bound':beta_prime_worst,
 'crossover_n_beta_over_A':n_cross,
 'rows':rows,
 'n_cubed_penalty_eventually_beats_n_squared_entropy':A>0,
 'scope':'asymptotic source-form stress; not a Monte Carlo path-sum evaluation'
}
with open(a.output,'w') as f: json.dump(out,f,indent=2,sort_keys=True)
print(json.dumps(out,sort_keys=True))

#!/usr/bin/env python3
import argparse, json, math
from pathlib import Path

p=argparse.ArgumentParser()
p.add_argument('--metric', required=True)
p.add_argument('--si-percent', type=float, required=True)
p.add_argument('--dsi-percent', type=float, required=True)
p.add_argument('--n-simulations', type=int, required=True)
p.add_argument('--output', required=True)
a=p.parse_args()
assert a.n_simulations > 0 and 0 < a.si_percent < 100 and 0 < a.dsi_percent < 100

def wilson(phat,n,z=1.959963984540054):
    z2=z*z
    den=1+z2/n
    center=(phat+z2/(2*n))/den
    half=z*math.sqrt(phat*(1-phat)/n+z2/(4*n*n))/den
    return max(0.0,center-half), min(1.0,center+half)

psi=a.si_percent/100.0
pdsi=a.dsi_percent/100.0
ksi=round(psi*a.n_simulations)
kdsi=round(pdsi*a.n_simulations)
si_proxy=ksi/a.n_simulations
dsi_proxy=kdsi/a.n_simulations
si_lo,si_hi=wilson(si_proxy,a.n_simulations)
dsi_lo,dsi_hi=wilson(dsi_proxy,a.n_simulations)
ratio=dsi_proxy/si_proxy
ratio_lo=dsi_lo/si_hi
ratio_hi=dsi_hi/si_lo if si_lo>0 else float('inf')
out={
 'record_type':'mc_precision','metric':a.metric,'n_simulations':a.n_simulations,
 'published_si_probability_proxy':psi,'published_dsi_probability_proxy':pdsi,
 'proxy_si_count':ksi,'proxy_dsi_count':kdsi,
 'proxy_ratio':ratio,
 'si_wilson95':[si_lo,si_hi],'dsi_wilson95':[dsi_lo,dsi_hi],
 'conservative_ratio_interval95':[ratio_lo,ratio_hi],
 'proxy_from_rounded_published_probabilities':True,
 'raw_mc_counts_available':False,
 'classification':'PASS_FINITE_MC_RATIO_REMAINS_DSI_FAVORED' if ratio_lo>1 else 'FINITE_MC_INTERVAL_CROSSES_UNITY'
}
Path(a.output).parent.mkdir(parents=True, exist_ok=True)
Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,sort_keys=True))
if ratio_lo <= 1: raise SystemExit(2)

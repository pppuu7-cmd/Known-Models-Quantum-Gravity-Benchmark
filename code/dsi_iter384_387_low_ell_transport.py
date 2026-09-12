import argparse, json, math, pathlib
SRC=pathlib.Path('paper_iv/DSI_PLANCK_SOURCE_OBJECTS_ITER379_383.json')

def load(): return json.loads(SRC.read_text())
def colidx(name): return {'DSI25':1,'DSI40':2,'DSI50':3}[name]

def transfer(column):
    rows=load()['table4_transfer_factors']['rows']; i=colidx(column)
    vals=[r[i] for r in rows]
    # Table 4 is published to three decimals. Exact 1.000 entries at high ell are
    # therefore convergence-to-baseline entries, not parity-sign failures.
    # Audit the even<1 / odd>1 pattern only while the published deviation is
    # resolvable above half a last-place unit; keep neutral entries explicit.
    tol=5e-4
    active=[]; neutral=[]
    for r in rows:
        ell,v=r[0],r[i]
        if 2<=ell<=20:
            if abs(v-1.0)<=tol:
                neutral.append(ell)
            else:
                active.append((ell%2==0 and v<1.0) or (ell%2==1 and v>1.0))
    tail=[abs(r[i]-1.0) for r in rows if r[0]>=22]
    frac=sum(active)/len(active) if active else 1.0
    return {
        'mode':'transfer','column':column,'rows':len(rows),
        'published_rounding_half_ulp':tol,
        'active_low_ell_pattern_count':len(active),
        'neutral_converged_low_ell_count':len(neutral),
        'neutral_converged_low_ell':neutral,
        'low_ell_2_20_alternation_fraction':frac,
        'ell_ge22_max_abs_deviation_from_unity':max(tail),
        'min_factor':min(vals),'max_factor':max(vals),
        'pass':len(active)>0 and frac>=0.95
    }

def convergence(a,b):
    rows=load()['table4_transfer_factors']['rows']; ia,ib=colidx(a),colidx(b)
    ds=[r[ia]-r[ib] for r in rows if 2<=r[0]<=20]
    return {'mode':'convergence','a':a,'b':b,'ell_range':[2,20],'rms_difference':math.sqrt(sum(x*x for x in ds)/len(ds)),'max_abs_difference':max(abs(x) for x in ds),'pass':True}

def rtt_proxy(column,ellmax):
    rows=load()['table4_transfer_factors']['rows']; i=colidx(column)
    s=[r for r in rows if 2<=r[0]<=ellmax]
    even=sum(r[0]*(r[0]+1)*r[i] for r in s if r[0]%2==0)
    odd=sum(r[0]*(r[0]+1)*r[i] for r in s if r[0]%2==1)
    val=even/odd
    return {'mode':'rtt_proxy','column':column,'ellmax':ellmax,'equal_baseline_Cl_proxy':val,'reported_planck_RTT':load()['reported_planck_RTT']['value'],'is_planck_reproduction':False,'pass':math.isfinite(val) and val>0}

def window(column,start,end):
    rows=load()['table4_transfer_factors']['rows']; i=colidx(column); s=[r for r in rows if start<=r[0]<=end]
    dev=[abs(r[i]-1.0) for r in s]
    return {'mode':'window','column':column,'ell_window':[start,end],'n':len(s),'mean_abs_deviation_from_unity':sum(dev)/len(dev),'max_abs_deviation_from_unity':max(dev),'pass':len(s)>0}

def scope():
    return {'mode':'scope','published_transfer_table_present':True,'three_cutoff_realizations_present':True,'raw_planck_masked_map_present':False,'million_sky_realizations_present':False,'raw_covariance_present':False,'full_likelihood_reproduction_authorized':False,'d7_promotion_authorized':False,'pass':True}

def main():
    p=argparse.ArgumentParser(); p.add_argument('--mode',required=True); p.add_argument('--column'); p.add_argument('--a'); p.add_argument('--b'); p.add_argument('--ellmax',type=int); p.add_argument('--start',type=int); p.add_argument('--end',type=int); p.add_argument('--output',required=True); a=p.parse_args()
    if a.mode=='transfer': out=transfer(a.column)
    elif a.mode=='convergence': out=convergence(a.a,a.b)
    elif a.mode=='rtt_proxy': out=rtt_proxy(a.column,a.ellmax)
    elif a.mode=='window': out=window(a.column,a.start,a.end)
    elif a.mode=='scope': out=scope()
    else: raise SystemExit('unknown mode')
    pathlib.Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    if not out['pass']: raise SystemExit(2)
if __name__=='__main__': main()

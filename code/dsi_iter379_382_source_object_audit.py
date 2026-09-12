import argparse, json, math, pathlib

SRC = pathlib.Path('paper_iv/DSI_PLANCK_SOURCE_OBJECTS_ITER379_383.json')

def load():
    return json.loads(SRC.read_text())

def ratio_audit(table_name, key):
    d=load()[table_name][key]
    computed=d['DSI']/d['SI']
    rel=abs(computed-d['reported_ratio'])/d['reported_ratio']
    return {'mode':'ratio','table':table_name,'key':key,'SI':d['SI'],'DSI':d['DSI'],'computed_ratio':computed,'reported_ratio':d['reported_ratio'],'relative_rounding_difference':rel,'pass':rel<0.03}

def transfer_audit(column):
    data=load()['table4_transfer_factors']
    idx={'DSI25':1,'DSI40':2,'DSI50':3}[column]
    rows=data['rows']
    vals=[r[idx] for r in rows]
    alternating=[]
    for r in rows:
        ell=r[0]; v=r[idx]
        if ell>=2 and ell<=20:
            alternating.append((ell%2==0 and v<1.0) or (ell%2==1 and v>1.0))
    tail=[abs(r[idx]-1.0) for r in rows if r[0]>=22]
    return {'mode':'transfer','column':column,'n_rows':len(rows),'low_ell_2_20_alternation_fraction':sum(alternating)/len(alternating),'tail_ell_ge22_max_abs_deviation_from_unity':max(tail),'pass':sum(alternating)/len(alternating)>=0.95}

def convergence_audit(pair):
    data=load()['table4_transfer_factors']; rows=data['rows']
    ia,ib={'25':1,'40':2,'50':3}[pair[:2]],{'25':1,'40':2,'50':3}[pair[-2:]]
    ds=[r[ia]-r[ib] for r in rows if 2<=r[0]<=20]
    rms=math.sqrt(sum(x*x for x in ds)/len(ds))
    maxabs=max(abs(x) for x in ds)
    return {'mode':'convergence','pair':pair,'ell_range':[2,20],'rms_difference':rms,'max_abs_difference':maxabs,'pass':math.isfinite(rms)}

def proxy_rtt(column, ellmax):
    data=load()['table4_transfer_factors']; idx={'DSI25':1,'DSI40':2,'DSI50':3}[column]
    selected=[r for r in data['rows'] if 2<=r[0]<=ellmax]
    even=sum(r[0]*(r[0]+1)*r[idx] for r in selected if r[0]%2==0)
    odd=sum(r[0]*(r[0]+1)*r[idx] for r in selected if r[0]%2==1)
    value=even/odd
    return {'mode':'proxy_rtt','column':column,'ellmax':ellmax,'equal_baseline_Cl_proxy':value,'reported_planck_RTT':load()['reported_planck_RTT']['value'],'scientific_boundary':'This is an equal-baseline-C_l transport proxy, not a reproduction of Planck R_TT.','pass':value<1.0}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--mode',required=True); ap.add_argument('--table'); ap.add_argument('--key'); ap.add_argument('--column'); ap.add_argument('--pair'); ap.add_argument('--ellmax',type=int,default=20); ap.add_argument('--output',required=True); a=ap.parse_args()
    if a.mode=='ratio': out=ratio_audit(a.table,a.key)
    elif a.mode=='transfer': out=transfer_audit(a.column)
    elif a.mode=='convergence': out=convergence_audit(a.pair)
    elif a.mode=='proxy_rtt': out=proxy_rtt(a.column,a.ellmax)
    else: raise SystemExit('bad mode')
    pathlib.Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    if not out['pass']: raise SystemExit(2)

if __name__=='__main__': main()

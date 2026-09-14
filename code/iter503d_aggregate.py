#!/usr/bin/env python3
import argparse, glob, json, os
EXPECTED={0,7,15}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--root',required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    rows=[]
    for p in glob.glob(os.path.join(a.root,'**','iter503d-box*.json'),recursive=True):
        with open(p) as f: x=json.load(f)
        x['_path']=p; rows.append(x)
    boxes={int(x['box']) for x in rows if 'box' in x}
    unique=len(rows)==len(boxes)
    total=sum(int(x.get('completed_identities',0)) for x in rows)
    complete=bool(unique and boxes==EXPECTED and total==1440 and all(x.get('controls',{}).get('complete') for x in rows))
    cs=[x.get('classification') for x in rows]
    if not complete or any(c=='ITER503D_INVALID_OR_BLOCKED' for c in cs): cls='ITER503D_INVALID_OR_BLOCKED'
    elif any(c=='ITER503D_DUAL_SOURCE_IDENTITY_VIOLATION' for c in cs): cls='ITER503D_DUAL_SOURCE_IDENTITY_VIOLATION'
    elif all(c=='ITER503D_DUAL_SOURCE_IDENTITY_CONFIRMED' for c in cs): cls='ITER503D_DUAL_SOURCE_IDENTITY_CONFIRMED'
    else: cls='ITER503D_INVALID_OR_BLOCKED'
    out={'iteration':'503D','classification':cls,'expected_boxes':sorted(EXPECTED),'observed_boxes':sorted(boxes),'expected_identities':1440,'completed_identities':total,
         'lanes':[{'box':x.get('box'),'classification':x.get('classification'),'completed_identities':x.get('completed_identities'),'value_all_contain_zero':x.get('value_all_contain_zero'),'derivative_all_contain_zero':x.get('derivative_all_contain_zero')} for x in sorted(rows,key=lambda z:int(z.get('box',-1)))],
         'scope':'Iter503 derivative implementation audit only; no science/D7/selector verdict'}
    os.makedirs(os.path.dirname(a.out) or '.',exist_ok=True)
    with open(a.out,'w') as f: json.dump(out,f,indent=2,sort_keys=True)
    print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__': main()

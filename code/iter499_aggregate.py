#!/usr/bin/env python3
import argparse, collections, glob, json, math, os

EXPECTED=[f'{c}-b{b}' for c in ['0to5','1to4','2to3'] for b in range(4)]


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--root',required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    rows=[]
    for p in sorted(glob.glob(os.path.join(a.root,'**','*.json'),recursive=True)):
        with open(p) as f: x=json.load(f)
        if x.get('iteration')==499: rows.append(x)
    ids=[x.get('job') for x in rows]
    counts=collections.Counter(ids)
    missing=sorted(set(EXPECTED)-set(ids)); duplicates=sorted(k for k,v in counts.items() if v!=1)
    blocker=[x.get('job') for x in rows if x.get('method_blocker') or not x.get('valid',False)]
    structure_ok=bool(len(rows)==12 and not missing and not duplicates)
    classes=[]; min_s=math.inf; max_s=-math.inf; max_d=-math.inf; min_beta=math.inf; min_chart=math.inf
    max_possible=0; crossing=[]; nboxes=0; point_fail=[]
    for x in rows:
        if not x.get('point_regression_all_pass',False): point_fail.append(x.get('job'))
        if x.get('min_beta_lower') is not None: min_beta=min(min_beta,float(x['min_beta_lower']))
        if x.get('min_chart_norm2_lower') is not None: min_chart=min(min_chart,float(x['min_chart_norm2_lower']))
        for p in x.get('paths',[]):
            d=p.get('direction'); sg=p.get('sign')
            for b in p.get('boxes',[]):
                if b.get('error'): continue
                nboxes+=1
                for q in b.get('per_rho',[]):
                    classes.append(q['classification']); min_s=min(min_s,float(q['S_lower'])); max_s=max(max_s,float(q['S_upper'])); max_d=max(max_d,float(q['drift_upper']))
                if x.get('causal')=='0to5' and d==[1,1,1,-1,-1,-1] and sg==1 and b.get('amp_upper',0)>=0.00234375:
                    crossrec={'job':x.get('job'),'box':b.get('box'),'amp_lower':b.get('amp_lower'),'amp_upper':b.get('amp_upper'),'R':[]}
                    for rr in b.get('per_R',[]):
                        if rr.get('R') in (10,12):
                            for q in rr.get('rho',[]):
                                max_possible=max(max_possible,int(q.get('possible_max_count',0)))
                                if abs(float(q.get('rho',0))-2.7)<1e-12:
                                    crossrec['R'].append({'R':rr['R'],'possible_max_indices':q.get('possible_max_indices',[]),'count':q.get('possible_max_count')})
                        else:
                            for q in rr.get('rho',[]): max_possible=max(max_possible,int(q.get('possible_max_count',0)))
                    crossing.append(crossrec)
                else:
                    for rr in b.get('per_R',[]):
                        for q in rr.get('rho',[]): max_possible=max(max_possible,int(q.get('possible_max_count',0)))
    method_block=bool((not structure_ok) or blocker or point_fail)
    if method_block:
        cls='ITER499_NUMERICAL_METHOD_BLOCKER'
    elif classes and all(c=='INTERVAL_ROBUST_NONDECAY' for c in classes):
        cls='ITER499_DIRECT_MAX_ENVELOPE_INTERVAL_ROBUST_QUALIFIED_SCOPED'
    elif classes and all(c in ('INTERVAL_ROBUST_NONDECAY','INTERVAL_NONDECAY') for c in classes):
        cls='ITER499_DIRECT_MAX_ENVELOPE_INTERVAL_NONDECAY_QUALIFIED_SCOPED'
    elif any(c=='INTERVAL_UNIFORM_DECAY_WITNESS' for c in classes):
        cls='SCIENTIFIC_FAIL_ITER499_UNIFORM_NONDECAY_INTERVAL'
    else:
        cls='ITER499_VALIDATED_INTERVAL_INCONCLUSIVE_SCOPED'
    cc=collections.Counter(classes)
    out={'iteration':499,'classification':cls,'valid_structure':structure_ok,'method_blocker':method_block,
         'n_jobs':len(rows),'job_ids':ids,'missing_job_ids':missing,'duplicate_job_ids':duplicates,'blocker_job_ids':blocker,'point_regression_fail_job_ids':point_fail,
         'n_direction_boxes':nboxes,'n_rho_box_states':len(classes),'class_counts':dict(cc),
         'global_min_S_lower':None if not classes else min_s,'global_max_S_upper':None if not classes else max_s,
         'global_max_drift_upper':None if not classes else max_d,
         'global_min_beta_lower':None if min_beta is math.inf else min_beta,'global_min_chart_norm2_lower':None if min_chart is math.inf else min_chart,
         'max_possible_max_channel_count':max_possible,'known_crossing_region':crossing,
         'jobs':[{'job':x.get('job'),'classification':x.get('classification'),'valid':x.get('valid'),'method_blocker':x.get('method_blocker'),'point_regression':x.get('point_regression_all_pass')} for x in rows],
         'scope':'validated direct 243-channel max-envelope on 16 q=1 amplitude subintervals along eight frozen signed directions only; no 6-D/20-D neighborhood or absolute-Haar theorem'}
    os.makedirs(os.path.dirname(a.out) or '.',exist_ok=True)
    with open(a.out,'w') as f: json.dump(out,f,indent=2,sort_keys=True)
    print(json.dumps(out,indent=2,sort_keys=True)); raise SystemExit(0)
if __name__=='__main__': main()

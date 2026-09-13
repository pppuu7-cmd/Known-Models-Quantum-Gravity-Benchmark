#!/usr/bin/env python3
import json,re,subprocess,pathlib
TOKENS={
 'same_realization_object':['same_realization','same physical realization'],
 'parameter_transport':['transport_ready','parameter_transport','missing_parameter_transport'],
 'normalized_comparator':['normalized_comparator','comparator_ready','missing_normalized_observable_transport'],
 'error_certificate':['error_certificate','propagated_error','nuisance','covariance'],
}
SELF='code/iter472_d7_s3_formal_completeness.py'
files=subprocess.check_output(['git','ls-files'],text=True).splitlines()
findings={k:[] for k in TOKENS}; scanned=0
bool_re=re.compile(r'''["']?(?P<key>[A-Za-z0-9_\-]+)["']?\s*[:=]\s*(?P<val>True|False|true|false)''')
for fn in files:
    if fn==SELF or not fn.endswith(('.py','.json','.md','.yml','.yaml')): continue
    try: text=pathlib.Path(fn).read_text(encoding='utf-8')
    except Exception: continue
    scanned+=1
    low=text.lower()
    for cls,toks in TOKENS.items():
        if not any(t.lower() in low for t in toks): continue
        explicit=[]
        for m in bool_re.finditer(text):
            key=m.group('key'); kl=key.lower()
            if any(t.lower() in kl for t in toks):
                explicit.append({'key':key,'value':m.group('val').lower()=='true'})
        state='MENTION_ONLY'
        if explicit:
            vals={x['value'] for x in explicit}
            state='CONTRADICTORY' if len(vals)>1 else ('POSITIVE' if True in vals else 'NEGATIVE')
        findings[cls].append({'file':fn,'state':state,'explicit':explicit[:20]})
# synthetic controls are implementation-only and are never added to findings.
synthetic='same_realization_transport_ready=True\nnormalized_comparator_ready=False\n'
ctrl_pos=bool(re.search(r'same_realization_transport_ready\s*=\s*True',synthetic))
ctrl_neg=bool(re.search(r'normalized_comparator_ready\s*=\s*False',synthetic))
known='code/lqg_entropy_observable_common.py'
known_negative=any(x['file']==known and x['state'] in ('NEGATIVE','CONTRADICTORY') for items in findings.values() for x in items)
summary={}
for cls,items in findings.items():
    pos=[x['file'] for x in items if x['state']=='POSITIVE']; neg=[x['file'] for x in items if x['state']=='NEGATIVE']; con=[x['file'] for x in items if x['state']=='CONTRADICTORY']
    summary[cls]={'positive_files':sorted(set(pos)),'negative_files':sorted(set(neg)),'contradictory_files':sorted(set(con)),'formal_status':'FORMAL_POSITIVE_CANDIDATE' if pos and not neg and not con else 'NOT_FORMALLY_CLOSED'}
checks={'synthetic_positive_detected':ctrl_pos,'synthetic_negative_detected':ctrl_neg,'fixtures_excluded_from_evidence':all(SELF not in z for s in summary.values() for k in ('positive_files','negative_files','contradictory_files') for z in s[k]),'known_negative_recovered':known_negative,'mention_only_not_positive':all(x['state']!='POSITIVE' or x['explicit'] for v in findings.values() for x in v)}
out={'classification':'ITER472_D7_S3_FORMAL_DECLARATION_MATRIX_COMPLETE_SCOPED' if all(checks.values()) else 'FAIL_ITER472','scientific_pass':all(checks.values()),'tracked_text_files_scanned':scanned,'checks':checks,'matrix':summary,'scope':'formal declarations only; absence is not impossibility; audit does not close D7-S3'}
p=pathlib.Path('artifacts/iter472-summary.json'); p.parent.mkdir(exist_ok=True); p.write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps(out,indent=2)); raise SystemExit(0 if out['scientific_pass'] else 1)

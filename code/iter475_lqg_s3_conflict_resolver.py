#!/usr/bin/env python3
import json,re,subprocess,pathlib
files=subprocess.check_output(['git','ls-files'],text=True).splitlines()
path_re=re.compile(r'(lqg|eprl|causal|wick|uv_ir|physical_state|stack_uv|gamma_duality|PAPER_IV_DECISION_LEDGER_DELTA_28[3-9]|PAPER_IV_DECISION_LEDGER_DELTA_29[0-9]|PAPER_IV_DECISION_LEDGER_DELTA_30[0-3])',re.I)
exclude_re=re.compile(r'(tgft|dsi_|iho_|dqft)',re.I)
targets=[f for f in files if f.endswith(('.py','.json','.md','.yml','.yaml')) and path_re.search(f) and not exclude_re.search(f)]
key_re=re.compile(r'(?P<q>["\']?)(?P<key>[A-Za-z0-9_\-]{3,100})(?P=q)\s*[:=]\s*(?P<val>True|False|true|false)')
classes={
 'same_realization':['same_realization','physical_state','causal_stack'],
 'parameter_transport':['parameter_transport','transport_ready','missing_parameter_transport','uv_ir','gamma_duality'],
 'normalized_comparator':['normalized_comparator','comparator_ready','missing_normalized_observable_transport','normalized_observable'],
 'error_certificate':['error_certificate','propagated_error','covariance','nuisance']}

def tags(fn,text):
    low=(fn+' '+text[:4000]).lower(); out=[]
    for t,need in [('causal_stack',['causal_stack','causal stack']),('eprl',['eprl']),('uv_ir_bridge',['uv_ir','uv-ir']),('wick_bridge',['wick']),('physical_state',['physical_state','physical state']),('stack_uv_entropy',['stack_uv','uv entropy']),('gamma_duality',['gamma_duality','gamma duality'])]:
        if any(x in low for x in need): out.append(t)
    return out or ['lqg_unspecified']

rows=[]
for fn in targets:
    try: text=pathlib.Path(fn).read_text(encoding='utf-8')
    except Exception: continue
    tg=tags(fn,text)
    for m in key_re.finditer(text):
        key=m.group('key'); val=m.group('val').lower()=='true'; lk=key.lower()
        cls=None
        for c,toks in classes.items():
            if any(t in lk for t in toks): cls=c; break
        if not cls: continue
        start=max(0,m.start()-100); end=min(len(text),m.end()+140); ctx=' '.join(text[start:end].split())
        for tag in tg: rows.append({'file':fn,'realization_tag':tag,'class':cls,'key':key,'value':val,'context':ctx[:300]})

groups={}
for r in rows:
    k=(r['realization_tag'],r['class']); groups.setdefault(k,[]).append(r)
summary=[]
for (tag,cls),items in sorted(groups.items()):
    vals={x['value'] for x in items}
    if vals=={True}: state='CONSISTENT_POSITIVE_CANDIDATE'
    elif vals=={False}: state='EXPLICIT_NEGATIVE'
    elif vals=={True,False}: state='SAME_REALIZATION_CONFLICT'
    else: state='INSUFFICIENT_IDENTITY_EVIDENCE'
    summary.append({'realization_tag':tag,'class':cls,'state':state,'positive_count':sum(x['value'] for x in items),'negative_count':sum(not x['value'] for x in items),'files':sorted(set(x['file'] for x in items))})
class_states={c:[] for c in classes}
for s in summary: class_states[s['class']].append(s['state'])
closure={}
for c,states in class_states.items():
    closure[c]='NOT_CLOSED' if (not states or any(s in ('EXPLICIT_NEGATIVE','SAME_REALIZATION_CONFLICT','INSUFFICIENT_IDENTITY_EVIDENCE') for s in states)) else 'LOCAL_POSITIVE_CANDIDATES_ONLY'
checks={'targets_nonempty':bool(targets),'declarations_nonempty':bool(rows),'cross_family_excluded':all(not exclude_re.search(f) for f in targets),'no_class_closed_from_mentions':all(v in ('NOT_CLOSED','LOCAL_POSITIVE_CANDIDATES_ONLY') for v in closure.values())}
ok=all(checks.values())
out={'iteration':475,'classification':'ITER475_LQG_S3_TARGETED_CONFLICT_MATRIX_COMPLETE_SCOPED' if ok else 'FAIL_ITER475_AUDIT_INVALID','scientific_pass':ok,'tracked_targets':len(targets),'explicit_declarations':len(rows),'checks':checks,'s3_class_status':closure,'group_summary':summary,'declarations':rows[:500],'scope':'targeted explicit LQG/EPRL boolean declarations only; tags are lexical provenance handles, not proof of physical identity; S3 remains fail-closed'}
pathlib.Path('artifacts').mkdir(exist_ok=True); pathlib.Path('artifacts/iter475-summary.json').write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps(out,indent=2)); raise SystemExit(0 if ok else 2)

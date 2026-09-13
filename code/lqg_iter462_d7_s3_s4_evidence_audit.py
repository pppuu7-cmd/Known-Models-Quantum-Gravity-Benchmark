import argparse, json, os, pathlib, subprocess

GATES={
'S3':['same_realization_parameter_transport','normalized_comparator_error_certificate','causal_stack_physical_realization','stack_parameter_weight_transport'],
'S4':['universal_stack_domain_inclusion','causal_stack_cutoff_domain','global_common_domain_normalization']}
EXT={'.md','.json','.py','.yml','.yaml','.txt','.csv'}
FORMAL=('code/','protocol/','benchmarks/')
MENTION=('recovery/','results/','docs/')

def tracked():
    out=subprocess.check_output(['git','ls-files'],text=True)
    return [p.strip() for p in out.splitlines() if p.strip()]

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--out',default='iter462_summary.json'); a=ap.parse_args()
    rows=[]; scanfiles=[]
    for p in tracked():
        if 'iter462' in p.lower(): continue
        if pathlib.Path(p).suffix.lower() not in EXT: continue
        try: text=pathlib.Path(p).read_text(encoding='utf-8',errors='ignore')
        except Exception: continue
        scanfiles.append(p)
        low=text.lower()
        for stage,gates in GATES.items():
            for gate in gates:
                if gate.lower() in low:
                    kind='formal_candidate' if p.startswith(FORMAL) else ('mention_only' if p.startswith(MENTION) else 'other_mention')
                    rows.append({'stage':stage,'gate':gate,'path':p,'kind':kind})
    report={}
    for stage,gates in GATES.items():
        report[stage]={}
        for gate in gates:
            hits=[r for r in rows if r['stage']==stage and r['gate']==gate]
            formal=sorted({r['path'] for r in hits if r['kind']=='formal_candidate'})
            mentions=sorted({r['path'] for r in hits if r['kind']!='formal_candidate'})
            report[stage][gate]={'formal_candidate_files':formal,'mention_files':mentions,'status':'CANDIDATE_ARTIFACT_PRESENT_NEEDS_REVIEW' if formal else 'NO_FORMAL_ARTIFACT_FOUND_IN_TRACKED_SNAPSHOT','auto_close':False}
    all_gates=sum((v for v in GATES.values()),[])
    ok=len(report['S3'])==4 and len(report['S4'])==3 and all(report[s][g]['auto_close'] is False for s in report for g in report[s])
    out={'iteration':462,'tracked_text_files_scanned':len(scanfiles),'hit_records':len(rows),'report':report,
         'classification':'ITER462_D7_S3_S4_EVIDENCE_LOCALIZATION_COMPLETE_SCOPED' if ok else 'INFRASTRUCTURE_OR_NUMERICAL_FAIL',
         'pass':ok,'gate_count':len(all_gates),'scope':'Repository-snapshot evidence localization only. Mentions/candidates do not close gates. D7-S5 remains NOT_AUTHORIZED; Candidate Gravity inactive.'}
    os.makedirs(os.path.dirname(a.out) or '.',exist_ok=True); json.dump(out,open(a.out,'w'),indent=2); print(json.dumps(out,indent=2))
if __name__=='__main__': main()

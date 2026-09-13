#!/usr/bin/env python3
import glob,json,os
expected=[f'{p}-{r}-{c}' for p in 'ABCD' for r in ['mild','strong'] for c in ['0to5','1to4','2to3']]
rows=[]; invalid=[]; failed=[]; missing=[]
for lane in expected:
    fs=glob.glob(f'artifacts/**/iter485-{lane}.json',recursive=True)+glob.glob(f'artifacts/iter485-{lane}.json')
    if not fs:
        missing.append(lane); continue
    try: x=json.load(open(fs[0])); rows.append(x)
    except Exception as e: invalid.append({'lane':lane,'error':repr(e)}); continue
    if not x.get('valid'): invalid.append({'lane':lane,'classification':x.get('classification'),'error':x.get('error')})
    elif not x.get('pass'): failed.append({'lane':lane,'classification':x.get('classification'),'tests':x.get('tests')})
passed=(not missing and not invalid and not failed and len(rows)==len(expected))
classification=('ITER485_SHARED_NODE_TEN_EDGE_TOLLER_MAGNETIC_NETWORK_QUALIFIED_SCOPED' if passed else
                'SCIENTIFIC_FAIL_ITER485_TEN_EDGE_TOLLER_NETWORK' if not missing and not invalid else
                'BLOCKED_OR_INFRASTRUCTURE_ITER485')
out={'iteration':485,'expected_lanes':len(expected),'present_lanes':len(rows),'missing':missing,'invalid':invalid,'scientific_fail_lanes':failed,'pass':passed,'classification':classification,
     'max_cycle_residual':max([x.get('cycle_residual',0) for x in rows],default=None),
     'max_kak_reconstruction':max([x.get('kak_reconstruction_max',0) for x in rows],default=None),
     'max_additive_identity':max([x.get('additive_identity_max',0) for x in rows],default=None),
     'max_reindex_residual':max([x.get('reindex_residual_max',0) for x in rows],default=None),
     'min_nonzero_witness':min([min([q.get('max_normalized_witness',float('inf')) for q in x.get('rho_rows',[])],default=float('inf')) for x in rows],default=None),
     'min_independent_edge_cycle_break':min([x.get('independent_edge_cycle_residual',float('inf')) for x in rows],default=None),
     'min_nonrepresentation_max':min([x.get('nonrepresentation_max',float('inf')) for x in rows],default=None),
     'scope':'Iter485 frozen j=1 shared-node ten-edge pre-Haar/pre-spectral network only'}
os.makedirs('artifacts',exist_ok=True)
json.dump(out,open('artifacts/iter485-summary.json','w'),indent=2,sort_keys=True)
print(json.dumps(out,indent=2,sort_keys=True))

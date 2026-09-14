#!/usr/bin/env python3
import argparse, collections, glob, json, math, os

PANELS=['T0','T1','T2']; CAUSALS=['0to5','1to4','2to3']; RHOS=[7,8]
EXPECTED=[f'{p}-{c}-rho{r}' for p in PANELS for c in CAUSALS for r in RHOS]
PASS='ITER504_FIXED_CAUSAL_K5_FULL_COLLISION_LEADING_CONTRACTION_SURVIVES_QUALIFIED_SCOPED'
FAIL='SCIENTIFIC_FAIL_ITER504_UNIFORM_FROZEN_FULL_COLLISION_LEADING_SURVIVAL'
BLOCK='BLOCKED_OR_INFRASTRUCTURE_ITER504'


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--root',required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    rows=[]
    for p in sorted(glob.glob(os.path.join(a.root,'**','*.json'),recursive=True)):
        with open(p) as f: x=json.load(f)
        if x.get('iteration')==504 and x.get('lane'): rows.append(x)
    ids=[x.get('lane') for x in rows]; cnt=collections.Counter(ids)
    missing=sorted(set(EXPECTED)-set(ids)); dup=sorted(k for k,v in cnt.items() if v!=1)
    structure=bool(len(rows)==18 and not missing and not dup)
    blocked=[x.get('lane') for x in rows if x.get('classification')==BLOCK or not x.get('valid',False)]
    failed=[x.get('lane') for x in rows if x.get('classification')==FAIL]
    passed=[x.get('lane') for x in rows if x.get('classification')==PASS and x.get('valid',False) and x.get('max_ratio',0)>1e-12]
    if not structure or blocked:
        cls=BLOCK; scientific_pass=False
    elif failed or len(passed)!=18:
        cls=FAIL; scientific_pass=False
    else:
        cls=PASS; scientific_pass=True
    maxrat=[float(x['max_ratio']) for x in rows if x.get('max_ratio') is not None]
    minrat=min(maxrat) if maxrat else None
    finerr=[float(x['finite_t_fine_max_relative_error']) for x in rows if x.get('finite_t_fine_max_relative_error') is not None]
    out={
      'iteration':504,'classification':cls,'scientific_pass':scientific_pass,'valid_structure':structure,
      'n_jobs':len(rows),'missing_job_ids':missing,'duplicate_job_ids':dup,'blocked_job_ids':blocked,'scientific_fail_job_ids':failed,'qualified_job_ids':passed,
      'minimum_lane_max_ratio':minrat,'global_max_finite_t_fine_relative_error':max(finerr) if finerr else None,
      'global_min_leading_coefficient_abs':min([float(x['min_beta_leading_coefficient_abs']) for x in rows if x.get('min_beta_leading_coefficient_abs') is not None],default=None),
      'global_max_axial_section_residual':max([float(x.get('axial_section_relative_residual',0.0)) for x in rows],default=None),
      'global_max_scale_ratio_residual':max([float(x.get('ratio_scale_invariance_relative_residual',0.0)) for x in rows],default=None),
      'global_max_reindex_residual':max([float(x.get('magnetic_reindex_relative_residual',0.0)) for x in rows],default=None),
      'total_nonzero_witnesses_gt_1e-12':sum(int(x.get('nonzero_witnesses_gt_1e-12',0)) for x in rows),
      'jobs':[{'lane':x.get('lane'),'classification':x.get('classification'),'valid':x.get('valid'),'max_ratio':x.get('max_ratio'),'max_channel':x.get('max_channel'),'nonzero':x.get('nonzero_witnesses_gt_1e-12'),'fine_error':x.get('finite_t_fine_max_relative_error')} for x in rows],
      'scope':'fixed-causal j=1 full-K5 common-node full-collision leading coefficient on frozen tangent panels only; no remainder, positive-measure, local-integrability, Haar, spectral-pairing or physical-vertex theorem'
    }
    os.makedirs(os.path.dirname(a.out) or '.',exist_ok=True)
    with open(a.out,'w') as f: json.dump(out,f,indent=2,sort_keys=True)
    print(json.dumps(out,indent=2,sort_keys=True)); raise SystemExit(0)

if __name__=='__main__': main()

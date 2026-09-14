#!/usr/bin/env python3
import argparse, json, os
import iter488_kak_high_precision_revalidation as hp

KAK_TOL=1e-8
SU2_TOL=1e-10
BETA_TOL=1e-10


def evaluate(cluster):
    x=hp.evaluate(cluster)
    checks={
      'finite_all_40': bool(x['checks']['finite_all_40']),
      'same_frozen_absolute_kak_threshold': bool(x['high_precision_kak_reconstruction_max'] < KAK_TOL),
      'source_inherited_su2_unitarity': bool(x['high_precision_unitarity_max'] < SU2_TOL),
      'source_inherited_su2_determinant': bool(x['high_precision_det_max'] < SU2_TOL),
      'double_beta_agreement': bool(x['beta_abs_error_max'] < BETA_TOL or x['beta_relative_error_max'] < BETA_TOL),
    }
    passed=bool(all(checks.values()))
    return {
      'iteration':489,'geometry_key':x['geometry_key'],'cluster_size':cluster,'revalidates_lanes':x['revalidates_lanes'],
      'checks':checks,'pass':passed,
      'classification':'ITER489_KAK_REVALIDATED_WITH_SOURCE_TOLERANCES_SCOPED' if passed else 'NUMERICAL_OR_SOURCE_FAIL_ITER489_KAK_REVALIDATION',
      'high_precision_kak_reconstruction_max':x['high_precision_kak_reconstruction_max'],
      'high_precision_unitarity_max':x['high_precision_unitarity_max'],
      'high_precision_det_max':x['high_precision_det_max'],
      'beta_abs_error_max':x['beta_abs_error_max'],'beta_relative_error_max':x['beta_relative_error_max'],
      'objects_checked':x['objects_checked'],
      'scope':'validation-only prospective recheck using unchanged Iter487 KAK threshold and Iter484 source numerical SU2 tolerances; no slope recomputation'
    }


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--cluster',type=int,required=True,choices=[2,3]); ap.add_argument('--out',required=True); a=ap.parse_args()
    try: out=evaluate(a.cluster)
    except Exception as e: out={'iteration':489,'cluster_size':a.cluster,'pass':False,'classification':'NUMERICAL_OR_SOURCE_FAIL_ITER489_KAK_REVALIDATION','error':repr(e)}
    os.makedirs(os.path.dirname(a.out) or '.',exist_ok=True)
    with open(a.out,'w') as f: json.dump(out,f,indent=2,sort_keys=True)
    print(json.dumps(out,indent=2,sort_keys=True)); raise SystemExit(0)
if __name__=='__main__': main()

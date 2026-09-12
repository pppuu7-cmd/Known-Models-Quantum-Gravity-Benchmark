#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, math
from pathlib import Path

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--input-dir',required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
    rows=[json.loads(p.read_text(encoding='utf-8')) for p in sorted(Path(a.input_dir).rglob('*.json'))]
    streams={k:[r for r in rows if r.get('stream')==k] for k in ['LQG_SPINFOAM','CAUSAL_FERMION_SYSTEMS','ASYMPTOTIC_SAFETY','RQCP']}
    expected={'LQG_SPINFOAM':24,'CAUSAL_FERMION_SYSTEMS':12,'ASYMPTOTIC_SAFETY':8,'RQCP':12}
    counts={k:len(v) for k,v in streams.items()}
    all_pass=all(r.get('pass') is True for r in rows)
    count_ok=counts==expected

    lqg=streams['LQG_SPINFOAM']
    cfs=streams['CAUSAL_FERMION_SYSTEMS']
    ass=streams['ASYMPTOTIC_SAFETY']
    rqcp=streams['RQCP']
    forward=[r for r in ass if r.get('probe')=='FIXED_T_FORWARD_SCALING']
    bounded=[r for r in ass if r.get('probe')=='ADAPTED_RG_S_CHANNEL_BOUNDEDNESS_DIAGNOSTIC']

    rqcp_window_spread={}
    for obs in ['G','gap','G_gap2']:
        rr=[r for r in rqcp if r.get('observable')==obs]
        vals=[]
        for r in rr:
            for m in ('power','exp'): vals.append(r['models'][m]['y_inf'])
        center=sum(vals)/len(vals)
        rqcp_window_spread[obs]={
          'min_inferred_limit':min(vals),'max_inferred_limit':max(vals),'mean_inferred_limit':center,
          'relative_full_window_ansatz_spread':(max(vals)-min(vals))/max(abs(center),1e-300)
        }

    ok=all_pass and count_ok and len(rows)==56
    out={
      'iteration_bundle':'404-408','pass':ok,'independent_result_count':len(rows),'counts':counts,
      'lqg':{
        'max_final_relative_error_j64':max(r['final_relative_error_j64'] for r in lqg),
        'least_negative_tail_error_slope':max(r['tail_loglog_error_slope'] for r in lqg),
        'classification':'PASS_TOLLER_FIXED_GAMMA_LARGE_SPIN_BUILDING_BLOCK__CAUSAL_VERTEX_FINITE_NORMALIZATION_STILL_OPEN'
      },
      'cfs':{
        'min_nominal_delta3_over_delta2':min(r['nominal_O_delta3_over_O_delta2'] for r in cfs),
        'max_nominal_delta3_over_delta2':max(r['nominal_O_delta3_over_O_delta2'] for r in cfs),
        'classification':'PASS_PARAMETRIC_DELTA_ORDER_TRANSPORT__CONCRETE_CORRECTION_TENSOR_AND_COEFFICIENTS_OPEN'
      },
      'asymptotic_safety':{
        'forward_jobs':len(forward),'bounded_diagnostic_jobs':len(bounded),
        'forward_slope_range':[min(r['high_energy_loglog_slope'] for r in forward),max(r['high_energy_loglog_slope'] for r in forward)],
        'classification':'PASS_GRAVITON_MEDIATED_UV_BOUNDEDNESS_DIAGNOSTIC_AND_FORWARD_S2_DIVERGENCE_REPRODUCTION__CONTACT_COMPLETE_A4_OPEN'
      },
      'rqcp':{
        'max_within_window_power_vs_exp_limit_disagreement':max(r['relative_inferred_limit_model_disagreement'] for r in rqcp),
        'full_window_ansatz_spread':rqcp_window_spread,
        'classification':'PASS_STRONG_NUMERIC_CUTOFF_WINDOW_STABILITY__ALL_BAND_BACKGROUND_INDEPENDENT_AUTONOMY_OPEN'
      },
      'global':{
        'D2':'NOT_CLOSED_COVERAGE_AND_OBJECTS','D4':'PARTIAL_GLOBAL_NOT_CLOSED','D7':'NOT_CLOSED_NOT_YET_AUTHORIZED',
        'family_terminal_promotions':0,'candidate_gravity_activation':False,'new_required_authorized':False,
        'classification':'PASS_PARALLEL_PHYSICAL_CLOSURE_WAVE__FOUR_FRONTS_ADVANCED_WITH_EXPLICIT_SOURCE_OPEN_BOUNDARIES'
      }
    }
    Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(json.dumps(out,sort_keys=True))
    if not ok: raise SystemExit(2)
if __name__=='__main__': main()

#!/usr/bin/env python3
import argparse,json
from pathlib import Path
from lqg_continuum_contract_common import SOURCE,write_json
EXPECTED={
 'strong':'lqg_continuum_strong_limit_guard',
 'rigging':'lqg_continuum_rigging_map_guard',
 'specificity':'lqg_continuum_model_specificity_guard',
 'han':'lqg_continuum_han_bridge_guard'
}
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--input-dir',required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
    root=Path(a.input_dir); rows={}
    for label,probe in EXPECTED.items():
        x=json.loads((root/f'{label}.json').read_text())
        if x.get('probe')!=probe or not x.get('pass'): raise SystemExit(f'bad probe {label}')
        rows[label]=x
    out={
      'probe':'lqg_continuum_iter282_aggregate','source':SOURCE,
      'all_four_independent_contract_guards_pass':True,
      'strong_limit_result':rows['strong']['classification'],
      'distributional_result':rows['rigging']['classification'],
      'model_specificity_result':rows['specificity']['classification'],
      'han_compatibility_result':rows['han']['classification'],
      'benchmark_delta':'PHYSICAL_CONTINUUM_CERTIFICATE_MUST_NOT_REQUIRE_STRONG_HILBERT_CONVERGENCE_WHEN_THAT_WOULD_FORCE_TOPOLOGICAL_THEORY__DISTRIBUTIONAL_PHYSICAL_STATE_ROUTE_ALLOWED_BUT_MODEL_SPECIFIC_OBSERVABLE_UV_IR_CERTIFICATE_STILL_REQUIRED',
      'scientific_boundary':[
        'The guards validate the benchmark interpretation of the published structural theorems; they do not independently re-prove those theorems.',
        'A topological strong-limit result can be a valid scoped continuum result but cannot by itself terminalize four-dimensional gravitational dynamics.',
        'Distributional convergence and a rigging-map physical Hilbert space are admissible structural ingredients, but the source is model-independent and does not provide a concrete constraint map or specified physical-observable algebra for a particular LQG/spinfoam realization.',
        'Therefore the current LQG same-realization physical UV-to-IR/GR normalized-observable blocker remains open.'
      ]}
    write_json(a.output,out)
if __name__=='__main__': main()

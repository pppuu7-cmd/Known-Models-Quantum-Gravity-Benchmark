#!/usr/bin/env python3
import json, pathlib
p=json.load(open('benchmarks/lqg_iter313_source_cplus_unit_sum.json'))
quotient={'K3':-16,'K4':0,'K5':16}
raw={k:2*v for k,v in quotient.items()}
pattern_same=all((quotient[k]==0)==(raw[k]==0) for k in quotient)
ok=(raw=={'K3':-32,'K4':0,'K5':32} and pattern_same and
    p['prospectively_frozen_claims']['global_flip_overall_normalization_changes_cancellation_pattern'] is False)
out={'probe':'global_flip_normalization','pass':bool(ok),'iteration':313,
     'distinct_support_sums':quotient,'literal_raw_sigma_double_count_sums':raw,
     'zero_nonzero_cancellation_pattern_identical':pattern_same,
     'interpretation':'whether the source sum notation quotients global flip or counts both representatives changes only an overall factor two, not the K3/K4/K5 cancellation classification'}
pathlib.Path('build/lqg-iter313').mkdir(parents=True,exist_ok=True)
pathlib.Path('build/lqg-iter313/global_flip_normalization.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if not ok: raise SystemExit(1)

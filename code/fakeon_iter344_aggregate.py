#!/usr/bin/env python3
from __future__ import annotations
import json, math
from pathlib import Path

GAMMA_M = 0.577215664901532860606512090082402431 + math.log(2.0)

def zeta(x: float) -> float:
    return 1.0/(1.0+x/2.0)

def global_upper_bracket(x: float) -> float:
    # Deliberately conservative KMQGB envelope Fs <= 2.5 across the full
    # source-consistency interval. This is wider than the published Fs bands
    # where the source states explicit uncertainties.
    return 202.0*zeta(x)+65.0*x*zeta(x)-144.0*GAMMA_M-8.0*math.pi**2+7.5*x

rows=[json.loads(p.read_text()) for p in sorted(Path('iter344-results').rglob('point-*.json'))]
expected_xi=[0.0,0.25,0.5,0.75,1.5,3.0,8.0,16.0]
expected_alpha=[0.0077,0.0087,0.0097]
assert len(rows)==len(expected_xi)*len(expected_alpha), len(rows)
seen={(round(float(r['xi']),12),round(float(r['alpha']),12)) for r in rows}
assert seen=={(x,a) for x in expected_xi for a in expected_alpha}

max_ratio=0.0
least_negative_total=-float('inf')
for r in rows:
    for e in r['endpoint_results']:
        assert e['bracket'] < 0.0
        assert e['leading_alpha3'] < 0.0
        assert e['nnll_alpha4_correction'] < 0.0
        assert e['through_alpha4'] < 0.0
        max_ratio=max(max_ratio,float(e['relative_abs_correction_to_alpha3']))
        least_negative_total=max(least_negative_total,float(e['through_alpha4']))

# Domain proof for the conservative Fs<=2.5 envelope.
# B_upper(x)=(202+65x)/(1+x/2)-const+7.5x
# derivative = -36/(1+x/2)^2 + 7.5. The only interior stationary point
# is a minimum because the derivative increases monotonically. Therefore the
# maximum on [0,16] is at an endpoint.
xcrit=2.0*(math.sqrt(36.0/7.5)-1.0)
assert 0.0 < xcrit < 16.0
b0=global_upper_bracket(0.0)
b16=global_upper_bracket(16.0)
bcrit=global_upper_bracket(xcrit)
assert bcrit < b0 and bcrit < b16
max_upper=max(b0,b16)
assert max_upper < 0.0

summary={
  'iteration':344,
  'source':'Anselmi arXiv:2010.04739v2 eqs. (4.27),(5.52),(6.3)',
  'matrix_points':len(rows),
  'xi_grid':expected_xi,
  'alpha_grid':expected_alpha,
  'all_matrix_endpoint_totals_negative_through_alpha4':True,
  'maximum_abs_alpha4_correction_over_alpha3_on_matrix':max_ratio,
  'least_negative_matrix_total':least_negative_total,
  'global_conservative_Fs_upper_envelope':2.5,
  'global_bracket_upper_endpoint_xi0':b0,
  'global_bracket_upper_endpoint_xi16':b16,
  'global_bracket_interior_minimum_xi':xcrit,
  'global_bracket_interior_minimum':bcrit,
  'global_bracket_maximum_upper_bound':max_upper,
  'global_sign_certificate':'B(xi,Fs)<=B_upper(xi)<0 for 0<=xi<=16 and Fs<=2.5; hence alpha4 correction has the same negative sign as the leading alpha3 term for alpha>0',
  'classification':'PASS_SCOPED_FAKEON_NNLL_CONSISTENCY_BREAKING_ROBUST_OVER_XI_0_TO_16_UNDER_FS_LE_2P5_STRESS_ENVELOPE__SOURCE_EQ63',
  'parent_family_status':'NONTERMINAL_0_OF_5_MATERIAL_QUANTIZATION_BRANCHES_TERMINAL',
  'd7_promotion_authorized':False,
  'scope_guard':[
    'EXACT_SOURCE_EQ63_WITH_SOURCE_DEFINED_XI_ZETA_GAMMA_M',
    'PUBLISHED_FS_BANDS_USED_WHERE_EXPLICIT_AND_KMQGB_WIDER_FS_ENVELOPE_USED_AT_LOW_XI',
    'DOMAIN_SIGN_CERTIFICATE_IS_SCOPED_TO_FS_LE_2P5',
    'NOT_A_CAUSAL_RESPONSE_CERTIFICATE',
    'NOT_ALL_HIGHER_DERIVATIVE_BRANCHES',
    'NO_PARENT_FAMILY_TERMINALIZATION',
    'NO_D7_PROMOTION'
  ]
}
Path('iter344-summary.json').write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n')
print(json.dumps(summary,sort_keys=True))

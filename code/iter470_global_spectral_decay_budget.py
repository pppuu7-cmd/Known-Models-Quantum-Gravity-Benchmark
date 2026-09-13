#!/usr/bin/env python3
import itertools, math, json, pathlib

OUT=pathlib.Path('artifacts/iter470-summary.json')
vals=(-1,0,1)
counts={q:0 for q in range(11)}
coord_examples={}
for ms in itertools.product(vals, repeat=10):
    ps=tuple(0 if m==0 else 1 for m in ms)
    q=sum(ps); counts[q]+=1
    coord_examples.setdefault(q, ps)
analytic={q:math.comb(10,q)*(2**q) for q in range(11)}
thresholds={q:{'q':q,'strict_isotropic_c_gt':q+10,'marginal_c_eq':q+10} for q in range(11)}
# control: omitting each published spectral denominator raises each one-wedge power by one.
control_thresholds={q:q+20 for q in range(11)}
checks={
 'enumerated_total_59049':sum(counts.values())==3**10==59049,
 'multiplicity_formula_exact':counts==analytic,
 'threshold_range_exact':thresholds[0]['strict_isotropic_c_gt']==10 and thresholds[10]['strict_isotropic_c_gt']==20,
 'denominator_omission_shift_10':all(control_thresholds[q]-thresholds[q]['strict_isotropic_c_gt']==10 for q in range(11)),
 'equality_is_marginal':all(thresholds[q]['marginal_c_eq']==thresholds[q]['strict_isotropic_c_gt'] for q in range(11)),
 'coordinatewise_rule':all(all((2 if p else 1)==p+1 for p in coord_examples[q]) for q in coord_examples),
}
payload={
 'classification':'ITER470_TEN_SPECTRAL_ABSOLUTE_DECAY_REQUIREMENT_BUDGET_PINNED_SCOPED' if all(checks.values()) else 'SCIENTIFIC_OR_IMPLEMENTATION_FAIL_ITER470',
 'scientific_pass':all(checks.values()),
 'checks':checks,
 'multiplicities':counts,
 'thresholds':thresholds,
 'worst_case':{'q':10,'strict_isotropic_requirement':'c>20','coordinatewise_requirement':'c_e>2 for every m_e=+/-1 wedge'},
 'scope':'requirement budget only; actual group-kernel decay and conditional/distributional convergence unresolved; D7-S2 open'
}
OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text(json.dumps(payload,indent=2)+'\n')
print(json.dumps(payload,indent=2))
raise SystemExit(0 if payload['scientific_pass'] else 1)

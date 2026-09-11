#!/usr/bin/env python3
import json
from pathlib import Path
rows=[json.loads(p.read_text()) for p in sorted(Path('iter338-341-results').rglob('*.json'))]
by={r['mode']:r for r in rows}
req={'tier1_terminalization_opportunity_scan','nonlocal_cross_order_functional_rigidity','higher_derivative_material_branch_closure_gap','authority_coherence_supersession_audit'}
assert set(by)==req,(set(by),req)
scan=by['tier1_terminalization_opportunity_scan']
nonlocal_r=by['nonlocal_cross_order_functional_rigidity']
hd=by['higher_derivative_material_branch_closure_gap']
coh=by['authority_coherence_supersession_audit']
assert scan['tier1_total']==15 and scan['counts']['terminal']==1
assert nonlocal_r['all_nonzero_nplus1_forward_differences'] is True
assert hd['terminal_branch_count']==0 and hd['material_branch_count']==5
assert coh['current_coverage_contract_tier1']==15 and coh['current_d7_readiness_tier1']==15
summary={
 'iteration_bundle':'338-341',
 'parallel_lanes':4,
 'tier1_total':15,
 'tier1_terminal':1,
 'new_scoped_scientific_result':nonlocal_r['classification'],
 'nonlocal_parent_status':'PARTIAL_SUBFAMILY_ONLY',
 'higher_derivative_material_branches_terminal':'0/5',
 'current_denominator_authority':'15-row coverage contract + D7 readiness; historical 14-row decision ledger is stale for denominator counts',
 'd7_terminal_decision_authorized':False,
 'next_high_information_fronts':[
   'NONLOCAL_QG physical Riemann/Weyl full-momentum normalized amplitude and local-EFT quotient',
   'PERTURBATIVE_HIGHER_DERIVATIVE fakeon beyond-leading or causal-response comparator plus material-branch disposition',
   'RELATIONAL_QUANTUM_CAUSAL_PROCESSES all-band autonomy and Hilbert-cutoff resource closure'
 ],
 'scope_guard':'New nonlocal functional-rigidity witness is scoped mathematics and does not by itself terminalize NONLOCAL_QG or authorize D7.'
}
Path('iter338-341-summary.json').write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n')
print(json.dumps(summary,sort_keys=True))

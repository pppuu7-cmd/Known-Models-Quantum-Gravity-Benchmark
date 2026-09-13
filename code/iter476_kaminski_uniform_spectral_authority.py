#!/usr/bin/env python3
import json,pathlib

# Frozen source-authority matrix from the preregistered primary-source reading.
# True fields require an explicit source-backed statement/reduction, not inference.
evidence={
  'fixed_label_integrability_theorem_present': True,
  'ten_spectral_labels_simultaneously_variable_in_iter468': True,
  'explicit_uniform_in_all_spectral_labels_bound_present': False,
  'explicit_decay_exponent_or_equivalent_strong_enough_for_iter470': False,
  'causal_toller_kernel_identical_to_the_theorem_integrand_without_extra_work': False,
}
controls={
  'fixed_label_does_not_imply_uniform': evidence['fixed_label_integrability_theorem_present'] and not evidence['explicit_uniform_in_all_spectral_labels_bound_present'],
  'graph_finiteness_does_not_identify_causal_toller_kernel': not evidence['causal_toller_kernel_identical_to_the_theorem_integrand_without_extra_work'],
  'absence_of_uniform_bound_is_not_divergence': True,
}
sufficient=all(evidence.values())
classification='KAMINSKI_UNIFORM_SPECTRAL_AUTHORITY_SUFFICIENT_SCOPED' if sufficient else 'BLOCKED_KAMINSKI_FIXED_LABEL_FINITE_NOT_YET_UNIFORM_SPECTRAL_BOUND_SCOPED'
out={
  'iteration':476,
  'classification':classification,
  'audit_completed':all(controls.values()),
  'scientific_pass':all(controls.values()),
  'source':{'author':'Wojciech Kaminski','title':'All 3-edge-connected relativistic BC and EPRL spin-networks are integrable','arxiv':'1010.5384'},
  'evidence':evidence,
  'negative_controls':controls,
  'iter470_requirement':{'worst_q':10,'simple_isotropic_absolute_comparison_requires':'c > 20','equality':'MARGINAL_UNRESOLVED'},
  'interpretation':'The checked theorem supports fixed-labeled-network finiteness but does not by itself supply the explicit uniform simultaneous ten-spectral-label decay/reduction required by Iter470. BLOCKED is authority insufficiency, not divergence or impossibility.',
  'd7_s2':'NOT_CLOSED',
}
pathlib.Path('artifacts').mkdir(exist_ok=True)
pathlib.Path('artifacts/iter476-summary.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
raise SystemExit(0 if out['audit_completed'] else 2)

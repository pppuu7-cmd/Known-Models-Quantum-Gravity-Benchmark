# Multi-Configuration / Intervention Rigidity for Future Candidate Gravity

**Status:** frozen methodology / pre-ansatz design rule.  
**Purpose:** use controllable source/detector/configuration changes to break comparator degeneracies while keeping one shared parent dynamics.

## 1. Configuration stack

Let controlled configurations be indexed by `a=1,...,A` with known design variables `u_a` such as source geometry, mass assignment, separation, orientation, modulation frequency, proper-time duration, probe state, detector polarization/orientation, or other pre-registered controls.

After exact physical reduction in each configuration, stack

`y_stack = col(y(u_1),...,y(u_A))`.

Use the full cross-configuration covariance `Sigma_stack`.

## 2. Parameter classes must be separated

Freeze the generative parameter incidence before fitting:

1. `theta_dyn`: dynamics parameters shared by all configurations;
2. `theta_shared_nuis`: common calibration/source/detector nuisance shared across configurations;
3. `theta_local,a`: genuinely configuration-local nuisances;
4. `u_a`: controlled design variables, **not fit parameters** when known;
5. uncertain controls: represented by explicit calibration parameters/covariance rather than silently floated.

The stacked Jacobian has the schematic structure

`J_stack=[J_dyn, J_shared_nuis, block/local nuisance columns]`.

Never clone `theta_dyn` independently for each configuration unless the parent theory itself changes between configurations.

## 3. Configuration-null contrasts

A contrast across configurations

`X_w = w^T y_stack`

is locally comparator/nuisance null when

`J_stack^T w=0`.

Simple differences are special cases. For example, if a nuisance contributes the same additive offset `b` to two configurations, `y_1-y_2` annihilates `b` exactly.

General contrasts must use the full covariance and union Jacobian from `protocol/OPTIMAL_COMPARATOR_CONTRASTS.md`.

## 4. Intervention design objective

The design variables `u_a` alter the predicted response vectors and tangent geometry.

For a candidate design set `D={u_a}`, compute

`Sigma(D)`, `J_C(D)`, and when available `J_KG(D)` or pre-registered signal `s(D)`.

Choose interventions prospectively to maximize one of:

- comparator-orthogonal dimension `d_perp(D)`;
- robust rank of `B_KG(D)=Pi_perp(D)Sigma(D)^(-1/2)J_KG(D)`;
- smallest robust nonzero singular value of `B_KG(D)`;
- projected signal SNR `||Pi_perp(D)Sigma(D)^(-1/2)s(D)||`.

Raw signal amplitude before comparator profiling is not the design objective.

## 5. Exact dimension-gain rule

Adding a new configuration with `k` physical observables gives

`Delta d_perp = k - Delta rank(J_union)`.

A configuration is structurally valuable when its physical response adds directions that are not accompanied by equally many new comparator/nuisance directions.

Thus repeating the same geometry with only more precision may be less useful than changing a control that rotates the signal/comparator tangent geometry.

## 6. Shared-vs-local nuisance penalty

Configuration diversity is not automatically useful. If every new configuration requires an equal number of completely free local nuisance parameters, the complement dimension may not grow.

Therefore pre-register

`information gain = physical-dimension gain - nuisance/comparator-rank gain`.

Prefer controls whose nuisance calibration is shared or independently measured.

## 7. Attribution-oriented interventions

Controls should be chosen to attack specific attribution loopholes, for example:

- source species/composition changes for universality/stress-energy tests;
- orientation/polarization changes for helicity/tidal structure;
- distance/time/frequency sweeps for causal/retarded support and analytic-origin tests;
- probe-state swaps for detector/state attribution;
- geometry reversal/null configurations for ordinary mediator/systematic rejection;
- multiple response orders under the same controls for cross-order rigidity.

No single scaling law is assumed KG-specific. In particular, mass/distance scaling alone may be reproduced by tuned scalar mediators and must be combined with spin-2/Ward/channel attribution.

## 8. Cross-configuration covariance

Retain shared

- numerical/truncation errors;
- source-calibration errors;
- detector calibration;
- common environmental backgrounds;
- theory/systematic uncertainties.

Use full `Sigma_stack`. Do not treat configurations as independent solely because they were measured/simulated separately.

## 9. Combined cross-order + intervention stack

The strongest future KG design may use a two-index stack

`y_(ell,a)`

for response order/channel `ell` and controlled configuration `a`.

Shared parent parameters run across both indices. Local nuisance incidence is declared explicitly.

Then the same COR/projected-rank machinery determines whether the enlarged design actually creates new comparator-orthogonal dimensions.

## 10. Candidate Gravity design consequence

A future KG model should be evaluated on a **designed family of linked configurations**, not one favorite benchmark point.

The ideal architecture has

- few shared KG parameters;
- many controlled response configurations/orders;
- few new local nuisances;
- exact Ward/contact/relational completion;
- growing post-comparator rank/conditioning under intervention.

This converts experimental/theoretical controls into a deliberate rigidity mechanism.

## 11. Promotion guardrail

Intervention design does not promote an ansatz. All Candidate Gravity Promotion Gate requirements remain mandatory.

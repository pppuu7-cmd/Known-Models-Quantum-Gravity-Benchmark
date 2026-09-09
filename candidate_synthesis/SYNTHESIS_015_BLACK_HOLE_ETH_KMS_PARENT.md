# SYNTHESIS-015 — Black-Hole Entropy + ETH + KMS Parent

**Status:** REJECTED as standalone P4 parent / retained thermal-consistency control.  
**KMQGB iteration:** 123.  
**Purpose:** test whether KMS/detailed balance closes the smooth spectral-envelope freedom left by the black-hole entropy + ETH parent.

## 1. Proposed completion

Iter122 established the hierarchy

`S_BH -> coarse density of states`,

`ETH -> statistical matrix-element template`,

while leaving smooth graviton transition envelopes, higher cumulants and phases.

A natural next proposal is to add exact thermal equilibrium consistency:

> the black-hole hard transition hierarchy is selected by Bekenstein-Hawking state counting + ETH + KMS detailed balance / fluctuation-dissipation relations.

## 2. Two-point KMS relation

For a bosonic thermal observable, define Wightman functions in frequency space `G^>(omega)` and `G^<(omega)`. KMS implies, up to convention,

`G^>(omega) = exp(beta omega) G^<(omega)`.

With spectral density

`rho(omega) = G^>(omega) - G^<(omega)`,

one obtains

`G^>(omega) = rho(omega)/(1-exp(-beta omega))`,

`G^<(omega) = exp(-beta omega) rho(omega)/(1-exp(-beta omega))`.

Therefore KMS fixes the **thermal ratio/reconstruction once rho is known**, but does not determine the positive-frequency spectral density `rho(omega)` itself.

Classification:

`A2 BLOCKED__KMS_FIXES_DETAILED_BALANCE_RATIO_NOT_ABSOLUTE_SPECTRAL_ENVELOPE`.

This matches ETH/open-system results in which local detailed balance emerges while the dynamics is controlled by a separate ETH spectral function.

## 3. Fluctuation-dissipation does not add an independent origin law

The fluctuation-dissipation theorem relates statistical/noise correlators to the dissipative or spectral part of the retarded response through a thermal factor.

Schematically,

`G_sym(omega) = thermal_factor(beta omega) * rho(omega)`.

Thus FDT changes representation: one spectral function generates several thermal correlators. It does not derive that spectral function from temperature/entropy alone.

This is another instance of KMQGB's transport-vs-origin distinction.

## 4. Higher-point KMS

At higher connected order, KMS cyclicity relates different real-time orderings and allows a causal/nested-commutator basis for thermal n-point functions.

But those relations do not specify the independent causal spectral functions / nested-commutator data themselves. In ETH language, the higher non-Gaussian cumulants/correlations found at Iter122 remain dynamical input unless the parent fixes them.

Therefore adding higher-point KMS does not close the all-point hard hierarchy.

## 5. Fresh black-hole spectral-function control

2026 holographic work provides a useful positive control: thermal spectral functions can factor into perturbative/OPE and nonperturbative pieces, and exact WKB can derive transseries asymptotics of the nonperturbative part from a concrete bulk black-hole wave equation.

This demonstrates the desired direction of inference:

`microscopic/bulk dynamics -> spectral function -> KMS-related thermal correlators`,

not

`KMS -> unique microscopic spectral function`.

The same work also shows that nonperturbative spectral data can encode black-hole interior/singularity information, reinforcing that the missing envelope is physically substantive rather than a convention.

## 6. A3 comparator pressure

Known realizations of `entropy + ETH + KMS` lie inside

- thermal QFT/statistical mechanics;
- holographic black-hole quantum chaos;
- JT/random-matrix gravity;
- ordinary unitary black-hole/microstate descriptions.

KMS is universal equilibrium consistency and therefore is not a novelty certificate.

## 7. A4 consequence

The proposal still does not uniquely derive

- the positive-frequency asymptotic-graviton spectral envelope;
- exact channel/angular-momentum dependence;
- higher causal spectral functions/cumulants;
- microscopic phases;
- a normalized comparator-orthogonal physical `4g` hard amplitude;
- the same-parent complete CTP hierarchy.

Classification:

`A4 BLOCKED__THERMAL_RELATIONS_RECONSTRUCT_COMPONENTS_BUT_DO_NOT_SELECT_HARD_SPECTRAL_DATA`.

## 8. Next gate

The strongest remaining thermal route is to ask whether **spectral sum rules / moments / OPE asymptotics** can determine the free positive-frequency spectral density.

A finite set of moments must be tested against the positive moment problem before it can be treated as a selector.

## 9. Score consequence

No P4 credit. R4 remains 45%.

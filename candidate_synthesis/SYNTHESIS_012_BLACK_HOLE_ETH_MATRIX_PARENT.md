# SYNTHESIS-012 — Black-Hole ETH / Random-Matrix Transition Parent

**Status:** REJECTED as standalone P4 parent / retained microstate-statistics control.  
**KMQGB iteration:** 112.  
**Purpose:** test whether ETH/random-matrix universality closes the microscopic transition-data freedom left by the black-hole entropy-density parent.

## 1. Proposed completion of SYNTHESIS-011

SYNTHESIS-011 found that `rho(E,J) ~ exp(S_BH)` fixes only a coarse density of strong-gravity states. A natural next step is to assume that black-hole microstate transition matrix elements obey a universal eigenstate-thermalization/random-matrix law.

Schematically, for a probe/operator `O`, ETH takes the form

`O_mn = O_bar(E) delta_mn + exp[-S(E)/2] f_O(E,omega) R_mn`,

where `R_mn` is a pseudo-random matrix with specified statistical structure.

Tempting claim:

> Bekenstein-Hawking entropy + ETH universality fixes the hard gravitational transition amplitudes statistically from finite data.

## 2. A1 — physically motivated strong-gravity statistical law

ETH and random-matrix ideas are well-motivated descriptions of chaotic black-hole microstates and are realized explicitly in JT-gravity/matrix-model constructions. Recent black-hole microstate work continues to use ETH as the boundary description of fine-grained state dependence.

Thus

`A1 PASS_AS_STATISTICAL_MICROSTATE_PRINCIPLE`.

## 3. A2 — ETH leaves smooth functions and higher moments

The ETH ansatz does not determine the smooth envelope `f_O(E,omega)` from entropy alone. Different operators/channels have different smooth functions.

Moreover, Gaussian/random independent matrix elements are insufficient for generic higher-point observables. ETH matrix-model work requires non-Gaussian corrections / higher statistical moments to reproduce nontrivial OTOCs and higher correlators.

For gravitational scattering this means that even after fixing `S_BH`, one still needs parent-derived data for

- the smooth two-graviton-to-microstate envelope;
- channel/angular-momentum dependence;
- correlations among matrix elements;
- non-Gaussian higher cumulants controlling `4g`, `5g`, ... observables;
- phases needed for a unitary microscopic S-matrix.

Therefore

`A2 BLOCKED__ETH_STATISTICAL_FORM_LEAVES_SMOOTH_ENVELOPES_AND_HIGHER_CUMULANTS`.

Choosing these functions/cumulants to reproduce a desired hard amplitude would be circular.

## 4. A3 — comparator containment

Known ETH/random-matrix realizations are already strong comparator architectures, especially

- JT gravity + matter;
- double-scaled/random matrix gravity;
- holographic black-hole quantum chaos;
- matrix/microstate models.

Thus statistical universality by itself is not architecture-new.

## 5. A4 — no deterministic normalized hard hierarchy

A statistical ensemble can predict averaged correlators or distributions, but KMQGB requires a parent-fixed physical hard relation with normalized observable semantics.

Without the smooth envelopes and higher cumulants, the parent does not uniquely give

- the physical `4g` hard amplitude or its probability distribution at the required precision;
- its all-point linked hierarchy;
- the same-parent CTP/retarded kernels;
- a comparator-orthogonal residual.

Classification:

`A4 BLOCKED__NO_UNIQUE_HARD_TRANSITION_HIERARCHY_FROM_ENTROPY_PLUS_ETH_ALONE`.

## 6. Positive lesson

The black-hole route now has an explicit hierarchy of missing data:

`S_BH -> density of states`

`ETH -> scaling/statistical template`

`parent-specific f_O + higher cumulants + phases -> actual hard transition hierarchy`.

A future strong-gravity parent would need to derive the third line from finite gravitational data rather than assume it.

## 7. Reopen condition

Reopen only for a microscopic gravity-native law that fixes

1. the ETH envelope(s) for asymptotic graviton operators;
2. the complete higher-cumulant hierarchy or a finite recursion generating it;
3. exact unitarity/phase correlations;
4. normalized `4g`/higher and CTP observables;
5. comparator escape from JT/random-matrix/matrix-theory/string/standard black-hole resonance descriptions.

## 8. Score consequence

No P4 credit. R4 remains 45%.

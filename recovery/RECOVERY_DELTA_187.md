# KMQGB Recovery Delta 187

**Date:** 2026-09-10  
**RQIR Core:** v1.0 FROZEN

## Main scientific result

The perturbative/higher-derivative family has been advanced from a vague ghost/pole blocker to an explicit material quantization-branch map.

The four-derivative spin-2 propagator contains an additional massive opposite-bare-residue pole, but this structural fact does not by itself determine a family-level unitarity verdict. Iter187 freezes materially distinct physical prescriptions:

- conventional/bare or indefinite-metric ghost interpretation;
- fakeon / purely-virtual average-continuation prescription;
- Lee-Wick / unstable-resonance treatment;
- PT-symmetric / modified-inner-product treatments;
- Euclidean reflection-positive lattice construction.

The branches are not silently merged. In particular, published Lee-Wick/complex-ghost analyses contain conflicting unitarity conclusions, so citation counting cannot produce a terminal family verdict.

Authorities:

- `paper_iv/O_HIGHER_DERIVATIVE_QUANTIZATION_BRANCH_AUDIT_2026-09-10.md`
- `paper_iv/HIGHER_DERIVATIVE_QUANTIZATION_BRANCH_MAP_2026-09-10.json`

## Fakeon scoped control

One fixed fakeon realization is now stored as a complete scoped child result:

`PASS_RQIR_GATE__SCOPED_FAKEON_RENORMALIZABILITY_UNITARITY_INFLATION_OBSERVABLE_CONTROL`

It records:

- renormalizable local `R + R^2 + C^2` parent;
- fakeon/purely-virtual spin-2 prescription;
- perturbative-unitarity control under that prescription;
- explicit inflationary scalar/tensor observables;
- explicit declaration that ordinary microcausality is modified rather than silently assumed.

Authority:

`post_freeze_paper_iv_wave_02/PF2_05_HIGHER_DERIVATIVE_FAKEON/result.json`

This is not a unique-QG residual and not a family-level PASS.

## Refined higher-derivative blocker

Old:

`HIGHER_DERIVATIVE_POLE_PRESCRIPTION_FAMILY_MAP_PLUS_SAME_REALIZATION_CAUSALITY_OBSERVABLE_COMPARATOR_CERTIFICATE`

Refined after branch mapping:

`HIGHER_DERIVATIVE_MATERIAL_QUANTIZATION_BRANCH_TERMINAL_DISPOSITION_PLUS_SAME_REALIZATION_CAUSALITY_OBSERVABLE_COMPARATOR_CERTIFICATE`

The next narrow gate is:

`HIGHER_DERIVATIVE_FAKEON_INFLATION_FULL_COMPARATOR_QUOTIENT_PLUS_CAUSAL_REPLACEMENT_CERTIFICATE`

This must compare the same fakeon inflation realization against Starobinsky `R+R^2`, complete same-order local higher-curvature EFT, and state/nuisance comparators, while preserving the fakeon causal-replacement domain.

## D7 rerun

D7 was recomputed after integrating the new scoped child. As required by the frozen semantics:

- Tier-1 total: 14;
- terminal family rows: 1/14;
- nonterminal family rows: 13/14;
- Tier-2 unresolved: 0;
- defined scoped child rows: 7;
- D2: NOT_CLOSED;
- D4: NOT_CLOSED;
- D7: NOT_CLOSED;
- global decision: `NOT_YET_AUTHORIZED`;
- Candidate Gravity activation: false.

No family-exclusion evidence is inferred from the scoped fakeon result.

## Stable readiness

- R1 = 100%.
- R2 = 100%.
- Candidate Gravity R3 = 24%, inactive.
- Closure Wave 02 = 0/3 terminal.

No readiness promotion in Iter187.

## Compute policy

Heavy compute remains IDLE. The next fakeon gate first requires a prospectively frozen comparator/domain/covariance/parameter-incidence package; blind numerical fitting before that would not be classification-changing evidence.

## Next operation

1. freeze fakeon inflation common-domain observable/comparator capsule;
2. determine whether the published scalar/tensor relation survives Starobinsky + full local-EFT/state/nuisance quotient;
3. if a residual survives, define an independent holdout; if absorbed, preserve comparator identity/degeneracy as a negative result;
4. then return to the remaining 12 other family blockers and rerun D7.

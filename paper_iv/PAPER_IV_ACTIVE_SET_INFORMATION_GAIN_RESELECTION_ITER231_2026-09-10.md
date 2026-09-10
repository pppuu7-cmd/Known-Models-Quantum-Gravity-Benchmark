# Paper IV active-set information-gain reselection — Iter231

**Date:** 2026-09-10  
**RQIR Core:** v1.0 FROZEN  
**Previous gate:** `PAPER_IV_ACTIVE_SET_INFORMATION_GAIN_RESELECTION_AFTER_ITER230`

## Purpose

Re-select the next nonterminal Tier-1 family after the higher-derivative branch map was exhausted to the current authority boundary in Iter227–230. Selection is by expected information gain, not by preference for a desired `NEW_REQUIRED` outcome.

## Stable global state

- D2 = `NOT_CLOSED_COVERAGE_AND_OBJECTS`.
- D4 = `PARTIAL_ACTIVE_SET_MATRIX__GLOBAL_COVERAGE_NOT_CLOSED`.
- D7 = `NOT_CLOSED`.
- Global decision = `NOT_YET_AUTHORIZED`.
- Candidate Gravity activation = false.
- Paper III remains frozen; Iter209 saturation criterion remains satisfied through Iter230.

## Reselection logic

The highest-information next family is `NONLOCAL_QG`.

Reason: unlike many families that are currently blocked before a normalized observable exists, nonlocal gravity already contains several comparator-resolved scoped children with mixed outcomes:

- Ricci/EOM-squared weakly nonlocal tree S-matrix: exact GR comparator identity;
- analytic Riemann/Weyl fixed-order EFT quotient: comparator-orthogonal residual vanishes at each complete fixed local EFT order;
- Weyl `H_K` eikonal branch: scoped causality FAIL;
- Weyl `H_T` eikonal branch: scoped causality PASS;
- Gödel/CTC-admitting form-factor classes: scoped global-causality FAIL.

Therefore the decisive open question is no longer whether nonlocal models can generate observables. It is whether a fixed, finite-parameter nonlocal realization predicts a **cross-order/full-momentum functional shape** that survives the complete local-EFT comparator quotient and can be tested on holdout kinematic/radial data.

## Competing fronts

- `ASYMPTOTIC_SAFETY`: very narrow and promising, but currently waits for stable inspectable same-realization `A4` equations/data. Re-searching before new authority appears has low expected gain.
- `LQG_SPINFOAM`: remains blocked on a long micro-to-area-metric/RG ancestry chain; high importance but larger missing-object distance.
- `STRING_MTHEORY_HOLOGRAPHY`: broad family-level material-subfamily coverage problem remains; high census burden but less immediate chance of a comparator-resolved residual.
- `CDT_EDT`: strong numerical front, but the decisive next move requires a multi-coupling line-of-constant-physics data capsule rather than another one-point analysis.
- `CAUSAL_SETS`: full 4D continuum-selection evidence remains the limiting object.

## Selected gate

`NONLOCAL_EXPONENTIAL_FORM_FACTOR_FULL_SHAPE_TO_LOCAL_EFT_HOLDOUT_COMPARATOR_AUDIT`

Primary target: exponential form-factor weak-field gravity with a finite parameterization, especially the 2026 Newtonian-limit result for

`f_s(Box) = exp[(-Box/mu_s^2)^{N_s}]`.

Test whether its radial/momentum dependence supplies a frozen full-shape prediction that cannot be exactly reproduced by any **finite-order** local EFT comparator over an extended domain, while preserving parameter ancestry and uncertainty controls.

## Guardrail

A scoped full-shape PASS must not be promoted to the entire `NONLOCAL_QG` family unless material form-factor classes are dispositioned. Conversely, a causality FAIL in one form-factor class must not be generalized to all nonlocal gravity.

## Paper III impact

No new transferable resource-closure failure mode is introduced by reselection itself.

`PAPER_III_REOPEN = NO`.

## Progress

- Iter231 reselection task: **100%**.
- Overall KMQGB infrastructure: **100%**.
- Candidate Gravity R3: **24% inactive**.
- Paper IV D2/D4/D7: **nonterminal**.

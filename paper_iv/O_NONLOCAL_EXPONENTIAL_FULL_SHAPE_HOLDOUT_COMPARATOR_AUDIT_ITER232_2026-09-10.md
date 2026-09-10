# Nonlocal exponential form-factor full-shape / holdout comparator audit — Iter232

**Date:** 2026-09-10  
**RQIR Core:** v1.0 FROZEN  
**Family:** `NONLOCAL_QG`  
**Branch:** exponential-form-factor weak-field gravity  
**Gate:** `NONLOCAL_EXPONENTIAL_FORM_FACTOR_FULL_SHAPE_TO_LOCAL_EFT_HOLDOUT_COMPARATOR_AUDIT`

## Question

Does a fixed exponential-form-factor realization now provide a finite-parameter, full radial/momentum-shape prediction that escapes the exact absorption found for complete fixed-order local EFT comparators and therefore supplies a genuine nonlocal holdout direction?

## Primary 2026 authority

Sangy, Burzillà, Giacchini and de Paula Netto, *Effective delta sources and Newtonian limit in nonlocal gravity*, Phys. Rev. D 113, 104006 (2026), studies

`f_s(Box) = exp[(-Box/mu_s^2)^{N_s}]`

with positive real `N_s` and scale `mu_s`.

The paper derives effective delta sources, mass functions and Newtonian potentials in series/integral/special-function representations and gives controlled approximations for their dependence on `N_s` and `mu_s`. It also identifies a qualitative discriminator: oscillations in the Newtonian potential occur only for `N_s > 1`, while the effective masses remain positive, and it computes the leading logarithmic quantum correction.

## A. Finite-parameter full-shape structure — PASS scoped

For a declared branch with fixed spin-sector assignment and a finite set of parameters `{N_s, mu_s}`, the model defines a non-polynomial entire form factor. Its weak-field potential is not merely one coefficient at one EFT order; it is a correlated radial function whose values at multiple radii are linked by the same parameters.

Therefore a prospective protocol can fit `{N_s, mu_s}` on a calibration radial window and test the predicted shape on disjoint holdout radii.

Classification:

`PASS_SCOPED_FINITE_PARAMETER_NONLOCAL_FULL_RADIAL_SHAPE_AND_HOLDOUT_STRUCTURE`.

## B. Relation to the fixed-order EFT quotient

The earlier KMQGB result remains correct: at any **complete finite local derivative order**, analytic nonlocal Riemann/Weyl effects can be represented by the corresponding finite tower of local operators and are absorbed by a sufficiently complete same-order local EFT comparator.

However, the entire exponential function carries an infinite correlated coefficient tower. A finite-order local EFT can approximate the nonlocal potential over a restricted low-momentum domain but cannot be exactly identical to the entire full-shape function on an extended domain unless the comparator itself is allowed an infinite functional freedom equivalent to the nonlocal form factor.

Thus the correct RQIR distinction is:

- coefficient-by-coefficient at fixed finite order: comparator residual can vanish;
- full non-polynomial shape over an extended domain: a finite-order local EFT comparator leaves truncation-dependent shape residuals;
- an unrestricted infinite-order local functional comparator would erase the distinction but would also cease to be a finite predictive EFT benchmark unless its coefficient correlations are independently fixed.

This establishes a genuine **scoped functional-rigidity direction**, but not yet a family-level residual.

## C. Why this is not yet a terminal residual

The 2026 Newtonian-limit paper supplies theory-side full-shape functions, not a complete RQIR observational capsule. The audited authority does not simultaneously freeze:

1. a unique family-wide form-factor choice rather than the declared exponential subfamily;
2. experimental/astrophysical data with a common-domain nuisance model;
3. a prospectively fixed calibration-versus-holdout radial partition;
4. a complete local-EFT comparator with an explicit truncation order and coefficient priors/ancestry;
5. propagated uncertainty from source structure, quantum/log corrections, weak-field approximation and form-factor parameters;
6. a causality/unitarity disposition for the exact same form-factor realization used in the potential test.

Therefore the result is a methodological and theory-prediction PASS, not an observational or family-terminal PASS.

## D. Cross-check against 2026 causality authority

Zhao, Modesto and Bambi, *Acausal exact vacuum solutions in nonlocal gravity* (2026), shows that a specific but large class of renormalizable nonlocal form factors admits Gödel-type vacuum solutions with closed timelike curves. This confirms that renormalizability by itself does not select a causally acceptable form factor.

That result cannot be automatically attached to the Sangy et al. exponential Newtonian branch without a same-realization form-factor match. It instead strengthens the family-level requirement that any full-shape branch also declare its causality class.

## E. State-dependent nonlocal scale is a separate branch

The 2026 curvature-history formulation introduces a state-dependent nonlocal scale using an auxiliary covariant history field and derives a conserved coupled system. This is a materially distinct dynamical realization; it must not be merged with fixed-scale exponential form-factor predictions unless an explicit reduction/equivalence map is supplied.

## Scoped result

`PASS_RQIR_GATE__NONLOCAL_EXPONENTIAL_FINITE_PARAMETER_FULL_SHAPE_HAS_COMPARATOR_ORTHOGONAL_HOLDOUT_POTENTIAL_IN_PRINCIPLE__OBSERVATIONAL_ERROR_AND_SAME_REALIZATION_CAUSALITY_CAPSULE_OPEN`

This is stronger than the prior statement that all analytic nonlocal effects are invisible after EFT subtraction. The correct statement is that **every complete finite-order Taylor sector is absorbable**, while the globally correlated infinite-order shape can remain predictive against a finite-order EFT comparator.

## Family consequence

`NONLOCAL_QG` remains `PARTIAL_SUBFAMILY_ONLY` because other form-factor classes differ in causality, spectrum, asymptotics and functional freedom. No family-level exclusion or sufficiency is authorized.

Refined missing certificate:

`NONLOCAL_FIXED_FORM_FACTOR_FULL_SHAPE_CALIBRATION_HOLDOUT_DATA_PLUS_FINITE_EFT_TRUNCATION_COMPARATOR_PLUS_SAME_REALIZATION_UNITARITY_CAUSALITY_ERROR_CERTIFICATE__MATERIAL_FORM_FACTOR_FAMILY_DISPOSITION`

## Paper III impact

This result does **not** expose a new Paper-III resource-closure failure mode. It reinforces already-frozen requirements for calibration/holdout separation, comparator completeness, finite resource/truncation accounting and same-realization provenance.

`PAPER_III_REOPEN = NO`.

## Heavy compute

`CONDITIONALLY_AUTHORIZED_FOR_SYNTHETIC_IDENTIFIABILITY_STRESS_TEST`.

A lightweight numerical test is now scientifically meaningful: generate the exact exponential-form-factor Newtonian shape, fit finite local-EFT polynomial/derivative surrogates on a calibration window, and measure holdout residual versus EFT order and radial domain. This would test RQIR functional rigidity but would not by itself establish empirical viability.

## Next gate

`NONLOCAL_FULL_SHAPE_SYNTHETIC_EFT_QUOTIENT_RIGIDITY_STRESS_TEST`

The test should determine whether the finite-parameter full-shape direction remains numerically identifiable after allowing finite-order local-EFT nuisance coefficients, source normalization and scale uncertainty, and how the holdout residual collapses as EFT order grows.

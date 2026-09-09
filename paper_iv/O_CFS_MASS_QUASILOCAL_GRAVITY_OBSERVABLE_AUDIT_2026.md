# O-CFS Mass / Quasilocal Gravity Observable Audit — 2026-09-10

**KMQGB iteration:** 163  
**RQIR standard:** Core v1.0 FROZEN  
**Closure-wave target:** CW2-03 / O-CFS.

## New accepted authority

CFS already contains native **gravity-specific observables**, not merely a generic surface-layer formalism.

### Total mass

Finster–Platzer, *A Positive Mass Theorem for Static Causal Fermion Systems* defines asymptotically flat static CFS and a total mass as a limit of surface-layer integrals comparing the spacetime measure with a vacuum measure near spatial infinity.

Important properties:

- the definition does not require ordinary spacetime regularity and applies in principle to singular/generalized `quantum` spacetimes;
- a positive-mass theorem is proved under the stated assumptions;
- in Dirac-sea CFS constructed in Schwarzschild geometry, the definition reduces to the ADM mass.

### Quasilocal mass and synthetic curvature

Finster–Kamran, *A positive quasilocal mass for causal variational principles* (2025), derives positivity inequalities for nonlinear surface-layer integrals, defines a positive quasilocal mass and synthetic scalar curvature, and works out ultrastatic/Schwarzschild examples. The continuum examples connect to ordinary scalar curvature and show close structural similarity to Brown–York mass.

## Frozen-RQIR interpretation

The blocker

`NO_GRAVITY_SPECIFIC_NATIVE_CFS_OBSERVABLE`

is obsolete.

CFS now has at least a concrete mass/quasilocal-curvature observable family that is defined at the causal-variational level and is not conceptually restricted to smooth continuum manifolds.

However, the presently controlled evaluations are **comparator successes**:

- Schwarzschild total mass -> ADM mass;
- quasilocal/synthetic-curvature examples -> familiar GR geometric quantities in their controlled limits.

These results validate the observable architecture but do not yet yield a comparator-orthogonal CFS residual.

## Current CW2-03 status

Scoped positive result:

`PASS_RQIR_GATE__NATIVE_GRAVITY_MASS_OBSERVABLE_CONTROL`.

CW2-03 remains open because its decisive beyond-continuum component is still missing.

Exact blocker becomes

`BEYOND_CONTINUUM_CFS_MASS_QUASILOCAL_OR_CURVATURE_EVALUATION_PLUS_COMPARATOR_RESIDUAL`.

## Shortest closure route

Use the already-defined native observable instead of inventing a new one.

Freeze one family of non-continuum / regularization-dependent CFS configurations and compute

`R_M = M_CFS - M_GR/QFT_comparator`

or the corresponding quasilocal/synthetic-curvature vector, with:

1. fixed universal measure / regularization prescription;
2. fixed asymptotic alignment and state;
3. controlled continuum limit recovering ADM/Brown–York/ordinary curvature;
4. the first non-continuum correction derived prospectively;
5. regulator scaling / removal test;
6. same-domain EFT/QFT comparator for any ordinary matter/loop correction;
7. parameter sharing across at least two masses/radii/configurations or another holdout block.

A raw deviation at one regulator value is not sufficient.

## Paper-IV consequence

CFS is closer to a complete frozen-RQIR test than Iter156 suggested: the observable definition exists. The missing object is now an **evaluation and comparator-quotient problem**, not an ontology/observable-definition problem.

This is still zero evidence for `NEW_REQUIRED`; until the non-continuum evaluation is supplied, CFS is not excluded.

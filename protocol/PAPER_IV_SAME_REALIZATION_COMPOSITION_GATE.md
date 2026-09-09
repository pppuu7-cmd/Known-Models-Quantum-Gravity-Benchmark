# Paper IV Same-Realization Composition Gate

**KMQGB iteration:** 161  
**Layer:** KMQGB benchmark/adaptor methodology only.  
**RQIR Core:** v1.0 FROZEN and unchanged.

## Motivation

Post-freeze benchmarking exposed the same failure mode independently in asymptotic safety (Iter154/158) and LQG/spinfoam entropy (Iter160): several individually strong results from one research school may live in different truncations, states, regulators, observables or normalizations.

Combining them by school name alone can manufacture a physical object that no paper/model realization actually predicts.

We call this a **Frankenstein composition**.

## Realization identity vector

For every ingredient `X_i` used in a terminal RQIR observable, record the realization vector

`R_i = {parent/effective action, field content, state, boundary data, regulator, RG trajectory, renormalisation conditions, gauge/constraint prescription, normalization, Lorentzian/analytic prescription, observable definition, approximation/truncation}`.

Two authorities are directly composable only if

`R_i == R_j`

for every scientifically material component, or if an explicit map

`M_ij : R_i -> R_j`

is derived and its induced uncertainty/parameter transformation is propagated to the final observable.

## Gate

A proposed composed observable

`O = F(X_1, X_2, ..., X_n)`

receives `SAME_REALIZATION_PASS` only if all of the following hold:

1. each `X_i` has a declared realization vector;
2. every mismatch has an explicit physical/mathematical map rather than an analogy;
3. parameter names shared across papers are proven to denote the same renormalized quantity;
4. state/boundary/contour prescriptions are compatible;
5. gauge/constraint/regulator changes are mapped or included in uncertainty;
6. crossing/species/helicity/domain differences are mapped;
7. normalization conventions are converted explicitly;
8. approximation/truncation errors are propagated through the composition;
9. the same-domain comparator is evaluated after the composition, not ingredient-by-ingredient only.

If any material map is absent:

`BLOCKED_CROSS_AUTHORITY_COMPOSITION_NOT_YET_SAME_REALIZATION`.

## Anti-gaming consequences

The following are insufficient:

- shared framework name;
- shared authorship;
- adjacent papers in one programme;
- same fixed-point label;
- same Barbero-Immirzi parameter symbol;
- same words `Lorentzian`, `continuum`, `contact`, `entropy`, `unitary`, or `UV fixed point`;
- agreement in one limiting coefficient.

No composed PASS may be used for Paper-IV global evidence until this gate closes.

## Examples

### AS

Mediated Lorentzian scattering, analytic contact-form-factor controls, a diffeomorphism-invariant error-controlled RG flow and a conference contact contribution are all strong ingredients. They are not one `A_s+A_t+A_u+A4` certificate until trajectory, field/species, vertex, normalization and error maps are explicit.

### LQG/spinfoam

The Lorentzian spinfoam-stack leading entropy and the algebraic fixed-area logarithmic correction are closely related. The subleading coefficient cannot be imported into the stack result until the state/algebra/stack-coupling/gamma/regulator map is explicit.

## Relation to frozen RQIR

This gate does **not** add a new RQIR observable or alter any Core-v1.0 decision rule. It ensures that the object handed to the frozen RQIR judge is actually predicted by one well-defined realization.

Therefore a failure of this composition gate is a KMQGB provenance/model-completion block, not an RQIR Core defect.

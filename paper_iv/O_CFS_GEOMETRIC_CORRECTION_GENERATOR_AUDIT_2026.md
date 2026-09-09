# O-CFS Geometric Correction-Generator Audit — 2026-09-10

**KMQGB iteration:** 170  
**RQIR standard:** Core v1.0 FROZEN  
**Closure-wave target:** CW2-03 / O-CFS.

## New 2026 authority

Finster–Krpoun, arXiv:2607.13871, *A Geometric Derivation of the Einstein Equations from the Causal Action Principle*, gives a direct geometric derivation of Lorentzian Einstein equations from the causal action for smooth four-dimensional CFS spacetimes.

Key structural results:

- the causal Lagrangian induces geometric data through osculating vacua;
- the Lorentzian metric is obtained using the CFS-specific regularizing vector field;
- the EL equations imply Einstein equations with a symmetric divergence-free effective energy-momentum tensor;
- the gravitational coupling scale is set by the square of the regularization length;
- the construction uses a systematic expansion in the microscopic length and supplies a procedure for computing corrections.

The Lorentzian Einstein tensor is expressed through explicit geometric/alignment terms and infinite expansion sums; this is substantially stronger than a purely qualitative `Einstein + corrections` statement.

## What Section 7 actually closes

The paper classifies four correction sources:

1. higher-order / Planck-scale terms in the microscopic length;
2. osculation corrections, including possible torsion when the osculation is non-optimal;
3. corrections from the regularizing timelike vector field;
4. corrections associated with modified measures.

Thus CFS already has a **parent-derived correction architecture**.

Scoped classification:

`PASS_RQIR_GATE__SYSTEMATIC_GRAVITY_CORRECTION_GENERATOR_CONTROL`.

## What remains open

The same Section 7 states that these corrections still need to be worked out in detail. In particular, the effects of the regularizing vector field on the Einstein equations remain to be analyzed.

Therefore the missing CW2-03 object is no longer a mechanism or formal expansion. It is

`FIRST_EXPLICIT_NORMALIZED_CFS_GRAVITY_CORRECTION_TENSOR_PLUS_COMPARATOR`.

At least one correction block must be evaluated to the point where RQIR can form an observable/residual.

## Comparator requirement

A curvature correction of schematic order

`delta^4 * Riem^2`

or another local analytic curvature structure is **not automatically CFS-unique**. In a low-energy smooth regime it overlaps the full gravitational EFT / higher-curvature comparator span.

A useful CFS discriminator therefore requires one of:

- a parent-fixed relation among several correction coefficients that generic EFT leaves independent;
- a nonlocal/regularization-vector/torsion/modified-measure structure not reducible to the declared EFT comparator;
- a cross-background/shared-parameter relation;
- a native surface-layer/mass observable correction linked to the same microscopic coefficient vector.

## Preferred next calculation

Do not scan arbitrary regularizations. Starting from one prospectively fixed CFS microscopic regularization law, derive the lowest nonzero correction tensor from the osculation/weight-function/alignment expansion and project it onto a basis

`Delta E_{mu nu} = sum_i c_i(delta,R) O^{(i)}_{mu nu}`.

Then perform

1. dimensional/Ward/Bianchi checks;
2. mapping to full C5 local higher-curvature basis where applicable;
3. identify any CFS-specific coefficient relation or non-C5 structure;
4. evaluate the same coefficient vector in at least two backgrounds/observables.

Only after this analytic object is frozen does a heavy numerical evaluation become useful.

## Current classification

`CORRECTION_GENERATOR_EXISTS__FIRST_COMPARATOR_READY_CORRECTION_NOT_WORKED_OUT`.

CW2-03 remains open, but the gap is now a concrete derivation task rather than an undefined beyond-continuum observable search.

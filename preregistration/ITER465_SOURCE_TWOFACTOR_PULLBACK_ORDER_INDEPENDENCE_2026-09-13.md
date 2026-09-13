# Iter465 preregistration — source two-factor distributional pullback / order independence

Date: 2026-09-13

## Scientific target
Test the **next D7-S2 prerequisite after Iter464**, without promoting the one-dimensional result to a full causal-vertex theorem.

The object is the tensor product of two exact Iter464 source channels,

`F(x1,x2)/[(x1-rho1-i*s1*0)(x2-rho2-i*s2*0)]`,

where each source factor is the exact finite exponential-polynomial representation reconstructed from `P11*d_source`. The gate checks whether this source-defined two-factor distributional object is invariant under frozen invertible linear reparameterizations and whether its canonical double-boundary value is independent of the order in which the two independent pole factors are resolved.

This is intentionally a **two-factor transversal pullback certificate only**. It does not represent the full causal vertex, shared-pole/non-transversal collisions, or a convergence theorem.

## Frozen panel
Six source-pair lanes:
1. `(m1,m2,beta1,beta2)=(-1,0,0.8,2.1)`
2. `(0,1,2.1,0.8)`
3. `(-1,1,2.1,2.1)`
4. `(0,0,0.8,2.1)`
5. `(1,-1,0.8,0.8)`
6. `(1,0,2.1,0.8)`

For every lane:
- `rho1=0.35`, `rho2=1.6`;
- all four boundary-sign pairs `(s1,s2) in {±1}^2`;
- all source exponential channels whose frequency signs match their respective boundary signs are retained, with their full polynomial coefficients through degree 2;
- frozen integer reparameterizations
  - `M1=[[1,1],[0,1]]`, det `+1`;
  - `M2=[[1,0],[1,1]]`, det `+1`;
  - `M3=[[2,1],[1,1]]`, det `+1`;
  - `M4=[[1,2],[1,1]]`, det `-1`.

## Frozen calculations
For each record compute independently:

A. **Canonical tensor-product selector value** in the original `(x1,x2)` variables as the product of the two Iter464 exact one-dimensional boundary selectors.

B. **Intersection/residue value after linear pullback** in `y=M x`: solve the two transformed pole hyperplanes exactly/numerically at high precision, include the absolute Jacobian factor, evaluate the transformed exponential-polynomial numerator at the common pole, and include the determinant of the transformed pole-normal matrix.

C. **Sequential resolution 1→2** using Schur-complement elimination of the transformed linear pole system.

D. **Sequential resolution 2→1** using the opposite Schur-complement elimination.

The two sequential routes are algebraically independent implementations and must agree with A/B whenever the transformed pole normals are transversal (all frozen M are invertible).

## Frozen controls
- Wrong sign control: flip exactly one boundary sign while keeping the original source-channel selector; relative difference from the canonical record must be `>=1e-3` whenever the canonical magnitude is `>=1e-20`.
- Wrong Jacobian control: omit the `1/abs(det M)` measure compensation. For the det=-1 lane this control is not discriminating by magnitude, so additionally use a synthetic scaling matrix `M5=[[2,0],[0,1]]`, det `2`, **control only**, and require relative difference `>=0.25` when the canonical magnitude is `>=1e-20`. M5 is not part of scientific pullback qualification.
- Singular-normal null control: `Msing=[[1,1],[2,2]]` must be detected as non-invertible/non-transversal and must not be assigned a finite qualified value.

## Frozen thresholds
For non-negligible canonical records (`|A|>=1e-20`):
- `rel(A,B) <= 1e-35`;
- `rel(A,C) <= 1e-35`;
- `rel(A,D) <= 1e-35`;
- `rel(C,D) <= 1e-35`;
- wrong-sign separation `>=1e-3`;
- wrong-Jacobian M5 separation `>=0.25`.

For negligible canonical records, require absolute differences `<=1e-45` and finite values.

All M1-M4 transformed normal determinants must be nonzero; Msing must be rejected.

## Frozen classification
PASS only if every scientific record and every control satisfies the frozen rules:

`ITER465_SOURCE_TWOFACTOR_TRANSVERSAL_PULLBACK_ORDER_INDEPENDENCE_QUALIFIED_SCOPED`

Otherwise:

`SCIENTIFIC_FAIL_ITER465_SOURCE_TWOFACTOR_PULLBACK_OR_ORDER_INDEPENDENCE`

Infrastructure, parser, dependency, or arithmetic exceptions before a valid record set are **not** scientific FAIL and must be classified separately.

## Interpretation lock
A PASS qualifies only a transversal two-factor tensor-product/source-channel pullback and order-independence prerequisite. It does **not** close D7-S2; the next unresolved layer is correlated/shared-variable or non-transversal multivariable structure from the actual causal-vertex contraction. A FAIL is a scoped failure of this frozen construction, not a universal causal-EPRL no-go theorem.

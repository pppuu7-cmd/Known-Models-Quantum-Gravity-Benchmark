# Comparator Residual-Space Geometry Protocol

**Protocol ID:** `KMQGB-RSG-001`  
**Purpose:** define the mathematical novelty quotient that must be passed before any future Candidate Gravity ansatz is promoted.

This protocol acts **after** physical observables, exact Ward/contact/constraint relations and a common validity domain have been frozen.

## 1. Observable space and whitening

Let the physical real observable vector be

`y in R^m`.

Complex observables are split into real and imaginary components only after exact conjugation/symmetry relations are applied, so no redundant coordinates are counted twice.

For one comparator family,

`c(theta)`

with covariance `Sigma`, define a profiled point `theta_*` and residual

`r = y - c(theta_*)`.

Let

`W = Sigma^{-1}`

on the supported physical subspace and whiten

`z = W^(1/2) r`.

The comparator tangent Jacobian is

`J_C = partial c / partial theta |_(theta_*)`,

`A_C = W^(1/2) J_C`.

## 2. Local comparator quotient

The local comparator tangent space is `col(A_C)`.

Define

`Pi_C = A_C A_C^+`,

`Pi_perp = I - Pi_C`,

where `A_C^+` is the Moore-Penrose pseudoinverse.

The **Comparator-Orthogonal Residual (COR)** is

`COR = Pi_perp z`.

A locally exact degeneracy has

`COR = 0`.

For a predicted candidate signal direction `s`, define its whitened direction

`s_w = W^(1/2) s`

and local separation fraction

`eta(s) = ||Pi_perp s_w|| / ||s_w||`.

Interpretation:

- `eta=0`: exact local tangent degeneracy;
- `0<eta<<1`: near-degeneracy / poor local identifiability;
- `eta` bounded away from zero: locally distinct direction, still subject to nonlinear/global profiling.

Do not invent a universal numerical threshold for `eta`; thresholds depend on the frozen measurement/statistical problem and must be pre-registered there.

## 3. Exact Ward/contact/constraint reduction must come first

Suppose exact linear physical relations are represented by

`L y = 0`.

Choose a full-column-rank basis `Z` for the physical null space,

`L Z = 0`.

Parameterize physical observables by

`y = Z x`.

Then perform comparator profiling in the reduced physical coordinate `x`, with the covariance and Jacobians pushed into the same basis. Do **not** count Ward/gauge/contact-null directions as residual dimensions.

For nonlinear constraints, use an explicit local coordinate chart on the constraint surface or the corresponding tangent-null basis, and retain a separate finite/global constraint validation.

Rule:

`constraint quotient -> physical observable basis -> comparator quotient`,

never the reverse.

## 4. Nuisance-block geometry

Partition comparator/nuisance coordinates schematically as

`theta={theta_dyn,theta_state,theta_detector,theta_cal,theta_mediator,...}`.

Corresponding tangent blocks:

`A=[A_dyn A_state A_detector A_cal A_mediator ...]`.

The **final novelty verdict always uses the joint column space** `col(A)`.

Blockwise projections are diagnostic only because sequential projection can be order-dependent when tangent blocks overlap.

Useful diagnostic quantities:

- block ranks;
- pairwise principal angles between nuisance subspaces;
- incremental rank after adding a block;
- overlap of a proposed KG signal with each block;
- which attribution layer absorbs the candidate direction.

This supplies a quantitative version of the frozen attribution stack.

## 5. Multiple comparator families

For locally linearized comparator families `C_a`, build the union tangent matrix

`A_union=[A_C0 A_C1 ... A_C6 A_C3b A_extra ...]`

after removing duplicate/representation-equivalent directions.

Use

`Pi_perp,union = I - A_union A_union^+`.

A candidate locally survives only if its direction has nonzero component in the union-comparator complement.

If families occupy disconnected/nonlinear manifolds, union-tangent projection is only a local prefilter; perform the global profile in section 6.

## 6. Nonlinear / finite comparator-manifold quotient

A local transverse direction can disappear under a finite excursion on a curved comparator manifold.

Define the common-domain profiled distance

`d_C^2(y) = inf_{theta in D_C} [y-c(theta)]^T Sigma(theta)^(-1) [y-c(theta)]`,

with

- all validity-domain constraints included in `D_C`;
- nuisance/state/detector ranges declared prospectively;
- covariance dependence handled consistently;
- boundaries and multiple minima audited.

For a proposed KG family `k(lambda)`, define a theory-separation problem

`d_min^2 = inf_{lambda in D_KG, theta in D_C} || W^(1/2)[k(lambda)-c(theta)] ||^2`

in a genuinely common validity domain.

A local COR is **not** a robust residual until finite/global profiling confirms that the comparator manifold cannot reach it.

## 7. Curvature / second-order warning

Let `H_C` denote second derivatives of the comparator map. If the residual scale is comparable to the normal displacement produced by allowed second-order comparator curvature, the tangent result is unreliable.

At minimum, audit

- second-order Taylor movement over the allowed nuisance range;
- sampled/profiled comparator manifold;
- stability of `COR` under the profiled point and bin/kinematic choices.

## 8. Candidate-parameter identifiability

For a concrete future KG parameter/vector `lambda`, define

`J_KG = partial k / partial lambda`,

`B_KG = Pi_perp,union W^(1/2) J_KG`.

The singular values of `B_KG` diagnose which KG parameter combinations remain identifiable **after** comparator profiling.

- zero singular value: locally absorbed/unidentifiable KG direction;
- very small singular value: near-degenerate direction;
- nonzero well-conditioned singular directions: candidates for further global/Fisher/resource analysis.

Do not run Fisher/resource claims on unprojected `J_KG`.

## 9. Robust residual certificate — pre-resource gate

Before a proposed Candidate Gravity ansatz is promoted beyond a design hypothesis, require all of:

1. exact physical/constraint basis frozen;
2. common validity domain frozen;
3. full applicable C5 parent included at the same order;
4. all C0-C6/C3b and stronger comparator/nuisance tangent blocks included;
5. field-redefinition/representation duplicates quotiented;
6. nonzero local comparator-orthogonal signal direction;
7. finite/global comparator profiling cannot absorb the direction;
8. result stable under declared state/detector/calibration ranges;
9. residual links at least two attribution layers rather than one feature coordinate;
10. Ward/contact/causal/relational structure remains satisfied;
11. if data are used, statistical significance is calibrated for profiling/boundaries rather than assuming an automatic chi-square law;
12. only then proceed to Fisher/identifiability/resources.

## 10. Consequence for Candidate Gravity design

The benchmark no longer asks for a qualitatively unusual effect. It asks for a concrete vector or relation whose projection onto the complement of the **full physical comparator manifold** is nonzero and robust.

Symbolically, the future KG target is

`Delta_KG^robust = inf_{C in comparator union} distance_W( O_KG , M_C ) > 0`

subject to all frozen attribution, causality, Ward/contact, relational and common-domain conditions.

No such robust residual has yet been established.

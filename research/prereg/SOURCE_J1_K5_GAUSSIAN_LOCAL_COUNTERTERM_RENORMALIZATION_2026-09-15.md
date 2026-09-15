# Prospective preregistration — Gaussian local-counterterm renormalization

Date: 2026-09-15
Gate: `SOURCE_J1_K5_GAUSSIAN_LOCAL_COUNTERTERM_RENORMALIZATION_GATE`
Status: `PROSPECTIVELY_FROZEN`

## Parent authority

Latest validated parent:

- `results/SOURCE_J1_K5_GAUSSIAN_COMPACT_SUPPORT_LOCALIZATION_RESULT_2026-09-15.md`
- result commit `a0ba962811b9364bceb03a28f4785aa75e42213a`
- classification `AUX_GAUSSIAN_UNRENORMALIZED_COMPACT_LOCAL_DIVERGENCE_SCOPED`
- authoritative parent run `34954491166`.

The parent establishes only that the same unrenormalized auxiliary Gaussian divergence is local to the aligned K5 collision neighborhood on P1-P3. It does not exclude a renormalized local extension.

The Critic-invalidated historical joint-Feynman source-authority blocker is not consumed as a premise.

## HYPOTHESIS

For the exact same scalar aligned-K5 Gaussian auxiliary object, the local divergence may be removable by a collision-supported O(4)-invariant counterterm of the full uniform-scaling degree allowed by the surrogate.

Each of the ten one-dimensional `delta''` factors has uniform scaling degree 3. Their product therefore has uniform scaling degree 30 in the four gauge-fixed scalar relative coordinates. The corresponding divergence degree is prospectively frozen as

`omega = 30 - 4 = 26`.

For O(4)-invariant scalar test functions, freeze the complete even local basis through order 26 as

`{ Delta^j delta_0 : j=0,...,13 }`.

On the frozen Gaussian test family

`phi_alpha(x) = exp(-alpha |x|^2)`, `alpha>0`,

this basis is equivalent to the polynomial space of degree <=13 in `alpha`, because in four dimensions

`(Delta^j phi_alpha)(0) = (-4 alpha)^j (j+1)!`.

Thus the gate tests locality on a family of test functions rather than cancelling one scalar pairing.

## Frozen object

Use exactly the parent:

- aligned K5 incidence geometry and edge order;
- scalar gauge-fixed four-coordinate auxiliary object;
- ten Gaussian `delta_epsilon''` factors;
- P1-P3 anisotropic exponent vectors;
- `t=2^-k`;
- decision grid `k={5,6,7,8}`;
- high-precision Gaussian/Wick evaluator.

P0 is reproduction/control only and cannot enter classification.

No new regulator path, source object, physical model, D7 threshold, or source-authority claim is introduced.

## Frozen renormalization condition

For every `(path,k)` independently, evaluate the unrenormalized pairing

`F_{path,k}(alpha) = <T_epsilon, exp(-alpha |x|^2)>`

on the 14 calibration points

`A_cal = {0.50,0.60,0.70,0.80,0.90,1.00,1.10,1.20,1.30,1.40,1.50,1.60,1.70,1.80}`.

Fit the unique degree-<=13 polynomial `C_{path,k}(alpha)` interpolating all 14 calibration values. This polynomial is the frozen KMQGB-derived local counterterm action on the Gaussian test family. Algebraically it is equivalent to coefficients of `Delta^j delta_0`, `j=0..13`.

No calibration point may be changed after execution.

The counterterm coefficients may depend on the full regulator vector epsilon, as regulator-dependent divergent local coefficients normally do, but may not depend on the held-out test point except through the single frozen polynomial `C_{path,k}` determined from `A_cal`.

## Frozen held-out tests

The independent held-out set is

`A_test = {0.55,0.95,1.35,1.75,1.95}`.

For each held-out alpha define

`R_{path,k}(alpha) = F_{path,k}(alpha) - C_{path,k}(alpha)`.

No held-out value participates in fitting.

## Numerical implementation

- arithmetic: `mpmath==1.3.0`;
- minimum precision: 180 decimal digits;
- fit in the shifted/scaled coordinate `z=(alpha-1.15)/0.65` to reduce conditioning;
- polynomial space remains exactly degree <=13; the coordinate change does not alter the local basis span;
- solve the 14x14 interpolation system at high precision;
- independently evaluate the same interpolant at held-out points using a barycentric interpolation formula from the same calibration data;
- linear-solve and barycentric held-out predictions must agree to relative tolerance `1e-120` (absolute fallback `1e-120`).

## Positive controls

1. At `alpha=1`, reproduce the source-locked parent P1-P3 pairings for `k=5..8` to relative tolerance `1e-45`. The durable parent artifact serializes these values to approximately 50 significant digits, so this is the strongest prospective lock supported by the stored authority record; demanding more digits would test unavailable serialization rather than scientific drift.
2. Reproduce the exact K5 star-coordinate-basis incidence rows.
3. All covariance matrices used by the Wick evaluator are positive definite.
4. Calibration interpolation residual at every `A_cal` point is <= `1e-130` relative (absolute fallback `1e-130`).
5. Linear-solve and barycentric held-out counterterm predictions agree to `1e-120` relative/absolute fallback.
6. The analytic identity `(Delta^j phi_alpha)(0)=(-4 alpha)^j (j+1)!` is independently checked for `j=0..4` by symbolic/radial recurrence in code.
7. A frozen vertex relabel control at P3, `k=5`, `alpha=1.35` agrees to relative tolerance `1e-90`.

## Adversarial controls

1. A synthetic degree-14 polynomial fixture sampled on `A_cal` must not be reproduced exactly on all `A_test` by the degree-13 interpolant; otherwise the held-out logic is invalid.
2. A synthetic path-dependent finite-offset fixture must classify as path-dependent under the frozen downstream classifier.
3. P0 must not enter any deciding fit, residual, or classification.
4. Any failed parent-value lock, changed alpha grid, changed polynomial degree, or use of held-out values in fitting is `INVALID_IMPLEMENTATION`.

## Frozen convergence classifier

For each held-out `alpha` and each path P1-P3, use residuals at `k=5,6,7,8`.

Let

- `d56=|R6-R5|`,
- `d67=|R7-R6|`,
- `d78=|R8-R7|`,
- `rel78=|R8-R7| / max(1,|R8|,|R7|)`.

A path/alpha pair is `FINITE_COMPATIBLE` iff

- `d56 > d67 > d78`, and
- `rel78 <= 1e-8`.

It is `DIVERGENT_AFTER_LOCAL_SUBTRACTION` iff the last three absolute residuals are strictly increasing and the median of the two last base-2 growth rates is >=2.

Otherwise it is `INCONCLUSIVE`.

For a held-out alpha, if all P1-P3 are `FINITE_COMPATIBLE`, define the cross-path final spread

`spread = max_{p,q}|R_{p,8}-R_{q,8}| / max(1,max_p |R_{p,8}|)`.

The held-out alpha is `PATH_INDEPENDENT_FINITE` iff `spread <= 1e-6`; otherwise it is `FINITE_PATH_DEPENDENT`.

## Terminal classifications

### `AUX_GAUSSIAN_LOCAL_RENORMALIZED_EXTENSION_COMPATIBLE_SCOPED`

iff all controls pass and all five held-out alphas are `PATH_INDEPENDENT_FINITE`.

This is evidence only for existence of a KMQGB-derived local renormalization in this auxiliary scalar Gaussian family under the frozen normalization conditions.

### `AUX_GAUSSIAN_LOCAL_RENORMALIZED_PATH_DEPENDENCE_WITNESS_SCOPED`

iff all controls pass, every held-out alpha is finite-compatible on all three paths, and at least one held-out alpha is `FINITE_PATH_DEPENDENT`.

### `AUX_GAUSSIAN_LOCAL_COUNTERTERM_ANSATZ_INSUFFICIENT_SCOPED`

iff all controls pass and at least one held-out path/alpha is `DIVERGENT_AFTER_LOCAL_SUBTRACTION`.

### `AUX_GAUSSIAN_LOCAL_RENORMALIZATION_INCONCLUSIVE`

iff controls pass but none of the above terminal predicates applies.

### `INVALID_IMPLEMENTATION`

for failed source lock, parent-value drift, altered frozen object/grid/test sets/basis degree, failed controls, held-out leakage into fit, or numerical interpolation inconsistency.

## Finite ambiguity accounting

Before imposing the 14 frozen renormalization conditions, the O(4)-invariant local extension space tested here has 14 finite coefficients, one for each `Delta^j delta_0`, `j=0..13`.

The calibration conditions fix those 14 coefficients uniquely at each regulator state. Therefore a compatible finite limit under this gate demonstrates existence under one KMQGB-derived normalization scheme but does **not** establish source-authorized uniqueness. A different admissible set of finite renormalization conditions can shift the limit by a collision-supported local distribution.

This is consistent with earlier repository evidence that collision-supported homogeneous ambiguity is a separate uniqueness issue conditional on extension existence.

## Interpretation ceiling

No outcome of this gate by itself establishes:

- existence/nonexistence of the published Eq. (4) distribution;
- source authorization of this counterterm prescription;
- uniqueness of a physical extension;
- validity beyond the auxiliary scalar Gaussian aligned-K5 witness;
- model/family failure;
- D7-S2/S3/S4 closure;
- `EXISTING_SUFFICIENT`, `ADAPT_EXISTING`, `HYBRID_REQUIRED`, or `NEW_REQUIRED`;
- Candidate Gravity activation.

A compatible result is KMQGB-derived mathematical extension evidence only. An insufficient result rejects only this frozen O(4)-invariant local ansatz/test protocol, not all possible renormalizations.

Governance remains: `RQIR Core v1.0 = FROZEN`; D7-S2/S3 not closed; D7-S4 partial; terminal selectors forbidden; Candidate Gravity inactive; KMQGB remains downstream of pinned DSIR authority.

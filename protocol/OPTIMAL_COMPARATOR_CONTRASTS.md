# Optimal Comparator-Annihilating Contrasts for Future Candidate Gravity

**Status:** frozen methodology layer for KMQGB wave 9.  
**Purpose:** turn comparator-residual geometry into constructive observable combinations and experimental/source-detector design rules before any Candidate Gravity ansatz is promoted.

## 1. Inputs and order of operations

All exact Ward/contact/gauge/constraint identities are imposed first. Work only in the resulting physical observable basis.

Let

- `y in R^m` be the physical observable vector;
- `Sigma` be its covariance matrix in the common validity domain;
- `J_C in R^(m x p)` be the union Jacobian of all allowed comparator/nuisance directions after block assembly;
- `s in R^m` be a pre-registered candidate signal direction when one exists.

The union Jacobian may contain dynamics, state, detector, calibration, source, mediator and other admissible nuisance blocks. The final null condition uses the **joint span**, not separate per-block verdicts.

## 2. Exact comparator-null contrasts

A linear contrast

`X_w = w^T y`

is locally insensitive to all comparator/nuisance retunings iff

`J_C^T w = 0`.

Thus the exact contrast space is the left nullspace of `J_C` in the physical basis.

If `rank(J_C)=r`, then for full-rank covariance the algebraic number of locally comparator-null contrast directions is

`d_perp = m-r`.

This count is a local tangent-space statement only; finite/global comparator profiling remains mandatory.

## 3. Covariance-optimal contrast for a proposed signal

For a candidate signal direction `s`, maximize

`SNR(w)=|w^T s|/sqrt(w^T Sigma w)`

subject to

`J_C^T w=0`.

For positive-definite `Sigma`, let `Sigma^(-1/2)` be the symmetric inverse square root and define

`A = Sigma^(-1/2) J_C`,

`Pi_perp = I - A A^+`.

Then an optimal direction is

`w_opt proportional to Sigma^(-1/2) Pi_perp Sigma^(-1/2) s`.

Normalize by `w_opt^T Sigma w_opt = 1` if a unit-variance contrast is desired.

The maximum achievable local comparator-null SNR is

`SNR_max = ||Pi_perp Sigma^(-1/2) s||`.

If this quantity is zero, the proposed signal is exactly locally absorbed by the union comparator tangent.

## 4. Observable augmentation rule

Suppose `k` new physical observables are added after all exact constraints are imposed. Let the comparator tangent rank change by

`Delta r = rank(J_C,new) - rank(J_C,old)`.

Then the local comparator-complement dimension changes exactly as

`Delta d_perp = k - Delta r`.

Consequences:

- if each new observable adds an independent comparator tangent direction, it may add **zero** novelty dimension;
- a new observable is structurally valuable when it enlarges the physical data space more than it enlarges the union comparator rank;
- more numerical precision in an already rank-saturated observable set cannot create a new algebraic residual direction.

For the current RQIR three-bucket pre-registration, if `rank(A_union)=3`, then `d_perp=0` and an additional linked observable is required regardless of bucket precision.

## 5. Correlated covariance and common-mode rejection

Do not diagonalize errors by assumption.

For positive-semidefinite `Sigma`, use an eigendecomposition/SVD on its supported subspace and the Moore-Penrose inverse square root. Exact zero-variance constraints must be handled as constraints, not as noisy directions.

Distinguish:

1. **stochastic correlated noise**, represented in `Sigma`;
2. **deterministic or calibratable common-mode nuisance**, represented as columns of `J_C`.

A contrast can reject both when it lies in the comparator left nullspace and is optimized using the full covariance metric.

Never count an exact common mode twice as both a free nuisance parameter and an independent stochastic direction without an explicit generative model.

## 6. Projected Candidate-Gravity identifiability matrix

For a future Candidate Gravity Jacobian `J_KG` define

`B_KG = Pi_perp Sigma^(-1/2) J_KG`.

Only singular directions of `B_KG` can be identified after local comparator profiling.

Design diagnostics:

- `rank(B_KG)`: number of locally identifiable KG parameter combinations;
- `sigma_min^+(B_KG)`: weakest nonzero projected singular value;
- condition number on the nonzero singular subspace;
- principal angles between the KG and comparator tangent spaces.

A tiny nonzero singular value is a near-degeneracy warning, not a robust discovery coordinate.

## 7. Experimental/source-detector design criterion

For a configurable design `d` (source masses, branch geometry, frequencies, detector orientations, proper-time separations, probe states, readout settings, etc.), compute

`Sigma(d)`, `J_C(d)`, and when available `J_KG(d)` or a pre-registered signal vector `s(d)`.

Single-signal objective:

`Phi_signal(d)=||Pi_perp(d) Sigma(d)^(-1/2) s(d)||^2`.

Multi-parameter objectives may include

- E-optimal: maximize the smallest robust nonzero singular value of `B_KG(d)`;
- D-optimal: maximize `log det[B_KG^T B_KG]` on the declared identifiable subspace;
- rank-first design: maximize robust numerical rank before conditioning/SNR refinements.

The design objective and allowed design domain must be frozen **before** looking at the candidate data/residual to avoid post-hoc observable selection.

## 8. Global/nonlinear guardrail

Comparator-null contrasts are local constructions. Every surviving contrast must still pass the nonlinear/global profile

`d_C^2(y)=inf_theta [y-c(theta)]^T Sigma(theta)^(-1)[y-c(theta)]`

and, for theory-family separation, a joint finite-domain minimum over Candidate Gravity and comparator parameters.

A locally nonzero contrast is therefore a promotion prefilter, not final evidence.

## 9. Candidate Gravity design consequence

Future KG observables should not be chosen because they are individually exotic. Prefer observables that satisfy

`Delta m_phys > Delta rank(J_union)`

and that increase the robust singular values of the projected KG Jacobian.

This converts the accumulated benchmark lesson into a constructive rule:

> **Add observables that increase comparator-orthogonal dimension and conditioning, not merely the length of the observable list.**

Cross-order/cross-attribution observables are especially valuable because they may add physical dimensions without opening equally many independent comparator nuisance directions.

## 10. Promotion guardrail

No Candidate Gravity ansatz is promoted because an optimal contrast protocol exists.

Promotion still requires a concrete parent dynamics, full-C5 and C0-C6/C3b matching, exact Ward/contact/constraint completion, attribution-stack survival, a nonzero global residual, rigidity and only then Fisher/resources.

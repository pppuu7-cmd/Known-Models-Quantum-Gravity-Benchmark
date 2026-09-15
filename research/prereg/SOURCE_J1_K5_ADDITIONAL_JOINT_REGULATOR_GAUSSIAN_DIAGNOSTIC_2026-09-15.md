# Prospective preregistration — additional joint-regulator Gaussian diagnostic

Date: 2026-09-15
Gate: `SOURCE_J1_K5_ADDITIONAL_JOINT_REGULATOR_GAUSSIAN_DIAGNOSTIC_GATE`
Status: `PROSPECTIVELY_FROZEN_FOR_NEW_ANISOTROPIC_PATHS`

Parent frontier: `SOURCE_J1_K5_ADDITIONAL_JOINT_REGULATOR_EQUIVALENCE_GATE` recommended by the terminal repaired Eq.4 existence result at commit `6c4d479c42d3b71de4c4c32c5abb910728b97fc9` / recovery index `83fa7055611dbc5c77180e62ae7ea8ede0dea6c6`.

## Exploratory disclosure

Before this preregistration, a private local sanity calculation was used only to verify that the proposed finite-dimensional Gaussian-moment algorithm is computationally viable on the **common-regulator** path. That exploratory common-path value/growth behavior is not prospective scientific evidence and MUST NOT be used to satisfy the new anisotropic-path decision criteria below.

The new scientific evidence of this gate is restricted to the frozen anisotropic paths P1-P3 and their independently generated high-precision outputs after this commit. P0 is reproduction/control only.

## HYPOTHESIS

A natural KMQGB-derived auxiliary extension candidate is obtained by replacing each highest-contact one-wedge factor `delta''(B_e)` by the second derivative of a normalized Gaussian approximate identity of width `epsilon_e`, multiplying the ten smooth factors on the exact aligned K5 conormal witness, and pairing with a fixed Schwartz localization. If this family were a plausible path-independent unrenormalized joint extension candidate, the pairing should have a finite regulator-removal limit independent of prospectively frozen relative regulator rates. Divergence or relative-rate dependence rejects **this auxiliary Gaussian candidate** but does not establish nonexistence of the published Eq. (4) distribution.

## EXACT OBJECT

Frozen graph/geometry:

- K5 vertices `(1,2,3,4,5)`;
- gauge-fixed free vertices `(2,3,4,5)`;
- ten oriented edges `(a,b)`, `a<b`;
- aligned Bloch vector `n0=(0,0,1)`;
- exact conormals `dB_ab=(e_a-e_b) tensor n0` from `code/source_j1_k5_aligned_contact_cyclespace_certificate.py`;
- exact conormal rank `4`, relation-space dimension `6`.

Because the frozen aligned witness depends only on the four z-normal coordinates, the diagnostic integrates those four active coordinates exactly and treats the eight spectator Gaussian test coordinates as a factored constant.

Frozen one-dimensional mollifier:

`delta_epsilon(B) = exp(-(B/epsilon)^2)/(sqrt(pi)*epsilon)`

and

`delta_epsilon''(B) = (4 B^2/epsilon^4 - 2/epsilon^2) * delta_epsilon(B)`.

Frozen test localization on the four active variables:

`phi(x)=exp(-x dot x)`.

This Schwartz test is a **diagnostic localization**, not a proof of convergence/nonconvergence in all of `D'`. A later compact-support localization theorem/control is required before promoting any diagnostic divergence to a theorem about the published distribution.

Frozen pairing:

`J(epsilon_1,...,epsilon_10) = integral_R4 phi(x) product_e delta_epsilon_e''(a_e dot x) d^4 x`,

where `a_e` is the exact 4D scalar incidence row inherited from the conormal certificate.

The integral must be evaluated by Gaussian covariance/Wick moments, not Monte Carlo or adaptive quadrature.

## REGULATOR PATHS

Let `t_k=2^{-k}` for `k=3,4,5,6,7,8`.

Edge order is frozen lexicographically:
`12,13,14,15,23,24,25,34,35,45`.

- P0 reproduction only: exponents `(1,1,1,1,1,1,1,1,1,1)`.
- P1 NEW: star-tree edges `12,13,14,15` use `epsilon=t`; six non-tree edges use `epsilon=t^2`: exponents `(1,1,1,1,2,2,2,2,2,2)`.
- P2 NEW: star-tree edges use `epsilon=t^2`; six non-tree edges use `epsilon=t`: exponents `(2,2,2,2,1,1,1,1,1,1)`.
- P3 NEW: vertex-graded rates `(1,2,3,4,2,3,4,3,4,4)` in the frozen edge order.

No path may be added or removed after seeing output.

## NUMERICAL / EXACT ALGORITHM

Use at least 100 decimal digits (`mpmath`, pinned version in workflow).

For each regulator vector:

1. form `M = I_4 + A^T diag(epsilon_e^-2) A`;
2. use covariance `Sigma=(1/2) M^-1`;
3. form ten-variable covariance `C=A Sigma A^T` for `y_e=a_e dot x`;
4. evaluate all Gaussian moments required by the product of ten quadratic factors using exact Wick/Isserlis recursion over multiplicity vectors; no random sampling;
5. multiply by the analytic Gaussian normalization `pi^2/sqrt(det(M))` and the ten mollifier normalizations.

Internal controls must include symmetry of `C`, positive definiteness of `M`, independent direct low-order moment identities, and a lower-dimensional two-edge analytic fixture.

## FROZEN METRICS

For each path record `J_k` and:

- `g_k = log2(|J_{k+1}/J_k|)` for adjacent frozen `k` values when both are nonzero;
- terminal three-step growth estimate `g_tail = median(g_5,g_6,g_7)` corresponding to transitions `k=5->6`, `6->7`, `7->8`;
- sign stability over the final three grid points.

No post-hoc rescaling may be used to manufacture a finite limit.

A path is `UNRENORMALIZED_DIVERGENT_DIAGNOSTIC` if all final three `|J_k|` are strictly increasing and `g_tail >= 2.0` with high-precision finite arithmetic.

A path is `FINITE_LIMIT_COMPATIBLE_DIAGNOSTIC` only if final adjacent absolute differences decrease monotonically and the final relative change is <= `1e-8` without rescaling.

Otherwise it is `INCONCLUSIVE_DIAGNOSTIC`.

## OUTCOME-SENSITIVE CONTROLS

1. a zero-edge/no-contact Gaussian integral fixture must return its known analytic value;
2. a one-edge `delta_epsilon''` pairing against the frozen Gaussian test must agree with an independently derived closed formula;
3. permuting vertices `2..5` together with the regulator assignment must leave the pairing invariant;
4. changing only the regulator assignment while holding geometry fixed must be capable of changing the path metrics; the implementation must not hard-code a common exponent;
5. P0 is labeled `EXPLORATORY_REPRODUCTION_ONLY` and cannot decide the scientific classification.

## TERMINAL CLASSIFICATIONS

### `AUX_GAUSSIAN_JOINT_REGULATOR_REJECTED_UNRENORMALIZED_SCOPED`

iff all controls pass and at least **two of P1-P3** are `UNRENORMALIZED_DIVERGENT_DIAGNOSTIC`. This rejects the unrenormalized Gaussian approximate-identity family as an immediate source-equivalent extension candidate in the frozen highest-contact aligned witness.

### `AUX_GAUSSIAN_JOINT_REGULATOR_PATH_DEPENDENCE_WITNESS_SCOPED`

iff all controls pass and at least two NEW paths have incompatible terminal behavior (for example one finite-limit-compatible and one divergent, or two finite nonzero limits differing beyond `1e-8`). This is stronger evidence against path independence of this auxiliary family.

### `AUX_GAUSSIAN_JOINT_REGULATOR_SURVIVES_DIAGNOSTIC_SCOPED`

iff all three NEW paths are finite-limit-compatible and agree in their terminal values to relative `1e-8`. This only authorizes a separately preregistered compact-support/source-equivalence gate; it is not proof of Eq. (4) existence.

### `AUX_GAUSSIAN_JOINT_REGULATOR_DIAGNOSTIC_INCONCLUSIVE`

for valid controls but no condition above.

### `INVALID_IMPLEMENTATION`

for failed source/geometry lock, failed analytic control, insufficient precision, altered paths/grid/thresholds, use of exploratory P0 as deciding evidence, or any post-hoc renormalization/counterterm.

## INTERPRETATION CEILING

This gate tests only one explicit KMQGB-derived **auxiliary regulator family** for the source-present highest-contact sector on the aligned K5 witness. Rejection does not prove that the source Eq. (4) distribution does not exist and does not rule out renormalized, microlocal, Epstein-Glaser-like, common-boundary-value, or other canonical extensions. Survival does not establish source equivalence.

No D7 terminal selector is authorized. `D7-S2`, `D7-S3`, `D7-S4` retain their current locked statuses. Candidate Gravity remains inactive.

# Prospective preregistration — Gaussian compact-support localization

Date: 2026-09-15
Gate: `SOURCE_J1_K5_GAUSSIAN_COMPACT_SUPPORT_LOCALIZATION_GATE`
Status: `PROSPECTIVELY_FROZEN`

## Parent

Validated terminal diagnostic:

- `results/SOURCE_J1_K5_ADDITIONAL_JOINT_REGULATOR_GAUSSIAN_DIAGNOSTIC_RESULT_2026-09-15.md`
- result commit `8982ea92de08bfb6028df35be16f116e0e58c22f`
- classification `AUX_GAUSSIAN_JOINT_REGULATOR_REJECTED_UNRENORMALIZED_SCOPED`.

This gate does not reopen or change the parent paths/grid/thresholds. It asks whether the parent divergence is local to the K5 collision rather than an artifact of the noncompact Schwartz test tail.

## HYPOTHESIS

For each NEW parent path P1-P3, replace the parent test `phi(x)=exp(-|x|^2)` by

`phi_chi(x)=exp(-|x|^2) chi(x)`

where `chi` is any smooth real cutoff satisfying

- `0 <= chi <= 1`;
- `chi(x)=1` for `|x| <= 1`;
- `chi(x)=0` for `|x| >= 2`.

If an explicit analytic upper bound on the omitted exterior contribution is negligible relative to the already source-locked parent pairing and is small enough to preserve the frozen divergent growth inequalities, then the unrenormalized Gaussian divergence is certified as a **local compact-support diagnostic** on that path without choosing a special transition profile for `chi`.

## Frozen object and authority

Use exactly the parent aligned K5 incidence geometry, Gaussian mollifier, highest-contact ten-factor object, edge order, P1-P3 exponents and grid `k=3..8`.

No new regulator path and no counterterm is allowed.

The parent P0 remains excluded from science classification.

## Analytic exterior bound

For every edge and `epsilon <= 1`, with `B_e=a_e dot x` and `|a_e|^2 <= 2`, use the pointwise bound

`|delta_epsilon''(B_e)| <= (10/sqrt(pi)) epsilon^{-5} (1+|x|^2) exp(-B_e^2/epsilon^2)`.

For the K5 star edges `12,13,14,15`, the gauge-fixed scalar incidence rows are exactly the four signed coordinate basis rows. Therefore

`sum_e B_e^2/epsilon_e^2 >= q_path(t) |x|^2`,

where the frozen lower bounds are

- P1: `q=t^{-2}`;
- P2: `q=t^{-4}`;
- P3: `q=t^{-2}`.

Consequently, for the difference between the parent full-Schwartz pairing `J` and any admissible compact pairing `J_chi`, freeze the bound

`|J-J_chi| <= B_ext`

with

`B_ext = (10/sqrt(pi))^10 * product_e epsilon_e^{-5} * pi^2 * integral_1^infinity u(1+u)^10 exp(-(1+q)u) du`.

The one-dimensional integral must be evaluated from the exact finite binomial expansion and upper incomplete gamma function at >=100 decimal digits. No multidimensional quadrature or stochastic sampling is needed.

## Frozen certificate grid

Only the parent NEW paths P1-P3 decide the gate.

For each path compute `B_ext(k)` on the unchanged parent grid. The compact-localization decision uses only `k=5,6,7,8`, fixed prospectively here.

Let parent pairings be `J_k > 0` as source-locked from run `34954054888` / artifact `10390423124`.

Define rigorous diagnostic intervals

`L_k = J_k - B_ext(k)` and `U_k = J_k + B_ext(k)`.

## Positive controls

1. Reproduce the exact K5 star-coordinate-basis incidence rows.
2. Verify all parent P1-P3 values consumed are byte-for-byte/numerically equal to the frozen canonical constants copied from the terminal artifact/log record; no recomputation may silently change parent evidence.
3. Verify `B_ext(k)>0` and finite.
4. Verify the radial-integral implementation against direct symbolic expansion at one fixed alpha value using two algebraically independent formulas.

## Adversarial controls

1. Replace `q` by zero in a control calculation; the resulting loose bound must not be allowed to certify localization merely because the code ignores `q`.
2. Artificially inflate `B_ext` to exceed `J` in a fixture; the classifier must return inconclusive for that fixture.
3. P0 must not enter the terminal classifier.

## Frozen path predicate

A NEW path is `COMPACT_LOCAL_DIVERGENCE_CERTIFIED` iff for all `k=5,6,7,8`:

- `L_k > 0`;
- `B_ext(k)/J_k <= 1e-20`;

and for each transition `5->6`, `6->7`, `7->8`:

`L_{k+1}/U_k > 4`.

The factor `4` is the exact growth threshold corresponding to the parent `g>=2` criterion.

Otherwise that path is `COMPACT_LOCALIZATION_INCONCLUSIVE`.

## Terminal classifications

### `AUX_GAUSSIAN_UNRENORMALIZED_COMPACT_LOCAL_DIVERGENCE_SCOPED`

iff all controls pass and all three NEW paths P1-P3 are `COMPACT_LOCAL_DIVERGENCE_CERTIFIED`.

### `AUX_GAUSSIAN_COMPACT_LOCALIZATION_PARTIAL_SCOPED`

iff all controls pass and one or two NEW paths certify.

### `AUX_GAUSSIAN_COMPACT_LOCALIZATION_INCONCLUSIVE`

iff controls pass and no NEW path certifies.

### `INVALID_IMPLEMENTATION`

for failed source lock, parent-value drift, altered paths/grid/bounds, failed controls, or use of P0 as deciding evidence.

## Interpretation ceiling

A PASS upgrades the parent statement only from a Schwartz-test diagnostic to a **local compact-support diagnostic** for the same unrenormalized Gaussian auxiliary regulator family at the aligned highest-contact witness. It still does not prove distributional nonexistence of published Eq. (4), does not exclude renormalized extensions, and does not select or reject collision-supported counterterms.

Existing Critic-confirmed collision-supported homogeneous ambiguity remains a separate uniqueness limitation conditional on base-extension existence.

Governance remains unchanged: `RQIR Core v1.0` frozen; D7-S2/S3 not closed; D7-S4 partial; terminal selectors forbidden; Candidate Gravity inactive; KMQGB downstream of pinned DSIR authority.

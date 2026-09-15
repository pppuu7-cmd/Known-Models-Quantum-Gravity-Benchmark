# Terminal result — source j=1 K5 joint Feynman regulator extension

Date: 2026-09-15
Status: `TERMINAL_SCOPED`
Classification: `JOINT_FEYNMAN_EXTENSION_AUTHORITY_BLOCKED_SCOPED`

## Frozen authority

Parent preregistration:

- `research/prereg/SOURCE_J1_K5_JOINT_FEYNMAN_REGULATOR_EXTENSION_2026-09-15.md`
- prereg commit `9b0e6fe35f04cfcf7af26a336b7fa4c3c56d994b`

Outcome-blind authority protocol:

- `research/prereg/SOURCE_J1_K5_JOINT_FEYNMAN_REGULATOR_PROTOCOL_SUPPLEMENT_2026-09-15.md`
- protocol commit `1c63a14be6326d3541df4c180d1ac6720409e21a`

Frozen primary sources:

1. Bianchi, Chen, Gamonal, `Toller matrices and the Feynman i epsilon in spinfoams`, arXiv:2604.24945v1.
2. Bianchi, Chen, Gamonal, `Causal spinfoam vertex for 4d Lorentzian quantum gravity`, arXiv:2601.23162v1.

## Predicate audit

### A. One-wedge spectral projector — arXiv:2604.24945v1

- `epsilon_location_is_spectral_rho = true`
  - Eq. (17) places finite positive epsilon in the Cauchy denominator in the spectral integration variable `tilde rho`.
- `one_wedge_limit_defined = true`
  - Eq. (19)-(20) defines each reduced Toller branch as the `epsilon -> 0+` limit of that spectral projector acting on a reduced Wigner matrix.
- `one_wedge_uniqueness_claimed_under_source_conditions = true`
  - the uniqueness argument immediately after Eq. (20) derives the admissible Toller splitting from the same projector under the stated pole/asymptotic/sum-rule assumptions.
- `group_collision_regularization_explicit = false`
  - the frozen construction is a projector in the spectral representation variable; it does not state that epsilon regularizes the singular K5 Lorentz-group collision coordinates or supplies a distributional extension across that group-space collision locus.

### B. K5 causal vertex — arXiv:2601.23162v1

- `vertex_has_ten_wedge_product = true`
  - Eq. (4) defines the fixed-causal vertex as the gauge-fixed Lorentz-group integral of the product over the ten K5 wedges of Toller matrices.
- `vertex_finite_eps_inside_group_integral_explicit = false`
  - Eq. (3) gives the one-wedge Toller matrix through its spectral limiting prescription; Eq. (4) uses the resulting Toller matrices and does not define the ten-wedge group integral at a finite vector `(epsilon_1,...,epsilon_10)`.
- `joint_eps_removal_order_explicit = false`
  - no common-versus-independent ten-regulator removal order relative to the K5 group integrations is specified in the frozen source construction.
- `joint_path_independence_proved = false`
  - the one-wedge branch uniqueness argument is not a theorem that ten correlated spectral limits and Lorentz-group integrations are path/order independent through the full collision.
- `collision_extension_prescription_explicit = false`
  - no explicit distributional extension prescription across the K5 group-collision locus is supplied by these frozen source equations.

## Controls

- Positive one-wedge projector control: PASS.
- Spectral-vs-group-regulator adversarial guard: PASS; spectral epsilon was not promoted to a group-collision regulator.
- Already-defined-Toller vertex guard: PASS; Eq. (4) was not promoted to a finite-ten-epsilon definition.
- Additive identity guard: PASS; `T+ + T- = D` was not promoted to existence of a ten-fold singular product.
- Representation-transfer guard: PASS; neither `Q=diag(1,-2,1)` nor `11/24` nor an unpinned coherent-to-magnetic map was used.

## Frozen decision

The preregistered BLOCKED condition is satisfied: the one-wedge spectral Feynman projector is source-authoritative and unique in its stated class, and the causal K5 vertex uses ten Toller factors, but the frozen source authority does not specify the exact finite-regulator correlated K5 collision object or prove common/independent regulator path/order independence.

Therefore the terminal classification is:

`JOINT_FEYNMAN_EXTENSION_AUTHORITY_BLOCKED_SCOPED`

## Scientific consequence

This materially narrows the problem. The missing ingredient is not another numerical estimate of one-wedge Toller matrices. It is a mathematical bridge from the source-authorized **spectral branch projector** to a source-authorized or separately hypothesized **joint distributional extension through the correlated K5 group collision**.

The next admissible research directions are:

1. locate a primary theorem/source that explicitly supplies this joint extension / exchange-of-limits authority; or
2. prospectively register a new mathematical extension hypothesis (for example a specific common-regulator pushforward / Epstein-Glaser-like extension / microlocal construction), clearly marked as KMQGB-derived and not source-implied, and then test existence, covariance, identities and path dependence adversarially.

Re-running one-wedge Feynman projectors or adding one epsilon per wedge by intuition is not authorized.

## Claim ceiling

This result does not show that the causal spinfoam vertex fails, that the correlated product does not exist, or that a new QG model is required. It says only that the frozen primary source does not justify interpreting its one-wedge spectral `i epsilon` projector as a canonical joint K5 collision-extension prescription.

Governance remains:

- `RQIR Core v1.0 = FROZEN`;
- `D7-S2 = NOT_CLOSED`;
- `D7-S3 = NOT_CLOSED`;
- `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`;
- terminal D7 selectors remain forbidden;
- Candidate Gravity remains inactive;
- KMQGB remains downstream of pinned DSIR authority.

Independent Iter504 run `34907349374` and Iter461 run `34748503239` must still be consumed only when terminal; partial substantive values remain non-evidence.

# Protocol supplement — source j=1 K5 joint Feynman regulator extension

Date: 2026-09-15
Parent gate: `SOURCE_J1_K5_JOINT_FEYNMAN_REGULATOR_EXTENSION_GATE`
Status: `FROZEN_BEFORE_TERMINAL_CLASSIFICATION`

Parent prereg commit: `9b0e6fe35f04cfcf7af26a336b7fa4c3c56d994b`

## Purpose

Before any expensive ten-wedge regulator computation, determine whether the frozen primary source actually supplies a **joint collision regulator prescription** or only a **one-wedge spectral branch projector**. This authority question is logically prior to numerical path-comparison: an invented lifting from one-wedge spectral `i epsilon` to a ten-wedge K5 collision regulator would add model/prescription data and is forbidden in the parent gate.

## Frozen primary-source predicates

The authority audit must answer the following from the frozen versions only.

### A. One-wedge spectral projector

For arXiv:2604.24945v1:

1. `epsilon_location_is_spectral_rho`: whether the finite `epsilon` appears in the Cauchy denominator in the integration variable `tilde rho` used to project a reduced Wigner matrix onto a Toller branch.
2. `one_wedge_limit_defined`: whether the source takes `epsilon -> 0+` to define each Toller branch.
3. `one_wedge_uniqueness_claimed_under_source_conditions`: whether the source proves uniqueness of that splitting under its analytic/asymptotic/pole assumptions.
4. `group_collision_regularization_explicit`: true only if the source explicitly states that this same epsilon regularizes singular support in the Lorentz-group collision variables (rapidity/group coordinates), rather than merely selecting spectral branches.

### B. K5 causal vertex

For arXiv:2601.23162v1:

1. `vertex_has_ten_wedge_product`: whether the fixed causal vertex is a Lorentz-group integral containing one Toller matrix for each of the ten K5 wedges.
2. `vertex_finite_eps_inside_group_integral_explicit`: true only if the source explicitly defines the causal vertex at finite positive wedge regulators before taking regulator limits.
3. `joint_eps_removal_order_explicit`: true only if the source specifies common versus independent wedge regulators and the order relative to group integration.
4. `joint_path_independence_proved`: true only if the source proves equality of the admissible common/independent/order limits through the correlated K5 collision.
5. `collision_extension_prescription_explicit`: true only if a distributional extension across the group-collision singular locus is explicitly defined by the source.

## Frozen decision rule

Classify the parent gate immediately as

`JOINT_FEYNMAN_EXTENSION_AUTHORITY_BLOCKED_SCOPED`

iff all of the following are true:

- A1-A3 are true;
- B1 is true;
- at least one of A4, B2, B3, B4, B5 is false in a way that prevents construction of the exact ten-wedge regulated collision object without adding a new prescription.

This BLOCKED classification is authority/definition scoped. It is **not** evidence that the joint distribution does not exist or that the causal vertex fails physically.

Do not classify scientific path-dependence FAIL unless the source-authorized joint finite-regulator object is first available and two prospectively frozen admissible paths are actually evaluated on the same frozen test function.

## Positive control

The audit must recognize Eq. (17)-(20) of arXiv:2604.24945v1 as a valid one-wedge spectral `i epsilon` projector and must recognize the one-wedge uniqueness argument following Eq. (20).

## Negative/adversarial controls

1. A formula containing `epsilon` only in the spectral `tilde rho` Cauchy kernel must **not** set `group_collision_regularization_explicit=true`.
2. A vertex written as an integral of already-defined Toller matrices must **not** by itself set `vertex_finite_eps_inside_group_integral_explicit=true`.
3. `T+ + T- = D` must not be promoted to a statement about existence of a product of ten singular boundary values.
4. The source calling the vertex an amplitude must not be promoted to a proof of local absolute integrability or a unique distributional collision extension.
5. No natural-looking prescription such as assigning one epsilon per wedge may be inserted unless explicitly source-authorized or separately preregistered as a new model/prescription hypothesis.

## Evidence to record

The terminal audit must record equation/section identifiers sufficient to reproduce each predicate and distinguish direct source statements from KMQGB inference. No moving-web content or later source revision may silently replace the frozen versions.

## Claim ceiling

A BLOCKED result means only that the frozen primary source does not furnish enough authority to treat its one-wedge spectral projector as a joint K5 collision extension. It does not invalidate the one-wedge Toller construction, the causal vertex proposal, or the possibility that a mathematically canonical joint extension exists by an additional theorem.

# KMQGB Current Benchmark Front

**Updated:** 2026-09-08  
**KMQGB iteration:** 036  
**Repository:** `pppuu7-cmd/Known-Models-Quantum-Gravity-Benchmark`  
**Branch:** `main`  
**Phase:** WAVES 1–13 TERMINALLY CLASSIFIED / PREDICTIVE RIGIDITY FROZEN / MINIMAL DISCRIMINATING TEST-SUITE NEXT

## Coverage

- Wave 1: **9/9 = 100%** — immutable.
- Waves 2–13: **each 5/5 = 100%** — immutable.
- Globally authorized robust unique-QG residuals: **0**.
- KMQGB-promoted Candidate Gravity ansatz: **none**.
- External Candidate Gravity readiness: **24%**.

## Permanent Candidate Gravity construction protocols

1. `protocol/CANDIDATE_GRAVITY_DESIGN_PRIORS.md`;
2. `protocol/CANDIDATE_GRAVITY_PROMOTION_GATE.md`;
3. `protocol/PARENT_KERNEL_RESPONSE_COMPLETENESS.md`;
4. `protocol/RESIDUAL_SPACE_GEOMETRY.md`;
5. `protocol/OPTIMAL_COMPARATOR_CONTRASTS.md`;
6. `protocol/CROSS_ORDER_RIGIDITY.md`;
7. `protocol/INTERVENTION_CONFIGURATION_RIGIDITY.md`;
8. `protocol/PREDICTIVE_HOLDOUT_RIGIDITY.md`.

Reference code:

- `code/inverse_kernel_ordered_partitions.py`;
- `code/residual_space_geometry_reference.py`;
- `code/optimal_comparator_contrasts_reference.py`;
- `code/cross_order_rigidity_reference.py`;
- `code/intervention_design_reference.py`;
- `code/predictive_holdout_reference.py`.

## Wave 12 — intervention rigidity

Terminal `5/5`, methodology PASS.

Known configuration controls are design variables, not free nuisance. Shared dynamics parameters remain shared across configurations. New configurations are chosen to increase post-comparator rank/conditioning/SNR rather than raw signal amplitude.

## Wave 13 — predictive/holdout rigidity

Terminal `5/5`, methodology PASS.

Prospectively split complete physical blocks into training `T` and holdout `H`.

Fit shared parent parameters only on `T`, then predict `H` without shared-parameter retuning:

`r_H^pred = y_H - c_H(theta_hat_T)`.

For the exact correlated linear-Gaussian reference,

`M=(J_T^T Sigma_TT^(-1)J_T)^+ J_T^T Sigma_TT^(-1)`

and

`Sigma_pred,H = Sigma_HH + J_H M Sigma_TT M^T J_H^T - J_H M Sigma_TH - Sigma_HT M^T J_H^T`.

This correctly retains training/holdout correlated noise/systematics.

Leave-one-configuration/order-out validation is frozen as a rigidity diagnostic. A holdout test is only sharp if training data actually constrain the shared parameters.

## Candidate Gravity design target

The strongest current architecture is:

- few shared parent parameters/functions;
- complete same-parent responses across several orders;
- multiple controlled configurations/interventions;
- exact Ward/contact/relational completion;
- nonzero comparator-orthogonal residual;
- global comparator separation;
- robust projected singular directions;
- successful prediction of held-out orders/configurations without retuning.

This is the current meaning of **rigidity by overconstraint** for future KG.

## External RQIR read-only authority

Latest directly observed scientific authority remains **Iteration 590**, `MODEL_READINESS=24%`.

Iter590 proves cubic MSSC source response requires local K3, six K1/K2 placements and six ordered K1^3 chains; K3/K1^3 have nonzero support.

Exact external next gate remains K3 hard-channel origin classification plus K1^3 linked-cut/origin classification before complete nonlinear source Ward closure and comparator subtraction.

KMQGB external pre-check `external_rqir_checks/iter590_k3_local_analyticity_precheck.md` argues the isolated local K3 coefficient should have zero standalone branch discontinuity, but this is not RQIR authority and does not classify the larger composite response.

## Candidate Gravity promotion gate

No ansatz is promoted before

`one parent dynamics -> complete response -> exact physical constraints -> common-domain comparator definition -> attribution stack -> full C5 quotient -> nonzero COR -> global separation -> projected identifiability -> cross-order/intervention/holdout rigidity`.

Only then may model-level readiness and later Fisher/resources advance.

## Exact next KMQGB front — minimal discriminating test suite

The next useful methodology problem is to choose the **smallest pre-registered set of orders/configurations/contrasts** that retains a target comparator-orthogonal rank and predictive rigidity.

Goals:

1. define a library of candidate observable/configuration blocks with cost/complexity metadata;
2. quantify incremental `Delta d_perp` and projected singular-value gain for each block;
3. construct minimal or near-minimal test suites under cost/resource ceilings;
4. require leave-one-block robustness so the claimed residual is not carried by one fragile observable;
5. separate this relative design-cost optimization from final Fisher/resource promotion, which remains forbidden until a real residual exists.

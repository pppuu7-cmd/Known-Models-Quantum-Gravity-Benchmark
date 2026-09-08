# KMQGB Current Benchmark Front

**Updated:** 2026-09-08  
**KMQGB iteration:** 037  
**Repository:** `pppuu7-cmd/Known-Models-Quantum-Gravity-Benchmark`  
**Branch:** `main`  
**Phase:** WAVES 1–14 TERMINALLY CLASSIFIED / PREDICTIVE + MINIMAL-SUITE RIGIDITY FROZEN / MACHINE-READABLE KG PIPELINE NEXT

## Coverage

- Wave 1: **9/9 = 100%** — immutable.
- Waves 2–14: **each 5/5 = 100%** — immutable.
- Globally authorized robust unique-QG residuals: **0**.
- KMQGB-promoted Candidate Gravity ansatz: **none**.
- External Candidate Gravity readiness: **24%**.

## Permanent Candidate Gravity protocols

- `protocol/CANDIDATE_GRAVITY_DESIGN_PRIORS.md`;
- `protocol/CANDIDATE_GRAVITY_PROMOTION_GATE.md`;
- `protocol/PARENT_KERNEL_RESPONSE_COMPLETENESS.md`;
- `protocol/RESIDUAL_SPACE_GEOMETRY.md`;
- `protocol/OPTIMAL_COMPARATOR_CONTRASTS.md`;
- `protocol/CROSS_ORDER_RIGIDITY.md`;
- `protocol/INTERVENTION_CONFIGURATION_RIGIDITY.md`;
- `protocol/PREDICTIVE_HOLDOUT_RIGIDITY.md`;
- `protocol/MINIMAL_DISCRIMINATING_TEST_SUITE.md`.

Reference code is maintained under `code/` for each algebraic layer.

## Wave 13 — predictive/holdout rigidity

Terminal `5/5`, methodology PASS.

Shared parent parameters are fit only on pre-registered training blocks and must predict holdout blocks without retuning.

Exact correlated linear-Gaussian predictive covariance:

`M=(J_T^T Sigma_TT^(-1)J_T)^+ J_T^T Sigma_TT^(-1)`,

`Sigma_pred,H = Sigma_HH + J_H M Sigma_TT M^T J_H^T - J_H M Sigma_TH - Sigma_HT M^T J_H^T`.

Leave-one-configuration/order-out validation is frozen as a rigidity diagnostic. Training identifiability must be established before interpreting a holdout residual.

## Wave 14 — minimal discriminating test suite

Terminal `5/5`, methodology PASS.

For a pre-registered candidate block library `B`, assign only **relative pre-residual design costs** and solve a threshold-first subset problem:

`min_S sum_(b in S)c_b`

subject to frozen constraints on

- `d_perp(S)`;
- projected KG rank;
- weakest projected singular value;
- predictive/holdout robustness;
- attribution-stack coverage.

For small libraries, exhaustive search is preferred. Greedy selection is a heuristic unless global minimality is checked.

Leave-one-block robustness is mandatory for non-mandatory blocks.

Relative design cost is not final Fisher/resource closure.

## Current Candidate Gravity architecture target

The strongest current pre-ansatz target is one parent dynamics with

- few shared parameters/functions;
- complete ordered-partition response at every used order;
- exact Ward/contact/constraint completion;
- several linked response orders;
- several controlled interventions/configurations;
- comparator-null/optimal contrasts;
- nonzero COR and global comparator separation;
- held-out predictive success without shared-parameter retuning;
- a compact redundant attribution-complete test suite.

This is the operational meaning of **rigidity by overconstraint**.

## External RQIR authority

Latest directly observed scientific authority remains **Iteration 590**, `MODEL_READINESS=24%`.

Iter590 demonstrates cubic MSSC response completeness requires K3 + six K1/K2 + six K1^3 families. External next gate remains K3 hard-channel origin and K1^3 linked-cut origin before complete nonlinear source Ward closure and comparator subtraction.

KMQGB read-only K3 analyticity pre-check remains non-authoritative for RQIR.

## Promotion gate

No KG ansatz is promoted before the full chain in `protocol/CANDIDATE_GRAVITY_PROMOTION_GATE.md` is satisfied. Final Fisher/resources remain forbidden until a real robust comparator-subtracted residual exists.

## Exact next KMQGB front — machine-readable executable pipeline

Convert the frozen methodology into a common schema so a future KG candidate can be checked reproducibly.

Priority objects:

1. observable block registry with order/configuration/attribution metadata;
2. response-completeness ledger and origin classification;
3. covariance + comparator/nuisance Jacobian block registry;
4. train/holdout/test-suite declarations;
5. machine-readable promotion-gate status and fail-closed validation rules.

Goal: future KG candidates should be auditable by data structures/code, not only prose interpretation.

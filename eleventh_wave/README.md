# KMQGB Eleventh Wave — Cross-Order Rigidity

**Frozen denominator:** 5 methodology targets.  
**Historical waves 1–10:** terminal and immutable.  
**Status:** **TERMINAL 5/5 = 100%**.  
**Purpose:** exploit shared parent parameters across response orders/channels to create comparator-orthogonal consistency directions that are invisible in isolated single-order fits.

| # | Target | Terminal result | State |
|---|---|---|---|
| T11-01 | stacked multi-order observable | freeze block-stacked observable/covariance/Jacobian notation | `PASS_RQIR_GATE` |
| T11-02 | shared-parent parameter incidence | forbid artificial independent per-order retuning of physically shared parameters | `PASS_RQIR_GATE` |
| T11-03 | cross-order null/invariant construction | derive local null contrasts and exact global monomial invariants when scaling permits | `PASS_RQIR_GATE` |
| T11-04 | cross-order covariance/systematics | retain full block covariance and separate stochastic from deterministic shared nuisance | `PASS_RQIR_GATE` |
| T11-05 | cross-order rigidity certificate | freeze shared-parameter rank gain and projected singular-value criterion | `PASS_RQIR_GATE` |

**Eleventh-wave terminal coverage: 5/5 = 100%.**

## Authoritative protocol

`protocol/CROSS_ORDER_RIGIDITY.md`

Reference code:

`code/cross_order_rigidity_reference.py`

## Central rank result

For blocks `ell` with physical dimensions `m_ell` and comparator Jacobians `J_ell`, the correct shared-parent stack is

`J_stack = vertical_stack(J_1,...,J_L)`

using one column for each genuinely shared parameter.

Then

`d_perp,stack = m_total - rank(J_stack)`.

Relative to analyzing orders separately, the extra comparator-orthogonal dimension is

`R_shared = sum_ell rank(J_ell) - rank(J_stack) >= 0`.

`R_shared>0` is a quantitative rigidity benefit of shared parent parameters.

## Exact global invariant example

If a comparator predicts

`c1=a f1`,

`c2=a^2 f2`,

then

`I = c2 f1^2/(c1^2 f2)=1`

is exactly independent of the shared amplitude `a`.

More generally, for

`c_i=A_i product_j theta_j^(P_ij)`,

any `u` with `u^T P=0` yields the exact multiplicative invariant

`I_u=product_i(c_i/A_i)^(u_i)`.

Such exact cross-order invariants are stronger than a local tangent quotient when their scaling assumptions and branch/sign domain are valid.

## Candidate Gravity design lesson

The strongest pre-ansatz direction is now:

> **few shared parent parameters predicting many linked response orders/channels.**

A future KG model should not introduce a fresh independent coefficient for every new observable. It should seek cross-order/cross-attribution relations where the physical data dimension grows faster than the comparator nuisance rank.

## Mandatory guardrails

- every order must first pass parent-response completeness;
- exact Ward/contact/physical reduction is performed before stacking;
- shared parameters remain shared unless the parent theory says otherwise;
- genuinely order-specific detector/calibration nuisances remain independent;
- full cross-order covariance is retained;
- global/nonlinear comparator profiling remains mandatory after local projected-rank gains.

## Promotion guardrail

This wave is methodology only. No Candidate Gravity ansatz/readiness increase is authorized.

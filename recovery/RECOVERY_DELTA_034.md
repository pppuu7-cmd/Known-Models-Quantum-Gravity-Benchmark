# RECOVERY DELTA 034 — Cross-Order Rigidity

Date: 2026-09-08  
KMQGB iteration: 034

## New authority

Wave 11 terminally closed `5/5 = 100%`.

Created:

- `protocol/CROSS_ORDER_RIGIDITY.md`;
- `code/cross_order_rigidity_reference.py`;
- `eleventh_wave/result.json`.

## Frozen rank result

For response-order blocks with shared parent parameters:

`R_shared = sum_ell rank(J_ell) - rank(J_stack) >= 0`.

`R_shared>0` is extra comparator-orthogonal consistency information that disappears if shared parameters are incorrectly allowed to retune independently per order.

## Exact invariant result

For monomial scaling

`c_i=A_i product_j theta_j^(P_ij)`,

any `u` satisfying `u^T P=0` yields the exact nuisance-free invariant

`I_u=product_i(c_i/A_i)^(u_i)`.

## Candidate Gravity lesson

Prefer few shared parent parameters predicting many linked response orders/channels. Do not add a fresh independent coefficient for every claimed effect.

Main Candidate Gravity design-prior ledger was consolidated through this result.

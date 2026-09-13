# Iter464 — source P11*d_source distributional pairing

Date: 2026-09-13

## Frozen gate
`ITER464_SOURCE_P11_D_EXACT_EXPONENTIAL_POLYNOMIAL_DISTRIBUTIONAL_PAIRING`

Preregistration: `599f49a76df6e745724cdc1fa06010e5442ca4af`
Implementation: `06774a643170161ba873721f4c93d597a55d7af7`
Production head: `933da7cf5cfeac82b643b2ab457d744670a6dcc1`
Authoritative run: `34750582787`
Aggregate job: `103706358448`
Aggregate artifact: `10316110295`
Artifact digest: `sha256:d628fbf9cf259cb6522d6d73d12d5e7a3ab3fd2c2d5c242be9cb35f2f559585d`

## Raw terminal result
- 6/6 independent matrix lanes PASS.
- 24/24 `(m,beta,rho,boundary-sign)` records PASS.
- Exact/high-precision `P11/(x+x^3)` denominator cancellation error is ~1e-81.
- Direct source reconstruction versus exponential-polynomial channels is ~1e-79 or better.
- Plemelj boundary value equals the independently evaluated Fourier selector exactly at the recorded precision in all records.
- Finite-epsilon errors decrease monotonically over the last three frozen epsilon values in all records and satisfy the frozen terminal tolerance.
- Wrong-boundary-sign controls remain separated.

## Scientific classification
`ITER464_SOURCE_P11_D_DISTRIBUTIONAL_PAIRING_QUALIFIED_SCOPED`

This is a scoped qualification of the exact one-dimensional source-specific spectral pairing for the published Feynman denominator. It does **not** prove full causal-vertex convergence, absolute integrability, a multivariable distributional pullback, or order independence. D7-S2 therefore remains `NOT_CLOSED`.

## Claim guards
No physical causal-vertex finiteness/divergence theorem. No universal contour theorem. No fitted subtraction, damping, or replacement of the published spectral i-epsilon. Conditional/PV/distributional boundary values remain distinct from absolute integrability.

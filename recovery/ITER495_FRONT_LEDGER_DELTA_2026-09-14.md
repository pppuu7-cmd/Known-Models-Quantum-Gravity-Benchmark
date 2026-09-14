# Iter495 Front / Decision-Ledger Delta

Date: 2026-09-14

## Closed evidence
Authoritative Iter495 run `34804409129` is terminal and valid. Aggregate artifact `10333052075` (`sha256:6d0cf4c19a3735d4509772ab43e246ab58da3d408534cbd09578348e3ed44a77`) classifies `ITER495_MULTIVARIATE_TAYLOR_STRESS_QUALIFIED_SCOPED` with 12/12 valid jobs.

The measured full-quadratic remainder is not uniformly cubic across the prospectively frozen simultaneous directions. Max absolute remainder is `2.1820206151890176e-4`, max `|r|/a^3` is `4069.3407635785657`, and the small/large remainder ratio has median `0.22654674656585128`, max `9.533261802575108`, versus cubic expectation `0.125`.

## Decision
Do not advance directly to an interval/uniform quadratic certificate and do not weaken thresholds. The next scientific ambiguity is whether the non-cubic remainder is dominated by finite-difference coefficient-stencil error or by genuine higher-order/nonlocal angular structure.

## Authorized next gate
Iter496 `COEFFICIENT_STENCIL_CONVERGENCE` is authorized and prospectively frozen at commit `fb9b2a5f8ed3dc24beba31e6e55fdf3f60692898`, with evaluator `4351165495050e533bd812b30dbcd31276c15634`, aggregate `c277968c65ddd2587250ce8b859cad6409cbd579`, production head `1098eb1f8a8ceac78013e8c85194bad61d43cf6a`, run `34807803061`.

Frozen h levels: `0.0050, 0.0025, 0.00125`; second-order Richardson from the two finest levels; targets `a=0.00125,0.0025`; same chart, directions, q=1, causal classes and rho witnesses as Iter495. Matrix 12 jobs, `fail-fast:false`, `max-parallel:12`.

## Locks retained
D7-S2 `NOT_CLOSED`; D7-S3 `NOT_CLOSED`; D7-S4 `PARTIAL_GLOBAL_NOT_CLOSED`. Terminal D7 classifier and `EXISTING_SUFFICIENT`, `ADAPT_EXISTING`, `HYBRID_REQUIRED`, `NEW_REQUIRED` remain forbidden. Candidate Gravity remains inactive.

## Progress rubric
`D2 82% -> D4 68% -> D7 63% -> integrated 74%`; no credit is added for Iter495 because it exposes a new scientific blocker rather than closing it, and no credit is added for launching Iter496 before terminal evidence.
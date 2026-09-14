# Iter496 — Coefficient-stencil convergence / Richardson diagnostic

Date: 2026-09-14

## Authority
- Prereg: `fb9b2a5f8ed3dc24beba31e6e55fdf3f60692898`
- Evaluator: `4351165495050e533bd812b30dbcd31276c15634`
- Aggregate implementation: `c277968c65ddd2587250ce8b859cad6409cbd579`
- Production head: `1098eb1f8a8ceac78013e8c85194bad61d43cf6a`
- Workflow run: `34807803061`
- Aggregate artifact: `10333948552`
- Aggregate digest: `sha256:3d8f62cc56d51ae0045c6a8ad30a1655713e1b18fda7caed6420b784bb68d274`

All 12 scientific lane artifacts were consumed. Each lane is `ITER496_LANE_VALID`; total frozen states = 240; missing/invalid jobs = 0. Source and high-precision controls remain valid.

## Terminal scoped classification
`ITER496_COEFFICIENT_STENCIL_CONVERGENCE_QUALIFIED_SCOPED`

## Frozen findings
Coefficient stencils were `h={0.0050,0.0025,0.00125}` with second-order Richardson extrapolation from the two finest stencils. Target amplitudes were `{0.00125,0.0025}`.

- Richardson improves the target remainder in `0.916666666666667` of frozen states (220/240).
- Median small/large Richardson remainder scaling is `0.125010164300838`, essentially the cubic expectation `1/8`.
- Maximum observed Richardson scaling ratio is `0.193858822037374`; therefore scaling is not yet uniform.
- Maximum Richardson absolute remainder is `1.92495030925155e-6`; median is `1.03908209858661e-7`.
- Maximum Richardson cubic-normalized remainder is `112.621961946326`; median is `13.8283405965097`, so a validated uniform Taylor enclosure is not yet established.
- The worst frozen target (`2to3`, block 0, rho=2.7, direction `[1,1,1,-1,-1,-1]`, sign `+`, amplitude `0.0025`) improves from `2.08029730732611e-4` at the original stencil to `1.75971898034259e-6` after Richardson.
- Largest h-mid to h-fine coefficient change is `0.192565945056137`, for `Q11`, causal class `1to4`, rho `0.15`; this is a nonuniform coefficient-convergence outlier that must be enclosed rather than ignored.
- Maximum HP reconstruction error is `7.384428036634117e-96`; maximum source-object identity relative residual is `3.03567429866262e-15`.

## Interpretation
Iter496 materially resolves the Iter495 ambiguity: finite-difference coefficient truncation accounts for most of the previously non-cubic stress remainder, and Richardson recovery restores near-cubic median scaling. However rare nonuniform coefficient/remainder outliers remain. Therefore Iter496 authorizes a prospectively frozen validated coefficient/remainder enclosure gate; it does **not** authorize D7-S2 closure, a positive-measure theorem, a Haar convergence/divergence theorem, or any terminal D7 classifier.

Candidate Gravity remains inactive. `EXISTING_SUFFICIENT`, `ADAPT_EXISTING`, `HYBRID_REQUIRED`, and `NEW_REQUIRED` remain forbidden while D7-S2/S3/S4 remain open.

# Iter480 preregistration — INVALIDATED BEFORE IMPLEMENTATION/PRODUCTION

Date: 2026-09-13
Original prereg commit: `9e1eb674e4c05e1cb3dcea1d01104d29e7cf29fa`

## Classification
`INVALID_PREREG_DIMENSIONAL_THRESHOLD_PREPRODUCTION`

No implementation commit, GitHub Actions production run, artifact, or scientific classification exists for Iter480.

## First causal defect
Frozen check C used
`|A| > 1e-12 * max(1, product_e max_m |C_e(m)|)`.
The intended scientific question is whether the intertwiner contraction is identically/structurally zero relative to its own leading-coefficient scale. The `max(1, ...)` floor mixes that scale with an arbitrary dimensionful absolute unit whenever the product of source coefficients is below unity. Therefore the preregistered predicate does not faithfully test the stated universal-cancellation question.

This was detected during pre-production implementation design/dry-run, before any authoritative GitHub Actions result was launched. The gate is withdrawn, not reclassified as PASS/FAIL. No D7 readiness credit is assigned.

## Integrity rule
Do not edit or reuse Iter480. A replacement gate, if opened, must have a new identifier and freeze a dimensionless ratio before its implementation/production. The replacement threshold must not be fitted to a desired outcome.

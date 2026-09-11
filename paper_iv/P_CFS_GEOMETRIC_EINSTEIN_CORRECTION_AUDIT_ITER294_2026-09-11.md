# Iter294 — CFS geometric Lorentzian Einstein / correction-hierarchy audit

## Authority
Felix Finster and Christoph Krpoun, *A Geometric Derivation of the Einstein Equations from the Causal Action Principle*, arXiv:2607.13871v1 (2026). Public preprint authority in the Iter294 audit.

## Source-level result
Theorem 6.8 gives the Lorentzian Einstein equations in the four-dimensional setting with an explicit energy-momentum tensor. The tensor is symmetric and divergence-free and scales as `O(delta^2)` for small regularization length. The paper also presents a systematic route to corrections, including higher-order-in-`delta` Planck-scale terms, osculation/torsion effects, regularizing-vector-field effects, and modified-measure effects.

The source explicitly states that these correction classes still need to be worked out in detail. Therefore the paper upgrades the CFS Einstein endpoint and correction pathway but does not provide the frozen concrete normalized beyond-Einstein correction residual/comparator object.

## Frozen machine audit
- Scientific run: `34585821754` on head `9d821ea02aae8a85c093cec27ecffb120250d6b7`.
- Four independent guards ran in parallel with `fail-fast:false`: Lorentzian Einstein endpoint, conservation/scaling, correction maturity, and frozen-blocker compatibility.
- Aggregate ran only after the dependency barrier.
- Methodology run: `34585821764` = SUCCESS.
- Summary artifact: `10193537053`.
- Artifact digest: `sha256:996064f831648b6f2a5e788b3e8f63f20f7a0213a13422d65d085676cd61439b`.
- Raw summary digest: `sha256:89a2f8b287d637b7d2ae664bfe84d4abd0e27b254d99adf5c353c72677343902`.

## Classification
`HIGH_VALUE_CFS_GEOMETRIC_LORENTZIAN_EINSTEIN_DERIVATION_AND_SYSTEMATIC_CORRECTION_HIERARCHY__CONCRETE_NORMALIZED_BEYOND_EINSTEIN_RESIDUAL_COMPARATOR_STILL_MISSING`

## Fail-closed boundary
CFS remains `BLOCKED_MISSING_REQUIRED_OBJECT`, not FAIL and not family-level PASS. The required next object is a concrete causal-action-derived beyond-Einstein gravity correction tensor/observable with fixed state/regularization, normalized same-domain comparator-orthogonal residual, and propagated uncertainty. D7 remains unauthorized.

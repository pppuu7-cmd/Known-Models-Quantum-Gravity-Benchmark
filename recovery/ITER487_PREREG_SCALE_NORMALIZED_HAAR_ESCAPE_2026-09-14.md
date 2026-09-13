# Iter487 preregistration — scale-normalized shared-node Haar escape

Date frozen: 2026-09-14
Status: FROZEN BEFORE IMPLEMENTATION/PRODUCTION

## Parent authority and reason for a new iteration
- Iter485 terminal full-network object: `ITER485_SHARED_NODE_TEN_EDGE_TOLLER_MAGNETIC_NETWORK_QUALIFIED_SCOPED`.
- Iter486 terminal classification: `INFRASTRUCTURE_OR_SOURCE_FAIL_ITER486`.
- Haar source snapshot: `sources/arxiv_2202_04360_sl2c_haar_cartan.json`.

Iter486 produced all 24 raw lanes, but the prospectively frozen **absolute** Toller nonrepresentation negative control became inactive in large-rapidity sectors because both sides of the comparison decay in absolute scale. The frozen Iter486 criteria are not changed. Iter487 is a new prospective gate whose sole methodological change is to make this validation control scale-invariant while preserving the exact Iter486 scientific object, escape family, source Haar measure, slope windows and DECAY/NONDECAY classifier.

## Scientific question
For the identical full Iter486 ten-edge shared-node/intertwiner Haar-escape object, does a stable post-Haar NONDECAY witness survive once the validation controls are made scale-robust, or do all valid escape profiles decay exponentially?

## Frozen scientific object — unchanged from Iter486
- `j=k=l=1`.
- `rho in {0.35,0.9,1.6,2.7}`.
- base panels `{A,C}`, strong regime only.
- node 0 identity.
- cluster sizes `s in {1,2,3,4}`, cluster `S_s={1,...,s}`.
- escape radii `R in {6,8,10,12}`.
- escaped nodes `g_a(R)=B_z(R) g_a^0` for `a in S_s`; other nodes unchanged.
- all ten edges `h_ab=g_b^{-1}g_a` from the same five nodes.
- causal patterns `{0to5,1to4,2to3}` with source branch signs.
- all 243 genuine `3^5` four-valent `j=1` intertwiner channels.
- 24 independent lanes = 2 panels x 4 cluster sizes x 3 causal patterns, `fail-fast:false`.

## Frozen Haar observables — unchanged from Iter486
Use the pinned source density `dg = const * sinh(r)^2 dr du dv`, omitting only the overall constant for slope diagnostics.

For each `(R,rho)`:
- `C_max(R,rho)=max_I |C_I|` over the 243 contracted channels;
- `log H(R)=sum_{a in S_s} 2 log sinh(eta_a(R))` using actual KAK rapidities of escaped nodes;
- `log E=log C_max + log H`;
- `network_slope`, `haar_slope`, `actual_slope` from fits on `R={8,10,12}`;
- slope drift = absolute difference between `log E` fits on `{6,8,10}` and `{8,10,12}`.

The exact numerical rescaling used by Iter486 is retained only to avoid overflow/underflow; it must reconstruct the same logarithmic contraction magnitude exactly and introduces no physical weight or regulator.

## Frozen controls A-F — unchanged
A. shared-node K5 cycle residual `<1e-8` at every R.
B. per-edge source KAK reconstruction residual `<1e-8` at every R.
C. all relevant observables finite and `C_max>0`.
D. `|haar_slope-2s| < 0.05` in every lane.
E. Haar bookkeeping `|(actual_slope-network_slope)-haar_slope| < 1e-8`.
F. at `R=10`, corrupt exactly one crossing edge independently of nodes; K5 cycle residual must exceed `1e-5`.

Retain the inherited intertwiner and source additive regressions used in Iter486.

## Frozen replacement for Iter486 control G
The scientific object is unchanged; only validation of the known Toller nonrepresentation property is made scale-invariant.

### G1 — escaped-scale relative nonrepresentation
At `R=10`, for the same frozen edge pair used in Iter486 and each frozen rho, compute

`q_rel = ||T+(g2 g1)-T+(g2)T+(g1)||_max / max(||T+(g2 g1)||_max, ||T+(g2)T+(g1)||_max, 1e-300)`.

Require all values finite and `max_rho q_rel > 1e-6` in every lane. The `1e-6` threshold is a prospective dimensionless numerical-separation threshold, not fitted to Iter486 raw values.

### G2 — undeformed-base absolute regression
On the corresponding undeformed Iter485 base nodes (same panel/strong regime, before applying the escape boost), compute the original absolute nonrepresentation mismatch on the same edge pair and rho panel. Require `max_rho > 1e-5` in every lane. This ensures the source nonrepresentation negative control remains independently active at a moderate scale.

A failure of A-G2 makes the lane invalid and prevents a scientific slope verdict.

## Frozen scientific classifier — exactly unchanged
For each valid `(lane,rho)`:
- **DECAY** iff `actual_slope <= -0.10` and slope drift `<=0.05`.
- **NONDECAY** iff `actual_slope >= 0.00` and slope drift `<=0.05`.
- otherwise `ASYMPTOTIC_INCONCLUSIVE`.

Aggregate:
1. `ITER487_HAAR_ESCAPE_ACTUAL_ENVELOPE_DECAY_QUALIFIED_SCOPED` iff all 24 lanes are valid and all 96 frozen `(lane,rho)` points are DECAY.
2. `SCIENTIFIC_FAIL_ITER487_HAAR_ESCAPE_ACTUAL_ENVELOPE` iff all 24 lanes are valid and at least one frozen point is a stable NONDECAY witness.
3. `INCONCLUSIVE_ITER487_HAAR_ESCAPE_ASYMPTOTIC` iff all lanes are valid, there is no NONDECAY witness, but not all points are DECAY.
4. `INFRASTRUCTURE_OR_SOURCE_FAIL_ITER487` iff any expected lane is missing/invalid or source/runtime/output controls fail.

## Interpretation ceiling
A valid stable NONDECAY witness proves only failure of this exponential absolute-envelope test along at least one prospectively fixed one-dimensional shared-node escape path. It is **not yet** an absolute Haar-divergence theorem because a path has zero angular measure. The next required gate after NONDECAY is positive-measure angular-neighborhood thickening around a frozen witness and a uniform lower-bound/stability test.

Even after a Haar absolute obstruction, ten source spectral integrations, possible conditional/PV cancellations and source-defined distributional boundary values remain separate. No physical causal-vertex divergence theorem, D7-S2 closure, terminal D7 label, or Candidate Gravity authorization is permitted by Iter487 alone.

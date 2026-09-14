# Iter501 preregistration — direct max-envelope interval science after Iter500

Date: 2026-09-14
Status: **FROZEN BEFORE IMPLEMENTATION / PRODUCTION**

## Purpose
Iter500 qualified the compact-sandwich/dependency-preserving KAK construction over the complete frozen Iter499 state space. Iter501 is the first fresh science gate allowed to use that construction to classify the continuous q=1 signed-direction max-envelope behavior. It must distinguish a numerical-method blocker from a scientific failure of the frozen NONDECAY hypothesis.

## Fixed authority inherited without post-hoc tuning
Use exactly the Iter499 source/science grid and thresholds unless stated below:
- causal classes: `0to5`, `1to4`, `2to3`;
- four frozen direction blocks from `iter499_arb_core.BLOCKS`;
- both signs for every direction;
- 16 amplitude subintervals covering the frozen q=1 amplitude range;
- point-regression amplitudes `0.00125, 0.00140625, 0.0015625, 0.00171875, 0.001875, 0.00203125, 0.0021875, 0.00234375, 0.00250`;
- rho witnesses from `iter499_arb_core.RHOS`;
- R grid `6,8,10,12`;
- all 243 intertwiner channels;
- drift tolerance `0.05`;
- ROBUST NONDECAY lower-slope floor `1.0`;
- NONDECAY lower-slope floor `0.0`;
- UNIFORM DECAY upper-slope ceiling `-0.10`;
- Arb/Acb precision 384 bits and `python-flint==0.9.0`.

## Mandatory Iter500 construction
For every interval box and R:
1. construct nodes and relatives with the exact Iter500 compact-sandwich/factorized method;
2. node `g_a=L_a (B G_a) R_a`: KAK only the fixed middle and restore compact factors;
3. `h_0b=R_b^{-1}(G_b^{-1}B^{-1})L_b^{-1}`: KAK only the fixed middle and restore compact factors;
4. internal `h_ab`: retain the dependency-preserving middle `G_b^{-1}B^{-1}L_b^{-1}L_a B G_a`, with outer compact factors stripped/restored;
5. require full interval reconstruction, SU(2), determinant and positive-beta predicates for every KAK object;
6. require source Toller additive identities and finite positive max-envelope bounds.

No fallback to the Iter499 generic interval-KAK path is allowed.

## Direct envelope and channel crossings
For each rho and R, compute every one of the 243 source-faithful contracted channel intervals and take a validated max-envelope bound over the full set. **No unique maximizing channel is assumed.** Multiple possible-max channels, including the Iter498 195→222 crossing region, are allowed and must remain in the enclosure.

Let `Y(R)=log Haar(R)+log max_channel |C_channel(R)|`. Define the late interval slope from R=8 to 12 and early interval slope from R=6 to 10 exactly as Iter499. The drift upper bound is the maximum separation between the early and late slope intervals.

Per rho/box classification is frozen:
- `INTERVAL_ROBUST_NONDECAY` iff late lower slope >= 1.0 and drift <= 0.05;
- `INTERVAL_NONDECAY` iff late lower slope >= 0.0 and drift <= 0.05;
- `INTERVAL_UNIFORM_DECAY_WITNESS` iff late upper slope <= -0.10 and drift <= 0.05;
- otherwise `INTERVAL_INCONCLUSIVE`.

## Frozen point containment regression
The nine source point evaluations must lie inside the corresponding interval late/early slope enclosures. A containment failure is a **numerical-method blocker**, not a scientific decay result.

## Terminal classification
- missing/duplicate jobs, invalid validated construction, failed point containment, failed source/Toller controls, or nonfinite interval arithmetic -> `ITER501_NUMERICAL_METHOD_BLOCKER`;
- if every frozen rho/box state is `INTERVAL_ROBUST_NONDECAY` -> `ITER501_DIRECT_MAX_ENVELOPE_INTERVAL_ROBUST_QUALIFIED_SCOPED`;
- else if every state is `INTERVAL_ROBUST_NONDECAY` or `INTERVAL_NONDECAY` -> `ITER501_DIRECT_MAX_ENVELOPE_INTERVAL_NONDECAY_QUALIFIED_SCOPED`;
- else if at least one valid state is `INTERVAL_UNIFORM_DECAY_WITNESS` -> `SCIENTIFIC_FAIL_ITER501_UNIFORM_NONDECAY_INTERVAL`;
- otherwise -> `ITER501_VALIDATED_INTERVAL_INCONCLUSIVE_SCOPED`.

A scientific FAIL must remain a scientific FAIL; thresholds may not be relaxed to obtain green CI. The workflow/evaluator should exit successfully after producing a structurally valid scientific classification so aggregate evidence is always preserved.

## Parallelism
Use 12 independent `causal × block` jobs, `fail-fast:false`, `max-parallel:12`, followed by one aggregate job.

## Scope guards
Even a full NONDECAY qualification proves only the direct continuous max-envelope result on the prospectively frozen one-dimensional q=1 signed direction intervals. It is **not** a 6-D/20-D positive-measure neighborhood theorem, not an absolute Haar divergence theorem, not a statement about the fully contracted ten-spectral causal vertex, and not D7-S2 closure.

D7-S2/S3/S4 remain open/partial. Terminal D7 labels remain forbidden. Candidate Gravity remains inactive.

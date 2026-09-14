# Iter504 preregistration — full centered max-envelope D7-S2 science campaign

Date: 2026-09-15
Status: **FROZEN BEFORE IMPLEMENTATION / PRODUCTION**

## Authorization chain

Iter504 is authorized for preregistration only because all three prospectively required method controls are terminal and green:

1. Iter503: `ITER503_CENTERED_DEPENDENCY_REPAIR_ENABLED_SCOPED`, run `34895563822`;
2. Iter503D: independent dual-source derivative identity audit PASS, 1440/1440 identities;
3. Iter503V: `ITER503V_ENDPOINT_CONTRACT_CONFIRMED`, run `34898125306`, 288/288 frozen endpoint checks contained.

These are enabling results only. Iter504 is the first full science classifier allowed to use the centered single-common-amplitude dependency-preserving enclosure on the complete Iter501 q=1 signed-direction domain.

## Scientific question

On the complete prospectively frozen continuous q=1 signed-direction interval domain inherited from Iter501, does the validated 243-channel max-envelope exhibit robust NONDECAY, weaker NONDECAY, a uniform DECAY witness, or remain interval-inconclusive once the Iter501 dependency-loss numerical blocker is replaced by the qualified Iter503 centered enclosure?

A valid uniform DECAY witness is a scientific failure of the frozen NONDECAY hypothesis on this scoped domain. It must not be reclassified as a numerical problem and must never trigger threshold relaxation.

## Frozen physical/source domain — inherited exactly

No physical/source dimension is changed from Iter501:

- active coordinates: `[0,1,3,5,6,11]`;
- eight frozen q=1 directions from `iter499_arb_core.DIRS`, grouped into the same four blocks `BLOCKS=[DIRS[0:2],DIRS[2:4],DIRS[4:6],DIRS[6:8]]`;
- both signs `+1,-1` for every direction;
- causal classes: `0to5`, `1to4`, `2to3`;
- 16 original amplitude boxes covering `[0.00125,0.00250]` exactly as `iter499_arb_core.box_amp(k)`;
- point-regression amplitudes exactly
  `0.00125, 0.00140625, 0.0015625, 0.00171875, 0.001875, 0.00203125, 0.0021875, 0.00234375, 0.00250`;
- rho witnesses: `0.35,0.9,1.6,2.7`;
- R grid: `6,8,10,12`;
- exact-rational j=1 intertwiners and all 243 channels;
- Iter500 compact-sandwich/factorized KAK source construction;
- `python-flint==0.9.0`, Arb/Acb precision 384 bits.

No direction, sign, causal, amplitude box, rho, R value, channel or point-regression amplitude may be removed after production begins.

## Frozen centered enclosure method

For each original amplitude box `[a0-h,a0+h]`, use one shared amplitude variable throughout the full source-faithful geometry/KAK/Toller/contraction path.

For every source quantity whose final centered enclosure is needed, use the already-qualified first-order mean-value form

`F_centered(a) = F(a0) + (a-a0) D([a0-h,a0+h])`,

where `D` is produced by the Iter503 validated interval-AD path with the single common amplitude dependency preserved. Repeated source factors may not be replaced by independent amplitude copies.

For every R:

1. construct the dual source state with `iter503_ad_core.construct_dual_state` on the full original amplitude box;
2. require the inherited construction and cycle predicates;
3. construct the exact Iter500 source-faithful center state at `a0` and require `enable.source_regression(...).pass`;
4. form centered `log Haar` from the center value plus the validated derivative enclosure;
5. for each rho and required causal branch, form the same source-defined full Toller matrix and its validated derivative through `iter503_ad_core.dfull_toller`;
6. contract all 243 channels with the exact inherited contraction path;
7. form centered channel enclosures with the common-amplitude delta and take the validated max-envelope over all 243 channels without assuming a unique maximizer;
8. require finite positive envelope bounds and all source-additivity controls.

No fallback to the failed Iter501 natural interval or Iter502 subdivision method is allowed.

## Frozen science observables and thresholds

For every `causal × direction × sign × amplitude box × rho`, let

`Y(R)=log Haar(R)+log max_channel |C_channel(R)|`.

From validated Y enclosures define exactly as Iter501:

- late slope interval `S` from R=8 to R=12;
- early slope interval `E` from R=6 to R=10;
- drift upper bound as the maximum separation between early and late slope intervals.

Thresholds are unchanged:

- drift tolerance: `0.05`;
- ROBUST NONDECAY lower-slope floor: `+1.0`;
- NONDECAY lower-slope floor: `0.0`;
- UNIFORM DECAY upper-slope ceiling: `-0.10`.

Per-rho/box classification is frozen:

- `INTERVAL_ROBUST_NONDECAY` iff late lower slope `>= 1.0` and drift `<= 0.05`;
- `INTERVAL_NONDECAY` iff late lower slope `>= 0.0` and drift `<= 0.05`;
- `INTERVAL_UNIFORM_DECAY_WITNESS` iff late upper slope `<= -0.10` and drift `<= 0.05`;
- otherwise `INTERVAL_INCONCLUSIVE`.

## Mandatory source-point containment

The same nine Iter501 source point amplitudes must be evaluated by the unchanged established Iter492 point path for every causal/direction/sign/rho.

For a point on a shared boundary of two amplitude boxes, containment may be witnessed by either adjacent original box, exactly as Iter501. Both the late and early point slopes must lie in the corresponding centered interval slope enclosures.

Any failed mandatory point containment, failed source/KAK/Toller control, nonfinite/invalid interval result, missing box/path, or malformed lane is a **numerical-method blocker**, not scientific DECAY evidence.

## Logical lanes and outcome-blind compute sharding

The scientific campaign retains exactly **12 logical lanes**:

`3 causal classes × 4 direction blocks`.

Each logical lane must contain all four signed paths of its block (two directions × two signs), all 16 amplitude boxes and all four rhos.

Because the qualified centered interval-AD calculation is substantially more expensive than Iter501 natural interval arithmetic, production may split a logical lane into outcome-blind compute shards **without changing the logical lane or classifier**:

- four fixed path indices per logical lane:
  - path 0 = first block direction, sign `+1`;
  - path 1 = first block direction, sign `-1`;
  - path 2 = second block direction, sign `+1`;
  - path 3 = second block direction, sign `-1`;
- each path is split into exactly two fixed box shards: boxes `0..7` and boxes `8..15`;
- therefore there are 8 centered box-shard artifacts per logical lane and 96 box-shard computations overall;
- point-regression values are computed in one separate point artifact per logical causal×block lane, giving 12 point artifacts;
- the terminal aggregate must reconstruct exactly the 12 logical lanes before applying any science classification.

Compute sharding is orchestration only. It may not alter precision, evaluation formulas, boxes, thresholds, channels or point-containment rules.

Production matrix requirements:

- all compute matrices use `fail-fast:false`;
- centered box-shard matrix uses `max-parallel:12`;
- point-regression matrix uses `max-parallel:12`;
- missing/duplicate shards or point artifacts force the method-blocker classification.

## Frozen terminal classification

After reconstructing the complete 12 logical lanes:

- structural incompleteness, duplicate/missing shards, failed controls, failed point containment, or invalid/nonfinite centered arithmetic -> `ITER504_NUMERICAL_METHOD_BLOCKER`;
- if every frozen rho/box state is `INTERVAL_ROBUST_NONDECAY` -> `ITER504_CENTERED_MAX_ENVELOPE_ROBUST_QUALIFIED_SCOPED`;
- else if every state is `INTERVAL_ROBUST_NONDECAY` or `INTERVAL_NONDECAY` -> `ITER504_CENTERED_MAX_ENVELOPE_NONDECAY_QUALIFIED_SCOPED`;
- else if at least one valid state is `INTERVAL_UNIFORM_DECAY_WITNESS` -> `SCIENTIFIC_FAIL_ITER504_UNIFORM_NONDECAY_INTERVAL`;
- otherwise -> `ITER504_VALIDATED_CENTERED_INTERVAL_INCONCLUSIVE_SCOPED`.

A structurally valid scientific FAIL must be preserved as FAIL while the workflow itself exits successfully so artifacts remain available. Thresholds may not be weakened to obtain a green scientific label.

## Expected complete counts

The aggregate must validate, before scientific classification:

- 12 logical causal×block lanes;
- 96 centered box-shard artifacts;
- 12 point-regression artifacts;
- 4 signed paths per logical lane;
- 16 boxes per signed path;
- `12 × 4 × 16 = 768` direction/sign/box records;
- `768 × 4 = 3072` rho/box science states;
- all 243 channels used in every envelope evaluation.

## Scope ceiling

Even a full Iter504 NONDECAY qualification proves only the centered continuous 243-channel max-envelope result on the frozen one-dimensional q=1 signed-direction amplitude intervals. It is not:

- a 6-D or 20-D positive-measure neighborhood theorem;
- an absolute Haar divergence theorem;
- spectral-cutoff removal;
- collision-cutoff removal;
- a theorem about the fully contracted ten-spectral causal vertex;
- D7-S2 closure by itself;
- authorization for a terminal D7 selector.

`D7-S2`, `D7-S3`, and `D7-S4` remain governed independently after this gate. Candidate Gravity remains inactive.

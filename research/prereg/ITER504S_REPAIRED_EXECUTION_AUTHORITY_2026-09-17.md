# Iter504S — repaired execution authority

Date: 2026-09-17
Status: PROSPECTIVELY FROZEN BEFORE REPAIRED SCIENTIFIC EXECUTION

Scientific gate remains exactly:

`ITER504S_ROOT_DERIVATIVE_VS_CHANNEL_COMPETITION_DISCRIMINATOR`

Scientific preregistration remains exactly:

`f6367456aa715fe6282ab70c1b2005971a4568c7`

No scientific criterion is changed by this authority record.

## Parent and first-execution state

Parent Iter504R remains terminal:

`ITER504R_ROOT_AFFINE_REUSE_INCONCLUSIVE_SCOPED`

with terminal record `598ede26e0db448411537e9d5f813aa344f88d0f` and independent Critic `6e300294e6c9a470099776d1c30357eed3fa4b93`.

The initial Iter504S run `35173442220`, workflow head `cb50a107b24232ef1b652baa9443e69fc3fa6ca1`, is terminal `completed/failure`. All six root jobs failed at the evaluator step with the same representation error family, including independently checked Python 3.11 and Python 3.13 lanes:

`TypeError("cannot create acb from type <class 'iter503_ad_core.CD'>")`

Assembly never produced a scientific payload. The first execution is therefore implementation-invalid and non-authoritative for scientific classification. Durable record:

`f916873228f970844c775dbaaabeba999b432365`

## Prospectively frozen repairs

Exactly two repairs are authorized, both frozen before any repaired execution and before substantive Iter504S scientific output consumption:

1. dual derivative extraction repair `88c92f86a765e9d8b441152674fc2c303f3f1ff3`;
2. fixed-channel drift-only semantics repair `4ef41c0f4ceed3082fd4d80930ef5d848f18802b`.

Repair 1 only extracts `ad.as_c(z).d` from the already-computed dual contraction object. Full-D retains the unchanged validated full-root derivative ball. Center-D uses only the deterministic midpoint of that same derivative ball and remains control-only.

Repair 2 affects only fixed-channel competition attribution. A complete fixed-channel competition row is within the competition tolerance iff its actual maximum eligible candidate `drift_upper <= 0.05`. Fixed-channel `S_lower` is not part of that competition predicate. The full-envelope predicate remains `S_lower >= 1.0 AND drift_upper <= 0.05`.

## Repaired implementation chain

Prepared without triggering the scientific workflow:

- repaired evaluator: `b20077e77b421a68f1a99135ff652e52a0d53227` — `code/iter504s_mechanism_discriminator_repaired.py`;
- repaired independent assembler: `7dc689f9b4d7e4f768a677e2afc80668a15b73d9` — `code/iter504s_mechanism_assemble_repaired.py`;
- repaired cross-environment aggregate: `b0347e225b986b63e079ef6ebf02cd928022eb39` — `code/iter504s_mechanism_aggregate_repaired.py`;
- repaired adversarial Critic: `38c705865b0397c7cf664ad142ad232d3b0a312f` — `code/iter504s_adversarial_critic_repaired.py`.

The repaired Critic independently reconstructs the drift-only competition predicate from `max_fixed_channel_drift_upper`, checks all 36 root/location/rho cases, exact rational points, rho/R grids, 243-channel completeness, no pruning, derivative representation, full-D vs center-D distinction, possible-max identities, strict dominance flags, mechanism flags, terminal classification, and cross-environment discrete agreement.

Its controls include a semantic positive control: changing only a fixed-channel witness `S_lower` must not alter competition attribution.

## Pre-execution verification

Methodology CI run `35175274675`, head `38c705865b0397c7cf664ad142ad232d3b0a312f`, completed/success before repaired scientific launch.

Its preflight compiled the reference code, validated JSON/methodology structure, all four deterministic methodology shards completed/success, and aggregate-and-bundle completed/success.

This is execution-quality evidence only; it is not a scientific Iter504S PASS.

## Frozen scientific inputs retained exactly

- `python-flint==0.9.0`;
- Arb/Acb precision `384` bits;
- all `243` channels retained;
- channel pruning forbidden;
- causal `0to5`;
- block `0`;
- path `2`;
- direction `[1,1,1,-1,-1,-1]`;
- sign `+1`;
- roots `13,14,15`;
- rhos `[0.35,0.9,1.6,2.7]`;
- R grid `[6,8,10,12]`;
- robust floor `+1.0`;
- drift threshold `0.05`;
- exact LOW/MID/HIGH points from preregistration;
- no new diagnostic point;
- no post-outcome channel selection;
- center-D remains control-only.

## Frozen terminal classifier retained exactly

Only these terminal scientific classes remain allowed:

- `ITER504S_ROOT_DERIVATIVE_RADIUS_LOCALIZED_SCOPED`;
- `ITER504S_CHANNEL_COMPETITION_NECESSARY_SCOPED`;
- `ITER504S_FIXED_CHANNEL_NONSTATIONARITY_REMAINS_SCOPED`;
- `ITER504S_MIXED_MECHANISM_SCOPED`;
- `ITER504S_INVALID`.

No fifth class may be introduced after output.

## Repaired execution rule

Exactly one repaired Iter504S workflow execution is authorized after this record.

It must run two independent environment cohorts, Python `3.11` and `3.13`, for roots `13,14,15`; assemble each environment independently; compare frozen scientific decisions rather than incidental float serialization; run the repaired adversarial Critic; and preserve all artifacts/environment metadata.

Any cross-environment disagreement that flips a frozen inequality, eligibility, possible-max identity, dominance flag, mechanism flag, or terminal classification makes the gate `ITER504S_INVALID` until reconciled.

## Claim ceiling

Even a valid scoped Iter504S mechanism result is only a bounded three-root mechanism-localization certificate. It does not reclassify the full 1888 Iter504 states, does not close D7, does not authorize Candidate Gravity or Paper IV, and does not establish quantum gravity or new physics.

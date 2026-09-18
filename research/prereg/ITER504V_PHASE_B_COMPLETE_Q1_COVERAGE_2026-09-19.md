# Iter504V Phase B complete q=1 cover — prospective preregistration

Date: 2026-09-19
Status: **FROZEN_BEFORE_IMPLEMENTATION_AND_EXECUTION**

## Gate

`ITER504V_BROADER_DOMAIN_COMPLETE_Q1_COVERAGE`

This gate is the separately preregistered Phase-B successor permitted by the prospectively frozen Iter504V campaign design only after terminal Phase-A closure.

It does not authorize execution by itself.

## Terminal parent

Phase A is terminal:

- terminal result commit: `d03cae09c04638cb02412435a284cfd9acdf8406`;
- terminal result blob: `2dbdcf3a611c014bd4ff52c9859a3890df06c9b2`;
- terminal classification:
  `ITER504V_SENTINEL_LOCAL_D_NO_COUNTEREXAMPLE_SCOPED`;
- source run: `35365466861`, run #3 / attempt #1;
- independent repaired Critic run: `35403877439`, run #2 / attempt #1;
- Critic cross-Python exact semantic agreement: true;
- counterexample identities: none.

This means only that no counterexample was found in the frozen 16-state sentinel. It does not certify the full q=1 domain.

## Frozen campaign authority

Bind exactly:

- broader-domain campaign design commit:
  `6a789730833120a5e3037fdc11fe03b28ed5b9cb`;
- campaign design blob:
  `0a0f4408b60710010cdcf4d2cd64a01ab2123487`;
- campaign manifest blob:
  `d3b8821e08243016bd475f3faf9f2161deed13d8`;
- canonical 768-record newline-terminated identity SHA256:
  `3cac282175830e795394dca5202f5368b27120817f2d4abd9eba54fc6c9f1e6f`.

No domain dimension may be removed after implementation/execution authority is frozen.

## Scientific question

Does the exact no-refit local-D depth-3 certificate certify every record in the complete authorized parent q=1 signed-direction domain under the unchanged contract, or does at least one parent-domain record retain an uncertified terminal leaf at frozen depth 3?

The scientific objective is complete deterministic coverage, not confirmation of the clean sentinel.

## Complete frozen domain

Exactly:

- causals: `0to5, 1to4, 2to3`;
- blocks: `0..3`;
- signed paths per block: `0..3`;
- amplitude boxes: `0..15`;
- total canonical records: `3×4×4×16 = 768`;
- rho values: `0.35, 0.9, 1.6, 2.7`;
- rho-level states: `3072`;
- R cohort: `6,8,10,12`;
- channels: `243`.

Canonical record:
`<causal>|b<block>|p<path>|x<box02>`.

Enumeration order remains causal-major, then block, path, box.

## No-refit science contract

Preserve exactly the terminal Phase-A contract:

- precision: 384 bits;
- `python-flint==0.9.0`;
- all 243 channels;
- no channel pruning;
- R = `6,8,10,12`;
- rho = `0.35,0.9,1.6,2.7`;
- exact drift tolerance `1/20`;
- exact robust late-slope floor `1`;
- deterministic dyadic midpoint partition;
- `MAX_DEPTH=3`;
- local validated `D(J)` recomputed at every visited node;
- exact rational cells and exact parent cover;
- leaf certification = conjunction of all four per-rho exact booleans;
- scientific decisions use exact Arb booleans only;
- display floats have no scientific authority;
- uncertified terminal leaf is allowed only at depth exactly 3;
- no threshold/floor/depth/R/rho/channel/source/classifier adaptation after outcomes.

## Deterministic Phase-B partition

Use exactly the campaign design:

- 48 logical path lanes = 3 causals × 4 blocks × 4 paths;
- each logical path lane contains all 16 boxes;
- split each lane into four fixed box quartiles:
  - `0..3`
  - `4..7`
  - `8..11`
  - `12..15`;
- exactly 192 deterministic compute shards per Python environment;
- Python environments: exactly `3.11` and `3.13`;
- exactly 384 source compute shards total across both environments;
- `fail-fast:false`;
- `max-parallel:12`.

Shard identity:
`(python, causal, block, path, box_quartile)`.

No shard order or inclusion may depend on partial scientific results.

## Partial-value firewall

Before complete source terminalization:

- do not consume leaf/slope/drift/certification values from completed shards;
- do not classify partial lanes;
- do not stop because the observed prefix appears clean;
- do not choose resume targets based on science values.

Only infrastructure/job/artifact metadata may be inspected preterminally.

Missing/failed shards may be replaced only by identity-preserving execution repair under the exact frozen science contract.

## Source classification

After all 768 records are present in both environments and exact cross-environment decision identity is established:

`ITER504V_BROADER_DOMAIN_LOCAL_D_CERTIFIES_COMPLETE_Q1_SCOPED`

iff all structure/provenance is valid and total unresolved terminal leaves over all 768 records are zero.

`ITER504V_BROADER_DOMAIN_LOCAL_D_INCONCLUSIVE_SCOPED`

iff all structure/provenance is valid and at least one record has at least one uncertified terminal leaf at depth 3.

`ITER504V_BROADER_DOMAIN_INVALID`

iff implementation/provenance/cohort/channel/depth/partition/source/artifact/cross-environment contract is invalid.

There is no model-level or physics-level FAIL label.

## Counterexample-first successor rule

If any valid unresolved record exists:

- terminalize the complete-cover source result;
- freeze the smallest exact unresolved record and cell identity;
- do not first increase `MAX_DEPTH`;
- prospectively localize residual mechanism:
  `LOCAL_DERIVATIVE_CONTRACTION`,
  `CHANNEL_SWITCHING`,
  `FIXED_CHANNEL_NONSTATIONARITY`,
  or `MIXED_OBSTRUCTION`.

## Independent Critic

Source production must not contain the authoritative Critic.

After source terminalization and exact artifact freeze, a separately prospectively frozen Critic must independently verify:

- chronology and frozen authority;
- canonical 768-record identity regeneration and SHA256;
- exact complete shard cover;
- source geometry, direction/sign/box identities;
- exact R/rho/channel/precision contract;
- dyadic tree and local-D recomputation binding;
- exact leaf/per-rho certification;
- unresolved-depth binding;
- immutable artifact provenance;
- exact cross-Python decision equality;
- all inherited negative controls.

Terminal authority requires Critic closure.

## Current authorization boundary

This preregistration freezes Phase-B science only.

At this commit:

- implementation authoring: **NOT AUTHORIZED**;
- source execution: **NOT AUTHORIZED**;
- Actions launch: **NOT AUTHORIZED**;
- Phase-B scientific payload consumption: **NOT AUTHORIZED**.

A separate static implementation authority and then a separate one-shot/bounded execution authority are required.

## Claim ceiling

Even future complete-cover PASS would mean only that the frozen local-D certificate covers the inherited 768-record q=1 signed-direction amplitude domain under this 243-channel construction.

It would not establish:

- global quantum gravity;
- all known models fail;
- new QG theory required;
- quantum gravity solved;
- unique mechanism;
- new physics found.


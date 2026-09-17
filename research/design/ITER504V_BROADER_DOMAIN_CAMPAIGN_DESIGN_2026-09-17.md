# Iter504V broader-domain campaign design — counterexample-first local-D generalization

Date: 2026-09-17
Status: PROSPECTIVELY_FROZEN_CAMPAIGN_DESIGN

## Authorization

This design is authorized only after:

- terminal Iter504U scientific classification `ITER504U_HELDOUT_LOCAL_D_GENERALIZES_SCOPED`;
- terminal Iter504U repaired-Critic authority commit `a31db0d6b9f98448977a6fcdde80a45e3e7195fe`;
- terminal bounded infrastructure audit `ITER504U_END_TO_END_INFRASTRUCTURE_AUDIT_PASS_SCOPED`;
- infrastructure freeze `ITER504U_POSTCLOSURE_INFRASTRUCTURE_FROZEN_SCOPED`;
- frozen outcome-blind successor policy `research/methodology/ITER504U_OUTCOME_BLIND_SUCCESSOR_POLICY_2026-09-17.md`.

The successor policy authorizes campaign DESIGN after an Iter504U PASS. This document does not by itself authorize the full broader-domain production.

## Scientific question

Does the exact no-refit local-D certificate that passed the prospectively frozen development and Iter504U held-out cases continue to certify the complete authorized Iter504 q=1 signed-direction amplitude domain under the same frozen depth-3 contract, or does there exist a valid parent-domain record for which the local-D certificate remains unresolved?

The cheapest decisive evidence is a single valid unresolved record. Therefore the campaign is designed counterexample-first rather than as an immediate full sweep.

This is a certificate-generalization question, not a model-family failure question and not a global quantum-gravity claim.

## Exact authorized parent domain

The parent domain is inherited exactly from the prospectively frozen Iter504 full centered campaign:

- causal classes: `0to5`, `1to4`, `2to3`;
- four direction blocks;
- four signed paths per block;
- sixteen amplitude boxes `0..15` covering `[0.00125,0.00250]`;
- four rho values `0.35,0.9,1.6,2.7`;
- R grid `6,8,10,12`;
- all 243 channels;
- exact source geometry and q=1 signed-direction realization.

A canonical parent record is identified by

`<causal>|b<block>|p<path>|x<box02>`.

Enumeration order is causal-major, then block, then path, then box. The exact 768-record identity sequence is defined machine-readably in `inputs/iter504v_broader_domain_campaign_manifest.json` and must regenerate with SHA256:

`3cac282175830e795394dca5202f5368b27120817f2d4abd9eba54fc6c9f1e6f`

when the canonical IDs are joined with `\n` and terminated by a final newline.

Counts:

- `3 × 4 × 4 × 16 = 768` causal/direction/sign/box records;
- `768 × 4 = 3072` rho-level certificate states.

No dimension may be removed after an execution authority is frozen.

## Frozen no-refit local-D scientific contract

Every broader-domain evaluation must preserve exactly the Iter504U local-D contract:

- Arb/Acb precision: 384 bits;
- `python-flint==0.9.0`;
- all 243 channels, no pruning;
- R cohort `(6,8,10,12)`;
- rho cohort `(0.35,0.9,1.6,2.7)`;
- exact drift tolerance `1/20`;
- exact robust late-slope floor `1`;
- deterministic dyadic midpoint subdivision;
- `MAX_DEPTH=3`;
- validated local derivative `D(J)` recomputed independently at every visited node;
- exact rational interval/cell identity and exact parent cover;
- inherited centered mean-value construction;
- local Haar/log derivative treated analogously;
- scientific decisions transported by exact Arb booleans; display floats have no authority;
- leaf certification bound exactly to all four per-rho decisions;
- an uncertified terminal leaf is valid only at `depth == MAX_DEPTH`;
- cross-environment disagreement is implementation/provenance invalidity, never voting/averaging.

No held-out or broader-domain outcome may change threshold, floor, R/rho cohort, channels, depth, partition, source realization, or classifier.

## Phase A — 16-record structural sentinel falsifier

Before any 768-record sweep, execute a small prospective falsifier covering the parent factors structurally.

Selection is outcome-independent and purely combinatorial:

For each `block b in {0,1,2,3}` and `path p in {0,1,2,3}`:

- `box = 4*b + p`;
- `causal_index = (b+p) mod 3` over `[0to5,1to4,2to3]`.

This yields exactly one record for every `block×path` pair and exactly one record for every amplitude box `0..15`, while covering all eight directions, both signs and all three causal classes. It has zero exact-record overlap with the nine local-D records used in Iter504T development plus Iter504U held-out science.

Exact sentinel IDs are frozen in the machine manifest. Their newline-sequence SHA256 is:

`b56a2a32cd96b28c14aaaa86f1062d1f2f2a167a2295ed99f904a99fd8371e82`.

### Phase-A terminal taxonomy

`ITER504V_SENTINEL_INVALID`

iff source/provenance/cohort/precision/channel/depth/partition/decision-binding/artifact identity/cross-environment contract is invalid.

`ITER504V_SENTINEL_LOCAL_D_COUNTEREXAMPLE_TO_UNIFORM_CERTIFICATION_SCOPED`

iff the execution is valid and cross-environment decisions agree, but at least one sentinel record contains at least one uncertified terminal leaf at frozen depth 3.

This is a counterexample to universal certification by the current local-D depth-3 procedure on the parent q=1 domain. It is NOT a scientific decay witness, model failure, D7 failure, or quantum-gravity failure.

`ITER504V_SENTINEL_LOCAL_D_NO_COUNTEREXAMPLE_SCOPED`

iff all 16 sentinel records are valid, exact cross-environment decisions agree, all required controls pass and total unresolved terminal leaves are exactly zero.

This label does NOT prove the complete parent domain. It only authorizes a separately frozen Phase-B full-cover production.

### Phase-A stopping rule

If a valid counterexample is found, do not execute the full 768-record campaign. Freeze the exact counterexample record/cell identities and move to prospective residual-mechanism localization for that record.

If no counterexample is found, Phase B may be preregistered separately without changing the local-D scientific contract.

## Phase-A execution design

Production cases: exactly 16 sentinel records in both Python 3.11 and Python 3.13.

- matrix `fail-fast:false`;
- maximum parallel case jobs: 12;
- one immutable case artifact per environment/record;
- independent per-environment assembly;
- exact cross-environment aggregate decision projection;
- no partial scientific payload consumption before all sentinel case artifacts required by the authority are terminal/frozen;
- independent repaired Critic consumes immutable artifacts only and must include all validated C4 and shallow-unresolved depth-binding controls;
- no producer rerun merely because Critic/control validation fails.

The Phase-A execution itself requires a separate preregistration/authority after this design is committed.

## Phase B — complete-cover plan (not yet authorized for execution)

If and only if Phase A terminates `ITER504V_SENTINEL_LOCAL_D_NO_COUNTEREXAMPLE_SCOPED`, a separate preregistration may authorize complete coverage of all 768 records.

Deterministic logical partition:

- 48 logical path lanes = `3 causals × 4 blocks × 4 paths`;
- each logical path lane contains all 16 boxes;
- each path lane is split into four fixed box-quartile compute shards: `0..3`, `4..7`, `8..11`, `12..15`;
- therefore 192 deterministic compute shards per Python environment;
- matrices use `fail-fast:false` and `max-parallel:12`;
- each shard identity is fully determined by `(python, causal, block, path, box_quartile)`;
- missing/failed shards may be resumed only as execution-only replacements under the exact frozen science contract; no threshold/cohort/depth/channel/classifier edits are allowed;
- completed shard scientific values must not be used to choose which other shards to run.

Phase-B aggregation must reconstruct exactly all 768 records / 3072 rho states before complete-domain classification.

### Phase-B planned terminal taxonomy

`ITER504V_BROADER_DOMAIN_LOCAL_D_CERTIFIES_COMPLETE_Q1_SCOPED`

iff complete structure/provenance is valid, both environments agree exactly on scientific decisions, independent Critic passes and total unresolved terminal leaves over all 768 parent records are zero.

`ITER504V_BROADER_DOMAIN_LOCAL_D_INCONCLUSIVE_SCOPED`

iff complete structure/provenance is valid and environments agree but at least one parent record retains an uncertified terminal leaf at frozen depth 3.

`ITER504V_BROADER_DOMAIN_INVALID`

for implementation/provenance/cross-environment/artifact/source/cohort/decision-contract invalidity.

There is no model-level or physics-level scientific FAIL label in this certificate-generalization campaign.

## Independent Critic requirements

The Critic must independently verify at minimum:

- exact campaign/prereg authority and chronology;
- canonical state identity regeneration and identity SHA256;
- exact source geometry/directions/signs/boxes;
- exact R/rho cohorts and 243-channel completeness;
- precision, threshold, floor, `MAX_DEPTH`, dyadic partition and local-D recomputation;
- exact leaf/per-rho binding;
- unresolved-leaf depth binding;
- source and immutable artifact identities;
- exact environment decision agreement;
- deterministic shard full cover for Phase B;
- all inherited negative controls, including C4 and premature-unresolved-depth controls;
- no development/held-out/broader result used post hoc to alter the frozen contract.

## Resource and resume ceiling

This design intentionally separates a cheap 16-record falsifier from the expensive complete cover. Full Phase B is forbidden unless the Phase-A sentinel gate finds no counterexample.

No adaptive expansion based on partial Phase-A or Phase-B science values is allowed. Resume semantics are identity-preserving execution repair only.

## Why this gate has highest current information gain

Historical full-domain Iter504 was scientifically valid but left 1888/3072 rho states INCONCLUSIVE solely because drift/envelope width exceeded the frozen tolerance; it found no uniform-decay witness and all late-slope lower bounds remained above the robust floor.

Iter504T/Iter504U then showed, with no refit, that recomputing validated local `D(J)` can close representative development and prospectively frozen held-out cases, including amplitude, causal, direction and sign variation.

Therefore the highest-value surviving question is no longer slope sign or whether one particular held-out case works. It is whether a single parent-domain counterexample to local-D certification still exists.

A 16-record structural sentinel can falsify the universal-certificate mechanism at roughly 1/48 of the record count of a 768-record full cover while spanning every block×path pair and every amplitude box. A found counterexample immediately prevents an expensive full sweep and localizes the next mechanism question. A clean sentinel result unlocks, but does not substitute for, the deterministic full-cover campaign.

The parallel D7 normalization/observable branch remains scientifically important, but current recovery retains group-only contact restriction and physical transverse quotient as `BLOCKED_SCOPED`; the local-D broader-domain gate is presently more executable while directly resolving the dominant validated Iter504 inconclusive mechanism.

## Claim ceiling

Neither this design nor Phase A can establish all-Iter504/global quantum gravity, all-model-family failure, D7 closure, Candidate Gravity, Paper IV, `ALL_KNOWN_MODELS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `QUANTUM_GRAVITY_SOLVED`, `UNIQUE_MECHANISM`, or `NEW_PHYSICS_FOUND`.

Even a future Phase-B complete q=1 certificate remains scoped to the inherited one-dimensional q=1 signed-direction amplitude domain and 243-channel max-envelope construction.

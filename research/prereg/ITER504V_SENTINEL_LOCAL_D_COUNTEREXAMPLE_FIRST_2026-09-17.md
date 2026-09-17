# Iter504V sentinel local-D counterexample-first gate — preregistration

Date: 2026-09-17
Status: FROZEN_BEFORE_IMPLEMENTATION_AND_PRODUCTION

## Gate

`ITER504V_SENTINEL_LOCAL_D_COUNTEREXAMPLE_FIRST`

This gate is the first execution stage authorized by the prospectively frozen broader-domain campaign design. It is a cheap falsifier for universal certification by the current local-D depth-3 procedure, not a full-domain proof attempt.

## Authorization chain

- terminal Iter504U class: `ITER504U_HELDOUT_LOCAL_D_GENERALIZES_SCOPED`;
- terminal Iter504U authority commit: `a31db0d6b9f98448977a6fcdde80a45e3e7195fe`;
- bounded infrastructure audit commit: `dd32ae2616f4cbe3826f73c7a1d2f51818b4954c`;
- campaign design commit: `6a789730833120a5e3037fdc11fe03b28ed5b9cb`;
- campaign design blob: `0a0f4408b60710010cdcf4d2cd64a01ab2123487`;
- campaign manifest blob: `d3b8821e08243016bd475f3faf9f2161deed13d8`;
- parent q=1 full-domain preregistration: `1ab46b7add51b36b5499f866eb4579137838bfae`.

No full 768-record Phase-B execution is authorized by this preregistration.

## Frozen scientific hypothesis

Hypothesis under attack:

`The exact no-refit Iter504U local-D depth-3 certificate has no unresolved record on the authorized parent q=1 signed-direction domain.`

A single valid sentinel record with an uncertified terminal leaf at frozen `MAX_DEPTH=3` is sufficient to falsify this universal-certificate hypothesis for the current procedure.

Such a counterexample is NOT a decay witness, model failure, D7 failure, or quantum-gravity failure.

## Exact sentinel cohort

Selection is structural and outcome-independent:

For every `block b in {0,1,2,3}` and `path p in {0,1,2,3}`:

- `box = 4*b + p`;
- `causal = [0to5,1to4,2to3][(b+p) mod 3]`.

Exact canonical state IDs, in frozen order:

1. `0to5|b0|p0|x00`
2. `1to4|b0|p1|x01`
3. `2to3|b0|p2|x02`
4. `0to5|b0|p3|x03`
5. `1to4|b1|p0|x04`
6. `2to3|b1|p1|x05`
7. `0to5|b1|p2|x06`
8. `1to4|b1|p3|x07`
9. `2to3|b2|p0|x08`
10. `0to5|b2|p1|x09`
11. `1to4|b2|p2|x10`
12. `2to3|b2|p3|x11`
13. `0to5|b3|p0|x12`
14. `1to4|b3|p1|x13`
15. `2to3|b3|p2|x14`
16. `0to5|b3|p3|x15`

Newline-terminated state-ID sequence SHA256:

`b56a2a32cd96b28c14aaaa86f1062d1f2f2a167a2295ed99f904a99fd8371e82`.

The cohort covers every `block×path` pair exactly once, every amplitude box exactly once, all eight directions, both signs and all three causal classes. It has zero exact-record overlap with the nine prior Iter504T/Iter504U local-D records.

No sentinel record may be substituted after production begins.

## Frozen science contract — no refit

Identical to Iter504U:

- source geometry inherited from Iter499/500/503;
- precision 384 bits;
- `python-flint==0.9.0`;
- all 243 channels, no pruning;
- R cohort exactly `6,8,10,12`;
- rho cohort exactly `0.35,0.9,1.6,2.7`;
- exact drift tolerance `1/20`;
- exact robust late-slope floor `1`;
- deterministic dyadic midpoint partition;
- `MAX_DEPTH=3`;
- local validated `D(J)` recomputed at every visited node;
- exact rational cell identities and exact parent cover;
- exact leaf certification = conjunction of all per-rho certifications;
- scientific decisions use exact Arb booleans only; floats are display-only;
- uncertified terminal leaf allowed only at depth 3;
- no threshold, floor, depth, R/rho, channel, partition, source-realization or classifier adaptation after outcomes.

## Researcher production

Execute every exact sentinel record independently in both Python `3.11` and `3.13`.

Matrix requirements:

- `fail-fast:false`;
- maximum parallel case jobs: 12;
- one immutable case artifact per environment/state ID;
- independent assembly per environment;
- one aggregate artifact comparing exact scientific decision projections;
- cross-environment disagreement => `ITER504V_SENTINEL_INVALID`;
- no voting, averaging or display-float fallback.

The production source workflow must contain no authoritative Critic. Independent Critic review occurs only after the source run is terminal and exact source artifact IDs/digests are prospectively frozen.

## Researcher classification

For each environment, classification derives only from exact validated case structure and unresolved terminal leaves.

`ITER504V_SENTINEL_LOCAL_D_NO_COUNTEREXAMPLE_SCOPED`

iff all 16 exact records are valid and total unresolved terminal leaves = 0.

`ITER504V_SENTINEL_LOCAL_D_COUNTEREXAMPLE_TO_UNIFORM_CERTIFICATION_SCOPED`

iff all required structure/provenance is valid and at least one exact sentinel record has at least one uncertified terminal leaf at depth 3.

`ITER504V_SENTINEL_INVALID`

iff source/provenance/cohort/precision/channel/depth/partition/decision-binding/case-set/cross-environment contract is invalid.

The source aggregate classification is provisional until independently reconstructed by the repaired Critic.

## Partial-value firewall

Until the source run is terminal:

- do not consume case leaf/slope/drift/certification values;
- do not classify completed case lanes;
- do not choose a residual mechanism from partial science;
- do not relaunch or replace a slow case based on its partial outcome.

Only job/artifact metadata may be inspected preterminally.

## Artifact freeze before Critic

After source terminalization and before Critic science consumption, prospectively freeze:

- exact source run id/head/attempt/status/conclusion;
- exact successful source-lock/case/assembly/aggregate job identities;
- exact required artifact names, IDs, digests and expiration state;
- exact source workflow/evaluator/assembler/aggregate blobs.

The independent Critic may consume only those frozen immutable source artifacts.

## Independent repaired Critic

Critic must independently validate and reconstruct:

- campaign design/prereg/manifest chronology and exact identities;
- 16-state sentinel set and frozen sentinel SHA256;
- source state identity/factors/direction/sign/box interval;
- exact source/cohort/precision/channel contract;
- exact dyadic cover;
- per-rho and leaf certification binding;
- unresolved-leaf depth binding;
- local derivative recomputation at each visited node;
- parent-inclusion structure;
- exact environment decision projection equality;
- source assembly and aggregate classification;
- immutable artifact provenance;
- all inherited outcome-independent negative controls, including C4 and `premature_unresolved_leaf_depth`.

Critic must run independently in Python 3.11 and 3.13 and terminal closure must require byte/semantic equality of reconstructed scientific decision payloads.

## Terminal authority taxonomy

After repaired independent Critic closure, the only terminal labels are:

- `ITER504V_SENTINEL_LOCAL_D_NO_COUNTEREXAMPLE_SCOPED`;
- `ITER504V_SENTINEL_LOCAL_D_COUNTEREXAMPLE_TO_UNIFORM_CERTIFICATION_SCOPED`;
- `ITER504V_SENTINEL_INVALID`.

No new physics-level FAIL label exists.

## Successor rule

If terminal `NO_COUNTEREXAMPLE_SCOPED`: Phase-B complete 768-record coverage may be preregistered separately under the already-frozen campaign design. It must not infer full-domain certification from the sentinel alone.

If terminal `COUNTEREXAMPLE_TO_UNIFORM_CERTIFICATION_SCOPED`: do not run Phase B. Freeze the exact counterexample record/cell identities and preregister residual-mechanism localization discriminating local derivative contraction, channel switching, fixed-channel nonstationarity or mixed obstruction.

If terminal `INVALID`: only minimal implementation/provenance repair is admissible; no scientific inference and no contract retuning.

## Claim ceiling

This sentinel can falsify or fail to falsify universal certification by the current local-D procedure on a structurally diverse 16-record sample. It cannot establish complete q=1 coverage, D7 closure, model/family failure, Candidate Gravity, Paper IV, `ALL_KNOWN_MODELS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `QUANTUM_GRAVITY_SOLVED`, `UNIQUE_MECHANISM`, or `NEW_PHYSICS_FOUND`.

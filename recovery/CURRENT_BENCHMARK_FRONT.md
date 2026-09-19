# Current Benchmark Front

Updated: 2026-09-18

Fresh repository `main` and fresh GitHub Actions state always outrank this navigation snapshot.

## Active front

Gate: `ITER504V_BROADER_DOMAIN_COMPLETE_Q1_COVERAGE`.
Execution gate: `ITER504V_PHASE_B_SOURCE_EXECUTION`.

Authority chain:
- terminal Phase-A result `d03cae09c04638cb02412435a284cfd9acdf8406` -> `ITER504V_SENTINEL_LOCAL_D_NO_COUNTEREXAMPLE_SCOPED` for the frozen 16-state sentinel only;
- Phase-B prereg `e42caf47f9201d79cd89b79dc72b90f696e3ec5d`;
- static implementation Critic `eaa2d1ef84fe8370f33cec360233f60571f9bcd0` -> `PASS_SCOPED`;
- one-source execution authority `caf67585a9fad990dd90948df51839e6ed7cf891`;
- source launch/head `31fcdacffcc394e96b73917083281edb90d6753c`;
- authoritative source run `35405065903`.

The source run is nonterminal. The run endpoint reports `queued / conclusion=null`, while the job endpoint shows active execution. Source-lock job `105792998164` is terminal `success`; case-shard jobs are `in_progress` or `queued`. Fresh artifact metadata is empty. No partial scientific payload has been consumed.

Current status: `IN_PROGRESS_NOT_CLASSIFIED`.

## Frozen object and topology

Complete q=1 domain: causals `0to5,1to4,2to3` x blocks `0..3` x signed paths `0..3` x amplitude boxes `0..15` = 768 canonical records. Frozen contract: rho `0.35,0.9,1.6,2.7`; R `6,8,10,12`; all 243 channels; 384-bit precision; deterministic dyadic midpoint partition; `MAX_DEPTH=3`; local validated `D(J)` recomputed at every visited node; exact leaf/per-rho and unresolved-depth binding.

Execution: 192 deterministic quartile shards per Python environment, Python 3.11 and 3.13, 384 source compute shards total, `fail-fast:false`, `max-parallel:12`.

## Frozen taxonomy

PASS `ITER504V_BROADER_DOMAIN_LOCAL_D_CERTIFIES_COMPLETE_Q1_SCOPED` iff structure/provenance are valid and total unresolved terminal leaves across all 768 records are zero.

INCONCLUSIVE `ITER504V_BROADER_DOMAIN_LOCAL_D_INCONCLUSIVE_SCOPED` iff structure/provenance are valid and at least one record has an uncertified terminal leaf at depth exactly 3.

INVALID `ITER504V_BROADER_DOMAIN_INVALID` for implementation/provenance/cohort/channel/depth/partition/source/artifact/cross-environment contract invalidity. There is no model-level or physics-level scientific FAIL label for this gate.

## Firewall and next admissible action

Before complete source terminalization, inspect status/job/artifact metadata only. Do not consume leaf/slope/drift/certification/counterexample values, classify partial lanes, adaptively stop, or launch a competing same-object gate.

After source terminalization: prospectively freeze exact terminal artifact IDs/digests, then run exactly one separately frozen independent Critic against the immutable source artifacts. Expected terminal source inventory is 384 shard artifacts + 2 assemblies + 1 aggregate. Terminal Phase-B authority requires independent Critic closure.

If a valid unresolved record exists, freeze the smallest exact unresolved record/cell as the counterexample-first successor; do not increase `MAX_DEPTH` first.

## Retained lower authority

Iter504U remains scoped terminal `ITER504U_HELDOUT_LOCAL_D_GENERALIZES_SCOPED` for its frozen six-case object. No Iter504U or Iter504V result is promoted to all-domain/model-family/D7/global closure.

## Governance

`RQIR Core v1.0 = FROZEN`. `D7-S2 = NOT_CLOSED`; `D7-S3 = NOT_CLOSED`; `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`. Terminal D7 selectors and `EXISTING_SUFFICIENT / ADAPT_EXISTING / HYBRID_REQUIRED / NEW_REQUIRED` remain forbidden. Candidate Gravity inactive; Paper IV `NOT_YET_AUTHORIZED`.

`INCONCLUSIVE != FAIL`; `BLOCKED != FAIL`; `INVALID_IMPLEMENTATION != SCIENTIFIC_FAIL`; green CI != science; missing object/certificate != zero residual; scoped child result != family closure.

No authority exists for `ALL_KNOWN_MODELS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `QUANTUM_GRAVITY_SOLVED`, `UNIQUE_MECHANISM`, `D7_FULLY_CLOSED`, `CANDIDATE_GRAVITY_ESTABLISHED`, or `NEW_PHYSICS_FOUND`.

Preterminal handoff: `recovery/KMQGB_HANDOFF_ITER504V_PHASE_B_SOURCE_PRETERMINAL_2026-09-18.md`.

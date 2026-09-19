# Current Benchmark Front

Updated: 2026-09-19

Fresh repository `main` and fresh GitHub Actions state always outrank this navigation snapshot.

## Active scientific front

Gate: `ITER504V_BROADER_DOMAIN_COMPLETE_Q1_COVERAGE`.
Execution gate: `ITER504V_PHASE_B_SOURCE_EXECUTION`.

Authority chain:
- terminal Phase-A result `d03cae09c04638cb02412435a284cfd9acdf8406` -> `ITER504V_SENTINEL_LOCAL_D_NO_COUNTEREXAMPLE_SCOPED` for the frozen 16-state sentinel only;
- Phase-B prereg `e42caf47f9201d79cd89b79dc72b90f696e3ec5d`;
- static implementation Critic `eaa2d1ef84fe8370f33cec360233f60571f9bcd0` -> `PASS_SCOPED`;
- one-source execution authority `caf67585a9fad990dd90948df51839e6ed7cf891`;
- source launch/head `31fcdacffcc394e96b73917083281edb90d6753c`;
- authoritative source run `35405065903`.

Fresh state after the latest closure work: the source run remains nonterminal. The run endpoint reports `queued / conclusion=null`; source-lock job `105792998164` is terminal `success`; source case jobs remain active/queued. Fresh source artifact metadata is still empty. No case, leaf, slope, drift, certification, assembly, aggregate or counterexample scientific value has been consumed.

Current scientific status: `IN_PROGRESS_NOT_CLASSIFIED`.

## Frozen Phase-B object

Complete q=1 domain: causals `0to5,1to4,2to3` x blocks `0..3` x signed paths `0..3` x amplitude boxes `0..15` = 768 canonical records. Frozen contract: rho `0.35,0.9,1.6,2.7`; R `6,8,10,12`; all 243 channels; 384-bit precision; deterministic dyadic midpoint partition; `MAX_DEPTH=3`; local validated `D(J)` recomputed at every visited node; exact leaf/per-rho and unresolved-depth binding.

Execution topology remains 192 deterministic quartile shards per Python environment, Python 3.11 and 3.13, 384 source compute shards total, `fail-fast:false`, `max-parallel:12`.

Frozen source taxonomy remains unchanged:
- PASS `ITER504V_BROADER_DOMAIN_LOCAL_D_CERTIFIES_COMPLETE_Q1_SCOPED` iff the complete source object is structurally/provenance valid and total unresolved terminal leaves are zero;
- INCONCLUSIVE `ITER504V_BROADER_DOMAIN_LOCAL_D_INCONCLUSIVE_SCOPED` iff structurally/provenance valid and at least one terminal leaf is unresolved at depth exactly 3;
- INVALID `ITER504V_BROADER_DOMAIN_INVALID` for implementation/provenance/cohort/channel/depth/partition/source/artifact/cross-environment contract invalidity.

There is no model-level or physics-level scientific FAIL label for this gate.

## Terminal preterminal closure result — source-assembler binding

Gate: `ITER504V_PHASE_B_SOURCE_ASSEMBLER_BINDING_ADVERSARIAL_GATE`.

Terminal classification:

`ITER504V_PHASE_B_SOURCE_ASSEMBLER_BINDING_DEFECTS_VERIFIED_SCOPED`.

Authority/result chain:
- preregistration `93670f89688d9ad673fe35274892701a43f818d9`;
- implementation `0d76824a93b3650a8f7ab770940300db4c0eecb1`;
- workflow `d5f80fff18ced2f015b7223a6aab148a858fb983`;
- execution authority `74477c32d4227db60cfee307fb9e0ff563941682`;
- launch head `ec58663bbc7db7007a8a1be3442cdd460eaaeaf0`;
- Actions run `35417735617`, terminal `completed/success`;
- terminal result `research/results/ITER504V_PHASE_B_SOURCE_ASSEMBLER_BINDING_ADVERSARIAL_TERMINAL_2026-09-19.md`.

Both Python 3.11 and 3.13 produced byte-identical canonical results. The gate consumed no production science payload and did not classify source run `35405065903`.

Two outcome-independent verifier/authority-path defects were terminally reproduced against the exact immutable source assembler blob `f93bea2c32ed383a054beebb4d4b1c64fcbbd2c1`:

1. **Parent-inclusion dyadic identity is not bound.** A malformed serialized child/parent depth relation was independently detected by the gate oracle, while the exact source assembler still returned nominal PASS with `errors=[]`.
2. **Frozen shard/artifact placement is not bound.** Two case files were exchanged between quartile shard directories while their bytes/internal state IDs remained unchanged and the original `shard.json` declarations stayed in place. The independent shard oracle detected the mismatch, while the exact source assembler returned the same nominal PASS and the same complete 768-state decision projection as the coherent baseline.

Sensitivity controls showed that this is not a universally accepting validator: duplicate-state and leaf/per-rho contradictions were correctly classified INVALID.

These defects do **not** assert that the active producer emitted malformed artifacts. They establish that green source assembler/aggregate output alone cannot prove the full frozen authority contract.

## Firewall and next admissible action

While source run `35405065903` remains nonterminal: status/provenance checking only. Do not consume partial source science, adaptively stop, rerun the producer based on observed values, or launch a competing same-object scientific gate.

After complete source terminalization:

1. prospectively freeze every exact terminal source artifact ID/digest before opening substantive science payloads;
2. execute exactly one separately frozen independent Critic closure against those immutable artifacts;
3. that Critic must explicitly bind all 192 shard identities per environment to their exact four-record cohorts and validate each `shard.json` against physically contained case files;
4. that Critic must independently reconstruct every parent-inclusion child/parent dyadic edge and reject duplicate/orphan/malformed edges;
5. it must also retain all existing leaf/per-rho, unresolved-depth, exact-midpoint, source/cohort/channel and cross-environment controls.

Expected complete source inventory remains 384 shard artifacts + 2 assemblies + 1 aggregate. No producer rerun is authorized merely because the verifier-binding defects were found.

If a valid unresolved record exists after a fully valid independent closure, freeze the smallest exact unresolved record/cell as the counterexample-first successor; do not increase `MAX_DEPTH` first.

## Retained lower authority

Iter504U remains scoped terminal `ITER504U_HELDOUT_LOCAL_D_GENERALIZES_SCOPED` for its frozen six-case object. No Iter504U or Iter504V result is promoted to all-domain/model-family/D7/global closure.

## Governance

`RQIR Core v1.0 = FROZEN`. `D7-S2 = NOT_CLOSED`; `D7-S3 = NOT_CLOSED`; `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`. Terminal D7 selectors and `EXISTING_SUFFICIENT / ADAPT_EXISTING / HYBRID_REQUIRED / NEW_REQUIRED` remain forbidden. Candidate Gravity inactive; Paper IV `NOT_YET_AUTHORIZED`.

`INCONCLUSIVE != FAIL`; `BLOCKED != FAIL`; `INVALID_IMPLEMENTATION != SCIENTIFIC_FAIL`; green CI != science; missing object/certificate != zero residual; scoped child result != family closure.

No authority exists for `ALL_KNOWN_MODELS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `QUANTUM_GRAVITY_SOLVED`, `UNIQUE_MECHANISM`, `D7_FULLY_CLOSED`, `CANDIDATE_GRAVITY_ESTABLISHED`, or `NEW_PHYSICS_FOUND`.

Latest handoff: `recovery/KMQGB_HANDOFF_ITER504V_PHASE_B_ASSEMBLER_BINDING_ADVERSARIAL_TERMINAL_2026-09-19.md`.

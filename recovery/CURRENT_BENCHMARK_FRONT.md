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

Fresh state after the latest closure work: source run `35405065903` remains nonterminal. The run endpoint reports `queued / conclusion=null`; source-lock `105792998164` is terminal `success`; source case jobs remain active/queued. Fresh partial source artifact metadata count is now `6`. Those six artifacts were **not downloaded or opened** and no case, leaf, slope, drift, certification, assembly, aggregate or counterexample scientific value has been consumed.

Current scientific status: `IN_PROGRESS_NOT_CLASSIFIED`.

## Frozen Phase-B object

Complete q=1 domain: causals `0to5,1to4,2to3` x blocks `0..3` x signed paths `0..3` x amplitude boxes `0..15` = 768 canonical records. Frozen contract: rho `0.35,0.9,1.6,2.7`; R `6,8,10,12`; all 243 channels; 384-bit precision; deterministic dyadic midpoint partition; `MAX_DEPTH=3`; local validated `D(J)` recomputed at every visited node; exact leaf/per-rho and unresolved-depth binding.

Execution topology remains 192 deterministic quartile shards per Python environment, Python 3.11 and 3.13, 384 source compute shards total, `fail-fast:false`, `max-parallel:12`.

Frozen source taxonomy remains unchanged:
- PASS `ITER504V_BROADER_DOMAIN_LOCAL_D_CERTIFIES_COMPLETE_Q1_SCOPED` iff the complete source object is structurally/provenance valid and total unresolved terminal leaves are zero;
- INCONCLUSIVE `ITER504V_BROADER_DOMAIN_LOCAL_D_INCONCLUSIVE_SCOPED` iff structurally/provenance valid and at least one terminal leaf is unresolved at depth exactly 3;
- INVALID `ITER504V_BROADER_DOMAIN_INVALID` for implementation/provenance/cohort/channel/depth/partition/source/artifact/cross-environment contract invalidity.

There is no model-level or physics-level scientific FAIL label for this gate.

## Latest preterminal status/provenance closure

`ITER504V_PHASE_B_PRETERMINAL_SOURCE_STATUS_PROVENANCE_GATE` -> `ITER504V_PHASE_B_PRETERMINAL_SOURCE_PROVENANCE_CONSISTENT_SCOPED`.

- preregistration: `8737545156b2a64a514e28652bfe761a660cf575`;
- exact source object: run `35405065903`, attempt 1, head `31fcdacffcc394e96b73917083281edb90d6753c`;
- frozen first-page job snapshot: 30 jobs = 7 completed/success, 17 in progress, 6 queued, 0 visible failed/cancelled;
- exposed artifact metadata: 6 partial shard artifacts, all non-expired, all with GitHub SHA256 digests and exact run/head binding;
- source artifact bytes opened/downloaded: false;
- partial scientific payload consumed: false;
- canonical result SHA256: `6f9cff143a11842f8c2bd349bc58fc4d7c2ec87944fdb0318ad9c0e03e81d4ad`.

This is a metadata/provenance closure only. It does not classify Phase-B science and does not relax the terminal artifact-freeze requirement.

## Terminal preterminal closure — source assembler binding

`ITER504V_PHASE_B_SOURCE_ASSEMBLER_BINDING_ADVERSARIAL_GATE` -> `ITER504V_PHASE_B_SOURCE_ASSEMBLER_BINDING_DEFECTS_VERIFIED_SCOPED`.

Independent Critical Review commit `c641e1083473000307c3399c4c1e51e8194cb43c` = `CONFIRMED_SCOPED`.

Two exact-source-assembler authority gaps remain mandatory future-Critic obligations:

1. independently reconstruct and bind every serialized parent-inclusion child/parent dyadic edge;
2. bind every expected artifact/shard identity plus `shard.json` to the exact frozen four physical case records.

These are verifier defects only, not evidence that active source artifacts are malformed.

## Terminal preterminal closure — source aggregate binding

Gate: `ITER504V_PHASE_B_SOURCE_AGGREGATE_BINDING_ADVERSARIAL_GATE`.

Terminal classification:

`ITER504V_PHASE_B_SOURCE_AGGREGATE_BINDING_DEFECTS_VERIFIED_SCOPED`.

Authority/result chain:
- preregistration `04a47f859323bea69472f142ec1a2f4b97e5df0b`;
- implementation `31d58bec122ca0995f576660b3dfeeda15b0ba3d`;
- workflow `0485a04ab4646b6e80df7c7555db4b3b5bcddd72`;
- execution authority `32f9f5cbf2d95fb31938b0d163a446a8fa43549a`;
- launch head `2514581ed3d93bbdc9ccefd8383627e8cb1e7e28`;
- Actions run `35420614607`, terminal `completed/success`;
- terminal result `research/results/ITER504V_PHASE_B_SOURCE_AGGREGATE_BINDING_ADVERSARIAL_TERMINAL_2026-09-19.md`;
- canonical lane result SHA256 `6c62ffe7e6d75d2246e5b25bedd971ba08541fd41d06a4e98e1f1bad32ce686b`;
- frozen gate decision SHA256 `bfd4a7d6b853b1a6c885086bf1851c0923187aaaa6b36044eec0042a9a310f63`.

Both Python 3.11 and 3.13 were byte-identical and all frozen positive/sensitivity controls passed. Against exact immutable source aggregate blob `ae1932a7cdd98a1cc74f1b2f07bc295e0c097274`, three additional outcome-independent verifier/authority-path defects were reproduced:

1. source PASS classification is not independently rebound to zero-unresolved evidence; a synthetic pair with one unresolved state, total unresolved `1`, and the matching counterexample was still accepted as source PASS with `errors=[]`;
2. `decision_projection_sha256_by_state` key set is not independently rebound to the canonical 768-state identity; one canonical key could be replaced by a foreign key while preserving cardinality 768 and cross-environment equality and still receive source PASS;
3. `case_file_sha256` key set is not independently rebound to the canonical 768-state identity; one canonical provenance key could be replaced by a foreign key while preserving cardinality 768 and still receive source PASS.

Sensitivity controls rejected cross-environment classification, state-identity and projection-map disagreements, so the aggregate is not universally accepting.

This result consumed no production science and did not classify source run `35405065903`.

## Firewall and next admissible action

While source run `35405065903` remains nonterminal: status/provenance checking only. Do not consume partial source science, adaptively stop, rerun the producer based on observed values, or launch a competing same-object scientific gate.

After complete source terminalization, prospectively freeze every exact terminal source artifact ID/digest before opening substantive science payloads, then execute exactly one separately frozen independent Critic closure against those immutable artifacts.

That Critic must independently satisfy all now-verified authority obligations:

1. bind every expected shard/artifact identity and `shard.json` to exactly its frozen four physical case records and prove exactly 192 unique complete shards per environment;
2. reconstruct every parent-inclusion child/parent dyadic edge and reject malformed/duplicate/orphan records;
3. rebind source PASS/INCONCLUSIVE classification to the independently recomputed unresolved evidence;
4. rebind decision-projection map keys and projection sequence to the exact canonical 768-state identity;
5. rebind case-provenance keys/content hashes to the exact canonical 768-state identity;
6. retain all inherited source/cohort/channel/precision/R/rho/tree/leaf/per-rho/unresolved-depth/cross-environment controls.

Expected complete source inventory remains 384 shard artifacts + 2 assemblies + 1 aggregate. No producer rerun is authorized merely because verifier-binding defects were found.

If a valid unresolved record exists after a fully valid independent closure, freeze the smallest exact unresolved record/cell as the counterexample-first successor; do not increase `MAX_DEPTH` first.

## Retained lower authority

Iter504U remains scoped terminal `ITER504U_HELDOUT_LOCAL_D_GENERALIZES_SCOPED` for its frozen six-case object. No Iter504U or Iter504V result is promoted to all-domain/model-family/D7/global closure.

## Governance

`RQIR Core v1.0 = FROZEN`. `D7-S2 = NOT_CLOSED`; `D7-S3 = NOT_CLOSED`; `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`. Terminal D7 selectors and `EXISTING_SUFFICIENT / ADAPT_EXISTING / HYBRID_REQUIRED / NEW_REQUIRED` remain forbidden. Candidate Gravity inactive; Paper IV `NOT_YET_AUTHORIZED`.

`INCONCLUSIVE != FAIL`; `BLOCKED != FAIL`; `INVALID_IMPLEMENTATION != SCIENTIFIC_FAIL`; green CI != science; missing object/certificate != zero residual; scoped child result != family closure.

No authority exists for `ALL_KNOWN_MODELS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `QUANTUM_GRAVITY_SOLVED`, `UNIQUE_MECHANISM`, `D7_FULLY_CLOSED`, `CANDIDATE_GRAVITY_ESTABLISHED`, or `NEW_PHYSICS_FOUND`.

Latest handoff: `recovery/KMQGB_HANDOFF_ITER504V_PHASE_B_PRETERMINAL_SOURCE_STATUS_PROVENANCE_2026-09-19.md`.

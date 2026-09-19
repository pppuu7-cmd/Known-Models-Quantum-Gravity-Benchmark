# Independent Critical Review — Iter504V Phase-B source-assembler binding adversarial gate

Date: 2026-09-19
Lane: independent KMQGB Critical Review / Verification
Verdict: `CONFIRMED_SCOPED`

## Result reviewed

Exactly one bounded terminal methodology/authority-path result:

- gate: `ITER504V_PHASE_B_SOURCE_ASSEMBLER_BINDING_ADVERSARIAL_GATE`;
- preregistration: `93670f89688d9ad673fe35274892701a43f818d9`;
- gate implementation: `0d76824a93b3650a8f7ab770940300db4c0eecb1`;
- workflow: `d5f80fff18ced2f015b7223a6aab148a858fb983`;
- execution authority: `74477c32d4227db60cfee307fb9e0ff563941682`;
- launch head: `ec58663bbc7db7007a8a1be3442cdd460eaaeaf0`;
- authoritative Actions run: `35417735617`, attempt 1;
- historical terminal classification: `ITER504V_PHASE_B_SOURCE_ASSEMBLER_BINDING_DEFECTS_VERIFIED_SCOPED`;
- exact source assembler under review: `code/iter504v_phase_b_assemble.py`, blob `f93bea2c32ed383a054beebb4d4b1c64fcbbd2c1`, from immutable Phase-B source launch head `31fcdacffcc394e96b73917083281edb90d6753c`.

The active scientific source run `35405065903` remains nonterminal and is not classified by this review. No partial Phase-B source scientific payload was consumed.

## Preregistration chronology and frozen contract

The adversarial gate was prospectively frozen before result. Its hypothesis is explicitly verifier-only: test whether the exact source assembler accepts either or both of two structurally/provenance-invalid synthetic inventories while preserving nominal source PASS:

A. malformed serialized parent-inclusion child/parent dyadic identity with inclusion booleans and leaf decisions held fixed;

B. cross-quartile shard/artifact placement mismatch where case bytes/internal state IDs remain unchanged and the complete 768-state union remains exact.

The preregistration also freezes a coherent complete 768-state baseline, independent parent-tree and shard-cover oracles, duplicate-state sensitivity, leaf/per-rho sensitivity, exact Python 3.11/3.13 canonical agreement, and the claim ceiling. No production science is part of the gate object.

`PREREG_CHECK = PASS`.

## Object/source identity

The workflow source-lock binds the exact preregistration, gate script, exact source assembler blob, campaign manifest blob and execution authority. It explicitly forbids production-science consumption and competing science execution.

The gate calls the source assembler as an external subprocess through the exact repository path `code/iter504v_phase_b_assemble.py`; the source-lock fixes that file to blob `f93bea2c32ed383a054beebb4d4b1c64fcbbd2c1`.

Independent source inspection confirms the two tested omissions in that blob:

1. `validate_case()` verifies inclusion record count, R/rho grid and componentwise boolean shapes, but it does not reconstruct/validate the serialized inclusion `depth`, `parent_depth`, child interval and parent interval as an exact dyadic parent-child edge.
2. assembler discovery recursively reads `case-*.json` and keys by internal `state_id`; it does not consume `shard.json` and does not bind case bytes to a frozen `(python, causal, block, path, quartile)` artifact/shard identity.

`OBJECT_IDENTITY_CHECK = PASS_SCOPED` for the bounded gate object.
`SOURCE/REALIZATION_CHECK = PASS_SCOPED` for the exact source assembler under test.

## Actions provenance

Run `35417735617` is terminal `completed/success` on launch head `ec58663bbc7db7007a8a1be3442cdd460eaaeaf0`.

Fresh artifact metadata:

- Python 3.11 artifact `10575754497`, digest `sha256:5e0dae63cc7a3d3fc98016ca00e60b61c9a2dc3ce124698c839004e9820c87aa`;
- Python 3.13 artifact `10575569736`, digest `sha256:bca4cf613d1c031c8b6c7c6f37c09793fde434bded90fe38bb1903579cc365df`;
- aggregate artifact `10576178004`, digest `sha256:cc2d6a49f72db79b2ff8fb4f52db20650b5b2e3beaf672554883bcc8873e230c`.

The independent Critical Review downloaded all three ZIPs and recomputed SHA256 locally. All three hashes match the fresh GitHub Actions digests exactly.

The two lane `result.json` files are byte-identical with SHA256:

`69029333114a3fda2fd208f166055896df0f259c57704682b4e28c7118d87fbf`.

The aggregate records the same result hash and `cross_environment_byte_identical=true`. The frozen decision SHA256 is:

`161b800d9d161c8067c6241052320139180bb505b4752ca2224186f4d3f35c9a`.

`PROVENANCE_CHECK = PASS`.
`SAME_REALIZATION_CHECK = PASS_SCOPED` for the bounded synthetic gate execution.

## Counterexample-first verification

### Baseline / sensitivity controls

The exact assembler accepts the coherent synthetic complete-q1 baseline with:

- `errors=[]`;
- `total_cases=768`;
- `total_unresolved_leaves=0`;
- `ITER504V_BROADER_DOMAIN_LOCAL_D_CERTIFIES_COMPLETE_Q1_SCOPED`.

Independent baseline parent-tree and shard-cover oracles are clean.

The exact assembler is not trivially accepting:

- duplicate internal state identity is rejected as `ITER504V_BROADER_DOMAIN_INVALID` with `duplicate_states`, `case_set`, `case_count`, `projection_count`;
- leaf/per-rho contradiction is rejected as `ITER504V_BROADER_DOMAIN_INVALID`, including `leaf_per_rho_binding` and `premature_unresolved_leaf_depth`.

### Candidate A — parent-inclusion dyadic identity

The frozen mutation changes only one inclusion record's serialized `parent_depth` so the child no longer satisfies `child.depth = parent.depth + 1`; inclusion booleans and leaf decisions remain unchanged.

The independent oracle detects `0:depth`.

The exact source assembler nevertheless returns:

- return code `0`;
- `errors=[]`;
- 768 cases;
- zero unresolved leaves;
- nominal `ITER504V_BROADER_DOMAIN_LOCAL_D_CERTIFIES_COMPLETE_Q1_SCOPED`.

Therefore candidate A is independently confirmed as a real verifier-binding defect.

### Candidate B — frozen shard/artifact placement

The frozen mutation swaps the complete bytes of case `x00` and `x04` between q0 and q1 physical shard directories for the same `(causal, block, path)`, leaving both internal state IDs and both original `shard.json` declarations unchanged.

The independent shard oracle detects two physical shard/content mismatches.

The exact source assembler nevertheless returns nominal PASS with no errors, the same complete 768-state decision projection as baseline, and the same assembly payload SHA256 as baseline:

- projection SHA256 `ddfe9b630d46a8096fac41f79928f6688d9a4fdf39e3897fdafa6d2d58e77fbf`;
- assembly payload SHA256 `1f5daa984e9ed370ee3dac250c4fe796b338aad62e27202e9a08c32eca161f73`.

Therefore candidate B is independently confirmed as a real provenance/topology verifier-binding defect.

`COUNTEREXAMPLE_ATTEMPTS = A SUCCESS; B SUCCESS; duplicate-state and leaf-binding sensitivity controls reject as required`.

## Numerical/statistical scope

This gate is exact/nonstatistical and synthetic. No physical slope, drift, certification, unresolved-state or other substantive Phase-B source value was consumed.

`NUMERICAL/STATISTICAL_CHECK = PASS_EXACT_NONSTATISTICAL_SCOPED`.

## Overclaim / interpretation ceiling

The terminal result is correctly scoped. It does not assert that the active producer emitted malformed parent-inclusion records or misplaced shard contents. It does not classify source run `35405065903`, does not convert any source result to scientific FAIL, and does not alter the frozen Phase-B PASS/INCONCLUSIVE taxonomy.

No all-domain/model-family/D7/Candidate Gravity/Paper IV/global quantum-gravity claim follows.

`OVERCLAIM_CHECK = PASS`.

## Verdict

`CONFIRMED_SCOPED`.

The independent Critical Review confirms the historical bounded methodology classification `ITER504V_PHASE_B_SOURCE_ASSEMBLER_BINDING_DEFECTS_VERIFIED_SCOPED`: both preregistered authority-path counterexamples are real against the exact immutable source assembler, the controls are live, the two Python lanes are byte-identical, and provenance is intact.

This is a scoped confirmation of verifier defects only, not a scientific verdict on the nonterminal Phase-B source execution.

## Current source-run firewall

Fresh Actions state for source run `35405065903` remains nonterminal (`queued`, `conclusion=null`). Fresh source-run artifact inventory is empty at this review. Therefore no source case/leaf/slope/drift/certification/assembly/aggregate value is admissible for scientific review yet.

## Handoff

- `RESULT_REVIEWED = ITER504V_PHASE_B_SOURCE_ASSEMBLER_BINDING_ADVERSARIAL_GATE / run 35417735617`
- `PREREG_CHECK = PASS`
- `OBJECT_IDENTITY_CHECK = PASS_SCOPED`
- `SOURCE/REALIZATION_CHECK = PASS_SCOPED`
- `PROVENANCE_CHECK = PASS`
- `SAME_REALIZATION_CHECK = PASS_SCOPED`
- `NUMERICAL/STATISTICAL_CHECK = PASS_EXACT_NONSTATISTICAL_SCOPED`
- `COUNTEREXAMPLE_ATTEMPTS = parent-inclusion malformed dyadic edge SUCCESS; shard/artifact placement mismatch SUCCESS; duplicate-state sensitivity PASS; leaf/per-rho sensitivity PASS`
- `OVERCLAIM_CHECK = PASS`
- `VERDICT = CONFIRMED_SCOPED`
- `QUALIFICATIONS = verifier/authority-path defects only; no evidence active producer emitted either defect; source run 35405065903 remains nonterminal and unclassified`
- `UPDATED_STATE = two Phase-B source-assembler binding defects independently terminally confirmed; source science remains IN_PROGRESS_NOT_CLASSIFIED`
- `NEXT_ADMISSIBLE_GATE = after complete source terminalization, prospectively freeze exact terminal artifact IDs/digests before substantive science consumption and execute one separately frozen independent Critic that binds all 192 shard identities per environment to exact four-case physical contents and reconstructs every parent-inclusion child/parent dyadic edge, while retaining leaf/per-rho, unresolved-depth, exact-midpoint, source/cohort/channel and cross-environment controls. No producer rerun is authorized merely because these verifier defects exist.`

Governance retained: `RQIR Core v1.0 = FROZEN`; `BLOCKED != FAIL`; finite certificate != universal theorem; scoped child != family closure; D7 required subgates remain unclosed; terminal selectors forbidden; Candidate Gravity inactive.
# KMQGB Critical Review — Iter504V Phase-B source aggregate binding adversarial gate

Date: 2026-09-19
Lane: independent KMQGB Critical Review / Verification
Result reviewed: `ITER504V_PHASE_B_SOURCE_AGGREGATE_BINDING_DEFECTS_VERIFIED_SCOPED`

## VERDICT

`CONFIRMED_SCOPED`

The terminal methodology result is supported by the prospectively frozen contract, exact source-object identity, terminal Actions provenance, independent cross-environment replay and live sensitivity controls. This review does not classify source run `35405065903` and does not consume its scientific payload.

## Chronology / preregistration

PASS.

The exact sequence is prospective:

- gate preregistration `04a47f859323bea69472f142ec1a2f4b97e5df0b`;
- implementation `31d58bec122ca0995f576660b3dfeeda15b0ba3d`;
- workflow `0485a04ab4646b6e80df7c7555db4b3b5bcddd72`;
- execution authority `32f9f5cbf2d95fb31938b0d163a446a8fa43549a`;
- one launch/head `2514581ed3d93bbdc9ccefd8383627e8cb1e7e28`;
- terminal Actions run `35420614607`;
- result/hashes/terminalization only after terminal execution.

No frozen PASS/FAIL/BLOCKED/INVALID rule was changed after result observation.

## Exact object identity

PASS.

The gate explicitly source-locked and runtime-rehashed the exact immutable source aggregate:

`code/iter504v_phase_b_aggregate.py` -> blob `ae1932a7cdd98a1cc74f1b2f07bc295e0c097274`.

That is the aggregate blob frozen by Phase-B execution authority `caf67585a9fad990dd90948df51839e6ed7cf891` and used by source launch head `31fcdacffcc394e96b73917083281edb90d6753c`.

The harness calls the source aggregate as an external subprocess; it does not substitute a local reimplementation for the object under test.

## Production-science firewall

PASS.

The adversarial workflow does not download artifacts from active source run `35405065903`. Both canonical lane results record `production_science_consumed=false` and `source_run_classified=false`. Fresh source-run inspection used only run/job/artifact metadata; the two currently visible partial source artifacts were not downloaded or opened.

## Artifact / cross-environment provenance

PASS.

Authoritative run `35420614607` is terminal `completed/success`. Jobs source-lock `105837471138`, Python 3.11 `105837491172`, Python 3.13 `105837491163`, and aggregate `105837508143` all completed success.

GitHub artifact digests:

- 3.11 `10577352415`: `sha256:8fe0d0cfe1905428952c1a82b618866c1ce56c56faaf424151fc8cbb32a5aae0`;
- 3.13 `10577866791`: `sha256:8fe0d0cfe1905428952c1a82b618866c1ce56c56faaf424151fc8cbb32a5aae0`;
- aggregate `10576787892`: `sha256:feda26c081203f1640be3eab91ba4461ad2e741f7fc94ff318db2a1e560ed95a`.

Independent ZIP rehashes match all three GitHub digests exactly. Python 3.11 and 3.13 `result.json` and `returncode.txt` are byte-identical. Lane result SHA256 is `6c62ffe7e6d75d2246e5b25bedd971ba08541fd41d06a4e98e1f1bad32ce686b`; decision SHA256 is `bfd4a7d6b853b1a6c885086bf1851c0923187aaaa6b36044eec0042a9a310f63`.

## Control audit

PASS.

Positive controls demonstrate expected nominal semantics:

- coherent zero-unresolved pair -> exact aggregate PASS;
- coherent one-unresolved pair -> exact aggregate INCONCLUSIVE.

Negative controls demonstrate live rejection rather than universal acceptance:

- cross-environment classification disagreement -> source INVALID;
- cross-environment state-identity disagreement -> source INVALID;
- cross-environment projection-map disagreement -> source INVALID.

Therefore candidate acceptance is not explained by a dead or trivially permissive test path.

## Candidate A — classification / unresolved binding

CONFIRMED.

The candidate contains a coherent unresolved map with one unresolved canonical state, `total_unresolved_leaves=1`, and the matching counterexample set, while both assemblies claim source PASS. The independent oracle flags `classification_unresolved_binding`.

The exact source aggregate nevertheless returns `ITER504V_BROADER_DOMAIN_LOCAL_D_CERTIFIES_COMPLETE_Q1_SCOPED`, `errors=[]`, return code 0 and exact cross-environment agreement.

Static source inspection independently explains this outcome: the aggregate compares classification and unresolved evidence across environments but does not recompute classification from unresolved evidence.

## Candidate B — decision-projection canonical key binding

CONFIRMED.

The candidate preserves the exact canonical `state_ids` list and map cardinality 768 but replaces one canonical projection-map key with a foreign noncanonical key in both environments. The independent oracle flags `projection_key_set`.

The exact source aggregate accepts source PASS with no errors. Static inspection explains the acceptance: it checks only projection-map cardinality and cross-environment equality, while the separately supplied projection-sequence scalar is compared across environments but not recomputed from the map.

This is a verifier/authority binding defect. It does not assert that the frozen source assembler itself generates such a map in normal execution.

## Candidate C — case-provenance canonical key binding

CONFIRMED.

The candidate preserves `case_file_sha256` cardinality 768 but replaces one canonical provenance key with a foreign key in both environments. The independent oracle flags `provenance_key_set`.

The exact aggregate accepts source PASS with no errors. Static source inspection confirms that only provenance-map cardinality is checked; canonical keys/content-to-state binding is not independently reconstructed.

Again this is an aggregate authority-path omission, not evidence that the active producer emitted malformed provenance.

## Overclaim audit

PASS.

The terminal result is appropriately limited to synthetic verifier/authority-path defects against one exact aggregate blob. It does not classify active Phase-B science, does not promote Phase A/U/V to model-family or D7 closure, and makes no global-QG claim.

## Downstream consequence

The result materially tightens the mandatory independent Critic contract after source terminalization. A valid terminal Critic may not trust green source aggregate semantics. It must independently:

1. bind each artifact/shard identity and `shard.json` to its exact four physical cases;
2. reconstruct every parent-inclusion child/parent dyadic edge;
3. recompute PASS/INCONCLUSIVE from independently validated unresolved evidence;
4. regenerate canonical projection keys/sequence for all 768 states;
5. regenerate canonical provenance keys and bind content hashes to those states;
6. retain all inherited source/cohort/channel/tree/leaf/unresolved-depth/cross-environment controls.

No source rerun follows merely from these verifier defects.

## CLAIM_CEILING

`CONFIRMED_SCOPED` applies only to the three preregistered source-aggregate verifier-binding omissions. Source run `35405065903` remains `IN_PROGRESS_NOT_CLASSIFIED` until complete terminalization and separately frozen Critic closure.

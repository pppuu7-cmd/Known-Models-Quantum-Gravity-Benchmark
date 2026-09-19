# ITER504V Phase-B source-assembler binding adversarial gate — terminal result

Date: 2026-09-19
Gate: `ITER504V_PHASE_B_SOURCE_ASSEMBLER_BINDING_ADVERSARIAL_GATE`

## Terminal classification

`ITER504V_PHASE_B_SOURCE_ASSEMBLER_BINDING_DEFECTS_VERIFIED_SCOPED`

This is a verifier/authority-path result only. It is **not** a scientific classification of Phase-B source run `35405065903` and consumed no production science payload.

## Frozen authority

- preregistration commit: `93670f89688d9ad673fe35274892701a43f818d9`;
- gate implementation commit: `0d76824a93b3650a8f7ab770940300db4c0eecb1`;
- workflow commit: `d5f80fff18ced2f015b7223a6aab148a858fb983`;
- gate authority commit: `74477c32d4227db60cfee307fb9e0ff563941682`;
- gate authority blob: `acfdaf3f2a009aab360abea6e9e60246f117faa8`;
- launch head: `ec58663bbc7db7007a8a1be3442cdd460eaaeaf0`;
- exact source assembler blob: `f93bea2c32ed383a054beebb4d4b1c64fcbbd2c1`;
- immutable source launch head under review: `31fcdacffcc394e96b73917083281edb90d6753c`.

## Authoritative execution

Actions run `35417735617`, attempt 1: `completed/success`.

Jobs:

- source-lock `105829513588`: success;
- Python 3.11 `105829537677`: success;
- Python 3.13 `105829537739`: success;
- aggregate `105829568772`: success.

The Python 3.11 and 3.13 canonical `result.json` files are byte-identical.

- canonical result SHA256: `69029333114a3fda2fd208f166055896df0f259c57704682b4e28c7118d87fbf`;
- decision SHA256: `161b800d9d161c8067c6241052320139180bb505b4752ca2224186f4d3f35c9a`.

Artifacts and independently rechecked ZIP hashes:

- `10575754497` `iter504v-phaseb-assembler-binding-3.11`: `sha256:5e0dae63cc7a3d3fc98016ca00e60b61c9a2dc3ce124698c839004e9820c87aa`;
- `10575569736` `iter504v-phaseb-assembler-binding-3.13`: `sha256:bca4cf613d1c031c8b6c7c6f37c09793fde434bded90fe38bb1903579cc365df`;
- `10576178004` `iter504v-phaseb-assembler-binding-aggregate`: `sha256:cc2d6a49f72db79b2ff8fb4f52db20650b5b2e3beaf672554883bcc8873e230c`.

For all three, independently computed ZIP SHA256 exactly equals the GitHub artifact digest.

## Positive and sensitivity controls

All frozen controls passed.

The coherent 768-record synthetic complete-q1 corpus was accepted by the exact source assembler with:

- `errors=[]`;
- `total_cases=768`;
- `total_unresolved_leaves=0`;
- classification `ITER504V_BROADER_DOMAIN_LOCAL_D_CERTIFIES_COMPLETE_Q1_SCOPED`.

Independent baseline parent-tree and shard-cover oracles were clean.

The exact assembler also retained expected sensitivity:

- duplicate internal state identity -> `ITER504V_BROADER_DOMAIN_INVALID`, with `duplicate_states`, `case_set`, `case_count`, `projection_count`;
- leaf/per-rho contradiction -> `ITER504V_BROADER_DOMAIN_INVALID`, including `leaf_per_rho_binding` and `premature_unresolved_leaf_depth` errors.

Therefore the verified gaps are specific and are not explained by a trivially accepting validator.

## Verified defect A — serialized parent-inclusion identity is not bound

A single coherent inclusion record was changed only so that its serialized parent depth no longer satisfies `child.depth = parent.depth + 1`. The independent frozen oracle detected `0:depth`.

The exact source assembler nevertheless returned:

- `errors=[]`;
- 768 cases;
- zero unresolved leaves;
- nominal `ITER504V_BROADER_DOMAIN_LOCAL_D_CERTIFIES_COMPLETE_Q1_SCOPED`.

Thus the source assembler validates inclusion counts/grids/booleans but does not independently reconstruct and bind the serialized child/parent dyadic edge identity before classification.

This does not assert that the actual producer emitted a malformed inclusion edge.

## Verified defect B — frozen shard/artifact placement is not bound

One case file from q0 and one from q1 were physically exchanged while both case payloads and their internal state IDs were left unchanged and both original `shard.json` declarations were left in place.

The independent frozen shard oracle detected two shard/content mismatches. The complete internal 768-state union remained unchanged.

The exact source assembler nevertheless returned the same nominal PASS, no errors, and the exact same decision projection as the coherent baseline:

`ddfe9b630d46a8096fac41f79928f6688d9a4fdf39e3897fdafa6d2d58e77fbf`.

The baseline and shard-permuted assembly payload SHA256 are also identical:

`1f5daa984e9ed370ee3dac250c4fe796b338aad62e27202e9a08c32eca161f73`.

Therefore the source assembler does not bind case bytes to their frozen source artifact/shard identity and does not consume `shard.json` when validating the complete 768-state union.

This does not assert that the actual Actions source run misplaced any case.

## New durable fact

Two distinct outcome-independent authority-path gaps are now terminally reproduced against the exact immutable Phase-B source assembler:

1. parent-inclusion child/parent dyadic identity can be malformed without source-assembler rejection;
2. case placement can violate the frozen 192-shard partition without source-assembler rejection, even with an unchanged 768-state scientific decision projection.

The active source execution may still be perfectly correct. These defects mean that green source assembly/aggregate alone cannot establish terminal Phase-B authority.

## Claim ceiling

`ITER504V_PHASE_B_SOURCE_ASSEMBLER_BINDING_DEFECTS_VERIFIED_SCOPED` is not scientific FAIL, not source-run INVALID, and not evidence of a physical counterexample.

It does not alter the Phase-B frozen PASS/INCONCLUSIVE taxonomy, does not classify run `35405065903`, and authorizes no all-domain/model-family/D7/Candidate Gravity/Paper IV/global quantum-gravity conclusion.

## Required downstream closure

When source run `35405065903` becomes completely terminal, the separately frozen independent Critic must, before accepting any Phase-B terminal authority:

1. bind every exact artifact ID/digest to the expected `(python, causal, block, path, quartile)`;
2. parse and validate each exact `shard.json`;
3. require each shard's physical case set to equal exactly its frozen four-state cohort;
4. prove exactly 192 unique shards per Python environment and exact complete cover;
5. independently reconstruct every serialized parent-inclusion child/parent dyadic edge and reject duplicate/orphan/malformed edges;
6. retain all pre-existing leaf/per-rho, unresolved-depth, exact-midpoint, source/cohort/channel and cross-environment controls.

No producer rerun is authorized merely because these verifier-binding defects were found.

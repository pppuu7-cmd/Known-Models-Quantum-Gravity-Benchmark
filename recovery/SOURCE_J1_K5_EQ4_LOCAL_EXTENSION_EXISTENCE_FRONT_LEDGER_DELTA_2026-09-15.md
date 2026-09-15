# Recovery/front ledger delta — Eq. (4) local full-collision extension existence

Date: 2026-09-15

## New terminal scoped result

`SOURCE_J1_K5_EQ4_LOCAL_EXTENSION_EXISTS_UNIQUENESS_OPEN_SCOPED`

Authority:

- prereg: `research/SOURCE_J1_K5_EQ4_LOCAL_EXTENSION_EXISTENCE_PREREG_2026-09-15.md`
- prereg commit: `43a4cb12289509a2b4f74192aa709e0c0c6c240e`
- implementation: `code/source_j1_k5_eq4_local_extension_existence_certificate.py`
- implementation commit: `6a503bacbabd36ac81a69e091f4322be651418cc`
- workflow head: `1c7d20683414844d4ccf4387245e80db9d303698`
- result: `research/SOURCE_J1_K5_EQ4_LOCAL_EXTENSION_EXISTENCE_RESULT_2026-09-15.md`
- result commit: `99e52495a746db07cd371215227a2066d8445dad`
- run: `34916570152`
- source-lock job: `104215364399` success
- exact-premise job: `104215410266` success
- artifact: `10375929193`
- digest: `sha256:644dc49c98952a9158326bef9af1633d99dc654cc06ef47ca44145ea54193eab`

Theorem-level scoped conclusion:

- frozen conic full-collision punctured distribution has finite transverse scaling degree 30 in codimension 12;
- finite-scaling-degree extension theorem implies at least one local same-scaling distributional extension exists;
- ordinary radial absolute exponent remains -19, so absolute-integral failure and distributional existence are distinct;
- automatic uniqueness does not follow because `30 >= 12`;
- normal ambiguity order is bounded through 18;
- explicit `delta_N`/EPRL-preserving counterterm witness shows off-collision agreement + scaling ceiling + K5 permutation covariance + EPRL sign sum remain insufficient for uniqueness.

Classification boundary:

- `LOCAL_DISTRIBUTIONAL_EXISTENCE = CERTIFIED_SCOPED`;
- `SOURCE_CANONICAL_UNIQUENESS = NOT_YET_CERTIFIED`.

## Active numerical front unchanged

Iter504 remains authoritative and must not be duplicated:

- run `34907349374`;
- source-lock success;
- all 12 point-lanes success;
- centered shards active/queued;
- no terminal aggregate consumed at the last verified check.

## Independent collision-partition stream unchanged

Iter461 remains unresolved and must not be duplicated:

- branch `research/iter461-k5-collision-partitions`;
- head `05c7f87c8519349057332bf90021f1128e1eefc3c`;
- run `34748503239`;
- last verified queued/no jobs.

## Authorized analytical next gate

`SOURCE_J1_K5_EQ4_SOURCE_NORMALIZATION_SELECTION_GATE`

The next gate must identify and test a source-derived uniqueness condition beyond the already-insufficient combination of:

- off-collision agreement;
- same scaling degree;
- K5 permutation covariance;
- EPRL independent-sign sum rule.

A new auxiliary regulator is not source authority unless source-equivalence is separately proved.

## Global locks unchanged

- `RQIR Core v1.0 = FROZEN`.
- `D7-S2 = NOT_CLOSED`.
- `D7-S3 = NOT_CLOSED`.
- `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`.
- terminal selectors forbidden.
- Candidate Gravity inactive.
- KMQGB remains downstream of pinned DSIR authority.

# Recovery/front ledger delta — one-wedge Toller uniqueness versus joint K5 extension

Date: 2026-09-15

## New terminal scoped result

`SOURCE_J1_K5_ONE_WEDGE_TOLLER_UNIQUENESS_INSUFFICIENT_FOR_JOINT_EXTENSION_SCOPED`

Authority:

- prereg: `research/SOURCE_J1_K5_ONE_WEDGE_UNIQUENESS_VS_JOINT_EXTENSION_PREREG_2026-09-15.md`
- prereg commit: `88c3d04a627b4cbef29c6b3246052a58508aaa0a`
- implementation: `code/source_j1_k5_one_wedge_uniqueness_vs_joint_extension_certificate.py`
- implementation commit: `fa97e038e5b417271dfc4a396c89f5fe2f1cce0d`
- workflow head: `082bbae295f857dd61af54479ded2ca6be0ed62e`
- result: `research/SOURCE_J1_K5_ONE_WEDGE_UNIQUENESS_VS_JOINT_EXTENSION_RESULT_2026-09-15.md`
- result commit: `4b8abb10d89e36801012972ec84f34eb722a5b49`
- run: `34916807591`
- source-lock job: `104216105796` success
- exact-certificate job: `104216135656` success
- artifact: `10376397688`
- digest: `sha256:dc7780208270cdcbb623171914ee86936523f245d7c4c509f018a72a62b1e8a1`

Certified level separation:

- all 10 individual Toller factor pairs are unchanged between joint extension families `E` and `E'`;
- all published one-wedge uniqueness conditions therefore remain unchanged;
- the joint extension changes by `c(kappa) delta_N` supported only on the full-collision submanifold;
- off-collision restrictions agree;
- scaling ceiling, EPRL sign sum and S5 covariance remain satisfied;
- causal sector shifts nontrivially.

Interpretation:

- the published uniqueness theorem for individual Toller matrices does not by itself fix the joint K5 collision extension;
- a genuinely joint vertex/product condition is required for source-canonical uniqueness;
- no claim is made that such a joint condition does not exist.

## Active numerical front unchanged

Iter504 remains authoritative and must not be duplicated:

- run `34907349374`;
- source-lock success;
- all 12 point-lanes success;
- centered shards active/queued at last verified check;
- no terminal aggregate consumed.

## Independent collision-partition stream unchanged

Iter461 remains unresolved and must not be duplicated:

- branch `research/iter461-k5-collision-partitions`;
- head `05c7f87c8519349057332bf90021f1128e1eefc3c`;
- run `34748503239`;
- last verified queued/no jobs.

## Authorized analytical frontier

`SOURCE_J1_K5_EQ4_JOINT_NORMALIZATION_AUTHORITY_GATE`

Search only genuinely joint source conditions. One-wedge asymptotic, matching, pole and Feynman-branch uniqueness are no longer admissible as sufficient joint uniqueness arguments by themselves.

## Global locks unchanged

- `RQIR Core v1.0 = FROZEN`.
- `D7-S2 = NOT_CLOSED`.
- `D7-S3 = NOT_CLOSED`.
- `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`.
- terminal selectors forbidden.
- Candidate Gravity inactive.
- KMQGB remains downstream of pinned DSIR authority.

# Recovery/front ledger delta — K5 collision-counterterm ambiguity versus EPRL sum rule

Date: 2026-09-15

## New terminal scoped result

`SOURCE_J1_K5_EPRL_SUMRULE_DOES_NOT_FIX_COLLISION_EXTENSION_SCOPED`

Authority:

- prereg: `research/SOURCE_J1_K5_COLLISION_COUNTERTERM_SUMRULE_PREREG_2026-09-15.md`
- prereg commit: `7e38d2a3aac339a7133e51b5589f3ba23b7f42c3`
- implementation: `code/source_j1_k5_collision_counterterm_sumrule_certificate.py`
- implementation commit: `4b7598cf6f2c2a7b8964b373e965d950eaafe26f`
- workflow head: `260fa3abd5290bf51a1ae6c72f64ad6bb7cf7c3c`
- result: `research/SOURCE_J1_K5_COLLISION_COUNTERTERM_SUMRULE_RESULT_2026-09-15.md`
- result commit: `79b29ff4a3fcc0675a8d0f2958aff57310fdc20f`
- run: `34916367231`
- source-lock job: `104214750411` success
- exact-certificate job: `104214778424` success
- artifact: `10376212425`
- digest: `sha256:8a394c79c533f123d2d7913b5feb49e3c0258b7a7a8be3560010df7bccd4f7d6`

Exact witness:

- 1024 independent K5 wedge-sign patterns;
- 16 distinct constrained causal patterns, multiplicity 2 under 32 sigma assignments;
- 1008 unconstrained patterns;
- counterterm coefficient +63 on constrained, -1 on unconstrained;
- full EPRL sign-sum shift exactly 0;
- constrained distinct-pattern shift 1008;
- sigma-counted constrained shift 2016;
- 120 K5 vertex permutations / 122880 pattern-permutation checks preserve membership and coefficients;
- zeroth-order `delta_N` has scaling degree 12, within frozen full-collision scaling ceiling 30.

Interpretation:

- EPRL sign-sum identity + K5 permutation symmetry + same-scaling ceiling do not uniquely fix the causal collision extension;
- a further source-faithful joint-limit/normalization condition is required to eliminate the explicit counterterm witness;
- no final claim of source nonuniqueness or Eq. (4) nonexistence is made.

## Active numerical front unchanged

Iter504 remains authoritative and must not be duplicated:

- run `34907349374`;
- source-lock success;
- all 12 point-lanes success;
- centered shards active/queued;
- no terminal aggregate consumed yet.

## Independent collision-partition stream unchanged

Iter461 remains unresolved and must not be duplicated:

- branch `research/iter461-k5-collision-partitions`;
- head `05c7f87c8519349057332bf90021f1128e1eefc3c`;
- run `34748503239`;
- last verified queued/no jobs.

## Analytical frontier

`SOURCE_J1_K5_EQ4_IMPROPER_DISTRIBUTIONAL_EXISTENCE_GATE`

Must now treat as insufficient uniqueness data, when used alone:

- off-collision agreement;
- same scaling degree;
- K5 permutation symmetry;
- EPRL independent-sign sum rule.

A successful uniqueness claim must identify and prove an additional source-faithful condition that kills the explicit counterterm witness.

## Global locks unchanged

- `RQIR Core v1.0 = FROZEN`.
- `D7-S2 = NOT_CLOSED`.
- `D7-S3 = NOT_CLOSED`.
- `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`.
- terminal selectors forbidden.
- Candidate Gravity inactive.
- KMQGB remains downstream of pinned DSIR authority.

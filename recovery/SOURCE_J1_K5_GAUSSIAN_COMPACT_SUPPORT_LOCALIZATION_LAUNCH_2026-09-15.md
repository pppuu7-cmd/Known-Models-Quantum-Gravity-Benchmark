# Recovery handoff — Gaussian compact-support localization

Date: 2026-09-15
Status: `LAUNCHED_NONTERMINAL`

## Consumed terminal parent

- Gate: `SOURCE_J1_K5_ADDITIONAL_JOINT_REGULATOR_GAUSSIAN_DIAGNOSTIC_GATE`
- Classification: `AUX_GAUSSIAN_JOINT_REGULATOR_REJECTED_UNRENORMALIZED_SCOPED`
- Result commit: `8982ea92de08bfb6028df35be16f116e0e58c22f`
- Run: `34954054888`, completed/success
- Artifact: `10390423124`
- Digest: `sha256:7679e9349798386bc53757207cbb85142420e10ae89745b62e4ab4117cf54009`
- P1/P2/P3: all `UNRENORMALIZED_DIVERGENT_DIAGNOSTIC`
- Tail growth approximately: P1 `40.99907756`, P2 `26.01103312`, P3 `66.00705355`.

Interpretation ceiling: rejection of the unrenormalized Gaussian auxiliary family on the aligned highest-contact witness only; not Eq.4 nonexistence or model/family failure.

## Active front

Gate: `SOURCE_J1_K5_GAUSSIAN_COMPACT_SUPPORT_LOCALIZATION_GATE`

Preregistration:
- `research/prereg/SOURCE_J1_K5_GAUSSIAN_COMPACT_SUPPORT_LOCALIZATION_2026-09-15.md`
- commit `1e3402aa02a2f52eac5d379ba8b0c5ffc5ebc4ef`

Implementation:
- `code/source_j1_k5_gaussian_compact_support_localization.py`
- commit `55c07deb557cd22460ba1790396e332bfe3bb83c`

Workflow:
- `.github/workflows/source-j1-k5-gaussian-compact-support-localization.yml`
- head `0dec512b067b3b19205d2015ee62c8ab401b2e31`
- run `34954491166`
- last observed status: source-lock queued, no terminal scientific result yet.

Do not duplicate this run. On next iteration consume run `34954491166` first. Repair only implementation/orchestration if necessary; paths, k-grid, exterior-bound formula, thresholds and terminal taxonomy are frozen.

## Intended certificate

For any smooth cutoff `chi` with `0<=chi<=1`, `chi=1` on `|x|<=1`, and `chi=0` on `|x|>=2`, the gate bounds the difference between the parent Schwartz pairing and compact pairing using the exact K5 star-edge coordinate basis and an analytic incomplete-gamma exterior bound.

A path certifies only if, for k=5..8, `B_ext/J <= 1e-20`, the compact lower bound remains positive, and every lower/upper growth ratio for `5->6`, `6->7`, `7->8` exceeds `4`.

## Independent streams

- Iter504 run `34907349374`: many jobs completed/success but no terminal aggregate consumed; partial values remain non-evidence.
- Iter461 run `34748503239`: last job query returned no jobs; do not duplicate until authoritative run status/history is reconciled.

## Existing uniqueness limitation

Critic-confirmed commit `97a4821f85f13e6f5c6d41356612c88939d45f2c` establishes a nonzero collision-supported homogeneous ambiguity under the specifically frozen conjugation/coefficient-pattern/permutation/zero-sum/scaling constraints, conditional on a base extension. Therefore a future counterterm subtraction is not source-selected merely because it cancels the Gaussian divergence.

## Governance

- `RQIR Core v1.0 = FROZEN`
- `D7-S2 = NOT_CLOSED`
- `D7-S3 = NOT_CLOSED`
- `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`
- terminal selectors forbidden
- Candidate Gravity inactive
- KMQGB downstream of pinned DSIR authority

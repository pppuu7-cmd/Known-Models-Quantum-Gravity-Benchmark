# Terminal result — SOURCE_J1_K5 highest-contact magnetic leading transfer V4 same-contract repair

Date: 2026-09-16
Status: `TERMINAL_REPAIRED_RESULT_PENDING_INDEPENDENT_CRITIC`

## Authority chain

- Scientific preregistration: `research/prereg/SOURCE_J1_K5_HIGHEST_CONTACT_MAGNETIC_LEADING_TRANSFER_V4_2026-09-15.md`, commit `01ccbad09d4a413066b1bcfbf77861d386926e73`.
- Frozen input: `inputs/source_j1_k5_highest_contact_magnetic_leading_transfer_v4.json`, commit `8b933f94b8eea1c6990b33f9f2f563f7fabae461`.
- Historical V4 implementation Critic: commit `c0358e348bbb225719bb1617f905e38d91f33e21`, verdict `INVALID_IMPLEMENTATION` because two mandatory controls were conclusion-loaded/vacuous.
- Accepted rotation-control repair: `f903669dd08c6ae6fa9ac4d140ff85f294dd36c1`.
- Same-contract repair protocol frozen before repair implementation: `recovery/V4_IMPLEMENTATION_REPAIR_PROTOCOL_2026-09-16.md`, commit `91bcaadc83be2934e09ec3e32b17709b3306d059`.
- Repair implementation: `code/source_j1_k5_highest_contact_magnetic_leading_transfer_v4_repair.py`, commit `bbb39f58bbda2a24977d2ab1438a7f78c80bdb91`.
- Repair workflow: `.github/workflows/source-j1-k5-highest-contact-magnetic-leading-transfer-v4-repair.yml`, commit `0b13ccac5eaf4cbb4d463411d0048c483af93af1`.

No frozen scientific object, source authority, tangent witness, channel, PASS/FAIL/BLOCKED/INVALID taxonomy, or interpretation ceiling was changed by the repair.

## GitHub Actions

Authoritative repair run: `35033194283`
Head: `0b13ccac5eaf4cbb4d463411d0048c483af93af1`
Workflow conclusion: `success`

Jobs:

- source-lock `104596220542`: `success`;
- exact lane Python 3.11 `104596257007`: `success`;
- exact lane Python 3.13 `104596256994`: `success`;
- aggregate `104596351274`: `success`.

Artifacts:

- Python 3.11: artifact `10422336163`, digest `sha256:08808cef77802a9c19ac2ddf8c075baa311a3bed1adbd3d3786d366aaf1823e8`;
- Python 3.13: artifact `10421889454`, digest `sha256:6d8d8f94825f4cb1f0faf180242c3e6d23383ef0fe83f88f65bb63bbfdfec889`;
- aggregate: artifact `10421794928`, digest `sha256:8f969582092101fb270afd0251f9f603b3695ff913332098fd75511b7fb0976b`.

## Repaired frozen controls

The two controls that invalidated the historical implementation are now executable rather than conclusion-loaded:

1. `UNIQUE_CUBIC_SOURCE`: the source split is rebuilt from the rederived `c1,c2,c3` coefficients; delta-derivative scaling is derived from the positive-scale distribution action. Both exact lanes derive

   - `step -> 0`,
   - `delta -> -1`,
   - `delta_prime -> -2`,
   - `delta_double_prime -> -3`.

2. `REMOVE_HIGHEST_CONTACT_NEGATIVE`: `c3/delta''` is physically omitted while `theta`, `delta`, and `delta'` remain. The same transfer classifier used in production rejects the mutated split with exact reason `NO_UNIQUE_CUBIC_SOURCE_COMPONENT`.

The wrong-ratio and synthetic-cancellation fixtures also pass through that same classifier. The accepted exact SO(3) covariance/non-orthogonal counterexample controls remain active.

## Aggregate terminal classification

Both exact lanes agree exactly and all frozen controls pass.

`SOURCE_J1_K5_CHANNEL00000_HIGHEST_CONTACT_SURVIVES_LEADING_SCOPED`

Exact recovered values:

- fixed channel-`00000` angular contraction: `11/24`;
- magnetic/contact scalar ratio: `3/4` in both branches;
- physical highest-contact leading coefficient:

`-216513/(8388608*rho**10*(rho**2 + 1)**10)`

for the frozen real nonzero-`rho`, `j=1`, fixed channel-`00000`, full-K5-collision tangent witness.

## Scientific interpretation

The repair removes the specific `INVALID_IMPLEMENTATION` defects identified by the historical V4 Critic and reproducibly restores the original scoped V4 PASS on two pinned Python versions.

This establishes only survival of the tested highest `delta''` contact leading homogeneous tensor in the exact frozen realization and tangent witness. It does **not** establish the existence/nonexistence of the full joint distribution product, complete K5 vertex divergence/convergence, family failure, D7 closure, or any terminal selector.

Governance remains:

- `RQIR Core v1.0 = FROZEN`;
- `D7-S2 = NOT_CLOSED`;
- `D7-S3 = NOT_CLOSED`;
- `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`;
- terminal selectors remain forbidden;
- Candidate Gravity remains inactive;
- KMQGB remains downstream of pinned DSIR authority.

## Next admissible step

Independent Critic should review this fresh repair run against the unchanged V4 preregistration, specifically verifying that the scaling derivation is not merely a disguised table, that the removal fixture truly changes the source split seen by the common classifier, and that the interpretation ceiling is preserved. A downstream physics gate may be opened only after current repository authority is re-read and this repaired result is not independently invalidated.

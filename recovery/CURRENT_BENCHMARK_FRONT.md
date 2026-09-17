# Current Benchmark Front
Updated: 2026-09-17

Fresh repository `main` and fresh Actions state always outrank this navigation document if they diverge.

## Latest terminal Research execution

`ITER504R_ROOT_AFFINE_REUSE_CONTINUOUS_DRIFT_DIAGNOSTIC_GATE`

Classification:

`ITER504R_ROOT_AFFINE_REUSE_INCONCLUSIVE_SCOPED`

This is a valid scientific INCONCLUSIVE localization result. It is not FAIL, not a decay witness, and not an implementation blocker.

Canonical terminal record:

- preregistration `147d68f26ed3a14ce3cd1fd77fcd96d5fb329ec8`;
- implementation `f846820bae39963a48272deccb2e4a539100fce1`;
- assembler `904cae881f86f213973110fc8f18a4c02d67cc3d`;
- aggregate `e0367d4e0b91afc668e733c2027fd39bf27637fc`;
- workflow head `a6b71f56b5900173029a291690b65e7ac644d000`;
- authoritative Actions run `35154724661`, terminal `completed/success`;
- terminal result commit `598ede26e0db448411537e9d5f813aa344f88d0f`;
- independent Critic record commit `6e300294e6c9a470099776d1c30357eed3fa4b93`.

Authoritative aggregate artifact `10473120351`, digest `sha256:a2ffc639688f9098e4db9abbcc457c347ab23520e83384bb1bcb106807738205`.

Both independent Python-environment assemblies are byte-identical with JSON SHA256 `9036ced6bb7b252fab5c2b147ef652fe2ee817bc7d49c07f7f8114c6ead17837`.

Aggregate JSON SHA256 `1b5efd75522ee9389ee805c84a0fb86b71fc64bf52b2a114ee21e97a2c2fc029`; internal aggregate payload SHA256 `3e06be81c7b88506e6617e18e43469bde3ac8ba98d96eef314bef48e5ea51c1d`.

## Exact Iter504R result

Frozen cohort remains exactly causal `0to5`, block `0`, path `2`, direction `[1,1,1,-1,-1,-1]`, sign `+1`, root boxes `13,14,15`, all frozen rhos and R grid `[6,8,10,12]`.

All three exact rational covers are valid; root/source controls pass; one derivative model is built per root; descendant derivative recomputation is false; all `243` channels are retained.

Terminal tree:

- total nodes `5829`;
- total leaves `2916`;
- certified leaves `24`;
- unresolved depth-10 leaves `2892`;
- depth histogram: `6:6, 7:6, 8:6, 9:6, 10:2892`.

Maximum terminal drift upper bound is `0.6136407189670734`, witness root box `15`, depth `10`, amplitude `[31/12800,6349/2621440]`, max possible channel count `46`.

Minimum terminal late-slope lower bound is `3.7043291995581735`.

Independent raw-leaf Critic reconstructed cover, counts, all-rho classifier, root depth-zero regression, channel/no-pruning controls and extrema from the two terminal assemblies. It returned:

`CRITIC_CONFIRMS_ITER504R_INCONCLUSIVE_SCOPED`.

All 15 negative controls were rejected.

## Scientific localization

Terminal Iter504P already established sampled-point drift `<=0.05` on the frozen decisive point grid. Iter504R now establishes that narrowing only the child displacement interval while retaining the full-root derivative enclosure is not sufficient to certify the known continuous crossing diagnostic by frozen depth 10.

Therefore the residual continuous uncertainty is localized to **full-root derivative enclosure width and/or nonsmooth max-channel competition/crossings**, not slope sign and not sampled-point stationarity.

Do not increase depth, change threshold, or convert this diagnostic result into a full Iter504 theorem.

## Multi-OS execution diagnostic

Execution-only multi-OS run `35155085604` completed with aggregate failure/INVALID after all six roots and both assemblies succeeded. Its two cross-OS assemblies had the same discrete scientific classification/count/cover structure but were not byte-identical at approximately 1e-10-level serialized floating bounds. This is a reproducibility/aggregation implementation issue only and does not supersede authoritative terminal run `35154724661`.

No rerun is required for Iter504R scientific terminalization.

## Active next gate — Iter504S

Prospectively frozen gate:

`ITER504S_ROOT_DERIVATIVE_VS_CHANNEL_COMPETITION_DISCRIMINATOR`

Scientific preregistration:

`f6367456aa715fe6282ab70c1b2005971a4568c7`

Purpose: bounded mechanism discrimination at the exact `LOW/MID/HIGH` points of roots `13,14,15`, retaining the same full-root derivative balls, all `243` channels, threshold `0.05`, robust floor `+1.0`, same rhos/R grid and no-pruning rule. The derivative-center branch is control-only sensitivity and is not a validated replacement enclosure.

Initial implementation chain:

- evaluator `a008d782618ac6a1c397d571ed091138107ac1ee`;
- assembler `0ef4a6c8e193eec5294485997e4cfdd60e8c0d19`;
- cross-environment aggregate `3f5c21056d9d701948c918b307f76c67f17eed41`;
- workflow head `cb50a107b24232ef1b652baa9443e69fc3fa6ca1`;
- workflow run `35173442220`.

Latest checked state: `35173442220` is nonterminal; source-lock completed successfully and all six root computations are in the frozen root mechanism-discriminator step. No duplicate Iter504S execution is authorized while this run is queued/running.

Outcome-blind adversarial Critic was frozen before terminal Iter504S artifacts:

- `code/iter504s_adversarial_critic.py` commit `7cf20886ee36b4621fe6ce36176a3f361d7927ea`;
- methodology CI run `35173630591` completed/success.

Independent root-affine set-inclusion note:

- `research/notes/ITER504R_ROOT_AFFINE_RIGOR_INDEPENDENT_CHECK_2026-09-17.md` commit `f306b05e5dc4918f4c1edd42e85716e0f67f8fc9`.

## Prospectively frozen Iter504S execution-only repairs

Two implementation mismatches were discovered by static audit while first Iter504S run `35173442220` was still in progress and before any substantive Iter504S artifact was consumed.

### Dual derivative extraction

Repair preregistration:

`88c92f86a765e9d8b441152674fc2c303f3f1ff3`

`iter503_ad_core.dcontract_all()` returns full dual `CD` channel objects. The frozen root-affine construction requires the derivative component `ad.as_c(z).d`. A repaired execution, if needed after the first run becomes terminal, may only extract this already-intended derivative component; full-D then uses the unchanged derivative ball and center-D uses the deterministic midpoint of that derivative ball.

### Fixed-channel drift semantics

Repair preregistration:

`4ef41c0f4ceed3082fd4d80930ef5d848f18802b`

The frozen competition diagnostic is drift-only for fixed channels: all eligible possible-max fixed channels satisfy the competition condition iff their `drift_upper <= 0.05`. The first implementation reused a composite `S_lower>=1 AND drift<=0.05` convenience boolean. A repaired execution, if needed after terminalization of the first run, must reconstruct competition from fixed-channel drift only while leaving the full-envelope scientific predicate unchanged.

These are execution/implementation repairs only. They do not authorize any change to points, roots, threshold, floor, source, rho/R grids, 243-channel completeness, no-pruning rule, mechanism categories or terminal classifier.

If the first Iter504S run is terminal success despite these mismatches, green CI does not override the preregistration mismatch; that execution remains implementation-invalid for science and the already-frozen minimal repairs must be applied before one repaired scientific execution. If it terminally fails, first verify the exact failure point before applying the frozen repairs.

No partial/nonterminal Iter504S numbers are scientific evidence.

## Iter504P retained baseline

`ITER504P_POINT_GRID_DRIFT_WITHIN_FROZEN_TOLERANCE_SCOPED` remains terminal. Maximum decisive sampled point drift is `0.009396862546624` with threshold margin `0.040603137453376`. Point-grid PASS is not a continuous theorem.

## Parallel D7 state retained

- `D7-S2 = NOT_CLOSED`;
- `D7-S3 = NOT_CLOSED`;
- `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`;
- raw group-variable tangent pushforward is closed scoped;
- group-only simultaneous contact-covector object remains BLOCKED_SCOPED because no admissible primary authority defines the required `CP1 x SL(2,C) -> group tangent covector` map.

Do not repeat the K5 source hunt absent genuinely new admissible primary authority.

## Governance lock

- `RQIR Core v1.0 = FROZEN`.
- selector labels remain unauthorized.
- Candidate Gravity remains inactive.
- `INCONCLUSIVE != FAIL`.
- `BLOCKED != FAIL`.
- point-grid PASS != continuous theorem.
- diagnostic localization != full-domain theorem.
- positive slope != absolute-Haar divergence theorem.
- no model/family/global/new-theory/new-physics conclusion follows.

# KMQGB Current Benchmark Front

**Updated:** 2026-09-10  
**KMQGB iteration:** **182**  
**Phase:** **RQIR Core v1.0 FROZEN / repository+methodology 100% VERIFIED / Paper-IV Closure Wave 02 active / D4 partial residual matrix frozen**.

## Stable metrics

- **R1 Repository readiness: 100%.**
- **R2 KMQGB methodology/material readiness: 100%.**
- **R3 external Candidate Gravity scientific readiness: 24%.**
- **Legacy parent-search R4: 45% — PAUSED / CONDITIONAL ON PAPER IV.**
- **Post-freeze PF1 regression: 5/5 = 100% terminal.**
- **Closure Wave 02: 0/3 terminal.**

No scientific readiness score was promoted in Iter182.

RQIR Core **v1.0 remains FROZEN**. `BLOCKED` is not evidence for `NEW_REQUIRED`.

## Paper-IV global decision

**`NOT_YET_AUTHORIZED`**. `NEW_REQUIRED` remains unauthorized.

## Global gates

- D1 Frozen-judge integrity — **PASS**.
- D2 Major-framework complete-object coverage — **NOT_CLOSED**.
- D3 Common-domain comparability — **PARTIAL**.
- D4 Comparator-subtracted residual matrix — **PARTIAL_MATRIX_FROZEN__NOT_CLOSED**.
- D5 Missing-object quarantine — **PASS**.
- D6 Same-realization composition discipline — **PASS_RULE_TARGETS_OPEN**.
- D7 Global terminal proof obligation — **NOT_CLOSED**.

New Iter182 authorities:

- `paper_iv/PAPER_IV_D2_D4_D7_CLOSURE_AUDIT_2026-09-10.md`
- `paper_iv/PAPER_IV_COMPARATOR_RESIDUAL_MATRIX_2026-09-10.json`
- `code/paper_iv_global_gate_validator.py`

D4 is now explicit and machine-auditable. Three mandatory rows remain undefined and are intentionally not zero-filled.

## CW2-01 — O-AS

Exact blocker:

**`STABLE_REPRODUCIBLE_SAME_REALIZATION_A4_PLUS_FULL_ERROR_COMPARATOR_CERTIFICATE`**.

Iter182 literature audit confirms that an explicit contact-amplitude sector exists in arXiv:2602.21285 and a Lorentzian mediated scattering object exists in arXiv:2603.10168. This does **not** close O-AS because the two cannot be composed across different trajectory/truncation/normalization realizations without a derived same-realization map. The contact calculation itself states that a more complete momentum-dependent propagator/all-relevant-vertices treatment is required for a final amplitude verdict.

Current residual status:

`UNDEFINED_PENDING_SAME_REALIZATION_COMPLETE_AMPLITUDE`.

## CW2-02 — O-LQG

Stable observable relations remain:

`q = 1/gamma - gamma - Delta_gamma`,

`beta_Delta = beta_rho - (1+1/gamma^2) beta_gamma`,

`gamma = -cot(4 psi)`,

`Delta_gamma = 2 cot(8 psi) - q`,

`beta_Delta = -16 csc^2(8 psi) beta_psi - beta_q`.

The same-realization ladder is:

- M0 kinematic area-metric representation — **CLOSED**.
- M1a Lorentzian EPRL -> Regge asymptotic dynamics — **PARTIAL / SCOPED PASS**.
- M1b EPRL/Regge -> effective Area-Regge multiscale coarse-graining/refinement — **OPEN**.
- M2 Area-Regge -> area-metric continuum action — **PARTIAL / STRONG AUTHORITY**.
- M3 `gamma_EPRL -> gamma_AM(mu)` identity/normalization — **OPEN**.
- M4 same-parent parity/RG transport — **OPEN**.
- M5 detector-visible area-metric observable — **CLOSED conditionally on ancestry**.

Iter182 checks strengthen the downstream side: area-metric RG has parity-sensitive left/right couplings and an explicit Immirzi beta function. However arXiv:2507.02034 explicitly treats the non-metric masses as independent because they are not currently computable from spin foams and assumes an intermediate EFT regime. Therefore the downstream `gamma` cannot be identified with microscopic EPRL `gamma` by notation alone.

Exact blocker:

**`EPRL_REGGE_TO_AREA_REGGE_PARITY_COUPLING_MATCHING_CERTIFICATE`**.

Current residual status:

`UNDEFINED_PENDING_MICRO_TO_AREA_METRIC_PARAMETER_ANCESTRY`.

## CW2-03 — O-CFS

Exact blocker:

**`FIRST_EXPLICIT_NORMALIZED_CFS_GRAVITY_CORRECTION_TENSOR_PLUS_COMPARATOR`**.

Iter182 confirms three strong pieces of authority:

- arXiv:2605.30199: curved-spacetime continuum iff Einstein–Dirac result in the stated setup;
- arXiv:2607.13871: geometric Einstein derivation plus systematic regularization-length correction generator;
- arXiv:2507.09633: tensor-current hierarchy generalizable to gravitation.

But the first normalized non-Einstein rank-2 correction tensor/coefficient vector is still not explicit. The currents paper describes the rank-2 Einstein sector as expected, and the correction generator has not yet been reduced to a fixed comparator-ready tensor.

Current residual status:

`UNDEFINED_PENDING_NORMALIZED_CORRECTION_TENSOR`.

## D4 residual matrix status

Defined rows:

- GR/EFT — baseline/comparator identity in its declared domain;
- string/dual resonance — scoped rigidity pass.

Undefined required rows:

- AS — missing complete same-realization amplitude;
- LQG — missing microscopic-to-area-metric parameter/coupling ancestry;
- CFS — missing normalized correction tensor.

Therefore D4 has materially advanced, but cannot pass.

## D7 logic

`code/paper_iv_global_gate_validator.py` enforces:

- D7 cannot pass unless D2 and D4 pass;
- no terminal decision can be authorized while D2/D4 are open;
- `NEW_REQUIRED` is forbidden while any required framework row is BLOCKED/undefined;
- undefined residuals cannot be interpreted as zero.

## Candidate Gravity

Scientific readiness remains **24%**. No ansatz is promoted and Candidate Gravity is not the active front.

## Heavy compute

**IDLE.** Current blockers are analytic/provenance/normalization/composition objects, not numerical sensitivity problems.

## Exact continuation order

1. Close one of the three missing physical certificates: O-AS, O-LQG or O-CFS.
2. Replace that row's undefined residual with a same-domain comparator-subtracted residual.
3. Re-run D2/D4 machine logic.
4. Only after all mandatory rows are complete may D7 evaluate `EXISTING_SUFFICIENT / ADAPT_EXISTING / HYBRID_REQUIRED / NEW_REQUIRED`.
5. Do not alter RQIR Core v1.0 unless a genuine benchmark semantic defect is discovered.

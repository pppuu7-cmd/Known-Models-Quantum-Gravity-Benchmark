# KMQGB Current Benchmark Front

**Updated:** 2026-09-08
**KMQGB iteration:** 003
**Repository:** `pppuu7-cmd/Known-Models-Quantum-Gravity-Benchmark`
**Branch:** `main`
**Migration:** COMPLETE — all 7 source benchmark artifacts migrated from RQIR branch `rqir7-known-models-benchmark`; source RQIR remains unchanged/read-only for KMQGB.

## Current benchmark state

- Terminal queue coverage: **4/9 = 44.44%**.
- M01 GR null control: **`EXACT_COMPARATOR_IDENTITY`** with C0.
- M02 perturbative quantum GR EFT: **`EXACT_COMPARATOR_IDENTITY`** with C5.
- M03 semiclassical gravity `SCG-MINK-SCALAR-LR-001`: **`EXACT_COMPARATOR_IDENTITY`** with C1.
- M04 stochastic gravity `SG-MINK-CONFORMAL-EL-001`: **`EXACT_COMPARATOR_IDENTITY`** with C2.
- Active realization: **KMQGB-M05-FR / FR-R2-MINK-001**.
- M05 current state: **ACTIVE / NONTERMINAL**.
- M05 first blocker: **`FR_QUOTIENT_OBSERVABLE_FREEZE`**.

## M03 terminal result — semiclassical gravity

Frozen slice:
- one free massless conformally coupled scalar (`m=0`, `xi=1/6`);
- Minkowski vacuum;
- `Lambda_ren=0`;
- renormalization condition `<0|T_ab^R[eta]|0>=0`;
- finite curvature-squared couplings retained as explicit renormalized parameters;
- low-curvature gauge-invariant linear-response domain at scales much larger than the Planck length.

The model is literally a member of comparator C1. With matched state/scheme/parameters/domain, the comparator-subtracted residual is analytically zero. The mean-only lack of an independent fundamental metric-noise/operator hierarchy remains an F3/F4 promotion limitation, **not** a consistency failure.

## M04 terminal result — stochastic gravity

Frozen slice:
- same conformal-scalar Minkowski setup;
- classical stochastic metric perturbation;
- Einstein-Langevin equation;
- zero-mean stochastic source with covariance given by the stress-tensor noise kernel;
- retarded/dissipative response linked to the same CTP/influence-functional parent structure.

The model is literally a member of comparator C2. With matched state/scheme/parameters/domain, the residual relative to C2 is zero.

Retained design lesson: **metric noise and symmetrized two-point fluctuations alone are not sufficient evidence for a quantum gravitational mediator**, because C2 can reproduce them with a classical stochastic metric.

## Active M05 — metric R+R^2 gravity

Concrete action:

`S = (M_Pl^2/2) ∫ sqrt(-g) [R + R^2/(6M^2)] + S_m`, with `M^2>0`.

Around Minkowski:
- `F=df/dR=1+R/(3M^2)` and `F(0)=1>0`;
- `f_RR=1/(3M^2)>0`;
- the GR massless spin-2 mode is retained;
- one additional scalaron of mass `M` is present;
- no extra massive spin-2 pole is introduced by the pure `R^2` term;
- finite-M trace-sector response is preliminarily distinct from C0 GR;
- exact identifiability against broader scalar-force/C4/C5/higher-curvature nuisance directions is not yet closed.

Current operational completion estimate for M05: **40%**.

## Literal RQIR authority retained

- Q1–Q7 + base residual: external `README.md`, blob `e431df35d929aa8b06b1b1369a2dc80352efe9e9`.
- Comparator C0–C6 registry: `candidate_gravity/BASELINE_COMPARATORS.md`, blob `a2b45188710c885f979123f77fa7aad2273b9983`.
- F0–F7 known-model funnel semantics: `candidate_gravity/landscape/RQIR_FUNNEL_AUDIT_ITERATION137.md`, blob `2757e8fe1004b5c0caef51d6d9fee6f982ac81d4`.
- Fixed-comparator fail-closed preflight semantics: Iteration-504 commit `9af20b657eb89114a954b55b75b59bb3cf284777`.

## External RQIR Candidate Gravity authority

Observed external RQIR `main`: `6839864cc6a2fa66616696db6b9f78b7b8b019f2`.
Authoritative research iteration: **564**.
Candidate Gravity `MODEL_READINESS`: **24%**.
Rank10 run `34165534613` remains verified **in_progress**. KMQGB therefore dispatches no competing heavy work to the shared runner.

## Repository firewall

All benchmark writes go here only. RQIR is read-only external protocol/Candidate Gravity authority. KMQGB does not modify Candidate Gravity readiness, recovery files, iteration numbering, workflows, runner state or scientific authority.

## Exact next gate

For `FR-R2-MINK-001`:
1. freeze a weak-field source-to-detector observable that explicitly projects the scalar trace channel;
2. derive the finite-`M` response and exact GR/C0-subtracted residual;
3. profile `M`, source normalization and calibration freedom;
4. test overlap with conventional scalar-force/C4 nuisance and C5/higher-curvature EFT directions;
5. distinguish `ROBUST_NONZERO_RESIDUAL` from `OPERATIONALLY_DEGENERATE` or a scoped blocker;
6. only after closure move to M06 Brans-Dicke/scalar-tensor.

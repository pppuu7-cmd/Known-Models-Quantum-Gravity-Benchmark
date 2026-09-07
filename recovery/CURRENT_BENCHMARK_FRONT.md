# KMQGB Current Benchmark Front

**Updated:** 2026-09-08
**KMQGB iteration:** 004
**Repository:** `pppuu7-cmd/Known-Models-Quantum-Gravity-Benchmark`
**Branch:** `main`
**Migration:** COMPLETE — all 7 source benchmark artifacts migrated from RQIR branch `rqir7-known-models-benchmark`; source RQIR remains unchanged/read-only for KMQGB.

## Current benchmark state

- Terminal queue coverage: **4/9 = 44.44%**.
- M01 GR null control: **`EXACT_COMPARATOR_IDENTITY`** with C0.
- M02 perturbative quantum GR EFT: **`EXACT_COMPARATOR_IDENTITY`** with C5.
- M03 semiclassical gravity: **`EXACT_COMPARATOR_IDENTITY`** with C1.
- M04 stochastic gravity: **`EXACT_COMPARATOR_IDENTITY`** with C2.
- Active realization: **KMQGB-M05-FR / FR-R2-MINK-001**.
- M05 state: **ACTIVE / NONTERMINAL**.
- M05 current operational completion estimate: **70%**.
- M05 first blocker: **`FR_BROADER_COMPARATOR_QUOTIENT`**.

## Closed control lesson M01–M04

The first four controls validate benchmark semantics rather than falsify their source theories. GR, perturbative quantum-GR EFT, semiclassical gravity and stochastic gravity are all correctly recognized as their own frozen comparator classes. The main retained hierarchy lesson is that mean backreaction and even classical stochastic metric noise do not by themselves certify a quantum gravitational mediator.

## Active M05 — metric R+R^2 gravity

Frozen action:

`S = (M_Pl^2/2) ∫ sqrt(-g) [R + R^2/(6M^2)] + S_m`, `M^2>0`.

Around Minkowski:
- `F(0)=1>0`;
- `f_RR=1/(3M^2)>0`;
- massless GR spin-2 mode retained;
- one extra scalaron of mass `M`;
- no extra massive spin-2 pole from the pure `R^2` term.

### Frozen calibration-resistant C0 observable

Use weak-field potentials `Phi` and `Psi` in

`ds^2=-(1+2Phi)dt^2+(1-2Psi)dx^2`.

For a localized traceful source,

`Phi(r) = -G m_s/r [1 + (1/3)e^{-Mr}]`,

`Psi(r) = -G m_s/r [1 - (1/3)e^{-Mr}]`.

Define

`gamma(r)=Psi/Phi=(3-e^{-Mr})/(3+e^{-Mr})`.

GR/C0 predicts `gamma=1`, so the exact C0-subtracted residual is

`Delta_gamma(r) = -2 e^{-Mr}/(3+e^{-Mr})`.

This is nonzero for finite `Mr`, approaches `0` for `Mr -> infinity`, and approaches `-1/2` for `Mr -> 0`. Common source-mass and Newton-constant normalization cancel exactly, so this is a stronger discriminator than raw force amplitude.

The radial shape also obeys

`ln(3[1-gamma(r)]/[1+gamma(r)]) = -Mr`,

which fixes a one-parameter exponential shape rather than an arbitrary amplitude at each radius.

### Representation-equivalence result

Metric f(R) is dynamically equivalent to a scalar-tensor formulation with `omega_BD=0` and a corresponding scalar potential. This is an exact change of representation when the potential and matter coupling are mapped consistently, so the benchmark must not count the equivalent scalar-tensor rewrite as an independent theory success.

M06 must therefore use a genuinely different scalar-tensor realization. This is now part of the queue contract.

### What remains open

The f(R) residual is robustly distinct from pure C0 GR in the frozen `gamma(r)` observable, but a generic scalar/Yukawa nuisance or broader scalar-tensor family may reproduce the same shape after parameter matching. The low-momentum response can also overlap higher-curvature EFT directions. Therefore M05 is not yet terminal and is not evidence for quantum gravity.

## External RQIR Candidate Gravity authority

Observed external RQIR `main`: `6839864cc6a2fa66616696db6b9f78b7b8b019f2`.
Authoritative research iteration: **564**.
Candidate Gravity `MODEL_READINESS`: **24%**.
Rank10 run `34165534613` was directly verified **in_progress** during this benchmark iteration. KMQGB dispatches no competing heavy work to the shared runner.

## Repository firewall

All benchmark writes go here only. RQIR is read-only external protocol/Candidate Gravity authority. KMQGB does not modify Candidate Gravity readiness, recovery files, iteration numbering, workflows, runner state or scientific authority.

## Exact next gate

For `FR-R2-MINK-001`:
1. compare frozen `gamma(r)` and its multi-radius shape against a generic scalar/Yukawa nuisance;
2. instantiate M06 with a nonduplicate scalar-tensor model and separate true physical degeneracy from exact field-redefinition equivalence;
3. map the low-`q` R+R^2 response against C5 and higher-curvature EFT directions;
4. terminally classify M05 only after this broader quotient is explicit.

# KMQGB Current Benchmark Front

**Updated:** 2026-09-08
**KMQGB iteration:** 006
**Repository:** `pppuu7-cmd/Known-Models-Quantum-Gravity-Benchmark`
**Branch:** `main`
**Migration:** COMPLETE — all benchmark work remains isolated from RQIR writes.

## Current benchmark state

- Terminal queue coverage: **5/9 = 55.56%**.
- M01 GR: **EXACT_COMPARATOR_IDENTITY** with C0.
- M02 perturbative quantum GR EFT: **EXACT_COMPARATOR_IDENTITY** with C5.
- M03 semiclassical gravity: **EXACT_COMPARATOR_IDENTITY** with C1.
- M04 stochastic gravity: **EXACT_COMPARATOR_IDENTITY** with C2.
- M05 metric `R+R^2`: **OPERATIONALLY_DEGENERATE** after the broader scalar/Yukawa quotient.
- Active realization: **KMQGB-M06-BRANS-DICKE / BD-MASSLESS-OMEGA200000-MINK-001**.
- M06 current operational completion estimate: **80%**.
- M06 first blocker: **BD_BROADER_SCALAR_TENSOR_QUOTIENT**.

## Terminal result retained — M05

`FR-R2-MINK-001` has a genuine nonzero GR-subtracted weak-field response

`gamma_fR(r)=(3-exp(-Mr))/(3+exp(-Mr))`,

`Delta_gamma^C0(r)=-2 exp(-Mr)/(3+exp(-Mr))`.

However the single-scalar Yukawa family

`gamma_Y(r)=[1-alpha exp(-m r)]/[1+alpha exp(-m r)]`

reproduces the entire curve exactly at `alpha=1/3`, `m=M`. Therefore the broader-profiled residual is zero and M05 is terminally `OPERATIONALLY_DEGENERATE` in this observable, not inconsistent.

## Active M06 — current-bound-refreshed Brans-Dicke control

Frozen action:

`S=(1/16pi) ∫ sqrt(-g)[phi R-(omega_BD/phi)(nabla phi)^2] + S_m`,

with `V=0`, `omega_BD=200000`, asymptotically constant `phi_0`, weak-field Minkowski domain.

The provisional `omega_BD=50000` point was retired after a current literature refresh. The 2024 Living Reviews pulsar review reports a conservative strong-field/triple-system lower bound around `150000`, with neutron-star EoS dependence. `50000` is therefore retained only as an excluded diagnostic point; the active benchmark moved to `200000`.

### Static channel

`gamma_BD=(1+omega_BD)/(2+omega_BD)=200001/200002`,

`Delta_gamma^C0=-1/200002 ≈ -4.9999500005e-6`.

The weak-field scalar coupling is

`alpha_0^2=1/(2omega_BD+3)=1/400003 ≈ 2.4999812501e-6`.

### Linked radiative channel

The same scalar sector produces leading dipole radiation for unequal-sensitivity compact binaries. In the frozen Living-Reviews convention,

`dot(E)_BD^dip = -(2/3) G_12^2 eta^2 (m^4/r^4) (1-gamma_BD) (s_1-s_2)^2`.

Since

`1-gamma_BD = 1/(omega_BD+2) = 1/200002`,

the static and radiative deviations are tied to the same exact coupling factor. They are not independently adjustable nuisance amplitudes.

This is now the strongest M06 discriminator: a linked static PPN deviation plus a scalar dipole-radiation coefficient from one action.

### Remaining blocker

A more general scalar-tensor family can modify strong-field scalar charges/sensitivities beyond pure Brans-Dicke. The remaining task is therefore to compare the **linked** two-channel fingerprint against that broader family without declaring a trivial superseding theory class an automatic degeneracy.

F6/F7 must also respect the difference between theoretical nonzero residual and present experimental detectability: current pulsar data constrain Brans-Dicke strongly, but `omega_BD=200000` is chosen above the conservative ~150000 benchmark lower limit and is not thereby a detected deviation from GR.

## External RQIR Candidate Gravity authority

Observed external RQIR `main`: `94f9e6735036c96275ea7d170fbee7c2cc5bd579`.
Authoritative research iteration: **566**.
Candidate Gravity `MODEL_READINESS`: **24%**.

RQIR rank10 has raw-PASSed. Rank11 `(+2.5e-6,-1.25e-6)` is the active heavy successor, run `34168897005`, job `101885271903`. KMQGB dispatches no competing heavy work to the shared runner.

## Repository firewall

All benchmark writes go here only. RQIR is read-only external protocol/Candidate Gravity authority. KMQGB does not modify Candidate Gravity readiness, recovery files, iteration numbering, workflows, runner state or scientific authority.

## Exact next gate

For `BD-MASSLESS-OMEGA200000-MINK-001`:
1. profile the linked `gamma` + dipole fingerprint against a broader nonlinear scalar-tensor family;
2. separate genuine observable degeneracy from simple theory-family containment;
3. assess F6/F7 using current Solar-System and pulsar constraints/resources;
4. terminally classify M06;
5. only then activate M07 Stelle quadratic gravity.

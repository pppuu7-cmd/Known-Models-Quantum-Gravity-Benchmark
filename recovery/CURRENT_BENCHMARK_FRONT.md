# KMQGB Current Benchmark Front

**Updated:** 2026-09-08
**KMQGB iteration:** 005
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
- Active realization: **KMQGB-M06-BRANS-DICKE / BD-MASSLESS-OMEGA50000-MINK-001**.
- M06 current operational completion estimate: **60%**.
- M06 first blocker: **BD_MULTI_CHANNEL_DISCRIMINATOR_FREEZE**.

## New terminal result — M05

Frozen model:

`S=(M_Pl^2/2) ∫ sqrt(-g)[R+R^2/(6M^2)] + S_m`, `M^2>0`.

Frozen C0 discriminator:

`gamma_fR(r)=Psi/Phi=(3-exp(-Mr))/(3+exp(-Mr))`,

`Delta_gamma^C0(r)=-2 exp(-Mr)/(3+exp(-Mr))`.

This is a genuine nonzero finite-M deviation from GR and is resistant to common source-mass/Newton-constant normalization.

However the admissible single-scalar Yukawa family

`gamma_Y(r)=[1-alpha exp(-m r)]/[1+alpha exp(-m r)]`

reproduces the entire frozen f(R) curve exactly at

`alpha=1/3`, `m=M`.

Therefore the broader-profiled residual is exactly zero in this observable and M05 closes as **OPERATIONALLY_DEGENERATE**, not as a theory inconsistency and not as an exact theory identity.

This is the first queue example where a theory is demonstrably different from GR but still fails to yield a unique model discriminator after a broader comparator quotient.

## Active M06 — nonduplicate Brans-Dicke control

Frozen action:

`S=(1/16pi) ∫ sqrt(-g)[phi R-(omega_BD/phi)(nabla phi)^2] + S_m`,

with `V=0`, `omega_BD=50000`, asymptotically constant `phi_0`, weak-field Minkowski domain.

This is not the `omega_BD=0` plus-potential scalar-tensor representation equivalent to M05. M06 has a genuinely massless long-range scalar.

Static weak-field fingerprint:

`gamma_BD=(1+omega_BD)/(2+omega_BD)=50001/50002`,

so

`Delta_gamma^C0=-1/(omega_BD+2)=-1/50002 ≈ -1.9999200032e-5`.

The scalar coupling is

`alpha_0^2=1/(2 omega_BD+3)=1/100003 ≈ 9.999700009e-6`.

The next discriminator is not another static force amplitude. The same scalar coupling also controls scalar dipole radiation in compact binaries with unequal sensitivities. Modern pulsar-test reviews show that scalar-tensor dipole radiation enters at lower PN order than the GR quadrupole channel and scales with the squared sensitivity difference.

The exact next task is therefore to freeze the Brans-Dicke-specific dipole normalization and test the linked two-channel fingerprint:

1. static `gamma_BD-1`;
2. scalar dipole-radiation coefficient for unequal-sensitivity binaries.

They must come from the same `omega_BD`, not be independently fit nuisance amplitudes.

## External RQIR Candidate Gravity authority

Observed external RQIR `main`: `94f9e6735036c96275ea7d170fbee7c2cc5bd579`.
Authoritative research iteration: **566**.
Candidate Gravity `MODEL_READINESS`: **24%**.

RQIR rank10 has now raw-PASSed. Rank11 `(+2.5e-6,-1.25e-6)` is the active heavy successor, run `34168897005`, job `101885271903`. KMQGB dispatches no competing heavy work to the shared runner.

## Repository firewall

All benchmark writes go here only. RQIR is read-only external protocol/Candidate Gravity authority. KMQGB does not modify Candidate Gravity readiness, recovery files, iteration numbering, workflows, runner state or scientific authority.

## Exact next gate

For `BD-MASSLESS-OMEGA50000-MINK-001`:
1. freeze the exact dipole-radiation coefficient in one convention;
2. map it to `omega_BD=50000` and body sensitivities;
3. verify static/radiative linkage from the same action;
4. profile against broader scalar-tensor alternatives;
5. assign terminal M06 status only after that two-channel quotient is explicit.

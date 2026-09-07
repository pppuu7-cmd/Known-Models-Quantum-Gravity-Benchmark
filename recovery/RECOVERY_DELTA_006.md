# RECOVERY DELTA 006 — 2026-09-08

## Scope

This delta records KMQGB Iterations 005–006. All writes are confined to `pppuu7-cmd/Known-Models-Quantum-Gravity-Benchmark`. External RQIR remains read-only.

## M05 terminal closure

Model: `FR-R2-MINK-001`, metric `f(R)=R+R^2/(6M^2)`, `M^2>0`.

Frozen GR/C0 discriminator:

`gamma_fR(r)=(3-exp(-Mr))/(3+exp(-Mr))`,

`Delta_gamma^C0=-2 exp(-Mr)/(3+exp(-Mr))`.

This is nonzero for finite `Mr` and cancels common `G`, source mass and `1/r` normalization.

Broader one-scalar Yukawa comparator:

`gamma_Y(r)=[1-alpha exp(-mr)]/[1+alpha exp(-mr)]`.

Exact match at `alpha=1/3`, `m=M` for every radius. Therefore the comparator-profiled frozen-observable residual is exactly zero.

Terminal M05 status: `OPERATIONALLY_DEGENERATE`.

Do not rewrite this as a consistency failure. The theory is distinct from GR in the frozen domain but not uniquely identifiable from this observable after the broader scalar/Yukawa quotient.

## M06 realization refresh

Initial provisional point: massless Brans-Dicke `omega_BD=50000`, `V=0`.

Literature refresh found that this is below the modern conservative pulsar-triple strong-field bound. The 2024 Living Reviews pulsar review reports a conservative lower limit around `omega_BD >= 150000`, with neutron-star EoS dependence.

Therefore the active point is now:

`BD-MASSLESS-OMEGA200000-MINK-001`

with `V=0`, massless long-range scalar, weak-field Minkowski background.

The old `omega_BD=50000` point is retained only as an observationally excluded diagnostic point.

## M06 frozen static channel

`gamma_BD=(omega_BD+1)/(omega_BD+2)=200001/200002`.

`Delta_gamma^C0=-1/(omega_BD+2)=-1/200002 ≈ -4.9999500005e-6`.

`alpha_0^2=1/(2omega_BD+3)=1/400003 ≈ 2.4999812501e-6`.

## M06 frozen linked radiative channel

Using the standard compact-binary Brans-Dicke convention retained in the audit,

`dot(E)_BD^dip = -(2/3) G_12^2 eta^2 (m^4/r^4) (1-gamma_BD) (s_1-s_2)^2`.

Since

`1-gamma_BD=1/(omega_BD+2)=1/200002`,

the static PPN residual and leading scalar dipole coefficient are tied to one exact theory parameter. Do not profile them as independent amplitudes.

## M06 current blocker

`BD_BROADER_SCALAR_TENSOR_QUOTIENT`.

Next work:
1. compare the linked static+radiative fingerprint against a broader nonlinear scalar-tensor family;
2. avoid calling trivial theory-family containment an observable degeneracy;
3. assess F6/F7 against current Solar-System and pulsar constraints/resources;
4. terminally classify M06;
5. then activate M07 Stelle quadratic gravity.

## Current progress

- terminal queue coverage: `5/9 = 55.56%`;
- active M06 operational task estimate: `80%`;
- Candidate Gravity RQIR readiness remains separate at `24%`.

## External RQIR authority observed

- main SHA: `94f9e6735036c96275ea7d170fbee7c2cc5bd579`;
- authoritative research iteration: `566`;
- rank10 raw-PASSed at Iteration 565;
- rank11 coordinate `(+2.5e-6,-1.25e-6)` active;
- run `34168897005`, job `101885271903`.

KMQGB must not launch competing heavy work on the shared runner while that RQIR job is active.

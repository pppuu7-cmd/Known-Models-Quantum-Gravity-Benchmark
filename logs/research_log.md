# KMQGB Research Log

## 2026-09-08 — KMQGB-001 — standalone migration and authority isolation

- Created standalone benchmark authority in `pppuu7-cmd/Known-Models-Quantum-Gravity-Benchmark`.
- Identified exact source RQIR branch `rqir7-known-models-benchmark`; migrated seven benchmark artifacts while preserving source RQIR unchanged.
- Established write firewall: KMQGB writes only to standalone repo; RQIR is read-only external authority.
- External Candidate Gravity readiness observed at 24%.

## 2026-09-08 — KMQGB-002 — protocol recovery, two terminal controls, semiclassical start

- Recovered Q1–Q7, comparator registry C0–C6, and F0–F7 funnel authority from RQIR.
- M01 GR weak-field null control closed `EXACT_COMPARATOR_IDENTITY` with C0; residual 0.
- M02 perturbative quantum GR EFT closed `EXACT_COMPARATOR_IDENTITY` with C5; residual 0.
- Activated M03 semiclassical gravity.
- Terminal coverage reached 2/9 = 22.22%.

## 2026-09-08 — KMQGB-003 — semiclassical/stochastic closure and f(R) activation

- M03 `SCG-MINK-SCALAR-LR-001` frozen to massless conformally coupled scalar in Minkowski vacuum and closed `EXACT_COMPARATOR_IDENTITY` with C1.
- Mean-only semiclassical closure retained as insufficient for full QG promotion, not a theory consistency failure.
- M04 `SG-MINK-CONFORMAL-EL-001` Einstein-Langevin/noise-kernel control closed `EXACT_COMPARATOR_IDENTITY` with C2.
- Design lesson: classical stochastic metric noise and symmetrized two-point fluctuations alone do not certify a quantum gravitational mediator.
- Activated M05 metric `R+R^2/(6M^2)` gravity.
- Terminal coverage reached 4/9 = 44.44%.

## 2026-09-08 — KMQGB-004 — f(R) calibration-resistant discriminator

For `FR-R2-MINK-001`, froze

`gamma(r)=Psi/Phi=(3-exp(-Mr))/(3+exp(-Mr))`

with C0 residual

`Delta_gamma=-2 exp(-Mr)/(3+exp(-Mr))`.

Common `G`, source mass and `1/r` normalization cancel. Multi-radius inversion gives

`ln[3(1-gamma)/(1+gamma)]=-Mr`.

Metric f(R) exact scalar-tensor representation equivalence (`omega_BD=0` plus mapped potential) was recorded; M06 was prohibited from duplicating this representation.

M05 remained active pending broader scalar/Yukawa quotient.

## 2026-09-08 — KMQGB-005 — M05 terminal broader-comparator closure

- Defined the admissible single-scalar Yukawa response family
  `gamma_Y=[1-alpha exp(-mr)]/[1+alpha exp(-mr)]`.
- Proved exact frozen-observable identity with M05 for all radii at `alpha=1/3`, `m=M`.
- Therefore M05 is genuinely distinct from C0/GR at finite `Mr`, but its full multi-radius `gamma(r)` signature is exactly absorbed by the broader scalar/Yukawa quotient.
- Terminal status: `OPERATIONALLY_DEGENERATE`.
- Broader-profiled residual: 0.
- This is not a consistency failure of f(R); it is failure of unique identification in the chosen observable.
- Terminal coverage advanced to 5/9 = 55.56%.
- Began nonduplicate massless Brans-Dicke M06.

## 2026-09-08 — KMQGB-006 — current-bound refresh and linked Brans-Dicke static/radiative fingerprint

### Literature refresh changed the concrete point

- Initial provisional M06 used `omega_BD=50000`, based on the classic Cassini lower bound near 40000.
- Current 2024 Living Reviews pulsar authority reports a conservative strong-field/triple-system lower limit around `omega_BD >= 150000`, with neutron-star EoS dependence.
- Therefore `omega_BD=50000` was retired as the active point and retained only as an observationally excluded diagnostic point.
- Active realization is now `BD-MASSLESS-OMEGA200000-MINK-001`, with `V=0` and a massless long-range scalar.

### Static channel

`gamma_BD=(omega_BD+1)/(omega_BD+2)=200001/200002`.

`Delta_gamma^C0=-1/200002 ≈ -4.9999500005e-6`.

`alpha_0^2=1/(2omega_BD+3)=1/400003 ≈ 2.4999812501e-6`.

### Linked dipole-radiation channel

Using the standard compact-binary Brans-Dicke convention,

`dot(E)_BD^dip = -(2/3) G_12^2 eta^2 (m^4/r^4) (1-gamma_BD) (s_1-s_2)^2`.

Since `1-gamma_BD=1/(omega_BD+2)=1/200002`, the static PPN shift and leading dipole coefficient are controlled by the same exact coupling. They are not independent nuisance amplitudes.

### Current gate

- M06 F0–F2: scoped pass.
- F3: classical partial; no intrinsic QG operator/noise hierarchy.
- F4: analytic nonzero distinction from C0.
- F5: linked static+radiative fingerprint frozen.
- F6: broader nonlinear scalar-tensor quotient still open.
- F7: current observational resources/identifiability still to be mapped without confusing a theoretical residual with a detected deviation.

Current blocker: `BD_BROADER_SCALAR_TENSOR_QUOTIENT`.

M06 operational completion estimate: 80%.
Terminal queue coverage remains 5/9 = 55.56%.

### External RQIR state

- External RQIR main observed at `94f9e6735036c96275ea7d170fbee7c2cc5bd579`.
- Authoritative Candidate Gravity research iteration 566; MODEL_READINESS 24%.
- Rank10 raw-PASSed; rank11 coordinate `(+2.5e-6,-1.25e-6)` is active in run `34168897005`, job `101885271903`.
- No KMQGB heavy work dispatched to the shared runner.

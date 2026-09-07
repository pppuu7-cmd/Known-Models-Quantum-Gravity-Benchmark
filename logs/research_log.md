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

- Defined the admissible single-scalar Yukawa response family `gamma_Y=[1-alpha exp(-mr)]/[1+alpha exp(-mr)]`.
- Proved exact frozen-observable identity with M05 for all radii at `alpha=1/3`, `m=M`.
- M05 remains genuinely distinct from C0 at finite `Mr`, but the broader-profiled residual is 0.
- Terminal status: `OPERATIONALLY_DEGENERATE`.
- Terminal coverage advanced to 5/9 = 55.56%.

## 2026-09-08 — KMQGB-006 — current-bound refresh and linked Brans-Dicke fingerprint

- Provisional M06 `omega_BD=50000` was retired after the 2024 Living Reviews pulsar authority reported a conservative lower limit around `150000`, EoS dependent.
- Active realization moved to `BD-MASSLESS-OMEGA200000-MINK-001`.
- Static channel: `Delta_gamma=-1/200002`.
- Linked radiative channel: scalar dipole response controlled by the same Brans-Dicke scalar coupling and `(s_1-s_2)^2` sensitivity factor.
- M06 reached 80% pending broader scalar-tensor quotient.
- External RQIR Iteration 566, Candidate Gravity 24%; rank11 active; no KMQGB heavy competitor launched.

## 2026-09-08 — KMQGB-007 — M06 nested-model closure and M07 Stelle consistency control

### M06 Brans-Dicke terminal closure

- General massless scalar-tensor gravity was frozen as the parent comparator family with coupling expansion `ln A(varphi)=alpha_0 varphi + (1/2) beta_0 varphi^2 + ...`.
- Brans-Dicke is a nested subfamily. At the matching constant-coupling/`beta_0=0` specialization and `alpha_0^2=1/(2omega_BD+3)`, the parent family contains the exact M06 point.
- Therefore the static `gamma` plus leading dipole fingerprint is nonzero relative to C0 but cannot uniquely identify Brans-Dicke versus its parent class.
- Parent-profiled model-identification residual: 0.
- Terminal status: `OPERATIONALLY_DEGENERATE` at `F6_FAIL_UNIQUENESS_VS_PARENT_ST`.
- Guardrail: this is nesting/non-identifiability, not global equivalence of all scalar-tensor theories.

### M07 standard Stelle quadratic gravity

- Froze `STELLE-MINK-STANDARD-FEYNMAN-001` as a fundamental local quadratic theory under the standard perturbative Feynman/Hilbert-space physical-state interpretation.
- Linearized spectrum: massless graviton + massive scalar + massive spin-2 mode.
- Spin-2 propagator has opposite residues schematically `1/p^2 - 1/(p^2-M_2^2)`; the same cancellation supplies `1/p^4` UV behavior.
- Under the frozen standard physical-state interpretation the massive spin-2 mode is a ghost and fails the RQIR F2 positivity/unitarity gate.
- Terminal status: `FAIL_RQIR_CONSISTENCY` at `F2_STANDARD_MASSIVE_SPIN2_GHOST`.
- Scope explicitly excludes low-energy EFT treatment and modified ghost prescriptions.

## 2026-09-08 — KMQGB-008 — higher-curvature EFT boundary control

- Froze `GR-EFT-RIEMANN3-MINK-001`: GR plus one curvature-cubed Wilson operator, `Q << Lambda`, treated perturbatively to fixed EFT order.
- High-scale roots from resumming the truncated higher-derivative equation are not promoted into the low-energy physical state space.
- The realization is a concrete Wilson-coefficient slice of C5 low-energy gravity EFT.
- It may differ from C0 at nonzero Wilson coefficient, but the C5-profiled theory-class residual is 0.
- Terminal status: `EXACT_COMPARATOR_IDENTITY` with C5.
- Retained design lesson: M07 fundamental/resummed higher derivatives and M08 ordered EFT higher derivatives are not the same physical object.

## 2026-09-08 — KMQGB-009 — type-II string scattering activation

- Activated provisional `TYPEII-T6-GRAV4-TREE-001`.
- Frozen ancestor object: type-II tree-level four-graviton Virasoro-Shapiro Gamma-function amplitude.
- Low-energy expansion: corresponding supergravity/Einstein massless exchange plus correlated derivative series beginning with the characteristic tree-level `alpha'^3 zeta(3) R^4` correction and higher `D^(2k)R^4` terms.
- At any fixed finite sub-string-threshold order, local analytic corrections are representable by C5 EFT Wilson coefficients and therefore are not automatically string-unique.
- The full Gamma-function amplitude contains massive string poles and all-orders correlations, but a finite low-energy C5 truncation must not be used outside its validity range as a straw-man comparator.
- Current blocker: `STRING_4D_COMPACTIFICATION_INTERFACE_FREEZE` — explicit compactification point, light-field/moduli ledger, 10D-to-4D coupling normalization, threshold choice and Q1-Q7/source-detector map.
- M09 operational completion estimate: 45%.
- Terminal queue coverage advanced to **8/9 = 88.89%**.
- External RQIR rank11 run `34168897005` directly verified `in_progress`; no competing KMQGB heavy work launched.

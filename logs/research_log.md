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

- M03 semiclassical control closed `EXACT_COMPARATOR_IDENTITY` with C1.
- M04 Einstein-Langevin stochastic control closed `EXACT_COMPARATOR_IDENTITY` with C2.
- Activated M05 metric `R+R^2/(6M^2)` gravity.
- Terminal coverage reached 4/9 = 44.44%.

## 2026-09-08 — KMQGB-004 — f(R) calibration-resistant discriminator

- Froze `gamma(r)=Psi/Phi=(3-exp(-Mr))/(3+exp(-Mr))` and exact C0 residual `Delta_gamma=-2 exp(-Mr)/(3+exp(-Mr))`.
- Common source normalization cancels; M05 remained open for broader scalar/Yukawa quotient.

## 2026-09-08 — KMQGB-005 — M05 terminal broader-comparator closure

- Generic one-scalar Yukawa family exactly reproduces M05 at `alpha=1/3`, `m=M`.
- Terminal M05: `OPERATIONALLY_DEGENERATE`; broader-profiled residual 0.
- Terminal coverage 5/9 = 55.56%.

## 2026-09-08 — KMQGB-006 — current-bound refresh and linked Brans-Dicke fingerprint

- Provisional `omega_BD=50000` retired after 2024 pulsar review lower bound near `150000`; active point moved to `omega_BD=200000`.
- Static `Delta_gamma=-1/200002` linked to scalar dipole-radiation sector through the same coupling.
- M06 reached 80% pending broader scalar-tensor quotient.

## 2026-09-08 — KMQGB-007 — M06 nested-model closure and M07 Stelle control

- General massless scalar-tensor gravity contains the exact Brans-Dicke point; M06 parent-profiled model-identification residual 0.
- M06 terminal: `OPERATIONALLY_DEGENERATE`, not inconsistency.
- Froze standard fundamental Stelle quadratic gravity under conventional Feynman/Hilbert-space physical-state interpretation.
- Opposite-residue massive spin-2 pole fails RQIR F2 positivity/unitarity.
- M07 terminal: `FAIL_RQIR_CONSISTENCY` at `F2_STANDARD_MASSIVE_SPIN2_GHOST`.

## 2026-09-08 — KMQGB-008 — higher-curvature EFT boundary control

- Froze `GR-EFT-RIEMANN3-MINK-001` for `Q << Lambda`, higher-curvature operator treated perturbatively.
- Spurious high-scale roots of a truncated EFT equation are not promoted into the low-energy state space.
- M08 is a C5 Wilson-coefficient slice.
- Terminal M08: `EXACT_COMPARATOR_IDENTITY` with C5.

## 2026-09-08 — KMQGB-009 — type-II string scattering activation

- Froze the type-II tree-level Virasoro-Shapiro ancestor amplitude and its low-energy `alpha'^3 zeta(3) R^4` onset.
- Identified the common-domain rule: finite-order sub-threshold analytic string corrections are C5-EFT Wilson data; threshold pole structure cannot be compared to a low-energy C5 truncation outside its validity domain.
- Initial M09 blocker was explicit 4D compactification/interface.

## 2026-09-08 — KMQGB-010 — type-II 4D zero-mode closure and first-queue completion

### 4D string realization frozen

- Used six-dimensional toroidal compactification with external four-dimensional zero-mode gravitons and tree-level genus-zero scope.
- Sannan's direct result supplies the anchor that the compactified zero-slope four-graviton string amplitude agrees with 4D GR graviton helicity amplitudes.
- Frozen normalized observable:
  `F_VS=Π_{x=s,t,u} Gamma(1-alpha' x/4)/Gamma(1+alpha' x/4)`.
- `F_VS -> 1` in the GR/zero-slope limit.
- Low-energy expansion starts with `ln F_VS=[zeta(3) alpha'^3/32] s t u + ...` in the declared Mandelstam convention, corresponding to the characteristic `alpha'^3 zeta(3) R^4` correction.

### M09 comparator result

- In the common sub-string-threshold domain, any fixed finite analytic order is absorbable into C5 gravitational-EFT Wilson coefficients: scoped low-energy result `OPERATIONALLY_DEGENERATE_WITH_C5_EFT`, residual 0 after matching.
- At energies resolving the massive string pole tower, low-energy C5 is no longer an admissible comparator.
- The current frozen comparator registry has no explicit UV-completion class valid in that same domain.
- Terminal M09 under the current protocol: `BLOCKED_PROTOCOL_MISMATCH`, not theory inconsistency.

### First queue complete

- Terminal coverage: **9/9 = 100%**.
- Rollup: 5 exact comparator identities, 2 operational degeneracies, 1 genuine consistency failure, 1 protocol/domain block, 0 authorized robust unique QG residuals.
- `100%` is queue-classification coverage only, not quantum-gravity completion.
- Next research front is a separately frozen second-wave queue; the historical 9/9 denominator will not be retroactively changed.

### External RQIR firewall

- External Candidate Gravity last observed Iteration 566, readiness 24%.
- Rank11 run `34168897005` verified `in_progress` during this cycle.
- No competing KMQGB heavy job was launched.

# Known Models / Quantum Gravity Benchmark (KMQGB)

Purpose: audit concrete gravity and quantum-gravity realizations through the frozen RQIR funnel while keeping all benchmark writes physically separated from the main Candidate Gravity repository.

Repository: `pppuu7-cmd/Known-Models-Quantum-Gravity-Benchmark`  
Default branch: `main`  
Recovery entrypoint: `recovery/RESTORE_FROM_NEW_CHAT.md`.

## Historical first wave — frozen and complete

The first-wave denominator is permanently frozen at **9 models** and is never retroactively changed.

| # | Target | Terminal state |
|---|---|---|
| 1 | 4D Einstein–Hilbert GR | `EXACT_COMPARATOR_IDENTITY` C0 |
| 2 | perturbative quantum-GR EFT | `EXACT_COMPARATOR_IDENTITY` C5 |
| 3 | semiclassical Einstein gravity | `EXACT_COMPARATOR_IDENTITY` C1 |
| 4 | Einstein–Langevin stochastic gravity | `EXACT_COMPARATOR_IDENTITY` C2 |
| 5 | metric `R+R^2/(6M^2)` | `OPERATIONALLY_DEGENERATE` |
| 6 | massless Brans–Dicke `omega_BD=200000` | `OPERATIONALLY_DEGENERATE` |
| 7 | standard fundamental Stelle quadratic gravity | `FAIL_RQIR_CONSISTENCY` |
| 8 | perturbative `Riemann^3` gravity EFT | `EXACT_COMPARATOR_IDENTITY` C5 |
| 9 | type-II `T^6` four-graviton tree string amplitude | historical `BLOCKED_PROTOCOL_MISMATCH`; low-energy slice degenerate with C5 |

**First-wave terminal coverage: 9/9 = 100%.**

Rollup: 5 exact comparator identities, 2 operational degeneracies, 1 real consistency failure, 1 protocol/domain block, 0 globally authorized robust unique QG residuals.

## Second wave — frozen and complete

The second-wave denominator is separately frozen at **5 targets** in `protocol/SECOND_WAVE_QUEUE.md`.

| S2 # | Concrete target | Terminal state | Main lesson |
|---|---|---|---|
| 1 | `NL-EOM-ENTIRE-MINK-001` weakly nonlocal entire-form-factor gravity | `OPERATIONALLY_DEGENERATE` | no extra Stelle pole, but all frozen on-shell tree amplitudes equal the mapped local/GR theory |
| 2 | `AS-SCALAR2TO2-LOR-2026-001` Lorentzian asymptotic-safety scalar scattering | `OPERATIONALLY_DEGENERATE` | `p_UV=0` scale-free scattering is shared by an independent UV quantum-effective-action comparator |
| 3 | `KTM-OSCILLATOR-MEASUREMENT-FEEDBACK-001` | `EXACT_COMPARATOR_IDENTITY` C3 | classical measurement/feedback can produce gravity-like interaction plus compulsory noise without an entangling quantum mediator |
| 4 | `PQCG-MINK-CONSERVED-STOCHASTIC-MODES-2026-001` | `EXACT_COMPARATOR_IDENTITY` C3b | the 2026 conserved transverse kernel resolves the linearized Bianchi issue; stochastic classical metric remains a strong comparator |
| 5 | `HR-TRIPLE-SINGLE-MASS-GRAV4-001` UV four-graviton amplitude comparator | `PASS_RQIR_GATE` as comparator infrastructure | provides the previously missing same-domain UV comparator for the string-threshold branch |

**Second-wave terminal coverage: 5/5 = 100%.**

This is benchmark-classification coverage only. It does not mean quantum gravity is solved or that all model classes have been exhausted.

## Cross-wave M09 update

Historical first-wave M09 remains immutable as `BLOCKED_PROTOCOL_MISMATCH` under the protocol available when first-wave closure occurred.

Second-wave S2-M05 prospectively repairs the missing-comparator problem. In the same four-graviton UV channel, type-II Virasoro–Shapiro is exactly distinct from the frozen Huang–Remmen one-mass comparator in pole support:

- HR comparator: one distinct positive massive level `m^2` carrying an infinite spin accumulation;
- type-II string: an infinite sequence of distinct massive string levels.

This establishes `DISTINCT_FROM_ONE_UV_COMPARATOR`, **not** global string uniqueness. See `cross_wave/M09_UV_REEVALUATION_AFTER_S2.md`.

## Main lessons after two waves

1. A nonzero deviation from GR is not automatically a unique theory signature.
2. Stochastic metric noise, decoherence, or quantum discord do not by themselves certify a quantum gravitational mediator; C2/C3/C3b can reproduce such structures.
3. Standard fundamental Stelle gravity has a real scoped consistency failure under the frozen conventional ghost interpretation, while perturbative higher-curvature EFT does not inherit that verdict.
4. Entire nonlocal form factors can remove extra propagator poles, but a special EOM-squared class becomes tree-S-matrix-degenerate with GR.
5. Scale-free trans-Planckian scattering is not unique to asymptotic safety.
6. UV string structure must be compared with other UV amplitudes in the same domain, not with out-of-domain low-energy C5.
7. No model tested so far has produced a **globally authorized** `ROBUST_NONZERO_RESIDUAL` surviving the applicable comparator/domain quotient.

## Status vocabulary

`PASS_RQIR_GATE`, `FAIL_RQIR_CONSISTENCY`, `EXACT_COMPARATOR_IDENTITY`, `OPERATIONALLY_DEGENERATE`, `ROBUST_NONZERO_RESIDUAL`, `BLOCKED_MISSING_REQUIRED_OBJECT`, `BLOCKED_PROTOCOL_MISMATCH`, `OPERATIONAL_FAILURE`.

## Repository firewall

KMQGB may read frozen RQIR protocol and Candidate Gravity authority as external inputs, but benchmark writes belong here only. It must not modify Candidate Gravity readiness, recovery state, workflows, runners, iteration numbering, or scientific authority in `pppuu7-cmd/Relativity-Quantum-Interface-Reconstruction`.

Heavy KMQGB work must not compete for the shared runner while the RQIR heavy chain is active.

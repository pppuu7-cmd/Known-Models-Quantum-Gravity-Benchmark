# Model Audit — massless Brans-Dicke weak-field + dipole-radiation control

Benchmark ID: KMQGB-M06-BRANS-DICKE
Concrete realization ID: BD-MASSLESS-OMEGA200000-MINK-001
Role: extra long-range scalar / scalar-tensor control
State: CLOSED / TERMINAL
Terminal status: OPERATIONALLY_DEGENERATE

## Frozen action

Use four-dimensional Jordan-frame Brans-Dicke gravity

`S = (1/16 pi) ∫ d^4x sqrt(-g) [ phi R - (omega_BD/phi) (nabla phi)^2 ] + S_m[g,psi]`,

with `V(phi)=0`, `omega_BD=200000`, asymptotically Minkowski `g_ab=eta_ab`, constant `phi_0`, and minimally coupled conserved matter.

The active point was raised from a provisional `omega_BD=50000` after the 2024 Living Reviews pulsar review reported a conservative lower limit around `150000` from the pulsar triple system, with neutron-star EoS dependence. The old `50000` point is retained only as an observationally excluded diagnostic point.

## Static fingerprint

For massless Brans-Dicke theory,

`gamma_BD = (1+omega_BD)/(2+omega_BD) = 200001/200002`,

so relative to C0/GR,

`Delta_gamma^C0 = -1/(omega_BD+2) = -1/200002 ≈ -4.9999500005e-6`.

The Einstein-frame weak-field scalar coupling is

`alpha_0^2 = 1/(2 omega_BD + 3) = 1/400003`.

This is an exact nonzero C0 direction at the frozen point.

## Linked dipole-radiation fingerprint

Massless Brans-Dicke gravity also predicts scalar dipole radiation for unequal-sensitivity compact binaries. In the standard pulsar notation the dipole contribution is proportional to

`kappa_D (s_p-s_c)^2`,

and the Brans-Dicke coupling controlling the departure from GR is fixed by the same scalar sector that fixes `gamma_BD`. Dipole damping enters one PN order earlier than the GR quadrupole damping and is especially sensitive in neutron-star/white-dwarf binaries.

The benchmark therefore retains the linked two-channel structure:

1. static weak-field `Delta_gamma^C0=-1/200002`;
2. radiative scalar dipole amplitude fixed by the same Brans-Dicke coupling and source sensitivities.

These are not treated as two independently adjustable signal amplitudes.

## Broader scalar-tensor quotient

A general massless scalar-tensor theory may be written in Einstein-frame language with a coupling function expanded schematically as

`ln A(varphi) = alpha_0 varphi + (1/2) beta_0 varphi^2 + ...`.

Brans-Dicke is a nested subfamily: the Brans-Dicke point is obtained by the appropriate constant linear coupling / `beta_0=0` specialization, with `alpha_0^2=1/(2 omega_BD+3)`.

Therefore a comparator class that is allowed to include the full massless scalar-tensor parent family contains an exact parameter point reproducing every Brans-Dicke observable, including the frozen static and dipole channels. After profiling over that parent family, the minimum comparator-subtracted residual is exactly zero because the parent family contains the candidate point.

This is a **nested-model operational degeneracy**, not the statement that all scalar-tensor theories are physically equivalent to Brans-Dicke. Nonzero `beta_0` theories can have additional strong-field phenomena such as scalarization and can be distinguished by suitable multi-system/strong-field observables. But a detected fingerprint compatible with the frozen Brans-Dicke point cannot by itself establish "Brans-Dicke rather than the broader scalar-tensor parent class".

## F0–F7 terminal map

| Gate | State | Reason |
|---|---|---|
| F0 — dynamics | PASS_SCOPED | exact Jordan-frame action and parameter point frozen |
| F1 — required limits | PASS_SCOPED | GR weak-field limit as `omega_BD -> infinity` |
| F2 — consistency | PASS_SCOPED_WEAK_FIELD | `2 omega_BD+3>0`; standard conserved matter coupling |
| F3 — RQIR hierarchy | CLASSICAL_PARTIAL | deterministic metric+scalar response; no fundamental QG operator/noise hierarchy |
| F4 — comparator distinction | DISTINCT_FROM_C0_BUT_NESTED_IN_ST | nonzero GR residual, but exact containment in broader scalar-tensor parent |
| F5 — hard discriminator | LINKED_TWO_CHANNEL_PASS_VS_C0 | static and dipole channels linked by one action/coupling |
| F6 — statistical identifiability | FAIL_UNIQUENESS_VS_PARENT_ST | parent scalar-tensor family includes the exact BD point, so profiled model-class residual is zero |
| F7 — physical resources | NOT_PROMOTED | current observations constrain the parameter but do not detect a non-GR BD signal; uniqueness already fails at F6 |

## Terminal decision

`OPERATIONALLY_DEGENERATE`

- residual relative to pure GR/C0: nonzero at finite `omega_BD`;
- residual relative to the allowed broader massless scalar-tensor parent class after profiling: `0`;
- no inconsistency of Brans-Dicke is inferred;
- no claim is made that all scalar-tensor theories are equivalent;
- the result is a model-identification limitation: the parent class can reproduce the exact candidate point by nesting.

## Q1–Q7 fingerprint

- Q1: classical metric/proper-time modification.
- Q2: no quantum superposed-geometry branch structure.
- Q3: modified classical source/backreaction through a long-range scalar.
- Q4: no quantum-mediator certificate.
- Q5: extra classical scalar gravitational degree of freedom, not quantum geometry noise.
- Q6: classical scalar+metric response with scalar radiative channel.
- Q7: classical modified gravity, not C5 quantized GR EFT.

## Sources

1. P. C. C. Freire and N. Wex, *Gravity experiments with radio pulsars*, Living Reviews in Relativity 27, 5 (2024): conservative Brans-Dicke lower limit near `150000`; dipole-radiation structure and sensitivity dependence.
2. Living Reviews scalar-tensor/GR-test literature: `gamma=(1+omega_BD)/(2+omega_BD)` and `alpha_0^2=1/(2omega_BD+3)`.
3. Living Reviews gravitational-wave tests: general scalar-tensor coupling families, Brans-Dicke as a special scalar-tensor case, and dipolar radiation as a leading discriminator.
4. External RQIR comparator/F0-F7 authority remains read-only.

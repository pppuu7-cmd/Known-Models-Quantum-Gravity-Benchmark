# Model Audit — massless Brans-Dicke weak-field + dipole-radiation control

Benchmark ID: KMQGB-M06-BRANS-DICKE
Concrete realization ID: BD-MASSLESS-OMEGA200000-MINK-001
Role: extra long-range scalar / scalar-tensor control
State: ACTIVE / NONTERMINAL

## Frozen action

Use four-dimensional Jordan-frame Brans-Dicke gravity

`S = (1/16 pi) ∫ d^4x sqrt(-g) [ phi R - (omega_BD/phi) (nabla phi)^2 ] + S_m[g,psi]`,

with

- `V(phi)=0`;
- `omega_BD = 200000`;
- asymptotically Minkowski background `g_ab=eta_ab`, `phi=phi_0=constant`;
- ordinary minimally coupled conserved matter.

This is deliberately not the f(R)-equivalent `omega_BD=0` plus-potential representation used by M05. It has a genuinely long-range massless scalar and a large finite Brans-Dicke coupling.

### Why 200000, not 50000

The first provisional M06 point used `omega_BD=50000`, chosen only from the classic Cassini lower bound near `40000`. A current literature refresh changed that choice: the 2024 Living Reviews pulsar review reports a conservative strong-field/triple-system Brans-Dicke lower limit around `150000` (with neutron-star equation-of-state dependence). Therefore `50000` is retained only as an observationally excluded diagnostic point, while the active concrete realization is moved to `omega_BD=200000`.

This is still not a global claim of complete observational viability; it is a concrete current-bound-safe benchmark point for the declared tests.

## Weak-field static fingerprint

For massless Brans-Dicke theory,

`gamma_BD = (1+omega_BD)/(2+omega_BD)`.

At the frozen point,

`gamma_BD = 200001/200002`.

Relative to C0/GR (`gamma_GR=1`),

`Delta_gamma^C0 = -1/(omega_BD+2) = -1/200002`

or numerically

`Delta_gamma^C0 ≈ -4.9999500005e-6`.

The Einstein-frame weak-field scalar coupling obeys

`alpha_0^2 = 1/(2 omega_BD + 3) = 1/400003 ≈ 2.4999812501e-6`.

Unlike M05, this massless theory has no Yukawa range parameter: the leading weak-field PPN gamma shift is long-range and radius-independent in the ordinary PPN domain.

## Nonduplication from M05

M05 metric `R+R^2` is equivalent to a scalar-tensor theory with `omega_BD=0` and a nontrivial potential producing a massive scalaron. M06 instead has

- `omega_BD=200000` rather than `0`;
- `V=0` rather than the mapped f(R) potential;
- a massless long-range scalar rather than scalaron mass `M`;
- constant weak-field PPN gamma rather than finite-range Yukawa `gamma(r)`.

Therefore M06 is not a field-redefinition duplicate of M05.

## Linked radiative fingerprint from the same action

The static PPN shift is not treated as an isolated fit parameter. In massless Brans-Dicke gravity the same scalar sector produces leading dipole radiation for compact binaries whose bodies have unequal sensitivities.

Using the standard compact-binary Brans-Dicke convention summarized in Living Reviews, the leading dipole contribution to the energy flux contains

`dot(E)_BD^dip = -(2/3) G_12^2 eta^2 (m^4/r^4) (1-gamma_BD) S^2`,

where `S=s_1-s_2` is the sensitivity difference and the remaining symbols have their standard binary-dynamics meaning in that convention.

Because

`1-gamma_BD = 1/(omega_BD+2)`,

the same exact parameter controlling the static PPN residual also controls the leading dipole coefficient:

`1-gamma_BD = -Delta_gamma^C0 = 1/200002`.

Thus the benchmark now has a two-channel same-dynamics linkage:

1. static metric ratio: `Delta_gamma^C0=-1/200002`;
2. radiative scalar dipole coefficient proportional to `(+1/200002) S^2`.

The two amplitudes are not independently profiled nuisance parameters.

Modern pulsar reviews emphasize that scalar dipole radiation enters at lower PN order than the GR quadrupole channel and is especially constrained in systems with strongly unequal sensitivities, such as neutron-star/white-dwarf binaries.

## Consistency / limits

- F0 dynamics: explicit local scalar-tensor action — PASS_SCOPED.
- GR limit: `omega_BD -> infinity` gives the standard weak-field GR limit — PASS_SCOPED.
- Scalar kinetic sign: `2 omega_BD + 3 > 0`, so the canonical Einstein-frame scalar is not a ghost in the declared perturbative domain — PASS_SCOPED.
- Matter source: the scalar couples to the trace of matter stress through the scalar-tensor field equations.
- Metric plus scalar response is classical; no intrinsic quantum-gravitational operator/noise hierarchy is supplied.

## F0–F7 current map

| Gate | State | Reason |
|---|---|---|
| F0 — dynamics | PASS_SCOPED | exact Jordan-frame action and parameter point frozen |
| F1 — required limits | PASS_SCOPED | finite near-GR point; exact GR weak-field limit as `omega_BD -> infinity` |
| F2 — consistency | PASS_SCOPED_WEAK_FIELD | `2 omega_BD+3>0`, conserved minimally coupled matter, standard scalar-tensor field equations |
| F3 — RQIR hierarchy | CLASSICAL_PARTIAL | deterministic metric+scalar response, no fundamental QG noise/operator hierarchy |
| F4 — comparator distinction | DISTINCT_FROM_C0_ANALYTIC | static `Delta_gamma=-1/200002 != 0`; linked scalar dipole channel absent in GR |
| F5 — hard discriminator | TWO_CHANNEL_LINK_FROZEN | static and dipole coefficients tied to the same `omega_BD`; common source normalization cannot independently tune both |
| F6 — statistical identifiability | BROADER_ST_QUOTIENT_OPEN | need to test whether a more general scalar-tensor family can match both weak-field gamma and strong-field scalar charges/sensitivities |
| F7 — physical resources | BLOCKED | not evaluated before broader model identifiability |

## Q1–Q7 fingerprint — current

- Q1: classical proper-time/metric modification through finite `gamma_BD-1`.
- Q2: no quantum superposed-geometry branch structure.
- Q3: modified classical source/backreaction through the Brans-Dicke scalar trace coupling.
- Q4: no quantum-mediator certificate.
- Q5: one extra classical long-range scalar gravitational degree of freedom; not quantum geometry noise.
- Q6: classical causal scalar+metric response plus a linked scalar radiative channel.
- Q7: not C5 perturbative quantized GR; it is a classical scalar-tensor modification.

## Current first blocker

`BD_BROADER_SCALAR_TENSOR_QUOTIENT`:

1. retain the exact linked static/dipole coefficient `1/(omega_BD+2)`;
2. compare against a broader scalar-tensor family with independent nonlinear coupling/strong-field scalarization freedom;
3. distinguish a true observable degeneracy from the trivial fact that Brans-Dicke is contained as a special subfamily of general scalar-tensor gravity;
4. preserve current empirical bounds as an external viability check, not as a substitute for the RQIR comparator test;
5. terminally classify M06 only after the two-channel broader quotient is explicit.

## Sources

1. Living Reviews tests of GR: `gamma=(1+omega_BD)/(2+omega_BD)` and `alpha_0^2=1/(2omega_BD+3)`.
2. N. Wex and P. Freire, *Gravity experiments with radio pulsars*, Living Reviews in Relativity 27, 5 (2024): dipole-radiation structure and conservative Brans-Dicke lower limit around `150000` from PSR J0337+1715, with EoS dependence.
3. Living Reviews compact-binary scalar-tensor summary: leading Brans-Dicke dipole energy flux proportional to `(1-gamma_BD)(s_1-s_2)^2`.
4. Cassini remains the canonical Solar-System weak-field reference near `omega_BD>40000`, but it is no longer the strongest benchmark bound used here.
5. External RQIR comparator and F0-F7 authority retained read-only from the RQIR repository.

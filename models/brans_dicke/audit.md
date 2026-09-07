# Model Audit — massless Brans-Dicke weak-field control

Benchmark ID: KMQGB-M06-BRANS-DICKE
Concrete realization ID: BD-MASSLESS-OMEGA50000-MINK-001
Role: extra long-range scalar / scalar-tensor control
State: ACTIVE / NONTERMINAL

## Frozen action

Use four-dimensional Jordan-frame Brans-Dicke gravity

`S = (1/16 pi) ∫ d^4x sqrt(-g) [ phi R - (omega_BD/phi) (nabla phi)^2 ] + S_m[g,psi]`,

with

- `V(phi)=0`;
- `omega_BD = 50000`;
- asymptotically Minkowski background `g_ab=eta_ab`, `phi=phi_0=constant`;
- ordinary minimally coupled conserved matter.

This is deliberately not the f(R)-equivalent `omega_BD=0` plus-potential representation used by M05. It has a genuinely long-range massless scalar and a large finite Brans-Dicke coupling.

The numerical value `omega_BD=50000` is chosen as a concrete near-GR control above the canonical Cassini weak-field lower bound near `40000`. This choice is not a claim that this single number exhausts all present observational constraints or strong-field scalar-tensor phenomenology.

## Weak-field static fingerprint

For massless Brans-Dicke theory the PPN parameter is

`gamma_BD = (1+omega_BD)/(2+omega_BD)`.

At the frozen point,

`gamma_BD = 50001/50002`.

Relative to C0/GR (`gamma_GR=1`),

`Delta_gamma^C0 = gamma_BD - 1 = -1/(omega_BD+2) = -1/50002`.

Numerically,

`Delta_gamma^C0 ≈ -1.9999200032e-5`.

The Einstein-frame weak-field scalar coupling obeys

`alpha_0^2 = 1/(2 omega_BD + 3) = 1/100003 ≈ 9.999700009e-6`.

Unlike M05, this massless theory has no Yukawa range parameter in the declared realization: the leading weak-field gamma shift is long-range and radius-independent within the ordinary PPN domain.

## Immediate representation/nonduplication check

M05 metric `R+R^2` is equivalent to a scalar-tensor theory with `omega_BD=0` and a nontrivial potential producing a massive scalaron. M06 instead has

- `omega_BD=50000` rather than `0`;
- `V=0` rather than the mapped f(R) potential;
- a massless long-range scalar rather than scalaron mass `M`;
- constant weak-field PPN gamma rather than finite-range Yukawa `gamma(r)`.

Therefore M06 is not a field-redefinition duplicate of M05.

## Consistency / limits

- F0 dynamics: explicit local scalar-tensor action — PASS_SCOPED.
- GR limit: `omega_BD -> infinity` gives the standard weak-field GR PPN limit — PASS_SCOPED.
- Scalar kinetic sign: `2 omega_BD + 3 > 0` at `omega_BD=50000`, so the canonical Einstein-frame scalar is not a ghost in the declared perturbative domain — PASS_SCOPED.
- Matter source: the scalar couples to the trace of matter stress through the scalar-tensor field equations.
- Metric plus scalar response is classical; no intrinsic quantum-gravitational operator/noise hierarchy is supplied.

## F0–F7 current map

| Gate | State | Reason |
|---|---|---|
| F0 — dynamics | PASS_SCOPED | exact Jordan-frame action and parameter point frozen |
| F1 — required limits | PASS_SCOPED | finite near-GR point; exact GR weak-field limit as `omega_BD -> infinity` |
| F2 — consistency | PASS_SCOPED_WEAK_FIELD | `2 omega_BD+3>0`, conserved minimally coupled matter, standard scalar-tensor field equations |
| F3 — RQIR hierarchy | CLASSICAL_PARTIAL | deterministic metric+scalar response, no fundamental QG noise/operator hierarchy |
| F4 — comparator distinction | DISTINCT_FROM_C0_ANALYTIC | `Delta_gamma=-1/50002 != 0` in exact algebra |
| F5 — hard discriminator | PARTIAL | gamma is calibration-resistant but a static PPN shift alone is not yet a unique scalar-tensor identifier |
| F6 — statistical identifiability | BLOCKED_MULTI_CHANNEL | need a second linked observable, preferably scalar dipole-radiation response with source sensitivities, to test model-specific parameter linkage |
| F7 — physical resources | BLOCKED | not evaluated before multi-channel identifiability |

## Q1–Q7 fingerprint — current

- Q1: classical proper-time/metric modification through finite `gamma_BD-1`.
- Q2: no quantum superposed-geometry branch structure.
- Q3: modified classical source/backreaction through the Brans-Dicke scalar trace coupling.
- Q4: no quantum-mediator certificate.
- Q5: one extra classical long-range scalar gravitational degree of freedom; not quantum geometry noise.
- Q6: classical causal scalar+metric response; time-dependent radiative sector is the next useful discriminator.
- Q7: not C5 perturbative quantized GR; it is a classical scalar-tensor modification.

## Current first blocker

`BD_MULTI_CHANNEL_DISCRIMINATOR_FREEZE`:

1. retain exact static `Delta_gamma=-1/50002` as the first amplitude-resistant C0 direction;
2. freeze a second linked channel from the same action, preferably scalar dipole radiation for an unequal-sensitivity compact binary;
3. derive the relation between the static scalar coupling and the radiative scalar channel rather than treating them as independent nuisance amplitudes;
4. compare that linked fingerprint against generic scalar-force/scalar-tensor alternatives;
5. only then assign a terminal KMQGB classification.

## Sources

1. Standard Brans-Dicke action and scalar-tensor field equations; modern scalar-tensor review summaries.
2. Living Reviews tests of GR: `gamma=(1+omega_BD)/(2+omega_BD)` and `alpha_0^2=1/(2omega_BD+3)`.
3. Cassini weak-field bound conventionally summarized as `omega_BD > 40000` for a long-range Brans-Dicke scalar.
4. External RQIR comparator and F0-F7 authority retained read-only from the RQIR repository.

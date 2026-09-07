# Model Audit — metric f(R) / R+R^2 Minkowski scalaron control

Benchmark ID: KMQGB-M05-FR
Concrete realization ID: FR-R2-MINK-001
Role: extra-scalar / modified-gravity control
State: ACTIVE / NONTERMINAL

## Frozen action

Use four-dimensional metric f(R) gravity

`S = (M_Pl^2/2) ∫ d^4x sqrt(-g) [ R + R^2/(6 M^2) ] + S_m[g,psi]`,

with `M^2 > 0`, expanded about Minkowski spacetime and coupled minimally to a conserved matter stress tensor.

For

`f(R)=R+R^2/(6M^2)`

we have

`F=df/dR = 1 + R/(3M^2)`,

`f_RR = 1/(3M^2) > 0`.

At the Minkowski background `R=0`, `F=1>0`. The standard metric-f(R) stability criteria therefore place this slice on the healthy side of the spin-2 ghost and scalar tachyon conditions in the declared weak-field domain.

Metric f(R) is dynamically equivalent to a scalar-tensor theory with Brans-Dicke parameter `omega_BD=0` plus a scalar potential. Around Minkowski the added scalar degree of freedom (scalaron) has mass `M`; the usual massless GR spin-2 sector is retained.

## Why this model is useful

Unlike M01–M04, this is not defined to be one of the frozen C0/C1/C2/C5 comparator classes. It is therefore the first queue item to produce a finite model-vs-GR direction before broader nuisance/comparator profiling.

For traceful matter and finite `M`, the extra scalaron modifies the weak-field response. In the large-`Mr` / large-mass limit the Yukawa contribution is exponentially suppressed and GR is recovered.

## F0–F7 map — current

| Gate | Current state | Reason |
|---|---|---|
| F0 — dynamics | PASS_SCOPED | exact local metric action frozen |
| F1 — required limits | PASS_SCOPED | GR recovered for `M -> infinity` or `Mr >> 1`, while matter remains ordinarily coupled |
| F2 — consistency | PASS_SCOPED_AROUND_MINKOWSKI | `F>0`, `f_RR>0`, `M^2>0`; extra mode is a scalar rather than the massive spin-2 ghost of generic Ricci-tensor quadratic gravity |
| F3 — RQIR hierarchy | CLASSICAL_PARTIAL | deterministic classical modified gravity supplies mean/retarded response but no independent quantum gravitational noise/operator hierarchy |
| F4 — comparator distinction | DISTINCT_FROM_C0_SCOPED | finite-M scalaron changes the ratio of the two weak-field metric potentials for traceful sources |
| F5 — hard-constraint discriminator | PASS_VS_C0 / BROADER_QUOTIENT_OPEN | a dimensionless potential-ratio observable cancels common source-mass/Newton-constant normalization, leaving an analytic nonzero C0 residual; broader scalar-force/ST/C4/C5 quotient remains open |
| F6 — statistical identifiability | BLOCKED_BROADER_COMPARATORS | `M` is identifiable from radial shape in the ideal model, but representation-equivalent/general scalar-tensor and nuisance directions have not yet been fully profiled |
| F7 — physical resources | BLOCKED | forbidden before broader F5/F6 closure |

## Pole / response fingerprint

Declared weak-field content:

- massless spin-2 GR pole;
- one additional scalar pole at mass scale `M`;
- no additional massive spin-2 pole from the pure `R^2` correction;
- scalar response couples to the trace sector of the matter stress tensor.

## Frozen C0 quotient observable

Use the standard weak-field isotropic metric convention

`ds^2 = -(1+2 Phi) dt^2 + (1-2 Psi) d x^2`.

For a localized nonrelativistic traceful source in the linear Minkowski regime of `R+R^2/(6M^2)` gravity,

`Phi(r) = - G m_s/r [1 + (1/3) exp(-M r)]`,

`Psi(r) = - G m_s/r [1 - (1/3) exp(-M r)]`.

The calibration-resistant observable is

`gamma(r) = Psi(r)/Phi(r)`

so the common factors `G`, source mass `m_s`, and `1/r` cancel exactly:

`gamma_fR(r) = [3 - exp(-M r)]/[3 + exp(-M r)]`.

Pure GR/C0 gives

`gamma_C0(r)=1`.

Therefore the exact C0-subtracted residual is

`Delta_gamma(r) = gamma_fR(r) - 1 = - 2 exp(-M r)/[3 + exp(-M r)]`.

Properties:

- for every finite `M r`, `Delta_gamma(r) < 0`;
- `M r -> infinity`: `Delta_gamma -> 0` and GR is recovered;
- `M r -> 0`: `gamma -> 1/2`, hence `Delta_gamma -> -1/2`;
- the residual cannot be removed by a common rescaling of `G` or the source mass.

This closes the simplest source-normalization/calibration degeneracy against C0 analytically.

## Radial shape consistency relation

The same formula can be inverted:

`x(r) = exp(-M r) = 3[1-gamma(r)]/[1+gamma(r)]`.

Hence an ideal multi-radius measurement must satisfy

`ln( 3[1-gamma(r)]/[1+gamma(r)] ) = - M r`.

The radial slope is fixed by one parameter `M`; the Yukawa amplitude in this metric-f(R) realization is not an independent free parameter. This supplies a stronger shape test than a one-point force-amplitude measurement.

## Exact representation-equivalence warning

Metric f(R) gravity is dynamically equivalent to a scalar-tensor formulation with `omega_BD=0` and a specific scalar potential. Therefore no physical observable can distinguish these two **representations of the same dynamics** when the field redefinition, potential and matter coupling are mapped consistently.

This is not an operational failure of f(R). It means the benchmark must not count the equivalent scalar-tensor rewrite as an independent successful theory. M06 should therefore use a genuinely different scalar-tensor realization (for example a distinct Brans-Dicke parameter/potential class) rather than duplicating M05 under another field variable.

A generic scalar/Yukawa nuisance can also imitate part of the weak-field radial structure if its coupling and range are allowed to match. The current `gamma(r)` residual is therefore robust against C0 normalization freedom but is **not yet a unique modified-gravity or quantum-gravity certificate** against the full comparator span.

## Q1–Q7 fingerprint — current

| Channel | M05 role |
|---|---|
| Q1 | classical modified proper-time/metric response only |
| Q2 | no branch-resolved quantum geometry |
| Q3 | strong classical source/backreaction modification through the scalar trace channel |
| Q4 | no quantum-mediator certificate |
| Q5 | extra classical scalar metric/curvature degree of freedom, not intrinsic quantum geometry noise |
| Q6 | causal classical weak-field response; exact retarded convention still to be written if needed for a time-dependent observable |
| Q7 | not itself standard quantized GR EFT C5; at low momentum its expansion overlaps higher-curvature EFT structure and must be comparator-profiled |

## Current first blocker

`FR_BROADER_COMPARATOR_QUOTIENT`:

1. retain `gamma(r)` and its multi-radius shape as the frozen C0 discriminator;
2. explicitly compare against a generic scalar/Yukawa nuisance and the non-duplicate M06 scalar-tensor family;
3. determine which distinctions are physical and which are merely frame/field-redefinition identities;
4. map the low-momentum expansion against C5/higher-curvature EFT directions;
5. assign terminal status only after this broader quotient is explicit.

## Sources

1. A. De Felice and S. Tsujikawa, *f(R) Theories*, Living Reviews in Relativity 13, 3 (2010): metric-f(R) scalar-tensor equivalence, stability conditions and the light-scalaron `gamma -> 1/2` limit.
2. Standard weak-field quadratic-gravity result specialized to the `m_W -> infinity` pure-f(R) limit: `gamma(r)=[3-exp(-M r)]/[3+exp(-M r)]`.
3. External RQIR comparator authority: `candidate_gravity/BASELINE_COMPARATORS.md`, blob `a2b45188710c885f979123f77fa7aad2273b9983`.
4. External RQIR funnel authority: `candidate_gravity/landscape/RQIR_FUNNEL_AUDIT_ITERATION137.md`, blob `2757e8fe1004b5c0caef51d6d9fee6f982ac81d4`.

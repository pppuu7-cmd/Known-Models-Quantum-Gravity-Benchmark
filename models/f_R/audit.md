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

Unlike M01–M04, this is not defined to be one of the frozen C0/C1/C2/C5 comparator classes. It is therefore the first queue item expected to produce a genuine finite model-vs-GR direction before broader nuisance/comparator profiling.

For traceful matter and finite `M`, the extra scalaron modifies the weak-field response. In the long-distance/large-M limit the extra scalar is Yukawa-suppressed and GR is recovered. Thus the benchmark can explicitly test the difference between

- a real nonzero modified-gravity residual relative to C0, and
- a signal that is not uniquely identifiable after scalar-force/nuisance comparators are admitted.

## Initial F0–F7 map

| Gate | Current state | Reason |
|---|---|---|
| F0 — dynamics | PASS_SCOPED | exact local metric action frozen |
| F1 — required limits | PASS_SCOPED | GR recovered for `M -> infinity` / momentum well below the scalaron mass, while matter remains ordinarily coupled |
| F2 — consistency | PASS_SCOPED_AROUND_MINKOWSKI | `F>0`, `f_RR>0`, `M^2>0`; extra mode is a scalar rather than the massive spin-2 ghost of generic quadratic Ricci-tensor gravity |
| F3 — RQIR hierarchy | CLASSICAL_PARTIAL | deterministic classical modified gravity supplies mean/retarded response but no independent quantum gravitational noise/operator hierarchy |
| F4 — comparator distinction | PRELIMINARY_DISTINCT_FROM_C0 | finite-M scalaron response differs from pure GR for traceful sources; broader comparator/nuisance span not yet closed |
| F5 — hard-constraint discriminator | BLOCKED | exact RQIR-facing observable and calibration quotient still to freeze |
| F6 — statistical identifiability | BLOCKED | parameter `M` and nuisance scalar-force directions not yet profiled |
| F7 — physical resources | BLOCKED | forbidden before F5/F6 closure |

## Pole / response fingerprint

Declared weak-field content:

- massless spin-2 GR pole;
- one additional scalar pole at mass scale `M`;
- no additional massive spin-2 pole from this pure `R^2` correction;
- scalar response couples to the trace sector of the matter stress tensor.

This already predicts a controlled direction that vanishes in the GR limit. However, a Yukawa-like scalar response is not automatically a unique quantum-gravity signature: conventional scalar-force or apparatus nuisance models may occupy a similar observable direction.

## Q1–Q7 fingerprint — preliminary

| Channel | M05 role |
|---|---|
| Q1 | classical modified proper-time/metric response only |
| Q2 | no branch-resolved quantum geometry |
| Q3 | strong classical source/backreaction modification through the scalar trace channel |
| Q4 | no quantum-mediator certificate |
| Q5 | extra classical scalar metric/curvature degree of freedom, not intrinsic quantum geometry noise |
| Q6 | causal retarded classical response to be frozen in the exact observable convention |
| Q7 | not itself standard quantized GR EFT C5; low-energy expansion can overlap higher-curvature EFT directions and must be comparator-profiled |

## Current first blocker

`FR_QUOTIENT_OBSERVABLE_FREEZE`:

1. freeze one weak-field source-to-detector observable sensitive to the scalar trace channel;
2. derive its finite-M response and GR-subtracted residual;
3. profile `M` and calibration/source-amplitude freedom;
4. test whether the residual is only C0-distinct or remains identifiable against applicable C4/C5/higher-curvature nuisance directions;
5. only then assign a terminal KMQGB state.

## Sources

1. A. De Felice and S. Tsujikawa, *f(R) Theories*, Living Reviews in Relativity 13, 3 (2010).
2. Standard metric-f(R) scalar-tensor equivalence and Minkowski stability results summarized in the same review.
3. External RQIR comparator authority: `candidate_gravity/BASELINE_COMPARATORS.md`, blob `a2b45188710c885f979123f77fa7aad2273b9983`.
4. External RQIR funnel authority: `candidate_gravity/landscape/RQIR_FUNNEL_AUDIT_ITERATION137.md`, blob `2757e8fe1004b5c0caef51d6d9fee6f982ac81d4`.

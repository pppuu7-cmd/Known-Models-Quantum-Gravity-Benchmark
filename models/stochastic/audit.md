# Model Audit — stochastic gravity / Einstein-Langevin Minkowski control

Benchmark ID: KMQGB-M04-STOCHASTIC
Concrete realization ID: SG-MINK-CONFORMAL-EL-001
Role: fluctuation/noise-kernel control (C2)
State: CLOSED / TERMINAL
Terminal status: EXACT_COMPARATOR_IDENTITY

## Frozen realization

Use the same low-curvature Minkowski scalar setup as M03, but promote the open-system fluctuation sector to the stochastic-gravity level:

- 4D background `eta_ab` plus classical stochastic metric perturbation `h_ab`;
- one free real quantized scalar field;
- `m=0`, `xi=1/6`;
- Minkowski vacuum `|0>`;
- `Lambda_ren=0` and `<0|T_ab^R[eta]|0>=0` renormalization convention;
- finite curvature-squared couplings retained explicitly;
- linearized Einstein-Langevin domain, low curvature and scales much larger than the Planck length.

The stochastic source `xi_ab` has

`<xi_ab(x)>_s = 0`

and covariance

`<xi_ab(x) xi_cd(y)>_s = N_abcd(x,y)`

with noise kernel

`N_abcd(x,y) = (1/2) < { t_ab(x), t_cd(y) } >`,

`t_ab = T_ab - <T_ab>`.

Schematically the linearized Einstein-Langevin equation is

`L_ab^{ cd} h_cd = 8 pi G [delta<T_ab^R> + xi_ab]`,

where the same influence-functional/CTP structure supplies the dissipative/retarded response paired with the stress-tensor fluctuations.

The stochastic metric is a classical random field in this benchmark; it is not promoted to a fundamental noncommuting metric operator.

## F0–F7 map

| Gate | Result | Reason |
|---|---|---|
| F0 — dynamics | PASS_SCOPED | explicit Einstein-Langevin stochastic equation derived from the open-system/influence-functional construction |
| F1 — required limits | PASS_SCOPED | averaging over the stochastic source returns the linearized semiclassical mean equation; turning off fluctuation forcing returns M03/C1 behavior in the matched domain |
| F2 — consistency | PASS_SCOPED | controlled renormalized Minkowski construction with conserved noise/response structure; stability requires the same declared treatment of unphysical Planck-scale runaways |
| F3 — RQIR hierarchy | STRONG_PASS_COMPARATOR | mean `J`, noise kernel `N`, and dissipation/retarded response are linked by the same CTP/influence-functional parent structure |
| F4 — comparator distinction | EXACT_COMPARATOR_IDENTITY_C2 | C2 is explicitly the stochastic gravity / noise-kernel baseline; this realization is a canonical member of that class |
| F5 — hard-constraint discriminator | N/A_AFTER_F4_IDENTITY | no nonzero model-vs-C2 novelty direction exists |
| F6 — statistical identifiability | N/A_AFTER_F4_IDENTITY | no independent residual parameter remains after exact C2 identity |
| F7 — physical resources | N/A_AFTER_F4_IDENTITY | no novel discriminator is being promoted |

## Q1–Q7 fingerprint

| RQIR channel | Scoped interpretation for M04 |
|---|---|
| Q1 — quantum clocks / proper time | stochastic metric fluctuations can induce stochastic proper-time variations, but the metric variable remains classical stochastic rather than a quantum operator |
| Q2 — superposed sources | matter stress fluctuations influence the stochastic geometry through the noise kernel; this is not branch-resolved quantum geometry |
| Q3 — backreaction / source rule | mean backreaction plus fluctuation forcing are both explicit |
| Q4 — gravity-mediated quantum information | stochastic classical mediation/noise alone does not certify a nonclassical gravitational information channel |
| Q5 — geometry fluctuations | PRIMARY DIRECT CHANNEL: induced metric fluctuations are the defining added structure relative to M03 |
| Q6 — causal/process structure | dissipation/retarded response is tied to the same open-system parent structure as the noise kernel |
| Q7 — low-energy quantum-gravity EFT | not identical to quantized GR EFT C5; M04 is the classical-stochastic C2 control |

## Comparator closure

The frozen RQIR comparator registry defines C2 as stochastic gravity / noise-kernel models in which stress-energy fluctuations drive classical metric fluctuations. `SG-MINK-CONFORMAL-EL-001` is exactly such an Einstein-Langevin realization.

With comparator state, renormalized parameters and observable domain matched,

`Delta_A^(M04-C2) = O_A^(M04) - O_A^(C2) = 0`.

Terminal KMQGB classification:

`EXACT_COMPARATOR_IDENTITY`.

This is not a failure of stochastic gravity. It establishes C2 as a stronger control than mean semiclassical gravity: any Candidate Gravity signature based only on extra classical metric noise, symmetrized two-point fluctuations or linked dissipative response can be absorbed by C2 unless it contains an additional nonclassical/operator-sensitive discriminator.

## Retained design lesson

Noise alone is not enough to certify quantum gravity. A future robust RQIR discriminator should seek structure that a positive classical stochastic metric process cannot reproduce after the same calibration/comparator quotient — for example an operator-ordering/noncommutativity or genuinely quantum-channel feature, provided it is derived from one consistent parent dynamics.

## Sources

1. B. L. Hu and E. Verdaguer, *Stochastic Gravity: Theory and Applications*, Living Reviews in Relativity 11, 3 (2008), DOI 10.12942/lrr-2008-3.
2. R. Martín and E. Verdaguer, *Stochastic semiclassical fluctuations in Minkowski spacetime*, arXiv:gr-qc/0001098.
3. External RQIR comparator authority: `candidate_gravity/BASELINE_COMPARATORS.md`, blob `a2b45188710c885f979123f77fa7aad2273b9983`.
4. External RQIR funnel authority: `candidate_gravity/landscape/RQIR_FUNNEL_AUDIT_ITERATION137.md`, blob `2757e8fe1004b5c0caef51d6d9fee6f982ac81d4`.

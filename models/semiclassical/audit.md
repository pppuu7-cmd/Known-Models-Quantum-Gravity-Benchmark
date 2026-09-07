# Model Audit — semiclassical Einstein gravity, conformal-scalar Minkowski control

Benchmark ID: KMQGB-M03-SEMICLASSICAL
Concrete realization ID: SCG-MINK-SCALAR-LR-001
Role: source/backreaction control (C1)
State: CLOSED / TERMINAL
Terminal status: EXACT_COMPARATOR_IDENTITY

## Frozen realization

Four-dimensional classical metric `g_ab` coupled to one quantized free real scalar field. The benchmark slice is

- scalar mass `m = 0`;
- curvature coupling `xi = 1/6` (4D conformal coupling);
- state: ordinary Minkowski vacuum `|0>`;
- background: `(R^4, eta_ab)`;
- renormalized cosmological constant `Lambda_ren = 0`;
- renormalization convention: `<0|T_ab^R[eta]|0> = 0`;
- finite curvature-squared couplings are retained explicitly as renormalized parameters `alpha(mu), beta(mu)` rather than hidden or zero-filled;
- observable domain: gauge-invariant linear metric response about Minkowski at low curvature and length/time scales parametrically larger than the Planck scale.

The standard renormalized semiclassical equation is

`G_ab[g] + Lambda_ren g_ab - 2(alpha A_ab + beta B_ab)[g] = 8 pi G <T_ab^R[g]>`.

`A_ab` and `B_ab` are the conserved local tensors obtained from the curvature-squared counterterms. Their finite coefficients can affect detailed linear response, but they do not alter the comparator-class identity: this realization is a member of C1 by construction.

This is a scoped control. It is not a claim about every cosmological, black-hole, strong-curvature, non-vacuum or nonperturbative semiclassical solution.

## Why this freeze is non-arbitrary

Anderson, Molina-París and Mottola formulate a gauge-invariant linear-response validity criterion for semiclassical gravity and apply it to a scalar field of arbitrary mass and curvature coupling in the Minkowski vacuum. The chosen `m=0, xi=1/6` slice is therefore contained in their analyzed family rather than being an unsupported parameter guess.

Hu and Verdaguer identify Minkowski spacetime plus the Minkowski vacuum as the simplest semiclassical solution when the renormalization convention sets the vacuum expectation value of the renormalized stress tensor to zero and `Lambda_ren=0`. Their review also makes explicit the distinction between mean semiclassical gravity and its stochastic Einstein-Langevin extension.

## F0–F7 map

| Gate | Result | Reason |
|---|---|---|
| F0 — dynamics | PASS_SCOPED | one declared renormalized semiclassical Einstein equation with classical metric and quantum scalar expectation-value source |
| F1 — required limits | PASS_SCOPED | flat vacuum with the declared renormalization condition recovers Minkowski/GR background; ordinary QFT matter remains the source sector; no UV-QG claim is made |
| F2 — consistency | PASS_SCOPED | covariant renormalized source/counterterms respect conservation structure; published gauge-invariant flat-space linear-response analysis is stable on scales much larger than the Planck length after unphysical runaway treatment |
| F3 — RQIR hierarchy | PARTIAL / INSUFFICIENT_FOR_FULL_QG_PROMOTION | the mean source `J=<T>` is fundamental to the equation and linear response can involve stress-tensor two-point structure, but the mean semiclassical equation does not contain an independent fundamental quantum/stochastic metric-noise/operator hierarchy |
| F4 — comparator distinction | EXACT_COMPARATOR_IDENTITY_C1 | C1 is defined as semiclassical gravity / controlled semiclassical EFT; the frozen realization lies inside that baseline class |
| F5 — hard-constraint discriminator | N/A_AFTER_F4_IDENTITY | no nonzero model-vs-C1 direction exists to send through the quotient |
| F6 — statistical identifiability | N/A_AFTER_F4_IDENTITY | no independent residual parameter remains after exact C1 identity |
| F7 — physical resources | N/A_AFTER_F4_IDENTITY | no novel discriminator is being promoted |

## Q1–Q7 fingerprint

| RQIR channel | Scoped interpretation for M03 |
|---|---|
| Q1 — quantum clocks / proper time | proper time is computed from a classical mean metric; M03 does not supply a quantum superposition of geometries |
| Q2 — superposed sources | the source rule is expectation-value backreaction; branch-resolved quantum geometry is not part of the mean equation |
| Q3 — backreaction / source rule | PRIMARY DIRECT CHANNEL: `G ~ <T>` is exactly the defining architecture |
| Q4 — gravity-mediated quantum information | mean classical geometry alone does not certify a quantum gravitational mediator/channel |
| Q5 — geometry fluctuations | independent metric noise is absent from the mean equation; the stress-tensor fluctuation/noise-kernel extension belongs to M04/C2 |
| Q6 — causal/process structure | retarded/gauge-invariant linear response exists in the controlled perturbative analysis, but no independent noncommuting gravitational process object is supplied by the mean equation |
| Q7 — low-energy quantum-gravity EFT | not a C5 quantum-GR EFT realization; M02 covers that separate comparator class |

These entries are interface fingerprints, not seven independent consistency tests.

## Comparator closure

The frozen RQIR comparator registry defines C1 as semiclassical gravity with representative structure `G_mn = 8 pi G <T_mn>` or the appropriate controlled semiclassical EFT formulation.

For a comparator instantiated with the same state, renormalized parameters, scheme and observable domain,

`Delta_A^(M03-C1) = O_A^(M03) - O_A^(C1) = 0`.

Therefore the terminal KMQGB classification is

`EXACT_COMPARATOR_IDENTITY`.

This is a successful control result. It means M03 supplies no novelty direction relative to C1. It does **not** mean that semiclassical gravity is inconsistent or experimentally ruled out.

## Retained limitation

Mean-only closure is insufficient evidence for a full quantum-gravitational interface whenever the proposed discriminator requires an independent gravitational noise/operator hierarchy, noncommuting ordered response or higher quantum gravitational correlators. That is an F3/F4 promotion limitation, not a general theory failure.

The next benchmark M04 deliberately adds the stress-tensor noise kernel and Einstein-Langevin stochastic metric response to test the stronger C2 control.

## Sources

1. B. L. Hu and E. Verdaguer, *Stochastic Gravity: Theory and Applications*, Living Reviews in Relativity 11, 3 (2008), DOI 10.12942/lrr-2008-3.
2. P. R. Anderson, C. Molina-París and E. Mottola, *Linear Response, Validity of Semi-Classical Gravity, and the Stability of Flat Space*, arXiv:gr-qc/0209075.
3. External RQIR comparator authority: `candidate_gravity/BASELINE_COMPARATORS.md`, blob `a2b45188710c885f979123f77fa7aad2273b9983`.
4. External RQIR funnel authority: `candidate_gravity/landscape/RQIR_FUNNEL_AUDIT_ITERATION137.md`, blob `2757e8fe1004b5c0caef51d6d9fee6f982ac81d4`.

# T3-02 Audit — full Planck-crossover asymptotic-safety amplitude vector

Benchmark ID: KMQGB-T3-M02-AS-CROSSOVER  
Concrete realization ID: `AS-SCALAR2TO2-PLANCK-CROSSOVER-2026-001`  
Role: strengthen second-wave asymptotic-safety audit beyond the non-unique UV exponent `p_UV=0`  
State: **TERMINAL — `BLOCKED_MISSING_REQUIRED_OBJECT`**

## Terminal decision

The 2026 Chiesa–Pawlowski–Reichert calculation is sufficiently concrete to freeze the mediated Lorentzian scalar-scattering crossover, but it explicitly does **not** yet provide the full direct four-scalar/contact contribution `A_4` needed for a contact-complete, crossing-complete amplitude in the same approximation.

Because the benchmark discriminator is the **full Planck-crossover vector**, not the already-nonunique UV exponent, the missing contact-complete observable is a required object rather than an optional refinement.

Therefore T3-02 is terminally classified

`BLOCKED_MISSING_REQUIRED_OBJECT`

at

`AS_CONTACT_COMPLETE_CROSSOVER_VECTOR`.

This is **not** a consistency failure of asymptotic safety and is **not** evidence that the published mediated amplitude is wrong.

## Frozen source calculation

Use Chiesa, Pawlowski & Reichert, *Towards Two-to-Two Scattering of Scalars in Asymptotically Safe Quantum Gravity*, arXiv:2603.10168 (2026).

Published scoped results include:

- momentum-dependent scalar-graviton three-point vertex computed with functional RG;
- analytic continuation/reconstruction toward the Lorentzian on-shell branch;
- graviton-mediated scalar `2->2` amplitude and cross section;
- GR behavior in the infrared;
- nontrivial angular dependence through the crossover;
- bounded high-energy behavior with a constant trans-Planckian amplitude/cross-section scaling compatible with the second-wave `p_UV=0` result;
- resonance-like/turnover structure in the Planckian crossover.

The missing published object is the fully incorporated direct four-scalar/contact amplitude in the same reproducible approximation and its resulting crossing/forward completion.

## Frozen target vector

`I_AS = {IR_GR, E_x, H_peak, W_peak, theta_dependence, A_UV, p_UV, contact_fraction, crossing_completion}`

where

- `IR_GR`: low-energy GR matching;
- `E_x`: crossover scale;
- `H_peak,W_peak`: crossover/peak height and width;
- `theta_dependence`: angular profile;
- `A_UV,p_UV`: UV plateau normalization and exponent;
- `contact_fraction`: direct `A_4` contribution;
- `crossing_completion`: consistent combined `s,t,u,A_4` observable including forward treatment.

The first seven components can be partly constrained from the mediated calculation, but the last two are not presently available as a complete published same-realization observable. Since they can alter the Planck-crossover shape, profiling an incomplete vector would overstate uniqueness.

## F0-F7 terminal map

| Gate | State | Reason |
|---|---|---|
| F0 dynamics | PASS_SCOPED_TRUNCATION | explicit momentum-dependent fRG vertex/propagator approximation |
| F1 IR limit | PASS_SCOPED | GR behavior recovered at low energy |
| F2 consistency | PASS_PARTIAL | bounded UV behavior and positive spectral evidence; full contact-completed unitarity not established by this object |
| F3 observable | PASS_PARTIAL | mediated on-shell amplitude/cross section explicit |
| F4 distinction | PARTIAL | `p_UV=0` already known non-unique; richer mediated crossover structure exists |
| F5 hard discriminator | **BLOCKED_MISSING_REQUIRED_OBJECT** | contact-complete/crossing-complete amplitude absent |
| F6 identifiability | BLOCKED | cannot profile full vector before F5 object exists |
| F7 resources | N/A | theory/scattering benchmark |

## Candidate Gravity design lesson

A full response/crossover shape is a stronger design target than one asymptotic exponent, **but only if every contribution required by the same symmetry/crossing problem is present**.

For future KG work this becomes a hard rule:

> do not freeze a supposedly unique multi-channel fingerprint while omitting a contact, constraint, Ward, or direct-interaction term that can modify the same observable.

This is the amplitude analogue of requiring Source/Ward/contact closure in the main RQIR Candidate Gravity chain.

## Reopen condition

T3-02 may be reopened in a future wave only when a public reproducible same-realization result provides the direct contact contribution and a crossing/forward-complete scalar-scattering observable suitable for the full `I_AS` quotient.

## Terminal completion

**100% — terminally classified as BLOCKED, not solved.**

## Sources

1. A. P. Chiesa, J. M. Pawlowski, M. Reichert, arXiv:2603.10168 (2026).
2. A. Pastor-Gutierrez et al., Phys. Rev. D 111, 106005 (2025).
3. J. M. Pawlowski, M. Reichert, J. Wessely, Phys. Lett. B 880 (2026) 140844.
4. T. Draper, B. Knorr, C. Ripken, F. Saueressig, Phys. Rev. Lett. 125, 181301 (2020).

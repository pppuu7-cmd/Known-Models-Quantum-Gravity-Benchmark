# T3-02 Audit — full Planck-crossover asymptotic-safety amplitude vector

Benchmark ID: KMQGB-T3-M02-AS-CROSSOVER
Concrete realization ID: `AS-SCALAR2TO2-PLANCK-CROSSOVER-2026-001`
Role: strengthen second-wave asymptotic-safety audit beyond the non-unique UV exponent `p_UV=0`
State: ACTIVE / NONTERMINAL

## Motivation

Second-wave S2-M02 proved that the single asymptotic observable

`p_UV = lim d ln|A|/d ln s = 0`

is not unique to asymptotic safety: an independent Lorentzian quantum-effective-action construction also gives scale-free trans-Planckian scattering.

T3-02 therefore freezes the **full crossover shape** rather than the UV exponent alone.

## Frozen source calculation

Use Chiesa, Pawlowski & Reichert, *Towards Two-to-Two Scattering of Scalars in Asymptotically Safe Quantum Gravity*, arXiv:2603.10168 (2026).

The calculation supplies

- a fully momentum-dependent scalar-scalar-graviton three-point vertex computed with the functional RG in Euclidean signature;
- reconstruction/analytic continuation to the Lorentzian on-shell branch;
- graviton-mediated scalar `2->2` scattering amplitude and cross section;
- GR behavior in the infrared;
- dimensionful scalar-graviton Newton coupling scaling as `G_phiphi h ~ 1/p^2` in the UV;
- a bounded scattering amplitude approaching a constant in the trans-Planckian regime;
- nontrivial angular dependence, particularly in the crossover region;
- a resonance-like/peak structure near the transition region whose physical interpretation remains open.

The published paper explicitly omits the direct four-scalar contact amplitude `A_4` from its main full amplitude, although a leading-order contact contribution and subsequent work are discussed. A September-2026 ERG conference presentation reports progress toward resumming the gravitational contact amplitude directly in Lorentzian signature, but a conference description is not silently promoted to the same authority level as a published complete S-matrix.

## Frozen crossover vector

Define

`I_AS = {IR_GR, E_x, H_peak, W_peak, theta_dependence, A_UV, p_UV, contact_fraction, crossing_completion}`

where

- `IR_GR`: normalized agreement with the GR low-energy amplitude/cross section;
- `E_x`: operational crossover energy relative to the Planck scale, defined by a frozen fractional departure from the IR and approach to the UV plateau;
- `H_peak`: height of the resonance-like maximum relative to the UV plateau/IR continuation;
- `W_peak`: width of the crossover/peak in `ln sqrt(s)`;
- `theta_dependence`: angular shape at several pre-registered scattering angles;
- `A_UV`: asymptotic plateau normalization;
- `p_UV`: asymptotic scaling exponent (already known to be non-unique);
- `contact_fraction`: contribution of the direct four-scalar/contact term to the same observable;
- `crossing_completion`: consistency of the combined `s,t,u,A_4` amplitude under crossing and the forward-limit treatment.

The precise numerical definitions of `E_x,H_peak,W_peak` must be extracted from the published interpolation/data before terminal classification.

## Why this vector may be stronger

A generic UV completion can share `p_UV=0` while differing in

- the energy at which screening begins;
- the angular evolution through the Planck regime;
- whether a resonance-like peak appears;
- the peak height/width;
- the UV normalization;
- contact/crossed-channel relations.

A useful AS-specific residual must therefore survive profiling of the **whole vector**, not one exponent.

## F0-F7 map

| Gate | State | Reason |
|---|---|---|
| F0 dynamics | PASS_SCOPED_TRUNCATION | momentum-dependent fRG vertex and propagator approximation frozen |
| F1 IR limit | PASS_SCOPED | published Lorentzian amplitude reproduces GR behavior at low energy |
| F2 consistency | PASS_PARTIAL | bounded UV amplitude and positive/self-consistent spectral evidence support the sector; full contact-completed unitarity remains unfinished |
| F3 observable | PASS_PARTIAL | on-shell mediated amplitude/cross section explicit; direct contact term incomplete in published calculation |
| F4 comparator distinction | ACTIVE | UV exponent alone fails; full crossover vector not yet profiled |
| F5 hard discriminator | BLOCKED_CONTACT_COMPLETE_VECTOR | cannot claim full S-matrix uniqueness before `A_4` and crossed/forward completion |
| F6 identifiability | BLOCKED | needs same-domain comparator vector |
| F7 resources | N/A | theory/scattering benchmark |

## Same-domain comparators to profile

At minimum:

1. Draper–Knorr–Ripken–Saueressig quantum-effective-action scattering, which already matches the UV scale-free exponent;
2. other UV-soft/finite scalar-scattering amplitudes with the same external states;
3. local/EFT C5 only in the sub-Planckian common domain;
4. string/nonlocal amplitudes only after matching external states and kinematic domain.

## Candidate Gravity design lesson

A single asymptotic exponent is a poor design target. A future KG model should predict a **crossover vector** whose normalization, shape, ordered response and consistency terms are linked by the same parent dynamics.

The analogous interface lesson is to use the full time/frequency-dependent response/noise/noncommutativity profile rather than one static number.

## Current blocker

`AS_CONTACT_COMPLETE_CROSSOVER_VECTOR`:

1. extract numerical/functional definitions of the peak and crossover from the 2026 amplitude;
2. freeze 3-5 scattering angles and compute the normalized vector components;
3. incorporate a public, reproducible direct-contact `A_4` result when available;
4. profile against at least one same-domain scale-free UV amplitude beyond the UV exponent;
5. terminally classify only after the combined vector is fixed.

## Operational completion estimate

**50%**.

## Sources

1. A. P. Chiesa, J. M. Pawlowski, M. Reichert, arXiv:2603.10168 (2026).
2. A. Pastor-Gutierrez et al., Phys. Rev. D 111, 106005 (2025), timelike asymptotically-safe matter scattering.
3. J. M. Pawlowski, M. Reichert, J. Wessely, Phys. Lett. B 880 (2026) 140844, positive self-consistent Lorentzian graviton spectral function.
4. T. Draper, B. Knorr, C. Ripken, F. Saueressig, Phys. Rev. Lett. 125, 181301 (2020), independent scale-free UV scattering comparator.
5. ERG2026 presentation by A. P. Chiesa (3 Sep 2026), reporting ongoing contact-amplitude completion; retained as current-progress evidence, not yet final published authority.

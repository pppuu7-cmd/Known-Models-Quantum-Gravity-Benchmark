# Model Audit — Lorentzian asymptotic-safety scalar-scattering realization

Benchmark ID: KMQGB-S2-M02-AS
Concrete realization ID: AS-SCALAR2TO2-LOR-2026-001
Role: Lorentzian asymptotic-safety / UV-completion control
State: TERMINAL
Final status: `OPERATIONALLY_DEGENERATE`

## Frozen realization

Use the 2026 Chiesa–Pawlowski–Reichert computation of graviton-mediated `2 -> 2` scattering of a massless scalar field in asymptotically safe quantum gravity.

Declared scope:

- flat-background quantum gravity plus one minimally coupled massless scalar;
- functional renormalisation group determination of the full momentum dependence of the scalar–scalar–graviton 1PI vertex for spacelike momenta;
- reconstruction/analytic continuation to the Lorentzian timelike branch;
- resummed single-graviton-mediated scalar scattering amplitude;
- fixed-angle / `s`-channel ultraviolet scaling as the frozen terminal observable;
- forward-scattering/contact-completion issues are explicitly outside this scoped terminal observable.

The 2026 self-consistent Lorentzian graviton spectral-function computation of Pawlowski–Reichert–Wessely is retained as independent consistency support for the same research program, not silently treated as the identical truncation used in the scalar-scattering calculation.

## Frozen observable

Define the asymptotic fixed-angle amplitude scaling exponent

`p_UV = lim_{s->infinity} d ln |A_s(s,theta_fixed)| / d ln s`.

The 2026 asymptotic-safety calculation finds that the Lorentzian amplitude approaches a finite constant in the UV once the scale-invariant fixed-point regime is reached. Therefore

`p_UV^AS = 0`.

In the IR, the amplitude returns to the GR behavior in the declared approximation.

## Same-domain UV comparator

Use the independent Lorentzian quantum-effective-action construction of Draper, Knorr, Ripken and Saueressig (PRL 2020) for gravity-mediated scattering of massless scalar fields. Their explicit form-factor realization is designed to be scale-free at trans-Planckian energy, with asymptotically constant partial-wave amplitudes. For example,

`lim_{s->infinity} a_0(s) = 1/(12 c_R)`,

`lim_{s->infinity} a_2(s) = -1/(60 c_C)`.

Thus the same frozen asymptotic exponent is

`p_UV^DKRS = 0`.

This comparator is not string theory and is not the same microscopic construction as the asymptotic-safety flow.

## Exact scoped quotient

For the frozen observable,

`Delta_p = p_UV^AS - p_UV^DKRS = 0`.

Therefore the statement **"the gravitationally mediated amplitude becomes scale-free / constant rather than growing with energy"** is not a unique signature of asymptotic safety.

This does not imply that the full amplitudes are identical. The detailed Planck-scale crossover, normalization, angular dependence, pole/continuum structure and resonance-like feature in the 2026 asymptotic-safety result may distinguish the models if a broader observable vector is frozen later.

## F0-F7 terminal map

| Gate | Result | Reason |
|---|---|---|
| F0 dynamics | PASS_SCOPED_APPROXIMATION | explicit fRG flow and momentum-dependent scalar–graviton vertex computation |
| F1 required limits | PASS_SCOPED | scattering returns to GR behavior at small energies |
| F2 consistency | PASS/PARTIAL_SCOPED | frozen amplitude remains bounded and compatible with UV unitarity; positive Lorentzian graviton spectral evidence independently supports absence of a simple ghost/tachyon instability in related truncations |
| F3 RQIR hierarchy | PARTIAL | physical Lorentzian scattering response is concrete; complete higher CTP/noise hierarchy is not frozen |
| F4 comparator distinction | FAIL_TO_DISTINGUISH_IN_UV_EXPONENT | independent UV QFT comparator has same scale-free exponent |
| F5 hard discriminator | ZERO_FOR_FROZEN_EXPONENT | `Delta_p=0` after the same-domain UV quotient |
| F6 identifiability | NOT_APPLICABLE_FOR_ZERO_EXPONENT_RESIDUAL | no independent beta direction in the frozen one-number observable |
| F7 resources | NOT_APPLICABLE_FOR_ZERO_EXPONENT_RESIDUAL | a zero discriminator cannot identify the theory |

## Forward-scattering guardrail

The 2026 paper notes that the nonperturbative single-graviton-mediated `t`-channel still has the familiar forward divergence if the required four-scalar/contact contribution is not included. This terminal classification therefore deliberately uses the computed fixed-angle / `s`-channel UV exponent and does **not** claim that every crossed amplitude or full S-matrix sector is already closed.

## Terminal interpretation

`AS-SCALAR2TO2-LOR-2026-001` is not rejected. It gives a concrete nonperturbative Lorentzian scattering realization with GR in the IR and a bounded fixed-point amplitude in the UV.

However, its simplest robust high-energy fingerprint — asymptotically scale-free scattering — is shared by an independent UV-complete Lorentzian quantum-effective-action construction. In that frozen observable it is therefore `OPERATIONALLY_DEGENERATE`.

## Sources

1. A. P. Chiesa, J. M. Pawlowski, M. Reichert, *Towards Two-to-Two Scattering of Scalars in Asymptotically Safe Quantum Gravity*, arXiv:2603.10168 (2026).
2. J. M. Pawlowski, M. Reichert, J. Wessely, *Self-consistent graviton spectral function in Lorentzian quantum gravity*, Phys. Lett. B 880 (2026) 140844, arXiv:2507.22169.
3. J. Fehre, D. F. Litim, J. M. Pawlowski, M. Reichert, *Lorentzian Quantum Gravity and the Graviton Spectral Function*, Phys. Rev. Lett. 130, 081501 (2023), arXiv:2111.13232.
4. T. Draper, B. Knorr, C. Ripken, F. Saueressig, *Finite Quantum Gravity Amplitudes: No Strings Attached*, Phys. Rev. Lett. 125, 181301 (2020), arXiv:2007.00733.

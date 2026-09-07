# Model Audit — type-II closed-string four-graviton / low-energy matching control

Benchmark ID: KMQGB-M09-STRING-EFT
Concrete realization ID: TYPEII-T6-GRAV4-TREE-001
Role: string quantum-gravity scattering / UV-completion versus low-energy EFT control
State: CLOSED / TERMINAL UNDER CURRENT FROZEN COMPARATOR PROTOCOL
Terminal status: BLOCKED_PROTOCOL_MISMATCH

## Frozen 4D realization

Use type-II closed superstring theory at tree level (genus zero), with six spatial dimensions compactified on a flat generic six-torus `T^6`. External states are the four-dimensional **zero-mode gravitons**: momenta and polarizations lie entirely in the noncompact four dimensions and carry no internal KK/winding quantum numbers.

The observable is the normalized four-graviton scattering form factor after matching the four-dimensional Einstein normalization. The compactification volume and `kappa_10 -> kappa_4` normalization cancel in the normalized string/GR ratio.

A classic direct calculation shows that, after compactifying six dimensions, the zero-slope limit of the four-particle type-II string amplitude agrees with the four-dimensional GR graviton helicity amplitudes. This supplies the required 4D low-energy anchor without inventing a compactification-dependent GR limit.

The audit is deliberately **tree-level four-graviton only**. Loop-sensitive torus moduli sums, compactification thresholds and non-graviton observables are not silently imported into this realization.

## Exact tree-level string object

Up to the standard external-polarization kinematic factor, the type-II tree four-graviton amplitude contains the Virasoro-Shapiro factor

`A_tree ~ K * [64/(alpha'^3 s t u)] * Π_{x=s,t,u} Gamma(1-alpha' x/4)/Gamma(1+alpha' x/4)`,

with `s+t+u=0` for massless external gravitons.

After dividing by the matched four-dimensional GR/supergravity tree amplitude, define the dimensionless normalized form factor

`F_VS(s,t,u) = Π_{x=s,t,u} Gamma(1-alpha' x/4)/Gamma(1+alpha' x/4)`,

so

`F_VS -> 1` as `alpha' -> 0`.

This is the frozen M09 observable.

## Low-energy analytic fingerprint

Using the Gamma-function expansion and `s+t+u=0`,

`ln F_VS = [zeta(3) alpha'^3/32] s t u + O(alpha'^5 E^10)`

in the small-`alpha'` domain (up to the fixed Mandelstam convention above). Equivalently the first characteristic local type-II correction is the familiar tree-level `alpha'^3 zeta(3) R^4` interaction, followed by correlated higher `D^(2k) R^4` terms.

The exact numerical normalization of a particular operator basis is convention-dependent, but the Gamma-function form factor and its correlated zeta-valued expansion are the invariant benchmark object.

## Common-domain C5 quotient

The frozen RQIR C5 comparator is **low-energy perturbative quantum GR / gravitational EFT**. Its valid common domain with M09 is the sub-string-threshold region

`|alpha' s|, |alpha' t|, |alpha' u| << 1`.

In that domain, the analytic string corrections are precisely higher-derivative local EFT data. At any fixed finite order, C5 with the allowed Wilson coefficients can reproduce the corresponding `R^4`, `D^(2k)R^4`, ... coefficients. Therefore a finite-order low-energy deviation from pure Einstein gravity is **not uniquely string-identifying**.

Retained scoped result:

`M09 low-energy slice -> OPERATIONALLY_DEGENERATE_WITH_C5_EFT`.

This is the same general EFT principle seen in M08, now with string theory supplying a highly correlated UV-matched set of Wilson coefficients.

## Why the full string pole tower cannot be used to 'beat C5'

The full Virasoro-Shapiro amplitude contains non-polynomial Gamma-function structure and an infinite tower of massive string poles. Those are genuinely beyond any finite local low-energy EFT truncation.

However, resolving the first massive string pole requires leaving the domain in which C5 was defined as a low-energy comparator. Comparing the full threshold-resolving string amplitude to a C5 truncation outside its validity range would be a straw-man comparison and violates the RQIR common-domain discipline.

The current frozen comparator registry has no explicit UV-completion comparator class spanning alternative high-energy quantum-gravity S-matrices at the string scale. Therefore the benchmark cannot honestly turn the string pole tower into a **unique** RQIR residual against a valid competing UV model.

## F0-F7 terminal map

| Gate | State | Reason |
|---|---|---|
| F0 — dynamics | PASS_SCOPED | exact genus-zero type-II four-graviton S-matrix object and 4D zero-mode external sector frozen |
| F1 — required limits | PASS | compactified zero-slope limit agrees with 4D GR helicity amplitude |
| F2 — consistency | PASS_SCOPED_TREE | tree amplitude has standard crossing/factorization pole structure; no M07-like standard massive-spin-2 ghost gate is encountered |
| F3 — RQIR hierarchy | PASS_SCATTERING_SUBCHANNEL / PARTIAL_FULL_INTERFACE | exact scattering object exists; full laboratory Q1-Q7 source-detector hierarchy is not claimed |
| F4 — comparator distinction | LOW_ENERGY_DEGENERATE_WITH_C5 | finite-order sub-threshold analytic corrections are ordinary C5 EFT Wilson data |
| F5 — hard discriminator | BLOCKED_NO_COMMON_DOMAIN_UV_COMPARATOR | string pole tower becomes distinctive only where low-energy C5 is no longer an admissible comparator |
| F6 — identifiability | BLOCKED_PROTOCOL | no frozen UV comparator/nuisance family at the string threshold |
| F7 — resources | NOT_REACHED | no unique common-domain discriminator to resource-certify |

## Terminal decision under the current protocol

`BLOCKED_PROTOCOL_MISMATCH`.

This terminal first-queue classification contains two retained subresults:

1. **sub-string-threshold common domain:** string tree corrections are `OPERATIONALLY_DEGENERATE` with C5 EFT after Wilson-coefficient profiling;
2. **string-threshold/full-pole domain:** the amplitude has genuinely new string structure, but the current frozen RQIR comparator registry lacks a valid UV-completion comparator in the same domain, so no unique RQIR residual is authorized.

This is not a failure of string theory and not evidence against its consistency. It is a limitation of the current benchmark/comparator scope.

## What would unblock a future M09-UV branch

A future second-wave benchmark may add a standalone KMQGB UV comparator overlay (without modifying core RQIR) containing concrete high-energy alternatives, for example:

- a fixed ghost-free/nonlocal form-factor model;
- a concrete asymptotic-safety trajectory/truncation with an S-matrix/kernel;
- another explicit string compactification or string-inspired UV amplitude;
- any other UV completion with a common external-state and energy domain.

Then the string pole/residue pattern, Regge behavior, coefficient correlations and crossing/factorization structure can be compared fairly.

## Sources

1. S. Sannan, *Gravity as the limit of the type-II superstring theory*, Phys. Rev. D 34, 1749 (1986): after compactifying six spatial dimensions, the four-particle string amplitude agrees with 4D GR helicity amplitudes in the zero-slope limit.
2. M. B. Green and P. Vanhove, type-II four-graviton amplitude literature: explicit Virasoro-Shapiro tree factor and low-energy higher-derivative expansion.
3. Type-II effective-action literature: leading tree-level `alpha'^3 zeta(3) R^4` interaction.
4. E. Claasen and M. Doroudiani, Phys. Rev. Lett. 134, 201601 (2025): modern one-loop type-II four-graviton low-energy expansion and transcendental structure; retained as context, not silently included in this tree-level realization.
5. External RQIR C5 comparator authority: perturbative quantum GR / low-energy gravity EFT, valid only in its declared low-energy domain.

# Model Audit — Lorentzian asymptotic-safety spectral realization

Benchmark ID: KMQGB-S2-M02-AS
Concrete realization ID: AS-LQG-SPECTRAL-CS-MINK-001
Role: Lorentzian asymptotic-safety / UV-completion control
State: ACTIVE / NONTERMINAL

## Frozen realization

Use the self-consistent Lorentzian graviton spectral-function computation of Pawlowski, Reichert and Wessely, published in Physics Letters B 880 (2026) 140844, together with its explicit spectral Callan-Symanzik flow setup.

Declared scope:

- metric quantum gravity;
- flat Minkowski background;
- linear split `g_mn = eta_mn + sqrt(32 pi G_N) sqrt(Z_h) h_mn`;
- fields `Phi=(h_mn,c_m,bar c_m)`;
- Lorentzian spectral functional RG / renormalized Callan-Symanzik flow;
- physical on-shell renormalisation;
- full self-consistent graviton spectral function fed back into the flow;
- de-Donder/harmonic gauge `alpha=beta=1` in the cited approximation;
- physical cosmological constant `Lambda_{k=0}=0`;
- full momentum-dependent graviton two-point function with Einstein-Hilbert-type vertices in the stated approximation.

This is a concrete approximation/trajectory, not the phrase "asymptotic safety" used as a program label.

## Frozen primary object

The primary RQIR-facing object is the transverse-traceless graviton spectral function `rho_h(lambda)` and the corresponding timelike propagator / response reconstructed from a Kallen-Lehmann representation.

The 2026 computation finds:

- positive graviton spectral function;
- a massless one-graviton peak;
- a multigraviton continuum;
- close-to-quadratic ultraviolet spectral decay;
- unit total spectral weight in the physical on-shell scheme;
- an asymptotic-state sum rule.

The earlier 2023 Lorentzian study likewise found a positive spectral function with no ghost/tachyonic instability in its approximation.

## F0-F7 current map

| Gate | State | Reason |
|---|---|---|
| F0 dynamics | PASS_SCOPED_APPROXIMATION | explicit Lorentzian spectral RG flow, fields, gauge, regulator and vertex truncation are frozen |
| F1 required limits | PASS/PARTIAL | classical on-shell dispersion and low-energy gravity are built into the physical scheme; full phenomenological matching is not yet the active gate |
| F2 consistency | STRONG_PARTIAL_PASS | positive spectral density, no ghost/tachyon signal in the frozen two-point sector, unit spectral weight; full unitarity requires scattering/vertex completion |
| F3 RQIR hierarchy | PARTIAL_STRONG_TWO_POINT | retarded/timelike two-point spectral response is concrete; complete higher-point spectral vertex hierarchy is not yet frozen self-consistently |
| F4 comparator distinction | DOMAIN_SPLIT_OPEN | sub-Planckian analytic corrections can be represented in low-energy C5 EFT; trans-Planckian behavior needs a same-domain UV comparator |
| F5 hard discriminator | BLOCKED_COMMON_DOMAIN_UV_COMPARATOR | no fair fixed UV comparator quotient yet |
| F6 identifiability | BLOCKED | cannot precede F5 and full scattering observable freeze |
| F7 resources | BLOCKED | cannot precede F5/F6 |

## Current scattering evidence

A 2025 asymptotically-safe Standard Model calculation of `e+ e- -> mu+ mu-` uses timelike momentum-dependent 1PI correlation functions and graviton spectral reconstructions. It finds a full cross section decreasing in the ultraviolet and compatible with unitarity bounds. This is important evidence that the spectral construction can feed an actual observable.

However, the current benchmark does not yet equate that matter-scattering truncation with the 2026 self-consistent spectral two-point approximation without an explicit shared approximation ledger. The two sources are treated as linked evidence, not silently identical calculations.

## Comparator/domain issue

Two regimes must remain separate:

1. **Low energy / sub-Planckian:** any finite analytic imprint of a UV completion is representable as gravitational EFT Wilson data. A C5 EFT with the corresponding allowed coefficients can absorb such a finite-order expansion. No unique asymptotic-safety claim follows merely from low-energy local coefficients.
2. **UV / trans-Planckian:** asymptotic-safety scaling and UV scattering behavior are the target, but low-energy C5 is outside its declared validity domain. A fair terminal uniqueness test therefore requires another UV-complete comparator or a protocol extension.

This mirrors the common-domain guardrail discovered in first-wave M09 string scattering.

## Current first blocker

`AS_UV_COMMON_DOMAIN_AND_VERTEX_FREEZE`:

1. freeze one scattering observable generated using the same self-consistent spectral approximation or an explicitly compatible vertex ledger;
2. specify the exact UV scaling observable and its nuisance freedom;
3. introduce at least one same-domain UV comparator (candidate supplied by second-wave S2-M05);
4. determine whether the positive spectral function plus UV scaling is unique to the chosen asymptotic-safety realization or shared by the wider UV-completion comparator span;
5. do not call the program inconsistent merely because the full vertex/unitarity proof is incomplete.

## Current completion estimate

Operational completion of this audit: **45%**.

## Sources

1. J. M. Pawlowski, M. Reichert, J. Wessely, *Self-consistent graviton spectral function in Lorentzian quantum gravity*, Phys. Lett. B 880 (2026) 140844, arXiv:2507.22169.
2. J. Fehre, D. F. Litim, J. M. Pawlowski, M. Reichert, *Lorentzian Quantum Gravity and the Graviton Spectral Function*, Phys. Rev. Lett. 130, 081501 (2023), arXiv:2111.13232.
3. A. Pastor-Gutierrez, J. M. Pawlowski, M. Reichert, G. Ruisi, `e+e- -> mu+mu- in the Asymptotically Safe Standard Model`, Phys. Rev. D 111, 106005 (2025), arXiv:2412.13800.
4. A. Eichhorn, *Asymptotically safe quantum gravity and its phenomenology — a review*, arXiv:2606.21522 (2026).

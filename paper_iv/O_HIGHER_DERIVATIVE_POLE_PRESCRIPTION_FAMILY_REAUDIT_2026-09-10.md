# Perturbative / higher-derivative quantum gravity — pole-prescription and observable family re-audit (Iter227)

**Date:** 2026-09-10  
**RQIR Core:** v1.0 FROZEN  
**Family:** `PERTURBATIVE_HIGHER_DERIVATIVE`  
**Gate:** `PERTURBATIVE_HIGHER_DERIVATIVE_POLE_PRESCRIPTION_CAUSALITY_OBSERVABLE_FAMILY_CLOSURE_REAUDIT`

## Question

Does any current higher-derivative / quadratic-gravity realization close, without cross-branch splicing,

`UV consistency/renormalizability -> pole/quantization prescription -> unitarity -> causality/stability -> RG/IR matching -> normalized physical observable -> GR/EFT comparator -> uncertainty`,

or must the family remain nonterminal?

## A. Family-level baseline: strict renormalizability is a strong established control

Quadratic gravity with curvature-squared terms has the classic perturbative renormalizability result, and Buoninfante, JHEP 07 (2025) 175, gives a modern peer-reviewed synthesis emphasizing strict renormalizability and the predictive sub-Planckian cosmological sector.

Classification:

`PASS_FAMILY_STRUCTURAL_CONTROL__STRICT_PERTURBATIVE_RENORMALIZABILITY_OF_QUADRATIC_ACTION_CLASS`.

This does not choose the physical Hilbert space / pole prescription and therefore does not solve unitarity by itself.

## B. Ordinary Feynman/Stelle branch

With the ordinary Feynman interpretation of the fourth-order propagator, the additional massive spin-2 pole has negative residue / ghost character. Renormalizability therefore does not imply a standard positive-norm asymptotic-state interpretation.

Scoped disposition:

`FAIL_SCOPED_STANDARD_FEYNMAN_POSITIVE_NORM_UNITARITY_FOR_MASSIVE_SPIN2_GHOST_REALIZATION`.

This is a branch-level failure of the ordinary particle interpretation, not a failure of every quantization of the same higher-derivative action.

## C. Fakeon / purely-virtual-particle branch

Piva, Eur. Phys. J. Plus 138, 876 (2023), reviews the fakeon construction and its spectral-identity argument for perturbative unitarity while retaining renormalizability. Anselmi, Bianchi and Piva, JHEP 07 (2020) 211, derive explicit inflationary scalar/tensor predictions in the `R + R^2 + C^2` realization.

These are strong same-programme positive controls:

`PASS_SCOPED_FAKEON_RENORMALIZABILITY_AND_PERTURBATIVE_UNITARITY_CONTROL`;

`PASS_SCOPED_FAKEON_INFLATIONARY_OBSERVABLE_CONTROL`.

However Dondarini, Phys. Rev. D 108, 083526 (2023), shows that in the full `phi^2` quadratic-inflation realization the fakeon causality issue can propagate to large time scales; the decoupling limit does not recover the free-fakeon spectrum in the required way, and that particular model is discarded phenomenologically.

Scoped disposition:

`FAIL_SCOPED_FAKEON_PHI2_INFLATION_CAUSALITY_DECOPLING_REALIZATION`.

This cannot be promoted to family FAIL: it is one inflationary dynamics / realization and the fakeon programme contains other physical settings.

## D. Scale-free agravity / amplitude branch

Cunha and Lehum, Phys. Rev. D 113, 085006 (2026), derive a broad set of explicit ultra-Planckian `2 -> 2` amplitudes in dimensionless quadratic gravity coupled to QED, including photon-graviton interference, gauge-fixing checks and the high-energy scaling `d sigma / d Omega ~ 1/s`.

This is a genuine physical-observable/amplitude control rather than only an action-level claim:

`PASS_SCOPED_AGRAVITY_ULTRAPLANCKIAN_SCATTERING_OBSERVABLE_CONTROL`.

The work itself treats higher-derivative ghost modes and positivity/unitarity as a subtle nonstandard issue. Tree-level positive squared amplitudes and good UV scaling do not by themselves provide a complete all-orders positive-Hilbert-space / causality certificate for the pole sector.

Therefore:

`BLOCKED_AGRAVITY_ALL_ORDERS_POLE_HILBERT_CAUSALITY_CLOSURE`.

## E. 2026 asymptotically-free Big-Bang / inflation branch

Liu, Quintin and Afshordi, Phys. Rev. Lett. 136, 111501 (2026), provide an especially strong scoped UV-to-observable chain:

- quadratic gravity is asymptotically free in the UV at the analysed one-loop level;
- the RG flow dynamically generates slow-roll inflation toward the IR;
- for sufficiently large matter content, the scalar spectral index and tensor-to-scalar ratio can lie in a phenomenologically viable region;
- avoiding the strong-coupling regime yields a minimum tensor-to-scalar ratio of order `r = 0.01` in the construction.

Classification:

`PASS_SCOPED_QQG_ASYMPTOTIC_FREEDOM_TO_INFLATIONARY_OBSERVABLE_RG_CHAIN`.

But the same paper explicitly identifies the Weyl-squared massive spin-2 mode as a ghost and does not itself resolve the competing quantization/pole prescriptions. It also states that toward the end of inflation the theory approaches strong coupling and that GR must emerge as an EFT for reheating / standard radiation evolution; that strong-coupling emergence is not derived as a controlled same-realization map in the paper.

Thus two decisive links remain open:

`BLOCKED_QQG_SPIN2_PHYSICAL_QUANTIZATION_SELECTION`;

`BLOCKED_QQG_STRONG_COUPLING_TO_GR_EFT_EMERGENCE_AND_ERROR_CONTROL`.

The PRL result therefore substantially strengthens the family but is not terminal RQIR closure.

## F. 2026 dual-IHO / spacelike principal-value branch — strong provisional control

K. Sravan Kumar and J. Marto, arXiv:2603.07150 and arXiv:2604.19707 (latest 2026 versions in the audited corpus), propose a materially distinct interpretation of the extra spin-2 mode. For positive Weyl-squared coefficient, they map it to an inverted-harmonic-oscillator-like sector with spacelike momentum support; the follow-up argues via the Wightman spectrum condition / Kallen-Lehmann support that the corresponding spectral density vanishes and that the principal-value Green function is selected without treating the mode as an asymptotic particle. The authors further argue that the optical theorem is preserved and the UV counterterm structure remains renormalizable.

This is not to be merged with fakeons or Feynman-Wheeler particles. The authors explicitly distinguish their spacelike-pole construction from timelike purely-virtual prescriptions.

Current KMQGB classification:

`PROVISIONAL_STRONG_PREPRINT_CONTROL__DUAL_IHO_SPACELIKE_POLE_UNITARITY_AND_RENORMALIZABILITY_CLAIM`.

It is not promoted to `ESTABLISHED_EXTERNAL` because the central quadratic-gravity result remains a 2026 preprint in the audited publication record and lacks independent peer-reviewed confirmation of the full interacting gravity construction.

### Relation to Jodlowski 2026

Jodlowski, Phys. Rev. D 113, 065016 (2026), proves serious obstructions for covariant interacting virtual tachyons in the fakeon / Wheeler-type setting, including Lorentz-covariance and equivalence-principle problems. This is a strong negative control for virtual-tachyon constructions.

It does **not automatically refute** the dual-IHO proposal because the latter declares a different support/pole structure and explicitly denies identification with a Feynman-Wheeler prescription. Conversely, citing that distinction is not enough to establish safety: the dual-IHO branch must independently demonstrate interacting Lorentz covariance, locality/counterterm closure, stability/causal support and matter coupling under its own exact prescription.

Therefore:

`BLOCKED_DUAL_IHO_INDEPENDENT_PEER_REVIEWED_INTERACTING_LORENTZ_CAUSALITY_AND_MATTER_COUPLING_CERTIFICATE`.

## G. Conditional black-hole area-law constraint

Calcagni, Phys. Rev. D 114, L021906 (2026), shows that if the Hawking area law is imposed exactly on the relevant black-hole merger physics, local Stelle gravity and nonlocal QG are restricted to very special structures, including restrictions on curvature-squared terms / extra real propagator poles and positivity of spectral representation.

Classification:

`PASS_SCOPED_CONDITIONAL_HAWKING_AREA_LAW_POLE_STRUCTURE_CONSTRAINT`.

This is a valuable comparator/consistency control but not an unconditional observational exclusion of all quadratic-gravity branches because the conclusion is explicitly conditional on exact area-law imposition and on the corresponding black-hole realization.

## H. Family synthesis

The 2026 landscape is richer than the old `renormalizable but ghost/fakeon` binary summary:

1. ordinary Feynman/Stelle particle interpretation has a standard ghost-unitarity failure;
2. fakeons provide a peer-reviewed renormalizable/unitary prescription with explicit cosmological observables, but at least one full inflationary realization has a causality failure;
3. agravity now has explicit ultra-Planckian matter/QED scattering observables but no all-orders pole/Hilbert/causality certificate;
4. the Liu-Quintin-Afshordi branch supplies a peer-reviewed asymptotically-free RG-to-inflation observable chain, but does not settle the spin-2 quantization and leaves strong-coupling GR emergence uncontrolled;
5. dual-IHO/spacelike-PV offers a potentially important new solution to the pole problem, but remains provisional/preprint and must survive independent interacting-theory checks.

No one branch currently supplies the complete frozen RQIR chain.

Updated family status:

`PARTIAL_SUBFAMILY_ONLY__STRICT_RENORMALIZABILITY_PLUS_MULTIPLE_OBSERVABLE_AND_UV_RG_STRONG_PASSES__POLE_QUANTIZATION_CAUSALITY_AND_IR_EMERGENCE_NOT_JOINTLY_CLOSED_IN_ONE_ESTABLISHED_REALIZATION`.

This is **not** a family scientific FAIL and contributes zero family-level exclusion evidence toward `NEW_REQUIRED`.

## I. Exact missing family certificate

`HIGHER_DERIVATIVE_FIXED_REALIZATION_POLE_QUANTIZATION_PLUS_UNITARITY_CAUSALITY_UV_RG_TO_IR_GR_MATCHING_NORMALIZED_OBSERVABLE_COMPARATOR_AND_FULL_ERROR_CERTIFICATE`.

A terminal branch must freeze, in one realization:

1. exact action / signs / matter content;
2. pole prescription and physical state space;
3. renormalization and RG authority;
4. unitarity beyond a merely formal tree-level positivity check;
5. causal/stability status under interactions;
6. RG / strong-coupling matching into the low-energy GR/EFT domain;
7. a normalized physical observable with parameter ancestry;
8. identical-domain GR/EFT or observational comparator;
9. propagated perturbative, RG, prescription and nuisance uncertainty.

## J. Paper-III impact

No new transferable resource-closure failure class is identified. Pole causality and ghost-state structure are theory-specific. The generic lessons (do not splice distinct realizations, require parameter ancestry and a physical comparator, propagate prescription uncertainty) are already represented in the frozen Paper-III methodology.

`PAPER_III_REOPEN = NO`.

## K. Heavy compute

`IDLE_FOR_FAMILY_TERMINAL_DECISION`.

The current bottlenecks are conceptual/authority/matching rather than numerical precision. A heavy run becomes justified only after one pole prescription / state-space realization is externally fixed and the calculation can discriminate a physical observable or RG-to-IR matching claim.

## Next gate

Because the newest potentially decisive escape route is the dual-IHO branch, test it separately rather than letting it hide inside the family aggregate:

`DUAL_IHO_QUADRATIC_GRAVITY_INTERACTING_LORENTZ_CAUSALITY_OBSERVABLE_AUTHORITY_AUDIT`.

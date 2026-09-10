# 4D Euclidean Dynamical Triangulations — continuum / observable / comparator audit (Iter225)

**Date:** 2026-09-10  
**RQIR Core:** v1.0 FROZEN  
**Family:** `CDT_EDT`  
**Branch:** four-dimensional EDT  
**Gate:** `EDT_4D_CONTINUUM_PHASE_UV_FIXED_POINT_OBSERVABLE_COMPARATOR_AUDIT`

## Question

Does modern four-dimensional Euclidean Dynamical Triangulations now close a same-realization chain

`lattice action/measure -> continuum/UV trajectory -> physical scale setting -> normalized gravity observable -> GR/EFT comparator -> propagated lattice/EFT uncertainty`,

or does the branch remain nonterminal?

## A. EDT is materially stronger than the old phase-diagram-only picture

The bounded audit finds several independent positive controls in the degenerate-triangulation / tuned-measure EDT programme.

### A1. Newtonian binding and lattice scale setting

Dai, Laiho, Schiffer and Unmuth-Yockey, *Newtonian binding from lattice quantum gravity*, Phys. Rev. D 103, 114511 (2021), compute two-scalar binding in EDT and recover behavior compatible with the four-dimensional Newton potential after infinite-volume / continuum extrapolation. The same analysis provides a lattice-spacing determination and a renormalized Newton coupling.

Classification:

`PASS_SCOPED_EDT_NEWTONIAN_BINDING_AND_SCALE_SETTING_CONTROL`.

### A2. Independent de Sitter / Hawking-Moss determination of Newton's constant

Bassler, Laiho, Schiffer and Unmuth-Yockey, *The de Sitter instanton from Euclidean dynamical triangulations*, Phys. Rev. D 103, 114504 (2021), show semiclassical de-Sitter-like behavior and extract a renormalized Newton constant from a distinct gravitational sector. The value is reported compatible with the scalar-binding determination.

Classification:

`PASS_SCOPED_EDT_SEMICLASSICAL_DESITTER_AND_CROSS_SECTOR_GN_CONTROL`.

The cross-sector agreement is especially valuable for RQIR because it reduces the risk that the inferred scale is an observable-specific normalization artifact.

### A3. Finer lattices

Dai et al., *Improved algorithm for dynamical triangulations and simulations of finer lattices*, Phys. Rev. D 109, 034518 (2024), introduce a rejection-free algorithm and report EDT ensembles at finer lattice spacings, with agreement with semiclassical Euclidean de Sitter improving as the lattice spacing decreases.

Classification:

`PASS_SCOPED_EDT_FINER_LATTICE_SCALING_CONTROL`.

### A4. Multi-lattice-spacing vacuum dynamics

Dai, Freeman, Laiho, Schiffer and Unmuth-Yockey, *Dynamical dark energy from lattice quantum gravity*, Phys. Rev. D 111, 034514 (2025), report higher-precision deviations from de Sitter that are modeled by a running cosmological constant. The analysis includes consistent behavior across multiple lattice spacings, identifies the running scale with the Hubble rate, determines the running parameters from the simulations, and extrapolates to cosmological predictions at approximately the 10^-3 level relative to LambdaCDM observables.

Classification:

`PASS_SCOPED_EDT_MULTI_LATTICE_SPACING_RUNNING_VACUUM_OBSERVABLE_AND_PREDICTION_CONTROL`.

This is a genuine nontrivial observable/prediction layer and retires any blanket statement that modern EDT has no phenomenological observable content.

## B. A universal low-energy GR/EFT comparator now exists

Laiho and Ratliff, *Euclidean correlation functions in quantum gravity*, Phys. Rev. D 113, 106032 (2026), calculate curvature and volume two-point functions through next-to-leading / one-loop order in low-energy gravity. Their final gauge-invariant expressions depend only on Newton's constant and source-sink separation and are explicitly presented as universal predictions suitable for comparison with nonperturbative lattice gravity.

Classification:

`PASS_SCOPED_UNIVERSAL_GR_EFT_CURVATURE_AND_VOLUME_CORRELATOR_COMPARATOR_AVAILABLE`.

This is an important upgrade of the EDT comparator side: the analytic comparator is no longer merely a future desideratum.

## C. Why the branch is nevertheless not terminal

The comparator and the lattice prediction are not yet closed in one audited same-observable, same-realization continuum object.

### C1. UV/critical continuum authority remains nonterminal

Asaduzzaman and Catterall, *Euclidean dynamical triangulations revisited*, Phys. Rev. D 107, 074505 (2023), map the 4D EDT phase diagram with a local measure term and find a line consistent with first-order transitions, although the latent heat decreases toward large kappa. They find Hausdorff dimension approaching four and short-distance spectral dimension near 3/2 along the critical line, but do not establish a second-order critical point / UV fixed point.

The tuned-measure EDT programme reports evidence for continuum scaling by approaching the transition line toward very large bare coupling, but the audited literature does not yet supply a universally established nonperturbative higher-order critical endpoint with a complete correlation-length/critical-exponent error certificate.

Classification:

`PASS_SCOPED_CONTINUUM_SCALING_EVIDENCE__BLOCKED_PROVEN_UV_CRITICAL_SURFACE`.

### C2. The historical curvature-correlator lattice object is not yet the required clean comparator partner

Earlier 4D EDT curvature-correlator studies used Regge/deficit-angle curvature proxies. Later nonperturbative curvature work notes that the deficit-angle local curvature is problematic in 4D dynamical triangulations because it diverges in the infinite-volume limit, and early 4D Euclidean correlator results were inconclusive.

Therefore the newly available 2026 gauge-invariant GR/EFT correlator cannot simply be spliced onto old EDT correlator plots and declared a successful physical match.

What is required is a prospectively frozen EDT lattice operator whose continuum interpretation matches the relational/gauge-invariant EFT observable, together with lattice-spacing transport and finite-volume/discretization errors.

Classification:

`BLOCKED_SAME_OBSERVABLE_EDT_TO_GR_EFT_CORRELATOR_MATCH`.

### C3. Euclidean-to-Lorentzian physical interpretation remains an explicit scope issue

EDT is fundamentally evaluated through a Euclidean sum over geometries. Its successful recovery of semiclassical de Sitter, Newtonian binding and cosmological effective behavior is strong evidence of physical content, but it is not by itself a proof that a unique Lorentzian quantum theory is reconstructed from the Euclidean ensemble.

This issue must be stated rather than silently borrowing CDT's causal/Wick-rotation structure.

Classification:

`BLOCKED_UNIQUE_LORENTZIAN_PHYSICAL_RECONSTRUCTION_FOR_FAMILY_TERMINAL_CLAIM`.

## D. Same-realization discipline across EDT variants

The 4D EDT literature contains materially different implementations, including combinatorial versus degenerate triangulations and different measure terms. The 2023 phase-diagram study reports broad universality-like agreement with earlier formulations, but this does not authorize arbitrary splicing of observables, scale determinations and critical behavior across formulations.

For terminal RQIR closure, the selected EDT realization must carry its own declared action/measure, trajectory, scale setting, observable and error ledger, or an explicit universality map with uncertainty must be provided.

## E. EDT branch result

Modern EDT is upgraded to:

`PARTIAL_SUBFAMILY_ONLY__SEMICLASSICAL_4D_NEWTONIAN_BINDING_CROSS_SECTOR_GN_MULTI_SPACING_PHENOMENOLOGY_AND_UNIVERSAL_EFT_COMPARATOR_STRONG_PASSES__PROVEN_UV_CRITICAL_SURFACE_AND_SAME_OBSERVABLE_CONTINUUM_MATCH_BLOCKED`.

This is a substantially stronger status than a generic `PARTIAL_SUBFAMILY_ONLY` label.

It is **not** a scientific FAIL and contributes zero exclusion evidence toward `NEW_REQUIRED`.

## F. Exact missing certificate

`EDT_FIXED_REALIZATION_PROVEN_UV_CRITICAL_TRAJECTORY_PLUS_SCALE_SETTING_TO_GAUGE_INVARIANT_CURVATURE_OR_VOLUME_CORRELATOR_CONTINUUM_MATCH_WITH_GR_EFT_COMPARATOR_AND_FULL_ERROR_LEDGER`.

Minimum payload:

1. one explicitly fixed 4D EDT action/measure/triangulation realization;
2. a demonstrated UV critical surface / continuum trajectory with finite-size scaling and uncertainties;
3. scale setting along that trajectory, not at one isolated point;
4. a well-defined lattice curvature or volume observable with controlled continuum limit;
5. mapping to the 2026 gauge-invariant GR/EFT correlator definition or another equally explicit physical comparator;
6. identical-domain comparison using the same Newton constant / distance convention;
7. finite-volume, lattice-spacing, operator, fit-window, autocorrelation and EFT-truncation uncertainty propagation;
8. an explicit statement of Euclidean-to-physical/Lorentzian scope.

## G. Paper-III impact

No new transferable Paper-III failure class is identified. The important lessons — same-observable matching, realization provenance, scale ancestry, normalization and error transport — are already represented by the frozen Paper-III resource-closure controls.

`PAPER_III_REOPEN = NO`.

## H. Heavy-compute consequence

`CONDITIONAL_HIGH_VALUE`.

EDT has moved close enough to a concrete comparator problem that a future compute campaign could be decision-relevant. The highest-value run is not a generic phase scan: it is a prospectively frozen multi-lattice-spacing measurement of a gauge-invariant curvature/volume correlator that can be compared directly with the 2026 GR/EFT formula.

Existing historical deficit-angle correlators should not be treated as sufficient without resolving their continuum-operator problem.

## I. Parent CDT/EDT consequence

Both major children now carry strong but distinct positive controls:

- CDT: 4D semiclassical phase + normalized curvature-correlator observable, with UV line-of-constant-physics / a->0 transport open;
- EDT: semiclassical de Sitter + Newtonian binding + scale setting + multi-spacing vacuum phenomenology + an available universal GR/EFT correlator comparator, with proven UV critical surface and same-observable continuum matching open.

Neither child can close the other. The combined `CDT_EDT` parent remains nonterminal.

## Next gate

Advance by information gain to test whether the **new 2026 universal GR/EFT correlator can already be paired with a sufficiently well-defined modern EDT lattice curvature/volume observable**, or whether a new lattice measurement is genuinely required:

`EDT_2026_EFT_CORRELATOR_TO_LATTICE_OPERATOR_MATCHABILITY_AUDIT`

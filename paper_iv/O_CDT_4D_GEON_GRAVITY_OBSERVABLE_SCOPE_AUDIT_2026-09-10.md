# O-CDT 4D curvature-correlator / geon observable scope audit — 2026-09-10

**KMQGB iteration:** 200  
**RQIR Core:** v1.0 FROZEN  
**Parent:** `CDT_EDT`  
**Scope:** close the previously vague “physical/invariant observable missing” part only where a fixed 4D CDT realization now has a normalized gravitational correlator with systematic controls and public data. Do not promote the continuum trajectory.

## Primary authority

Axel Maas, Simon Plätzer, Felix Pressler, *Hints for a Geon from Causal Dynamic Triangulations*, Phys. Lett. B **879** (2026) 140600; arXiv:2504.11047v4 (3 June 2026).

The final arXiv version explicitly added an appendix on systematic effects. The calculation is performed in four-dimensional CDT at one fixed bare simulation point, `Delta = 0.6`, `kappa_0 = 2.2`, in the de-Sitter-like phase.

Associated public stochastic samples are archived on Zenodo as record `20589545` (version v1, 8 June 2026), including the 60×80k, 80×160k and 80×320k ensembles and a multi-smearing-radius sample.

## Fixed realization and observable

The simulations use

- `(N_t,N_simp) = (60,80k), (80,160k), (80,320k)`;
- 5000 configurations for the two smaller standard ensembles and 2000 for `N_simp=320k`;
- a quoted spatial simplex lattice-spacing estimate `a ≈ 2.1 l_P`, taken by the authors as an external conversion rather than a continuum-extrapolated result;
- geodesic distance between dual vertices within a fat foliation slice;
- curvature proxies based on the Quantum Ricci Curvature Scalar `Q`, its square and a fitted continuum-curvature proxy `R`.

The measured two-point quantity is normalized by the unit-operator correlator,

`D_OO(tau,s) = C_OO(tau,s) / C_11(tau,s)`, with `D_11=1`,

so the same stochastic pair-sampling geometry enters numerator and normalization. In the declared intermediate-distance window, the subtracted curvature correlators are fit by

`a + b exp(-m s)`.

This is a genuine correlation observable of invariant curvature quantities rather than a bare lattice coupling or an unnormalized action diagnostic.

## Scoped robustness controls now available

The final paper supplies several controls material to RQIR:

1. **operator variation** — `Delta Q`, `Delta Q^2` and the reconstructed `R` correlator show the same exponential-decay mass scale within the reported statistical precision;
2. **volume variation** — the qualitative mass history and the quoted early-time averaged mass are stable to within a few standard deviations across 80k, 160k and 320k simplices; no statistically significant volume dependence is claimed for the primary conclusion;
3. **smearing variation** — for the `Q` construction the correlator becomes approximately independent of the smearing radius once `delta >= 4`; the appendix explicitly studies `delta=1..10`, with the expected lattice-artifact distortion at the smallest radii;
4. **fit uncertainty** — the paper displays and propagates `1 sigma` uncertainty bands in the normalized correlator fits;
5. **open data** — the associated stochastic samples for all main ensembles and the multi-delta control are publicly archived on Zenodo.

Representative early-time averaged dimensionless masses quoted by the paper are:

- `Delta Q`: `0.18(1), 0.16(1), 0.17(3)` for 80k, 160k, 320k;
- `Delta Q^2`: `0.14(1), 0.17(1), 0.15(3)` for 80k, 160k, 320k.

Using the external lattice-spacing estimate gives an illustrative physical scale of order `0.09 M_P`, but the authors explicitly warn that this physical-unit conversion may carry discretization artifacts and requires lines-of-constant-physics studies. KMQGB therefore does **not** freeze `0.09 M_P` as a continuum prediction.

## Scoped result

**`PASS_RQIR_GATE__CDT_4D_NORMALIZED_CURVATURE_CORRELATOR_PHYSICAL_OBSERVABLE_WITH_OPERATOR_VOLUME_SMEARING_SYSTEMATICS_AND_OPEN_DATA`**

This means that the 4D CDT row can no longer be described as lacking any normalized gravity-sector observable. A concrete observable capsule exists in a fixed realization and has nontrivial systematics plus public raw stochastic samples.

The word “geon” remains an interpretation, not a frozen particle discovery. The RQIR PASS applies to existence and controlled measurement of the observable, not to proof that the state is a stable geon or dark-matter object.

## What remains open

This result does **not** close the parent `CDT_EDT` family because:

- only one bare parameter point is used for the geon observable;
- the calculation is not performed along a line of constant physics toward a continuum critical point;
- the lattice spacing used for physical-unit conversion is not derived simultaneously from a continuum trajectory;
- finite-volume robustness is not the same as an `a -> 0` continuum extrapolation;
- the long-distance correlator departs from the simple exponential window and the physical interpretation remains exploratory;
- a same-domain GR/EFT/alternative-QG prediction for the same normalized correlator has not been frozen;
- EDT is not dispositioned by this CDT child result.

The independent CDT↔FRG analysis by Ambjørn, Gizbert-Studnicki, Görlich and Németh, *IR and UV Limits of CDT and Their Relations to FRG* (Acta Phys. Pol. B 55, 12-A2; arXiv:2411.02330), develops a concrete critical-scaling/FRG matching strategy but explicitly concludes that present numerical precision is insufficient to decide whether a CDT UV fixed point exists. The 2026 Ambjørn–Loll review likewise describes simulations as indicating a possible UV fixed point and observable construction as ongoing.

Thus the missing object is no longer “continuum trajectory plus some invariant observable” as one undifferentiated blocker. The observable side has a strong 4D scoped control; the continuum/RG and comparator side remains decisive.

## Refined CDT blocker

**`CDT_4D_LINE_OF_CONSTANT_PHYSICS_TO_UV_CONTINUUM_TRAJECTORY_PLUS_LATTICE_SPACING_SCALING_AND_GEON_CORRELATOR_COMPARATOR_ERROR_CERTIFICATE__EDT_DISPOSITION`**

Minimum payload:

1. a fixed 4D CDT phase/bare-coupling trajectory approaching a demonstrably higher-order critical surface or UV fixed point;
2. a line-of-constant-physics or equivalent scale-setting prescription along that trajectory;
3. an explicit `a -> 0` map with uncertainty;
4. transport/remeasurement of the normalized curvature-correlator observable (or a declared equally physical gravity observable) along the trajectory;
5. finite-volume + discretization + fit-window + smearing + critical-scaling error ledger;
6. same-domain GR/EFT and alternative-QG comparator predictions;
7. a declared disposition of EDT rather than silently using a CDT child to close the combined row.

## D7 / compute consequence

`CDT_EDT` remains `PARTIAL_SUBFAMILY_ONLY` and its family residual remains undefined. No family PASS/FAIL or `NEW_REQUIRED` evidence follows. D2/D4/D7 remain nonterminal; Candidate Gravity remains inactive at R3=24%.

Heavy compute remains `IDLE` for KMQGB. The publicly archived geon samples could support a replication study, but re-fitting one fixed bare point cannot close the missing continuum trajectory. Heavy compute becomes scientifically justified only after a prospectively frozen multi-coupling line-of-constant-physics/critical-scaling data capsule is identified.
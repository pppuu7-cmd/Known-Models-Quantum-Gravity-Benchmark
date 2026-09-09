# KMQGB Current Benchmark Front

**Updated:** 2026-09-09  
**KMQGB iteration:** 134  
**Repository:** `pppuu7-cmd/Known-Models-Quantum-Gravity-Benchmark`  
**Branch:** `main`  
**Phase:** UNIQUE GRAVITY-NATIVE INTERACTING OPERATOR/PROCESS ORIGIN LAW REQUIRED / DETECTOR-VISIBLE RESIDUAL GATE ADDED

## Stable readiness metrics

Authority: `protocol/READINESS_METRICS.md`.

- **R1 — Repository readiness: 92%.**
- **R2 — KMQGB methodology/material readiness: 89%.**
- **R3 — Candidate Gravity scientific readiness: 24%.**
- **R4 — `MINIMAL_NOVEL_PARENT_PRINCIPLE_SEARCH`: 45%.**

No novel P4 survivor exists. Last score change remains Iter060. Negative gates, comparator upgrades, external Paper-III progress and detector-methodology improvements do not substitute for P4.

## Provenance

Read `recovery/PROVENANCE_CORRECTION_POST116_ID_COLLISION.md` before interpreting historical commit numbers after Iter116. Recovery deltas are now restored through Iter134.

## What Iter123–132 established

### Spectral/strong-gravity route

- **Iter123:** `S_BH + ETH + KMS` still does not determine the absolute spectral envelope; KMS fixes detailed-balance relations once the spectrum is supplied.
- **Iter124:** finitely many positive spectral moments do not determine a unique measure; an executable counterexample is frozen in `code/p4_spectral_moment_nonuniqueness_reference.py`.
- **Iter125:** a finite constant-coefficient linear recurrence for the entire moment sequence forces a positive measure onto finitely many atoms, giving a rational finite-mediator/resonance resolvent.
- **Iter126:** a finite nonlinear recurrence can determine a continuous spectrum; the Catalan/Marchenko-Pastur control proves A2 finite generation is possible, but is random-matrix/free-probability contained.
- **Iter127:** a black-hole wave operator + physical boundary normalization + ingoing causal condition can determine a complete non-rational probe spectral function. This is a strong gravity-native A2-positive `G2` blueprint, but not an intrinsic interacting `K4` parent.

### Interacting-generator / operator route

- **Iter128:** Lorentzian asymptotic safety is upgraded as a strong comparator: functional/spectral RG already generates nonperturbative graviton spectra, effective actions/form factors and multi-graviton vertex information.
- **Iter129:** process-matrix consistency defines a convex feasible process set rather than unique dynamics; indefinite causal order also lacks unique gravity attribution.
- **Iter130:** quantum-corner representations, gluing and area-law state structure constrain Hilbert/state kinematics but do not select a unique hard transition operator.
- **Iter131:** one finite covariant operator can generate an all-point one-loop metric hierarchy through `Tr log Delta` and admits a CTP route, but local counterterm freedom remains and the architecture is ordinary QFT/induced-gravity/quantum-GR contained.
- **Iter132:** equivalence principle / diffeomorphism covariance / the causal principal symbol do not select the complete operator. `Delta_xi=-Box+m^2+xi R` is an exact witness: identical characteristics, different quantum curvature response.

The resulting primitive question is now very sharp:

> **what finite gravity-native physical law selects the complete interacting operator/process itself?**

It must fix principal symbol, lower-order curvature/endomorphism terms, gauge/ghost/constraint complex, state, measure, Lorentzian contour, local renormalization/null data and then generate hard `4g`/higher + all-point + CTP observables.

## External RQIR advance — Iter133 sync

The external repository has advanced materially on **Paper III / programme readiness**, even though its separate Candidate-Gravity front remains Iter675 / 24%.

Latest observed programme audit:

- Paper I scientific material: 100%;
- Paper II scientific material: 100%;
- Paper III strengthened apparatus-specific readiness: **68%**;
- Paper IV: **55%**, still prerequisite-blocked at the decisive physical-residual bridge;
- Paper V Candidate-Gravity groundwork: **24% conditional**;
- overall working RQIR programme/model readiness: approximately **71%**.

`external_rqir_checks/iter133_rqir_programme_paper3_physical_psd_sync.md` records the firewall: **programme 71% is not Candidate-Gravity R3**.

The Paper-III branch now uses a source-traceable SYRTE colored vibration PSD and physical Toeplitz covariance. It reproduces independent published apparatus scales without amplitude fitting and gives the correct nuisance identifiability pattern.

## Iter134 — detector-visible residual certificate

Added:

- `protocol/P5_DETECTOR_VISIBLE_RESIDUAL_PHYSICAL_COVARIANCE_GATE.md`;
- `code/detector_visible_residual_physical_covariance_reference.py`.

For detector science direction `r`, covariance `C`, nuisance tangent matrix `N` and external nuisance prior precision `P`, define

`I0 = r^T C^-1 r`

`Iprof = I0 - r^T C^-1 N (N^T C^-1 N + P)^+ N^T C^-1 r`

`eta_det = sqrt(max(Iprof,0)/I0)`.

A comparator-orthogonal theory residual must also satisfy `eta_det>0` after the physical detector map, source-traceable whitening and declared nuisance profiling.

The source-traceable fixture reproduces the external RQIR physical PSD scales and correctly rejects static/free-offset, no-reference and unconstrained-reference cases while preserving the calibrated/prior-constrained modulated science direction under strong crosstalk stress.

This does **not** yet promote R2. The frozen `residual/identifiability/rigidity` component remains `19/20` until the detector-facing nonlinear transition-probability/readout layer is closed.

## External Candidate-Gravity authority

Candidate Gravity remains **24%** at Iter675. Missing authorities remain

- M1 physical observable bridge;
- M2 matched same-parent Source/Born/contact completion;
- M3 robust comparator-subtracted residual;
- M4 actual `Tr U1` if later required.

No independent Candidate-Gravity compute gate is authorized.

## Heavy compute

**IDLE_BY_SCIENTIFIC_DESIGN.**

The present bottleneck is an origin-law/authority problem, not a numerical one.

## Exact next KMQGB front

Search for a finite gravity-native **operator/process selection law**, not another chosen operator or functional equation.

Immediate tests:

1. does the principle uniquely determine the complete microscopic operator/process rather than only its causal cone or symmetry class?
2. are state/measure/contour/local-renormalization data fixed by the same law?
3. does the same parent generate a normalized comparator-orthogonal hard `4g`/higher datum and all-point hierarchy?
4. is a same-parent Lorentzian CTP/retarded object explicit?
5. does it survive ordinary covariant QFT/`Tr log`, Lorentzian AS, string/q-string, BFSS/matrix, JT/random-matrix, LQG/spinfoam/corner, causal/nonlocal and process-matrix comparators?
6. if a structural residual is found, does it survive the Iter134 detector-visible physical-covariance certificate?

Do not launch heavy computation until a frozen A1–A3 survivor produces a genuinely numerical discriminator.

# O-GFT spin-foam reduction and relational-observable scope audit — 2026-09-10

**KMQGB iteration:** 202  
**RQIR Core:** v1.0 FROZEN  
**Parent:** `GFT_TENSOR_MODELS`  
**Status:** structural/scoped progress only; no family-level promotion.

## Question

The Iter186 blocker bundled two different questions:

1. is GFT independent from, or reducible to, spin-foam/LQG dynamics in a fixed realization?  
2. does GFT already possess a concrete continuum/effective gravity observable with a same-domain GR comparator?

Iter202 separates these questions and freezes only what is explicitly supported by published constructions.

## Primary authorities

1. D. Oriti, J. P. Ryan, J. Thürigen, *Group field theories for all loop quantum gravity*, New J. Phys. 17 (2015) 023042, DOI `10.1088/1367-2630/17/2/023042`, arXiv:1409.3150.
2. A. F. Jercher, L. Marchetti, A. G. A. Pithis, *Scalar cosmological perturbations from quantum entanglement within Lorentzian quantum gravity*, Phys. Rev. D 109 (2024) 066021, DOI `10.1103/PhysRevD.109.066021`.
3. R. Dekhil, A. F. Jercher, A. G. A. Pithis, *Phase transitions in tensorial group field theory: Landau-Ginzburg analysis of the causally complete Lorentzian Barrett-Crane model*, Phys. Rev. D 111 (2025) 026014.
4. R. Dekhil, F. Greco, S. Liberati, D. Oriti, *Emergent scalar field dynamics in a cosmological spacetime from GFT quantum gravity*, arXiv:2608.12003 (12 August 2026).

## A. Microscopic GFT ↔ spin-foam relation

Oriti–Ryan–Thürigen establish that GFT can be formulated as a second-quantized reformulation of the LQG state space and as a completion of the spin-foam formalism. Crucially for RQIR, they give an explicit GFT formulation of the KKL spin-foam model rather than merely claiming conceptual similarity.

Therefore the selected KKL-compatible GFT sector satisfies the scoped relation

`fixed GFT interaction/propagator data -> perturbative GFT Feynman expansion -> KKL spin-foam amplitudes on the generated combinatorial complexes`.

This supports:

**`PASS_STRUCTURAL_GATE__SELECTED_KKL_COMPATIBLE_GFT_HAS_EXPLICIT_SPINFOAM_REDUCTION_MAP_AT_THE_MICROSCOPIC_AMPLITUDE_LEVEL`**.

The statement is deliberately scoped. It does **not** mean that the entire GFT/TGFT family is equivalent to one fixed spin-foam model. GFT contains second-quantized graph-changing structure, sums over Feynman complexes, tensorial interactions, renormalization/phase structure and condensate sectors that are not exhausted by a single fixed-complex spin-foam amplitude.

Thus KMQGB forbids both extremes:

- `GFT is wholly independent of spin foams` — too strong for KKL-compatible GFT;
- `GFT is just spin foams and can be deleted as a separate family` — also too strong because continuum/collective GFT sectors add dynamical structure not fixed by one spin-foam amplitude.

## B. Relational gravity-sector effective observables

Jercher–Marchetti–Pithis derive scalar cosmological perturbation dynamics from a causally complete Lorentzian Barrett-Crane GFT using a physical Lorentzian reference frame built from four scalar fields. The construction yields relational macroscopic observables from GFT states. In the reported regime the effective geometric and matter perturbation equations agree with GR for sub-Planckian modes, while deviations become important in the trans-Planckian/subhorizon regime.

This is stronger than a purely formal condensate ansatz: the selected GFT realization contains a concrete theory-to-effective-cosmology map and an explicit GR comparison domain.

The 2025 Landau-Ginzburg analysis of the causally complete Lorentzian Barrett-Crane TGFT shows that a nontrivial condensate phase can be realized in mean field for several interaction classes, strengthening the plausibility of the collective continuum regime used by GFT cosmology. However, a mean-field phase transition is not by itself a nonperturbative continuum theorem.

The 2026 Dekhil–Greco–Liberati–Oriti construction further derives effective scalar-field dynamics from GFT quantum-gravity hydrodynamics in a fully relational setting. It recovers the standard massless-scalar dynamics in the late-time GR regime and generates an early-universe modified dispersion relation with dispersive and dissipative corrections. This is a concrete microscopic-signature channel, but it is a matter-sector effective observable, not a complete gravitational comparator residual.

Scoped status:

**`PASS_STRUCTURAL_GATE__GFT_RELATIONAL_CONDENSATE_DYNAMICS_SUPPLIES_EXPLICIT_GR_LIMIT_AND_QUANTUM_CORRECTION_CHANNELS`**.

## Why no new gravity residual row is added

RQIR requires the same physical observation operator/domain, comparator subtraction and propagated error/remainder control before a family/scoped residual is declared comparator-ready.

The present GFT authorities do not jointly provide all of:

- a nonperturbatively controlled continuum/thermodynamic limit for the chosen Lorentzian GFT realization;
- a prospectively normalized observational operator connecting the relational perturbation variables to one measured data vector/covariance;
- a complete uncertainty budget covering mean-field/condensate truncation, interaction choice, graph/Feynman-complex sum, relational-frame approximation and continuum scaling;
- a same-domain comparator suite against GR/EFT and alternative quantum-gravity families.

Therefore Iter202 does **not** increment the count of comparator-ready gravity residual rows. The GFT family residual remains undefined rather than zero-filled.

## Refined family decomposition

The old blocker

`GFT_SPINFOAM_INDEPENDENCE_OR_REDUCTION_PLUS_FULL_GRAVITY_OBSERVABLE_COMPARATOR_CERTIFICATE`

is decomposed as follows:

### Closed scoped component

`GFT_KKL_MICROSCOPIC_SPINFOAM_RELATION = PASS_STRUCTURAL`

### Open components

1. `GFT_FAMILY_RELATION_SCOPE`: classify which material GFT/TGFT branches reduce to named spin-foam parents and which possess genuinely independent collective/RG dynamics;
2. `GFT_CONTINUUM_CONTROL`: establish a controlled continuum/thermodynamic/critical trajectory for one declared Lorentzian gravity realization beyond mean-field plausibility alone;
3. `GFT_GRAVITY_OBSERVABLE_NORMALIZATION`: transport a relational gravitational observable through that continuum regime;
4. `GFT_COMPARATOR_ERROR_QUOTIENT`: freeze same-domain GR/EFT/alternative-QG comparators and the full approximation/error ledger.

## Refined exact blocker

**`GFT_MATERIAL_BRANCH_REDUCTION_OR_INDEPENDENCE_MAP_PLUS_CONTROLLED_CONTINUUM_TRAJECTORY_AND_NORMALIZED_RELATIONAL_GRAVITY_OBSERVABLE_COMPARATOR_ERROR_CERTIFICATE`**.

Minimum payload:

1. material GFT/TGFT branch census;
2. for each branch, explicit `REDUCES_TO_SPINFOAM(parent)` or `INDEPENDENT_COLLECTIVE_DYNAMICS` justification;
3. one fixed Lorentzian gravity realization with controlled continuum/thermodynamic trajectory;
4. relational gravitational observable carried along that trajectory;
5. normalization to a common physical observation domain;
6. GR/EFT and alternative-QG comparator predictions;
7. uncertainty ledger covering continuum, condensate/mean-field, interaction/truncation and numerical errors;
8. family-level disposition without silently promoting one Barrett-Crane cosmology child to the whole family.

## D7 / compute consequence

`GFT_TENSOR_MODELS` remains `PARTIAL_SUBFAMILY_ONLY`. D2/D4/D7 remain open. No family PASS/FAIL and no `NEW_REQUIRED` evidence follows. Candidate Gravity remains inactive at R3=24%.

Heavy compute remains `IDLE`. The immediate blocker is classification/provenance and continuum-control structure; brute-force numerics without a frozen branch/continuum prescription cannot produce a valid family-level certificate.
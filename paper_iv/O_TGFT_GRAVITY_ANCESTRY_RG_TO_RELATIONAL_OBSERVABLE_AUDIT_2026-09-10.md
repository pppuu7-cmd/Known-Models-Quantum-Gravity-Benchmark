# O-TGFT — Gravity-ancestry RG/continuum to relational-observable same-realization audit

**Date:** 2026-09-10  
**KMQGB iteration:** 205  
**RQIR Core:** v1.0 FROZEN

## Gate

`TGFT_GRAVITY_ANCESTRY_RG_CONTINUUM_TO_RELATIONAL_OBSERVABLE_SAME_REALIZATION_CERTIFICATE`

Required object: one declared gravity-ancestry TGFT/GFT realization in which a controlled RG/critical/continuum trajectory and a normalized relational/condensate gravitational observable are derived from the same microscopic theory, with parameter transport, common physical domain, GR/EFT comparator and propagated RG/mean-field/truncation error ledger.

## Primary authorities inspected

1. A. F. Jercher, D. Oriti, A. G. A. Pithis, *Emergent cosmology from quantum gravity in the Lorentzian Barrett-Crane tensorial group field theory model*, JCAP 01 (2022) 050, DOI: 10.1088/1475-7516/2022/01/050, arXiv:2112.00091.
2. L. Marchetti, D. Oriti, A. G. A. Pithis, J. Thürigen, *Mean-Field Phase Transitions in Tensorial Group Field Theory Quantum Gravity*, Phys. Rev. Lett. 130 (2023) 141501, DOI: 10.1103/PhysRevLett.130.141501, arXiv:2211.12768.
3. L. Marchetti, D. Oriti, A. G. A. Pithis, J. Thürigen, *Phase transitions in TGFT: a Landau-Ginzburg analysis of Lorentzian quantum geometric models*, JHEP 02 (2023) 074, DOI: 10.1007/JHEP02(2023)074, arXiv:2209.04297.
4. R. Dekhil, A. F. Jercher, A. G. A. Pithis, *Phase transitions in tensorial group field theory: Landau-Ginzburg analysis of the causally complete Lorentzian Barrett-Crane model*, Phys. Rev. D 111 (2025) 026014, DOI: 10.1103/PhysRevD.111.026014, arXiv:2407.02325.

## Same-realization findings

### Relational gravitational observable exists in a gravity-ancestry realization

The 2022 Lorentzian Barrett-Crane GFT with a free massless scalar reference field derives relational condensate dynamics and generalized Friedmann equations from a declared Lorentzian quantum-gravity microscopic model. This is a genuine gravity-ancestry observable object, not a generic tensor-theory surrogate.

Scoped structural result:

`PASS_STRUCTURAL_GATE__LORENTZIAN_BC_GFT_RELATIONAL_CONDENSATE_COSMOLOGY_OBJECT_EXISTS`

This PASS is limited to existence of the relational/condensate cosmological observable under the approximations stated in the source. It is not a continuum-RG or family-level PASS.

### A controlled mean-field phase-transition argument exists for realistic Lorentzian TGFT

The 2023 Landau-Ginzburg analyses show that realistic quantum-geometric TGFT ingredients admit a nontrivial condensate phase whose mean-field treatment can be self-consistent at large correlation length. The 2025 causally complete Lorentzian Barrett-Crane extension strengthens this statement for a broader BC microscopic content.

Scoped structural result:

`PASS_STRUCTURAL_GATE__REALISTIC_LORENTZIAN_TGFT_MEAN_FIELD_CONDENSATE_PHASE_IS_SELF_CONSISTENT_IN_DECLARED_LANDAU_GINZBURG_DOMAIN`

### Full RG trajectory is still missing for the realistic gravity realization

The same literature explicitly characterizes a full renormalization-group-flow analysis of the relevant realistic TGFT models as not yet available because of model complexity, and presents the Landau-Ginzburg analysis as preparation/support for future functional-RG work. Existing FRG results for simpler Abelian/tensorial models therefore cannot be spliced into the Lorentzian Barrett-Crane cosmological realization under the frozen same-realization rule.

There is consequently no authenticated object establishing

`microscopic Lorentzian BC/TGFT couplings -> controlled RG trajectory/critical surface -> condensate effective couplings -> normalized relational gravity observable`

with one continuous parameter ancestry and one propagated RG + mean-field + truncation error ledger.

## Disposition

`BLOCKED_MISSING_REQUIRED_OBJECT__TGFT_GRAVITY_ANCESTRY_FULL_RG_TRAJECTORY_TO_RELATIONAL_GRAVITY_OBSERVABLE_SAME_REALIZATION_MAP`

This is **BLOCKED**, not FAIL. The existing mean-field/relational results are positive scoped evidence, but they do not satisfy the frozen complete-object requirement. No child result is promoted to `GFT_TENSOR_MODELS` family-level PASS/FAIL.

Family residual remains undefined.

## Comparator/error status

- Same-realization microscopic gravity ancestry: partial/pass for declared BC constructions.
- Relational observable: exists in scoped Lorentzian BC condensate cosmology.
- Controlled full RG trajectory in that same realization: missing.
- Cross-scale parameter transport: missing.
- Common-domain normalized GR/EFT residual with propagated RG/mean-field/truncation remainder: missing.
- Family residual: undefined.

## Compute disposition

`HEAVY_COMPUTE = IDLE`.

The missing object is structural/provenance/matching limited. Running FRG numerics for a different simplified TGFT would not close this gate and would violate the same-realization rule.

## Next gate

`GFT_SPINFOAM_GENERATING_BRANCH_INDEPENDENCE_OR_REDUCTION_PLUS_CONTINUUM_OBSERVABLE_CERTIFICATE`

The next useful question is whether the surviving gravity GFT branch is an independent Tier-1 physical alternative or reducible, in a fixed realization and observable domain, to the already-tracked spin-foam/LQG branch. This can reduce family-level ambiguity without inventing a cross-model RG trajectory.

# TGFT same-realization FRG-to-relational-observable gap audit — Iter208

**Date:** 2026-09-10  
**RQIR Core:** v1.0 FROZEN  
**Parent row:** `GFT_TENSOR_MODELS`  
**Target branch:** gravity-ancestry TGFT RG/phase structure

## Question

Does the identified primary-literature corpus contain one declared quantum-geometric TGFT realization that supplies the complete chain

`microscopic gravity action/constraints -> nonperturbative RG trajectory or equivalently controlled continuum trajectory -> condensate/collective state -> relational gravitational observable -> normalized common-domain comparator -> approximation/error ledger`

without splicing different microscopic realizations?

## Scope guard

This is a scoped corpus audit, not a universal theorem that no such construction can exist. A missing link is classified `BLOCKED_MISSING_REQUIRED_OBJECT`, not scientific FAIL. Results from different TGFT realizations may support plausibility but may not be concatenated into a same-realization certificate.

## Primary corpus

### R1 — Lorentzian Barrett-Crane relational cosmology

A. F. Jercher, D. Oriti, A. G. A. Pithis, *Emergent Cosmology from Quantum Gravity in the Lorentzian Barrett-Crane Tensorial Group Field Theory Model*, arXiv:2112.00091.

- microscopic gravity ancestry: YES — Lorentzian Barrett-Crane GFT with scalar reference field;
- condensate/mean-field hydrodynamics: YES;
- relational background observable/dynamics: YES — generalized Friedmann dynamics and bounce;
- full FRG trajectory for the same realization: NO object supplied by this work;
- comparator/error closure required by KMQGB: NO.

### R2 — Lorentzian Barrett-Crane relational perturbations

The later Lorentzian Barrett-Crane perturbation analysis derives relational scalar cosmological perturbations from the mean-field hydrodynamics of the full Lorentzian two-sector model and recovers the GR behavior in the appropriate sub-Planckian regime while retaining quantum-gravity corrections outside it.

- microscopic gravity ancestry: YES;
- relational perturbation observable: YES;
- full same-realization FRG trajectory: NO object supplied in this line of work;
- complete normalized comparator/error ledger: NO.

### R3 — realistic quantum-geometric TGFT mean-field phase transition

L. Marchetti, D. Oriti, A. G. A. Pithis, J. Thürigen, *Mean-Field Phase Transitions in Tensorial Group Field Theory Quantum Gravity*, Phys. Rev. Lett. 130 (2023) 141501, DOI `10.1103/PhysRevLett.130.141501`.

The paper explicitly frames a full RG-flow analysis of the relevant realistic TGFT models as difficult and instead justifies the mean-field continuum/condensate assumption from realistic quantum-geometric ingredients.

- realistic gravity ingredients: YES;
- controlled mean-field phase argument: YES;
- complete full FRG trajectory of the same realistic gravity model: NO;
- relational observable in the same calculation: NO.

### R4 — causally complete Lorentzian Barrett-Crane Landau-Ginzburg phase analysis

R. Dekhil, A. F. Jercher, A. G. A. Pithis, *Phase transitions in tensorial group field theory: Landau-Ginzburg analysis of the causally complete Lorentzian Barrett-Crane model*, Phys. Rev. D 111 (2025) 026014, arXiv:2407.02325, DOI `10.1103/PhysRevD.111.026014`.

- explicit Lorentzian Barrett-Crane gravity ancestry: YES;
- spacelike/timelike/lightlike causal sectors and scalar variables: YES;
- mean-field nontrivial condensate phase: YES;
- full nonperturbative FRG trajectory of this same complete model: NO object supplied;
- relational cosmological observable transported through such an FRG trajectory: NO.

### R5 — FRG controls on simpler TGFT realizations

Examples in the primary corpus include:

- D. Benedetti, V. Lahoche, arXiv:1508.06384: rank-6 Abelian TGFT with closure constraint, FRG fixed-point analysis;
- V. Lahoche, D. O. Samary, arXiv:1608.00379: Abelian `U(1)` tensorial GFT with closure constraint and nontrivial fixed points in a truncation;
- A. G. A. Pithis, J. Thürigen, arXiv:2009.13588: cyclic-melonic TGFT on compact `U(1)` and FRG phase-transition analysis.

These works provide genuine RG methodology/results, but they are not the same microscopic Lorentzian Barrett-Crane gravity realization used by R1/R2/R4. Therefore they cannot be spliced into the missing R1/R2/R4 RG link.

## Same-realization lineage matrix

| Object | Lorentzian BC cosmology / perturbations | Lorentzian BC Landau-Ginzburg | Simple Abelian/compact TGFT FRG controls |
|---|---|---|---|
| explicit gravity ancestry | YES | YES | NOT SUFFICIENTLY IDENTICAL TO BC GRAVITY TARGET |
| Lorentzian BC group/causal structure | YES | YES | NO |
| scalar relational clocks/rods as used by cosmology | YES | YES/related scalar variables | generally NO / different realization |
| nonperturbative full FRG trajectory | NO | NO | YES, but for different simplified models/truncations |
| condensate/mean-field phase | YES | YES | branch/model dependent |
| relational gravity observable | YES | indirect support, not full observable transport | NO BC relational observable |
| common same-realization chain | INCOMPLETE | INCOMPLETE | INCOMPATIBLE FOR SPLICING |

## KMQGB result

No row in the audited corpus supplies all required columns in one declared realization. The apparent near-closure obtained by combining Lorentzian BC relational cosmology with Abelian/simple-TGFT FRG is invalid under D6 same-realization composition discipline.

The correct disposition is therefore:

`BLOCKED_MISSING_REQUIRED_OBJECT__NO_AUDITED_PUBLISHED_SAME_REALIZATION_FULL_FRG_TO_RELATIONAL_GRAVITY_OBSERVABLE_CHAIN_FOR_GRAVITY_ANCESTRY_TGFT`

This is a **BLOCKED certificate**, not a scientific FAIL of TGFT. The existing mean-field and relational results remain positive scoped structural evidence.

## Missing certificate payload

A future closure object must contain, within one declared gravity TGFT realization:

`{microscopic action, group/signature data, gauge/closure constraints, simplicity/gravity-selection map, matter-reference variables, RG regulator and truncation, beta functions/flow trajectory, fixed/critical/continuum prescription, parameter and scale ancestry, condensate/state map, relational gravitational observable, normalization/observation operator, GR/EFT and alternative-QG comparators, truncation/RG/mean-field/numerical error ledger}`.

The payload must state which links are exact, asymptotic, truncation-dependent or conjectural.

## Scientific consequence

The TGFT branch is **parked on a concrete missing published object** rather than repeatedly searched as an undefined problem. Since the blocker is literature/derivation authority rather than numerical cost, heavy compute remains IDLE.

The parent `GFT_TENSOR_MODELS` row remains `PARTIAL_SUBFAMILY_ONLY`, because the enhanced/nonmelonic pure-random-tensor branch also remains unresolved.

## Global gates unchanged

- Tier-1 terminal: 1/14.
- Tier-1 nonterminal: 13/14.
- D2: `NOT_CLOSED_COVERAGE_AND_OBJECTS`.
- D4: `PARTIAL_ACTIVE_SET_MATRIX__GLOBAL_COVERAGE_NOT_CLOSED`.
- D7: `NOT_CLOSED`.
- Paper IV: `NOT_YET_AUTHORIZED`.
- Candidate Gravity R3: 24%, inactive.

## Next permitted gate

Because TGFT is now parked on a precise missing same-realization object, anti-idle policy moves to the independent surviving tensor branch:

`PURE_RANDOM_TENSOR_ENHANCED_NONMELONIC_CONTINUUM_TO_NORMALIZED_4D_GRAVITY_OBSERVABLE_COMPARATOR`

This gate must distinguish proven enhanced/nonmelonic universality classes from still-open interaction/RG sectors and may not extrapolate the standard melonic branched-polymer FAIL to the entire pure-tensor branch.
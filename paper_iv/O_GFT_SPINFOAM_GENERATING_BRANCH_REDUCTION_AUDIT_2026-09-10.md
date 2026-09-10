# O-GFT — spin-foam-generating GFT independence/reduction audit

**Date:** 2026-09-10  
**Iteration:** 206  
**RQIR Core:** v1.0 **FROZEN**  
**Parent Tier-1 family:** `GFT_TENSOR_MODELS`

## Question

Does the microscopic gravity/spin-foam-generating GFT branch constitute an independent Tier-1 physical alternative, or is it an explicit second-quantized / Feynman-generating reformulation of an already counted LQG/spin-foam realization?

The frozen rule is applied narrowly: an explicit fixed-realization map may reduce coverage duplication, but it does **not** transfer a PASS/FAIL, does not define a family residual, and does not identify TGFT condensate/RG or pure-random-tensor branches with LQG unless their own physical map is supplied.

## Primary authorities and provenance

1. **D. Oriti, “Group field theory as the 2nd quantization of Loop Quantum Gravity,” Class. Quantum Grav. 33 (2016) 085005, DOI 10.1088/0264-9381/33/8/085005, arXiv:1310.7786.** The paper constructs a second-quantized reformulation of canonical LQG at the kinematical and dynamical level and states a general correspondence taking specified canonical spin-network dynamics to a specific GFT; the covariant spin-foam correspondence is obtained via the GFT definition.
2. **D. Oriti, J. P. Ryan, J. Thürigen, “Group field theories for all loop quantum gravity,” New J. Phys. 17 (2015) 023042, DOI 10.1088/1367-2630/17/2/023042, arXiv:1409.3150.** This extends GFT combinatorics to the full arbitrary-valence LQG state space and gives an explicit GFT formulation of the KKL spin-foam model. The work characterizes GFT as a second-quantized reformulation of the LQG state space and a completion of the spin-foam formalism.
3. **T. Krajewski, J. Magnen, V. Rivasseau, A. Tanasa, P. Vitale, “Quantum Corrections in the Group Field Theory Formulation of the EPRL/FK Models,” Phys. Rev. D 82 (2010) 124069, DOI 10.1103/PhysRevD.82.124069, arXiv:1007.3150.** This explicitly studies a GFT formulation of the EPRL/FK spin-foam models, confirming that fixed spin-foam dynamics can be encoded as GFT Feynman amplitudes.
4. **T. Krajewski, “Group field theories,” PoS QGQGS2011 (2011/2012), arXiv:1210.6257.** Review-level construction: GFTs reproduce spin-foam amplitudes in the perturbative expansion and treats BF/EPRL examples. Used only as corroboration, not as the decisive authority.

## Fixed-realization physical map

For the declared spin-foam-generating microscopic branch, the literature supplies the map

`LQG spin-network Hilbert/algebra + declared dynamics`

`<-> GFT Fock-space fields/operators + corresponding GFT dynamics`

and, covariantly,

`fixed GFT action + propagator/interaction kernels -> perturbative Feynman 2-complexes -> the corresponding named spin-foam amplitudes`.

This is stronger than mere analogy or shared variables. In the declared scope it is an explicit reformulation/generating completion of the same named microscopic dynamics.

## What the map does NOT prove

- It does not prove that **all** GFT/TGFT models are equivalent to one LQG/spin-foam theory.
- It does not reduce pure random tensor models lacking the Lie-group/geometric/simplicity data.
- It does not identify a condensate effective phase with the microscopic spin-foam observable without a same-realization derivation.
- It does not supply the missing LQG EPRL/KKL UV-to-IR/Area-Regge parameter-ancestry certificate.
- It does not supply a continuum normalized gravity observable, common-domain comparator, or propagated continuum/RG/mean-field error budget for the parent `GFT_TENSOR_MODELS` family.

## Scoped disposition

`PASS_REDUCTION_GATE__GFT_SPINFOAM_GENERATING_FIXED_REALIZATIONS_REDUCE_TO_EXISTING_LQG_SPINFOAM_TIER1_WITH_EXPLICIT_SECOND_QUANTIZED_AMPLITUDE_MAP`

Coverage consequence:

`GFT_SPINFOAM_GENERATING_GRAVITY_MODELS` is **not counted as an independent additional Tier-1 physical family inside the GFT/tensor umbrella when the fixed GFT is explicitly constructed to reproduce a named LQG/spin-foam dynamics**. Its unresolved continuum/observable obligations inherit the already-declared LQG/spin-foam object gap only within that mapped realization; no scientific PASS/FAIL is inherited.

The generalized all-graph/KKL GFT completion is likewise a reformulation/completion of the mapped LQG/spin-foam dynamics in its explicit construction, not evidence for a distinct physical family by itself.

## Parent-family disposition

`GFT_TENSOR_MODELS` remains `PARTIAL_SUBFAMILY_ONLY`.

Surviving materially non-reduced sectors include at minimum:

- gravity-ancestry TGFT RG/phase structure where a full same-realization RG trajectory to the relational gravity observable remains missing;
- derived condensate/hydrodynamic observables, which are state/phase sectors and require microscopic ancestry plus controlled error transport;
- pure random tensor models, whose solved melonic sector has a scoped FAIL while enhanced/nonmelonic gravity closure remains BLOCKED.

Family residual remains **undefined**. No family PASS, family FAIL, or `NEW_REQUIRED` exclusion is authorized.

## Error/remainder ledger

This iteration is an **exact structural reduction audit**, not a numerical observable fit. The reduction claim is limited to the explicit fixed-realization algebra/dynamics/amplitude maps in the cited constructions. The unresolved physical remainder is precisely the absence of a controlled continuum/observable map for the surviving non-reduced GFT/TGFT branches; it is not assigned zero.

## Next gate

`GFT_TENSOR_SURVIVING_NONREDUCED_BRANCHES_TERMINAL_DISPOSITION_PLUS_CONTINUUM_OBSERVABLE_COMPARATOR_ERROR_CERTIFICATE`

Priority subgate:

`GFT_GENERALIZED_GRAPH_COMPLETION_SCOPE_EXHAUSTION_AND_TGFT_MICROSCOPIC_ANCESTRY_BOUNDARY_CERTIFICATE`.

Heavy compute remains `IDLE`: the blocker is equivalence/provenance/continuum matching, not a prospectively frozen numerical discriminator.

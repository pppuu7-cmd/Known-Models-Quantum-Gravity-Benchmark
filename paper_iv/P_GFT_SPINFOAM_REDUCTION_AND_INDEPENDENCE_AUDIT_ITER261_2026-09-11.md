# GFT / spinfoam reduction and independence audit — Iter261

Date: 2026-09-11
Family: `GFT_TENSOR_MODELS`
RQIR Core: `v1.0 FROZEN`

## Question
Can the GFT/Tensor-model Tier-1 row be reduced to the LQG/spinfoam row, or does it contain materially independent sectors that must remain separately represented?

## Authorities checked
1. T. Krajewski, *Group field theories*, arXiv:1210.6257. The review states that GFTs reproduce spin-foam amplitudes and explicitly examines BF theory and the EPRL model.
2. T. Krajewski, J. Magnen, V. Rivasseau, A. Tanasa, P. Vitale, *Quantum Corrections in the Group Field Theory Formulation of the EPRL/FK Models*, arXiv:1007.3150. This supplies an explicit GFT formulation of EPRL/FK spin-foam models.
3. J. Ben Geloun, R. Gurau, V. Rivasseau, *EPRL/FK Group Field Theory*, arXiv:1008.0354. The EPRL/FK vertex/propagator data are encoded in a GFT whose perturbative graphs generate the corresponding spin-foam amplitudes.
4. A. Mozota Frauca, *Foundational Issues in Group Field Theory*, Foundations of Physics 54, 33 (2024). It explicitly distinguishes the covariant GFT construction, whose perturbative amplitudes reproduce spin foams, from broader/canonical GFT interpretations and argues that their full foundational equivalence should not simply be assumed.
5. A. F. Jercher, D. Oriti, A. G. A. Pithis, *Emergent Cosmology from Quantum Gravity in the Lorentzian Barrett-Crane Tensorial Group Field Theory Model*, JCAP 01 (2022) 050, arXiv:2112.00091. The Lorentzian Barrett-Crane TGFT condensate sector yields effective cosmology similar to EPRL-like models but only supports the expectation that the two may lie in the same continuum universality class.
6. A. Marchetti, E. Wilson-Ewing, *Relational observables in group field theory*, Class. Quantum Grav. 42 (2025) 155008. This develops relational-observable machinery in GFT beyond the narrow perturbative spin-foam-amplitude identification.
7. Recent Lorentzian Barrett-Crane TGFT phase-transition work, Phys. Rev. D 111, 026014 (2025), supplies nontrivial continuum/mean-field structure but not an equivalence theorem to EPRL/FK.

## Result 1 — EPRL/FK covariant GFT is not an independent Tier-1 physical parent at the perturbative amplitude level
For the specifically constructed EPRL/FK covariant GFT, the perturbative/Feynman expansion generates the EPRL/FK spin-foam amplitudes. Therefore counting both the corresponding EPRL/FK-GFT realization and the EPRL/FK spinfoam realization as two independent failures/successes would double-count the same amplitude family.

Scoped reduction:
`MERGED_INTO_LQG_SPINFOAM_WITH_EXPLICIT_PERTURBATIVE_GFT_TO_EPRL_FK_SPINFOAM_AMPLITUDE_MAP`

This reduction is scoped to the declared covariant EPRL/FK GFT and its perturbative amplitude content. It is not a theorem that every GFT observable, state, continuum phase or canonical construction is identical to LQG/spinfoams.

## Result 2 — broad GFT/TGFT cannot be wholly merged into LQG/spinfoams
The broad Tier-1 label also contains materially different constructions, including Lorentzian Barrett-Crane TGFT, tensorial interactions/RG and condensate/hydrodynamic sectors, and canonical/relational-observable constructions. The checked literature does not provide a single reduction/equivalence map identifying all these sectors with one EPRL/FK spinfoam realization.

In particular, the Barrett-Crane condensate result says its cosmology supports an *expectation* that BC and EPRL-like models may share a continuum universality class. This is not an RG/universality theorem with matching fixed point, relevant directions, observables and propagated errors.

The 2024 foundational analysis also explicitly warns against treating covariant and canonical GFT formulations as automatically equivalent.

Therefore the broad parent remains independent/nonterminal outside the reduced EPRL/FK child.

## Result 3 — remaining non-EPRL GFT object
A terminal KMQGB disposition of the independent remainder would require at least one of:

A. an explicit universality/reduction theorem mapping the relevant non-EPRL TGFT continuum phase to an already benchmarked spinfoam/LQG realization, including parameter/observable/error transport; or
B. a comparator-ready independent gravity object from the non-EPRL TGFT sector with microscopic realization, continuum map, normalized physical observable, common-domain comparator and propagated truncation/RG/mean-field errors.

The 2025 Lorentzian Barrett-Crane phase-transition work strengthens the existence of a continuum condensate regime, and the 2025 relational-observable work strengthens observable definition, but neither closes the complete same-realization comparator chain above.

Remaining disposition:
`BLOCKED_MISSING_REQUIRED_OBJECT__NON_EPRL_TGFT_UNIVERSALITY_REDUCTION_THEOREM_OR_COMPARATOR_READY_INDEPENDENT_GRAVITY_OBSERVABLE_WITH_ERROR_TRANSPORT`

## Family disposition
`GFT_TENSOR_MODELS` remains `PARTIAL_SUBFAMILY_ONLY`, but its ambiguity is materially reduced:
- EPRL/FK covariant GFT child: explicitly reduced/merged into `LQG_SPINFOAM` for perturbative amplitude benchmarking;
- non-EPRL / continuum / canonical TGFT remainder: independent and nonterminal pending a universality theorem or comparator-ready gravity object.

No family-level scientific FAIL is authorized. No `NEW_REQUIRED` inference is authorized.

## Governance
- D2: `NOT_CLOSED`.
- D4: `PARTIAL_GLOBAL_NOT_CLOSED`.
- D7: `NOT_CLOSED / NOT_YET_AUTHORIZED`.
- Candidate Gravity R3: 24%.
- Heavy compute: `IDLE` because the remaining blocker is equivalence/observable provenance rather than a numerical threshold.

## Polygon saturation
Operational known-school polygon saturation increases from ~95% to ~96% because the GFT row is no longer an undifferentiated open family: its EPRL/FK child is explicitly reduced to the spinfoam row and the independent remainder is bounded by a precise missing-object gate.

This is operational saturation only, not strict D7 closure or family-level exclusion.

## Next gate
Move to another finite Tier-1 blocker, prioritizing `HORAVA_LIFSHITZ` projectable/non-projectable split or `ASYMPTOTIC_SAFETY` same-realization amplitude/comparator object. Do not repeat generic GFT/spinfoam correspondence searches unless new authority supplies the missing universality/reduction or comparator-ready object.

# O-GFT / tensor-model material branch census audit — 2026-09-10

**KMQGB iteration:** 203  
**RQIR Core:** v1.0 FROZEN  
**Parent:** `GFT_TENSOR_MODELS`  
**Purpose:** replace the ambiguous single-label family with a material branch map that respects microscopic ancestry, collective dynamics, geometric data and continuum universality.

## Why this census is required

The label “GFT/tensor models” covers constructions that are not interchangeable under RQIR. Some GFTs are explicitly engineered so their Feynman amplitudes reproduce named spin-foam models; tensorial GFT adds an independent renormalization/phase-structure layer; condensate cosmology is a derived collective state sector; pure random tensor models can exist without the group/geometric/simplicity data needed for a spin-foam interpretation.

A valid family-level D2/D4 disposition therefore cannot infer one branch from another by name similarity.

## Primary authorities

### Explicit spin-foam-generating GFT

Oriti, Ryan and Thürigen, *Group field theories for all loop quantum gravity*, New J. Phys. 17 (2015) 023042, arXiv:1409.3150, construct an explicit GFT formulation of the KKL spin-foam model and generalize the combinatorics to the full LQG graph state space. This supplies an explicit microscopic amplitude ancestry for the selected KKL-compatible GFT branch.

Oriti, *Group field theory as the 2nd quantization of Loop Quantum Gravity*, arXiv:1310.7786, formulates the broader second-quantized LQG/GFT correspondence and makes clear that GFT dynamics can encode graph-changing canonical dynamics and covariant spin-foam amplitudes.

### Tensorial GFT / RG and phase structure

Carrozza, *Flowing in Group Field Theory Space: a Review*, SIGMA 12 (2016) 070, arXiv:1603.01902, reviews closure-constrained GFTs closely related to lattice gauge/spin-foam models and the distinct tensorial-renormalization structure obtained by importing tensor-model tools.

Ben Geloun, Martini and Oriti, Phys. Rev. D 94 (2016) 024017, study rank-d TGFTs on group manifolds, with and without gauge-invariance constraints, and find UV/IR fixed-point structure and condensation-type phase-transition evidence in a truncation. The paper explicitly states that a TGFT requires appropriate data to carry a quantum-spacetime interpretation; the abstract TGFT formalism by itself is not a gravity certificate.

Pithis and Thürigen, Phys. Lett. B 816 (2021) 136215 / arXiv:2007.08982, show in the cyclic-melonic local-potential setting on compact configuration space that the effective dimension flows to zero and symmetry is restored. Their conclusion is that noncompact degrees of freedom are required for a continuum-spacetime phase transition in that stated setting. This is a scoped structural constraint, not a family-wide no-go.

Marchetti, Oriti, Pithis and Thürigen, arXiv:2110.15336, show how phase transitions can occur when noncompact group variables or appropriate local matter/reference degrees of freedom are included, reinforcing the fact that “TGFT phase structure” is realization-dependent.

### Pure tensor models

Random tensor models retain the combinatorial/tensor structure while dropping the Lie-group geometric data. The 2020 GFT renormalization review explicitly describes GFTs as group-theoretic enrichments of random tensor models and notes that replacing the Lie-group domain by a finite set reduces the theory to a tensor model. This establishes a one-way structural relation but not an automatic gravity/spin-foam interpretation for a generic tensor model.

Multi-critical/enhanced tensor-model analyses show that generic tree/melonic dominated sectors can lead to branched-polymer continuum universality, while modified/enhanced nonmelonic interactions can access different universality classes. Therefore KMQGB forbids promoting “melonic -> branched polymer” into a family-wide tensor-model FAIL.

## Frozen material branch map

The authoritative machine-readable branch map is

`paper_iv/GFT_TENSOR_MATERIAL_BRANCH_MAP_ITER203.json`.

It separates five material classes.

### B1 — `GFT_SPINFOAM_GENERATING_GRAVITY_MODELS`

Microscopic geometric GFTs with group/gauge/simplicity data chosen so perturbative amplitudes reproduce named spin-foam/lattice-gauge models. Examples include topological Boulatov/Ooguri controls and gravity-oriented Barrett-Crane, EPRL/FK and KKL-compatible constructions.

**Relation:** `REDUCES_TO_OR_GENERATES_NAMED_SPINFOAM_AMPLITUDES_IN_FIXED_REALIZATION`.

### B2 — `GFT_GENERALIZED_GRAPH_COMPLETION`

Multi-field/dually-weighted/all-LQG GFT constructions that retain explicit spin-foam ancestry while adding second-quantized graph-changing sums over generated complexes.

**Relation:** `SPINFOAM_RELATED_BUT_NOT_REDUCIBLE_TO_ONE_FIXED_COMPLEX_OBJECT`.

### B3 — `TGFT_RG_PHASE_STRUCTURE`

Tensor-invariant GFT with RG/thermodynamic dynamics. Some realizations carry explicit quantum-geometric/spin-foam data; other Abelian/SU(2) models are structural RG testbeds. A gravity interpretation must be earned by explicit geometric/simplicity ancestry rather than inherited from the acronym TGFT.

**Relation:** `BRANCH_DEPENDENT__REQUIRES_EXPLICIT_GEOMETRIC_AND_SIMPLICITY_DATA`.

### B4 — `GFT_CONDENSATE_HYDRODYNAMIC_COSMOLOGY`

Collective/condensate/hydrodynamic states derived from a declared microscopic GFT parent. These can carry relational observables and GR-limit calculations, but they are not independent microscopic schools.

**Relation:** `DERIVED_FROM_DECLARED_GFT_PARENT__NOT_AN_INDEPENDENT_MICROSCOPIC_FAMILY`.

### B5 — `PURE_RANDOM_TENSOR_MODELS`

Combinatorial tensor/random-geometry models without the group-theoretic geometric data that makes a GFT amplitude a spin-foam amplitude.

**Relation:** `NOT_AUTOMATICALLY_REDUCIBLE_TO_SPINFOAM__ADDITIONAL_GROUP_GEOMETRY_DATA_REQUIRED`.

Their continuum universality is interaction/model dependent. Generic melonic/tree-like dominance can produce branched-polymer behavior, but enhanced/nonmelonic sectors prevent a family-wide exclusion theorem.

## Cross-cutting labels

`colored`, `melonic` and `condensate` are not accepted as independent physical families by label alone:

- coloring is primarily a combinatorial/topology-control device;
- melonic identifies an interaction/large-N dominance sector;
- condensate identifies a state/phase and inherits microscopic ancestry from a declared parent.

They can become separate RQIR rows only if they induce response-distinct physical dynamics that cannot be represented by their parent branch.

## Governance result

**`PASS_GOVERNANCE_GATE__GFT_TENSOR_MATERIAL_BRANCH_CENSUS_SEPARATES_SPINFOAM_GENERATING_GFT__SECOND_QUANTIZED_GRAPH_COMPLETION__TGFT_RG_PHASE_STRUCTURE__DERIVED_CONDENSATE_SECTORS__AND_PURE_RANDOM_TENSOR_UNIVERSALITY`**

This closes the **census/classification component only** of the Iter202 blocker. It does not close the parent family scientifically.

## Refined family blocker after census

**`GFT_TENSOR_MATERIAL_BRANCH_TERMINAL_DISPOSITION_PLUS_CONTROLLED_GRAVITY_CONTINUUM_TRAJECTORY_NORMALIZED_OBSERVABLE_COMPARATOR_ERROR_CERTIFICATE`**

Remaining obligations:

1. terminal disposition of each material branch without cross-branch splicing;
2. for any surviving gravity branch, one controlled continuum/thermodynamic trajectory in a fixed realization;
3. a relational gravitational observable transported through that trajectory;
4. normalized common-domain observation operator;
5. GR/EFT and alternative-QG comparators;
6. full continuum/RG/condensate/truncation/numerical error ledger;
7. family-level residual only after the above are closed.

## Scientific discipline

The census does not change Tier-1 terminal counts, does not add a comparator-ready residual row and does not authorize `NEW_REQUIRED`. `GFT_TENSOR_MODELS` remains `PARTIAL_SUBFAMILY_ONLY`; D2/D4/D7 remain open; Candidate Gravity remains inactive at R3=24%.

Heavy compute stays `IDLE`: the next missing object is branch-specific continuum/comparator authority, not a numerical scan over an undefined unified tensor-model parameter space.
# KMQGB Current Benchmark Front

**Updated:** 2026-09-10  
**KMQGB iteration:** **203**  
**Phase:** **RQIR Core v1.0 FROZEN / GFT-tensor material branch census closed / branch terminal dispositions + controlled gravity continuum/comparator remain open**.

## Stable metrics

- R1 repository readiness: **100%**.
- R2 methodology/material readiness: **100%**.
- Candidate Gravity R3: **24%**, inactive.
- Candidate activation condition: D7=`NEW_REQUIRED` only.
- AS/LQG/CFS Closure Wave 02: **0/3 terminal**.
- Tier-1: **1/14 terminal**, **13/14 nonterminal**.
- Tier-2 unresolved: **0**.
- comparator-ready scoped gravity residual/control rows remain **10**.
- No scientific-readiness promotion in Iter203.

## Validation baseline / auto-research reconciliation

Canonical Iter202 main head is `f23432b2cfc52d474799e8b0cfa488d8f623f012`. Its post-merge methodology CI run `34473197943` completed successfully and reproducibility-release run `34473254410` also completed successfully. The hourly KMQGB auto-research was rechecked before Iter203 and had not created a newer competing front.

## Paper-IV global gates

D1 PASS; D2A NOT_CLOSED; D2B NOT_CLOSED; D2 `NOT_CLOSED_COVERAGE_AND_OBJECTS`; D3 PARTIAL; D4 `PARTIAL_ACTIVE_SET_MATRIX__GLOBAL_COVERAGE_NOT_CLOSED`; D5 PASS; D6 `PASS_RULE_TARGETS_OPEN`; D7 NOT_CLOSED; global decision **`NOT_YET_AUTHORIZED`**.

## Iter202 retained results

Two GFT components remain valid:

- selected KKL-compatible GFT has an explicit microscopic spin-foam amplitude relation;
- Lorentzian Barrett-Crane GFT/TGFT condensate/relational constructions provide GR-limit effective dynamics and quantum-correction channels.

Neither is promoted to family sufficiency or a comparator-ready gravity residual.

## Iter203 — material branch census

The umbrella `GFT_TENSOR_MODELS` row has now been partitioned into five material classes using microscopic ancestry, geometric/group data and level of dynamics rather than labels alone.

### B1 — spin-foam-generating gravity GFT

`GFT_SPINFOAM_GENERATING_GRAVITY_MODELS`

Lie-group field data plus gauge/geometric/simplicity structure are chosen so perturbative GFT amplitudes reproduce named spin-foam/lattice-gauge models. Examples include topological Boulatov/Ooguri controls and gravity-oriented Barrett-Crane, EPRL/FK and KKL-compatible constructions.

Relation: `REDUCES_TO_OR_GENERATES_NAMED_SPINFOAM_AMPLITUDES_IN_FIXED_REALIZATION`.

### B2 — generalized second-quantized graph completion

`GFT_GENERALIZED_GRAPH_COMPLETION`

Multi-field/dually-weighted/all-LQG constructions keep explicit spin-foam ancestry but add graph-changing sums over generated complexes and therefore are not reducible to one fixed-complex amplitude object.

Relation: `SPINFOAM_RELATED_BUT_NOT_REDUCIBLE_TO_ONE_FIXED_COMPLEX_OBJECT`.

### B3 — TGFT RG/phase structure

`TGFT_RG_PHASE_STRUCTURE`

Tensor-invariant GFT carries independent field-theoretic RG/thermodynamic structure. Some realizations include explicit quantum-geometric/spin-foam data; simpler Abelian/SU(2) RG models can instead be structural testbeds. Gravity status must be earned from geometric/simplicity ancestry.

Relation: `BRANCH_DEPENDENT__REQUIRES_EXPLICIT_GEOMETRIC_AND_SIMPLICITY_DATA`.

### B4 — condensate/hydrodynamic cosmology

`GFT_CONDENSATE_HYDRODYNAMIC_COSMOLOGY`

This is a derived collective state/phase sector of a declared microscopic GFT parent, not an independent microscopic school.

Relation: `DERIVED_FROM_DECLARED_GFT_PARENT__NOT_AN_INDEPENDENT_MICROSCOPIC_FAMILY`.

### B5 — pure random tensor models

`PURE_RANDOM_TENSOR_MODELS`

These retain tensor/combinatorial random-geometry structure but lack the Lie-group geometric data that makes a GFT Feynman amplitude a spin-foam amplitude.

Relation: `NOT_AUTOMATICALLY_REDUCIBLE_TO_SPINFOAM__ADDITIONAL_GROUP_GEOMETRY_DATA_REQUIRED`.

Generic melonic/tree-dominated continuum behavior can lie in branched-polymer universality, but KMQGB explicitly does **not** promote this to a family-wide tensor-model FAIL because enhanced/nonmelonic interactions and geometric TGFT data can change the universality class.

## Governance result

`PASS_GOVERNANCE_GATE__GFT_TENSOR_MATERIAL_BRANCH_CENSUS_SEPARATES_SPINFOAM_GENERATING_GFT__SECOND_QUANTIZED_GRAPH_COMPLETION__TGFT_RG_PHASE_STRUCTURE__DERIVED_CONDENSATE_SECTORS__AND_PURE_RANDOM_TENSOR_UNIVERSALITY`

Machine-readable authority:

- `paper_iv/GFT_TENSOR_MATERIAL_BRANCH_MAP_ITER203.json`
- `paper_iv/O_GFT_TENSOR_MATERIAL_BRANCH_CENSUS_AUDIT_2026-09-10.md`
- `paper_iv/PAPER_IV_COMPARATOR_RESIDUAL_MATRIX_DELTA_203.json`
- `paper_iv/PAPER_IV_DECISION_LEDGER_DELTA_203.json`
- `recovery/RECOVERY_DELTA_203.md`

The census/classification component is closed. No new comparator-ready residual row is added.

## Refined GFT/tensor family blocker

**`GFT_TENSOR_MATERIAL_BRANCH_TERMINAL_DISPOSITION_PLUS_CONTROLLED_GRAVITY_CONTINUUM_TRAJECTORY_NORMALIZED_OBSERVABLE_COMPARATOR_ERROR_CERTIFICATE`**.

Remaining obligations:

1. terminal disposition of the five material branches without cross-branch splicing;
2. for any surviving gravity branch, a fixed-realization controlled continuum/thermodynamic/critical trajectory;
3. relational gravitational observable transported through that trajectory;
4. normalized common physical observation operator/domain;
5. same-domain GR/EFT and alternative-QG comparators;
6. full continuum/RG/condensate/mean-field/truncation/numerical error ledger;
7. family-level residual only after those objects exist.

## Immediate next scientific gate

**`PURE_RANDOM_TENSOR_CONTINUUM_UNIVERSALITY_SCOPED_TERMINAL_DISPOSITION`**.

This is chosen first because pure random tensor models are the most sharply separated material branch. The gate must distinguish generic melonic/branched-polymer universality from enhanced/nonmelonic continuum classes and must not extrapolate any scoped no-go to geometric GFT/TGFT.

## Other parked fronts retained

- LQG: EPRL/KKL UV→IR crossover with topology escape and gamma ancestry.
- CDT/EDT: 4D line of constant physics, `a -> 0` observable transport, comparator/error certificate and EDT disposition.
- Causal sets: fundamental quantum gravitational measure → manifoldlike `3+1` continuum → normalized gravity observable/comparator.
- Hořava: material branches parked pending new same-realization UV→IR authority.

## Heavy compute

**IDLE.** The next GFT/tensor question is a branch-specific continuum-universality disposition. A numerical scan over an undefined umbrella tensor-model parameter space would mix inequivalent universality classes and cannot validly change D7.

## Exact next order

1. exact-head CI-validate Iter203;
2. recheck the KMQGB hourly auto-research before integration;
3. if no newer conflicting canonical front exists, merge Iter203;
4. audit pure/random tensor-model continuum universality and determine whether any subbranch can receive a scoped terminal PASS/FAIL/BLOCKED disposition;
5. retain `NOT_YET_AUTHORIZED` until D2 and D4 actually close.
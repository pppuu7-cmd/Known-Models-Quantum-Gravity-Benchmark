# KMQGB Current Benchmark Front

**Updated:** 2026-09-10  
**KMQGB iteration:** **202**  
**Phase:** **RQIR Core v1.0 FROZEN / GFT microscopic spin-foam relation scoped-pass / relational GR-limit and correction channels scoped-pass / controlled continuum + comparator closure blocked**.

## Stable metrics

- R1 repository readiness: **100%**.
- R2 methodology/material readiness: **100%**.
- Candidate Gravity R3: **24%**, inactive.
- Candidate activation condition: D7=`NEW_REQUIRED` only.
- AS/LQG/CFS Closure Wave 02: **0/3 terminal**.
- Tier-1: **1/14 terminal**, **13/14 nonterminal**.
- Tier-2 unresolved: **0**.
- comparator-ready scoped gravity residual/control rows remain **10**.
- No scientific-readiness promotion in Iter202.

## Validation baseline / auto-research reconciliation

Canonical Iter201 main head is `ef0ca4b3bc50addc0577a4528c8f2dafe3e4f21a`. The hourly KMQGB auto-research repaired the Iter201 recovery-JSON infrastructure defect, merged PR #14, and the post-merge reproducibility-release run `34470705526` completed successfully. No Iter202 branch or PR existed when this iteration began, so the present GFT work is nonduplicating.

## Paper-IV global gates

D1 PASS; D2A NOT_CLOSED; D2B NOT_CLOSED; D2 `NOT_CLOSED_COVERAGE_AND_OBJECTS`; D3 PARTIAL; D4 `PARTIAL_ACTIVE_SET_MATRIX__GLOBAL_COVERAGE_NOT_CLOSED`; D5 PASS; D6 `PASS_RULE_TARGETS_OPEN`; D7 NOT_CLOSED; global decision **`NOT_YET_AUTHORIZED`**.

## Iter202A — selected GFT ↔ spin-foam microscopic relation

Oriti, Ryan and Thürigen provide an explicit GFT formulation of the KKL spin-foam model and formulate GFT as a second-quantized reformulation/completion of the LQG/spin-foam framework. For a selected KKL-compatible realization, the microscopic relation can therefore be frozen as

`fixed GFT propagator/interaction data -> perturbative GFT Feynman expansion -> KKL spin-foam amplitudes on generated complexes`.

Scoped result:

`PASS_STRUCTURAL_GATE__SELECTED_KKL_COMPATIBLE_GFT_HAS_EXPLICIT_SPINFOAM_REDUCTION_MAP_AT_THE_MICROSCOPIC_AMPLITUDE_LEVEL`.

This is **not** family-wide equivalence. GFT/TGFT contains graph-changing sums over complexes, tensorial interactions, RG/phase structure and collective condensate dynamics not exhausted by one fixed spin-foam amplitude.

## Iter202B — relational GFT continuum/effective observables

Causally complete Lorentzian Barrett-Crane GFT/TGFT constructions supply relational cosmological observables using scalar reference fields. Published perturbation dynamics recover the GR regime for sub-Planckian modes and develop quantum-gravity modifications outside that regime. Mean-field Landau-Ginzburg analysis supports a nontrivial condensate phase for several Lorentzian Barrett-Crane interaction classes.

The 2026 GFT hydrodynamic derivation of emergent scalar dynamics on FLRW geometry further recovers the late-time massless-scalar GR limit and produces early-universe dispersive/dissipative modified-dispersion corrections from the microscopic GFT dynamics.

Scoped result:

`PASS_STRUCTURAL_GATE__GFT_RELATIONAL_CONDENSATE_DYNAMICS_SUPPLIES_EXPLICIT_GR_LIMIT_AND_QUANTUM_CORRECTION_CHANNELS`.

These are material theory-to-effective-observable controls, but no new comparator-ready gravity residual row is added because the same declared realization does not yet jointly carry a nonperturbatively controlled continuum trajectory, normalized observation operator, common-domain comparator suite and full error/remainder ledger.

Authorities:

- `paper_iv/O_GFT_SPINFOAM_REDUCTION_AND_RELATIONAL_OBSERVABLE_SCOPE_AUDIT_2026-09-10.md`
- `paper_iv/PAPER_IV_COMPARATOR_RESIDUAL_MATRIX_DELTA_202.json`
- `paper_iv/PAPER_IV_DECISION_LEDGER_DELTA_202.json`
- `recovery/RECOVERY_DELTA_202.md`

## Refined GFT family blocker

The previous blocker

`GFT_SPINFOAM_INDEPENDENCE_OR_REDUCTION_PLUS_FULL_GRAVITY_OBSERVABLE_COMPARATOR_CERTIFICATE`

is replaced by

**`GFT_MATERIAL_BRANCH_REDUCTION_OR_INDEPENDENCE_MAP_PLUS_CONTROLLED_CONTINUUM_TRAJECTORY_AND_NORMALIZED_RELATIONAL_GRAVITY_OBSERVABLE_COMPARATOR_ERROR_CERTIFICATE`**.

Required payload:

1. material GFT/TGFT branch census;
2. explicit `REDUCES_TO_SPINFOAM(parent)` or `INDEPENDENT_COLLECTIVE_DYNAMICS` classification for each material branch;
3. one fixed Lorentzian gravity realization with controlled continuum/thermodynamic/critical trajectory;
4. relational gravitational observable transported through that trajectory;
5. common physical observation normalization/operator;
6. same-domain GR/EFT and alternative-QG comparator predictions;
7. continuum + condensate/mean-field + interaction/truncation + numerical error ledger;
8. family-level disposition without promoting a single Barrett-Crane cosmology child to the whole family.

## Parked family fronts retained

- LQG: EPRL/KKL UV→IR crossover with topology escape and gamma ancestry.
- CDT/EDT: 4D line of constant physics, `a -> 0` observable transport, comparator/error certificate and EDT disposition.
- Causal sets: fundamental quantum gravitational measure → manifoldlike `3+1` continuum → normalized gravity observable/comparator.
- Hořava: material branches parked pending new same-realization UV→IR authority.

## Heavy compute

**IDLE.** The immediate GFT deficit is classification/provenance plus continuum-control structure. A brute-force numerical run without a prospectively frozen branch, critical trajectory and observation operator cannot change the family terminal classification.

## Exact next order

1. exact-head CI-validate Iter202;
2. recheck the hourly KMQGB auto-research before integration;
3. if no newer conflicting canonical front exists, merge Iter202;
4. then test whether a material GFT/TGFT branch census can be made sufficiently explicit from existing primary literature to close the first remaining component of the refined blocker;
5. if not, park GFT at this literature ceiling and rotate to another Tier-1 family with an analytically closable object.

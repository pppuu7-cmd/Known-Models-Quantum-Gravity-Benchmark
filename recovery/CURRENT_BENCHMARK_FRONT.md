# KMQGB Current Benchmark Front

**Updated:** 2026-09-10  
**KMQGB iteration:** **206**  
**Phase:** **RQIR Core v1.0 FROZEN / fixed spin-foam-generating GFT reduced to mapped LQG/spinfoam Tier-1 / surviving TGFT-tensor branches nonterminal**.

## Stable metrics

- R1 repository readiness: **100%**.
- R2 methodology/material readiness: **100%**.
- Candidate Gravity R3: **24%**, inactive.
- Candidate activation condition: D7=`NEW_REQUIRED` only.
- AS/LQG/CFS Closure Wave 02: **0/3 terminal**.
- Tier-1: **1/14 terminal**, **13/14 nonterminal**.
- Tier-2 unresolved: **0**.
- scoped child comparator/residual-control rows: **11**.
- scoped child scientific FAIL rows: **3**.
- No family-level scientific-readiness promotion in Iter206.

## Validation baseline

Iter205 authoritative head `3183e0f4c034c2ef910f6057bc497ceed87d489c` is fully validated: methodology CI run `34480282784` completed `success`, and reproducibility-release run `34480349424` completed `success`. No running/queued scientific job was duplicated before Iter206.

## Paper-IV global gates

D1 PASS; D2A NOT_CLOSED; D2B NOT_CLOSED; D2 `NOT_CLOSED_COVERAGE_AND_OBJECTS`; D3 PARTIAL; D4 `PARTIAL_ACTIVE_SET_MATRIX__GLOBAL_COVERAGE_NOT_CLOSED`; D5 PASS; D6 `PASS_RULE_TARGETS_OPEN`; D7 NOT_CLOSED; global decision **`NOT_YET_AUTHORIZED`**.

## Iter206 — GFT spin-foam-generating branch reduction

Primary literature supplies an explicit fixed-realization map between canonical LQG spin-network dynamics and a corresponding GFT second-quantized dynamics, and explicit GFT formulations exist for EPRL/FK and generalized KKL/all-LQG spin-foam constructions.

Scoped disposition:

`PASS_REDUCTION_GATE__GFT_SPINFOAM_GENERATING_FIXED_REALIZATIONS_REDUCE_TO_EXISTING_LQG_SPINFOAM_TIER1_WITH_EXPLICIT_SECOND_QUANTIZED_AMPLITUDE_MAP`

Interpretation: when a GFT is explicitly constructed to encode a named LQG/spin-foam dynamics, it is not counted as an additional independent Tier-1 physical family. This removes a coverage double-count only within the declared map. It does **not** transfer scientific PASS/FAIL and does not define a family residual.

The generalized KKL/all-graph GFT construction is likewise reduced within its explicit LQG/spin-foam construction. Scope exhaustion remains required for generalized GFTs not covered by that map.

## Surviving non-reduced GFT/tensor sectors

- gravity-ancestry TGFT RG/phase structure: full same-realization RG trajectory to relational gravity observable remains `BLOCKED_MISSING_REQUIRED_OBJECT`;
- condensate/hydrodynamic cosmology: derived state/phase sector requiring microscopic ancestry plus controlled continuum/error transport;
- pure random tensors: standard melonic large-N sector retains scoped scientific FAIL, while enhanced/nonmelonic gravity closure remains BLOCKED.

Therefore `GFT_TENSOR_MODELS` remains `PARTIAL_SUBFAMILY_ONLY`; family residual remains **undefined**.

## Authorities

- `paper_iv/O_GFT_SPINFOAM_GENERATING_BRANCH_REDUCTION_AUDIT_2026-09-10.md`
- `paper_iv/GFT_TENSOR_MATERIAL_BRANCH_MAP_ITER206.json`
- `paper_iv/PAPER_IV_COMPARATOR_RESIDUAL_MATRIX_DELTA_206.json`
- `paper_iv/PAPER_IV_DECISION_LEDGER_DELTA_206.json`
- `recovery/RECOVERY_DELTA_206.md`

Primary literature: Oriti, CQG 33 (2016) 085005, DOI `10.1088/0264-9381/33/8/085005`; Oriti-Ryan-Thürigen, NJP 17 (2015) 023042, DOI `10.1088/1367-2630/17/2/023042`; Krajewski et al., PRD 82 (2010) 124069, DOI `10.1103/PhysRevD.82.124069`.

## Immediate next scientific gate

**`GFT_GENERALIZED_GRAPH_COMPLETION_SCOPE_EXHAUSTION_AND_TGFT_MICROSCOPIC_ANCESTRY_BOUNDARY_CERTIFICATE`**.

Required determination: whether any materially relevant generalized graph-completion GFT escapes the explicit LQG/spin-foam reduction map, while keeping TGFT collective/RG sectors separate unless their own fixed-realization physical map is supplied.

## Other parked fronts retained

- LQG: EPRL/KKL UV→IR crossover with topology escape and gamma ancestry.
- CDT/EDT: 4D line of constant physics, `a -> 0` observable transport, comparator/error certificate and EDT disposition.
- Causal sets: fundamental quantum gravitational measure → manifoldlike `3+1` continuum → normalized gravity observable/comparator.
- Hořava: material branches parked pending new same-realization UV→IR authority.
- AS: same-realization `A_s+A_t+A_u+A4` plus full crossing/error comparator certificate.

## Heavy compute

**IDLE.** Current missing information is equivalence/provenance/continuum matching, not a prospectively frozen numerical discriminator.

## Exact next order

1. validate the Iter206 exact head through methodology CI;
2. preserve all frozen counts and D7=`NOT_CLOSED` unless D2/D4 actually close;
3. exhaust generalized graph-completion GFT reduction scope;
4. keep unmapped sectors BLOCKED rather than FAIL;
5. run executable D7 evaluator through the validated methodology chain after this substantive classification update.

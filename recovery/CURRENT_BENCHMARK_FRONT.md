# KMQGB Current Benchmark Front

**Updated:** 2026-09-10  
**KMQGB iteration:** **205**  
**Phase:** **RQIR Core v1.0 FROZEN / gravity-ancestry TGFT relational observable + mean-field continuum evidence scoped PASS / same-realization full RG transport BLOCKED / GFT-tensor parent nonterminal**.

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
- No family-level scientific-readiness promotion in Iter205.

## Validation baseline

Iter204 scientific head `6314fecb5c1f97212deb15094505d8022301dbbe` failed methodology CI only at JSON validation because `recovery/state.json` contained trailing extra data. The state file was canonicalized in commit `707958a2d863bfe0249475ac3e4749a3e8491996` without changing science. Iter205 then proceeded only after identifying that infrastructure defect; no duplicate heavy or queued scientific computation was launched.

## Paper-IV global gates

D1 PASS; D2A NOT_CLOSED; D2B NOT_CLOSED; D2 `NOT_CLOSED_COVERAGE_AND_OBJECTS`; D3 PARTIAL; D4 `PARTIAL_ACTIVE_SET_MATRIX__GLOBAL_COVERAGE_NOT_CLOSED`; D5 PASS; D6 `PASS_RULE_TARGETS_OPEN`; D7 NOT_CLOSED; global decision **`NOT_YET_AUTHORIZED`**.

## Iter205 — gravity-ancestry TGFT RG-to-relational audit

### Positive scoped evidence

Lorentzian Barrett-Crane GFT coupled to a scalar reference field has an explicit relational condensate cosmology with generalized Friedmann dynamics. Realistic Lorentzian quantum-geometric TGFT models also admit a self-consistent mean-field condensate phase under published Landau-Ginzburg/Ginzburg-criterion analyses, including the causally complete Lorentzian Barrett-Crane extension.

Scoped structural dispositions:

`PASS_STRUCTURAL_GATE__LORENTZIAN_BC_GFT_RELATIONAL_CONDENSATE_COSMOLOGY_OBJECT_EXISTS`

`PASS_STRUCTURAL_GATE__REALISTIC_LORENTZIAN_TGFT_MEAN_FIELD_CONDENSATE_PHASE_IS_SELF_CONSISTENT_IN_DECLARED_LANDAU_GINZBURG_DOMAIN`

Neither is a family-level PASS.

### Missing same-realization RG transport

The realistic Lorentzian TGFT literature still treats a full RG-flow analysis as an open/future task. Existing FRG flows for simpler Abelian/tensorial models cannot be spliced into the Barrett-Crane cosmological realization under the frozen same-realization rule.

Disposition:

`BLOCKED_MISSING_REQUIRED_OBJECT__TGFT_GRAVITY_ANCESTRY_FULL_RG_TRAJECTORY_TO_RELATIONAL_GRAVITY_OBSERVABLE_SAME_REALIZATION_MAP`

Missing chain:

`microscopic gravity TGFT -> controlled RG/critical trajectory -> condensate couplings -> normalized relational gravity observable -> common-domain GR/EFT comparator`,

with one parameter ancestry and propagated RG/mean-field/truncation remainder.

`GFT_TENSOR_MODELS` remains `PARTIAL_SUBFAMILY_ONLY`; family residual remains undefined.

## Authorities

- `paper_iv/O_TGFT_GRAVITY_ANCESTRY_RG_TO_RELATIONAL_OBSERVABLE_AUDIT_2026-09-10.md`
- `paper_iv/PAPER_IV_COMPARATOR_RESIDUAL_MATRIX_DELTA_205.json`
- `paper_iv/PAPER_IV_DECISION_LEDGER_DELTA_205.json`
- `recovery/RECOVERY_DELTA_205.md`

Primary literature tracked in the audit includes DOI `10.1088/1475-7516/2022/01/050`, DOI `10.1103/PhysRevLett.130.141501`, DOI `10.1007/JHEP02(2023)074`, and DOI `10.1103/PhysRevD.111.026014`.

## Retained Iter204 result

The standard melonic/tree-dominated pure-random-tensor large-N sector retains its scoped terminal FAIL to the extended 4D GR-like continuum target. Enhanced/nonmelonic tensors remain BLOCKED and that child FAIL is not promoted to the parent.

## Immediate next scientific gate

**`GFT_SPINFOAM_GENERATING_BRANCH_INDEPENDENCE_OR_REDUCTION_PLUS_CONTINUUM_OBSERVABLE_CERTIFICATE`**.

Required determination: whether a gravity/spinfoam-generating GFT is a genuinely independent physical Tier-1 alternative in the benchmark domain or a second-quantized completion/reorganization of a named spin-foam realization, with explicit fixed-realization reduction/equivalence map where applicable. Any residual or terminal disposition still requires a continuum observable and common-domain comparator; formal amplitude ancestry alone is insufficient.

## Other parked fronts retained

- LQG: EPRL/KKL UV→IR crossover with topology escape and gamma ancestry.
- CDT/EDT: 4D line of constant physics, `a -> 0` observable transport, comparator/error certificate and EDT disposition.
- Causal sets: fundamental quantum gravitational measure → manifoldlike `3+1` continuum → normalized gravity observable/comparator.
- Hořava: material branches parked pending new same-realization UV→IR authority.
- AS: same-realization `A_s+A_t+A_u+A4` plus full crossing/error comparator certificate.

## Heavy compute

**IDLE.** The current blocker is structural/provenance/matching-limited. A simplified-TGFT FRG scan would not establish the missing same-realization gravity map.

## Exact next order

1. validate the repaired Iter204/Iter205 exact head through methodology CI;
2. preserve all frozen counts and D7=`NOT_CLOSED` unless D2/D4 actually close;
3. audit fixed-realization GFT→spin-foam amplitude maps and whether they establish reduction/equivalence or only ancestry;
4. keep any unresolved scope as BLOCKED rather than FAIL;
5. run executable D7 evaluator after the next substantive classification update.

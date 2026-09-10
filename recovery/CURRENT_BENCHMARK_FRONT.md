# KMQGB Current Benchmark Front

**Updated:** 2026-09-10  
**KMQGB iteration:** **192**  
**Phase:** **RQIR Core v1.0 FROZEN / projectable Hořava UV→IR same-realization gap frozen / non-projectable BPS branch next**.

## Stable metrics

- R1 repository readiness: **100%**.
- R2 methodology/material readiness: **100%**.
- Candidate Gravity R3: **24%**, inactive.
- Candidate activation condition: D7=`NEW_REQUIRED` only.
- AS/LQG/CFS Closure Wave 02: **0/3 terminal**.
- No readiness promotion in Iter192.

## Paper-IV global gates

- D1: PASS.
- D2A: NOT_CLOSED.
- D2B: NOT_CLOSED.
- D2: `NOT_CLOSED_COVERAGE_AND_OBJECTS`.
- D3: PARTIAL.
- D4: `PARTIAL_ACTIVE_SET_MATRIX__GLOBAL_COVERAGE_NOT_CLOSED`.
- D5: PASS.
- D6: `PASS_RULE_TARGETS_OPEN`.
- D7: NOT_CLOSED.
- Global decision: **`NOT_YET_AUTHORIZED`**.

## Coverage status

- Tier-1 required rows: **14**.
- terminal family-level rows: **1/14**.
- nonterminal family rows: **13/14**.
- untouched Tier-1 rows: **0/14**.
- Tier-2 unresolved classifications: **0**.
- scoped child residual count: **9**.
- scoped scientific FAIL rows: **2**.

## Iter192 — projectable Hořava UV→IR same-realization gap

The admitted 3+1 projectable AF result remains scoped PASS: the primary RG analyses establish asymptotically-free trajectories for the **marginal Lifshitz couplings** and reach a region with `0 < lambda-1 << 1` / GR-like kinetic structure.

However, the available low-energy FRG crossover literature is a separate truncation and does not provide an authenticated composition from the same AF realization through the relevant lower-derivative operators into a normalized extra-scalar observable with propagated matching/truncation error.

Therefore the projectable H1 subgate is frozen as:

**`BLOCKED_MISSING_REQUIRED_OBJECT__HORAVA_PROJECTABLE_AF_MARGINAL_TRAJECTORY_TO_RELEVANT_IR_COUPLINGS_AND_NORMALIZED_EXTRA_SCALAR_SAME_REALIZATION_MAP`**.

This is not a scientific FAIL and does not define a family-level residual.

Authority: `paper_iv/O_HORAVA_PROJECTABLE_UV_IR_SAME_REALIZATION_GAP_AUDIT_2026-09-10.md`.

Required future certificate fields:
`{microscopic_action, UV_fixed_point, marginal_trajectory, relevant_operator_basis, crossover_matching_scale, UV_to_IR_basis_map, scalar_mode_normalization, stability_and_strong_coupling_domain, loop_order, truncation_error, matching_remainder, normalized_observable, GR_EFT_comparator}`.

## Hořava parent status

`HORAVA_LIFSHITZ = PARTIAL_SUBFAMILY_ONLY`.

Projectable branch: scoped AF trajectory PASS + UV→IR matching BLOCKED missing required object.

Non-projectable/BPS branch exact next gate:

**`HORAVA_NONPROJECTABLE_BPS_UV_TO_IR_TRAJECTORY_PLUS_SCALAR_TENSOR_COMPARATOR_CERTIFICATE`**.

The 2025 non-projectable path-integral/one-loop work establishes concrete quantum progress but only in 2+1 dimensions and explicitly leaves further questions toward perturbative renormalizability; it is not yet a 3+1 UV→IR terminal certificate.

## Validation / CI

Iter191 methodology run `34435560170` failed at the generic JSON parse step before science validators. A diagnostic-only CI patch now reports the malformed JSON path explicitly on failure; no RQIR criterion or science gate was changed. Latest-head CI must be consumed before Iter192 is called repository-validated.

## D7 after Iter192

No family-level row became terminal:

- D2 = NOT_CLOSED;
- D4 = NOT_CLOSED;
- D7 = NOT_CLOSED;
- global decision = **`NOT_YET_AUTHORIZED`**;
- `NEW_REQUIRED=false`;
- Candidate Gravity activation=false, R3=24%.

## Heavy compute

**IDLE.** Projectable blocker is a missing same-realization crossover/matching object. Free numerical scans cannot manufacture it.

## Exact next order

1. Consume the latest diagnostic methodology CI and repair only the exact malformed JSON/synchronization defect if present.
2. Audit non-projectable/BPS 3+1 quantum/RG status and require one same-realization UV→IR trajectory plus normalized scalar-tensor observable and GR/EFT comparator.
3. If no such object exists, freeze that branch as `BLOCKED_MISSING_REQUIRED_OBJECT`; do not infer FAIL.
4. Only after both material Hořava branches have terminal dispositions may a family-level disposition be considered.
5. Rerun D7 only after a family-level terminal change or material decision-ledger change.

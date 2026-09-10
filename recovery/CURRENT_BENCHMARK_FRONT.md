# KMQGB Current Benchmark Front

**Updated:** 2026-09-10  
**KMQGB iteration:** **186**  
**Phase:** **RQIR Core v1.0 FROZEN / Paper-IV PF2 all-Tier1 first pass complete / family closure + Tier2 resolution active**.

## Stable metrics

- R1 repository readiness: **100%**.
- R2 methodology/material readiness: **100%**.
- Candidate Gravity R3: **24%**, inactive.
- Candidate activation condition: D7=`NEW_REQUIRED` only.
- AS/LQG/CFS Closure Wave 02: **0/3 terminal**.

No readiness promotion in Iter186.

## Paper-IV global gates

- D1: PASS.
- D2A framework-set coverage: NOT_CLOSED.
- D2B complete same-realization objects: NOT_CLOSED.
- D2: `NOT_CLOSED_COVERAGE_AND_OBJECTS`.
- D3: PARTIAL.
- D4: `PARTIAL_ACTIVE_SET_MATRIX__GLOBAL_COVERAGE_NOT_CLOSED`.
- D5: PASS.
- D6: `PASS_RULE_TARGETS_OPEN`.
- D7: NOT_CLOSED.
- Global decision: **`NOT_YET_AUTHORIZED`**.

## Major coverage result

Tier-1 required families: **11**.

- Terminal family-level coverage: **1/11** (GR/EFT baseline).
- Nonterminal family rows: **10/11**.
- `NOT_YET_BENCHMARKED`: **0/11** (was 5/11 before Iter186).
- Tier-2 unresolved classifications: **5**.

Every Tier-1 family now has a concrete audit. This is not the same as terminal family closure.

New first-pass authority:

`paper_iv/PF2_OMITTED_TIER1_FIRST_PASS_AUDIT_2026-09-10.md`

### Newly audited Tier-1 families

- higher-derivative/fakeon QG — `PARTIAL_SUBFAMILY_ONLY`;
- Hořava-Lifshitz — `PARTIAL_SUBFAMILY_ONLY`;
- causal sets — `PARTIAL_SUBFAMILY_ONLY`;
- CDT/EDT — `PARTIAL_SUBFAMILY_ONLY`;
- GFT/tensor models — `PARTIAL_SUBFAMILY_ONLY`.

## Nonlocal PF2-01B3 closure

For analytic `F(Box)=sum f_n Box^n`, every fixed finite derivative truncation is a local higher-derivative operator expansion. With the complete same-order local EFT comparator, its fixed-order amplitude deformation is comparator-contained:

`r_N in Col(J_EFT,N)`

and

`Pi_perp,N r_N = 0`.

Status:

**`PASS_RQIR_GATE__FIXED_ORDER_LOCAL_EFT_COMPARATOR_ABSORPTION`**.

This is a negative uniqueness control, not a theory FAIL. Nonlocal uniqueness must instead be sought in a finite-parameter cross-order coefficient law or full non-polynomial momentum shape.

Authority:

`paper_iv/O_NONLOCAL_RIEMANN_WEYL_EFT_QUOTIENT_2026-09-10.md`.

Next nonlocal gate:

**`NONLOCAL_CROSS_ORDER_FUNCTIONAL_RIGIDITY_OR_FULL_MOMENTUM_SHAPE_CERTIFICATE`**.

## Exact family-level blockers

- AS: same-realization `A_s+A_t+A_u+A4` + error/comparator certificate.
- LQG: EPRL/Regge -> Area-Regge/area-metric coupling and Immirzi ancestry.
- CFS: first normalized non-Einstein correction tensor + comparator.
- Nonlocal QG: cross-order/full-shape rigidity + material-branch exhaustion.
- String/M/holography: family/subfamily coverage/equivalence certificate.
- Higher derivative: pole-prescription family map + causality/observable comparator.
- Hořava: projectable UV->IR/extra-mode observable + non-projectable disposition.
- Causal sets: fundamental dynamics -> emergent continuum + normalized observable.
- CDT/EDT: continuum trajectory + invariant observable/error/comparator.
- GFT/tensor: spinfoam independence/reduction + full gravity observable comparator.

## Heavy compute

**IDLE.** The remaining obstacles are primarily missing physical certificates, continuum/ancestry maps and family-level comparator quotients.

## Next order

1. Resolve Tier-2 watchlist classifications by explicit promotion, reduction/merge or scope proof.
2. Convert as many Tier-1 partial rows as current literature permits into terminal coverage dispositions; do not manufacture missing physics.
3. Re-run D2/D4/D7 after each closure.
4. If all scientifically necessary objects close, let D7 choose among EXISTING/ADAPT/HYBRID/NEW.
5. If irreducible published-object gaps remain, D7 must return `NOT_YET_AUTHORIZED` and identify them exactly.

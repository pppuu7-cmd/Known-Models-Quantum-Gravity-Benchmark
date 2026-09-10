# KMQGB Current Benchmark Front

**Updated:** 2026-09-10  
**KMQGB iteration:** **187**  
**Phase:** **RQIR Core v1.0 FROZEN / D7 blocker-reduction wave / higher-derivative pole-prescription map active**.

## Stable metrics

- R1 repository readiness: **100%**.
- R2 methodology/material readiness: **100%**.
- Candidate Gravity R3: **24%**, inactive.
- Candidate activation condition: D7=`NEW_REQUIRED` only.
- AS/LQG/CFS Closure Wave 02: **0/3 terminal**.

No readiness promotion in Iter187.

## Paper-IV global gates

- D1: PASS.
- D2A framework-set/family coverage: NOT_CLOSED.
- D2B complete same-realization objects: NOT_CLOSED.
- D2: `NOT_CLOSED_COVERAGE_AND_OBJECTS`.
- D3: PARTIAL.
- D4: `PARTIAL_ACTIVE_SET_MATRIX__GLOBAL_COVERAGE_NOT_CLOSED`.
- D5: PASS.
- D6: `PASS_RULE_TARGETS_OPEN`.
- D7: NOT_CLOSED.
- Global decision: **`NOT_YET_AUTHORIZED`**.

## Coverage status

The census contains **14 Tier-1 rows**. Every row has been audited; none remains merely `NOT_YET_BENCHMARKED`.

- terminal family-level rows: **1/14** (GR/EFT baseline);
- nonterminal family rows: **13/14**;
- untouched Tier-1 rows: **0/14**;
- Tier-2 unresolved classifications: **0**.

No scoped child result is promoted to family exclusion/sufficiency.

## Iter187 — higher-derivative pole-prescription map

Authority:

- `paper_iv/O_HIGHER_DERIVATIVE_POLE_PRESCRIPTION_MAP_2026-09-10.md`
- `post_freeze_paper_iv_wave_02/PF2_05_HIGHER_DERIVATIVE/result_stelle_standard.json`
- `post_freeze_paper_iv_wave_02/PF2_05_HIGHER_DERIVATIVE/result_fakeon_control.json`

The former higher-derivative blocker contained an unresolved `pole_prescription_map`. Iter187 resolves its first material split:

1. **ordinary Feynman/Stelle spin-2 pole** — scoped scientific FAIL at positive-metric perturbative unitarity;
2. **fakeon/purely-virtual prescription** — scoped renormalizability + perturbative-unitarity control, but ordinary microcausality is not a PASS and the published construction predicts microscopic causality violation above the fakeon scale;
3. **other Lee-Wick/contour prescriptions** — remain materially distinct and require their own realization map;
4. **scalar-only/degenerate higher-curvature sectors** — do not inherit the generic four-derivative spin-2 UV claim automatically and must be reduced to EFT/scalar-tensor scope or separately benchmarked.

Parent family remains `PARTIAL_SUBFAMILY_ONLY`.

Narrowed blocker:

`HIGHER_DERIVATIVE_REMAINING_PRESCRIPTIONS_PLUS_FAKEON_SAME_REALIZATION_CAUSALITY_OBSERVABLE_COMPARATOR_CERTIFICATE`.

This adds one genuine scoped scientific FAIL without changing the family-level terminal count.

## D4 evidence

Required family rows with complete defined residual remain **1/14**.

Previously frozen scoped child results remain valid. Iter187 adds a defined scoped pathology result for the standard Stelle/Feynman spin-2 branch and a nonterminal fakeon control. Neither counts as family-level exclusion or `NEW_REQUIRED` evidence.

## Thirteen family-level blockers

1. higher derivative — remaining pole prescriptions + fakeon same-realization causality/observable comparator;
2. Hořava — projectable UV->IR/extra-mode observable + non-projectable disposition;
3. AS — same-realization `A_s+A_t+A_u+A4` + error/comparator;
4. nonlocal — cross-order/full-shape rigidity + branch exhaustion;
5. string/M/holography — material-subfamily/family equivalence coverage;
6. causal sets — fundamental dynamics -> manifold continuum + normalized observable;
7. CDT/EDT — continuum trajectory + invariant observable/error/comparator;
8. LQG — EPRL->Area-Regge/area-metric coupling and Immirzi ancestry;
9. GFT/tensor — spinfoam reduction/independence + full gravity observable;
10. CFS — first normalized non-Einstein correction tensor;
11. noncommutative spectral geometry — quantum spectral dynamics + normalized QG observable;
12. canonical WDW — physical Hilbert space/clock/Dirac observable + semiclassical comparator;
13. Quantum Graphity — continuum Lorentzian spin-2/GR emergence + normalized observable.

## Heavy compute

**IDLE.** Current active higher-derivative blocker is analytic/provenance/same-realization causality and prescription classification; heavy computation cannot yet change the terminal family classification.

## Next operation

Complete the higher-derivative material-prescription disposition by freezing a same-realization fakeon causality/observable/comparator certificate and explicitly resolving whether remaining Lee-Wick/alternative pole prescriptions are independent viable parents or reducible/failed branches. Then rerun D7. If this family remains nonterminal, move to the next highest-leverage blocker rather than weakening RQIR.

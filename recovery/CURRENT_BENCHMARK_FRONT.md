# KMQGB Current Benchmark Front

**Updated:** 2026-09-10  
**KMQGB iteration:** **199**  
**Phase:** **RQIR Core v1.0 FROZEN / Hořava parked / EPRL-KKL UV fixed point integrated / continuum-topology escape obligation frozen / UV→IR ancestry blocked**.

## Stable metrics

- R1 repository readiness: **100%**.
- R2 methodology/material readiness: **100%**.
- Candidate Gravity R3: **24%**, inactive.
- Candidate activation condition: D7=`NEW_REQUIRED` only.
- AS/LQG/CFS Closure Wave 02: **0/3 terminal**.
- No scientific-readiness promotion in Iter199.

## Validation baseline

Canonical Iter198 main head `2c99ab1ea1d1eb1c962eed6d0a78fc017fe8ceee` passed exact-head methodology-ci run `34464218594` and reproducibility-release run `34464270486`, both `success`.

Iter199 is being prepared on `research/lqg-continuum-topology-iter199` and is not canonical until its exact head passes CI and the integration is completed.

## Paper-IV global gates

D1 PASS; D2A NOT_CLOSED; D2B NOT_CLOSED; D2 `NOT_CLOSED_COVERAGE_AND_OBJECTS`; D3 PARTIAL; D4 `PARTIAL_ACTIVE_SET_MATRIX__GLOBAL_COVERAGE_NOT_CLOSED`; D5 PASS; D6 `PASS_RULE_TARGETS_OPEN`; D7 NOT_CLOSED; global decision **`NOT_YET_AUTHORIZED`**.

## Coverage status

Tier-1 required rows **14**; terminal family rows **1/14**; nonterminal **13/14**; Tier-2 unresolved **0**. Defined scoped child residual rows remain **9**. Scoped structural results do not count as family exclusion or sufficiency.

## Iter198 retained result — EPRL/KKL UV fixed point

Han, *Ultraviolet fixed point in covariant loop quantum gravity*, Phys. Rev. D 114, 044040 (2026), supplies a concrete Lorentzian EPRL/KKL complete-amplitude stack construction with a candidate small-spin UV fixed point. At leading order the object becomes topological, triangulation ambiguity reduces to finite boundary coefficients, and the expansion carries `O(A^-1)` control.

Scoped status:

`PASS_STRUCTURAL_GATE__LQG_EPRL_KKL_COMPLETE_AMPLITUDE_HAS_CANDIDATE_UV_FIXED_POINT_WITH_FINITE_BOUNDARY_DATA_AND_EXPLICIT_LEADING_REMAINDER`.

O-LQG remains `BLOCKED_MISSING_REQUIRED_OBJECT` because the same realization is not yet transported through relevant deformation into a large-spin semiclassical Regge/Area-Regge regime with gamma ancestry and a normalized comparator.

## Iter199 — continuum-topology escape constraint

Bruno, Colafranceschi, Mele and Rovelli, *Structure of the continuum limit of spin foams*, Phys. Rev. D 114, 066005 (published 8 September 2026), prove in a model-independent ordered-triangulation framework that sufficiently strong convergence assumptions force a topological continuum theory. They also develop a weaker distributional continuum construction in which the cylinder amplitude defines a rigging map on physical states.

This theorem is **not automatically applied** to Han's concrete stack amplitude. Instead Iter199 freezes a conditional same-realization obligation:

`PASS_STRUCTURAL_GATE__LQG_UV_TO_IR_BRIDGE_REQUIRES_EXPLICIT_TOPOLOGICAL_CONTINUUM_ESCAPE_MECHANISM`.

If a proposed EPRL/KKL UV→IR flow satisfies the strong-convergence hypotheses of the theorem, strong convergence alone cannot produce the required non-topological GR-like propagating sector. An admissible bridge must therefore prospectively provide either:

1. `DISTRIBUTIONAL_RIGGING_MAP_CONTINUUM_WITH_FIXED_EPRL_KKL_REALIZATION`, together with relevant deformation(s); or
2. `EXPLICIT_STRONG_CONVERGENCE_ASSUMPTION_ESCAPE_WITH_REPLACEMENT_CONTROL`, stating which theorem hypothesis fails for the concrete stack and what controlled convergence notion replaces it.

Authority:

- `paper_iv/O_LQG_CONTINUUM_TOPOLOGY_ESCAPE_GATE_2026-09-10.md`
- `paper_iv/PAPER_IV_DECISION_LEDGER_DELTA_199.json`

## Refined O-LQG chain

`EPRL/KKL gamma_micro`
→ `topological UV fixed-point boundary data`
→ `{relevant deformation + continuum-topology escape}`
→ `large-spin semiclassical Regge/Area-Regge gamma ancestry`
→ `area-metric physical observable comparator`.

The Barbero–Immirzi parameter must be transported by an explicit same-realization map. Name matching of `gamma` across microscopic EPRL, Regge/Area-Regge and area-metric descriptions remains forbidden.

## Exact next gate

**`EPRL_KKL_UV_FIXED_POINT_TO_SEMICLASSICAL_AREA_REGGE_CROSSOVER_WITH_TOPOLOGY_ESCAPE_GAMMA_ANCESTRY_AND_ERROR_CERTIFICATE`**.

Required payload:

- fixed Lorentzian EPRL/KKL stack/refinement realization;
- normalized UV boundary coefficients and inherited `O(A^-1)` error;
- relevant deformation(s);
- topology-escape mechanism satisfying one of the two declared alternatives;
- explicit small-spin UV → large-spin semiclassical crossover;
- Barbero–Immirzi normalization/transport;
- Regge → Area-Regge/area-metric coupling ancestry;
- normalized common-domain GR/EFT/QG comparator;
- propagated UV/refinement/crossover/truncation error ledger.

## O-AS status

No repository-authoritative same-realization `A_s+A_t+A_u+A4` package with full crossing/error/comparator control has superseded the AS blocker. Cross-realization splicing remains forbidden.

## Heavy compute

**IDLE.** The missing LQG object is a flow/convergence/provenance map. Numerical scans before a frozen relevant-deformation equation or continuum construction would manufacture assumptions rather than test a defined physical object.

## Next order

1. CI-validate Iter199 and integrate only if exact-head checks remain green.
2. Search specifically for a concrete EPRL/KKL relevant-deformation or rigging-map/distributional continuum realization linking the Han UV stack to the large-spin semiclassical regime.
3. If absent, record the literature ceiling and park this LQG branch rather than repeatedly searching the same missing object.
4. Move to the next analytically closable Tier-1 blocker while the hourly auto-research continues independently.

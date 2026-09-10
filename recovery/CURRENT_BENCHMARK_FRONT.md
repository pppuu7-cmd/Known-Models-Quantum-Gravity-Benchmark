# KMQGB Current Benchmark Front

**Updated:** 2026-09-10  
**KMQGB iteration:** **198**  
**Phase:** **RQIR Core v1.0 FROZEN / Hořava parked / concrete EPRL-KKL UV fixed-point object integrated / O-LQG UV→IR ancestry gate narrowed**.

## Stable metrics

- R1 repository readiness: **100%**.
- R2 methodology/material readiness: **100%**.
- Candidate Gravity R3: **24%**, inactive.
- Candidate activation condition: D7=`NEW_REQUIRED` only.
- AS/LQG/CFS Closure Wave 02: **0/3 terminal**.
- No scientific-readiness promotion in Iter198.

## Validation carried forward

Iter197 authoritative head `7e608ff955a386e536bc92034dded1fe19c4986e` is validated. The first Iter198 scientific audit commit `8e3218b98e879faf031a5ea23d47ca915ab711c4` is also validated: methodology-ci run `34463728735` and reproducibility-release run `34463798628` both completed `success`. Later synchronization commits require exact-head validation before Iter198 is declared fully canonical.

## Paper-IV global gates

D1 PASS; D2A NOT_CLOSED; D2B NOT_CLOSED; D2 `NOT_CLOSED_COVERAGE_AND_OBJECTS`; D3 PARTIAL; D4 `PARTIAL_ACTIVE_SET_MATRIX__GLOBAL_COVERAGE_NOT_CLOSED`; D5 PASS; D6 `PASS_RULE_TARGETS_OPEN`; D7 NOT_CLOSED; global decision **`NOT_YET_AUTHORIZED`**.

## Coverage status

Tier-1 required rows **14**; terminal family rows **1/14**; nonterminal **13/14**; Tier-2 unresolved **0**. Scoped child PASS/FAIL remains scoped.

## Iter198 — concrete EPRL/KKL UV fixed-point authority

Han, *Ultraviolet Fixed Point in Covariant Loop Quantum Gravity*, arXiv:2602.18665v1 (21 February 2026), supplies a concrete Lorentzian EPRL/KKL stack-amplitude construction with a candidate UV fixed point for the complete covariant-LQG amplitude after the sum/refinement over 2-complexes. The leading UV result compresses microscopic ambiguity into finite boundary-block coefficients and carries an explicit `O(A^-1)` asymptotic remainder.

Scoped structural result:

`PASS_STRUCTURAL_GATE__LQG_EPRL_KKL_COMPLETE_AMPLITUDE_HAS_CANDIDATE_UV_FIXED_POINT_WITH_FINITE_BOUNDARY_DATA_AND_EXPLICIT_LEADING_REMAINDER`.

This materially narrows O-LQG: a concrete EPRL-family UV/continuum object with approximation control exists. It does **not** close the RQIR family object. The authority leaves the relevant-deformation/IR flow and physical observable connection open; the UV small-spin regime is not yet bound to the large-spin semiclassical Regge regime. Although microscopic Barbero–Immirzi `gamma` is present, no same-realization `gamma` transport into Regge/Area-Regge/area-metric parity-sensitive couplings is derived.

Therefore O-LQG remains `BLOCKED_MISSING_REQUIRED_OBJECT`; family residual remains undefined and is not zero-filled.

Required chain:

`EPRL/KKL microscopic gamma -> UV fixed-point boundary data -> relevant deformation / IR crossover -> semiclassical Regge/Area-Regge couplings -> area-metric observable comparator`.

Authority: `paper_iv/O_LQG_EPRL_KKL_UV_FIXED_POINT_SCOPE_AUDIT_2026-09-10.md`.
Comparator delta: `paper_iv/PAPER_IV_COMPARATOR_RESIDUAL_MATRIX_DELTA_198.json`.

## O-AS status

No same-realization `A_s+A_t+A_u+A4` plus full crossing/error package has become repository-authoritative during this iteration. O-AS remains `BLOCKED_MISSING_REQUIRED_OBJECT`; no cross-realization splice is permitted.

## Heavy compute

**IDLE.** The active blocker is a UV→IR matching/provenance object. A scan without a prospectively fixed EPRL/KKL flow equation would manufacture assumptions rather than close the frozen gate.

## Exact next gate

**`EPRL_KKL_UV_FIXED_POINT_TO_SEMICLASSICAL_AREA_REGGE_CROSSOVER_PLUS_GAMMA_ANCESTRY_AND_ERROR_CERTIFICATE`**.

Require one explicit EPRL/KKL realization connecting the UV fixed point to an IR/semiclassical regime; a relevant-deformation/RG map from the UV boundary data; explicit Barbero–Immirzi normalization/transport; Regge→Area-Regge/area-metric coupling ancestry; a normalized common-domain comparator; and propagated `O(A^-1)` plus crossover/refinement/truncation remainder. If absent, preserve BLOCKED and move to the next analytically closable Tier-1 family.

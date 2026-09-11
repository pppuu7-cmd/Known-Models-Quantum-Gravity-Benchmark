# Current Benchmark Front
Updated: 2026-09-11
Iteration: Iter281 LQG spinfoam-stack explicit Hessian/refinement audit
Authoritative operational-saturation milestone: Iter270
Authoritative D7 infrastructure milestone: Iter272
Authoritative 15-row census synchronization milestone: Iter276

## Global lock
- RQIR Core v1.0 remains FROZEN.
- Tier-1 census = 15 families.
- Strict terminal coverage = 1/15.
- Strict nonterminal coverage = 14/15.
- Candidate-family terminal coverage = 0/14.
- Tier-2 unresolved = 0.
- D1 = PASS.
- D2 = NOT_CLOSED_COVERAGE_AND_OBJECTS.
- D3 = PARTIAL.
- D4 = PARTIAL_GLOBAL_NOT_CLOSED.
- D5 = PASS.
- D6 = PASS_RULE_TARGETS_OPEN.
- D7 = NOT_CLOSED / NOT_YET_AUTHORIZED.
- D7-S0 = PASS.
- D7-S1 = PASS.
- D7-S2 = NOT_CLOSED.
- D7-S3 = NOT_CLOSED.
- D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED.
- D7-S5 = NOT_AUTHORIZED.
- D7-S6 = INACTIVE.
- `NEW_REQUIRED`, `EXISTING_SUFFICIENT`, `ADAPT_EXISTING`, `HYBRID_REQUIRED` are not authorized.
- Candidate Gravity remains inactive at canonical R3 = 24%.

## Readiness metrics
- Operational polygon readiness = 100%.
- D7 protocol infrastructure readiness = 100%.
- 15-row decision-stack synchronization remains validated.
These are infrastructure/operational metrics, not scientific D7 closure.

## Recent material reopens
### Iter277 — RQCP multi-axis resource closure
RQCP remains a distinct nonterminal Tier-1 parent. Independent cutoff audit established a material Hilbert/domain axis: cutoff 8 -> 28 shifts `G` ~7.32%, gap ~3.07%, `G*gap^2` ~1.36%; high-cutoff 24 -> 28 is extremely stable. Methodological delta: `MULTI_AXIS_RESOURCE_CLOSURE`.

### Iter278 — Asymptotic Safety PIRG
Diffeomorphism-invariant/background-independent PIRG fixed-point evidence strengthened. Six published variants retain two positive relevant directions, but scheme/procedure dependence remains and the public contact-complete `s+t+u+A4` object is still missing.

### Iter279 — NSF classification
NSF was reduced to the existing GR parent rather than promoted as a new Tier-1 family. Tree-level normalization/t-u symmetry checks pass; fixed-angle growth is ~`s^1`; forward behavior remains pole-like. Census remains 15.

### Iter280 — Asymptotic Safety Lorentzian spectral function
Positive normalisable Lorentzian TT-graviton spectral evidence was cross-checked, but the source states those fluctuation states are not physical diffeomorphism-invariant Hilbert-space states, the full numerical curve was not independently reproduced from a public dataset, and the contact-complete scattering blocker remains active.

### Iter281 — LQG spinfoam-stack explicit audit
Primary object: Muxin Han, *Summation and triangulation independence of Lorentzian spinfoam amplitudes for all LQG*, Phys. Rev. D 113, 084034 (2026), DOI `10.1103/n76f-31gf`.

Parallel workflow `lqg-spinfoam-stack-hessian-audit`, run `34554825500`: 4/4 independent jobs + aggregate `SUCCESS`, with `fail-fast: false` and `max-parallel: 4`.
Methodology CI `34554825514`: `SUCCESS`.
Reproducibility release `34554911718`: `SUCCESS`.
Aggregate digest: `sha256:4ebddf182b7b5c469947acab11eabab7a2422b92d43ea1cf2c85d4b687cb82e1`.

Exact/numerical result:
- `det(M_6x6)=125`;
- strict negative definiteness and nondegeneracy;
- exact `M=-B^T B`;
- `rank(B)=6`, projected kernel `0`;
- 18x18 block rank `18`, exact determinant identity and nondegeneracy;
- final `C0,C1,C2` positive on beta = 0.25, 0.5, 1, 2;
- max relative 256->512 change on that grid = `0.0` in binary64.

Scoped result:
`PASS_SCOPED_EXPLICIT_TRIVIAL_TOPOLOGY_SPINFOAM_STACK_HESSIAN_NONDEGENERACY_INCIDENCE_FACTORIZATION_AND_COEFFICIENT_CONVERGENCE__TOPOLOGICAL_LARGE_CUTOFF_NOT_PHYSICAL_UV_IR_GR_CLOSURE`

Interpretation: the explicit localization/nondegeneracy and triangulation/refinement-control machinery is independently strengthened, but the infinite internal-area-cutoff regime is topological/scale-invariant and cannot be silently identified with the distinct finite-large-cutoff/small-Barbero-Immirzi semiclassical Regge/GR regime. Therefore the same-realization physical UV->IR/GR bridge remains open.

LQG/spinfoam remains `PARTIAL/BLOCKED`, not FAIL and not family-level PASS.

Current decisive LQG blocker:
`BLOCKED_MISSING_SAME_REALIZATION_PHYSICAL_UV_TO_IR_GR_TRAJECTORY_NORMALIZED_GRAVITY_OBSERVABLE_PARAMETER_IDENTITY_COMPARATOR_AND_PROPAGATED_ERROR_CERTIFICATE_FROM_COMPLETE_SPINFOAM_CONTINUUM_FIXED_POINT`

## Publication handoff
`recovery/PUBLICATION_IMPACT_LEDGER.md` is authoritative.
- Paper III: Iter277 `MULTI_AXIS_RESOURCE_CLOSURE` = `READY`.
- Paper III: Iter278–281 = `NOT_NEEDED` as additional rules; optional corroboration only.
- Paper IV: Iter277–281 = `READY` for inclusion with their stated scope boundaries.

## Current scientific decision state
- 15 Tier-1 families.
- 1/15 strict terminal in its declared low-energy benchmark domain (GR + controlled low-energy EFT baseline).
- 0/14 candidate-QG families strict terminal.
- Remaining rows are PARTIAL/BLOCKED/nonterminal; this is not refutation.
- D7-S2/S3/S4 remain open; no global new-theory/adaptation verdict is authorized.

## Current compute policy
Shard every scientifically independent calculation immediately with `fail-fast: false`; dependent scoring/classification begins only after an explicit aggregate barrier. Do not rerun saturated grids merely to occupy runners.

## Exact next gate
`D7_S2_EXTERNAL_AUTHORITY_DRIVEN_TERMINALIZATION_WITH_MULTI_AXIS_RESOURCE_CLOSURE_EXPLICIT_REDUCTION_MAPS_AND_PHYSICAL_CONTINUUM_CERTIFICATES`

Priority:
1. audit Bruno–Colafranceschi–Mele–Rovelli, Phys. Rev. D 114, 066005 (2026), to determine how the strong-convergence-to-topological no-go and distributional/rigging-map physical continuum affect the LQG closure certificate;
2. stable public contact-complete Asymptotic-Safety `s+t+u+A4` package;
3. LQG same-realization physical UV->IR/GR observable/transport package;
4. RQCP all-band/background-independent autonomy bridge with Hilbert-cutoff closure;
5. other Tier-1 families only on materially new primary authority;
6. any apparently new QG parent must first pass explicit reduction/equivalence audit before census promotion.

# LQG UV-to-IR same-realization bridge identity audit — Iter283

Date: 2026-09-11
Family: `LQG_SPINFOAM`
RQIR Core: `v1.0 FROZEN`

## Question
Do the strongest currently identified covariant-LQG endpoint results already form one explicit same-realization UV-to-IR/GR trajectory, or do they remain strong endpoints without a published transport certificate?

## Endpoint authorities
### Semiclassical/GR endpoint
Muxin Han, *Einstein Equation from Covariant Loop Quantum Gravity in Semiclassical Continuum Limit*, Phys. Rev. D 96, 024047 (2017), DOI `10.1103/PhysRevD.96.024047`, arXiv `1705.09030`.

The construction uses EPRL/FK covariant-LQG spinfoam amplitudes on refining triangulations. Its physical regime is large spin, with coupled refinement/semiclassical/regulator limits including `mu -> 0`, `lambda -> infinity`, `delta -> 0` and the hierarchy `lambda >> 1/delta >> 1`. Its target is the continuum Einstein equation.

### UV endpoint
Muxin Han, *Ultraviolet Fixed Point in Covariant Loop Quantum Gravity*, Phys. Rev. D 114, 044040 (2026), DOI `10.1103/d8s7-jqfl`, arXiv `2602.18665`.

The 2026 construction concerns the complete Lorentzian covariant-LQG amplitude summed over two-complexes/spinfoam-stack families and identifies a candidate UV fixed point associated with the small-spin regime. At leading fixed-point order the regime is topological.

### Stack/cutoff structure
Muxin Han, *Summation and triangulation independence of Lorentzian spinfoam amplitudes for all LQG*, Phys. Rev. D 113, 084034 (2026), DOI `10.1103/n76f-31gf`, arXiv `2510.26926`.

The internal-area-cutoff-to-infinity limit localizes on the topological SU(2) flat-connection sector in the declared scope.

## Parallel bridge audit
Workflow: `lqg-uv-ir-bridge-identity-audit`
Run: `34555702346`
Head: `38734d01a4f88fa45c341dd395e3bded15a07d4c`

Four independent guards ran concurrently (`fail-fast: false`, `max-parallel: 4`) followed by an aggregate dependency barrier:
1. broad-family versus explicit same-realization identity;
2. UV/IR limit orientation and spin-regime compatibility;
3. regulator/parameter transport (`lambda`, `delta`, `mu` versus stack/UV variables);
4. normalized-observable/GR-target transport.

Result: **4/4 independent guards SUCCESS + aggregate SUCCESS**.
Methodology CI run `34555702337`: `SUCCESS`.
Aggregate artifact digest: `sha256:32701d4931ddce73e1674025cda8e518195fc64b477e1a02d9227fda9913cbc5`.

## Aggregate result
- `shared_parent_family = true`;
- `material_positive_endpoints = true`;
- `same_realization_terminal_bridge_ready = false`.

Guard classifications:
- `PASS_SHARED_LQG_PARENT__SAME_REALIZATION_IDENTITY_NOT_EXPLICIT`;
- `PASS_ENDPOINTS_IN_DISTINCT_SPIN_REGIMES__EXPLICIT_UV_TO_IR_TRAJECTORY_MISSING`;
- `PASS_DISTINCT_REGULATOR_LIMITS_IDENTIFIED__PARAMETER_TRANSPORT_MAP_MISSING`;
- `PASS_MATERIAL_UV_AND_GR_ENDPOINTS_IDENTIFIED__NORMALIZED_OBSERVABLE_TRANSPORT_MISSING`.

Canonical aggregate classification:
`HIGH_VALUE_UV_AND_GR_ENDPOINTS_IN_SHARED_LQG_PARENT__NO_EXPLICIT_SAME_REALIZATION_PARAMETER_AND_OBSERVABLE_TRANSPORT_BRIDGE`

## Scientific interpretation
This is materially stronger than saying that LQG merely lacks both UV and GR endpoints. The benchmark now has strong evidence for both ends of the desired chain:
- a small-spin complete-amplitude UV fixed-point/topological endpoint;
- a large-spin/refinement semiclassical endpoint yielding the continuum Einstein equation.

What remains missing is the **middle transport certificate**. The located primary sources do not provide:
1. an explicit equality/reduction/identity map between the 2017 refining-triangulation amplitude and the 2026 stack-summed complete amplitude;
2. an explicit transport map between the 2017 `lambda/delta/mu` limits and the 2026 internal-area-cutoff/fixed-point variables;
3. a demonstrated trajectory connecting the small-spin UV regime to the large-spin semiclassical regime in one realization;
4. a normalized same-domain gravitational observable transported through that chain with comparator and propagated uncertainty.

Therefore two strong endpoints must not be silently concatenated into a same-realization UV-to-IR/GR trajectory.

## Family status
LQG/spinfoam remains nonterminal (`PARTIAL/BLOCKED`), not FAIL and not family-level PASS.

The existing blocker remains accurate but is now better localized:
`BLOCKED_MISSING_SAME_REALIZATION_PHYSICAL_UV_TO_IR_GR_TRAJECTORY_NORMALIZED_GRAVITY_OBSERVABLE_PARAMETER_IDENTITY_COMPARATOR_AND_PROPAGATED_ERROR_CERTIFICATE_FROM_COMPLETE_SPINFOAM_CONTINUUM_FIXED_POINT`

Interpretive refinement: the blocker is now best read as **missing bridge/transport**, not missing UV and GR endpoint evidence.

## Global consequence
- Tier-1 census remains `15`.
- strict terminal remains `1/15`.
- candidate-QG terminal remains `0/14`.
- D7 remains `NOT_CLOSED / NOT_YET_AUTHORIZED`.
- Candidate Gravity remains inactive at R3 `24%`.

## Publication handoff
- Paper III: `NOT_NEEDED`; no new general quantum-sensing/resource-closure rule.
- Paper IV: `READY`; explicitly present LQG as a two-endpoint/high-value-near-bridge case and state that the unresolved object is a same-realization identity/parameter/observable transport certificate.

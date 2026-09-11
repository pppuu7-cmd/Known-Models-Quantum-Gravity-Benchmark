# LQG canonical/covariant physical-state link compatibility audit — Iter284

Date: 2026-09-11
Family: `LQG_SPINFOAM`
RQIR Core: `v1.0 FROZEN`

## Primary object
Yang, Zhang, Ma, *Relating spin-foam to canonical loop quantum gravity by graphical calculus*, Physical Review D 104, 044025 (2021), DOI `10.1103/PhysRevD.104.044025`, arXiv `2102.05881`.

The source studies a generalized **Euclidean EPRL** spin-foam model. In the declared scope it relates the spin-foam amplitude to the canonical Euclidean Hamiltonian constraint, obtains a rigging-map interpretation, and finds weak constraint satisfaction on certain spin-network/physical states at Immirzi parameter `beta=1`.

## Parallel compatibility audit
Workflow: `lqg-physical-state-link-compatibility-audit`
Run: `34556068228`
Head: `db998ad568524c7b777e896c67ce5350f2c7c90d`

Four independent guards ran under `fail-fast: false` and were aggregated only after the dependency barrier:
1. physical-state / rigging-map content;
2. Euclidean-versus-Lorentzian signature scope;
3. `beta=1` and certain-state scope;
4. compatibility with the Iter283 Lorentzian UV-to-IR chain.

Result: **4/4 independent guards SUCCESS + aggregate SUCCESS**.
Methodology CI run `34556068266`: preflight + 4/4 methodology shards + aggregate/bundle `SUCCESS`.
Aggregate artifact digest: `sha256:61a71ea3aab1fa23b58ad2760b27500c84f34ac62aca5d020526516125cb7d47`.

## Aggregate classifications
- `PASS_SCOPED_EPRL_RIGGING_MAP_WITH_WEAK_CONSTRAINT_SATISFACTION_ON_CERTAIN_STATES`
- `PASS_EUCLIDEAN_PHYSICAL_STATE_LINK__LORENTZIAN_SAME_REALIZATION_MAP_MISSING`
- `PASS_SCOPED_BETA1_CERTAIN_STATES__NO_GENERIC_BETA_OR_FULL_STATE_SPACE_CERTIFICATE`
- `PASS_HIGH_VALUE_PHYSICAL_STATE_COMPONENT__NOT_YET_COMPATIBLE_SAME_REALIZATION_UV_IR_CHAIN`

Canonical aggregate classification:
`HIGH_VALUE_EUCLIDEAN_BETA1_RIGGING_MAP_COMPONENT__NO_EXPLICIT_COMPATIBLE_TRANSPORT_INTO_LORENTZIAN_UV_IR_CHAIN`

The aggregate explicitly records `physical_state_component = HIGH_VALUE_SCOPED_POSITIVE` and `same_realization_chain_ready = false`.

## Scientific interpretation
This result adds a genuine physical-state/canonical-covariant consistency component to the LQG evidence base. It materially weakens any claim that LQG has no relation at all between covariant amplitudes and canonical physical-state machinery.

It does **not** close the Iter283 bridge because the published object is scoped to:
- generalized Euclidean EPRL;
- Euclidean Hamiltonian constraint;
- `beta=1`;
- certain states rather than a full state-space certificate;
- weak constraint satisfaction.

No explicit source-level map was located that transports this 2021 Euclidean `beta=1` rigging-map result into the Lorentzian 2017/2026 same-realization chain, including state/signature/parameter identity and a normalized gravity observable transported from the UV endpoint to the semiclassical GR endpoint.

Therefore the current LQG picture is now best described as three strong but not yet fully stitched components:
1. scoped canonical/covariant physical-state link;
2. large-spin/refinement Einstein-equation endpoint;
3. small-spin Lorentzian complete-amplitude UV fixed-point endpoint.

The missing object is still the compatible same-realization transport among them.

## Family status
LQG/spinfoam remains `PARTIAL/BLOCKED`, not FAIL and not family-level PASS.

Canonical blocker remains:
`BLOCKED_MISSING_SAME_REALIZATION_PHYSICAL_UV_TO_IR_GR_TRAJECTORY_NORMALIZED_GRAVITY_OBSERVABLE_PARAMETER_IDENTITY_COMPARATOR_AND_PROPAGATED_ERROR_CERTIFICATE_FROM_COMPLETE_SPINFOAM_CONTINUUM_FIXED_POINT`

Interpretive refinement: physical-state evidence exists, but it is scoped and not yet transported into the Lorentzian UV-to-IR chain.

## Global consequence
- Tier-1 census remains `15`.
- strict terminal remains `1/15`.
- candidate-QG terminal remains `0/14`.
- D7 remains `NOT_CLOSED / NOT_YET_AUTHORIZED`.
- Candidate Gravity remains inactive at R3 `24%`.

## Publication handoff
- Paper III: `NOT_NEEDED`; no new general quantum-sensing/resource-closure failure mode.
- Paper IV: `READY`; add the 2021 scoped rigging-map/canonical-covariant result as a positive physical-state component, while explicitly preserving its Euclidean, `beta=1`, certain-state, weak-constraint scope and the missing Lorentzian transport into the Iter283 chain.

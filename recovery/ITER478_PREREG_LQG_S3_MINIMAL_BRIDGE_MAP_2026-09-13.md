# Iter478 preregistration — LQG/EPRL D7-S3 minimal bridge map

Date: 2026-09-13
Status: FROZEN BEFORE IMPLEMENTATION
Parent: main through Iter473–476 recovery.

## Question
Given the already source-audited positive LQG/EPRL endpoint/components, what named bridge classes are still explicitly open before those pieces can legally form one D7-S3 same-realization object/parameter/observable/error bundle?

## Frozen authorities
Only these existing repository audits are authoritative inputs:
1. `paper_iv/P_LQG_UV_IR_BRIDGE_IDENTITY_AUDIT_ITER283_2026-09-11.md`
2. `paper_iv/P_LQG_PHYSICAL_STATE_LINK_COMPATIBILITY_AUDIT_ITER284_2026-09-11.md`
3. `paper_iv/P_LQG_EPRL_WICK_SIGNATURE_BRIDGE_AUDIT_ITER286_2026-09-11.md`
4. `paper_iv/P_LQG_SAME_STACK_UV_ENTROPY_ALIGNMENT_AUDIT_ITER287_2026-09-11.md`
5. `paper_iv/LQG_GAMMA_DUALITY_OBSERVABLE_PARAMETER_BRIDGE_AUDIT_ITER291_2026-09-11.md`
6. `paper_iv/P_LQG_TOLLER_HALF_LINK_COMPOSITION_SCOPE_AUDIT_ITER302_2026-09-11.md`

## Frozen bridge classes and required explicit markers
A. `UV_IR_SAME_REALIZATION_IDENTITY_AND_PARAMETER_MAP`
- `same_realization_terminal_bridge_ready=false` and/or explicit missing parameter/observable transport in Iter283.

B. `PHYSICAL_STATE_SIGNATURE_STACK_TRANSPORT`
- `same_realization_chain_ready=false` in Iter284;
- `same_real_gamma_identity=false`, `rigging_map_transport_ready=false`, `complete_stack_transport_ready=false`, `same_realization_chain_ready=false` in Iter286.

C. `CONTINUOUS_SHARED_STACK_UV_TO_GR_TRANSPORT`
- `continuous_same_realization_transport_ready=false` in Iter287.

D. `NORMALIZED_OBSERVABLE_AND_PROPAGATED_ERROR_TRANSPORT`
- `normalized_observable_with_full_propagated_qg_error_ready=false` and/or complete-stack observable transport still open in Iter291.

E. `CAUSAL_TOLLER_GLUE_FINITE_NORMALIZED_STACK_TO_REGGE_GR`
- `fixed_toller_branch_representation_composition_available=false`;
- `causal_stack_finiteness_normalization_cutoff_control_proven=false`;
- `same_realization_uv_to_regge_gr_transport_proven=false` in Iter302.

## Frozen rule
For each class, emit `OPEN_EXPLICIT_SOURCE_BLOCKER` if at least one frozen negative marker is recovered from its designated authority, and `NO_EXPLICIT_BLOCKER_RECOVERED` otherwise. Positive anchors may be recorded but cannot override an explicit negative readiness marker unless the same authority explicitly supersedes it.

The aggregate may be `ITER478_LQG_S3_MINIMAL_BRIDGE_MAP_COMPLETE_SCOPED` if all six authority files are present, all five bridge classes are reproducibly resolved, and source-positive anchors are not misclassified as closure. This label means the dependency map is complete, **not** that D7-S3 is closed.

## Scope lock
No claim that these are mathematically impossible bridges; no cross-family evidence; no automatic ordering/supersession beyond explicit repository authority; no D7-S5 classification. If any class remains OPEN, D7-S3 remains NOT_CLOSED.
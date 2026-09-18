# Iter504V independent repaired Critic — preregistration

Date: 2026-09-19
Status: **FROZEN_BEFORE_CRITIC_IMPLEMENTATION_AND_EXECUTION**

## Gate

`ITER504V_SENTINEL_LOCAL_D_INDEPENDENT_CRITIC`

This gate reviews the already-completed source run only. It does not rerun, replace, refit, retune, or expand the source science.

## Frozen source object

- source gate: `ITER504V_SENTINEL_LOCAL_D_COUNTEREXAMPLE_FIRST`;
- original prereg commit: `c162f23df45a58c567fa04fcdf99035497e482f2`;
- authoritative source run: `35365466861`;
- source run number / attempt: `3 / 1`;
- source head: `d10ccd5f9bb465d306dad0b74bedfd3ecf5ad05e`;
- complete source metadata freeze commit: `5d093ed6b7ccb2c404515ecb77315d44c271b199`;
- complete source metadata freeze blob: `4886caa5d1e77e515b7ad0cda8698ab089f761b9`;
- provisional source authority commit: `72c02b6e50c4c3d4778473ad66d380aac3cc73d9`;
- provisional source authority blob: `e541dd281ac7e4b1794d37b07d73f6824213d135`;
- provisional source classification:
  `ITER504V_SENTINEL_LOCAL_D_NO_COUNTEREXAMPLE_SCOPED`.

This source classification is not terminal until this Critic closes.

## Immutable source inventory

Consume only the exact frozen source artifacts of run `35365466861`:

- 32 case artifacts: 16 Python 3.11 + 16 Python 3.13;
- 2 assembly artifacts;
- 1 aggregate artifact;
- total: 35.

The Critic source-lock must independently query GitHub artifact metadata and require exact agreement with the complete metadata freeze for artifact names, IDs, SHA256 digests, expiration state and count.

No source job is rerun.

## Independent reconstruction requirements

The Critic must independently reconstruct and validate, rather than trusting the source aggregate classification:

1. exact 16-state sentinel sequence and newline-terminated SHA256;
2. exact structural selection rule `box=4*block+path` and causal cycling rule;
3. direction/sign mapping from the frozen campaign manifest;
4. exact parent amplitude box intervals;
5. precision `384`, `python-flint==0.9.0`, 243 channels, no pruning;
6. R cohort exactly `6,8,10,12`;
7. rho cohort exactly `0.35,0.9,1.6,2.7`;
8. threshold exactly `1/20`;
9. robust slope floor exactly `1`;
10. deterministic dyadic midpoint tree with `MAX_DEPTH=3`;
11. every serialized leaf is an exact dyadic cell and has exact midpoint;
12. exact parent-child tree binding for every non-root visited node;
13. every terminal leaf belongs to the reconstructed visited tree;
14. `visited_node_count = 1 + parent_inclusion_record_count`;
15. local-D recomputation binding:
    - frozen evaluator blob identity is exact;
    - source evaluator semantics call the local evaluator inside the visit loop for every visited node;
    - case-level `local_derivative_recomputed_each_visited_node=true`;
    - terminal leaf `validated_local_derivative=true` and `local_derivative_recomputed_here=true`;
16. exact per-rho certification Boolean binding;
17. exact leaf certification = conjunction of all per-rho certifications;
18. uncertified terminal leaf allowed only at depth exactly 3;
19. possible-max grid covers exactly 4 R × 4 rho and channel indices are unique integers in `0..242`;
20. componentwise parent inclusion grid covers exactly 4 R × 4 rho × 243 channels and its summary Boolean is independently reconstructed;
21. exact case-set and no duplicates;
22. independent per-environment classification from unresolved leaves;
23. independent decision projection and SHA256;
24. exact cross-Python equality of all 16 case payloads and reconstructed decision projections;
25. exact source assembly and aggregate consistency;
26. exact immutable artifact provenance.

The Critic must not decide science from display floats. Exact serialized scientific booleans and exact rational identities control the decision.

## Required negative controls

At minimum all of these malformed variants must be rejected:

- `wrong_state_identity`;
- `missing_sentinel_case`;
- `changed_threshold`;
- `changed_floor`;
- `changed_depth`;
- `channel_pruning`;
- `wrong_R_cohort`;
- `wrong_rho_cohort`;
- `root_derivative_reuse`;
- `float_decision_transport`;
- `non_dyadic_partition`;
- `C4_true_leaf_false_rho`;
- `premature_unresolved_leaf_depth`;
- `wrong_exact_local_midpoint`;
- `wrong_parent_inclusion_child_interval`;
- `wrong_parent_inclusion_parent_interval`;
- `wrong_parent_inclusion_summary_boolean`.

Any required negative control that is not rejected => Critic invalid.

## Cross-Python Critic rule

Run the same frozen Critic independently in:

- Python 3.11;
- Python 3.13.

Both lanes consume the same frozen source artifacts.

Terminal Critic closure requires:

- both review jobs valid;
- byte-identical deterministic Critic JSON payloads;
- semantic classification equality;
- exact reconstructed source decision equality.

## Critic taxonomy

Only:

- `ITER504V_SENTINEL_CRITIC_CONFIRMS_NO_COUNTEREXAMPLE_SCOPED`;
- `ITER504V_SENTINEL_CRITIC_CONFIRMS_COUNTEREXAMPLE_SCOPED`;
- `ITER504V_SENTINEL_CRITIC_INVALID`.

The first maps to source terminal label
`ITER504V_SENTINEL_LOCAL_D_NO_COUNTEREXAMPLE_SCOPED`.

The second maps to source terminal label
`ITER504V_SENTINEL_LOCAL_D_COUNTEREXAMPLE_TO_UNIFORM_CERTIFICATION_SCOPED`.

Invalid maps to
`ITER504V_SENTINEL_INVALID`.

## Successor lock

Before terminal Critic closure:

- `PHASE_B_AUTHORIZED=false`;
- no MAX_DEPTH change;
- no 768-record run;
- no counterexample mechanism localization unless a valid counterexample is independently confirmed.

If Critic confirms no counterexample, claim only:
`no counterexample in frozen 16-state sentinel`.

Any Phase-B execution remains a new prospective gate.

## Claim ceiling

No full q=1 certification, all-768 certification, model-family failure, quantum-gravity solution, unique mechanism, or new-physics claim is authorized.


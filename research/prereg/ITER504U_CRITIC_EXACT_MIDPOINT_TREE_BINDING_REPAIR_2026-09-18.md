# Iter504U exact-midpoint and parent-tree verifier binding repair — preregistration

Date: 2026-09-18
Status: FROZEN_BEFORE_IMPLEMENTATION_AND_EXECUTION

## Gate

`ITER504U_CRITIC_EXACT_MIDPOINT_TREE_BINDING_REPAIR`

This is a same-science verifier repair required by independent Critical Review commit `b3d4a81b65ec0f4d2ac8a8210c45b5c98a0354cd`.
It repairs authority-path binding only. It does not rerun producer physics and does not alter the frozen Iter504U scientific object.

## Frozen parent objects

- source run: `35246605860`, head `102c7f9cafec956f3bc7bed4384ae755c98f761a`, attempt 1;
- source artifact freeze authority: `3302f77593e668ab48fdff887801571fa46467b1`;
- repaired-Critic historical closure run: `35267499787`;
- historical classification: `ITER504U_HELDOUT_LOCAL_D_GENERALIZES_SCOPED`;
- Critical Review qualification: `INVALID_IMPLEMENTATION` due verifier binding, not scientific FAIL.

## Frozen repair

For every serialized terminal leaf require exactly:

`Fraction(local_mid_q) == (Fraction(amp_lower_q) + Fraction(amp_upper_q)) / 2`.

For every componentwise parent-inclusion record require a reconstructed rooted dyadic-tree identity:

- child depth equals parent depth + 1;
- child interval is exactly one of the two dyadic halves of the serialized parent interval;
- every non-root visited child interval is unique;
- every parent is either the exact case root or another reconstructed visited child;
- every terminal leaf is either the root or a reconstructed visited child;
- the number of reconstructed non-root visited nodes equals `visited_node_count - 1`.

Both the repaired assembler validator and the independent repaired Critic validator must enforce these predicates.

## Required adversarial controls

At minimum:
- `wrong_exact_local_midpoint`;
- `wrong_parent_inclusion_child_interval`;
- `wrong_parent_inclusion_parent_interval`;
- inherited `C4_true_leaf_false_rho`;
- inherited `premature_unresolved_leaf_depth`.

Malformed controls must be rejected exactly. A malformed control that passes => `INVALID_IMPLEMENTATION`.

## Frozen execution rule

Use only the already-frozen immutable source artifacts from run `35246605860`.
No producer/source physics rerun is authorized.

The repaired assembler must reconstruct both environment assemblies from the frozen raw case artifacts. For valid source data its JSON output must be byte-identical to the frozen source assembly artifact in the corresponding environment.

The repaired Critic runs independently in Python 3.11 and 3.13 over the same frozen artifacts. Terminal closure requires byte equality of repaired Critic decision payloads and reconstructed assembly outputs across the independent review lanes.

## Terminal methodology taxonomy

- `ITER504U_CRITIC_EXACT_MIDPOINT_TREE_BINDING_REPAIR_VALIDATED_SCOPED`
- `ITER504U_CRITIC_EXACT_MIDPOINT_TREE_BINDING_REPAIR_INVALID`

If validated, the historical Iter504U scientific classification may be re-qualified as independently bound to the frozen exact object. If invalid, no scientific inference changes and Iter504V remains blocked.

## Claim ceiling

Same frozen Iter504U six-case held-out object only. No all-domain, model-family, D7, Candidate Gravity, new-physics, or global quantum-gravity claim is authorized.

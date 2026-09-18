# Iter504U exact-midpoint/tree verifier binding repair — terminal authority

Date: 2026-09-18  
Status: `TERMINAL_METHODOLOGY_AUTHORITY`

## Classification

`ITER504U_CRITIC_EXACT_MIDPOINT_TREE_BINDING_REPAIR_VALIDATED_SCOPED`

Run `35364505282`, head `5665ef6b6b4a682ee35ddbf4ff9cacf179a6a651`, attempt 1, terminal `completed/success`.

The repair used only immutable source artifacts from Iter504U source run `35246605860`; no producer physics rerun occurred.

## Repaired object binding

The repaired assembler and independent Critic now require exact rational
`local_mid_q == (amp_lower_q + amp_upper_q)/2` for every terminal leaf and reconstruct the serialized parent-inclusion records as one rooted dyadic visited-node tree.

Adversarial controls all reject malformed objects, including:

- `C4_true_leaf_false_rho`;
- `premature_unresolved_leaf_depth`;
- `wrong_exact_local_midpoint`;
- `wrong_parent_inclusion_child_interval`;
- `wrong_parent_inclusion_parent_interval`.

Both Python 3.11 and 3.13 review lanes passed. Repaired assembler outputs for both source environments were byte-identical to the frozen source assembly artifacts. Repaired Critic payloads were byte-identical across review lanes.

## Re-qualified historical science payload

- historical scientific classification: `ITER504U_HELDOUT_LOCAL_D_GENERALIZES_SCOPED`;
- cases: 6;
- terminal leaves: 19;
- unresolved leaves: 0;
- exact cross-environment decision agreement: true;
- decision projection SHA256: `b44f7bd0711a45d5469c8c1ce968f9b7f7e4cbe773dd33e0fb1bcf5beb22d3e6`;
- repaired Critic SHA256: `e6ba8fdc7221b065a92662fd9411ce525bcce0115161965f085868d61f13d214`;
- closure payload SHA256: `5ddf2717d7b954a57347b41a186388c474157880cf94e17b7e72bb2aeae22e30`.

## Immutable repair artifacts

- review 3.11: id `10556385581`, digest `sha256:7f251a969f810a1712e3f53dd6c65314b109db1851089d5a6082d539aaf338c5`;
- review 3.13: id `10556190878`, digest `sha256:74db6a0cd2076d13a501072c993b6ec849287eae005ac2005cd9c67d71ca7266`;
- closure: id `10555801284`, digest `sha256:edbc32b83358c4ea68edf5de69683182302a840ffea78fb9db09765a8e936cdf`.

All were unexpired at terminal read.

## Effect on frontier

The Independent Critical Review's `INVALID_IMPLEMENTATION` qualification is repaired for this exact frozen Iter504U object. It never constituted a scientific FAIL. The historical scoped science classification is now independently rebound to the exact midpoint and reconstructed parent-tree contract.

Iter504V sentinel may resume under its already-frozen preregistration. No Phase B is authorized.

## Claim ceiling

Exact frozen Iter504U six-case held-out object only. No all-domain, D7, model-family, Candidate Gravity, new-physics, or global quantum-gravity authority.

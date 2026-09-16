# D7_S2_EQ4_K5_GROUP_VARIABLE_TANGENT_PUSHFORWARD_GATE — terminal result

Date: 2026-09-16
Status: TERMINAL

## Classification

`D7_S2_EQ4_K5_GROUP_VARIABLE_TANGENT_PUSHFORWARD_PASS_SCOPED`

This is a scoped PASS for the raw/group-variable tangent-pushforward prerequisite only.

## Governance / authority

- Governing prospective preregistration: `bc9aa01263df1172206eb211b456bf5d78fe1b1b`.
- Later compatible duplicate preregistration: `32a2575ded77a938ed742526a9d62fe1e4756d41`.
- Frozen authority manifest: `716bf34bec114e160c88ff5a84bcd3d697f62fdd`.
- Execution-only coverage repair: `c0f8500aee43d4ee5686fc8dfc7b313e94b299d5`.
- Exact RREF/cycle/root/S5 implementation: `0c536f05e2203509f38a2e4d82cb4f3e21947ef6`.
- Independent tree/minor implementation: `453387a0d50d8426af52bee22dc8b1ddba7d9335`.
- Aggregate enforcing governing prereg: `67ee10b1dc21950eaaef4aa14273aadd8f9d72b1`.
- Workflow head: `da7f399e32dbacd41b7ae43c8a23ba991699bf84`.
- Authoritative Actions run: `35149367832`, terminal `completed/success`.
- Jobs: source-lock `104973468892`; tree-minors `104973521589`; RREF/cycle/root/S5 `104973521773`; aggregate `104973581115`.
- Aggregate artifact `10468447576`, `sha256:5c05ba9947691e8bf5a8c36bb5a63a3fc448c2ae00af327f4ddb4406bdd0144a`.
- Aggregate JSON SHA256 `e80384b0d0260bb6d30f1cef0be7399b1b8b6f3038c08755fb982fa7f29bef00`.
- Aggregate scientific SHA256 `07b2de217778082501f679f70aca5365f176ee627265f81e3badd69181bbaea4`.

The earlier run `35149108398` at `0918d64...` is retained as noncanonical partial evidence because it did not explicitly emit two checks required by the earlier governing preregistration. It was not used to weaken the criteria.

## Exact result

For all ten ordered Eq.(4) wedges `1<=a<b<=5`, the source-authorized identity `g_ab=g_b^{-1}g_a` differentiates at the identity to

`Y_ab = X_a - X_b`.

After fixing any one gauge root `X_r=0`, the per-real-generator reduced K5 incidence map is `Z^4 -> Z^10` and has, for every one of the five roots:

- exact rank `4`;
- domain nullity `0`;
- edge-space left-nullity / cycle dimension `6`.

Therefore the six-real-generator `sl(2,C)` raw map is

`R^24 -> R^60`, exact rank `24`, domain nullity `0`, cycle left-nullity `36`.

The root-1 restriction to wedges `(12,23,13)` exactly reproduces the prior terminal triangle differential `(-X2, X2-X3, -X3)`.

## Independent exact controls

Two independent proof paths agree:

1. rational RREF plus explicit integer cycle/root/S5 transport;
2. independent spanning-tree enumeration plus fraction-free integer determinant minors.

Frozen checks all pass:

- a fixed six-vector integer triangle-cycle basis has exact rank `6` and annihilates `B_r` for all five roots;
- all `20` ordered root-to-root tangent-coordinate changes are integer unimodular, determinants only `-1` or `+1`;
- K5 has `125` enumerated spanning trees for each root;
- all `625` root x spanning-tree `4x4` minors are exactly unimodular, determinants only `-1` or `+1`;
- all `600` S5-permutation x root signed orientation transports agree exactly;
- the rank/cycle invariants agree with terminal Iter466 at its topology-only scope.

## Scientific meaning

The full K5 **raw group-variable tangent pushforward** is now exact, injective on the gauge-fixed vertex-tangent domain, integrally unimodular on every spanning-tree coordinate chart, and invariant under root choice and exact signed S5 relabeling.

The six per-generator left-null directions are cycle relations in edge space. They are not a physical transverse quotient and are not physical zero modes.

Unit tree minors establish only raw linear tangent-coordinate Jacobians. They do not establish Haar measure transport or contact-distribution normalization.

## D7-S2 state

This closes exactly one D7-S2 layer:

`RAW_GROUP_VARIABLE_TANGENT_PUSHFORWARD = CLOSED_SCOPED`.

D7-S2 as a whole remains `NOT_CLOSED`. Still separate are at least:

- source-faithful simultaneous contact/distributional pushforward;
- Haar/contact normalization transport where required;
- physical transverse quotient/rank (currently source-authority BLOCKED);
- observable pushforward / any final distributional classification.

## Claim ceiling

No physical transverse rank, distributional existence/nonexistence, convergence/finiteness theorem, D7-S2 closure, terminal D7 selector, model/family failure, Candidate Gravity or new-theory/new-physics conclusion follows.

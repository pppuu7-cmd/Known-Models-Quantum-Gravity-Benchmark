# D7_S2_EQ4_K5_GROUP_VARIABLE_TANGENT_PUSHFORWARD_GATE

Date: 2026-09-16  
Status: PROSPECTIVELY PREREGISTERED — no production outcome consumed

## Independent D7-S2 question

Given the already source-authorized Eq.(4) identity

`g_ab = g_b^{-1} g_a`, for all `1 <= a < b <= 5`,

and the already applied global vertex gauge fixing, does the identity-point differential of **all ten K5 wedge maps** define an exact source-faithful group-variable tangent pushforward whose incidence/cycle structure is root-, tree- and relabeling-invariant?

This gate tests only the raw/group-variable pushforward layer of D7-S2. It is independent of the blocked physical-transverse quotient and does not compute a distributional/contact pushforward.

## Frozen authority

- primary source record: `sources/arxiv_2601_23162v1_causal_vertex.json`, Git blob `f0b520fc04904e038f252dc5b45d23893cb020ed`;
- exact general wedge-identity record: `sources/arxiv_2601_23162v1_eq4_triangle_wedge_group_argument_identity_v15.json`, Git blob `92a43e79a0f0934db78933c453fd45fcad6daab9`;
- terminal triangle raw-Lie result: commit `bfb0cf44c3a95e667941d34ae9961234c8923bf2`;
- terminal Iter466 K5 correlation-carrier result: commit `67c66a2edc3425f06aaadb369d2f3606184d3733`.

Historical V8, a textbook quotient, the blocked physical quotient and partial Iter461 artifacts are forbidden inputs.

## Frozen mathematical object

Vertices: `V={1,2,3,4,5}`.  
Ordered wedges: `E={(a,b):1<=a<b<=5}`, ten edges.

For a gauge root `r`, set `X_r=0`. At the identity, differentiate the literal source product `g_b^{-1}g_a` using the same convention already verified on triangle `(12,23,13)`:

`Y_ab = X_a - X_b`.

For each Lie generator this gives a `10 x 4` integer edge-by-free-vertex matrix `B_r`. The real `sl(2,C)` map is six identical generator blocks.

## PASS criteria

PASS requires all of the following exactly:

1. source records match the frozen Eq.(4) ten-wedge object and literal `g_ab=g_b^{-1}g_a` identity;
2. the root-1 restriction to wedges `(12,23,13)` equals the terminal triangle differential `(-X2, X2-X3, -X3)`;
3. for every root `r=1..5`, `rank(B_r)=4`, domain nullity `0`, edge-space left-nullity `6`;
4. therefore the real six-generator map is `24 -> 60` with exact rank `24`, domain nullity `0`, left-nullity `36`;
5. an exact six-vector integer cycle basis annihilates `B_r` from the left and has rank `6`;
6. all `125` spanning trees of K5 are found exactly; for every root and every spanning tree, the selected `4 x 4` edge minor has determinant `+/-1`;
7. all root-to-root tangent-coordinate changes are integer unimodular (`|det|=1`);
8. all `120` vertex relabelings preserve the rank/cycle/tree invariants after the induced ordered-edge orientation transport;
9. independent exact RREF and tree/minor methods agree on the scientific payload;
10. no physical quotient, distributional contact product, Haar/contact normalization or observable pushforward is inserted.

The unit tree minors authorize only a **raw linear tangent-coordinate Jacobian**. They are not Haar/contact normalization statements.

## FAIL / BLOCKED / INVALID

- FAIL: the source-defined differential is exact and computable but violates a frozen algebraic criterion above (for example rank < 4, a non-unimodular spanning-tree minor, or a failed exact cycle relation).
- BLOCKED: a required source identity needed to define the raw full-K5 differential is absent from frozen authority.
- INVALID: source identities are changed post hoc; historical V8, a textbook/physical quotient, partial nonterminal artifacts, or outcome-selected conventions are introduced; or a raw tangent Jacobian is relabeled as a physical measure normalization.

## Claim ceiling

A PASS closes only the D7-S2 **group-variable tangent pushforward prerequisite**. It does not establish the distributional/contact pushforward, physical transverse quotient, Haar/contact normalization, observable pushforward, convergence/finiteness, D7-S2 closure, terminal D7 selector, Candidate Gravity, model/family failure or new physics.

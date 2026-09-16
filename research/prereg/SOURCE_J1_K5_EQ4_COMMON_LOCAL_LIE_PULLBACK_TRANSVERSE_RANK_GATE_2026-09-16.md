# SOURCE_J1_K5_EQ4_COMMON_LOCAL_LIE_PULLBACK_TRANSVERSE_RANK_GATE

Date: 2026-09-16
Status: PROSPECTIVELY PREREGISTERED — no production outcome consumed

## Frozen parent authority

- Terminal wedge-identity result: `results/SOURCE_J1_K5_EQ4_TRIANGLE_WEDGE_GROUP_ARGUMENT_IDENTITY_TERMINAL_2026-09-16.md`, terminal classification `EQ4_TRIANGLE_WEDGE_GROUP_ARGUMENT_IDENTITY_PASS_SCOPED`.
- Canonical identity result commit `6df9d695afb4aa406af8aae7fdfe17a9f5ac0f71` and terminal record commit `c433ec7ce09a61e3401abd6ec0b04348d7d777e9`.
- Independent identity Critic commit `4c4adc87b167caf6811d79e5953de012978684b8`.
- Primary PDF `arXiv:2601.23162v1`, SHA256 `cc533af3c84de8c0de57523a795ba4357523712f1746ce55fa78eb521cd51713`.
- Frozen source records: `sources/arxiv_2601_23162v1_eq4_triangle_wedge_group_argument_identity_v15.json` blob `92a43e79a0f0934db78933c453fd45fcad6daab9`; `sources/arxiv_2601_23162v1_eq4_local_collision_map_expansion_v13.json` blob `fdfb13f9974ebc891cb3f490ca553dd0991d9136`; `sources/arxiv_2604_24945v1_eq4_local_collision_map_expansion_v13.json` blob `c742e8cab0648b8fbaef88f09876644c6c2c3077`.

No later source extraction may silently enlarge this gate's authority.

## Frozen scientific object

The fixed same-realization Eq.(4) triangle is `(12,23,13)`, with `g1=1` and source-authorized maps

- `G12(g2,g3)=g2^{-1}`;
- `G23(g2,g3)=g3^{-1} g2`;
- `G13(g2,g3)=g3^{-1}`.

Eq.(4) integrates over `SL(2,C)` group variables. The local point for the common-contact pullback is the identity tuple `(g2,g3)=(1,1)`.

Use left-trivialized tangent variables `X2,X3 in sl(2,C)`. The raw local pullback is the differential of the literal source map only. Ordinary Lie-group differential identities for inversion and multiplication may be used algebraically; no Toller matrix composition, V8 additive relation, representation-argument substitution or guessed wedge map is allowed.

## Frozen raw differential checks

Construct the exact coefficient map for each Lie-algebra generator. Do not freeze its outcome/rank before execution. Compute rank by two independent exact methods:

1. exact rational row reduction of the generator-level coefficient matrix;
2. exact nullity/minor or independent linear-map argument implemented separately.

Repeat under at least two invertible rational basis replacements in domain/codomain and under the three triangle relabelings induced by permutations of wedge labels, with orientation/inversion transported from the literal `g_b^{-1}g_a` rule. Raw rank must be invariant under admissible invertible coordinate replacements.

## Physical transverse quotient lock

Raw coordinate rank is **not** by itself physical transverse rank.

A finite physical transverse quotient may be assigned only if the frozen primary authority explicitly defines, for this same realization:

1. which local tangent directions are quotiented as gauge/redundant after `g1=1`;
2. the quotient/domain-codomain projection used for the three contact conditions;
3. how the scalar one-wedge contact variables/distributions pull back to that quotient;
4. the corresponding Jacobian/Haar/contact-normalization transport;
5. S3/orientation coordinate transport on the quotient.

If any essential object is absent from the frozen authority, set `physical_transverse_rank=null` and classify the physical-rank question BLOCKED even if raw rank is exact and nonzero.

## PASS / FAIL / BLOCKED / INVALID

- `PASS_SCOPED`: all frozen authority objects above are present, the physical quotient is explicit, two independent exact rank computations agree, admissible basis/orientation/S3 controls pass, and the quotient rank satisfies the preregistered full-transversality criterion of the explicitly defined quotient.
- `FAIL_SCOPED`: only if the quotient and normalization objects are all source-authorized and exact independent computations prove rank deficiency on that defined physical quotient.
- `BLOCKED_SCOPED`: raw local differential may be computed, but one or more essential physical quotient/Jacobian/Haar/contact-normalization/S3 transport objects are absent. Missing rank remains `null`, never zero.
- `INVALID`: guessed quotient, textbook/contact formula not in frozen authority, historical V8 relation, unstated orientation/inversion, noninvertible basis selector, outcome-dependent basis choice, numerical tolerance, post-hoc criteria change, or partial/nonterminal artifact consumption.

## Controls

Positive fixture: a fully specified abstract quotient with full generator-level rank must PASS its internal rank checks.

Negative fixtures must distinguish:

- undefined quotient -> BLOCKED with `physical_transverse_rank=null`;
- explicit rank-deficient quotient -> FAIL only when all authority fields are present;
- noninvertible basis map -> INVALID;
- reversed wedge product/inversion -> INVALID;
- omitted normalization transport -> BLOCKED;
- raw rank substituted for physical quotient rank -> INVALID.

## Claim ceiling

Even PASS is a finite local same-realization Lie-pullback/transversality certificate only. It does not establish smooth Eq.(4) remainder, order-7 jet completeness, distributional global existence/nonexistence, full K5/model/family failure, D7 closure, selector authority, Candidate Gravity, or any new theory/physics claim.

Governance locks remain unchanged: `RQIR Core v1.0 = FROZEN`; `D7-S2 = NOT_CLOSED`; `D7-S3 = NOT_CLOSED`; `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`; Candidate Gravity inactive; terminal selector labels unauthorized.

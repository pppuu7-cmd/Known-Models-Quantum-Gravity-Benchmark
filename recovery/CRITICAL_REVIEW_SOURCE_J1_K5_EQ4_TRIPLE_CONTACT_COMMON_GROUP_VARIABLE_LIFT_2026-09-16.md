# Independent Critical Review — SOURCE_J1_K5_EQ4_TRIPLE_CONTACT_COMMON_GROUP_VARIABLE_LIFT_GATE

Date: 2026-09-16
Status: TERMINAL_CRITIC
Verdict: `INVALID_IMPLEMENTATION`

## Scope

Adversarial review of terminal Research commit `48f59aa10203903b494bd33edb5e498be24bb24f`, without introducing alternative physics. The review checks only whether the frozen primary authority and implementation support the terminal claim that exact same-realization wedge argument maps `G12/G23/G13` were absent.

## Frozen authority checked

- `arXiv:2601.23162v1`, locked PDF SHA256 `cc533af3c84de8c0de57523a795ba4357523712f1746ce55fa78eb521cd51713`.
- `arXiv:2604.24945v1`, locked PDF SHA256 `f37659f5cb4674dd0c1b81a6e55f5d1dfd992c60b0e85cb2859322b860e22046`.
- authority ledger commit `bb5d7b922784231b8e89d6538fea11ab8ee0a09e`.
- classifier commit `e46c47a96e77a2819d171e1888dca3b1a584360a`.
- terminal result `48f59aa10203903b494bd33edb5e498be24bb24f`.

## Adversarial finding

The primary causal-vertex source explicitly defines, immediately before Eq. (4), the Lorentz-group wedge element

`g_ab = g_b^{-1} g_a`

as the parallel transport associated with wedge `(ab)`. Eq. (4) then uses the Toller factor with literal group argument `(g_b^{-1} g_a)` for the product over `1 <= a < b <= 5`. Immediately after Eq. (4) the source states the vertex gauge fixing `g1 = 1`. The same source explicitly states wedge causal orientation `kappa_ab = sigma_a sigma_b`.

The spinorial/contact realization also preserves the same group input. Eq. (16) again evaluates each Toller factor at `(g_b^{-1} g_a)`, Eq. (17) defines the one-group contact scalar/distribution in terms of `B(z,g)`, and the source explicitly writes

`B_ab = B(z_ab, g_b^{-1} g_a)`.

Therefore the frozen primary authority does contain the exact group argument identity needed to instantiate the triangle wedges. In the gauge-fixed Eq. (4) realization this gives literally:

- wedge `12`: `G12 = g_2^{-1} g_1 = g_2^{-1}`;
- wedge `23`: `G23 = g_3^{-1} g_2`;
- wedge `13`: `G13 = g_3^{-1} g_1 = g_3^{-1}`.

These are source identities, not historical V8 `B12=x, B23=y, B13=x+y` and not textbook reconstructions.

## Implementation defect

The production classifier did not parse or test those primary-source identities. It verified each durable source record only by `git hash-object`, PDF SHA256 and number of `candidate_passages`. It then set `maps_obj` solely by reading the manually populated authority-ledger field `authorized_primitives.three_wedge_group_argument_maps`; because that field was `null`, the classifier deterministically concluded `three_wedge_group_argument_maps_present=false` without examining the source passage that explicitly contains `g_ab=g_b^{-1}g_a`.

Thus the negative result for `THREE_WEDGE_GROUP_ARGUMENT_MAPS` is circular with respect to the summary ledger rather than an independent extraction from the frozen primary authority.

## Required checks from the review request

- absence of wedge maps follows from frozen authority: **FAIL** — primary authority explicitly contains the map;
- Eq.(4)/Appendix/contact identities mapped correctly: **FAIL in production**, because the explicit Eq.(4) map was omitted from the production ledger;
- integration variables vs wedge/Toller/representation arguments mixed: no evidence of a physical-variable conflation in the terminal prose, but the implementation failed to propagate the group-argument identity from source to ledger;
- `null` rank converted to `0`: **no**; terminal correctly kept `null`;
- historical V8 auxiliary relation reintroduced: **no**; V8 remained non-authoritative;
- orientation/inversion/multiplication order silently imposed: **no hidden guess is needed** for the group argument, because the primary source explicitly fixes `g_b^{-1}g_a` and `1<=a<b<=5`.

## Critic verdict

`INVALID_IMPLEMENTATION`

This verdict invalidates the terminal Research result as downstream authority for the claim that `G12/G23/G13` are absent. It does **not** assert that the full parent common-local-Lie lift passes, because Jacobian/Haar/contact-normalization transport, local Lie pullback, transverse quotient/rank and S3 transport were not recomputed here.

The scientifically admissible continuation is the already prospectively frozen `SOURCE_J1_K5_EQ4_TRIANGLE_WEDGE_GROUP_ARGUMENT_IDENTITY_GATE`, which must terminalize the exact maps and conventions before any transverse-rank calculation.

`BLOCKED != FAIL`; this Critic result is an implementation/source-extraction defect, not a physical transversality claim. Governance locks and D7 status remain unchanged.

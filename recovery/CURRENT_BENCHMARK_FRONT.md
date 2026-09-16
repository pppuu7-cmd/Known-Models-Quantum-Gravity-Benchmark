# Current Benchmark Front
Updated: 2026-09-17

Fresh repository `main` and fresh Actions state always outrank this navigation document if they diverge.

## Latest terminal Research execution

`D7_S2_EQ4_K5_SIMULTANEOUS_CONTACT_COVECTOR_OBJECT_GATE`

Classification:

`D7_S2_EQ4_K5_SIMULTANEOUS_CONTACT_COVECTOR_OBJECT_BLOCKED_SCOPED`

**BLOCKED, not FAIL.**

Authority/execution chain:

- preregistration `e20aafb9c894759b8093bada4bacdbb9b8e1a425`;
- source extraction `9f94f8dae1f24ede68f1cb7dbe102710fc03f4e6`;
- preterminal Critic `f26908e4a859584df4638f537d5342d1338198a6`;
- frozen authority `b4c9c0a4ddfa0742f1ba9aad490f3d0510a36bcc`;
- execution-only classifier normalization repair `d8bd1bc204d1e0ea91b59296a5163d46163a4f43`;
- repaired classifier `04e4bda8c3f80dcdec49c2629493e8d9fcd6cb20`;
- aggregate `71306a6f083ec0c4f1df7a1416fc71fd626966f4`;
- workflow head `ea5f576216cc1098cdcf82aeca1b1fc2c2a7b759`;
- authoritative Actions run `35150140512`, terminal `completed/success`;
- jobs: source-lock `104976079713`, Python 3.11 `104976121380`, Python 3.13 `104976121634`, aggregate `104976188535`;
- aggregate artifact `10468089503`, digest `sha256:73fa7ba06de3f024dbc953d4a6aec58bc134d881ba9added610cd33fbed1123b`;
- aggregate JSON SHA256 `c3e57bd7f1abc3fd27b9ac919ae849de5620b6026ffd9a1d535836ddd06fde8a`;
- aggregate scientific SHA256 `3e2aef96bd4029336490383c03f9b3a42b4f9cb0671d5f1faab559c4f8a48a58`;
- both classifier lanes scientific SHA256 `8c4dc6059e6b908575ea400099167e4da0eacde9a2ff3144862c0b135c5b0263`.

Post-terminal Critic: `515c947e27043b8c447ddd28ef81b4fb89c28a46`, verdict `CRITIC_CONFIRMS_SCOPED_CONTACT_OBJECT_BLOCKED_NO_ZERO_OR_RANK_PROMOTION`.

Green CI is execution/provenance evidence only.

## Exact contact-object result

The locked primary `arXiv:2601.23162v1` explicitly defines the one-wedge contact scalar

`B(z,g)=log(<g^dagger z|g^dagger z>/<z|z>)`

and composes the causal contact distribution with the full `B(z,g)` object. In the source coherent-state realization, the auxiliary `z_ab in CP1` variables and the group variables are joint integration variables. Thus the full first differential on `CP1 x SL(2,C)` is mathematically defined; the contact formula itself is not missing.

The source does not establish:

- a rule setting `dz_ab=0` for the exact contact distribution;
- conditioning the contact distribution on fixed `z_ab`;
- an equivalent ten-wedge contact-covector object living only on the gauge-fixed Eq.(4) group-variable tangent domain.

Minimal blocker:

`SOURCE_AUTHORIZED_RESTRICTION_OR_CONDITIONING_MAP_FROM_FULL_CONTACT_COVECTOR_ON_CP1_X_SL2C_TO_GROUP_ONLY_TANGENT_COVECTOR`.

Therefore `group_only_contact_covector_rank=null` and `physical_transverse_rank=null`. Missing restriction is not a zero covector, not a rank deficiency and not physical/transversality FAIL.

Do not repeat this source gate unless a new preregistration-authorized primary artifact explicitly supplies the restriction/conditioning map.

## Newly closed D7-S2 raw layer

Immediately upstream, `D7_S2_EQ4_K5_GROUP_VARIABLE_TANGENT_PUSHFORWARD_GATE` is terminal:

`D7_S2_EQ4_K5_GROUP_VARIABLE_TANGENT_PUSHFORWARD_PASS_SCOPED`.

Canonical terminal commit `5f6dfa2bac5915647aa21fe0cde2843bee25ed46`; governing preregistration `bc9aa01263df1172206eb211b456bf5d78fe1b1b`; repaired authoritative workflow head `da7f399e32dbacd41b7ae43c8a23ba991699bf84`; run `35149367832`.

Exact result:

- for all ten ordered wedges, `Y_ab=X_a-X_b`;
- per Lie generator reduced K5 map `Z^4 -> Z^10`: rank `4`, domain nullity `0`, cycle left-nullity `6` for every gauge root;
- full real `sl(2,C)` map `R^24 -> R^60`: rank `24`, domain nullity `0`, cycle left-nullity `36`;
- fixed six-cycle integer basis has exact rank `6` and annihilates every root-reduced map;
- all `20` root-to-root coordinate changes are integer unimodular;
- all `625` root x spanning-tree minors are exactly `+/-1`;
- all `600` signed S5-permutation x root transports agree exactly;
- triangle restriction reproduces the earlier source-authorized differential exactly.

Aggregate scientific SHA256 `07b2de217778082501f679f70aca5365f176ee627265f81e3badd69181bbaea4`.

Independent Critic `f9c756d6cc6af1775bad2132245b5493b55f32e1` confirms the scoped raw PASS. A separately implemented auto-research pipeline also reproduced the same frozen scientific invariants under the same governing preregistration; reproduction record `97ff25be7120ab38fa7cccc32eae343cef061cd0`.

Unit tree minors establish raw tangent-coordinate unimodularity only; they do not establish Haar/contact normalization or a physical quotient.

Thus:

`RAW_GROUP_VARIABLE_TANGENT_PUSHFORWARD = CLOSED_SCOPED`.

## Physical quotient branch retained

`SOURCE_J1_K5_EQ4_PHYSICAL_TRANSVERSE_QUOTIENT_PRIMARY_AUTHORITY_ESCALATION_GATE` remains terminal

`EQ4_PHYSICAL_TRANSVERSE_QUOTIENT_PRIMARY_AUTHORITY_BLOCKED_SCOPED`.

Its minimal blocker remains `PUBLISHED_VERSION_FULLTEXT_AUTHORITY_ACCESS_CEILING`; `physical_transverse_rank=null`. The inaccessible published version is not treated as evidence that the object cannot exist.

## D7 state / next information-efficient frontier

D7-S2 remains `NOT_CLOSED`. Its layers are now separated:

1. raw group-variable tangent pushforward = `CLOSED_SCOPED`;
2. group-only simultaneous contact-covector object = `BLOCKED_SCOPED` on the explicit CP1/group restriction map;
3. physical transverse quotient/projection = `BLOCKED_SCOPED` on primary-authority access/object definition;
4. Haar/contact normalization transport = not closed;
5. observable/distributional final pushforward = not closed.

Do not spend compute repeating the two source-blocked K5 branches. A future K5 child requires genuinely new authorized authority for either the contact restriction or physical quotient.

For independent global D7 work, the frozen D7 contract still requires:

- `D7-S3 SAME_REALIZATION_OBJECT_COMPLETENESS`: same-realization physical objects, parameter transport, normalized comparator-ready observables, propagated theory/nuisance/covariance/numerical errors;
- `D7-S4 COMMON_DOMAIN_GLOBAL_COMPARABILITY`: explicit common-domain normalization, documented cross-family reduction/overlap maps, common frozen decision semantics, global D4 closure.

Current evidence does not justify inventing a missing S3/S4 map merely to create another gate. Highest-information policy is therefore to reopen only a concrete S3/S4 obligation whose object and same-realization authority are already pinned, or when new primary/comparator data makes such an obligation executable. Metadata-only audits and repeated broad searches are deprioritized.

Iter461 run `34748503239` remains nonterminal/consumer-locked; do not duplicate or consume partial substantive values.

## Governance lock

- `RQIR Core v1.0 = FROZEN`.
- `D7-S2 = NOT_CLOSED`.
- `D7-S3 = NOT_CLOSED`.
- `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`.
- terminal selector labels remain unauthorized.
- Candidate Gravity remains inactive.
- `BLOCKED != FAIL`.
- missing restriction/map/rank != zero.
- raw rank != physical rank.
- finite/local result != global theorem.
- no model/family/global/new-theory/new-physics conclusion follows.

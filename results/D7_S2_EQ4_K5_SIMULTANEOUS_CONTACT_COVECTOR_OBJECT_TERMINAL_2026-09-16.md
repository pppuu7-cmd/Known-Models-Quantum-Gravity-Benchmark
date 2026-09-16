# D7_S2_EQ4_K5_SIMULTANEOUS_CONTACT_COVECTOR_OBJECT_GATE — terminal result

Date: 2026-09-16
Status: TERMINAL

## Classification

`D7_S2_EQ4_K5_SIMULTANEOUS_CONTACT_COVECTOR_OBJECT_BLOCKED_SCOPED`

**BLOCKED, not FAIL.**

## Authority/execution

- prospective preregistration `e20aafb9c894759b8093bada4bacdbb9b8e1a425`;
- primary-source extraction `9f94f8dae1f24ede68f1cb7dbe102710fc03f4e6`;
- independent preterminal Critic `f26908e4a859584df4638f537d5342d1338198a6`;
- frozen authority manifest `b4c9c0a4ddfa0742f1ba9aad490f3d0510a36bcc`;
- execution-only status-normalization repair freeze `d8bd1bc204d1e0ea91b59296a5163d46163a4f43`;
- repaired classifier `04e4bda8c3f80dcdec49c2629493e8d9fcd6cb20`;
- aggregate `71306a6f083ec0c4f1df7a1416fc71fd626966f4`;
- workflow head `ea5f576216cc1098cdcf82aeca1b1fc2c2a7b759`;
- authoritative Actions run `35150140512`, terminal `completed/success`;
- jobs: source-lock `104976079713`, Python 3.11 `104976121380`, Python 3.13 `104976121634`, aggregate `104976188535`;
- aggregate artifact `10468089503`, `sha256:73fa7ba06de3f024dbc953d4a6aec58bc134d881ba9added610cd33fbed1123b`;
- aggregate JSON SHA256 `c3e57bd7f1abc3fd27b9ac919ae849de5620b6026ffd9a1d535836ddd06fde8a`;
- aggregate scientific SHA256 `3e2aef96bd4029336490383c03f9b3a42b4f9cb0671d5f1faab559c4f8a48a58`;
- both Python lanes scientific SHA256 `8c4dc6059e6b908575ea400099167e4da0eacde9a2ff3144862c0b135c5b0263`.

The first run `35149976729` is retained as noncanonical execution evidence because a derived boolean failed to normalize a `NOT_ESTABLISHED_WITHOUT_*` ledger value. The classification itself remained BLOCKED, but the contradictory diagnostic payload was not terminalized.

## Exact source result

The locked primary `arXiv:2601.23162v1` explicitly provides:

- Eq.(4) group variables and `g_ab=g_b^{-1}g_a`;
- the coherent-state realization integrating both group variables and one auxiliary `z_ab in CP1` per wedge;
- Appendix C Eq.(31)-Eq.(32): `B(z,g)=log(<g^dagger z|g^dagger z>/<z|z>)`;
- Appendix D Eq.(35)-Eq.(36): the causal step/contact distribution is composed with the full `B(z,g)` object.

Therefore the contact formula itself is not missing, and the full first differential on the joint `CP1 x SL(2,C)` domain is algebraically defined.

However, the admissible source does **not** establish:

1. a rule restricting the contact differential to group directions by setting `dz=0`;
2. a conditioning of the contact distribution on fixed auxiliary spinor `z`;
3. an equivalent group-only ten-wedge contact-covector object on the gauge-fixed Eq.(4) group-variable tangent domain.

Minimal missing object:

`SOURCE_AUTHORIZED_RESTRICTION_OR_CONDITIONING_MAP_FROM_FULL_CONTACT_COVECTOR_ON_CP1_X_SL2C_TO_GROUP_ONLY_TANGENT_COVECTOR`.

## Scientific boundary

The terminal full-K5 raw group tangent map remains valid and closed at its own scope. It can pull back a group component once such a component is source-authoritatively selected, but it cannot authorize discarding the auxiliary-spinor component of `dB`.

Thus:

- `group_only_contact_covector_rank = null`;
- `physical_transverse_rank = null`;
- missing restriction is not a zero covector;
- no contact/transversality FAIL is established;
- no distributional product existence/nonexistence follows.

`CP1` projectivization is an auxiliary-spinor construction, not the missing group-tangent quotient/restriction. Raw spanning-tree unit determinants do not provide contact or Haar normalization.

## D7-S2 state

- `RAW_GROUP_VARIABLE_TANGENT_PUSHFORWARD = CLOSED_SCOPED`.
- `GROUP_ONLY_SIMULTANEOUS_CONTACT_COVECTOR_OBJECT = BLOCKED_SCOPED`.
- physical quotient remains independently BLOCKED.
- D7-S2 remains `NOT_CLOSED`.

Do not repeat this source gate unless new preregistration-authorized primary authority explicitly supplies the missing restriction/conditioning map.

## Claim ceiling

No physical transverse rank, contact rank, distribution-product theorem, convergence/finiteness theorem, Haar/contact normalization, observable pushforward, D7-S2 closure, terminal selector, model/family failure, Candidate Gravity or new-theory/new-physics conclusion follows.

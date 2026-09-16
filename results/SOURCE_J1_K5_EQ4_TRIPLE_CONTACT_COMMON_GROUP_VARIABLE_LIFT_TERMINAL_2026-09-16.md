# SOURCE_J1_K5_EQ4_TRIPLE_CONTACT_COMMON_GROUP_VARIABLE_LIFT_GATE — terminal result

Date: 2026-09-16
Status: TERMINAL

## Authority

- Gate: `SOURCE_J1_K5_EQ4_TRIPLE_CONTACT_COMMON_GROUP_VARIABLE_LIFT_GATE`.
- Prospective preregistration commit: `7620bc32ad691d37100642e8e33fd15cadd729a9`.
- Frozen authority-ledger commit: `bb5d7b922784231b8e89d6538fea11ab8ee0a09e`.
- Exact classifier commit: `e46c47a96e77a2819d171e1888dca3b1a584360a`.
- Aggregate-code commit: `cd36c9311546db327cabac993927cb7b43658b7c`.
- Workflow head: `8b190337ed61020cd0d4c264cf7195f2acfaf324`.
- Authoritative Actions run: `35130513871`, terminal `completed/success`.
- Jobs: source-lock `104910071913`; Python 3.11 `104910115562`; Python 3.13 `104910115607`; aggregate `104910174438`.
- Artifacts: Python 3.11 `10461570684` / `sha256:ab0cbdcb80d3d09a12fa42d90b5b7257d7c06f4f7255b61743b121a5e9a30fb3`; Python 3.13 `10460832183` / `sha256:881b466212055fd229540f4cdb1643f4564db63fb3da645a5ea341602e5c37ca`; aggregate `10460872090` / `sha256:d4f99d3d3e6a31db9ff48bf82c8dc86e4eb1198d3f25f16bd5917ad9def29c2e`.
- Aggregate JSON SHA256 `b64dbd71a54f1c76f486ea4dbcbafc8ac909edc0d329f3a86f8837b18b92ac9d`.
- Aggregate log SHA256 `f807f8f44661bd05f59a81fbfd85b03c7929893bf7f367756622924d5c86d5bc`.
- Aggregate decision SHA256 `e3bc1d12580ee03c1c18049b7881668242e24990bfe0779292bc98b4e6eab32f`.

Green CI is execution/provenance evidence only.

## Frozen terminal classification

`EQ4_TRIPLE_CONTACT_COMMON_GROUP_VARIABLE_LIFT_BLOCKED_SCOPED`

**BLOCKED, not FAIL.**

## Exact result

Both independent lanes agree and all frozen outcome-sensitive controls pass.

For the fixed Eq. (4) triangle `(12,23,13)` the frozen source authority establishes:

- `COMMON_GAUGE_FIXED_GROUP_TUPLE = present`.

It does not establish:

- `THREE_WEDGE_GROUP_ARGUMENT_MAPS`;
- `COMMON_LOCAL_GROUP_LIE_LIFT`;
- `TWO_DIMENSIONAL_TRANSVERSE_QUOTIENT`;
- `JACOBIAN_HAAR_CONTACT_NORMALIZATION_TRANSPORT`;
- `S3_ORIENTATION_COORDINATE_TRANSPORT`.

Therefore:

- `three_wedge_group_argument_maps_present=false`;
- `common_local_group_lie_lift_present=false`;
- `transverse_rank=null`, not zero;
- `jacobian_haar_contact_normalization_transport_present=false`;
- `s3_orientation_coordinate_transport_present=false`.

The positive rank-2 shared-lift, rational basis-change and orientation-sign controls pass. The missing-wedge-map control reaches BLOCKED with undefined rank, the explicit rank-1 fixture reaches FAIL, and the missing-transport fixture reaches BLOCKED. Thus the production BLOCKED branch is outcome-sensitive rather than hard-coded.

## New fact

The current durable source authority is strong enough to identify the shared gauge-fixed Eq. (4) integration variables, but not strong enough to specify the three actual wedge group arguments `G12`, `G23`, `G13` on those variables in the frozen same-realization triangle. Because those explicit wedge maps are absent, the simultaneous local Lie-algebra pullback and its transverse differential cannot yet be constructed source-authoritatively. The transverse rank is undefined, not rank zero.

A one-group Cartan/Toller reconstruction cannot substitute for the missing three wedge argument maps, and the documented fact that Toller matrices do not obey an ordinary representation composition law cannot be repurposed as a group-variable composition rule.

## Claim ceiling

This result establishes only a same-realization source/object-definition blocker for the fixed Eq. (4) triangle common-group lift. It does not establish a transversality failure, smooth Eq. (4) remainder, order-7 jet, V8 physical quotient/nullspace-action rank, distributional existence/nonexistence, full-K5/model/family failure, D7 closure/selector, Candidate Gravity, `QUANTUM_GRAVITY_SOLVED`, `ALL_KNOWN_MODELS_FAIL`, `NEW_THEORY_REQUIRED`, or `NEW_PHYSICS_FOUND`.

## Next recommended gate

Prospectively freeze `SOURCE_J1_K5_EQ4_TRIANGLE_WEDGE_GROUP_ARGUMENT_IDENTITY_GATE`.

That gate should ask only whether the frozen primary authority explicitly pins the Eq. (4) group argument of each triangle wedge `12`, `23`, `13`, including multiplication order, inversion/orientation convention, gauge-fixed variable identity and the input group element used by the one-wedge contact scalar. PASS would pin the three same-realization maps; BLOCKED would record absent source identity; guessed textbook formulas or unstated orientation conventions must be INVALID. No contact rank should be inferred until those maps are terminally pinned.

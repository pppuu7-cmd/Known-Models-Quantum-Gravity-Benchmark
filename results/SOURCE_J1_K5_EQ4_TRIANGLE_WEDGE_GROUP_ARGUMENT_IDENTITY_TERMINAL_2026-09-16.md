# SOURCE_J1_K5_EQ4_TRIANGLE_WEDGE_GROUP_ARGUMENT_IDENTITY_GATE — terminal result

Date: 2026-09-16
Status: TERMINAL

## Authority

- Preregistration: `ddf246b861d4e367af409e3ae5b6c97ccfd1ea7e`.
- Frozen authority: `440c853516c2357029c848c83e48a7f6a39d0c86`.
- Primary-source extraction: `4a21e9148393ebcefdfbb2a17cfbbf51af82b052`.
- Independent parent Critic: `18133e8de9f919960e7100952da3aeee77c0bc06`.
- Classifier: `1f48955a2f8b15a544121ab07675cdba8830907f`.
- Aggregate implementation: `a4263330c207b5fdc048fa1996a3e64652490f72`.
- Failed shallow-history execution retained as non-scientific historical evidence: run `35142365235`.
- Execution-only repair freeze: `03b3d0f1f22f6bb2318fc365372ba70a1b42d449`.
- Authoritative repaired workflow head: `5ede230e4b7a23b2215dc3b86232545c0bf93418`.
- Authoritative Actions run: `35145567502`, terminal `completed/success`.
- Jobs: source-lock `104959887288`; Python 3.11 `104959924421`; Python 3.13 `104959924158`; aggregate `104960607814`.
- Artifacts: py3.11 `10467510918` / `sha256:6240eeac4929b8b375f7f2f7d1cc2e98b734462a5975dc46204be09a9b9d97dc`; py3.13 `10467176707` / same digest; aggregate `10467640795` / `sha256:93aab926f9de411471061f80b87b30e1bb313523aed7a4b91bf47248b39fcbe5`.
- Independent decision SHA256: `3a35f63623e12ea5cf6cc5857fa599f2a60c9989187c718955721acc78158751`.
- Identity-map digest: `3335104f90e897232e81be2892339751de3b34b8fcf073af9fcd89660d074f20`.
- Aggregate SHA256: `f391d0b55c86c1ea35e1898d8b9e8633df581421019559dd54f7dd0b1f38128b`.

Green CI is provenance/execution evidence only; the classification below is taken from the independently identical frozen decision payloads and their aggregate.

## Terminal classification

`EQ4_TRIANGLE_WEDGE_GROUP_ARGUMENT_IDENTITY_PASS_SCOPED`

## Exact source-authorized identity ledger

For the fixed Eq.(4) triangle `(12,23,13)` in one gauge-fixed realization with `g1=1`:

- `G12 = g_2^{-1} g_1 = g_2^{-1}`;
- `G23 = g_3^{-1} g_2`;
- `G13 = g_3^{-1} g_1 = g_3^{-1}`.

The primary authority fixes the general ordered identity `g_ab = g_b^{-1} g_a`, Eq.(4) uses `1 <= a < b <= 5`, the orientation convention is `kappa_ab=sigma_a sigma_b`, and the one-wedge contact scalar uses `B_ab=B(z_ab,g_b^{-1}g_a)`.

All frozen essential identity fields are present. No historical V8 auxiliary relation, guessed textbook composition formula, or Toller-matrix composition is used.

## Controls

The positive source-authorized ledger fixture passes. Negative controls correctly reject/reclassify reversed multiplication, dropped inversion, wedge/contact relabeling, historical V8 substitution, and guessed Toller composition. Python 3.11 and 3.13 produce byte-identical scientific decision payloads.

## Scientific boundary

This PASS closes only the object-identity blocker. `transverse_rank=null` in this gate by design. No local-Lie transverse rank, physical transverse quotient, Jacobian/Haar/contact-normalization transport, or S3 differential transport is inferred here.

The earlier `EQ4_TRIPLE_CONTACT_COMMON_GROUP_VARIABLE_LIFT_BLOCKED_SCOPED` remains an immutable historical result for its then-frozen source extraction; its missing-map premise has subsequently been superseded by the independent Critic plus this source-authorized identity gate. It is not reinterpreted as physical/transversality FAIL.

## Next admissible gate

Prospectively freeze `SOURCE_J1_K5_EQ4_COMMON_LOCAL_LIE_PULLBACK_TRANSVERSE_RANK_GATE`. It must distinguish the raw local differential from any physical transverse quotient and must not promote raw Jacobian rank to physical transversality unless quotient and normalization transport are source-authorized.

Governance locks remain unchanged: `RQIR Core v1.0 = FROZEN`; `D7-S2 = NOT_CLOSED`; `D7-S3 = NOT_CLOSED`; `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`; Candidate Gravity inactive; selector labels remain unauthorized.

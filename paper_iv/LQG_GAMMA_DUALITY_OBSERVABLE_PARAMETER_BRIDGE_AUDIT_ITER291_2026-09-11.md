# Iter291 — LQG gamma-duality observable / parameter bridge

## Authority
Primary authority: Eugenio Bianchi and Monica Rincon-Ramirez, *Spinfoams, gamma-duality, and parity violation in primordial gravitational waves*, Physical Review D **113**, 124013 (published 2026-06-05), DOI `10.1103/qz89-26hk`, arXiv:`2403.06053`.

Peer-reviewed authority states that the Barbero-Immirzi parameter `gamma` is a coupling in EPRL spinfoam dynamics and can be interpreted as controlling gravitational parity violation through a duality rotation. In the authors' gamma-dual gravity+scalar EFT, `gamma` fixes a relation between parity-even and parity-odd higher-curvature couplings. For the inflationary realization studied there, primordial tensor circular polarization together with tensor tilt and tensor-to-scalar ratio provides an in-principle semiclassical inference route for `gamma`, hence for the discreteness scale.

## Prospectively frozen guards
Scientific workflow: `.github/workflows/lqg-gamma-duality-observable-audit.yml`.

Run `34568777275`, head `4b2212fe21830964b43fa8c0f9fabef842c6e6aa`:
- `authority` = PASS;
- `gamma_duality` = PASS;
- `eft_observable` = PASS;
- `transport_scope` = PASS;
- aggregate = SUCCESS after the explicit dependency barrier.

Summary artifact: `10186981524` (`lqg-gamma-duality-iter291-summary`), artifact digest `sha256:3ef255ea6377cc487447b5ac62df01c43e870ca1f9913e2f7bedbba165b714ad`.
Raw aggregate digest: `sha256:3b7f1797aa37d1722a3fce276520a7e7467c27f834823c6240764f1c32f727b0`.

Machine aggregate:
- `scoped_observable_parameter_bridge=true`;
- `semiclassical_gamma_observable_anchor=true`;
- `complete_stack_same_realization_uv_ir_transport_ready=false`;
- `normalized_observable_with_full_propagated_qg_error_ready=false`;
- `family_terminal=false`;
- `d7_authorized=false`.

## Frozen classification
`HIGH_VALUE_LQG_GAMMA_DUALITY_SEMICLASSICAL_OBSERVABLE_PARAMETER_BRIDGE__NO_COMPLETE_STACK_SAME_REALIZATION_UV_TO_IR_TRANSPORT`

This is a **scoped PASS** for an EPRL semiclassical parameter-to-observable bridge. It is not a family-level PASS and is not an equivalence/reduction map between the Iter287 complete-stack UV object and the Iter290 causal large-spin Regge endpoint.

The result materially sharpens the LQG blocker: absence of any semiclassical `gamma` observable is no longer a valid description. The still-missing object is the same-realization complete-stack transport law (or valid reduction/equivalence certificate) carrying stack coupling / `gamma` / spin-scale identity from the small-spin UV sector through the causal large-spin Regge/Einstein regime, with a normalized observable in a common comparator domain and propagated theory/resource uncertainty.

## D7 impact
- D7-S2 remains `NOT_CLOSED`.
- D7-S3 remains `NOT_CLOSED`.
- D7-S4 remains `PARTIAL_GLOBAL_NOT_CLOSED`.
- D7-S5 remains `NOT_AUTHORIZED`; no terminal classifier is run.
- Candidate Gravity remains inactive.
- Strict Tier-1 terminal count remains `1/15`.

No BLOCKED/PARTIAL state is converted to FAIL, and no scoped child result is promoted to family level.

# SOURCE_J1_COHERENT_MAGNETIC_TOLLER_BRIDGE_V3 — prospective freeze

Date: 2026-09-15
Status: `PROSPECTIVELY_FROZEN_BEFORE_IMPLEMENTATION_OR_RESULT`

## HYPOTHESIS

For the source-defined lowest-spin block `j=l=k=1`, real nonzero `rho`, and either Toller branch `sigma=+1` or `sigma=-1`, the coherent-basis Toller distribution used in the causal-spinfoam source is exactly the coherent-state basis transform of the magnetic-basis Toller matrix, with the same Feynman `i epsilon` projector and no residual phase mismatch. This gate tests only that one-wedge representation bridge.

## OBJECT

One source-defined wedge only. Frozen object:

- principal-series block `(rho,k)=(rho,1)` with `rho in R\{0}`;
- `j=l=k=1`;
- branch `sigma in {+1,-1}`;
- source wedge orientation `g_ab = g_b^{-1} g_a`;
- source wedge sign `sigma = sigma_a sigma_b`;
- coherent states and antilinear map `J` exactly as in the source spinor convention;
- magnetic Toller matrix and coherent Toller distribution obtained from the same Feynman projector.

No K5 contraction, no channel-`00000` coefficient, and no contact-survival/cancellation decision is part of this gate.

## DEPENDENCY

The immediately preceding repository-local authority-corpus gate `SOURCE_J1_K5_CONTACT_REPRESENTATION_DERIVATION_V2` is terminal `SOURCE_DERIVATION_BLOCKED_SCOPED` at Actions run `34952153723`, artifact `10389513085`, digest `sha256:ea9d904ebde54aad12dfb5bf1d21775dd2380d8b28fd377116e948dc933a9945`. Its exhaustive frozen corpus contained 57 files but no qualifying exact coherent-contact -> magnetic/intertwiner bridge and no exact coherent-contact coefficient. Missing bridge is not zero coefficient.

This V3 gate expands source authority to two primary 2026 papers by the same authors and tests only the missing one-wedge representation/convention bridge. It does not alter or rewrite the V2 result.

The running P1 mixed-Taylor method repair and Iter504 are independent; no partial values from them enter this gate.

## SOURCE / REALIZATION AUTHORITY

Primary source A:

- Eugenio Bianchi, Chaosong Chen, Mauricio Gamonal, `Causal spinfoam vertex for 4d Lorentzian quantum gravity`, arXiv:2601.23162v1.
- Frozen source equations/definitions: Eq. (3), Eq. (4), Appendix C Eq. (C2), Eq. (C4), Eq. (C5), and Appendix D Eq. (D1)-Eq. (D4).
- Required semantics: magnetic Toller Feynman `i epsilon` definition; wedge sign/orientation; source antilinear spinor map `J`; normalized coherent-state expansion in the magnetic basis; coherent Wigner matrix element; and the same Feynman prescription applied to that coherent matrix element, including the contact distribution.

Primary source B:

- Eugenio Bianchi, Chaosong Chen, Mauricio Gamonal, `Toller matrices and the Feynman i epsilon in spinfoams`, arXiv:2604.24945v1.
- Frozen source equations/definitions: Eq. (1)-Eq. (4), Eq. (13), Eq. (15)-Eq. (20), and the uniqueness statement immediately following Eq. (20).
- Required semantics: canonical magnetic basis; Cartan decomposition; Ruehl phase convention; explicit phase conversion; magnetic Toller reconstruction; additive split; Feynman projector acting on reduced Wigner matrices; uniqueness of the admissible Toller splitting.

The implementation must record these exact source IDs/equation selectors and canonical formula-string digests. It may use only exact symbolic algebra for the deciding controls.

## FROZEN BRIDGE IDENTITY

Let the normalized source coherent-state expansion at `j=1` be

`|1,zeta> = sum_{m=-1}^{1} c_m(zeta) |(rho,1);1,m>`.

Then the tested identity is

`T_coh^(sigma)(J xi, zeta; g) = sum_{p,n=-1}^{1} conjugate(c_p(J xi)) T_mag^(sigma)_{1p,1n}(g) c_n(zeta)`.

The identity is distribution-valued in the source sense: the Feynman projector acts linearly on the Wigner/Toller object, and the coherent coefficients are independent of the integration variable `tilde_rho` for fixed `j=1` and coherent labels.

The bridge must preserve source branch, orientation, normalization, basis ordering, `J`, and phase convention.

## FROZEN EXACT CONTROLS

1. `PHASE_TRIVIAL_J1`: prove symbolically from source-B Eq. (4) and `Gamma(conjugate(z))=conjugate(Gamma(z))` that for real `rho`, `Phi(rho;1,1)=1` exactly. A numerical sample is insufficient.
2. `COHERENT_J1_NORMALIZATION`: generate the exact `j=1` coefficients from source-A Eq. (C4) and verify exact unit normalization on frozen exact spinors `(1,0)`, `(0,1)`, `(1,1)`, `(1,i)`.
3. `COHERENT_SPAN`: exact coefficient vectors for frozen spinors `(1,0)`, `(0,1)`, `(1,i)` must have nonzero determinant, proving that the tested coherent states span the magnetic `j=1` block and exercise a complex phase.
4. `GENERIC_MATRIX_BASIS_TRANSFORM`: for a symbolic generic `3x3` magnetic matrix, direct bra/matrix/ket contraction must equal the frozen coefficient-sum bridge identity exactly.
5. `PROJECTOR_LINEARITY`: the implementation must verify algebraically that the coherent coefficients are independent of `tilde_rho`, and that distributing a formal linear Feynman projector through the nine magnetic terms gives the same symbolic coherent projection.
6. `SOURCE_ORIENTATION`: exact source tuple must be `(g_b^{-1} g_a, sigma_a sigma_b)`. A reversed `g_a^{-1} g_b` fixture and a sign-flipped fixture must be rejected.
7. `SOURCE_J_MAP`: use exactly `J(z0,z1)=(-conjugate(z1), conjugate(z0))`. A fixture with the first minus sign removed must change the `j=1` coefficient vector for a complex spinor and must be rejected.
8. `NEGATIVE_PHASE`: a deliberately injected nontrivial residual phase symbol, and a `j!=l` fixture, must not be classified as the source `j=l=1` trivial-phase bridge.
9. `ADDITIVE_GUARD`: generic symbolic branch matrices satisfying `T_plus+T_minus=D` must preserve the same equality after the coherent basis transform; a deliberately altered branch sign must fail.
10. `SOURCE_SELECTOR_LOCK`: all frozen source IDs/equation selectors and canonical formula-string digests must match exactly.

Any deciding floating-point approximation makes the implementation invalid.

## PASS

Classify `SOURCE_J1_COHERENT_MAGNETIC_TOLLER_BRIDGE_CONFIRMED_SCOPED` iff all source locks and all exact controls pass, including exact phase triviality in `j=l=1`, exact coherent normalization/span, exact generic matrix basis transform, exact projector linearity, and source orientation/`J`/branch preservation.

A PASS authorizes only a separate prospectively frozen exact K5 channel-`00000` coherent-contact contraction gate that consumes this bridge.

## BLOCKED / INVALID

Classify `SOURCE_J1_COHERENT_MAGNETIC_TOLLER_BRIDGE_CONVENTION_BLOCKED_SCOPED` if the primary-source equations leave a required phase, basis, orientation, normalization, `J`, or branch convention unresolved after exact transcription.

Classify `INVALID_IMPLEMENTATION` if any source selector/digest/control fails, if the bridge is inferred from a numerical sample rather than exact algebra, if `g_a^{-1}g_b` is substituted for `g_b^{-1}g_a`, if the source `J` map is changed, if a residual phase is silently set to one, or if the gate computes/promotes a K5 contact coefficient not frozen here.

`BLOCKED != FAIL`; absence of a bridge would not mean a zero contact coefficient.

## INTERPRETATION CEILING

PASS establishes only a source-authoritative one-wedge basis/convention bridge between the coherent `j=1` Toller distribution and the magnetic `j=1` Toller matrix. It does not establish:

- a channel-`00000` contact coefficient;
- contact survival or cancellation after K5 contraction;
- Eq. (4) distributional existence/nonexistence;
- ordinary/absolute convergence;
- model or family failure;
- D7-S2/S3/S4 closure;
- any terminal selector;
- Candidate Gravity activation.

Governance remains frozen: `RQIR Core v1.0 = FROZEN`; `D7-S2 = NOT_CLOSED`; `D7-S3 = NOT_CLOSED`; `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`; terminal selector labels remain forbidden; Candidate Gravity remains inactive; KMQGB remains downstream of pinned DSIR authority.

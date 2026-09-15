# SOURCE_J1_K5_HIGHEST_CONTACT_MAGNETIC_LEADING_TRANSFER_V4 — prospective freeze

Date: 2026-09-15
Status: `PROSPECTIVELY_FROZEN_BEFORE_V4_IMPLEMENTATION_OR_RESULT`

## HYPOTHESIS

For the source-defined `j=l=k=1`, real nonzero-`rho` Toller branches, the unique cubic `beta^-3` magnetic Laurent tensor at a one-wedge collision is exactly the magnetic image of the source highest coherent contact term `delta''(B)` from Appendix D, not an unrelated singular surrogate. If this identification is source-authoritatively established, then the already frozen exact K5 channel-`00000` contraction of the ten cubic tensors decides whether the **highest contact leading tensor** survives or cancels at the fixed generic full-collision tangent witness.

## OBJECT

The exact object is only the highest contact / leading-collision piece:

- source spin block `j=l=k=1`;
- `rho in R\{0}`;
- Toller branch sign `sigma in {+1,-1}`;
- one-wedge collision `g_beta -> identity` with positive boost radius `beta -> 0+` and fixed nonzero tangent direction;
- source coherent contact decomposition of arXiv:2601.23162v1 Appendix D;
- the unique `beta^-3` magnetic Laurent coefficient of the same source Toller branch;
- after the one-wedge identification is proved, the exact source-order K5 full-collision tangent points
  `X0=(0,0,0)`, `X1=(1,0,0)`, `X2=(0,1,0)`, `X3=(0,0,1)`, `X4=(1,1,1)`
  in the repository's zero-based K5 convention, and fixed intertwiner channel `00000`.

This gate does **not** multiply the singular distributions as a joint distribution and does not decide existence of the full Eq. (4) product.

## DEPENDENCY / AUTHORITY

1. Terminal V3 one-wedge source bridge:
   - classification `SOURCE_J1_COHERENT_MAGNETIC_TOLLER_BRIDGE_CONFIRMED_SCOPED`;
   - run `35017297255`;
   - aggregate artifact `10415708250`;
   - digest `sha256:09268182961e09b3413d13684526574c1924d6aa37f17b39a9d65477907cabc1`;
   - result commit `f98a2d41dc67db42ced6890179b3d09dbda0b885`.
2. Terminal V3K cross-paper scalar-projector verifier:
   - classification `SOURCE_J1_TOLLER_PROJECTOR_KERNEL_EQUIVALENCE_CONFIRMED_SCOPED`;
   - run `35017730315`;
   - artifact `10416047992`;
   - digest `sha256:bfa25bdfe600f090ca5f273c1797e8804b94dc190d5d68130466e692876ec292`;
   - result commit `8ee4f29d99419182a9506519007563ba452185b2`.
3. Primary source A: Bianchi–Chen–Gamonal, arXiv:2601.23162v1, especially Eq. (3), Eq. (17), Appendix C Eq. (C6)–Eq. (C9), Appendix D Eq. (D1)–Eq. (D4).
4. Frozen repository exact source formulas in `code/iter499_arb_core.py::source_coeffs`, independently locked by the prior source-formula lineage.
5. Exact j=1 intertwiner/tangent contraction machinery in `code/source_j1_full_collision_leading_certificate.py`. Its historical `11/24` result is a known control but must be recomputed by the V4 implementation; it may not be imported as a conclusion-bearing scalar.
6. Historical coherent-contact Hörmander result fixes the source `j=1` Appendix-D highest-contact coefficient as an independently derived control; V4 must rederive it from the source polynomial rather than merely read its result label.

Historical channel-transfer BLOCKED/INVALID results remain historical. V4 is a new prospectively frozen derivation chain enabled by V3/V3K; it does not rewrite them.

## SOURCE CONTACT DECOMPOSITION

For source `j=1`, Appendix D gives exactly

`Theta_(sigma,rho,1)[B] = theta(sigma B) + sigma delta^(rho,1)(B)`

with

`delta^(rho,1)(B) = sum_{n=0}^{2} c_(n+1)/(n+1)! * (-i)^(n+1) * delta^(n)(B)`.

From the exact source polynomial

`F_1(rho_tilde,rho) = rho_tilde(1+rho_tilde^2) / [rho(1+rho^2)]`

at `rho_tilde=rho`, rederive

- `c1=(1+3rho^2)/[rho(1+rho^2)]`,
- `c2=6/(1+rho^2)`,
- `c3=6/[rho(1+rho^2)]`.

Therefore the highest contact coefficient inside a branch is exactly

`K_contact^(sigma) = sigma * i/[rho(1+rho^2)]`

multiplying `delta''(B)`.

## FROZEN COLLISION-SCALING LEMMA

For a fixed nonzero pure-boost tangent direction and `beta -> 0+`, source Eq. (C7) has

`B(z,g_beta) = beta*b1(z,n) + O(beta^2)`

with nontrivial real `b1`. The remaining coherent-Wigner integrand is locally bounded on compact `CP^1` in this limit when kept in the source polynomial/integral combination.

Consequently, under pullback in the frozen collision scaling:

- the `theta(sigma B)` contribution has no negative cubic power;
- `delta(B)` can contribute at order no worse than `beta^-1`;
- `delta'(B)` can contribute at order no worse than `beta^-2`;
- `delta''(B)` can contribute at order `beta^-3`.

Thus, within the complete source split D1–D4 for `j=1`, any nonzero `beta^-3` coefficient is uniquely attributable to the highest `delta''(B)` contact term. This is an identification of the leading homogeneous source component, not a claim that the joint product of contact distributions exists.

## FROZEN MAGNETIC LAURENT TARGET

The implementation must independently rederive from the exact `j=1` source branch formulas, not from a stored conclusion, that with magnetic ordering `m=(-1,0,+1)` and

`A(rho)=3 i/[4 rho(1+rho^2)]`,

one has

`lim_(beta->0+) beta^3 t_plus(beta) = A(rho) diag(1,-2,1)`,

`lim_(beta->0+) beta^3 t_minus(beta) = -A(rho) diag(1,-2,1)`.

The scalar ratio must be established exactly:

`A(rho) / ( i/[rho(1+rho^2)] ) = 3/4`.

Combined with the frozen collision-scaling lemma and V3/V3K basis authority, this is the decisive one-wedge transfer statement: the magnetic cubic tensor is the image of the source highest `delta''` contact term.

For a general pure-boost tangent direction `n`, exact spin-1 covariance must map the spherical tensor to the Cartesian quadrupole

`Q(n) = I - 3 n n^T`.

## FROZEN K5 CONTRACTION

Only after all one-wedge transfer controls pass, construct for every K5 edge `(a,b)`

`n_ab = (X_a-X_b)/||X_a-X_b||`,
`Q_ab = I - 3 n_ab n_ab^T`,

and contract the ten `Q_ab` with the exact `j=1` intertwiners in channel `00000`.

The implementation must recompute the rational contraction from tensors. It must not read `11/24` from a result file. The branch signs are the source wedge signs `sigma_ab=sigma_a sigma_b`. Their ten-edge product must be derived graph-theoretically, not assumed.

## POSITIVE / NEGATIVE CONTROLS

1. `SOURCE_POLYNOMIAL`: exact symbolic differentiation of `F_1` reproduces `c1,c2,c3` and the branch highest-contact coefficient.
2. `MAGNETIC_LAURENT`: exact symbolic limits of all six source branch/magnetic components reproduce the frozen `±A*(1,-2,1)` pattern.
3. `UNIQUE_CUBIC_SOURCE`: exact power bookkeeping over the complete `j=1` Appendix-D split identifies `delta''` as the only source component allowed at `beta^-3`.
4. `SCALAR_TRANSFER`: exact ratio magnetic cubic/contact scalar is `3/4` for both branches after the outer source `sigma` sign is included.
5. `SPHERICAL_CARTESIAN`: exact frozen spherical-to-Cartesian spin-1 basis transform maps `diag(1,-2,1)` for the z-axis boost to `I-3 e_z e_z^T`, and exact rotation covariance gives `I-3nn^T`.
6. `K5_INTERTWINER_REGRESSION`: exact spherical/Cartesian intertwiner map and frozen norms pass.
7. `K5_CONTRACTION_RECOMPUTED`: channel `00000` angular contraction is computed from the ten tensors, not imported.
8. `BRANCH_PARITY`: derive exactly `product_(a<b)(sigma_a sigma_b)=product_a sigma_a^4=1` on K5 for every vertex-sign assignment.
9. `REMOVE_HIGHEST_CONTACT_NEGATIVE`: deleting `c3` / `delta''` while retaining lower contact and step pieces must make the frozen transfer chain reject any `beta^-3` attribution.
10. `WRONG_RATIO_NEGATIVE`: replacing `3/4` by `1` must be rejected exactly.
11. `WRONG_MAGNETIC_ORDER_NEGATIVE`: a fixture that moves the `-2` entry away from `m=0` must fail the exact spherical/Cartesian basis control.
12. `SYNTHETIC_CANCELLATION`: replacing one physical edge tensor by the exact zero tensor must make the same K5 contraction classifier reach the zero/cancellation branch.
13. `SCOPE_FIREWALL`: no distribution-product existence, ordinary/absolute convergence, D7 closure, terminal selector, or Candidate Gravity field may be inferred from the leading coefficient.

Any deciding floating approximation makes the gate `INVALID_IMPLEMENTATION`.

## PASS

Classify

`SOURCE_J1_K5_CHANNEL00000_HIGHEST_CONTACT_SURVIVES_LEADING_SCOPED`

iff all source/chronology locks and exact controls pass, the one-wedge cubic/contact identification is established, and the recomputed fixed-tangent channel-`00000` highest-contact leading coefficient is exactly nonzero.

A PASS establishes in particular that universal cancellation of the highest `delta''` contact tensor in this fixed channel/full-collision leading sector is false.

## FAIL

Classify

`SOURCE_J1_K5_CHANNEL00000_HIGHEST_CONTACT_CANCELS_LEADING_SCOPED`

iff all transfer/source controls pass but the exact recomputed physical channel-`00000` contraction is zero.

This is cancellation of the tested leading highest-contact component only, not model/family success or distributional existence.

## BLOCKED

Classify

`SOURCE_J1_K5_HIGHEST_CONTACT_MAGNETIC_TRANSFER_BLOCKED_SCOPED`

if source/chronology locks and implementation controls pass but the complete source D1–D4 split plus V3/V3K does not suffice to identify the magnetic `beta^-3` coefficient uniquely with the source `delta''(B)` component without an additional convention/theorem.

`BLOCKED != FAIL` and missing transfer != zero contraction.

## INVALID

Classify `INVALID_IMPLEMENTATION` if a source lock/control fails, historical `11/24` is imported instead of recomputed, `Q` is assumed to be the contact tensor without the frozen uniqueness chain, a floating approximation decides the result, or a lower-order/step component is silently promoted to `beta^-3`.

## INTERPRETATION CEILING

Even PASS establishes only survival of the **highest `delta''` contact leading homogeneous tensor** in fixed `j=1`, real nonzero-`rho`, channel `00000`, at the frozen generic full-K5 tangent witness. It does **not** establish:

- that the product of the ten contact distributions exists in `D'`;
- that the source Feynman regulator fails or succeeds jointly;
- absolute/ordinary convergence or divergence of the complete vertex by itself;
- survival of every lower contact/Laurent order;
- all channels, all spins, or all collision strata;
- model/family failure;
- D7-S2/S3/S4 closure;
- any terminal selector;
- Candidate Gravity activation.

Governance remains frozen: `RQIR Core v1.0 = FROZEN`; `D7-S2 = NOT_CLOSED`; `D7-S3 = NOT_CLOSED`; `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`; terminal selectors forbidden; Candidate Gravity inactive; KMQGB downstream of pinned DSIR authority.

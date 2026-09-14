# Iter492 preregistration — local angular tangent / boundary-layer scaling at the C-s4 NONDECAY center

Date frozen: 2026-09-14
Status: FROZEN BEFORE IMPLEMENTATION/PRODUCTION

## Parent authority
- Iter487/Iter489 authority: a valid one-dimensional shared-Haar NONDECAY center path exists on the frozen j=1 control layer.
- Iter491 authority: `SCIENTIFIC_FAIL_ITER491_ANGULAR_THICKENING_HP`; the four frozen nonzero constant angular radii `{0.0025,0.005,0.01,0.02}` do not preserve sampled NONDECAY across all causal classes.
- Iter491 run `34792644222`, aggregate artifact `10329135024`, digest `sha256:fb7881955756e63b309865f59ad3fa726641ed780c8d946dd805a1e69cf5e61f`.
- Current front explicitly forbids post-hoc shrinking of the Iter491 radius grid and permits only a new prospective local asymptotic/tangent-response gate with frozen directions/bases and an `eps -> 0` scaling law.

## Question
Does the central C-s4 NONDECAY exponent persist when a generic angular perturbation is forced to approach the center with rapidity according to a prospectively frozen boundary-layer law

`eps_q(R) = kappa * exp(-q R)`?

This is a local asymptotic diagnostic. It is designed to distinguish a fixed-angle unstable ridge from a center with a parametrically shrinking angular boundary layer. It is **not** an open-neighborhood or positive-measure certificate.

## Frozen source object
Unchanged from Iter491 except for the prospectively defined R-dependent angular amplitude below:
- panel `C`, strong regime;
- cluster size `s=4`, nodes 1..4 escaped together;
- `j=k=l=1` full ten-edge Toller/intertwiner network;
- rho witnesses `{0.35,0.9,1.6,2.7}`;
- causal patterns `{0to5,1to4,2to3}`;
- radial grid `R={6,8,10,12}`;
- same 20-D chart `g_a(delta;R)=L_a(delta_L) g_a^0(R) R_a(delta_R)`, with `L=Rx Ry Rz`, `R=Rx Ry`;
- all 243 genuine `3^5` four-valent intertwiner channels;
- same source radial Haar factor;
- high-precision node/edge construction and KAK machinery inherited from Iter491.

No source KAK replacement, determinant projection, scalar renormalization, fitted phase, independent-edge surrogate, artificial Haar suppression or modified spectral object is allowed.

## Frozen tangent directions
Coordinates are ordered by nodes 1..4, five chart coordinates per node. Eight deterministic integer sign directions are frozen and normalized by their Euclidean norm before use:

- `d0 = [+1,+1,+1,+1,+1,  +1,+1,+1,+1,+1,  +1,+1,+1,+1,+1,  +1,+1,+1,+1,+1]`
- `d1 = [+1,-1,+1,-1,+1,  -1,+1,-1,+1,-1,  +1,-1,+1,-1,+1,  -1,+1,-1,+1,-1]`
- `d2 = [+1,+1,-1,-1,+1,  +1,-1,-1,+1,+1,  -1,-1,+1,+1,-1,  -1,+1,+1,-1,-1]`
- `d3 = [+1,-1,-1,+1,+1,  -1,-1,+1,+1,-1,  -1,+1,+1,-1,-1,  +1,+1,-1,-1,+1]`
- `d4 = [+1,-1,+1,+1,-1,  +1,+1,-1,+1,-1,  +1,-1,+1,-1,+1,  -1,+1,-1,+1,+1]`
- `d5 = [+1,+1,-1,+1,-1,  -1,+1,+1,-1,+1,  +1,-1,+1,+1,-1,  -1,+1,-1,+1,+1]`
- `d6 = [+1,-1,-1,-1,+1,  +1,+1,-1,-1,-1,  -1,+1,+1,-1,-1,  -1,-1,+1,+1,-1]`
- `d7 = [+1,+1,+1,-1,-1,  -1,+1,+1,+1,-1,  -1,-1,+1,+1,+1,  +1,-1,-1,+1,+1]`

Both signs `+d` and `-d` must be evaluated. This prevents a one-sided directional artifact.

## Frozen epsilon scaling family
`kappa = 0.02`.

Five exponents are frozen before production:
`q = {0.50, 0.75, 1.00, 1.25, 1.50}`.

For each radial point, each sign and each direction,
`delta(R) = sign * d_hat * 0.02 * exp(-q*R)`.

The q-grid, kappa, directions, signs and R-grid cannot be modified after production. In particular, a failed q may not be rescued by adding a larger q post hoc within Iter492.

## Frozen numerical realization and controls
- Primary precision: 100 decimal digits for nodes, relative edges and KAK before conversion of bounded SU(2) factors/beta to the already-qualified spin-1 Toller network.
- Composite source parameters are frozen by the Iter491 float-repr -> mpf lift rule.
- High-precision node determinant residual `<1e-50`.
- High-precision relative-edge determinant residual `<1e-50`.
- High-precision KAK absolute reconstruction residual `<1e-50`.
- High-precision compact-factor unitarity/determinant residuals `<1e-50`.
- Shared-node K5 cycle residual `<1e-50`.
- Source-object identity after hp->complex128 against the same double chart formula `<1e-9` relative.
- At the unperturbed center, reproduce the frozen parent C-s4 slopes for each causal class within absolute error `<5e-3`.
- All contractions finite and strictly positive; source additive residual `<1e-9`; Haar bookkeeping residual `<1e-8`.
- Center chart tangent ranks must remain `[5,5,5,5]`.

Any failed required control makes the lane `INFRASTRUCTURE_OR_NUMERICAL_FAIL_ITER492` and forbids a science interpretation.

## Frozen observables
For every `(causal, direction, q, sign, rho)` evaluate the four R points using the R-dependent `eps_q(R)` and compute:
- `C_max(R,rho)=max_I |C_I|` over all 243 channels;
- source Haar log-factor from the actual high-precision node KAK rapidities;
- `log E = log C_max + log H`;
- late actual slope on `R={8,10,12}`;
- early actual slope on `R={6,8,10}`;
- slope drift = absolute difference of late and early actual slopes.

State:
- `NONDECAY` iff late actual slope `>= 0.00` and drift `<= 0.05`;
- `ROBUST` iff late actual slope `>= +1.00` and drift `<= 0.05`.

Per `(causal,direction,q)` lane, both signs and all four rho witnesses must be valid.
- `ITER492_TANGENT_ROBUST_LANE` iff all 8 sign×rho states are ROBUST.
- `ITER492_TANGENT_NONDECAY_LANE` iff all 8 are NONDECAY but at least one misses ROBUST.
- `SCIENTIFIC_FAIL_ITER492_TANGENT_LANE` iff valid but at least one sign×rho state is not NONDECAY.

Aggregate by q across all 3 causal patterns × 8 directions:
- q is `FULL_ROBUST` iff all 24 lanes are ROBUST;
- q is `FULL_NONDECAY` iff all 24 lanes are at least NONDECAY;
- otherwise q is `NOT_FULL_NONDECAY` if all lanes are valid.

Terminal Iter492 classification:
1. `ITER492_TANGENT_BOUNDARY_LAYER_BRACKET_QUALIFIED_SCOPED` iff all 120 lanes are valid and at least one q is FULL_NONDECAY while at least one smaller q is NOT_FULL_NONDECAY. Report the smallest frozen q with FULL_NONDECAY and do not interpolate beyond the frozen grid.
2. `ITER492_TANGENT_ALL_Q_NONDECAY_QUALIFIED_SCOPED` iff all 120 lanes are valid and every q is FULL_NONDECAY.
3. `SCIENTIFIC_FAIL_ITER492_TANGENT_BOUNDARY_LAYER` iff all 120 lanes are valid and no q is FULL_NONDECAY.
4. otherwise `INFRASTRUCTURE_OR_NUMERICAL_FAIL_ITER492`.

No monotonicity in q is assumed; all q states must be reported. A non-monotone pattern is itself a diagnostic and forbids interpolation.

## Interpretation ceiling
Even a qualified boundary-layer bracket is only finite-R, finite-direction evidence that the central NONDECAY path has a shrinking angular stability scale. It does **not** establish a fixed nonzero angular open set, positive Haar measure, or an absolute Haar-divergence theorem. An analytic/uniform neighborhood certificate would still be required for any positive-measure statement.

A scientific FAIL would mean that even the frozen `exp(-1.5 R)` approach does not preserve NONDECAY across the tested generic directions/causal classes on this frozen control layer. It would not prove an exact theorem about all tangent directions.

Ten source spectral integrations, conditional/PV cancellation, source-defined distributional amplitudes, D7-S3/D7-S4 and the physical causal vertex remain separate. D7-S2 remains NOT_CLOSED. Terminal D7 labels and Candidate Gravity authorization remain forbidden.
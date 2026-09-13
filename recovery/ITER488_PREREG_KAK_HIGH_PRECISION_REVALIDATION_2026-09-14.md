# Iter488 preregistration — high-precision KAK revalidation of Iter487 invalid lanes

Date frozen: 2026-09-14
Status: FROZEN BEFORE IMPLEMENTATION/PRODUCTION

## Parent authority
- Iter487 prereg: `5a7bc8e909bfa7a0b9a865a372e112eebe81654f`.
- Iter487 workflow head: `2af59f62b841b3cdf2731040968105c2edaac4a5`.
- Iter487 authoritative run: `34789538305`.
- Iter487 aggregate artifact: `10327910402`, digest `sha256:a17235d63f4f645a81bd2dc7222245724847e5c02530ab26cacb6675a877b467`.

The Iter487 aggregate is terminal `INFRASTRUCTURE_OR_SOURCE_FAIL_ITER487` because exactly five lanes fail only the inherited frozen `per_edge_kak_reconstruction < 1e-8` control: `C-s2-0to5`, `C-s2-2to3`, `C-s3-0to5`, `C-s3-1to4`, `C-s3-2to3`. Their scale-normalized G1 and base G2 controls pass. The observed failed KAK residuals are only about `1.33e-8` to `1.40e-8`, at large boosts where double-precision SVD reconstruction is ill-conditioned in absolute norm.

## Purpose
Determine whether those five failures are numerical decomposition precision failures or genuine violations of the same frozen KAK reconstruction predicate. No scientific slope, path, panel, rho, causal branch, threshold, source formula, Haar factor, or Iter487 classifier may be changed.

## Frozen audit object
For each of the five invalid Iter487 lanes, reconstruct exactly the same five shared nodes and ten edge matrices at the same `R={6,8,10,12}` using the existing Iter487/Iter486 node generator. For every edge matrix, perform an independent high-precision complex SVD/KAK decomposition at >=80 decimal digits on the *same double-precision edge matrix represented exactly as decimal real/imaginary entries*.

For `h = U diag(s1,s2) Vh`, split the determinant phase exactly as in Iter484 so that `U1,U2 in SU(2)` and `A=diag(exp(beta/2),exp(-beta/2))`, `beta=log(s1/s2)`.

## Frozen predicates
A lane is numerically REVALIDATED iff all of the following hold:
1. high-precision absolute KAK reconstruction max residual `< 1e-8` (the original Iter487 threshold; unchanged);
2. high-precision U1/U2 unitarity and determinant residuals `< 1e-30`;
3. high-precision decomposition is finite for all 40 edge/R objects;
4. rapidity agrees with the original double-precision KAK beta to relative error `< 1e-10` or absolute error `< 1e-10` when beta is near zero;
5. the lane identity is one of the exactly five preregistered invalid lanes and the frozen Iter487 raw artifact reports every other control PASS.

No lowering or reinterpretation of `1e-8` is permitted. If high precision still fails it, the lane remains invalid.

## Composite science rule
Iter488 does not recompute or alter Iter487 scientific slopes. It may only repair the numerical validity status of the five pinned raw Iter487 artifacts.

If all five lanes are REVALIDATED and the other 19 Iter487 lanes were already valid, then the Iter487 frozen aggregate scientific classifier is applied to the original 96 raw `(lane,rho)` states without modification:
- at least one stable `NONDECAY` -> `SCIENTIFIC_FAIL_ITER487_HAAR_ESCAPE_ACTUAL_ENVELOPE_REVALIDATED_BY_ITER488`;
- all DECAY -> corresponding qualified DECAY label;
- otherwise -> INCONCLUSIVE.

If any of the five lanes is not revalidated, Iter487 remains `INFRASTRUCTURE_OR_SOURCE_FAIL_ITER487` and no scientific verdict is promoted.

## Interpretation ceiling
A promoted NONDECAY result proves only failure of the frozen exponential absolute-envelope decay test along at least one one-dimensional shared-node escape path in this j=1 control layer. It is not an absolute Haar-divergence theorem. The next required gate is positive-measure angular-neighborhood thickening around a prospectively frozen valid NONDECAY witness, followed by uniform lower-bound/stability testing. Ten source spectral integrations and conditional/distributional cancellations remain separate.

D7-S2 remains NOT_CLOSED. Terminal D7 labels and Candidate Gravity remain forbidden/inactive.
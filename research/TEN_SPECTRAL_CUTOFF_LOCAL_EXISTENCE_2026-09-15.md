# Ten-spectral correlated kernel — cutoff-local existence decomposition

Date: 2026-09-15
Status: `DERIVED_KMQGB` local mathematical lemma only; no D7-S2 promotion

## Authority chain

This note consumes only already-established structure:

1. Iter468 pins the source-faithful formal object with ten independent wedge spectral variables and one correlated four-group kernel: `ITER468_EQ4_SOURCE_SPECTRAL_GROUP_CONTRACTION_OBJECT_PINNED_SCOPED`, run `34770144171`, artifact `10322025879`.
2. `research/TEN_SPECTRAL_TENSOR_PRODUCT_SOURCE_AUDIT_2026-09-14.md` at commit `7321c9b8a045a7d5018de97c7c7297c49e6ae548` establishes that the ten source-defined one-wedge boundary-value distributions form a well-defined separate-variable tensor product `T` before correlated group integration.
3. `recovery/ITER503V_PARALLEL_SPECTRAL_ADMISSIBILITY_SCAFFOLD_2026-09-15.md` separates absolute and distributional admissibility obligations and keeps collision/Haar exchanges open.

## Source object

Write the Iter468 formal kernel schematically as

`F(lambda,g) = boundary/intertwiner contraction of product_e D_e^(lambda_e,k_e)(g_b^-1 g_a)`

with `lambda in R^10` and four gauge-fixed group variables `g in G^4`, `G=SL(2,C)`.

Let `T = tensor_e T_e` be the ten-fold one-wedge boundary-value distribution on `R^10`.

## Cutoffs

Choose:

- `chi_Lambda(lambda) in C_c^infinity(R^10)`, a compact spectral cutoff;
- `psi_R(g) in C_c^infinity(G^4)`, a compact group/Haar cutoff;
- `theta_delta(g)`, a smooth factor whose support stays a positive distance from the selected K5 collision set inside the compact group patch.

Assume only the regular-region property appropriate to the source representation: on the compact set

`supp(chi_Lambda) x supp(psi_R theta_delta)`

the contracted integrand `F(lambda,g)` is smooth in `lambda` and `g`. No global decay or collision estimate is assumed.

Define

`C_{R,delta}(lambda) = integral_{G^4} psi_R(g) theta_delta(g) F(lambda,g) dg`

and

`phi_{Lambda,R,delta}(lambda) = chi_Lambda(lambda) C_{R,delta}(lambda)`.

## Lemma — cutoff-local pairing exists

Under the regular-region assumption above,

`phi_{Lambda,R,delta} in C_c^infinity(R^10)`.

Therefore the pairing

`A_{Lambda,R,delta} = <T, phi_{Lambda,R,delta}>`

is well-defined.

### Proof

The group integrand and every finite `lambda` derivative are continuous on a compact set. They are therefore bounded there, and the compactly supported Haar integral may be differentiated under the integral sign. Hence `C_{R,delta}(lambda)` is smooth on the spectral patch. Multiplication by `chi_Lambda` makes the result compactly supported and smooth in all ten independent spectral variables. By definition, the distribution `T in D'(R^10)` acts continuously on `C_c^infinity(R^10)`. Thus `A_{Lambda,R,delta}` exists. QED.

## What this removes as a blocker

The finite-cutoff compact regular core is not itself a distribution-product ambiguity. Once all three cutoffs are present and the source integrand is smooth on that compact regular patch, no arbitrary ordering of the ten spectral boundary values is required to define the local pairing.

This is a local existence statement only.

## Exact remaining removal problem

Recovering the physical uncut object now requires separate control of at least the following limits/operations:

### S — spectral cutoff removal

`Lambda -> infinity` requires a source-backed multiplier/test-function theorem or growth/decay bounds strong enough for the noncompact spectral kernel to lie in a space on which `T` acts continuously.

Status: `SPECTRAL_REMOVAL_OPEN`.

### H — noncompact Haar/group-tail removal

`R -> infinity` requires control of the four-group noncompact tails. The active D7-S2 Haar-escape numerical programme addresses evidence about this sector but does not by itself prove the ten-spectral distributional exchange theorem.

Status: `HAAR_TAIL_REMOVAL_OPEN`.

### C — collision cutoff removal

`delta -> 0` requires a correlated local bound or a valid microlocal product/pullback/pushforward theorem on every relevant K5 collision stratum. Iter461 is the frozen geometry-prioritization input for this task and must be consumed rather than duplicated.

Status: `COLLISION_REMOVAL_OPEN`.

### J — joint-limit / exchange compatibility

Even if S, H, and C each admit a limit in some sense, equality of different removal orders and identification with the source-defined correlated amplitude require a separate compatibility theorem or a single joint domination/continuity argument.

Status: `JOINT_LIMIT_COMMUTATION_OPEN`.

## Consequence for research scheduling

The correlated-kernel problem should be tracked as the tuple

`(local cutoff existence, S, H, C, J)`

with current status

`(PROVED_SCOPED, OPEN, OPEN, OPEN, OPEN)`.

This prevents two recurring overclaims:

1. a failure to control one removal cannot be called divergence of the full amplitude;
2. success of the Haar-tail numerical gate cannot silently close spectral-growth or collision-transversality obligations.

## Claim guards

- No absolute convergence theorem is claimed.
- No spectral-cutoff removal is claimed.
- No Haar-tail removal is claimed.
- No collision-cutoff removal is claimed.
- No interchange/order-independence of cutoff removals is claimed.
- `D7-S2 = NOT_CLOSED`, `D7-S3 = NOT_CLOSED`, `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`.
- No terminal D7 selector is authorized.
- Candidate Gravity remains inactive.

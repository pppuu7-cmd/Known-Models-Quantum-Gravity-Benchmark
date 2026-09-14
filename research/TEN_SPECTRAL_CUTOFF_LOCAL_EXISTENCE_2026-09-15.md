# Ten-spectral correlated kernel — cutoff-local existence decomposition

Date: 2026-09-15
Status: `DERIVED_KMQGB` local mathematical lemma only; no D7-S2 promotion

## Authority chain

This note consumes only already-established structure:

1. Bianchi–Chen–Gamonal, arXiv:2601.23162, Eq. (3) defines each Toller `T` through its one-wedge Feynman spectral boundary value and Eq. (4) then defines the causal vertex as the four-group integral of the product of ten already-defined `T` matrices.
2. Iter468 pins the formal **direct-substitution** object with ten independent wedge spectral variables and one correlated four-group kernel: `ITER468_EQ4_SOURCE_SPECTRAL_GROUP_CONTRACTION_OBJECT_PINNED_SCOPED`, run `34770144171`, artifact `10322025879`.
3. `research/TEN_SPECTRAL_TENSOR_PRODUCT_SOURCE_AUDIT_2026-09-14.md` at commit `7321c9b8a045a7d5018de97c7c7297c49e6ae548` establishes that the ten source-defined one-wedge boundary-value distributions form a well-defined separate-variable tensor product before correlated group integration.
4. `recovery/ITER503V_PARALLEL_SPECTRAL_ADMISSIBILITY_SCAFFOLD_2026-09-15.md` separates absolute and distributional admissibility obligations and keeps collision/Haar exchanges open.

## Two objects that must not be conflated

### A. Source-order causal vertex

The primary source order is

`one-wedge spectral boundary value -> T_e(g)`,

for each edge, followed by

`A_source = integral_{G^4} product_e T_e(g_b^-1 g_a) dg`.

Thus the original causal vertex does **not** require first constructing a group-integrated function of ten spectral variables. Its remaining existence/finiteness problem is the correlated four-group integral of the source-defined Toller functions, including noncompact Haar tails and K5 collision regions.

### B. Reordered/direct-substitution ten-spectral representation

If Eq. (3) is substituted into Eq. (4) before the group integral is performed, one obtains schematically

`A_reordered = <T, C>`

with ten independent spectral variables and

`C(lambda) = integral_{G^4} F(lambda,g) dg`.

Equality `A_reordered = A_source` is an **exchange/reordering theorem**. It is not automatic from the existence of the ten separate one-wedge boundary values.

The cutoff lemma below concerns this reordered/direct-substitution representation.

## Direct-substitution source object

Write the Iter468 formal kernel schematically as

`F(lambda,g) = boundary/intertwiner contraction of product_e D_e^(lambda_e,k_e)(g_b^-1 g_a)`

with `lambda in R^10` and four gauge-fixed group variables `g in G^4`, `G=SL(2,C)`.

Let `T = tensor_e T_e` be the ten-fold one-wedge boundary-value distribution on `R^10`.

## Cutoffs for the reordered representation

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

## Lemma — cutoff-local reordered pairing exists

Under the regular-region assumption above,

`phi_{Lambda,R,delta} in C_c^infinity(R^10)`.

Therefore the pairing

`A_{Lambda,R,delta} = <T, phi_{Lambda,R,delta}>`

is well-defined.

### Proof

The group integrand and every finite `lambda` derivative are continuous on a compact set. They are therefore bounded there, and the compactly supported Haar integral may be differentiated under the integral sign. Hence `C_{R,delta}(lambda)` is smooth on the spectral patch. Multiplication by `chi_Lambda` makes the result compactly supported and smooth in all ten independent spectral variables. By definition, the distribution `T in D'(R^10)` acts continuously on `C_c^infinity(R^10)`. Thus `A_{Lambda,R,delta}` exists. QED.

## What this removes as a blocker

The finite-cutoff compact regular core of the **reordered** representation is not itself a distribution-product ambiguity. Once all three cutoffs are present and the source integrand is smooth on that compact regular patch, no arbitrary ordering of the ten spectral boundary values is required to define the local pairing.

This is a local existence statement only.

## Correct separation of remaining problems

### Source-order physical vertex: H/C

For the original Eq. (4) source-order object, the unresolved existence/finiteness questions are dominated by:

#### H — noncompact Haar/group-tail control

The four-group integral of the product of ten source-defined Toller functions must be controlled as the group cutoff is removed.

Status: `SOURCE_ORDER_HAAR_TAIL_OPEN`.

#### C — collision-region control

The correlated K5 collision regions must be controlled either by source-faithful local integrability estimates or an appropriate distributional/microlocal theorem if singular products/pullbacks actually occur in the chosen representation.

Status: `SOURCE_ORDER_COLLISION_OPEN`.

A proof of H and C (with their compatibility) may establish the source-order causal vertex without ever treating `C(lambda)` as an ordinary uncut ten-spectral test function.

### Reordered/direct-substitution representation: S/H/C/J

To justify the fully uncut direct-substitution representation `<T,C>` and identify it with the source-order vertex, the following additional obligations remain.

#### S — spectral admissibility/removal

The uncut correlated spectral kernel must lie in a function/multiplier class on which the ten-fold boundary-value distribution acts continuously. `research/TEN_SPECTRAL_TEMPERED_SUFFICIENT_CLASS_2026-09-15.md` gives `C in S(R^10)` as one concrete sufficient target, not as a proved property.

Status: `REORDERED_SPECTRAL_ADMISSIBILITY_OPEN`.

#### H — group-tail control under the reordered construction

The group integral defining `C(lambda)` needs sufficient noncompact-tail control, with the uniformity/seminorm bounds required by the spectral pairing.

Status: `REORDERED_HAAR_TAIL_OPEN`.

#### C — collision control under the reordered construction

The same correlated collision geometry must be handled with bounds/transversality strong enough for the ten-spectral distributional pairing.

Status: `REORDERED_COLLISION_OPEN`.

#### J — exchange/equality theorem

One must prove that the reordered/direct-substitution construction equals the primary source-order causal vertex. This may follow from a sufficiently strong Fubini/Tonelli/dominated-convergence theorem or from a named distributional continuity theorem, but it cannot be inferred merely from separate-variable tensor-product existence.

Status: `SOURCE_REORDERING_EQUIVALENCE_OPEN`.

## Consequence for research scheduling

Track two ledgers, not one:

1. **source-order existence ledger**: `(H_source, C_source, compatibility_source)`;
2. **reordered spectral ledger**: `(local cutoff existence, S, H, C, J)`.

Current scoped status is

- source order: `(OPEN, OPEN, OPEN)`;
- reordered representation: `(PROVED_SCOPED, OPEN, OPEN, OPEN, OPEN)`.

This prevents two opposite overclaims:

1. failure to prove spectral admissibility of the reordered representation is **not** by itself failure of the source-defined vertex;
2. existence of the source-order group integral, if later proved, would **not** automatically justify a particular reordered ten-spectral/Fubini representation.

## Relation to active Iter504

Iter504 probes the source-order Toller/Haar escape sector numerically on its frozen q=1 continuous max-envelope domain. Even a strong Iter504 result does not prove absolute four-group convergence/divergence, but it is conceptually attached to the source-order H sector, not contingent on proving the reordered ten-spectral representation first.

## Claim guards

- No source-order Haar convergence or divergence theorem is claimed.
- No physical collision theorem is claimed.
- No reordered spectral-admissibility theorem for the physical `C` is claimed.
- No interchange/equality of source order and direct-substitution order is claimed.
- `D7-S2 = NOT_CLOSED`, `D7-S3 = NOT_CLOSED`, `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`.
- No terminal D7 selector is authorized.
- Candidate Gravity remains inactive.

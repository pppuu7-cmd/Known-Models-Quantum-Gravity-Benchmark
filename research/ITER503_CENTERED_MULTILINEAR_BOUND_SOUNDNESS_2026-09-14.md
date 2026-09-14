# Iter503 centered-multilinear bound soundness audit — 2026-09-14

Status: **mathematical/method audit only; no production verdict and no classifier change**.

This note audits the already-frozen Iter503 formula while authoritative run `34862605028` is in progress. It does not change the preregistration, code, domain, thresholds, or interpretation rules.

## 1. Same scalar network object

For a fixed recoupling channel `I`, the j=1 five-node K5 contraction has the form

`C_I(M_1,...,M_10) = sum_mu c_{I,mu} product_{e=1}^{10} (M_e)_{mu_e}`,

where `c_{I,mu}` is the product of the five fixed intertwiner entries selected by the magnetic assignment `mu`. Each edge matrix occurs exactly once. Hence `C_I` is separately multilinear in all ten edge matrices.

The legacy point evaluator may normalize each edge as `M_e=n_e Mhat_e` and restore `sum_e log(n_e)`. Multilinearity gives exactly

`C_I(M_1,...,M_10) = (product_e n_e) C_I(Mhat_1,...,Mhat_10)`.

Therefore the Iter501/502/503 unnormalized direct contraction is the same scalar envelope, not a changed physics object.

## 2. Entrywise interval radii are safe

Let `A` be one frozen scalar-amplitude interval and `a0` its midpoint. The existing factorized-KAK construction provides complex interval matrices `M_e(A)` containing every actual source matrix `M_e(a)` for `a in A`, and a degenerate-midpoint enclosure `M_e^0` containing `M_e(a0)`.

Define entrywise

- `B_e = abs_upper(M_e^0)`,
- `R_e = abs_upper(M_e(A)-M_e^0)`.

For every `a in A`, interval inclusion implies

`|M_e(a0)| <= B_e`,

`|M_e(a)-M_e(a0)| <= R_e`

entrywise. Loss of shared dependency between `M_e(A)` and `M_e^0` can enlarge `R_e`; it cannot invalidate this inequality.

## 3. Multilinear variation theorem used by Iter503

Write

`M_e(a) = M_e(a0) + delta_e(a)`.

By multilinearity,

`C_I(M(a)) - C_I(M(a0))`

is the sum over all nonempty subsets `S` of the ten edges of the term obtained by inserting `delta_e` on edges in `S` and `M_e(a0)` on the complementary edges.

Define `A_I(X_1,...,X_10)` by taking the same tensor-network incidence and replacing every intertwiner coefficient by its absolute value and every edge entry by a nonnegative entry bound. This map is nonnegative and separately multilinear. Therefore the triangle inequality gives

`|C_I(M(a))-C_I(M(a0))|`

`<= sum_{empty != S subset E} A_I(R_S,B_{E\S})`

`= A_I(B_1+R_1,...,B_10+R_10)-A_I(B_1,...,B_10)`.

Thus the frozen Iter503 quantity

`Delta_I = upper(A_I(B+R)-A_I(B))`

is a rigorous variation upper bound whenever the underlying interval edge enclosures and nonnegative contractions are valid.

## 4. Channel and max-envelope bounds

For each channel,

`L_I = max(0, abs_lower(C_I(M^0))-Delta_I)`,

`U_I = abs_upper(C_I(M^0))+Delta_I`

satisfy

`L_I <= |C_I(M(a))| <= U_I`

for every `a in A`. Consequently

`L=max_I L_I <= max_I |C_I(M(a))| <= max_I U_I=U`.

No unique maximizing channel is used. In particular, the Iter498 `195 -> 222` crossing is compatible with the bound and requires no branch selection.

## 5. What this audit does not establish

This soundness proof does not show that the bound is numerically sharp enough to have `L>0`; it only shows that a positive bound, if produced with the frozen controls passing, is mathematically conservative. It does not establish point-slope containment, NONDECAY, a continuous multidimensional angular neighborhood, positive Haar measure, spectral admissibility, or a physical causal-vertex theorem.

The authoritative Iter503 PASS/INSUFFICIENT/VALIDATION_FAIL classification remains solely determined by the prospectively frozen workflow artifacts.
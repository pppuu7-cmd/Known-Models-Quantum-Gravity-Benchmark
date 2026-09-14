# Ten-spectral Toller kernel — tempered-distribution sufficient pairing class

Date: 2026-09-15
Status: `DERIVED_KMQGB` mathematical lemma; no D7-S2 promotion

## Source authority

Primary source: Bianchi–Chen–Gamonal, *Toller matrices and the Feynman i-epsilon in spinfoams*, arXiv:2604.24945v1.

The source defines

`P_jl(rhot;rho) = product_{n=0}^{j+l} [i rhot - (n-j)]/[i rho - (n-j)]`

and explicitly states

- `P_jl(rho;rho)=1`;
- `P_jl(rhot;rho)=O(|rhot|^(j+l+1))`;
- the Feynman functional is
  `I_eps^(±)[f] = int_R [d rhot/(2 pi i)] [± P_jl(rhot;rho)/(rhot-rho ∓ i eps)] f(rhot)`;
- the `eps -> 0+` boundary value projects onto the corresponding Toller branch.

The existing repository audit `research/TEN_SPECTRAL_TENSOR_PRODUCT_SOURCE_AUDIT_2026-09-14.md` already proves that ten independent one-wedge source-defined boundary values form a well-defined separate-variable tensor product before correlated group integration.

## Lemma 1 — one-wedge Feynman kernel is tempered

For fixed finite representation labels `(j,l,rho)`, define the scalar source kernel distribution

`W_±(rhot) = bv_{eps->0+} [ ± P_jl(rhot;rho) / (2 pi i (rhot-rho ∓ i eps)) ]`.

Then

`W_± in S'(R)`.

### Proof

The standard real-line Feynman boundary value `bv 1/(x-rho ∓ i0)` is a linear combination of the principal-value distribution `PV 1/(x-rho)` and a delta distribution at `rho`. Both are tempered distributions.

For fixed finite `j,l`, `P_jl(x;rho)` is a polynomial of finite degree `j+l+1`. Multiplication of a tempered distribution by a polynomial preserves temperedness. The delta part is also harmless because the source identity `P_jl(rho;rho)=1` fixes its finite coefficient. Hence `W_±` is tempered. QED.

No contour closure, absolute integrability, or group-variable estimate is used in this lemma.

## Lemma 2 — the ten-wedge source boundary-value tensor product is tempered

For the ten K5 wedges let `W_e` be the corresponding fixed one-wedge source kernels above. Then

`W = tensor_{e in E(K5)} W_e in S'(R^10)`.

### Proof

The tensor product of finitely many tempered distributions is a tempered distribution on the product space. Apply this iteratively to the ten independent spectral coordinates. QED.

This strengthens the existing `D'(R^10)` statement to a concrete tempered-distribution statement for the source Feynman kernels.

## Corollary — a source-faithful sufficient class for spectral-cutoff removal

Let the correlated four-group contraction, after whatever group/collision operations have independently been justified, define a function `C(lambda_1,...,lambda_10)`.

If

`C in S(R^10)`,

then the uncut spectral pairing

`<W,C>`

exists canonically and continuously, with no arbitrary ordering of the ten spectral integrals and no spectral compact-support cutoff required.

More generally, any explicitly proved continuous multiplier/test-function class embedded in the domain of `W` is sufficient, but the Schwartz condition is now a concrete source-compatible sufficient target.

## What this does NOT prove

This note does **not** prove that the physical correlated kernel `C` belongs to `S(R^10)`.

In particular, the primary Toller source gives polynomial boundedness / explicit spectral analytic structure of individual representation factors, but that alone does not establish joint rapid decay of the four-group contracted kernel in all ten independent spectral variables.

Therefore the physical spectral-removal status remains:

`SPECTRAL_REMOVAL_OPEN`.

The open task is sharpened from

> find some admissible spectral function space

to the concrete disjunction

1. prove `C in S(R^10)` after the required group/collision operations; or
2. identify and prove a weaker weighted/multiplier space on which the explicit finite-order tempered distribution `W` acts continuously.

## Finite-order / growth consequence to exploit next

Because each one-wedge kernel is obtained from `PV(1/(x-rho))` and `delta(x-rho)` by multiplication by a finite-degree polynomial, the spectral obstruction is finite-order/polynomial rather than an undefined exotic distributional singularity.

A future weighted-space theorem should therefore track explicitly:

- polynomial degrees `j_e+l_e+1` from the ten `P_{j_e l_e}` factors;
- the finite distributional order associated with the ten principal-value factors;
- joint spectral decay/growth of the correlated kernel and the derivatives needed by those finite-order seminorms.

This bookkeeping may yield a weaker sufficient class than full Schwartz decay without changing the source object.

## Independence from Haar/collision problems

Temperedness of `W` does not justify the four noncompact group integrations and does not remove K5 collision singularities. The current correlated-kernel status remains

`(cutoff-local existence, spectral removal, Haar-tail removal, collision removal, joint-limit compatibility)`

`= (PROVED_SCOPED, OPEN, OPEN, OPEN, OPEN)`.

A Schwartz theorem for the already group-integrated `C` would close only the spectral pairing component appropriate to its hypotheses; the group/collision construction of `C` must itself first be legitimate.

## Claim guards

- No absolute convergence theorem is claimed.
- No physical spectral-cutoff removal is claimed yet.
- No Haar-tail or collision-cutoff removal is claimed.
- No Fubini/Tonelli exchange with the four group integrations is claimed.
- `D7-S2 = NOT_CLOSED`, `D7-S3 = NOT_CLOSED`, `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`.
- No terminal D7 selector is authorized.
- Candidate Gravity remains inactive.

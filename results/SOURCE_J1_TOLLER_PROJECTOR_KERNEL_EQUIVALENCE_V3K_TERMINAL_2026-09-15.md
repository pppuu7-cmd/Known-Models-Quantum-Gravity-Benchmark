# SOURCE_J1_TOLLER_PROJECTOR_KERNEL_EQUIVALENCE_V3K — terminal result

Date: 2026-09-15
Status: `TERMINAL_SCOPED`
Classification: `SOURCE_J1_TOLLER_PROJECTOR_KERNEL_EQUIVALENCE_CONFIRMED_SCOPED`

## Authority

- prereg commit: `d9b95dee3f090f828eb54cfed4432fb20f13a625`
- implementation commit: `a853946dc0ba28fb18e80cab65f15d7ddea6cd9d`
- workflow launch commit: `38bc424505ae9ee1762d0127ab6deefc50aa18d9`
- authoritative run: `35017730315`
- exact verifier job: `104545312480`
- artifact: `10416047992`
- artifact digest: `sha256:bfa25bdfe600f090ca5f273c1797e8804b94dc190d5d68130466e692876ec292`

## Frozen exact result

All controls passed. Using only Gamma recurrence `Gamma(z+1)=z Gamma(z)`, the arXiv:2601.23162v1 Eq. (3) `j=l=1` gamma-ratio kernel reduces exactly to the same meromorphic rational function as the arXiv:2604.24945v1 Eq. (20) finite product.

With `x=i*tilde_rho` and `y=i*rho`, both kernels reduce to

`x(1-x^2) / [ y(1-y^2) ]`.

The exact cross-multiplied difference is `0`.

Negative controls passed:

- deleting the middle `n=1` product factor gives a nonzero exact difference;
- replacing the frozen `j+l=2` product range by a two-factor `j+l=1` fixture gives a nonzero exact difference.

## Consequence

The independent V3K verifier removes the cross-paper scalar-projector-kernel ambiguity identified during adversarial review of the terminal V3 bridge. Together with terminal V3, it authorizes prospectively freezing the next exact K5 channel-`00000` coherent-contact contraction gate.

## Interpretation ceiling

This proves only exact equality of the scalar one-wedge Feynman projector kernels in the frozen `j=l=1` scope. It is not by itself a full bridge proof, K5 contact result, distributional existence/nonexistence result, D7 closure, terminal selector, or Candidate Gravity result.

Governance remains unchanged.

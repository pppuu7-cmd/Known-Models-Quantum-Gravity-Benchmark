# SOURCE_J1_TOLLER_PROJECTOR_KERNEL_EQUIVALENCE_V3K — prospective verifier

Date: 2026-09-15
Status: `PROSPECTIVELY_FROZEN_BEFORE_IMPLEMENTATION_OR_RESULT`

## HYPOTHESIS

For the frozen lowest-spin block `j=l=k=1`, the gamma-ratio Feynman projector kernel used in Bianchi–Chen–Gamonal, arXiv:2601.23162v1 Eq. (3), is exactly identical as a meromorphic function of `(tilde_rho,rho)` to the finite-product kernel used in Bianchi–Chen–Gamonal, arXiv:2604.24945v1 Eq. (20). Therefore the cross-paper one-wedge bridge does not hide an extra scalar normalization or phase in the projector kernel.

## OBJECT

Only the scalar kernel multiplying the same reduced/magnetic Wigner matrix in the Feynman spectral integral. Freeze `j=l=1`; `rho` and `tilde_rho` are symbolic complex variables away from poles. No coherent-state coefficient, Toller branch value, K5 contraction, contact coefficient, numerical amplitude, or D7 verdict is part of this verifier.

## SOURCE AUTHORITY

Source A: arXiv:2601.23162v1 Eq. (3), kernel

`F_A = Gamma(-1-i*rho) Gamma(2-i*tilde_rho) / (Gamma(-1-i*tilde_rho) Gamma(2-i*rho))`.

Source B: arXiv:2604.24945v1 Eq. (20), `j=l=1`, kernel

`F_B = product_{n=0}^{2} (i*tilde_rho-(n-1))/(i*rho-(n-1))`.

Allowed identity: Gamma recurrence `Gamma(z+1)=z Gamma(z)` only. No numerical fitting.

## EXACT CONTROLS

1. Rewrite `Gamma(2-x)/Gamma(-1-x)` by three recurrence steps and derive exactly `x(1-x^2)`.
2. Apply the same identity to the `rho` denominator.
3. Derive `F_A = x(1-x^2)/(y(1-y^2))`, where `x=i*tilde_rho`, `y=i*rho`.
4. Expand the source-B product and derive exactly the same rational function.
5. Exact symbolic difference must be zero after cross multiplication.
6. Negative fixture: delete the middle `n=1` factor from `F_B`; exact cross-multiplied difference must be nonzero.
7. Negative fixture: set `j+l=1` product range; it must not classify as the frozen `j=l=1` kernel.

## PASS

`SOURCE_J1_TOLLER_PROJECTOR_KERNEL_EQUIVALENCE_CONFIRMED_SCOPED` iff all exact controls pass.

## INVALID

`INVALID_IMPLEMENTATION` if any deciding control uses floating-point approximation, a source kernel is transcribed differently, or a negative fixture is accepted.

## INTERPRETATION CEILING

PASS establishes only exact equality of the two scalar one-wedge Feynman projector kernels in the frozen `j=l=1` block. It does not establish the full coherent↔magnetic bridge by itself, any contact coefficient, K5 survival/cancellation, distributional existence, D7 closure, terminal selector, or Candidate Gravity activation.

This verifier is outcome-independent of the already-running V3 bridge gate and does not modify its frozen contract. Governance remains unchanged.

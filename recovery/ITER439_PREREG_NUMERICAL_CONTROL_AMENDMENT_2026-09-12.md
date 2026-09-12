# Iter439 preregistration numerical-control amendment — 2026-09-12

This amendment is frozen **before creation/launch of the Iter439 calculation workflow**. It changes numerical adequacy thresholds only; the source equation, spin/gamma matrix, beta grid, physical question, classifications, scope guard, and all RQIR/D7 statuses remain unchanged.

## Why an amendment is required

A static preflight of the already-frozen Eq. (46) hypergeometric series shows that the originally written absolute tail controls in `ITER438_RESULT_AND_ITER439_PREREG_TOLLER_FINITE_BETA_2026-09-12.md` are inconsistent with the frozen final rapidity `beta=10` for the largest source parameters. The first hypergeometric correction is proportional to `z=exp(-20)` times the finite coefficient `a*b/c`; for the frozen `j=5`, extremal-m branch this naturally leaves a correction of order `2.3e-8`. Thus requiring `|R(10)-1| <= 1e-10` would classify the exact source formula as a numerical-control failure even when the implementation is correct.

No Actions lane for Iter439 has been launched and no scientific classification has been observed at the time of this amendment.

## Superseding numerical thresholds

Items 1–3 and 6 of the original Iter439 frozen controls remain unchanged.

Original item 4 is superseded by:

4. `|R(10)-1| <= 5e-8`.

Original item 5 is superseded by:

5. the last-pair effective exponent

   `alpha_eff(8,10) = alpha - [log R(10) - log R(8)] / 2`

   must satisfy `|alpha_eff-alpha| <= 1e-6`.

The standard-vs-tight complex-series agreement remains `<= 5e-12` on the full beta grid.

These thresholds are numerical realization controls only. They are not causal-vertex convergence criteria and they must not be interpreted as evidence for or against full noncompact integrability.

## Frozen anti-post-hoc rule

After this amendment, Iter439 controls are frozen. If a lane fails, the aggregate is `CONTROL_INVALID`; thresholds must not be loosened on the basis of its output. Any further numerical-design correction requires a new numbered iteration or an explicitly separated failed-control record.
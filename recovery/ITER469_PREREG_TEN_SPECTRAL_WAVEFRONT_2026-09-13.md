# Iter469 preregistration — ten-spectral Plemelj tensor-product wavefront locality

Date: 2026-09-13
Status: FROZEN BEFORE IMPLEMENTATION
Parent main: `b5aeab93105dabb20f12963cd890767e0f865fb8`

## Question
For the exact Iter468 source object with ten distinct spectral coordinates `x_e = rhot_e-rho_e`, is the local product of the ten one-dimensional Feynman/Plemelj boundary-value distributions obstructed by a Hörmander wavefront collision, or is the remaining D7-S2 blocker global/noncompact rather than local product definition?

## Frozen mathematical model
Each wedge distribution is the one-dimensional boundary value `u_e(x_e)=1/(x_e - i*kappa_e*0)` pulled back by the coordinate projection `pi_e:R^10->R`. Its singular conormal direction is supported on `x_e=0` with covectors proportional to the coordinate basis covector `e_e^*`. The source uses ten distinct coordinates from Iter468; no equality constraints between them are allowed.

## Frozen streams
A. Exact coordinate-conormal audit: for every nonempty subset of the 10 wedges and every sign assignment, test whether a sum of nonzero conormals supported on distinct coordinate axes can vanish. Expected: no zero sum.

B. Exact invertible-basis robustness: apply a frozen panel of unimodular 10x10 integer basis changes and verify the zero-sum obstruction status is invariant.

C. Collision negative controls: identify pairs/sets after deliberately collapsing two spectral variables onto the same coordinate and verify opposite conormals can cancel, demonstrating the audit detects a genuine shared-variable wavefront collision.

D. Source-kernel scope check: record that multiplication by the common group-contraction kernel is locally admissible only under the explicitly frozen condition that the kernel is smooth in all ten spectral variables at fixed group variables. No claim about decay, group integration, or global pairing is permitted.

## PASS rule
PASS iff A and B find no local zero-sum wavefront collision for the ten distinct source coordinates, C detects the deliberate shared-variable collision, and D preserves the smooth-kernel scope lock.

PASS label: `ITER469_TEN_SPECTRAL_PLEMEJ_LOCAL_PRODUCT_WAVEFRONT_QUALIFIED_SCOPED`.

## Scope guards
PASS means only that the ten distinct spectral boundary values form a locally well-defined tensor-product/pullback distribution under the frozen coordinate model. It does not prove global spectral convergence, justify exchanging spectral/group integrations, establish decay of the group-contraction kernel, prove the SL(2,C) group integral exists, or close D7-S2. The next blocker would be global source-kernel growth/pairing/integrability. Terminal D7 labels remain forbidden and Candidate Gravity remains inactive.
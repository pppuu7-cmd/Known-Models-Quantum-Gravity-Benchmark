# Recovery Delta 004 — f(R) C0 quotient and representation-equivalence result

Date: 2026-09-08
KMQGB iteration: 004

## Active target

`KMQGB-M05-FR / FR-R2-MINK-001`

Action:

`S=(M_Pl^2/2) int sqrt(-g)[R+R^2/(6M^2)] + S_m`, with `M^2>0`.

## Newly frozen observable

Weak-field metric convention:

`ds^2=-(1+2Phi)dt^2+(1-2Psi)dx^2`.

For a localized traceful source:

`Phi=-G m_s/r [1+(1/3)e^{-Mr}]`,

`Psi=-G m_s/r [1-(1/3)e^{-Mr}]`.

Define

`gamma(r)=Psi/Phi=(3-e^{-Mr})/(3+e^{-Mr})`.

GR/C0 gives `gamma=1`.

Exact C0 residual:

`Delta_gamma(r)=-2e^{-Mr}/(3+e^{-Mr})`.

Common `G`, source mass and `1/r` normalization cancel identically. This closes the simplest source-amplitude/calibration degeneracy against C0.

Limits:
- `Mr -> infinity`: GR recovery, residual `0`;
- `Mr -> 0`: `gamma -> 1/2`, residual `-1/2`.

## Radial-shape relation

`e^{-Mr}=3(1-gamma)/(1+gamma)`

so

`ln[3(1-gamma(r))/(1+gamma(r))]=-Mr`.

Thus the ideal response has a one-parameter exponential radial shape with fixed f(R) scalar amplitude.

## Representation-equivalence result

Metric f(R) is dynamically equivalent to a scalar-tensor representation with Brans-Dicke parameter `omega_BD=0` and the corresponding mapped scalar potential/matter coupling.

This is not an experimentally distinguishable pair of theories; it is the same physical dynamics in different variables when the mapping is complete.

Queue rule added: M06 must use a genuinely nonduplicate scalar-tensor/Brans-Dicke realization rather than re-testing the exact f(R)-equivalent `omega_BD=0` rewrite.

## Remaining blocker

`FR_BROADER_COMPARATOR_QUOTIENT`:

1. compare `gamma(r)` and the radial shape against a generic scalar/Yukawa nuisance;
2. compare against a nonduplicate scalar-tensor family;
3. separate true physical degeneracy from exact field-redefinition identity;
4. map low-q response against C5/higher-curvature EFT directions;
5. then assign terminal M05 status.

## Progress

- terminal queue coverage: `4/9 = 44.44%`;
- M05 operational task completion: approximately `70%`;
- external RQIR Candidate Gravity readiness: `24%` and separate from KMQGB;
- no KMQGB heavy job launched while external RQIR rank10 remains active.

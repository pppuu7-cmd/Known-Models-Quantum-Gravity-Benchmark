# Iter505 preregistration — finite-t asymptotic regression repair

**Prospectively frozen after consuming Iter504 and before Iter505 production evidence.**

## Purpose
Iter504 was blocked solely by its finite-t source regression: all 18 lanes had valid source/geometry/SU(2)/homogeneity/intertwiner/reindex/zero-edge controls and nonzero leading witnesses, while the fine regression errors at t=5e-4 were 0.0143–0.0199 and every lane refined in the correct direction. Iter505 repairs only that numerical-control resolution. It does not weaken any scientific threshold or change the physical object.

## Frozen scope
Reuse Iter504 without modification for panels T0/T1/T2, causal classes 0to5/1to4/2to3, rho 7/8, all ten K5 edges, the same j=1 source coefficients B_m=C_m^(src)/8, the same 243 intertwiner channels, the same witness threshold 1e-12, and the same fixed-causal no-branch-sum contraction.

Only the finite-t regression points are changed prospectively to
- t_coarse = 1.25e-4
- t_fine = 6.25e-5
with the same frozen requirements:
- every fine per-edge relative Frobenius error < 5e-3;
- every fine error <= 0.75*coarse error + 1e-10;
- KAK reconstruction residual < 1e-10.

This is a numerical-resolution repair justified by the observed first-order refinement trend; the 5e-3 criterion is unchanged.

## Frozen classifications
PASS: `ITER505_FINITE_T_ASYMPTOTIC_REGRESSION_REPAIR_QUALIFIED_SCOPED` iff all 18 lanes are valid under the unchanged Iter504 controls and every lane has max_I R_I > 1e-12.

SCIENTIFIC FAIL: `SCIENTIFIC_FAIL_ITER505_UNIFORM_FROZEN_FULL_COLLISION_LEADING_SURVIVAL` iff all controls are valid but at least one lane has max_I R_I <= 1e-12.

BLOCKED: `BLOCKED_OR_INFRASTRUCTURE_ITER505` iff any control, including the smaller-t finite source regression, fails.

## Claim locks
No threshold change. No tangent-panel change. No causal/rho change. No branch sum. No post-hoc t selection. No remainder, positive-measure, local-integrability, Haar, ten-spectral pairing, or physical-vertex theorem. D7-S2/S3/S4 remain unchanged. Terminal D7 classifier remains forbidden. Candidate Gravity remains inactive.

## Post-gate decision
After PASS, the fixed-causal full-K5 leading-survival blocker is numerically qualified on the frozen panels and the next dependent collision gate is a prospectively frozen uniform full-collision blow-up remainder/neighborhood certificate. After BLOCKED, diagnose only the first causal smaller-t numerical defect; do not loosen the 5e-3 criterion.
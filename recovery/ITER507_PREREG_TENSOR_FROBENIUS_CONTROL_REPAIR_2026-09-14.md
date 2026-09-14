# Iter507 — Tensor Frobenius control repair

Prospectively frozen after consuming terminal Iter506 production evidence and before any Iter507 production evidence.

## Causal diagnosis from Iter506
Iter506 completed 18/18 lanes plus aggregate but every lane was invalid with `ValueError('Improper number of dimensions to norm.')`. The first causal defect is a numerical/control implementation error: `numpy.linalg.norm(T, ord='fro')` was applied to rank-4 intertwiner tensors. NumPy's `ord='fro'` matrix norm is not defined for rank-4 arrays. This is infrastructure/numerical plumbing, not a scientific DECAY/NONDECAY result.

## Frozen repair
The only intended mathematical implementation change relative to Iter506 is the tensor Frobenius norm evaluation. For any intertwiner tensor `T`, use the Euclidean norm of all tensor entries, equivalently `sqrt(sum |T_i|^2)`, implemented as `np.linalg.norm(np.ravel(T))`. This is exactly the Frobenius/Hilbert-Schmidt norm of the tensor viewed as a coefficient vector and does not change the scientific object.

## Frozen science scope
- Same fixed-causal j=1 full-K5 leading contraction as Iter506.
- Same panels T0/T1/T2, causal classes 0to5/1to4/2to3, rho in {7,8}.
- Same 243 intertwiner channels and no-branch-sum rule.
- Same Iter505 upstream qualification requirement and thresholds, including `5e-3` finite-t source-regression and `1e-12` witness threshold.
- Same prospective radii: eta in {1e-12, 1e-10, 1e-8, 1e-6}.
- Same analytic edge-variation formula and center-channel selection before the eta scan.
- No post-hoc radius insertion or refinement is allowed.

## Frozen interpretation
- PASS only if all 18 lanes are valid and the smallest frozen radius `1e-12` is certified in every lane.
- Scientific FAIL only if controls are valid yet at least one lane has no certificate at `1e-12`.
- Any remaining control/containment/runtime defect is BLOCKED/INFRASTRUCTURE and must not be interpreted scientifically.
- Even PASS is only a scoped open coordinate-neighborhood nonzero leading-contraction certificate.
- No Haar theorem, positive-measure theorem, spectral theorem, D7-S2 closure, terminal D7 label, or EXISTING_SUFFICIENT/ADAPT_EXISTING/HYBRID_REQUIRED/NEW_REQUIRED classification follows from Iter507.
- Candidate Gravity remains inactive.

## Next gate lock
After PASS, the next allowed dependent gate is a prospectively frozen uniform finite-t remainder/blow-up domination certificate before any positive-measure/Haar claim. Otherwise repair only the first causal blocker without weakening scientific criteria.
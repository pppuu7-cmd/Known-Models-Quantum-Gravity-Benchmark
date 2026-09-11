# LQG spinfoam-stack Hessian and convergence audit — Iter281

Date: 2026-09-11
Family: `LQG_SPINFOAM`
RQIR Core: `v1.0 FROZEN`

## Primary object
Muxin Han, *Summation and triangulation independence of Lorentzian spinfoam amplitudes for all LQG*, Physical Review D 113, 084034 (2026), DOI `10.1103/n76f-31gf`, arXiv `2510.26926`.

The source constructs a spinfoam-stack sum over an infinite class of 2-complexes. In the infinite internal-area-cutoff limit, the amplitude localizes on SU(2) flat connections; for topologically trivial manifolds the renormalized finite part is independent of bulk triangulation. The same source makes clear that this large-cutoff limit is topological/scale-invariant, whereas the semiclassical Regge/GR regime is associated with finite large cutoff and small Barbero–Immirzi parameter.

## Parallel independent audit
Workflow: `lqg-spinfoam-stack-hessian-audit`
Run: `34554825500`
Head: `cb0d459291ab208a65cc744f9443d7bae473756f`

Four independent jobs were executed concurrently with `fail-fast: false`, `max-parallel: 4`, followed by an aggregate dependency barrier:

1. exact 6x6 Hessian determinant and Sylvester negative-definiteness test;
2. exact incidence-factorization check `M = -B^T B`, rank and projected kernel;
3. exact 18x18 Kronecker consistency check `M tensor I_3`;
4. positivity/truncation convergence of the published `C0,C1,C2` coefficient sums on beta = 0.25, 0.5, 1, 2.

Result: **4/4 independent jobs SUCCESS + aggregate SUCCESS**.
Aggregate artifact: `lqg-stack-iter281-summary`, digest `sha256:4ebddf182b7b5c469947acab11eabab7a2422b92d43ea1cf2c85d4b687cb82e1`.

Methodology CI run `34554825514`: SUCCESS.
Reproducibility-release run `34554911718`: SUCCESS.

## Numerical/exact result
- `det(M_6x6) = 125`.
- The published 6x6 Hessian block is strictly negative definite by the exact Sylvester criterion and is nondegenerate.
- `M = -B^T B` is satisfied exactly for the explicit 1–5 Pachner example and chosen orientations.
- `rank(B) = 6`; projected kernel dimension = `0`.
- The 18x18 `M tensor I_3` block has rank `18`, is nondegenerate, and satisfies the exact determinant identity `det(M tensor I_3)=det(M)^3`.
- All tested final `C0,C1,C2` values are positive.
- Maximum relative difference between truncations 256 and 512 on the tested beta grid is `0.0` at binary64 precision.

## Scoped classification
`PASS_SCOPED_EXPLICIT_TRIVIAL_TOPOLOGY_SPINFOAM_STACK_HESSIAN_NONDEGENERACY_INCIDENCE_FACTORIZATION_AND_COEFFICIENT_CONVERGENCE__TOPOLOGICAL_LARGE_CUTOFF_NOT_PHYSICAL_UV_IR_GR_CLOSURE`

This independently strengthens the explicit localization/nondegeneracy and triangulation/refinement-control evidence. It does **not** independently reproduce the complete stack amplitude or prove the generic theorem for all complexes/topologies.

Most importantly, the topological large-cutoff regime must not be silently identified with the physical semiclassical GR regime. The audit therefore does not provide the missing same-realization physical UV-to-IR/GR trajectory, normalized gravity observable, parameter/refinement identity, common comparator, or propagated error certificate.

Family status remains nonterminal (`PARTIAL/BLOCKED`), not FAIL.

Existing decisive blocker remains:
`BLOCKED_MISSING_SAME_REALIZATION_PHYSICAL_UV_TO_IR_GR_TRAJECTORY_NORMALIZED_GRAVITY_OBSERVABLE_PARAMETER_IDENTITY_COMPARATOR_AND_PROPAGATED_ERROR_CERTIFICATE_FROM_COMPLETE_SPINFOAM_CONTINUUM_FIXED_POINT`

## Global consequence
- Tier-1 census remains `15`.
- strict terminal remains `1/15`.
- candidate-QG terminal remains `0/14`.
- D7 remains `NOT_CLOSED / NOT_YET_AUTHORIZED`.
- Candidate Gravity remains inactive at R3 `24%`.

## Publication handoff
- Paper III: `NOT_NEEDED` as a new general rule; Iter281 corroborates Iter277 `MULTI_AXIS_RESOURCE_CLOSURE` / claim-domain separation only.
- Paper IV: `READY`; include the Han spinfoam-stack result, the four-way independent audit, and the explicit distinction between topological large-cutoff closure and the still-missing physical UV→IR/GR bridge.

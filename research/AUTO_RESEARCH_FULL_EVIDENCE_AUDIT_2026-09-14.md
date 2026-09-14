# Auto-research full evidence audit — 2026-09-14

Status: **provenance/scientific audit only; no new D7 promotion**.

This ledger was reconstructed from `main`, diverged research branches, committed recovery/result files, and terminal GitHub Actions artifacts. It records terminal evidence even when the branch itself was never merged or the result existed only in Actions. It does not convert preregistered-but-unrun work into evidence.

## Global claim locks

- `D7-S2 = NOT_CLOSED`.
- `D7-S3 = NOT_CLOSED`.
- `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`.
- `D7-S5 = NOT_AUTHORIZED`; terminal D7 labels remain forbidden.
- Candidate Gravity remains inactive.
- No physical causal-vertex finiteness/divergence theorem is established.
- Absolute convergence, conditional/PV amplitudes, and source-defined distributional amplitudes remain distinct.

## A. Source object / one-wedge distributional chain

- Iter442: `SOURCE_SPECTRAL_PROJECTOR_AND_TOLLER_POLE_CANCELLATION_REALIZED` (32/32 PASS). Source projector/pole cancellation realized; S2 strengthened, not closed.
- Iter450: `BLOCKED_SOURCE_CAUSAL_INVARIANT_CONTRACTION_OBJECT_AMBIGUOUS`. Historical source-object blocker.
- Iter451: `BLOCKED_PRIMARY_SOURCE_CAUSAL_VERTEX_OBJECT_INCOMPLETE`. Historical source-object blocker.
- Iter452: `PRIMARY_SOURCE_CAUSAL_VERTEX_OBJECT_PINNED_COMPLETE`. arXiv:2601.23162v1 Eq.(3)/(4)/(5)/(6)/(7) object pinned; source ambiguity removed.
- Iter453: `ITER453_EQ4_MAGNETIC_INTERTWINER_CONTRACTION_TOPOLOGY_QUALIFIED`; synthetic tensor topology only.
- Iter454: historical `SCIENTIFIC_FAIL_ITER454_TOLLER_FEYNMAN_PROJECTOR_KERNEL`, but the frozen zero-scaling predicate was malformed for a simple reciprocal-Gamma zero. Preserve as historical FAIL, not source refutation.
- Iter455: `ITER455_TOLLER_RECIPROCAL_GAMMA_SIMPLE_ZERO_QUALIFIED_SCOPED`.
- Iter456: `ITER456_REDUCED_TOLLER_APPENDIXB_RUHL_PHASE_QUALIFIED_SCOPED`; j=1 reduced Toller branch formulas, additive identity and pole controls qualified.
- Iter457: `ITER457_TOLLER_EQ7_FULL_MAGNETIC_RECONSTRUCTION_QUALIFIED_SCOPED`; source Eq.(7) full magnetic reconstruction qualified.
- Iter458: `SCIENTIFIC_FAIL_ITER458_TOLLER_FEYNMAN_IEPSILON_ORDINARY_TRUNCATION`; ordinary symmetric real-line truncation fails, without changing published i-epsilon.
- Iter459, run `34746472976`, artifact `10313863332`: `ITER459_TOLLER_PLEMELJ_DISTRIBUTIONAL_KERNEL_QUALIFIED_SCOPED`. Standard Plemelj/test-function pairing qualifies; ordinary truncation failure is not a source no-go.
- Iter463: `ITER463_SOURCE_P11_D_LEADING_OSCILLATORY_ASYMPTOTICS_QUALIFIED_SCOPED`.
- Iter464: `ITER464_SOURCE_P11_D_DISTRIBUTIONAL_PAIRING_QUALIFIED_SCOPED`.
- Iter465: `ITER465_SOURCE_TWOFACTOR_TRANSVERSAL_PULLBACK_ORDER_INDEPENDENCE_QUALIFIED_SCOPED`; only transversal two-factor product, not shared-variable/full-vertex pairing.
- Iter469, run `34770250944`, artifact `10322120889`: `ITER469_TEN_SPECTRAL_PLEMEJ_LOCAL_PRODUCT_WAVEFRONT_QUALIFIED_SCOPED`; local ten-variable tensor-product/wavefront issue qualified, global correlated-kernel pairing still open.

## B. Exact one-wedge collision singularity and contraction survival

- Iter447: `SOURCE_TOLLER_PAIR_COLLISION_LOCAL_POWER_OBSTRUCTION_ON_FROZEN_GRID`; fixed-branch local pair-power obstruction, worst p about 11; not a divergence theorem.
- Iter448: `SOURCE_TOLLER_BRANCH_SUM_PAIR_COLLISION_POWER_INTEGRABLE_ON_FROZEN_GRID`; strong T+ + T- cancellation, but physical causal vertex fixes branch signs wedge-by-wedge.
- Iter449: `SOURCE_TOLLER_COHERENT_SHARED_SCALE_TWO_THREE_PAIR_POWER_INTEGRABLE_ON_FROZEN_GRID`; branch-sum multipair control, not physical fixed-causal contraction.
- Iter474: `UNRESOLVED_ITER474_ON_FROZEN_GRID`; numerical beta-power hint, later superseded by exact Iter477.
- Iter477, run `34772546243`, artifact `10322307672`: `ITER477_SOURCE_TOLLER_EXACT_BETA0_BRANCH_ORDER_2JPLUS1_QUALIFIED_SCOPED`. Each individual fixed causal branch has exact beta^{-(2j+1)} singular order with finite nonzero leading coefficient.
- Iter479, run `34772768304`, artifact `10322656348`: `ITER479_SOURCE_TOLLER_LEADING_MAGNETIC_MATRIX_FULL_RANK_QUALIFIED_SCOPED`. Leading magnetic matrix remains full rank; magnetic-rank loss cannot by itself remove the singularity.
- Iter480 was prospectively invalidated before implementation for a dimensionful threshold; never reuse its contract.
- Iter480B, authoritative retry run `34773320961`, aggregate artifact `10323081045`: `ITER480B_SOURCE_INTERTWINER_CONTRACTION_NONZERO_WITNESS_SCOPED`. 130/243 j=1 recoupling assignments give nonzero source-compatible leading-coefficient witnesses; boundary intertwiners alone do not enforce universal cancellation.
- Iter481: `ITER481_SOURCE_ANGULAR_INTERTWINER_NETWORK_NONZERO_WITNESS_SCOPED`; 243/243 nonzero witnesses on frozen angular panels. Angular Eq.(7) mixing + intertwiners still do not force universal cancellation.
- Iter482: `ITER482_COMMON_NODE_SU2_CORRELATED_NETWORK_NONZERO_WITNESS_SCOPED`; exact common-node SU(2) correlation/cycle consistency still does not force cancellation.
- Iter483: `ITER483_COMMON_NODE_SL2C_POLAR_GEOMETRY_QUALIFIED_SCOPED`; common-node noncompact kinematics/polar machinery qualified.
- Iter484: `ITER484_SOURCE_TOLLER_KAK_ONE_EDGE_RECONSTRUCTION_QUALIFIED_SCOPED`; actual source KAK/Toller one-edge lift qualified and false polar-factor substitution rejected.
- Iter485: `ITER485_SHARED_NODE_TEN_EDGE_TOLLER_MAGNETIC_NETWORK_QUALIFIED_SCOPED`; all ten source Toller edges from the same five shared SL(2,C) nodes plus genuine intertwiners form a finite convention-consistent pre-Haar network on frozen panels. Tested causal patterns do not force universal cancellation.

Consequence: no tested local/intertwiner/angular/common-node/magnetic-rank mechanism universally kills the fixed-causal leading branch singularity before integration. Any rescue must use a more global correlated mechanism (Haar/group integration, collision geometry, spectral/distributional pairing, or another source-backed effect not already excluded).

## C. Group infinity / Haar chain

- Iter443: one-leg radial envelope integrable on frozen grid; late slope about -2.
- Iter444: two-group separated radial envelope integrable on frozen grid; common-shift slope about -2.
- Iter445: exact independent-factor envelope covers only K5 escape cones k=1,2; k=3 marginal and k=4 insufficient. Nonpositive margin is not divergence.
- Iter446: fixed-label collision-excised K5 noncompact tail controlled by Kaminski comparison. Infinity away from collisions is not the principal fixed-label group-space blocker.
- Iter486: terminal `INFRASTRUCTURE_OR_SOURCE_FAIL_ITER486`; raw s=4 slopes near +4 were not promotable because an absolute nonrepresentation negative control was scale-nonuniform.
- Iter487/489: after prospective numerical revalidation, `SCIENTIFIC_FAIL_ITER487_HAAR_ESCAPE_ACTUAL_ENVELOPE_REVALIDATED_BY_ITER489`. Valid one-dimensional s=4 shared-node paths have stable post-Haar NONDECAY slopes about +4. This falsifies universal exponential decay on all frozen paths but is zero angular measure, not a Haar divergence theorem.
- Iter490: `INFRASTRUCTURE_OR_NUMERICAL_FAIL_ITER490`; fixed-radius angular thickening invalidated by ill-conditioned absolute KAK control.
- Iter491: high-precision re-evaluation removes the numerical issue and gives `SCIENTIFIC_FAIL_ITER491_ANGULAR_THICKENING_HP`. No frozen fixed radius {0.0025,0.005,0.01,0.02} is sampled NONDECAY for all causal classes; sampled slopes range about -9.91 to -1.86. Therefore the +4 center ray is not stable over those finite nonzero radii.
- Iter492: `ITER492_TANGENT_BOUNDARY_LAYER_BRACKET_QUALIFIED_SCOPED`. For eps_q(R)=0.02 exp(-qR), frozen tangent directions give full NONDECAY at q>=1 and fail at q=0.5,0.75. Thus the center has a shrinking q=1 boundary layer, not a fixed open cone.
- Iter493: `ITER493_CRITICAL_Q1_LOCAL_VARIATION_QUALIFIED_SCOPED`; q=1 local response finite but strongly anisotropic.
- Iter494: `ITER494_CRITICAL_Q1_MIXED_CURVATURE_QUALIFIED_SCOPED`; mixed curvature can be order unity and is strongly anisotropic; diagonal/separable Taylor models are invalid.
- Iter495: `ITER495_MULTIVARIATE_TAYLOR_STRESS_QUALIFIED_SCOPED`; original quadratic model lacks stable cubic remainder on frozen simultaneous perturbations.
- Iter496: `ITER496_COEFFICIENT_STENCIL_CONVERGENCE_QUALIFIED_SCOPED`; Richardson removes most stencil truncation and restores near-cubic median scaling, but rare nonuniform outliers remain.
- Iter497: `ITER497_RICHARDSON_ENCLOSURE_HOLDOUT_QUALIFIED_SCOPED`; all 768/768 independent holdouts covered, worst coverage ratio 0.483944..., but this remains finite holdout evidence, not a continuous neighborhood certificate.
- Iter498: `ITER498_MAX_ENVELOPE_NONSMOOTH_BLOCKER_IDENTIFIED_SCOPED`; true finite max-envelope channel crossing 195->222 at R=10,12, not KAK degeneracy.
- Iter499: `ITER499_NUMERICAL_METHOD_BLOCKER`; first natural Arb/Acb direct interval construction fails through dependency/KAK overestimation.
- Iter500: `ITER500_COMPACT_SANDWICH_FACTORIZED_KAK_QUALIFIED_SCOPED`; factorized KAK removes the KAK dependency blocker on all 1024/1024 frozen states.
- Iter501: terminal `ITER501_NUMERICAL_METHOD_BLOCKER`; after KAK repair, natural interval dependence is still lost in the 243-channel contraction, driving max-envelope lower bounds to zero / breaking point containment.
- Iter502: authoritative run `34830476485`, terminal aggregate artifact `10356359599`, digest `sha256:b25baacf2d1cc04cd71a018189234c29501faedcbd2434a4b3aa308b5f97b7e3`; `ITER502_NUMERICAL_METHOD_BLOCKER`. Four 2to3 lanes were cancelled, so `valid_structure=false`; all eight completed 0to5/1to4 lanes independently show the same nonpositive-envelope-lower-bound method blocker. No science slope promotion is allowed.
- Iter503: separately preregistered centered-multilinear max-envelope **method diagnostic only** on branch `research/iter503-centered-multilinear-envelope`. As of this audit, retry run `34862605028` has source-lock PASS and all three causal lanes still running; no terminal verdict may be inferred.

## D. K5 collision geometry

- Iter461 remained queued with no jobs and has no terminal evidence.
- Iter471, run `34770611238`, artifact `10321737765`, supersedes its scientific intent with `ITER471_K5_COLLISION_STRATA_EXACT_GEOMETRY_QUALIFIED_SCOPED`.
- Exact naive pair-power critical exponents by partition type:
  - 2+1+1+1: 3
  - 2+2+1: 3
  - 3+1+1: 2
  - 3+2: 9/4
  - 4+1: 3/2
  - 5: 6/5
- Equality is marginal/unresolved. Exceeding a naive threshold means only `SIMPLE_BOUND_INSUFFICIENT`, never a divergence declaration.

Therefore Iter461 should not be duplicated merely to recover the same partition geometry.

## E. Ten-spectral correlated-kernel chain

- Iter460: `ITER460_SOURCE_P11_D_TAIL_CHARACTERIZED_SCOPED`; source-weighted spectral envelope is oscillatory/growing, not Schwartz/L1.
- Iter463 pins leading oscillatory powers/phases.
- Iter464 gives exact one-dimensional source-specific distributional pairing.
- Iter465 gives transversal two-factor pullback/order independence.
- Iter468 pins the actual formal source object: ten independent wedge spectral variables/weights acting on one common four-group correlated kernel; no artificial shared spectral variable or delta.
- Iter469 qualifies the local ten-variable tensor-product/Plemelj/wavefront level.
- Iter470: `ITER470_TEN_SPECTRAL_ABSOLUTE_DECAY_REQUIREMENT_BUDGET_PINNED_SCOPED`; an absolute-decay route would require worst-case isotropic c>20, or coordinatewise c_e>2 on each m=±1 wedge.
- Iter473: `BLOCKED_SOURCE_KERNEL_EXECUTABLE_NOT_PRESENT_IN_TRACKED_REPO_SCOPED`; tracked repo lacked one executable combining ten independent spectra, source-faithful factors, actual four-group integration/validated bound, and ten-variable output.
- Iter476: `BLOCKED_KAMINSKI_FIXED_LABEL_FINITE_NOT_YET_UNIFORM_SPECTRAL_BOUND_SCOPED`; fixed-label Kaminski integrability does not supply the required simultaneous ten-spectral uniform decay budget.
- 2026-09-14 source/mathematical audit removes the false subproblem of choosing an arbitrary iterated order among ten independent one-variable boundary values. The unresolved object is the action/pairing of their tensor product on the correlated four-group kernel, including collision strata and noncompact/spectral growth.

## F. D7-S3 / S4 formal bridge chain

- Iter441: early fail-closed gap graph; S3 components absent, S4 partial; exact K5 orientation witness already nontrivial.
- Iter462: `ITER462_D7_S3_S4_EVIDENCE_LOCALIZATION_COMPLETE_SCOPED`.
- Iter472: `ITER472_D7_S3_FORMAL_DECLARATION_MATRIX_COMPLETE_SCOPED`; individual declarations exist, but no complete compatible chain; parameter transport is especially missing/conflicted.
- Iter475: `ITER475_LQG_S3_TARGETED_CONFLICT_MATRIX_COMPLETE_SCOPED`; same-realization transport/comparator conflicts explicit.
- Iter478: `ITER478_LQG_S3_MINIMAL_BRIDGE_MAP_COMPLETE_SCOPED`; all five remaining bridge classes have explicit source blockers.

Consequence: do not run more generic S3 evidence scans. The missing compatible transport/comparator/certificate chain is explicit and must be solved source-faithfully or remain blocked.

## Current scientific bottlenecks after full audit

1. **Continuous q=1 max-envelope certification:** finite holdouts are strong, but Iter501/502 show that naive interval arithmetic loses correlation. Iter503 tests a centered multilinear enclosure without changing the physical object or thresholds.
2. **Correlated fixed-causal K5 collision contraction:** one-wedge singular order is exact and survives magnetic rank/boundary/angular/common-node preintegration tests; naive collision thresholds are known, but no correlated collision theorem for the physical fixed-causal contracted object is established.
3. **Ten-spectral boundary-value action on the correlated four-group kernel:** local tensor-product distribution theory is not the bottleneck; global multiplier/growth/collision admissibility is.
4. **D7-S3 compatible bridge:** formal source conflicts remain explicit.

## Immediate admissible decision

Do not launch a competing full science gate while Iter503 is nonterminal. Consume Iter503 first. If it is method-qualified, the preregistration authorizes a fresh full 12-job science gate using the identical centered formula and the already-frozen Iter501 thresholds/domain. If it is method-insufficient, do not subdivide again; move to a genuinely dependency-preserving affine/Taylor/mean-value common-amplitude enclosure. If it is validation-fail, repair only the identified validation defect.

Independently, future collision/spectral work should target the actual correlated source object, not rerun Iter461 geometry, independent-factor Plemelj tests, boundary-intertwiner cancellation, or fixed-label infinity checks that are already consumed above.

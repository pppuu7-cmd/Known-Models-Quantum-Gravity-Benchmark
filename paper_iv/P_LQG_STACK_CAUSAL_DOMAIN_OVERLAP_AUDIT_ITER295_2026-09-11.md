# Iter295 — LQG Han-stack / generalized causal EPRL-KKL domain-overlap audit

## Authorities
- Muxin Han, *Summation and triangulation independence of Lorentzian spinfoam amplitudes for all LQG*, Phys. Rev. D 113, 084034 (2026), DOI `10.1103/n76f-31gf`, arXiv:2510.26926.
- Carlos E. Beltrán, *Causal Structure for Generalized Spinfoams*, arXiv:2603.22661v2 (2026).

## Source-level bridge
Han defines each member of a spinfoam stack as a generalized EPRL amplitude on a concrete 2-complex, using the KKL formalism for generally non-simplicial complexes. Beltrán defines causal structure and a causal EPRL-KKL vertex on an arbitrary 2-complex. This establishes a shared per-complex formalism and makes a nonempty conditional overlap testable.

Beltrán's working scope adds conditions: time orientation, timelike edges in the remainder of the analysis, and 3-link-connected vertex boundary graphs. Han's complete family does not prove these conditions universally. Therefore the valid result is conditional overlap, not universal Han-stack inclusion.

## Exact K5 witness
The frozen guard constructs the five-valent / 4-simplex-compatible K5 causal graph used by Beltrán:
- nodes = 5; links = 10;
- causality/incidence matrix rank over GF(2) = 4;
- kernel dimension = 1;
- global sign flip leaves wedge-orientation bits unchanged;
- every one-link and every two-link deletion leaves K5 connected.
This is an explicit nonempty admissible witness, not a family-wide proof.

## Frozen machine audit
- Scientific run: `34592425741` on head `300159ee62c096aeaff766658169be5d5fea83fe`.
- Four independent guards with `fail-fast:false`, `max-parallel:4`: formalism overlap, domain scope, exact K5 witness, transport guard.
- Aggregate after dependency barrier = SUCCESS.
- Methodology run: `34592425770` = SUCCESS, including preflight, 4/4 shards and aggregate/bundle.
- Summary artifact: `10196164627`.
- Artifact digest: `sha256:5ac870b2e59d0717913042bc2a0eb809e650c24bcc4c0ca7ad0facf929eeef70`.
- Raw summary digest: `sha256:55b371ffda6542839d1cdfc92b07196e207e4b4b83253d00142ed35d7bf86eb6`.

## Classification
`PASS_SCOPED_CONDITIONAL_GENERALIZED_EPRL_KKL_DOMAIN_OVERLAP_WITH_EXPLICIT_K5_CAUSAL_WITNESS__NO_HAN_STACK_SUM_LIFT_OR_SAME_REALIZATION_UV_TO_IR_TRANSPORT`

## Fail-closed boundary
Beltrán does not explicitly insert the causal vertex into Han's complete stack sum over face multiplicities with `lambda_f` weights and area cutoffs, and does not supply a same-realization UV-to-large-spin Regge/GR parameter/observable/error transport certificate. LQG/spinfoam remains `PARTIAL/BLOCKED`, not FAIL and not terminal. D7 remains unauthorized.

Refined active blocker:
`BLOCKED_MISSING_CAUSAL_VERTEX_LIFT_THROUGH_HAN_COMPLETE_STACK_SUM_FACE_MULTIPLICITIES_AND_LAMBDA_F_WEIGHTS_PLUS_SAME_REALIZATION_UV_TO_CAUSAL_LARGE_SPIN_REGGE_GR_TRANSPORT_WITH_GAMMA_SPIN_SCALE_IDENTITY_NORMALIZED_OBSERVABLE_COMMON_DOMAIN_COMPARATOR_AND_PROPAGATED_ERROR`

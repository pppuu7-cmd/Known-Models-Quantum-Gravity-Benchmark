# Iter297 — formal causal-vertex composition on Han stack members

## Authorities and derivation status
- Muxin Han, *Summation and triangulation independence of Lorentzian spinfoam amplitudes for all LQG*, Phys. Rev. D 113, 084034 (2026), DOI `10.1103/n76f-31gf`, arXiv:2510.26926.
- Carlos E. Beltrán, *Causal Structure for Generalized Spinfoams*, arXiv:2603.22661v2 (2026).
- The Iter297 result is a source-grounded formal composition inference. It is not a claim that either source proves a finite causal Han-stack amplitude.

## Formal composition bridge
Han's stack sums generalized EPRL-KKL amplitudes over a face-multiplicity/spin-labelled family of 2-complexes and attaches external weights `prod_f lambda_f^p_f`. The multi-vertex amplitude is built by gluing local vertex amplitudes. Beltrán defines a causal alternative to the generalized EPRL-KKL vertex on arbitrary 2-complexes and explicitly proposes replacing the EPRL-KKL amplitude by the causal alternative at each vertex in multi-vertex discretizations.

Together with the Iter296 causal-orientation lift, this permits a formal causal amplitude to be assigned member-by-member on the admissible Han stack family by local vertex substitution while retaining the same member labels and external `lambda_f^p_f` multiplicity bookkeeping.

## Frozen machine audit
- Scientific run `34593574762` on `880b01f89488492c50deda7b315d02f425e0a3f4`: 4/4 independent guards + aggregate SUCCESS.
- Member-label preservation: 512 cases, up to 8 root faces and multiplicity 7.
- Exact-rational Han coupling identity: 1,792 cases covering 2..8 vertices, multiplicities 1..16, 16 seeds; `prod_v lambda_vf^p = (prod_v lambda_vf)^p` exactly in every case.
- Methodology run `34593574674`: preflight + 4/4 shards + aggregate/bundle SUCCESS.
- Summary artifact `10260556884`; artifact digest `sha256:56e8aa47970c6bb29d11bd013466262b08495325d7b612aca5ba9d1374bb14c9`; raw summary digest `sha256:d2886d62a8b590a6be83b4e9eb318f10f9454950a74abc3fa0afb505301af95a`.

## Classification
`PASS_SCOPED_FORMAL_MEMBERWISE_CAUSAL_VERTEX_SUBSTITUTION_ON_ITER296_ADMISSIBLE_HAN_STACK_COMPLEXES_WITH_RETAINED_EXTERNAL_LAMBDA_MULTIPLICITY_BOOKKEEPING__NO_HALF_LINK_GLUE_EQUIVALENCE_FINITE_NORMALIZED_CAUSAL_STACK_SUM_CUTOFF_REMOVAL_OR_UV_IR_OBSERVABLE_CERTIFICATE`

## Fail-closed boundary
Beltrán explicitly leaves finiteness of the generalized causal vertex open. The available sources also do not prove that the causal replacement is exactly identical to Han's special half-link/Haar gluing kernel representation, that Han's face-factorized analytic stack formula and large-cutoff localization survive the replacement, that the causal stack is normalized or cutoff-independent, or that a same-realization UV-to-causal-Regge/GR observable/error transport exists. Therefore this is a formal memberwise composition result only. LQG/spinfoam remains `PARTIAL/BLOCKED`, not terminal; D7 remains unauthorized.

Refined blocker:
`BLOCKED_MISSING_EXACT_HAN_HALF_LINK_GLUE_EQUIVALENCE_AND_FINITE_NORMALIZED_GENERALIZED_CAUSAL_VERTEX_STACK_AMPLITUDE_WITH_LAMBDA_F_WEIGHTED_AREA_CUTOFF_CONTROL_PLUS_SAME_REALIZATION_UV_TO_CAUSAL_LARGE_SPIN_REGGE_GR_TRANSPORT_WITH_GAMMA_SPIN_SCALE_IDENTITY_NORMALIZED_OBSERVABLE_COMMON_DOMAIN_COMPARATOR_AND_PROPAGATED_ERROR`

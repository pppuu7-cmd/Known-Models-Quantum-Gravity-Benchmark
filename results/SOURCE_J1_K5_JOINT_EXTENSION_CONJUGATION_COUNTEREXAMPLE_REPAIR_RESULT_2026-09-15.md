# Terminal result — source j=1 K5 joint-extension conjugation counterexample repair

Date: 2026-09-15
Lane: KMQGB Research / Closure
Status: `TERMINAL_SCOPED`

## Authority

This result is governed by the prospective v2 preregistration:

- `research/SOURCE_J1_K5_JOINT_EXTENSION_CONJUGATION_COUNTEREXAMPLE_REPAIR_PREREG_V2_2026-09-15.md`
- prereg commit: `7b83dc0f29ef142d56d36ceb89909810a1f1fc26`

The earlier v1 preregistration at `b194a6d4b56f93eabb982fd3af7f7da93d0a068b` was explicitly withdrawn before certificate code/workflow/substantive computation by commit `6dedf5e02b63147420f2ebf5fb7abd99499095fd`; it carries no scientific classification.

The current gate repairs the implementation defect identified by:

- `recovery/CRITICAL_REVIEW_SOURCE_J1_K5_VERTEX_CONJUGATION_DERIVATION_2026-09-15.md`
- Critic authority/main at recovery start: `1a54df61c780eb44aeef56986d2481dcfdd55410`
- Critic verdict on the previous joint-extension terminal decision: `INVALID_IMPLEMENTATION`.

Recovery was reconciled before this gate at commit `29ed9ba003e549623db237798836006907285f97`.

## Production provenance

- exact certificate code: `code/source_j1_k5_joint_extension_conjugation_counterexample_repair.py`
- code commit: `5ce3a5fafd19f7ade17f3f9dc83ff252124376df`
- workflow: `.github/workflows/source-j1-k5-joint-extension-conjugation-counterexample-repair.yml`
- workflow/head commit: `ac239d4d568ca03e3233b7ed89eed9b3e4cae032`
- Actions run: `34927882706`
- run event: `push`
- run status/conclusion: `completed / success`
- source-lock job: `104249699277`, `success`
- exact-certificate job: `104249731753`, `success`
- source-lock output: `SOURCE_LOCK=PASS`
- source-locked HEAD: `ac239d4d568ca03e3233b7ed89eed9b3e4cae032`

CI success is provenance only; the scientific classification below is taken from the preregistered exact predicates.

## Raw / canonical artifacts

Actions artifact:

- artifact ID: `10380890593`
- name: `source-j1-k5-joint-extension-conjugation-counterexample-repair`
- size: `3184` bytes
- artifact ZIP digest: `sha256:64874d6a1cef2f91e9d3f2983f8d1edcf9ddcbd94dbd782605679c182b6d6f21`

The artifact contains the raw log, canonical JSON, JSON SHA256 file, and workflow provenance file.

Repository canonical copy:

- `results/source_j1_k5_joint_extension_conjugation_counterexample_repair_2026-09-15.json`
- JSON SHA256 from the terminal Action: `e793c0f3b5f5a0834275d8eead664a7585f211d92aedff611376ba5fa336dd12`
- hash ledger: `results/source_j1_k5_joint_extension_conjugation_counterexample_repair_2026-09-15.sha256`
- provenance ledger: `results/source_j1_k5_joint_extension_conjugation_counterexample_repair_2026-09-15.provenance.txt`

Canonical-copy commits before this terminal note:

- JSON: `61f689e914a731756d3406a63c23d70c2613359a`
- hash: `cf43ad9a210fce9ef5869fde4f341b7715503d4c`
- provenance: `581e83390e69de94fe47beae5e1a3b910aedb7ff`

## Exact outcome

The implementation source-locked the actual channel-0 tensor from `code/iter499_arb_core.py` and propagated the Critic-retained representation-valued conjugation matrix

`C = [[0,0,1],[0,-1,0],[1,0,0]]`.

Exact results:

- channel-0 source support size: `9`;
- canonical `(C tensor C tensor C tensor C) I = I`: `81/81` components exact, `0` mismatches;
- `C^2 = I`: exact `true`;
- node-by-node fixed-channel C absorption criterion: `true`;
- deliberately asymmetric `C_bad`: only `77/81` components equal, `4` mismatches;
- first `C_bad` mismatch: magnetic tuple `(-1,+1,0,0)`, original `-1/3`, transformed `+1/3`;
- 32 vertex-sign assignments give exactly `16` distinct constrained causal K5 patterns, exactly `2` preimages each;
- globally negated set has exactly `16` patterns and zero intersection with the causal set;
- nonzero witness sectors: `32` of `1024` independent edge-sign patterns;
- anti-linear checks `c(-kappa)=conj(c(kappa))`: `1024/1024`, `0` failures;
- K5 permutations: `120`;
- exhaustive permutation-pattern checks: `122880`, `0` failures;
- full independent-sign coefficient sum: exactly `(0,0)`;
- collision distribution scaling degree: `12` against certified ceiling `30`;
- uniform `+1` negative-control sum: `(1024,0)`, therefore correctly nonzero;
- causal-only `+i` negative control: `32` anti-linear covariance failures;
- all frozen positive controls: `true`;
- all frozen negative controls: adversarial as required.

## CLASSIFICATION

`SOURCE_J1_K5_FROZEN_CONJUGATION_CONSTRAINTS_LEAVE_NONZERO_COLLISION_AMBIGUITY_SCOPED`

This is the prospectively frozen PASS classification.

## NEW FACT

For the fixed source-order `j=1`, nonzero-real-rho, intertwiner-channel-`00000`, full-K5-collision realization, the complete tested representation-valued conjugation covariance does **not** eliminate the explicit collision-supported homogeneous witness

`Delta(kappa) = c(kappa) delta_N`,

with `c=+i` on the 16 constrained causal patterns, `c=-i` on their 16 global negatives, and `c=0` on the other 992 patterns.

The same witness simultaneously satisfies:

- the exact channel-`00000` representation-valued `C` propagation tested here;
- anti-linear causal/co-causal covariance;
- all 120 K5 vertex permutations;
- the full 1024-pattern independent-sign EPRL zero-sum identity;
- collision support;
- the certified same-scaling ceiling.

Therefore this frozen constraint set has a nontrivial homogeneous collision-supported kernel. Conditional on existence of any base joint extension `E` satisfying these same tested constraints, `E_lambda = E + lambda Delta`, `lambda in R`, gives a distinct family satisfying the same tested constraints.

## CLAIM CEILING

This result does **not** prove:

- existence of a base joint Eq. (4) extension;
- unconditional, physical, or global nonuniqueness of the published causal vertex;
- that the source chooses this counterterm;
- that no additional source-faithful joint regulator, microlocal product theorem, normalization, boundary condition, nested-collision compatibility rule, or other authority removes this ambiguity;
- any result for other spins, intertwiner channels, model families, or lower collision strata;
- closure of D7-S2, D7-S3, or D7-S4;
- any terminal D7 selector;
- Candidate Gravity authority;
- `QUANTUM_GRAVITY_SOLVED`, `ALL_KNOWN_MODELS_FAIL`, `NEW_THEORY_REQUIRED`, or `NEW_PHYSICS_FOUND`.

The previous hard-coded joint-extension blocker remains historically preserved as `INVALID_IMPLEMENTATION`; this repaired result supersedes it only for the v2 frozen scoped question.

## Consequence

The high-DAG obstruction is now localized more sharply: one-wedge conjugation plus exact fixed-channel propagation, K5 permutation symmetry, the independent-sign EPRL identity, and the known scaling ceiling are still insufficient **by themselves** to select a unique full-collision joint extension in the frozen channel-`00000` scope.

The next admissible gate should therefore search for an additional source-faithful **joint selection authority** — e.g. an Eq. (4) correlated limiting prescription, microlocal product/extension rule, normalization condition, or nested-stratum compatibility condition — and test outcome-sensitively whether that added authority kills the explicit `Delta` witness. No such second gate is executed in this run.

## Governance

- `RQIR Core v1.0 = FROZEN`.
- `D7-S2 = NOT_CLOSED`.
- `D7-S3 = NOT_CLOSED`.
- `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`.
- Terminal D7 labels and `EXISTING_SUFFICIENT / ADAPT_EXISTING / HYBRID_REQUIRED / NEW_REQUIRED` remain forbidden.
- Candidate Gravity remains inactive.
- Historical FAIL/BLOCKED/INVALID records remain preserved.

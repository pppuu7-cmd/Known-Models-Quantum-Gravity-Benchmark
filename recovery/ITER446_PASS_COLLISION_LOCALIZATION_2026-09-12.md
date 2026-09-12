# KMQGB recovery delta — Iter446 PASS and collision localization

Date: 2026-09-12

## Iter446 — terminal PASS

- Branch: `research/iter446-kaminski-tail-comparison`
- Head: `aa70873638ddac05354f2e78c9bb60efe31bc4dc`
- Workflow run: `34718261533`
- Run conclusion: `success`
- Summary artifact: `iter446-summary`
- Artifact id: `10305203003`
- Artifact digest: `sha256:b1a4ee76bfacbd7dc311c1096c9093b9ece0a523eba100cc57984cab3bcbddf2`
- Aggregate payload SHA256: `a2109e612bbae65b3f460ab614c502a4f2197cf6fc6387c6ad52a2ac0ab21629`
- Frozen lanes: `4/4` PASS.
- Classification: `SOURCE_BACKED_CAUSAL_K5_COLLISION_EXCISED_DOMAIN_ABSOLUTELY_INTEGRABLE_BY_KAMINSKI_COMPARISON`.
- K5 minimum cut measured by the gate: `4`.
- Maximum frozen comparison ratio `M(beta)*(cosh beta)^0.95`: `0.3730700758970565`.

## Scientific interpretation

This is the first KMQGB result that replaces the insufficient independent-product radial argument by a source-backed correlated graph-integral comparison. At fixed source labels, outside any fixed neighborhood of the pair-collision loci, the Toller KAK bound has asymptotic radial exponent `1`, which is stronger than the frozen Kaminski comparison exponent `0.95`. K5 satisfies the required 3-edge-connected condition. The collision-excised absolute causal integrand is therefore controlled by the finite hyperbolic comparison integral.

This resolves the noncompact-tail question only on the collision-excised fixed-label domain. It does **not** prove the full causal vertex finite, because the comparison constant is allowed to depend on the collision exclusion `delta` and no bound uniform as `delta -> 0` has been established.

Frozen D7-S2 localization after PASS:
- noncompact infinity away from collisions: positive comparison certificate;
- one-group radial escape: positive Iter443 certificate;
- two-group independent-product reach: positive for k=1,2 from Iter445, with direct Iter444 stress test still running;
- k=3/k=4 naive product-envelope failure: superseded as a tail blocker by the stronger correlated comparison outside collision tubes;
- remaining fixed-label local blocker: pair and multi-pair collision strata `r_ab -> 0`, including exact invariant contraction / distributional-extension behavior;
- generalized causal-vertex normalization and stack/spin/refinement issues remain separate and open.

Formal status remains:
- D7-S2: `NONCOMPACT_TAIL_LOCALIZED__COLLISION_STRATA_REMAIN_OPEN`
- D7-S3: `NOT_CLOSED`
- D7-S4: `PARTIAL_GLOBAL_NOT_CLOSED`
- D7-S5: `NOT_AUTHORIZED`
- Candidate Gravity: inactive / not authorized.

## Next authorized fixed-label gate

Before opening any terminal classifier, audit existing Iter325-438 collision work for overlap. If no later source-faithful general-j collision audit exists, preregister a new frozen test on gamma `{7,8}`, j `{2,5}`, all magnetic channels and both causal branches:

1. measure the exact small-beta asymptotic exponent/coefficient of the published general-j Toller functions;
2. distinguish raw branch singularity from invariantly contracted physical data;
3. apply only source/representation-valid invariant contractions (no synthetic projector promoted to physics);
4. classify surviving local coefficients as `COLLISION_OBSTRUCTION_CANDIDATE_SURVIVES`, not model failure;
5. if the leading coefficient is annihilated, continue to the first nonzero subleading coefficient and multi-pair collision sectors.

Terminal D7 and Candidate Gravity remain locked.

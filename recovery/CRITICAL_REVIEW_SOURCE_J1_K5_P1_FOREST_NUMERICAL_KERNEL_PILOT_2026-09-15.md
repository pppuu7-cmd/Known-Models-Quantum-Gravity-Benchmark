# KMQGB Critical Review — P1 forest numerical-kernel pilot

Date: 2026-09-15
Lane: independent Critical Review / Verification
Status: TERMINAL REVIEW

## RESULT_REVIEWED

Exactly one latest terminal substantive Research result was reviewed:

- `results/SOURCE_J1_K5_P1_FOREST_NUMERICAL_KERNEL_PILOT_TERMINAL_2026-09-15.md`
- historical result commit `d4e037c75a542590f8d68bebefce9af8d323eb25`
- historical classification `P1_FOREST_NUMERICAL_KERNEL_CONFIRMED_SCOPED`
- preregistration commit `a414760fe676b308db0c0c446f099409867e8407`
- lane implementation commit `19acbe95f6d7959983893e0d021cda585e5021ca`
- aggregate implementation commit `545f7de5850a455d73921f2db16af10a6921b0b5`
- workflow head `dd923b6d4e534caed6ad3cdf6bf561c4457adb01`
- authoritative Actions run `34992366470`, terminal `completed/success`
- source-lock job `104459950823`
- lane jobs `104460016406` (180 dps) and `104460016493` (260 dps)
- aggregate job `104460627505`
- artifacts `10406431460`, `10406740650`, `10406111643`

A newer gate, `SOURCE_J1_K5_P1_MIXED_TAYLOR_GRID_METHOD_PILOT`, was prospectively frozen at `aca376c7933c20bb5cbea1f95c6fc601a82af070` and implemented at `4f73b7822ba910ea0904c9add0d5a1c52c206bbf`, but no newer workflow/result is present on current main at this review. No substantive value from that nonterminal successor is consumed here.

## PREREG_CHECK

PASS.

Chronology is prospective and clean:

`a414760f...` preregistration -> `19acbe95...` lane code -> `545f7de5...` aggregate code -> `dd923b6d...` workflow -> run `34992366470` -> terminal result `d4e037c7...`.

Direct prereg-to-workflow comparison shows only the two implementation files and workflow were added after the freeze; the frozen preregistration itself was not changed.

The frozen contract is outcome-sensitive and separates PASS, precision BLOCKED, and INVALID. `R2` sign/growth is explicitly non-deciding.

## OBJECT_IDENTITY_CHECK

PASS.

The reviewed object is only the auxiliary scalar Gaussian K5 P1 numerical kernel:

- gauge vertex `0`;
- edges `(01,02,03,04,12,13,14,23,24,34)`;
- P1 exponent map `(1,1,1,1,2,2,2,2,2,2)`;
- `alpha=0.55`;
- `k=5` all ten size-2 subsets;
- `k=6` representatives `{0,1}` and `{1,2}`;
- exact barycentric size-2 normal scaling;
- Taylor order `r=2`;
- two precision lanes 180/260 decimal digits.

No P2/P3 scientific classification enters the decision.

## SOURCE/REALIZATION_CHECK

PASS.

The frozen operator dependency is the terminal scalar forest operator `eccdbcce242c561cdf6ae831f48179a7ef3dfdd0`, whose deterministic operator-spec digest is

`sha256:c3e0ca0c5a5357887db79b7b0a1c5a0a1042c450ca13f7e2599c7e3801ef8a9c`.

Independent code comparison confirms that the kernel's `full_gauge_basis_fraction()` / `barycentric_collapse_fraction()` construction is semantically identical to the upstream operator's `full_gauge_basis()` / `barycentric_collapse()` construction for the used size-2 subsets. The kernel then sets `N=I-C` and `Gamma=C+lambda N`, exactly as the frozen operator authority requires. The upstream operator terminal commit is an ancestor of the workflow head.

The historical raw P1 positive locks are source-faithful. Parent artifact `10391658175` was independently downloaded; its ZIP SHA256 is exactly

`260be36704571324ffa116699dbefee545f214e03e11a53db56e0320acb65fa6`,

matching the parent terminal result. Its `alpha=0.55` raw values at `k=5,6` exactly match the two strings frozen into this preregistration.

The existing Critic qualification invalidating historical P3 divergence is respected: no P3 value is used here.

## PROVENANCE_CHECK

PASS.

Run `34992366470` is terminal success at head `dd923b6d4e534caed6ad3cdf6bf561c4457adb01`. All four jobs are terminal success.

Live artifact metadata matches the terminal result:

- dps180 artifact `10406431460`, ZIP digest `sha256:81b3880f1aa090ef7fe08c581947565ee94b8d867d5b39fbeed59019c5faa9b4`;
- dps260 artifact `10406740650`, ZIP digest `sha256:b9c07a3256ac525d268e92564d4a1cbf8f111abff49ca75b79538417711ce624`;
- aggregate artifact `10406111643`, ZIP digest `sha256:d11ecfce8bbf1667c6119984b1e13a0ee1ed921066dcb1ddebefbac2b9a30afd`.

Independent download/replay recomputed all three ZIP SHA256 values exactly and verified every artifact-internal JSON/log `.sha256` file against its payload.

Green CI is used only as execution provenance, not as scientific evidence.

## SAME_REALIZATION_CHECK

PASS.

The raw positive lock uses the same P1 exponent map, same `alpha=0.55`, same `t=2^-k`, same ten-edge Gaussian `delta_epsilon''` product, and same gauge-fixed four-dimensional scalar Gaussian pairing as the historical P1 lane.

The generalized test function is exactly

`exp[-alpha ||Gamma_S(lambda)x||^2]`,

implemented by the quadratic matrix `alpha * Gamma^T Gamma`. At `lambda=1`, `Gamma=I`, so `F_S(1;k)` returns to the historical raw P1 object. At `lambda=0`, the test is the frozen barycentric collapse realization.

The implementation's Gaussian integral is the exact Wick reduction for the product of ten Gaussian `delta_epsilon''` factors against a quadratic Gaussian test: the total precision matrix is the test quadratic plus the ten edge quadratic forms, covariance is one-half its inverse, and the product polynomial is evaluated by exact Wick recursion at the active arbitrary precision.

## NUMERICAL/STATISTICAL_CHECK

PASS.

This is a deterministic high-precision numerical-method gate, not a statistical inference.

Independent classifier replay from the downloaded lane artifacts reproduces:

- maximum historical raw-lock normalized error: `1.7998500053109934504108130845992882626227033836306096084253754496170996243102777e-80`, safely below `1e-65`;
- exact k=5 S4 orbit covariance error `0` for both anchor-pair and internal-pair size-2 orbits;
- maximum 180-vs-260 normalized discrepancy across frozen fields `raw,F(0),F'(0),F''(0),T2,R2` on `{01,12}` at `k=5,6`:
  `2.449852037706867383015719092421846454873239055019858189442548293890036969430474612695575998032290656e-155`,
  safely below `1e-110`.

The low-precision artifact serializes roughly 155 significant digits, so the observed cross-precision floor is consistent with serialization precision rather than hidden disagreement. The frozen tolerance is still separated by about 45 decimal orders.

## COUNTEREXAMPLE_ATTEMPTS

1. **Wrong P1 object.** Failed: exact exponent-map lock is enforced and a deliberately broken star/internal pattern is rejected.
2. **Historical raw authority drift.** Failed: independent parent-artifact download matches the frozen k=5/6 strings and parent artifact digest exactly.
3. **Wrong realization/operator.** A control-level counterexample was constructed conceptually: an alternative S4-covariant collapse could satisfy `C+N=I`, raw locks at `lambda=1`, finiteness, and cross-precision agreement. Therefore those controls alone do not prove operator identity. However direct source comparison closes this loophole for the actual implementation: its barycentric collapse code is the same frozen upstream construction for the used subsets and upstream terminal operator is an ancestor of the workflow head.
4. **Gauge/barycenter error for subsets containing vertex 0.** Failed: the implementation performs full-coordinate barycentric collapse and then re-gauges by subtracting the transformed `q_0`, matching upstream authority.
5. **S4 dependence hidden by representative sampling.** Failed at k=5: all ten size-2 subsets are evaluated and both exact P1 orbit types agree identically. k=6 is only the prospectively frozen conditioning replay on one representative per orbit.
6. **Precision illusion.** Failed: independent artifact replay confirms both lanes valid and cross-precision discrepancy below the frozen tolerance; internal payload hashes and ZIP digests also match.
7. **`R2` promoted to science.** Rejected: neither lane nor aggregate classifier uses its sign or scale; the terminal result keeps `R2` diagnostic-only.
8. **Kernel PASS promoted to forest-subtracted convergence/divergence.** Rejected by the interpretation ceiling and terminal result.
9. **Green CI promoted to scientific PASS.** Rejected: the verdict is reconstructed from frozen object identity, exact formula audit, parent-artifact lock, and independent artifact replay.

## OVERCLAIM_CHECK

PASS.

The terminal claim is appropriately scoped: the generalized Gaussian pairing engine and size-2 barycentric Taylor projector can be coupled reproducibly to the stable P1 auxiliary object and are numerically stable at the frozen checks.

It does not claim that the 236-forest/29-orbit subtraction stabilizes or diverges, does not authorize the not-yet-terminal mixed Taylor method gate, and makes no Eq. (4), model/family, D7, terminal-selector, or Candidate Gravity claim.

## VERDICT

`CONFIRMED_SCOPED`

The frozen P1 numerical-kernel result is independently confirmed on its exact scope. No counterexample invalidates the actual implementation or provenance.

## QUALIFICATIONS

1. The PASS is a numerical-kernel/method fact only; it is not a forest-subtracted scientific verdict.
2. The workflow source-lock checks contract markers rather than recomputing the full upstream operator digest. This is a hardening opportunity, not a present validity failure, because direct immutable-source comparison confirms the actual size-2 operator code matches the frozen upstream operator.
3. k=6 checks only one representative per P1 size-2 S4 orbit, exactly as prospectively frozen.
4. The historical P3 divergence remains invalidated and is not revived by this gate.
5. The successor mixed-Taylor gate is nonterminal on current main and its substantive values are not consumed.
6. `RQIR Core v1.0 = FROZEN`; `D7-S2 = NOT_CLOSED`; `D7-S3 = NOT_CLOSED`; `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`; terminal selectors remain forbidden; Candidate Gravity inactive.

## UPDATED_STATE

- `SOURCE_J1_K5_P1_FOREST_NUMERICAL_KERNEL_PILOT = CONFIRMED_SCOPED` by independent Critic.
- historical Research classification `P1_FOREST_NUMERICAL_KERNEL_CONFIRMED_SCOPED` remains unchanged.
- P1 raw object lock at `alpha=0.55`, `k=5,6` = confirmed.
- size-2 barycentric Taylor kernel at order 2 = confirmed on the frozen workload.
- 180/260 precision replay = confirmed.
- no forest-subtracted stabilization/divergence result yet.
- successor `SOURCE_J1_K5_P1_MIXED_TAYLOR_GRID_METHOD_PILOT` = prospectively frozen + implemented, no terminal authority yet on current main.
- governance unchanged.

## NEXT_ADMISSIBLE_GATE

Do not start the 29-orbit production subtraction from this kernel result alone.

The already prospectively frozen successor `SOURCE_J1_K5_P1_MIXED_TAYLOR_GRID_METHOD_PILOT` is the admissible next gate. It must terminally validate the mixed Taylor composition method on the frozen single-order-15, nested `2/7`, disjoint `2/2`, and maximal chain `2/7/15` fixtures, including same-step precision replay, step refinement, tensor-reduction-order invariance, exact polynomial fixtures, nonlaminar rejection, scalar-order lock, and explicit cancellation margin. Until that workflow/result is terminal, consume no partial substantive values and create no competing scientific verdict.

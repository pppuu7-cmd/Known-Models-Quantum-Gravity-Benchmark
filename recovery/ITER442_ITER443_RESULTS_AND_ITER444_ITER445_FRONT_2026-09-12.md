# KMQGB recovery delta — Iter442/443 terminal results and next multi-group front

Date: 2026-09-12

This note supersedes the launch-only status of Iter442/443 for the current D7-S2 source-level causal-integrability front. It does not supersede the global D7 decision contract.

## Iter442 — terminal PASS: source spectral projector / Toller-pole cancellation

- Branch: `research/iter442-toller-spectral-projector`
- Head: `1cde553791fc15a9994530ef9e4e1413b2c91aaf`
- Workflow run: `34716591952`
- Run conclusion: `success`
- Summary artifact: `iter442-summary`
- Artifact id: `10305050851`
- Artifact digest: `sha256:4c7b2cb565a0e3bc63622d8104039a125a8ad06591206fd888b8f5ad2511b8c0`
- Frozen lanes: `32/32` PASS.
- Classification: `SOURCE_SPECTRAL_PROJECTOR_AND_TOLLER_POLE_CANCELLATION_REALIZED`.
- Maximum final residue scaled error: `1.854998307689984e-09`.
- Maximum Toller-pole last-pair scaled difference: `3.0910567354313406e-07`.
- Minimum Feynman-to-Toller-pole distance: `14.0`.

Scientific interpretation: the source-faithful spectral `i epsilon` projector and the published Toller-kernel pole cancellation are numerically realized on the prospectively frozen gamma-simple `gamma={7,8}`, `j={2,5}`, all-`m` matrix. The epsilon shift is in spectral `rho-tilde`, never `beta+i epsilon`.

Scope lock: this is not full K5 Haar/angular causal-vertex finiteness, generalized causal-vertex normalization, stack cutoff removal, family terminality, terminal D7 authorization, or Candidate Gravity activation.

Frozen status after PASS:
- D7-S2: `STRENGTHENED_BUT_NOT_CLOSED`
- D7-S3: `NOT_CLOSED`
- D7-S4: `PARTIAL_GLOBAL_NOT_CLOSED`
- D7-S5: `NOT_AUTHORIZED`
- Candidate Gravity: `false`

## Iter443 — terminal PASS: one-group noncompact radial envelope

- Branch: `research/iter443-one-leg-radial-integrability`
- Head: `41d7a40a8f640776f51c9b3cbc79ba97c3d7ed8c`
- Workflow run: `34716909118`
- Run conclusion: `success`
- Summary artifact: `iter443-summary`
- Artifact id: `10304814788`
- Artifact digest: `sha256:5df4f8de1fb7e9fa3eebfafc93ce5b8d19996fd055c089ec749bfb2b06ef70a2`
- Frozen lanes: `4/4` PASS.
- Classification: `SOURCE_ONE_LEG_RADIAL_ENVELOPE_INTEGRABLE_ON_FROZEN_GRID`.
- Worst late-window log slope: `-2.0000000317733115`.
- Maximum scaled `M_j(beta) exp(beta)` variation: `1.1078297363348e-07`.

Scientific interpretation: for one K5 group variable escaping radially with the other vertex variables fixed, the conservative source envelope `sinh(beta)^2 M_j(beta)^4` decreases exponentially and is numerically consistent with an asymptotic exponent `-2` on the frozen matrix.

Scope lock: one-group radial escape only. It is not simultaneous multi-group escape integrability, arbitrary angular-direction control, full causal-vertex finiteness, generalized EPRL-KKL normalization, stack cutoff removal, or D7 closure.

## Next authorized independent D7-S2 gates

The source-level local/spectral and one-group radial layers are now sufficiently saturated that further repetitions have lower information gain. Two independent prospectively admissible next gates are authorized:

1. **Iter444 — two-group separated radial escape gate.**
   For two simultaneously escaping noncompact group variables on K5, freeze a common-axis, fixed-relative-rapidity family and test the conservative source envelope
   `sinh(beta1)^2 sinh(beta2)^2 M_j(beta1)^3 M_j(beta2)^3 M_j(|beta1-beta2|)`
   with `beta1=B+c/2`, `beta2=B-c/2`, frozen `c in {0.5,1,2,4}` and large common shift `B`. This is a genuine two-variable noncompact escape witness, but remains narrower than full Haar/angular integrability.

2. **Iter445 — exact cut-cone reach diagnostic.**
   Enumerate K5 escape subsets of cardinality `k=1..4` under the already validated one-factor `M_j(beta)~exp(-beta)` envelope and compare crossing-edge decay with `k` radial Haar factors. The exact common-shift envelope exponent is `2k-k(5-k)=k(k-3)`. The diagnostic may certify where this envelope argument is sufficient and where stronger correlated/angular/intertwiner bounds are required. Nonnegative envelope exponent is `UNRESOLVED_BY_THIS_BOUND`, never a divergence theorem or scientific FAIL.

These gates are independent and may run concurrently. Neither may authorize terminal D7 or Candidate Gravity.

## S3/S4 frontier retained

Iter441 remains authoritative for the independent S3/S4 blockers:
- explicit same-realization UV-to-Regge/GR parameter, observable, and propagated-error transport;
- normalized same-realization comparator/error certificate;
- finite and normalized physical causal-stack realization;
- explicit `lambda_f` face-multiplicity transport;
- universal common-domain inclusion;
- causal-stack cutoff removal and normalization.

Existing UV-IR guards explicitly prohibit silently identifying the 2017 `lambda/delta/mu` hierarchy with the causal-stack area cutoff or UV fixed-point coordinates and record the absence of a normalized operational observable bridge. Those remain source/definition blockers, not numerical parameters to retune.

## Working research-progress rubric

This is a stable research-progress metric, not a formal gate status or probability of `NEW_REQUIRED`.

- `D2 82% (Delta 0 pp)`
- `D4 68% (Delta 0 pp)`
- `D7 56% (Delta +4 pp from the post-Iter441 working value 52%)`
- `overall 67% (Delta +2 pp from the post-Iter441 working value 65%)`

The increase is justified only by two prospectively frozen substantive D7-S2 results: full 32-lane source spectral projector/pole cancellation and a 4-lane one-group noncompact radial integrability witness. No formal D7 stage changed state.

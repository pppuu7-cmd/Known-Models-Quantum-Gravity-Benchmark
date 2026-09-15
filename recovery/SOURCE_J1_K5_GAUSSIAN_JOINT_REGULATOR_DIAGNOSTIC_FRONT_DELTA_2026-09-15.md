# Recovery/front delta — Gaussian auxiliary joint-regulator diagnostic

Date: 2026-09-15
Status: `TERMINAL_SCOPED_AND_NEXT_FRONT_AUTHORIZED`

## Terminal result consumed

Gate:
`SOURCE_J1_K5_ADDITIONAL_JOINT_REGULATOR_GAUSSIAN_DIAGNOSTIC_GATE`

Terminal classification:
`AUX_GAUSSIAN_JOINT_REGULATOR_REJECTED_UNRENORMALIZED_SCOPED`

Authority chain:

- prereg commit `b4d5fc5734fe3fdde4b1008651b4e86f911e457a`;
- decision-precedence supplement `1d5b9123f71db860816ba7e8948c7ee5a78b364d`;
- implementation `8ca8ba683b0bada0faca8015daae0ac6393db338`;
- workflow head `14ed14ee9f7951f5a3a9c65d8a33b9e3f45e5af1`;
- run `34954054888`, completed/success;
- source-lock job `104331699506`, success;
- diagnostic job `104331985957`, success;
- artifact `10390423124`;
- artifact digest `sha256:7679e9349798386bc53757207cbb85142420e10ae89745b62e4ab4117cf54009`;
- terminal result commit `8982ea92de08bfb6028df35be16f116e0e58c22f`.

All NEW anisotropic paths P1-P3 are `UNRENORMALIZED_DIVERGENT_DIAGNOSTIC` with frozen tail growth values approximately `40.9991`, `26.0110`, and `66.0071`, respectively. P0 remains exploratory reproduction only and did not control classification.

## Interpretation lock

This rejects only the unrenormalized Gaussian approximate-identity auxiliary extension on the frozen aligned highest-contact K5 witness. It is not Eq. (4) distributional nonexistence and does not authorize a model/family failure.

The historical redundant joint-Feynman authority result at `aecdc3e6...` is Critic-qualified `INVALID_PROVENANCE` at `3d5900cf44f23e636e3d2c549567d4331410d95c` and is not a downstream premise here.

Validated parent remains the repaired Eq.4 existence result `6c4d479c42d3b71de4c4c32c5abb910728b97fc9` (`SOURCE_J1_K5_EQ4_DISTRIBUTIONAL_EXISTENCE_BLOCKED_SCOPED`).

## Existing uniqueness limitation

Independent exact Critic-confirmed chain at commit `97a4821f85f13e6f5c6d41356612c88939d45f2c` establishes, conditional on a base extension, a nonzero collision-supported homogeneous witness compatible with the specifically frozen conjugation / coefficient-pattern K5 relabeling / independent-sign zero-sum / scaling constraints. Therefore those constraints alone cannot uniquely select an extension.

Do not interpret a future subtraction/counterterm construction as source-selected merely because it cancels the Gaussian divergence.

## Next admissible front

`SOURCE_J1_K5_GAUSSIAN_COMPACT_SUPPORT_LOCALIZATION_GATE`

Goal: determine whether the terminal Gaussian divergence is genuinely local to the full K5 collision by replacing the Schwartz diagnostic with a compactly supported test equal to the same Gaussian test in a fixed neighborhood of the collision and proving/validating that the exterior contribution is exponentially subleading along the frozen NEW regulator paths.

This gate should preferentially use analytic Gaussian tail bounds plus exact K5 spanning-tree/conormal geometry rather than expensive multidimensional quadrature.

If compact-support localization succeeds, it strengthens rejection of the unrenormalized Gaussian auxiliary family as a local distributional extension candidate. It still does not prove nonexistence of renormalized/canonical/source-selected extensions.

## Locks

- `RQIR Core v1.0 = FROZEN`
- `D7-S2 = NOT_CLOSED`
- `D7-S3 = NOT_CLOSED`
- `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`
- terminal selectors forbidden
- Candidate Gravity inactive
- KMQGB downstream of pinned DSIR authority
- Iter504 / Iter461 partial values remain non-evidence until terminal

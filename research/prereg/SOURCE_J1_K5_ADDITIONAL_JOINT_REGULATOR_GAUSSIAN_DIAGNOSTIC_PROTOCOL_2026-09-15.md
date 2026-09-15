# Protocol supplement — Gaussian joint-regulator diagnostic

Date: 2026-09-15
Parent prereg: `research/prereg/SOURCE_J1_K5_ADDITIONAL_JOINT_REGULATOR_GAUSSIAN_DIAGNOSTIC_2026-09-15.md`
Parent prereg commit: `b4d5fc5734fe3fdde4b1008651b4e86f911e457a`
Status: `FROZEN_BEFORE_NEW_PATH_EXECUTION`

This supplement resolves only terminal-label precedence and does not change paths, grid, thresholds, object, or controls.

If more than one terminal predicate is simultaneously true, use this fixed order:

1. `INVALID_IMPLEMENTATION`
2. `AUX_GAUSSIAN_JOINT_REGULATOR_PATH_DEPENDENCE_WITNESS_SCOPED`
3. `AUX_GAUSSIAN_JOINT_REGULATOR_REJECTED_UNRENORMALIZED_SCOPED`
4. `AUX_GAUSSIAN_JOINT_REGULATOR_SURVIVES_DIAGNOSTIC_SCOPED`
5. `AUX_GAUSSIAN_JOINT_REGULATOR_DIAGNOSTIC_INCONCLUSIVE`

`PATH_DEPENDENCE` requires incompatible terminal behavior among at least two NEW paths P1-P3 under the exact parent definition; a mere difference of divergent growth exponents is not promoted to two different finite distributional limits. If all NEW paths are divergent diagnostics, classify `REJECTED_UNRENORMALIZED_SCOPED` unless another frozen path-dependence condition is independently met.

P0 remains reproduction-only and cannot satisfy any scientific terminal predicate.

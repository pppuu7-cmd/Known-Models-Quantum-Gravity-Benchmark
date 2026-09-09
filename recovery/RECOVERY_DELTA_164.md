# KMQGB Recovery Delta 164

**Date:** 2026-09-10

A model-specific adapter correction was made for CFS regularization.

CFS microscopic UV regularization can have physical significance as spacetime microstructure; it is not automatically a technical regulator that must be removed.

Therefore the correct frozen-RQIR adapter requirement is

`PHYSICAL_REGULARIZATION_LAW_FIXED_AND_PREDICTIVE`

rather than unconditional `epsilon -> 0`.

Required discipline:

- microscopic regularization fixed prospectively / derived from the parent;
- no post-hoc tuning to the residual;
- stability across the admissible microscopic family;
- continuum GR/QFT control where appropriate;
- shared-parameter predictions for non-continuum effects;
- full comparator quotient.

New authority:

`paper_iv/O_CFS_PHYSICAL_REGULARIZATION_ADAPTER_RULE_2026.md`.

Iter163 audit was updated to use this corrected adapter rule.

This is explicitly **not** an RQIR Core change; it is a framework-native mapping clarification in KMQGB.

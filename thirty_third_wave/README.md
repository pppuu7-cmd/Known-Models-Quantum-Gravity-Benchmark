# KMQGB Wave 33 — D-Nonlocal Minimality Audit

**Frozen denominator:** 5 P4 red-team targets.  
**Status:** terminal 5/5.  
**Purpose:** test whether exponential boundedness plus crossing/unitarity/causality selects a unique low-freedom nonlocal parent amplitude.

| # | Target | Terminal result |
|---|---|---|
| T33-01 | naive crossing-symmetric Gaussian exponential sum | `FAIL_PARTIAL_WAVE_UNITARITY_AT_HIGH_ENERGY` |
| T33-02 | existence of exponentially bounded unitary/crossing amplitudes | `PASS_EXISTENCE_SCOPED` |
| T33-03 | asymptotic-causality compatible nonlocal examples | `PASS_EXISTENCE_SCOPED` |
| T33-04 | uniqueness from minimal exponential boundedness | `BLOCKED_NO_SELECTION_THEOREM__FAMILY_REMAINS` |
| T33-05 | P4 novel parent-principle status | `NO_SURVIVOR__D_NONLOCAL_IS_ESCAPE_CLASS_NOT_SELECTOR` |

## Result

The D-nonlocal branch is scientifically admissible in principle: modified dispersion relations allow exponentially bounded amplitudes, and explicit proof-of-concept amplitudes can satisfy crossing symmetry, partial-wave unitarity and asymptotic causality.

But exponential boundedness does **not** select a unique amplitude/kernel. The simplest symmetric Gaussian exponential sum fails partial-wave unitarity at high energy, while working examples require additional structure/parameters.

Therefore D-nonlocality is an escape class that changes the dispersion/causality rules; it is not yet the missing low-freedom P4 parent principle.

R4 remains 45% under `MINIMAL_NOVEL_PARENT_PRINCIPLE_SEARCH_RUBRIC.md`.

No KG ansatz is promoted.
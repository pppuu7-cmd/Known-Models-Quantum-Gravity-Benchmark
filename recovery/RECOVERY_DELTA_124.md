# Recovery Delta 124

**Iteration:** 124  
**Status:** immutable recovery; score-neutral; executable exact gate.

Added

- `protocol/P4_FINITE_SPECTRAL_MOMENT_NONUNIQUENESS_GATE.md`;
- `code/p4_spectral_moment_nonuniqueness_reference.py`.

Exact witness: on support `(1,2,3,4,5)`, the finite-difference vector `(1,-4,6,-4,1)` annihilates all moments of degree `0..3`. Adding/subtracting it from positive base weights gives two distinct strictly positive measures with identical first four moments and different fourth moment. Thus finite positivity + sum rules/moments do not uniquely determine the spectral envelope. KMS completion does not remove this positive-frequency nullspace.

Classification: `A2 BLOCKED__FINITE_SPECTRAL_MOMENTS_LEAVE_POSITIVE_MEASURE_NULLSPACE`.

**Scores:** R1 92, R2 89, R3 24, R4 45.

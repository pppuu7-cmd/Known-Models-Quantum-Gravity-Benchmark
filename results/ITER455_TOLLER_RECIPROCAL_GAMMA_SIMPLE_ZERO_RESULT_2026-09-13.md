# Iter455 — Toller reciprocal-Gamma simple-zero scaling

Date: 2026-09-13

## Frozen gate
Prospectively preregistered replacement for the malformed finite-displacement reciprocal-Gamma predicate in Iter454. Historical Iter454 remains immutable. The replacement tests the mathematically correct local law near each negative-integer Gamma pole,

`1/Gamma(-m+δ) = (-1)^m m! δ + O(δ^2)`,

using multiple δ scales, ratio convergence to `m!`, unit log-log slope, strict monotone decrease, and rejection of a quadratic-zero hypothesis. The unaffected Iter454 controls were retained: projector diagonal normalization, exact source-pole enumeration, regulated Sokhotski–Plemelj convergence, and wrong-branch negative control.

## Authoritative provenance
- workflow: `iter455-toller-reciprocal-gamma-zero-scaling`
- head: `5a974e9ac8843a79f374d5ccd1aaa54655a8f127`
- run: `34739025302`
- jobs: lanes `103675418664` (L0), `103675418696` (L1), `103675418819` (L2), `103675418594` (L3); aggregate `103675539451`
- summary artifact: `10311248731`
- summary digest: `sha256:a473971667b2518b46e300e2ad910452badb610be0c624a6e705f8a50f9c69e5`
- raw artifacts: L0 `10311827667`, L1 `10311443056`, L2 `10312376445`, L3 `10311438020`

## Terminal scientific classification
`ITER455_TOLLER_RECIPROCAL_GAMMA_SIMPLE_ZERO_QUALIFIED_SCOPED`

All 4/4 lanes are valid and pass all frozen predicates. Across the source pole sets, `|1/Gamma|/δ` converges to the exact factorial coefficients 1, 2, 6, 24 as applicable; the log-log slopes converge to 1; the magnitudes decrease strictly with δ; and the deliberately wrong quadratic-zero hypothesis is rejected. Diagonal projector normalization is exact in the audit, source-pole enumeration is exact, the regulated physical branch converges, and the wrong branch stays separated.

## Interpretation
This closes only the malformed reciprocal-Gamma prerequisite exposed by Iter454. It does not rewrite Iter454's historical frozen FAIL. It qualifies the scalar source-projector simple-zero structure required to proceed to a source-faithful reduced Toller `t`-matrix gate.

## Scope guards
No full reduced Toller reconstruction is proved here; no Eq.(7) magnetic reconstruction; no causal-vertex convergence/finiteness theorem; no D7-S2 closure; no terminal D7 classifier; no Candidate Gravity activation.

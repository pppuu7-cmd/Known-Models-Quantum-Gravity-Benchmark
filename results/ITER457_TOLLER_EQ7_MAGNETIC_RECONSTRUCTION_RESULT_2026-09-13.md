# Iter457 — Toller Eq. (7) full magnetic reconstruction

## Terminal classification
`ITER457_TOLLER_EQ7_FULL_MAGNETIC_RECONSTRUCTION_QUALIFIED_SCOPED`

## Frozen provenance
- preregistration: `dd0e6dc6cf8bf5e700e40e204186337d0545214a`
- implementation: `b5fb92fa6e712273b16dfb35b2cb98cee1c086fe`
- authoritative head: `680e4e7d9b1360a6699a4676f0f9cd72de6ad143`
- production run: `34741925566`
- aggregate job: `103683031716`
- summary artifact: `10313410848`
- summary digest: `sha256:7ba47ac6e73567f017100b780c23e1f1c951fb667b4fc48a378685b733765a11`
- raw artifacts: L0 `10312920723`, L1 `10312891447`, L2 `10313490515`, L3 `10313276016`
- valid/pass: 4/4, 4/4

## Scientific result
All four frozen lanes independently passed the source Eq. (7) Cartan magnetic reconstruction audit for the already-qualified `k=j=l=1` reduced Toller layer. The matrix-product and explicit magnetic-index sum routes agree to high precision; `T+ + T-` reconstructs the corresponding Wigner-D object; the Cartan U(1) redundancy and left/right SU(2) covariance controls pass; deliberately wrong p-index and wrong right-conjugation constructions are rejected in every lane.

Worst observed residuals over the four lanes were:
- route agreement: `2.49e-81`
- SU(2) unitarity control: `4.53e-81`
- Eq. (7) sum/product agreement: `6.80e-80`
- additive reconstruction: `7.66e-80`
- Cartan redundancy: `2.00e-81`
- covariance: `2.08e-81`
- wrong-index rejection fraction: `1.0`
- wrong-conjugation rejection fraction: `1.0`

## Scope
This is a scoped qualification of the exact Eq. (7) magnetic reconstruction for the tested source-defined `j=l=k=1` sector. It is not an arbitrary-spin theorem, not a proof of noncompact vertex convergence, not a physical causal-vertex finiteness/divergence theorem, and it does not close D7-S2 by itself.

## Next allowed gate
A separately prospectively preregistered source-defined finite-`i epsilon` / noncompact convergence pilot is now allowed. The published spectral prescription and integration measure must be pinned exactly before implementation; no retuned regulator, fitted cancellation, or replacement prescription is allowed.

## Classification guards
D7-S2, D7-S3, and D7-S4 remain open. Terminal D7 classification and `EXISTING_SUFFICIENT`, `ADAPT_EXISTING`, `HYBRID_REQUIRED`, `NEW_REQUIRED` remain unauthorized. Candidate Gravity remains inactive.

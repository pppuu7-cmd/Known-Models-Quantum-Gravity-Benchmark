# Iter453 — Eq.(4) magnetic/intertwiner contraction-topology qualification

Date: 2026-09-13

## Frozen gate and provenance
- Preregistration commit: `0dff3cf95fd98c202da515631b6f4905e69de202`
- Implementation commit: `c3b2e99273eecf5d9da83d42dc2e3d814b7c8ca4`
- Pre-production bounded contraction-path correction: `0cad3690b4a5e32c848dc4dd86718a58e11192e4`
- Authoritative production head/workflow commit: `8e2ba9e4a1a11bcc821112f404cca6f6661e00c7`
- Authoritative run: `34734577271`
- Aggregate job: `103663579304`
- Summary artifact: `10309998447`
- Summary artifact digest: `sha256:a4bc75e51f8429a35164e2c5a5ab1717dff8e81d27b519340ad01f001aed2d14`
- Immutable source id inherited from terminal Iter452: `arXiv:2601.23162v1`

## Raw artifacts consumed
All four lane artifacts and the frozen aggregate were downloaded and read.

| seed | artifact | artifact digest | qualified |
|---|---:|---|---|
|17|`10310522384`|`sha256:de1d128cad45246aa640920d9c262a0111d97712839d58fa9b5325e8ef65c141`|yes|
|29|`10310770877`|`sha256:6152835948e0e78e97e98ee0c35ac51b80f53fc68a555c90677b77edaeecba88`|yes|
|43|`10310661111`|`sha256:f892e80b63737238ecedf2cac6593b30d5d2f7bcb074488028fd971aaab07878`|yes|
|71|`10311090285`|`sha256:28d103f278e239f65b72d2e994273dd788db9bb31137c81e7f871a30c4525fbe`|yes|

Every lane passed all eight frozen predicates: scalar incidence/contraction validity, local Eq.(5), full explicit `2^10` Eq.(6) branch-sum reconstruction, S5 relabeling covariance, intertwiner-leg-order invariance, broken-incidence negative control, broken-Eq.(5) negative control, and independently assembled contraction-order repeatability.

Worst positive-control residuals over the four lanes:
- local Eq.(5): exactly `0.0`;
- full `2^10` branch-sum relative residual: `1.1364755910069911e-16`;
- S5 permutation relative residual: `1.0500451862475693e-16`;
- intertwiner-leg-order residual: `1.1801220661588445e-16`;
- independent contraction-order residual: `1.6170191174069288e-16`.

Negative controls were nontrivial and passed with margin:
- smallest deliberately broken-incidence relative change: `0.006088625814197581` vs frozen minimum `1e-6`;
- smallest deliberately broken Eq.(5) relative mismatch: `2.06576072991377e-06` vs frozen minimum `1e-8`.

Aggregate: `4/4 qualified`, structurally valid.

## Scientific classification
`ITER453_EQ4_MAGNETIC_INTERTWINER_CONTRACTION_TOPOLOGY_QUALIFIED`

## Interpretation lock
This establishes only the finite deterministic executable index/contraction topology and Eq.(5)/(6) additive-control algebra of the pinned Eq.(4)/boundary object. The test tensors are synthetic deterministic finite-dimensional tensors, not physical Toller matrix elements. Therefore this result does **not** establish convergence, absolute integrability, finite normalization, an epsilon-to-zero distributional limit, D7-S2 closure, a family-level sufficiency result, terminal D7, or Candidate Gravity authorization.

## Next permitted dependent gate
Search/reuse existing validated source-faithful Eq.(3)/(7) Toller implementations. If technically available, prospectively freeze a finite-`i epsilon` actual-Toller insertion/convergence pilot with pointwise Eq.(5)/(6) controls and independent numerical convergence lanes. If no validated implementation exists, record that as the next technical blocker rather than substituting synthetic tensors or weakening the source prescription.

# Iter481 terminal result — source angular/intertwiner network

Date: 2026-09-13

## Authority
- Preregistration: `4609d55741e02db086dc42168d067ffb43dfe7f5`.
- Implementation: `11e358a2441aa1800b3ccbb5a923604d325ee242`.
- Initial production head: `2a35dc91abeae9f07fe99112bd278c67f558a56b`.
- Initial production run `34773608221`: NONAUTHORITATIVE infrastructure/output-serialization failure only. The frozen evaluator reached result construction but failed serializing a NumPy boolean in `zero_matrix_negative`; scientific model, panels, thresholds and interpretation were unchanged.
- Minimal serialization-only repair / authoritative retry head: `1d44bbf3c4fdd1a06e28beae498ebf0a680f927f`.
- Authoritative retry run: `34775946391`.
- Aggregate job: `103774033555`.
- Aggregate artifact: `10323930725`.
- Aggregate digest: `sha256:25cae4be01215585362481ae6296729bfb0769093d8a8ac17d0913778a191475`.

## Scientific classification
`ITER481_SOURCE_ANGULAR_INTERTWINER_NETWORK_NONZERO_WITNESS_SCOPED` — SCIENTIFIC PASS, scoped.

All 12 frozen lanes (`gamma in {7,8}` x three causal representatives x two held-out angular patterns) pass the frozen A-F checks after consuming the raw lane artifacts, not from CI status alone.

## Raw-lane findings
- Every lane has `243/243` recoupling-channel nonzero witnesses above the frozen dimensionless threshold `R>1e-12`.
- P0 lanes have `R_max` about `1.074930989572539e-4`; P1 lanes have `R_max` about `4.07951836187954e-4`.
- Identity-angle regression exactly reproduces the terminal Iter480B support count `130/243` and `R_max=0.0046296296296296285` with zero reported relative residual in every lane.
- Eq.(90) intertwiner Gram residual is `5.551115123125783e-17` in every lane.
- Wigner unitarity maxima are about `2.22e-16`.
- Magnetic-basis reindex relative residuals lie between about `4.08e-16` and `1.16e-15`, safely below the frozen `1e-10` bound.
- Zero-matrix negative controls vanish exactly.

Raw artifacts and digests:
- `10323104796` `sha256:8f96518385bc4c7962c282a2494645b96478a32ac1162ff18caae32020a66086`
- `10323611150` `sha256:2aad9a492756f69fd6d88595ce45c43f9818a58ba9709e85db38fb91c5c44f18`
- `10323751308` `sha256:07a9ea02e841d0ac61cee35611e6ed19492f0512da6efc8cd1902c35b6def2b7`
- `10323203665` `sha256:1122753b2bf5598637a8a4204cb388a547e8c8c951d24827b5e6077c508ccb4f`
- `10323099837` `sha256:bfadf02ab151c6e91fde1771ec5029ffa1ebf11d89eea4009fed8ee607caa239`
- `10323266967` `sha256:4499fd756029b9b50542039efb2b984303c64f543ca607a19df31ec5808d1b13`
- `10323671639` `sha256:5ca612144c4895d04f61aa9019e2b823848e3e6bd4384acb63dcac0c79d24f86`
- `10323766242` `sha256:3330362dda5637bc7b3801cd13fb61da10b9dff8cd877ab4dfcd8adf652504cb`
- `10323860924` `sha256:009f3e305457b6abebd082c02952f6699a9bc53b992fdfcf32615a4b6611d2ad`
- `10323910766` `sha256:06e4d7a5adac275568557ee5494bd1d3d81aa89a3837b1d09af07c53d9d99a8c`
- `10324125393` `sha256:e3686b56c9f5ae946e8fed7be5eccaa66dc62c2d1c926c82d4d378fc8f7b5f6b`
- `10324110326` `sha256:e06dd89b1480fec70fb0100b7787531af7847d1b07df80df531fa56296174405`

## Interpretation
On the frozen j=1 panels, restoring full two-index Eq.(7) angular magnetic matrices together with genuine five-node four-valent SU(2) intertwiners does not force universal leading cancellation. This materially rules out another local-angular/boundary-intertwiner cancellation mechanism.

## Scope guards
This is still a local angular/intertwiner diagnostic. The ten edge matrices were not required to arise from one common set of five `SL(2,C)` group variables. No Haar/group integration, boost sector, spectral integration, Jacobian theorem or full K5 collision-stratum theorem is established. D7-S2 remains `NOT_CLOSED`; D7-S3 remains `NOT_CLOSED`; D7-S4 remains `PARTIAL_GLOBAL_NOT_CLOSED`. No terminal D7 label and no Candidate Gravity authorization follow.

## Next permitted gate
Restore a single common set of node group variables before any further cancellation claim. The next gate should first test a compact `SU(2)` common-node control slice where all ten edge rotations are derived from five node rotations, with exact cycle-consistency and gauge-covariance controls, then evaluate the same source-backed leading magnetic/intertwiner network. A PASS would be only a common-group compatibility witness on that compact control slice, not a full `SL(2,C)` Haar result.
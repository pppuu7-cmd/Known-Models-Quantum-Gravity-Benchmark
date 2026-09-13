# Iter484 — source-faithful one-edge Toller/KAK reconstruction

Date: 2026-09-14

## Frozen gate
Prospectively preregistered before implementation/production in `recovery/ITER484_PREREG_SOURCE_TOLLER_KAK_ONE_EDGE_2026-09-14.md`.

Parent authorities:
- terminal Iter456 reduced Toller Appendix-B / Rühl-phase qualification (`k=j=l=1`, `m=-1,0,+1`);
- terminal Iter483 five-shared-node `SL(2,C)` common-node geometry.

Source locks:
- `sources/arxiv_2601_23162v1_causal_vertex.json`;
- `sources/arxiv_2604_24945v1_toller_cartan.json`.

## Authoritative provenance
- source-lock commit: `407be28347d45eee7dc24cfc8c56cda176becfd6`
- prereg commit: `e7c3f280d5bb07f8c5c223328cd2bdaf51d3c463`
- implementation commit: `b3d7775fbbd5dec3a20912800cc570a7a4192340`
- aggregate implementation commit: `bb7601df1177712f03704d30c60ebac5365e0a3e`
- workflow/head: `d80fc93d02fbe32212976afd2d3254a197383c90`
- authoritative run: `34787734912`
- source-lock job: `103806176109`
- aggregate job: `103806231962`
- aggregate artifact: `10326933008`
- aggregate digest: `sha256:1146847e79c50be7bf2c9213238990d877ba8c598f0d38dfc217385a0359aa1e`

Raw lane artifacts:
- A-mild `10326992814`, `sha256:5d364e3b819ee920e03e4ddbd46dd8deae64946f59808eb0583f65a941d86951`
- A-strong `10326888382`, `sha256:d007df4be12105262cffa9664a4631fc6abae32f6403ec8e4772376118547325`
- B-mild `10326354200`, `sha256:3f0572008c3e5bbfaa24a80520e3bd92a8f7089b100efda4c70098270560aa26`
- B-strong `10327476411`, `sha256:6332edbbffa5019b76986537f4f449a0837245e92fa8149d4d5586c6726a6c71`
- C-mild `10326449051`, `sha256:16b992090113b92b96b68161d588b2849ba20254152545cf5978508b0895fa2c`
- C-strong `10326807759`, `sha256:01f8ca20ec38636454ff395c75df16feb1d3e13b91744e29a9ed446391628b21`
- D-mild `10327530620`, `sha256:c40e6ab849916200737e89dd185ca04ea7c91ca260afe08a42d9b37dd7708f4d`
- D-strong `10327032779`, `sha256:29ff78aa69758109e19763ca0c6161fe17999537d353d2975ea512ec1174e64e`

## Terminal scientific classification
`ITER484_SOURCE_TOLLER_KAK_ONE_EDGE_RECONSTRUCTION_QUALIFIED_SCOPED`

Frozen aggregate: 8/8 expected lanes present, 8/8 valid, 8/8 PASS, zero scientific-fail lanes, zero invalid or missing lanes. Source-lock job PASS.

## New scientific result
For the frozen `j=k=l=1` source realization and all eight Iter483 common-node noncompact panels, the source Cartan/Toller lift

`h = U1 A(beta) U2  ->  T^(+/-)(h)=D^1(U1) diag_m[t^(+/-)_m(beta)] D^1(U2)`

is numerically stable and convention-consistent under the prospectively frozen tests.

Worst observed positive-control residuals across all lanes:
- Cartan reconstruction: `8.082545620880531e-16`;
- continuity of Cartan beta with Iter483 polar/singular-value rapidity: `5.828670879282072e-16`;
- full magnetic additive identity `T+ + T- = D`: `1.1369844158915326e-13` versus frozen `1e-11` ceiling;
- axial KAK-gauge invariance: `4.547695798758324e-13` versus frozen `1e-10` ceiling;
- reduced gamma-simple conjugation/reversal residual: `7.380102368044855e-81` versus frozen `1e-35` ceiling;
- inversion reconstruction: `7.447602459741819e-16`;
- predicted-vs-direct inverse Toller KAK reconstruction: `1.6825652809228595e-11` versus frozen `1e-9` ceiling.

Both prospectively frozen negative controls were strongly active:
- naive polar-factor substitution reconstruction error was at least `0.15200770610375844` (required `>1e-4`);
- Toller nonrepresentation mismatch was at least `34.4270324664872` across lane maxima (required at least one rho per lane `>1e-5`).

Thus Iter483 positive-polar factors cannot be silently identified with the source KAK factors, while the actual source-defined KAK lift is qualified on the frozen one-edge panels. The computation also directly preserves the source warning that Toller matrices are not a group representation.

## Interpretation ceiling
This is a one-edge, frozen-`j=1` source-reconstruction qualification only. It does **not** establish:
- arbitrary-spin reconstruction;
- the ten-edge boost-dependent magnetic network;
- shared Haar/group integration or its convergence;
- ten spectral integrations or collision/boundary-value admissibility;
- a finite or divergent physical causal vertex;
- D7-S2 closure;
- a terminal D7 classifier;
- Candidate Gravity authorization.

No D7 terminal label changes are authorized by this result.

## Next admissible gate
Prospectively construct and test the **ten-edge boost-dependent Toller magnetic network from the same five shared `SL(2,C)` node variables**, using source Eq.(4)/(7)/(13) edge ordering and branch signs plus genuine five-node boundary intertwiners. Preserve one-edge Iter484 KAK reconstruction per edge as a positive control and include explicit negative controls against independent-edge surrogates and false Toller composition. Only after that network object is qualified may a Haar/group-integration gate be interpreted.

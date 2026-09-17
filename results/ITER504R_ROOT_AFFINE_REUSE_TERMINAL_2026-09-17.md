# Iter504R — terminal root-affine reuse continuous-drift diagnostic

Date: 2026-09-17
Status: TERMINAL

## Frozen classification

`ITER504R_ROOT_AFFINE_REUSE_INCONCLUSIVE_SCOPED`

This is a **valid scientific INCONCLUSIVE** result. It is not FAIL, not a decay witness, and not an implementation blocker.

## Frozen authority

- preregistration: `147d68f26ed3a14ce3cd1fd77fcd96d5fb329ec8`;
- root-affine implementation: `f846820bae39963a48272deccb2e4a539100fce1`;
- exact-cover/classifier assembler: `904cae881f86f213973110fc8f18a4c02d67cc3d`;
- aggregate implementation: `e0367d4e0b91afc668e733c2027fd39bf27637fc`;
- authoritative workflow head: `a6b71f56b5900173029a291690b65e7ac644d000`;
- authoritative Actions run: `35154724661`, terminal `completed/success`.

The later multi-OS diversification run `35155085604` is retained only as an execution/reproducibility diagnostic. Its roots and assemblies completed, but its aggregate classified INVALID because two cross-OS assembled JSON files were not byte-identical at approximately 1e-10-level serialized floating bounds. That run does not supersede this already-terminal same-science authoritative run.

## Authoritative artifacts

- root 13 / Python 3.11: artifact `10471742557`, digest `sha256:4e4297838615ba82934fe46a60bc1b502bae2d46621473896b08448154beb6ce`;
- root 14 / Python 3.11: artifact `10471797229`, digest `sha256:23221eb1577f1c1f0b01d4cf91bc40490a088b8d266a96bdb290638a332cb14d`;
- root 15 / Python 3.11: artifact `10471412596`, digest `sha256:eb3326352046340a272303e9968a4eb4b54fb6356e52c569dc8302ff20ba8173`;
- root 13 / Python 3.13: artifact `10472357089`, digest `sha256:9232c2eec657af8a4c438d0bb68805f528a9eefe7400b0190ebd6408169c7250`;
- root 14 / Python 3.13: artifact `10472465709`, digest `sha256:fc8291101b8355b693869f5165e1f8830f1f3a413e6a49bab6895407f751d354`;
- root 15 / Python 3.13: artifact `10472166412`, digest `sha256:d56b08c876d6260fa38a3dcef1565b918c54bdf475ebf3d4f2b1c826f704da34`;
- assembled Python 3.11: artifact `10471709668`, digest `sha256:877dbe38d12983d9395de8a2e0a239d2cd850944eb34fb541041276e662a8c2d`;
- assembled Python 3.13: artifact `10472665406`, digest `sha256:546c6c8a57cce18fef31d365ff8b159e42e45700b11de9f73d4a741b02ad908d`;
- aggregate: artifact `10473120351`, digest `sha256:a2ffc639688f9098e4db9abbcc457c347ab23520e83384bb1bcb106807738205`.

Both assembled JSON payloads are byte-identical with SHA256:

`9036ced6bb7b252fab5c2b147ef652fe2ee817bc7d49c07f7f8114c6ead17837`.

Authoritative aggregate JSON SHA256:

`1b5efd75522ee9389ee805c84a0fb86b71fc64bf52b2a114ee21e97a2c2fc029`.

Internal aggregate payload SHA256:

`3e06be81c7b88506e6617e18e43469bde3ac8ba98d96eef314bef48e5ea51c1d`.

## Exact terminal result

Frozen cohort remained exactly boxes `13,14,15`, causal `0to5`, block `0`, path `2`, direction `[1,1,1,-1,-1,-1]`, sign `+1`, all four frozen rhos and R grid `[6,8,10,12]`.

All three exact rational covers are valid. Every root model was built exactly once; descendant derivative recomputation is false; all `243` channels are retained; root controls pass.

Terminal tree totals:

- total nodes: `5829`;
- total leaves: `2916`;
- certified leaves: `24`;
- unresolved depth-10 leaves: `2892`;
- per-root leaf counts: `972,972,972`;
- depth histogram: depth 6 = `6`, depth 7 = `6`, depth 8 = `6`, depth 9 = `6`, depth 10 = `2892`.

Global terminal extrema:

- maximum `drift_upper = 0.6136407189670734`;
- witness: root box `15`, depth `10`, amplitude `[31/12800,6349/2621440]`, status `UNRESOLVED_DEPTH10`, max possible channel count `46`;
- minimum terminal `S_lower = 3.7043291995581735`;
- maximum terminal possible-max count = `46`.

Per-rho worst terminal drift is approximately:

- rho `0.35`: `0.10312107571542181`;
- rho `0.9`: `0.1493282089739344`;
- rho `1.6`: `0.6136407189670734`;
- rho `2.7`: `0.475434136127578`.

Thus the frozen robust slope floor remains comfortably positive on the diagnostic, but the unchanged `0.05` continuous-drift condition remains violated on many depth-10 leaves.

## Independent adversarial Critic

An independent raw-leaf Critic reconstructed the three exact dyadic covers, root identities, full-binary-tree node invariant, leaf/depth counts, all-rho certification rule, root depth-zero regression to terminal Iter504, all-243-channel/no-pruning controls, maximum drift, minimum slope, and final classifier from the two terminal assembly payloads rather than trusting the aggregate verdict.

Critic result:

`CRITIC_CONFIRMS_ITER504R_INCONCLUSIVE_SCOPED`.

- assembly A SHA256: `9036ced6bb7b252fab5c2b147ef652fe2ee817bc7d49c07f7f8114c6ead17837`;
- assembly B SHA256: `9036ced6bb7b252fab5c2b147ef652fe2ee817bc7d49c07f7f8114c6ead17837`;
- Critic payload SHA256: `cd640f81b2313c6ca02815f51903f4cd54ac50e6830fb90a17c2022e5dbdb11d`;
- persisted Critic JSON file SHA256 before repository serialization: `218eca047dcc8a8563910c8038a134752a99d783ddd00f4776c7fa1462fb9ea2`.

Negative controls were all rejected: missing leaf, duplicate leaf, gap, overlap, wrong root endpoint, omitted channel, changed threshold, changed floor, depth > 10, descendant derivative recomputation, outcome-dependent leaf removal, wrong rho, wrong box, altered path and altered sign.

## Scientific meaning

Iter504R answers the frozen localization question in the INCONCLUSIVE branch: narrowing only `delta` while reusing the full-root derivative enclosure is **not sufficient** to bring the rigorous continuous drift below `0.05` on the frozen crossing diagnostic by depth 10.

The residual uncertainty is therefore localized to the width of the frozen root derivative enclosure and/or nonsmooth max-channel competition/crossings. This is substantially more informative than the parent Iter504 INCONCLUSIVE state because point-grid drift was already small in Iter504P and delta-only refinement has now been ruled out as a sufficient remedy on this diagnostic.

## Claim ceiling

This is only a three-root-box one-dimensional signed-direction diagnostic. It does not reclassify the full 1888 Iter504 inconclusive states, does not establish absolute-Haar divergence, does not close D7-S2/S3/S4, does not authorize selector labels, does not activate Candidate Gravity, and does not establish a quantum-gravity solution or new physics.

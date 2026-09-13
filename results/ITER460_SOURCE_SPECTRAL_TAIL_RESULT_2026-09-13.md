# Iter460 source spectral-tail result — PASS (scoped)

- Workflow run: `34748501676`
- Head: `f61965f9e1c3533398531c9be14d4700c78b4b76`
- Summary artifact: `10314837771`
- Artifact digest: `sha256:ce4f1a8a18c6c8282dad4a7f424f322e0e5133c926dfb327ce0c68f7f34163d0`
- Classification: `ITER460_SOURCE_P11_D_TAIL_CHARACTERIZED_SCOPED`
- Records: **24/24 PASS**
- Maximum `P11` route relative disagreement: `8.795034170402503e-16`
- Maximum frozen tail-power fit instability: `0.09444309500782455` (contract ceiling `0.20`)

## Main result
On the frozen radii `[40,80,160,320,640]`, width-40 envelope windows, both signs of the spectral tail, `rho in {0.35,1.60}`, `beta in {0.80,2.10}`:

- `m=0`: fitted four-window slope of `|P11*d_source|` is about `+0.837 ... +0.845`;
- `m=+/-1`: fitted four-window slope is about `+1.671`;
- `d_source` alone decays approximately as `R^-2` for `m=0` and `R^-1` for `m=+/-1` on this frozen panel;
- multiplication by the cubic source polynomial produces a growing oscillatory envelope rather than a Schwartz/L1 tail.

Therefore the Iter459 Sokhotski-Plemelj qualification on Schwartz test functions cannot simply be promoted to the source-specific `P11*d_source` object without an additional oscillatory/distributional/contour construction.

## Claim lock
This is **not** a proof of physical causal-vertex divergence. It is a source-tail regularity classification. D7-S2 remains open, D7-S5 remains NOT_AUTHORIZED, Candidate Gravity remains inactive.

# SOURCE_J1_COHERENT_MAGNETIC_TOLLER_BRIDGE_V3 — terminal result

Date: 2026-09-15
Status: `TERMINAL_SCOPED`
Classification: `SOURCE_J1_COHERENT_MAGNETIC_TOLLER_BRIDGE_CONFIRMED_SCOPED`

## Authority chain

- prospective preregistration: `research/prereg/SOURCE_J1_COHERENT_MAGNETIC_TOLLER_BRIDGE_V3_2026-09-15.md`
- prereg commit: `9bfcbeb0048e8e3ea75032a394dafcc8986c7f68`
- corrected pre-implementation source transcription: `inputs/source_j1_coherent_magnetic_toller_bridge_v3.json`
- source-input commit: `98034792ccd2f87e05ab0d9b4fde46cd1bcf3033`
- exact implementation: `code/source_j1_coherent_magnetic_toller_bridge_v3.py`
- implementation commit: `ab7b4732ef5123922e71e1780a5a5d9580877863`
- workflow launch commit: `49ec33f5fa71b71d9924b551c3c904e2edf03e54`
- authoritative Actions run: `35017297255`
- source-lock job: `104543837299` — `success`
- exact Python 3.11 lane: `104544198307` — `success`
- exact Python 3.13 lane: `104544198439` — `success`
- aggregate job: `104544570623` — `success`
- aggregate artifact: `10415708250`
- aggregate artifact digest: `sha256:09268182961e09b3413d13684526574c1924d6aa37f17b39a9d65477907cabc1`

## Frozen source authority

Primary sources consumed by the prospectively frozen gate:

1. Bianchi–Chen–Gamonal, `Causal spinfoam vertex for 4d Lorentzian quantum gravity`, arXiv:2601.23162v1: Eq. (3), Eq. (4), Appendix C Eq. (C2), Eq. (C4), Eq. (C5), Appendix D Eq. (D1)–Eq. (D4).
2. Bianchi–Chen–Gamonal, `Toller matrices and the Feynman i epsilon in spinfoams`, arXiv:2604.24945v1: Eq. (1)–Eq. (4), Eq. (13), Eq. (15)–Eq. (20), uniqueness statement following Eq. (20).

Frozen canonical formula digest:
`sha256:a54741269fc4da8cd039a113b0cc2d7ada240f4bbf361265d881382e6248b3cd`.

## Terminal controls

The aggregate required two independent exact-symbolic lanes to agree. Both returned the frozen PASS label and identical controls/source digest/phase proof/span determinant.

Controls passed:

- exact source selector/transcription lock;
- exact `j=l=k=1`, real-`rho` phase triviality `Phi(rho;1,1)=1`;
- exact `j=1` coherent-state normalization on the frozen spinors;
- exact coherent-state spanning control, including a complex-phase spinor;
- exact generic `3x3` magnetic/coherent basis-transform identity;
- formal exact Feynman-projector linearity with coherent coefficients independent of the spectral integration variable;
- exact source orientation `g_b^{-1}g_a` and wedge sign `sigma_a sigma_b`, with reversed/sign-flipped fixtures rejected;
- exact source antilinear map `J(z0,z1)=(-conjugate(z1),conjugate(z0))`, with wrong-`J` fixture rejected;
- negative residual-phase / wrong-`j,l` fixtures rejected;
- additive `T_plus + T_minus = D` guard preserved through the coherent basis transform;
- scope firewall: no K5 contraction or channel coefficient was computed by this gate.

Aggregate output:

`SOURCE_J1_COHERENT_MAGNETIC_TOLLER_BRIDGE_CONFIRMED_SCOPED`

with `all_controls_pass=true`, `same_controls=true`, `same_source_digest=true`.

## Scientific fact established

Within the frozen lowest-spin one-wedge scope `j=l=k=1`, real nonzero `rho`, and the source branch/orientation conventions, the source-authoritative coherent-basis Toller distribution is connected to the magnetic-basis Toller matrix by the exact coherent-state basis transform without a residual phase mismatch.

This resolves the representation/convention part of the earlier repository-local `SOURCE_DERIVATION_BLOCKED_SCOPED` V2 result. It does **not** rewrite that historical V2 result: V2 correctly established insufficiency of its then-frozen repository corpus; V3 expanded authority prospectively to the two primary 2026 sources.

## Independent adversarial qualification opened before promotion

Before using this PASS to launch a K5 contact contraction, an outcome-independent verifier was prospectively frozen and launched:

`SOURCE_J1_TOLLER_PROJECTOR_KERNEL_EQUIVALENCE_V3K`.

It checks explicitly that the gamma-ratio projector kernel of arXiv:2601.23162v1 Eq. (3) is exactly the finite-product kernel of arXiv:2604.24945v1 Eq. (20) at `j=l=1`. The V3 terminal classification remains valid under its frozen contract, but downstream promotion is voluntarily deferred until V3K is terminal.

## Interpretation ceiling

This result establishes only the one-wedge coherent↔magnetic Toller representation/convention bridge in the frozen `j=1` scope. It does not establish:

- a channel-`00000` K5 contact coefficient;
- contact survival/cancellation after K5 contraction;
- Eq. (4) distributional existence/nonexistence;
- absolute or ordinary convergence;
- any model/family FAIL;
- D7-S2/S3/S4 closure;
- any terminal selector;
- Candidate Gravity activation.

Governance remains:

- `RQIR Core v1.0 = FROZEN`
- `D7-S2 = NOT_CLOSED`
- `D7-S3 = NOT_CLOSED`
- `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`
- terminal selectors forbidden
- Candidate Gravity inactive
- KMQGB downstream of pinned DSIR authority.

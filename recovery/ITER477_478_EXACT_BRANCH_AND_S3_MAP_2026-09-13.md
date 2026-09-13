# Iter477–478 exact branch / LQG-S3 front — 2026-09-13

Repository/source artifacts remain authoritative. D7 remains fail-closed.

## Iter477 — exact source Toller beta->0 individual-branch singular order — PASS scoped
- branch `research/iter477-toller-exact-beta0-singular-order`
- prereg `afc444ee8b458cbad2f88224a11cf61d34943c5e`
- implementation `f77b2a7ac7992b29780d81ecb84a304599954d58`
- launch head `c80e9dfdcd58fe03b1008ab013e3d5f7449e7c9f`
- run `34772546243`, SUCCESS
- artifact `10322307672`, digest `sha256:2c4e747456dc859ab95b91678fd59bbd40c43266f216cb49f8032704106b1b5c`
- classification `ITER477_SOURCE_TOLLER_EXACT_BETA0_BRANCH_ORDER_2JPLUS1_QUALIFIED_SCOPED`

All four frozen checks passed:
- exact source-parameter identity `a+b-c = 2j+1` for both Toller branches;
- DLMF leading coefficients including the source Gamma prefactors are finite and nonzero on the frozen EPRL panel;
- the correctly scaled ratio approaches its unit asymptotic value monotonically over beta={0.05,0.025,0.0125};
- wrong exponents `N-1` and `N+1` are separated in every frozen record.

External mathematical authority is NIST DLMF 15.4.23: for `Re(c-a-b)<0`, the Gauss hypergeometric function has leading `(1-z)^(c-a-b)` behavior with the explicit Gamma coefficient. The published source Toller parameters satisfy `c-a-b=-(2j+1)`, and `1-exp(-2 beta) ~ 2 beta`. Therefore each individual source Toller branch has exact one-wedge local order
`T^(+/-) ~ beta^(-(2j+1))`
in the qualified scope. In particular j=2 gives order 5 and j=5 gives order 11.

Numerical confirmation details: maximum direct-series work was 7323 terms; at beta=0.0125 correct-order scaled-ratio residuals ranged approximately 0.0542–0.4795, while both wrong-exponent controls were farther from unit scaling for every record. Recombined `t_+ + t_-` remains approximately 0.9902–0.9987 in magnitude on the same smallest-beta panel while individual branches reach roughly 1.15e4–4.22e10, consistent with strong additive cancellation.

Scope lock: this is an **individual one-wedge branch** singular order. It is not a K5 contracted collision exponent, does not prove that invariant/intertwiner/group contractions preserve the leading coefficient, and is not a causal-vertex divergence theorem. The recombined noncausal identity cannot silently replace a fixed causal branch.

## Iter478 — LQG/EPRL D7-S3 minimal bridge map — PASS audit; all five bridge classes OPEN
- branch `research/iter478-lqg-s3-minimal-bridge-map`
- prereg `9951d7fbcf50acd1135c8152dcdd7b6e505ba022`
- implementation `cd667f30a2211c42490bd766bcdd2b9c52d4da5a`
- launch head `bda8042fdfdd831d8589ec1b2a6ed491e76825ec`
- run `34772636331`, SUCCESS
- artifact `10322566515`, digest `sha256:72ade38c061fb49a8d11a9922efc743c3c0609d6b4537625459192d868d57382`
- classification `ITER478_LQG_S3_MINIMAL_BRIDGE_MAP_COMPLETE_SCOPED`

All six frozen authority files were found and all five bridge classes resolved reproducibly. Every class is `OPEN_EXPLICIT_SOURCE_BLOCKER`:
1. `UV_IR_SAME_REALIZATION_IDENTITY_AND_PARAMETER_MAP` — endpoints exist, but `same_realization_terminal_bridge_ready=false`, parameter transport and normalized-observable transport remain missing.
2. `PHYSICAL_STATE_SIGNATURE_STACK_TRANSPORT` — physical-state and explicit Euclidean/Lorentzian vertex bridges exist, but same-real-gamma identity, rigging-map transport, complete-stack transport and same-realization chain readiness remain false.
3. `CONTINUOUS_SHARED_STACK_UV_TO_GR_TRANSPORT` — shared Lorentzian stack/observable anchors exist, but `continuous_same_realization_transport_ready=false`.
4. `NORMALIZED_OBSERVABLE_AND_PROPAGATED_ERROR_TRANSPORT` — scoped gamma observable/parameter bridge exists, but complete-stack UV/IR transport and normalized observable with full propagated QG error remain false.
5. `CAUSAL_TOLLER_GLUE_FINITE_NORMALIZED_STACK_TO_REGGE_GR` — additive Toller completion recovers D, but fixed-branch representation composition is unavailable, causal-stack finiteness/normalization/cutoff control is unproven, and UV->Regge/GR same-realization transport is unproven.

Thus D7-S3 remains `NOT_CLOSED`. OPEN means a missing certificate/bridge, not impossibility.

## Locked state
- D7-S2 = NOT_CLOSED.
- D7-S3 = NOT_CLOSED.
- D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED.
- D7-S5 = NOT_AUTHORIZED.
- Candidate Gravity = inactive/false.
- terminal labels remain unauthorized.

## Working readiness rubric
Keep `D2≈82%`, `D4≈68%`, `D7≈56%`, integrated `≈67%` until a frozen D7 prerequisite actually closes. These percentages are workflow/readiness heuristics, not scientific probabilities.

## Next high-information S2 gate
Combine Iter477 with the already qualified Eq.(7) magnetic reconstruction: if every diagonal leading coefficient is nonzero and the left/right SU(2) reconstruction matrices are invertible/unitary, test whether the full leading magnetic coefficient matrix is necessarily nonzero/full-rank. A positive result would only rule out cancellation internal to a single-wedge magnetic reconstruction; it would still leave intertwiner, multi-edge, angular and group-integration cancellations open.

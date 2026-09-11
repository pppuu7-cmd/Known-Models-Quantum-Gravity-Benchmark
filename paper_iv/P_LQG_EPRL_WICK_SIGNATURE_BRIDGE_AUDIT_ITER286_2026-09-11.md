# Iter286 — EPRL Wick/signature bridge audit
Date: 2026-09-11

Primary authority: Pietro Donà, Francesco Gozzini, Gianluca Nicotra, *Wick rotation for spin foam quantum gravity*, Phys. Rev. D 104, 126008 (2021), DOI `10.1103/PhysRevD.104.126008`, arXiv:2106.14672.

## Prospective audit
Four independent source-contract guards were executed in parallel with `fail-fast:false`, `max-parallel:4`:
1. existence of an explicit Euclidean↔Lorentzian EPRL vertex analytic continuation;
2. Immirzi-domain behavior under the continuation;
3. vertex/fixed-complex scope versus rigging-map/complete-stack scope;
4. compatibility with the Iter284 physical-state component and Iter283/285 Lorentzian chain.

Scientific workflow `34557396727`: 4/4 guards + aggregate `SUCCESS`.
Methodology CI `34557396730`: preflight + 4/4 shards + aggregate/bundle `SUCCESS`.
Reproducibility release `34557551569`: `SUCCESS`.
Aggregate digest: `sha256:8ff5a0004e5de88b72f1a3b1ef50bb469ec2b09a961d6e59171b901e616969d6`.

## Aggregate result
- `explicit_euclidean_lorentzian_vertex_map = true`;
- `structural_signature_bridge = true`;
- `same_real_gamma_identity = false`;
- `rigging_map_transport_ready = false`;
- `complete_stack_transport_ready = false`;
- `same_realization_chain_ready = false`.

Canonical classification:
`HIGH_VALUE_EPRL_SIGNATURE_ANALYTIC_CONTINUATION_BRIDGE__REAL_GAMMA_PHYSICAL_STATE_AND_COMPLETE_STACK_TRANSPORT_STILL_OPEN`

Guard classifications:
- `PASS_EXPLICIT_EUCLIDEAN_LORENTZIAN_EPRL_VERTEX_ANALYTIC_CONTINUATION`;
- `PASS_SIGNATURE_MAP_REQUIRES_IMMIRZI_ANALYTIC_CONTINUATION__NO_SAME_REAL_GAMMA_IDENTITY`;
- `PASS_VERTEX_LEVEL_SIGNATURE_RELATION__RIGGING_MAP_AND_COMPLETE_STACK_TRANSPORT_NOT_ESTABLISHED`;
- `PASS_HIGH_VALUE_SIGNATURE_BRIDGE_COMPONENT__NO_YANG_TO_HAN_REAL_GAMMA_STATE_AND_STACK_TRANSPORT`.

## Interpretation
The Euclidean/Lorentzian signature gap is narrower than after Iter284: an explicit EPRL vertex-level analytic continuation exists. This is a material structural bridge, not a terminal transport certificate. The published continuation analytically continues the Immirzi parameter rather than proving identity in the same real-`gamma` quantum realization; it does not transport the scoped Yang–Zhang–Ma rigging map over the full physical state space and does not establish equality/transport to the Lorentzian complete spinfoam-stack amplitude used in the Iter283/285 chain.

LQG/spinfoam remains `PARTIAL/BLOCKED`; no family-level PASS/FAIL and no D7 terminal classifier is authorized.

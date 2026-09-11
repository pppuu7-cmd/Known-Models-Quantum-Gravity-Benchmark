# Recovery Delta 284 — LQG canonical/covariant physical-state link compatibility

Date: 2026-09-11

## What changed
Yang–Zhang–Ma 2021 was audited as a possible physical-state component of the Iter283 LQG UV-to-IR bridge rather than being silently concatenated into the Lorentzian chain.

Primary source: *Relating spin-foam to canonical loop quantum gravity by graphical calculus*, Phys. Rev. D 104, 044025 (2021), DOI `10.1103/PhysRevD.104.044025`, arXiv `2102.05881`.

Workflow `lqg-physical-state-link-compatibility-audit`, run `34556068228`:
- physical-state / rigging-map content guard;
- Euclidean-vs-Lorentzian signature guard;
- `beta=1` / certain-state scope guard;
- compatibility with the Iter283 Lorentzian UV-to-IR chain.

All 4 independent guards + aggregate = `SUCCESS`.
Methodology CI `34556068266` = `SUCCESS`.
Aggregate digest: `sha256:61a71ea3aab1fa23b58ad2760b27500c84f34ac62aca5d020526516125cb7d47`.

## Scientific result
`HIGH_VALUE_EUCLIDEAN_BETA1_RIGGING_MAP_COMPONENT__NO_EXPLICIT_COMPATIBLE_TRANSPORT_INTO_LORENTZIAN_UV_IR_CHAIN`

Positive scoped facts:
- rigging-map interpretation exists in the declared generalized Euclidean EPRL scope;
- the Euclidean Hamiltonian constraint is weakly satisfied on certain states;
- the result supplies a real canonical/covariant physical-state consistency component.

Remaining scope/transport gaps:
- Euclidean rather than Lorentzian realization;
- `beta=1` rather than generic Immirzi parameter;
- certain states rather than a full state-space certificate;
- no explicit state/signature/parameter map into the 2017/2026 Lorentzian chain;
- no normalized gravity observable transported through the full UV-to-IR chain.

Thus LQG now has a stronger three-component evidence picture (physical-state link + GR endpoint + UV endpoint), but the compatible same-realization transport among them remains missing.

## Global state
- Tier-1 = 15.
- strict terminal = 1/15.
- candidate-QG terminal = 0/14.
- D7 = NOT_CLOSED / NOT_YET_AUTHORIZED.
- Candidate Gravity remains inactive; R3 = 24%.

## Publication handoff
- Paper III: `NOT_NEEDED`.
- Paper IV: `READY`; add the scoped rigging-map result and preserve the Euclidean / `beta=1` / certain-state / weak-constraint boundaries and missing Lorentzian transport.

## Next front
Search specifically for a Lorentzian or generic-Immirzi canonical/covariant physical-state construction and/or an explicit map from the 2021 rigging-map sector into the Han 2017/2026 amplitude chain. In parallel retain the external Asymptotic-Safety contact-complete `s+t+u+A4` front.

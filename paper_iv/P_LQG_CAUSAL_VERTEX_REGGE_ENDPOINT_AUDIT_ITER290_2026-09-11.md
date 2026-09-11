# Iter290 — LQG causal Lorentzian vertex / Regge endpoint audit
Date: 2026-09-11

Primary authority: Eugenio Bianchi, Chaosong Chen, Mauricio Gamonal, *Causal spinfoam vertex for 4d Lorentzian quantum gravity*, arXiv:2601.23162 (2026-01-30).

Frozen family context: the LQG/spinfoam row is already `PARTIAL/BLOCKED`. Iter281–288 established complete-stack/refinement machinery, a physical-continuum certificate adapter, scoped physical-state evidence, a small-spin Lorentzian complete-stack UV endpoint, a large-spin/refinement Einstein endpoint, a Lorentzian entropy anchor, and a nonempty small-gamma semiclassical hierarchy overlap. The decisive missing object remains controlled same-realization UV-to-IR/GR transport with parameter identity, normalized observable, comparator and propagated uncertainty.

## Prospective audit
Four independent guards were run in parallel with `fail-fast:false`, `max-parallel:4`, followed by an explicit aggregate barrier:
1. causal Toller split identity at vertex scope;
2. large-spin Lorentzian Regge / single causal phase endpoint;
3. vertex-scope versus complete-stack boundary;
4. preservation of the frozen UV-to-IR transport blocker.

Scientific workflow `34561212081`: all four guards + aggregate `SUCCESS` on head `a6cbecf7507adb9dc52dc0090d171905e1432b50`.
Summary artifact `10184373486` (`lqg-causal-iter290-summary`), artifact digest `sha256:ee0ba2168b4ea3113517fadc94abdac82dcfd9c1bfbafff94a686ef3a1e264ec`.
Raw aggregate digest: `sha256:573a5590ffe7a4bfcd298f0a14c13e77c5a034a31bc8d69b280b17dd23493b02`.

## Aggregate result
- causal Toller split identity at vertex scope = PASS;
- large-spin causal data select a Lorentzian Regge endpoint with a single `exp(+i S_Regge / hbar)` phase = PASS;
- complete-stack/refinement transport supplied by this authority = false;
- same-realization UV-to-IR parameter transport ready = false;
- family terminal = false;
- D7 authorized = false;

Canonical classification:
`HIGH_VALUE_CAUSAL_LARGE_SPIN_LORENTZIAN_REGGE_ENDPOINT__NO_COMPLETE_STACK_SAME_REALIZATION_UV_TO_IR_TRANSPORT`

Guard classifications:
- `PASS_CAUSAL_TOLLER_SPLIT_IDENTITY_AT_VERTEX_SCOPE`;
- `PASS_CAUSAL_LARGE_SPIN_SINGLE_PHASE_LORENTZIAN_REGGE_ENDPOINT`;
- `PASS_SCOPE_BOUNDARY__VERTEX_RESULT_NOT_COMPLETE_STACK_TRANSPORT`;
- `PASS_BLOCKER_PRESERVATION__UV_TO_IR_PARAMETER_TRANSPORT_STILL_MISSING`.

## Interpretation
This materially strengthens the IR/semiclassical side of the LQG/spinfoam near-bridge. The previously established large-spin Einstein/Regge endpoint now has an explicit Lorentzian causal vertex realization whose asymptotics select causal Lorentzian Regge data with a single phase, reducing ambiguity about whether the desired endpoint can be represented causally at EPRL-vertex scope.

It does **not** close the frozen family blocker. The paper is vertex-level and does not demonstrate a complete-stack/refinement trajectory from the Iter287 small-spin UV fixed-point sector to the causal large-spin Regge/Einstein sector. It does not by itself supply one continuous coupling/Immirzi/spin-scale map, a normalized observable transported along that trajectory, a same-domain comparator residual, or propagated theory/numerical uncertainty.

Therefore LQG/spinfoam remains `PARTIAL/BLOCKED`, not FAIL and not family-level PASS. The missing object is sharpened to a complete-stack same-realization transport certificate connecting the established Lorentzian UV/entropy sector to the now explicitly causal large-spin Regge/Einstein endpoint while preserving parameter identity and comparator/error closure.

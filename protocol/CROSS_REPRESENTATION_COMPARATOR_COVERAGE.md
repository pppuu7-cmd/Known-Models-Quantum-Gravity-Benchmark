# Cross-Representation Comparator Coverage Matrix

**Status:** frozen comparator-coverage methodology / no Candidate Gravity promotion.  
**Purpose:** identify which strong comparator classes can currently populate scattering, CTP/real-time and relational/channel blocks under one parent, and prevent missing comparator representations from being silently interpreted as zero.

## Representation columns

- `R_S`: in-out scattering / physical cross section / helicity amplitude;
- `R_CTP`: in-in/retarded/spectral/noise/ordered real-time object;
- `R_REL`: relational detector/phase/tidal/quantum-channel observable;
- `R_LINK`: same-realization parameter/renormalization map tying the populated representations together.

States:

- `PASS_SCOPED`: a concrete object exists in the declared scope;
- `PARTIAL`: related objects exist but not the complete required block;
- `BLOCKED_MISSING_OBJECT`: no authoritative object frozen for this use;
- `BLOCKED_SAME_REALIZATION_LINK`: representations exist separately but their shared-parameter map is not frozen strongly enough;
- `N_A_BY_MODEL_CLASS`: the representation is not a fundamental degree of freedom of that comparator class, which may itself be a discriminating model-class fact but is not numerical zero.

## C5 — perturbative quantum GR / gravity EFT

- `R_S`: `PASS_SCOPED` — standard graviton/matter scattering and EFT amplitudes;
- `R_CTP`: `PASS_SCOPED` — graviton influence functional, retarded/Hadamard/noise kernels and reduced dynamics exist in perturbative quantum GR;
- `R_REL`: `PARTIAL/PASS_SCOPED` depending on chosen detector/probe model;
- `R_LINK`: `PASS_IN_PRINCIPLE__MUST_MATCH_ORDER_STATE_SCHEME`.

**Consequence:** C5 is the primary cross-representation null comparator. A KG relation must not merely reproduce generic QFT consistency between scattering and real-time kernels.

## Asymptotic safety / Lorentzian FRG

Current 2026 evidence includes

- concrete graviton-mediated `2->2` scalar scattering with momentum-dependent vertices and Lorentzian reconstruction;
- positive Lorentzian graviton spectral functions with massless graviton peak and multigraviton continuum;
- momentum-dependent quantum effective-action information.

Thus

- `R_S`: `PASS_SCOPED_SCALAR_SCATTERING`;
- `R_CTP`: `PARTIAL_SPECTRAL_RETARDED`;
- `R_REL`: `BLOCKED_MISSING_OPERATIONAL_CHANNEL_OBJECT`;
- `R_LINK`: `BLOCKED_SAME_REALIZATION_LINK` until one prospectively frozen parameter/renormalization map ties the relevant scattering and real-time blocks in the exact benchmark representation.

Do not treat the missing link as zero.

## Type-II/string-like UV completion

- `R_S`: `PASS_STRONG` for tree-level four-graviton/Virasoro-Shapiro and broader amplitude structure;
- `R_CTP`: `BLOCKED_MISSING_FROZEN_REALTIME_GRAVITATIONAL_BLOCK` for the current KMQGB operational target;
- `R_REL`: `BLOCKED_MISSING_FROZEN_OPERATIONAL_CHANNEL_OBJECT`;
- `R_LINK`: `BLOCKED` for the KMQGB cross-representation benchmark.

String remains a mandatory structural scattering comparator; missing operational blocks do not authorize a KG victory.

## C2 stochastic gravity

- `R_S`: `N_A_BY_MODEL_CLASS` for a fundamental quantum-graviton S-matrix;
- `R_CTP`: `PASS_SCOPED` for mean/noise/dissipation stochastic kernels;
- `R_REL`: `PASS/PARTIAL` for stochastic detector consequences;
- `R_LINK`: `PASS_SCOPED_CLASSICAL_STOCHASTIC`.

C2 remains a strong null for symmetrized noise/spatial-correlation sectors but not for a non-entanglement-breaking quantum spin-2 mediator.

## C3/C3b classical-channel / postquantum classical gravity

- `R_S`: `N_A_BY_MODEL_CLASS` for a fundamental quantum-graviton S-matrix;
- `R_CTP`: `PASS/PARTIAL` for classical-CQ stochastic/channel dynamics;
- `R_REL`: `PASS_SCOPED` for force/noise/decoherence/channel predictions;
- `R_LINK`: `PASS_SCOPED` where the concrete model is fully frozen.

These comparators are mandatory for operational nonclassical-interface claims.

## C4/C6 ordinary quantum mediator/source alternatives

- `R_S`: `PASS_SCOPED` for ordinary quantum mediator scattering where defined;
- `R_CTP`: `PASS_SCOPED` as ordinary quantum environments have real-time correlators/influence functionals;
- `R_REL`: `PASS_SCOPED` for quantum-channel/entanglement transfer;
- `R_LINK`: `PASS_IN_PRINCIPLE__MODEL_SPECIFIC`.

They remain mandatory for mediator attribution. Gravity-specific spin-2/Ward/universality anchors are required to exclude them.

## Coverage rule for KG promotion

A candidate cross-representation residual cannot be promoted merely because one comparator has `BLOCKED_MISSING_OBJECT` in one representation.

Promotion requires either

1. a same-domain comparator block showing separation; or
2. a theorem/structural model-class obstruction proving that the comparator cannot realize the claimed linked relation under its own assumptions.

Otherwise the relevant comparator branch remains `BLOCKED`.

## Current conclusion

Cross-representation rigidity is most immediately actionable against

- full C5;
- C4/C6 mediator alternatives;
- C2/C3/C3b operational nulls.

String and asymptotic-safety comparisons remain partly blocked at the exact multi-representation level even though strong scattering/spectral subobjects exist.

The strongest future candidate should therefore derive a linked vector that

1. survives the fully populated C5/C4/C6/C2/C3 family first;
2. has enough structural scattering information to compare against string-like/AS subspaces;
3. remains explicitly `BLOCKED` rather than claiming uniqueness where a strong comparator representation is missing.

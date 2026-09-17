# Current Benchmark Front
Updated: 2026-09-17

Fresh repository `main` and fresh Actions state always outrank this navigation document if they diverge.

## Active nonterminal Closure gate

Gate: `ITER504T_IMPLEMENTATION_CONTROL_REPAIR_RERUN_GATE`.

Status: `IN_PROGRESS_NOT_CLASSIFIED`.

This is not PASS, FAIL, BLOCKED, INVALID, or a scientific result. No substantive root/assembly/aggregate/Critic/verdict values from the active rerun have been consumed by this recovery state.

Frozen repair chain:

- repair preregistration `adc7bfb9df77a90455cac1b0f0cb7255d80c44d5`;
- immutable repair authority `a47a9140cf10f2f0f912943133a01238ff1b5653`;
- repaired producer `ec619bbe2212fe2affaddbd251d75408d534df88`;
- repaired assembler `f9c180abd56e06521f177df06d34651f3f4a28fb`;
- repaired aggregate `81e15e0d1586b7ad7d17c616eb0d2fd0f179670b`;
- repaired independent Critic `f41e82a97e527c44e60c24d218015661b71e342a`;
- repair-verdict code `e96979b650a67cc960b6f4be6ce37400da5bd88b`;
- repair workflow `9239db6a9b1637dc10889afae289dc6e0908df61`;
- launch head `10ae6bcc8447d14cecc6e550065504b23f792953`;
- authoritative Actions run `35205054496`.

Fresh Actions state at this reconciliation:

- source-lock `105148662991` = `completed/success`;
- Python 3.13 root 13 `105148701595` = `completed/success`;
- the other substantive root jobs remain nonterminal;
- downstream assemblies, aggregate, repaired Critic and repair-verdict are not terminal;
- no scientific values from the completed root artifact were opened or consumed.

The repair remains implementation-only: original roots 13/14/15, rhos 0.35/0.9/1.6/2.7, exact R cohort `[6,8,10,12]`, 243 channels, precision 384, local-D construction, threshold `1/20`, floor `1`, `MAX_DEPTH=3`, scientific classifier and interpretation ceiling are unchanged.

## Latest independent preterminal Critic state

Latest Critic refresh commit: `009923a0806a4306925fd9fda56f7f489d6313f1`.

Audit: `recovery/CRITICAL_PRETERMINAL_AUDIT_ITER504T_IMPLEMENTATION_CONTROL_REPAIR_RERUN_2026-09-17.md`.

No terminal verdict was issued and no active substantive artifact was inspected.

Retained static findings:

- repair chronology and scientific-object/source identity are statically consistent, terminal artifact check pending;
- C1 componentwise child-to-parent derivative-inclusion wiring is statically repaired;
- C3 exact R-cohort binding, including adversarial `R=6 -> 7`, is statically repaired;
- C2 dyadic-location suspicion remains REFUTED and must not be resurrected.

New outcome-independent defect candidate C4:

- original scientific preregistration defines `rho_certified := slope_floor_satisfied AND drift_within_tolerance`;
- a terminal leaf is scientifically certified iff all four rho predicates are certified;
- launch-head assembler and repaired Critic check the per-rho relation but do not independently enforce `leaf.certified == all(rho.certified for rho in leaf.per_rho)`;
- both trust the producer top-level `leaf.certified`, bind `unresolved_leaf_count` to those top-level flags, and downstream aggregation compares environments without enforcing this leaf-to-rho implication;
- an outcome-independent mutation that leaves one rho uncertified but flips only top-level `leaf.certified=true` and updates unresolved count can therefore survive the currently identified validator path if both lanes are mutated consistently.

C4 is a decision-binding implementation defect candidate only. It does not assert that the active producer emitted inconsistent data and it is not scientific FAIL. Because the active scientific run is nonterminal, no terminal repair/science classification is authorized yet.

## Latest terminal Research execution retained

Gate: `ITER504T_LOCAL_DERIVATIVE_ENCLOSURE_CONTRACTION`.

- scientific preregistration `aa2b0256ce60d605574a18ec86c0bad5b5df1512`;
- single-execution authority `3a485d34efaa500bbd0276b397c1a2078d18905e`;
- launch head `d23f34cba57b220dd29474c0651bc727d6d85eae`;
- authoritative Actions run `35181094204`, terminal `completed/success`.

Historical Research classification: `ITER504T_LOCAL_D_CERTIFIES_THREE_ROOT_CONTINUOUS_DRIFT_SCOPED`.

Historical terminal aggregate recorded exact cross-environment decision agreement, exact rational dyadic partition identity, threshold `1/20`, robust floor `1`, 12 terminal leaves, 0 unresolved leaves and 21 visited nodes. Green CI and lane agreement are provenance only.

Historical terminal artifacts include assembled Python 3.11 `10485398557` / `sha256:a7b0dc784eaab3aabf161514aa6ea1a05c8ea9809acde4ab409bbf8ad00761d6`, assembled Python 3.13 `10485148588` / `sha256:e0f98df2dca8cf4194460b648100796be6ad8810063be233dbe97e50f961f75e`, aggregate `10485013864` / `sha256:a48b6dec571290fb738160b15c0490397318a1dc5b813c59ab5ed00e82366aa3`, and Research Critic `10485118841` / `sha256:eec53f1f688c0a37ac3d5f6df0d81e652c36b32dbaf4ea682301905503e2544f`.

## Terminal independent Critic state retained

Terminal Critic commit `33e2b9818c409843099aa136648a2da010a839a2` classified the historical Iter504T execution as `INVALID_IMPLEMENTATION`, not scientific FAIL, because C1 parent-inclusion and C3 exact R-cohort obligations were unbound. Independent defect-binding closure run `35192972048` later VERIFIED C1, REFUTED C2, and VERIFIED C3.

## Parent / D7 retained state

- `ITER504S_ROOT_DERIVATIVE_RADIUS_LOCALIZED_SCOPED` remains terminal parent localization for roots 13-15 only;
- `ITER504R_ROOT_AFFINE_REUSE_INCONCLUSIVE_SCOPED` remains valid;
- `ITER504P_POINT_GRID_DRIFT_WITHIN_FROZEN_TOLERANCE_SCOPED` remains point-grid only, not a continuous theorem;
- no Iter504T result is promoted to all 1888 states while the repaired rerun is nonterminal;
- `D7-S2 = NOT_CLOSED`; `D7-S3 = NOT_CLOSED`; `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`;
- terminal D7 selectors remain forbidden.

## Next admissible work

Before any terminal scientific consumption, independently verify or refute C4 against the immutable launch head and original scientific preregistration without opening active scientific artifacts. Do not launch a competing scientific gate and do not consume partial root values.

If C4 is verified, any eventual green repair verdict at unchanged launch head remains independently implementation-invalid until a prospectively frozen same-science repair binds the top-level leaf flag to the conjunction of its four per-rho certification predicates. If C4 is refuted, preserve that refutation and wait for full terminalization of run `35205054496` before consuming aggregate/Critic/verdict.

## Governance lock

- `RQIR Core v1.0 = FROZEN`.
- Candidate Gravity remains inactive.
- Paper IV remains `NOT_YET_AUTHORIZED`.
- `INCONCLUSIVE != FAIL`.
- `BLOCKED != FAIL`.
- `INVALID_IMPLEMENTATION != SCIENTIFIC_FAIL`.
- missing object/rank/certificate != zero.
- scoped child result != family closure.
- green CI != scientific PASS.
- no authority exists for `QUANTUM_GRAVITY_SOLVED`, `ALL_KNOWN_MODELS_FAIL`, `NEW_THEORY_REQUIRED`, or `NEW_PHYSICS_FOUND`.

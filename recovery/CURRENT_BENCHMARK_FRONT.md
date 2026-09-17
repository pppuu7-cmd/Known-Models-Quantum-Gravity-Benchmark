# Current Benchmark Front
Updated: 2026-09-17

Fresh repository `main` and fresh Actions state always outrank this navigation document if they diverge.

## Terminal execution awaiting closure review

Gate: `ITER504T_IMPLEMENTATION_CONTROL_REPAIR_RERUN_GATE`.

The authoritative repair execution is now terminal:

- Actions run `35205054496`: `completed/success`;
- immutable launch head `10ae6bcc8447d14cecc6e550065504b23f792953`;
- source-lock and all root/assembly/aggregate/Critic/repair-verdict jobs completed;
- terminal artifact set is present, including `iter504t-repair-aggregate`, `iter504t-repair-critic`, and `iter504t-repair-verdict`.

This terminalization is execution/provenance only. No substantive repair-run artifact has yet been consumed by the Closure lane after terminalization, and no scientific/repair authority is promoted by green CI alone.

The repair execution remains same-science by its prospective contract: roots 13/14/15, rhos 0.35/0.9/1.6/2.7, exact R cohort `[6,8,10,12]`, all 243 channels, precision 384, local-D construction, threshold `1/20`, floor `1`, `MAX_DEPTH=3`, scientific classifier and interpretation ceiling unchanged. The launch gate repaired C1 parent-inclusion and C3 R-cohort wiring; C2 dyadic-location remains REFUTED.

## Latest terminal closure authority

Gate: `ITER504T_PRETERMINAL_LEAF_CERTIFICATION_BINDING_VERIFICATION_GATE`.

Terminal classification:

`ITER504T_LEAF_CERTIFICATION_BINDING_DEFECT_VERIFIED_SCOPED`

Independent Critic verdict: `CONFIRMED_SCOPED`.

C4 is terminally verified for the immutable repair launch-head downstream path: assembler, aggregate and independent Critic do not independently enforce the original frozen relation

`leaf.certified == all(rho.certified for rho in leaf.per_rho)`.

The verified synthetic replay shows that a leaf with an internally consistent `rho.certified=false` can retain top-level `leaf.certified=true` and `unresolved_leaf_count=0` and still traverse assembler -> aggregate -> Critic as the scientific PASS class. This is an implementation/decision-binding defect, not a scientific FAIL and not evidence that the actual producer emitted such a leaf.

## Historical Iter504T state retained

- Historical Research run `35181094204` reported `ITER504T_LOCAL_D_CERTIFIES_THREE_ROOT_CONTINUOUS_DRIFT_SCOPED`, but terminal independent Critic classified that execution `INVALID_IMPLEMENTATION`, not scientific FAIL, on C1/C3.
- Defect-binding closure VERIFIED C1, REFUTED C2, VERIFIED C3.
- Repair run `35205054496` was prospectively designed to repair C1/C3 only; C4 was discovered and independently confirmed after its immutable launch head was fixed.
- Therefore a terminal green/PASS repair-verdict from launch head `10ae6bcc...` cannot by itself restore scientific authority under the original frozen predicate.

## Next admissible work

Perform exactly one prospectively frozen terminal authority review of completed run `35205054496`. Only after that review is frozen may terminal aggregate/Critic/repair-verdict and, if required, terminal assemblies be consumed. The review must apply terminal C4 authority and distinguish implementation invalidity from scientific FAIL.

Do not launch a competing same-object execution during that review. Preserve the completed repair execution and all historical classifications.

If the terminal review confirms that no stronger independent terminal binding closes C4, the next implementation repair may prospectively add explicit assembler/Critic enforcement of `leaf.certified == all(rho.certified for rho in leaf.per_rho)` plus the exact adversarial C4 mutation while leaving the scientific object unchanged.

## Governance lock

- `RQIR Core v1.0 = FROZEN`.
- `D7-S2 = NOT_CLOSED`; `D7-S3 = NOT_CLOSED`; `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`.
- terminal D7 selectors remain forbidden.
- Candidate Gravity remains inactive; Paper IV remains `NOT_YET_AUTHORIZED`.
- `INCONCLUSIVE != FAIL`; `BLOCKED != FAIL`; `INVALID_IMPLEMENTATION != SCIENTIFIC_FAIL`.
- missing object/rank/certificate != zero; scoped child result != family closure; green CI != science.
- no authority exists for `QUANTUM_GRAVITY_SOLVED`, `ALL_KNOWN_MODELS_FAIL`, `NEW_THEORY_REQUIRED`, or `NEW_PHYSICS_FOUND`.

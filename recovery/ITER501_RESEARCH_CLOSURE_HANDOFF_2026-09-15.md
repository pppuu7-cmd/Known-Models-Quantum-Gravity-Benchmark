# KMQGB Research / Closure handoff — Iter501 terminal consumption

Date: 2026-09-15

## STATE_READ
At selection time, `main` exposed the prospectively frozen Iter501 direct max-envelope interval gate as the active executable D7-S2 science gate, downstream of terminal Iter500 enabling qualification. The frozen Iter501 authority was prereg commit `a02637a56eab2c9d71641ff5c0c9c7b19bfe1b84`, evaluator `6a3571826f2f55b4589daf266abcfc57b1f69022`, aggregate `712b1efdb5e151fba697b46bb7590066fa1f83e8`, production head `c7888d5f2f75239196deecd010312333c3337b2e`, run `34820198677`. Iter461 remained independently queued and was not duplicated.

During this closure run, other lanes advanced `main` beyond Iter501. The current active-front authority now records Iter501 as historical method-blocker evidence, Iter502 as another blocker, Iter503/503D/503V as centered-method qualification, Iter504 as a separate frozen active run, and additional collision/source-order work. This handoff therefore records only the one Iter501 closure step performed here and does not supersede newer active-front records.

## TARGET_GATE
D7-S2 / Iter501 direct 243-channel continuous max-envelope interval science gate.

## WHY_THIS_GATE
Iter500 had prospectively removed the generic interval-KAK obstruction and explicitly authorized this direct all-channel gate. At selection time it was the highest-information frozen experiment capable of distinguishing certified NONDECAY, certified uniform DECAY, validated inconclusive behavior, or a remaining numerical-method blocker while preserving all 243 channels and allowing channel crossings.

## PREREG
`recovery/ITER501_PREREG_DIRECT_MAX_ENVELOPE_INTERVAL_SCIENCE_2026-09-14.md`; prereg commit `a02637a56eab2c9d71641ff5c0c9c7b19bfe1b84`. No frozen hypothesis, object, thresholds, controls, amplitude boxes, directions, causal signatures, channel set, or interpretation ceiling was changed.

## WORK_PERFORMED
Consumed terminal run `34820198677`; verified source-lock success, all 12/12 lane jobs complete, aggregate job `103905778710` complete, and aggregate artifact `10338716481` with digest `sha256:dd0c50998749abf03d7913037d105c7b8ec99f8272788a193a185d60894dc38a`. Inspected representative raw lane artifacts and recorded the exact enclosure failure. Saved the durable scientific result note with complete raw-artifact provenance.

## RESULT
The run is structurally complete but produces no admissible science interval state. The aggregate has 12/12 expected jobs, no missing or duplicate IDs, all lanes method-blocked, `class_counts={}`, `n_direction_boxes=0`, and `n_rho_box_states=0`. Representative completed raw lanes show every attempted frozen amplitude box failing at the direct 243-channel max-envelope stage with `ArithmeticError('envelope lower bound not positive')`. Null science aggregates are missing/inadmissible objects, not zeros.

## CLASSIFICATION
`ITER501_NUMERICAL_METHOD_BLOCKER`

## NEW_FACT
Iter500's upstream KAK obstruction was not the final validated-arithmetic obstruction. The next failure is downstream: the direct all-243-channel max-envelope enclosure cannot certify a strictly positive lower envelope on the frozen boxes. This is a numerical/enclosure fact, not evidence for physical decay or nondecay.

## CLAIM_CEILING
No scientific PASS or FAIL for the q=1 NONDECAY hypothesis. No zero residual from missing lower bounds. No positive-measure claim. No absolute Haar convergence/divergence theorem from Iter501. No ten-spectral causal-vertex conclusion. No D7-S2 closure, terminal D7 label, family-level exclusion, or Candidate Gravity authorization.

## FILES_CHANGED
- `results/ITER501_DIRECT_MAX_ENVELOPE_INTERVAL_RESULT_2026-09-14.md`
- `recovery/ITER501_RESEARCH_CLOSURE_HANDOFF_2026-09-15.md`

No newer `CURRENT_BENCHMARK_FRONT` or `CURRENT_ACTIVE_FRONT_INDEX` content was overwritten because concurrent lanes had already advanced and synchronized those authorities beyond Iter501.

## COMMITS
- `226447848dee0d287f44e5eae19eb5d9e2b57e73` — terminal Iter501 result/provenance note.
- this handoff commit (the commit containing this file).

## OPEN_BLOCKERS
Current active-front governance remains authoritative: `D7-S2 = NOT_CLOSED`, `D7-S3 = NOT_CLOSED`, `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`. Iter501 specifically leaves the positive max-envelope lower-bound enclosure unresolved. Newer active work must also be consumed according to `recovery/CURRENT_ACTIVE_FRONT_INDEX_2026-09-15.md`, including the independently frozen Iter504 run, source-order/collision-extension obligations, and Iter461 when its artifact exists.

## NEXT_RECOMMENDED_GATE
Do not rerun or weaken Iter501. For the Iter501 numerical lineage, the admissible successor is the already-recorded centered/dependency-preserving repair chain (Iter502/503/503D/503V/Iter504), not post-hoc threshold relaxation. For global recovery, read the current active-front index first and consume whichever currently registered frozen run becomes terminal; do not duplicate concurrent gates.
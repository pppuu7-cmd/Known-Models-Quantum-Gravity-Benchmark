# Current Benchmark Front
Updated: 2026-09-17

Fresh repository `main` and fresh Actions state always outrank this navigation document if they diverge.

## Active nonterminal Closure gate

Gate: `ITER504T_IMPLEMENTATION_CONTROL_REPAIR_RERUN_GATE`.

Status: `IN_PROGRESS_NOT_CLASSIFIED`.

Authoritative repair run `35205054496` remains `in_progress / conclusion=null` at the latest metadata check. No substantive root/assembly/aggregate/Critic/repair-verdict value from that active run has been consumed. The frozen repair launch head remains `10ae6bcc8447d14cecc6e550065504b23f792953`.

The repair is same-science: roots 13/14/15, rhos 0.35/0.9/1.6/2.7, exact R cohort `[6,8,10,12]`, all 243 channels, precision 384, local-D construction, threshold `1/20`, floor `1`, `MAX_DEPTH=3`, scientific classifier and interpretation ceiling are unchanged. C1 parent-inclusion and C3 R-cohort wiring were added; C2 dyadic-location remains REFUTED.

## Latest terminal closure result

Gate: `ITER504T_PRETERMINAL_LEAF_CERTIFICATION_BINDING_VERIFICATION_GATE`.

Terminal classification:

`ITER504T_LEAF_CERTIFICATION_BINDING_DEFECT_VERIFIED_SCOPED`

This is **C4 VERIFIED**, an implementation/decision-binding result only, not scientific FAIL.

Authority / execution:

- prospective preregistration `aa421bd0b1aec1cbcc7a381fb00e947798d1b084`;
- frozen authority `9aa9f77093bd34e058641bb141c8f95a4794d841`;
- verifier `72f952cb0ce6c3bc08f244fdde815337d3504b1e`;
- aggregate verifier `c2527cb1966e6afe7fcdd8c9f1d0df435b35080a`;
- workflow head `2a550a44cdf69b1b165ba65fec8f6a5d56bd0f40`;
- Actions run `35220141450`, terminal `completed/success`;
- jobs `105197957392`, `105197992013`, `105197992075`, `105198050663`;
- artifacts: 3.11 `10496991098` / `sha256:011a0b8363dcf313d62bc9c2dd681afd1ecff0f91b2b3cee52a4f7492ca79562`; 3.13 `10496836236` / `sha256:71c367aa409fa18b3bd04b423b377cbbbd90589543a06c94387d424f2010617d`; aggregate `10496519019` / `sha256:7a932e0c36bdc09871ac114c9264c6997c4c352a84c2373e6323086ecbdb3daa`;
- lane decision SHA256 `3eefcd29f0699da8c7bcae6639cabbffd04f0fa154f31862d6f716c216899c05`;
- aggregate decision SHA256 `770ec74f672105a303c792586a8f644f12c1a54788021ff9856511d7c3fea6e5`.

Exact frozen synthetic replay established that the immutable launch-head path accepts, in both environments, a terminal leaf with one internally consistent `rho.certified=false` while top-level `leaf.certified=true` and `unresolved_leaf_count=0`. Both assemblers, aggregate and repaired independent Critic return `ITER504T_LOCAL_D_CERTIFIES_THREE_ROOT_CONTINUOUS_DRIFT_SCOPED`; Critic errors are empty and cross-environment decision agreement is true.

Positive controls confirm the replay is outcome-sensitive: a compliant fixture passes; an internally broken per-rho relation is rejected; `R=6 -> 7` is rejected; all frozen blob identities match. No active repair-run scientific artifact was inspected.

Therefore the launch-head chain does not independently enforce the original frozen relation

`leaf.certified == all(rho.certified for rho in leaf.per_rho)`.

C4 is now terminally verified, not merely a candidate.

## Historical Iter504T state retained

Historical Research run `35181094204` reported `ITER504T_LOCAL_D_CERTIFIES_THREE_ROOT_CONTINUOUS_DRIFT_SCOPED`, but terminal independent Critic classified that execution `INVALID_IMPLEMENTATION`, not scientific FAIL, on C1/C3. Defect-binding run `35192972048` VERIFIED C1, REFUTED C2, VERIFIED C3.

The current repair rerun was designed to repair C1/C3, but its immutable launch head now has independently verified C4. A future green CI or PASS repair-verdict from that unchanged launch head cannot by itself be promoted to scientific authority.

## Next admissible work

Do not launch another same-object authoritative execution while run `35205054496` remains nonterminal. After it terminalizes, perform one terminal repair-run review that records terminal jobs/artifacts/provenance and applies the already-terminal C4 finding. Preserve the execution, but do not promote a green/PASS result as scientifically validated under the original predicate.

Only after that terminal review may a new prospectively frozen same-science implementation repair bind top-level leaf certification to the conjunction of all four per-rho certifications and add the exact adversarial C4 mutation, without changing the scientific object.

## Governance lock

- `RQIR Core v1.0 = FROZEN`.
- `D7-S2 = NOT_CLOSED`; `D7-S3 = NOT_CLOSED`; `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`.
- terminal D7 selectors remain forbidden.
- Candidate Gravity remains inactive; Paper IV remains `NOT_YET_AUTHORIZED`.
- `INCONCLUSIVE != FAIL`; `BLOCKED != FAIL`; `INVALID_IMPLEMENTATION != SCIENTIFIC_FAIL`.
- missing object/rank/certificate != zero; scoped child result != family closure; green CI != science.
- no authority exists for `QUANTUM_GRAVITY_SOLVED`, `ALL_KNOWN_MODELS_FAIL`, `NEW_THEORY_REQUIRED`, or `NEW_PHYSICS_FOUND`.

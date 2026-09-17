# ITER504T_REPAIR_RERUN_TERMINAL_AUTHORITY_REVIEW_SEMANTICS_REPAIR_GATE — terminal result

Date: 2026-09-17
Status: TERMINAL

## Authority and chronology

- Prospective preregistration: `5b18ffbe46b967ef64c54d6181924aa8acf6f43e`.
- Frozen authority ledger: `39bd24ff03cba8858dca39ceb2935509352f295a`.
- Repaired reviewer: `b0f9fa5f2efe1e1f09d72d33e78bbee904ad5eb5`.
- Aggregate code: `311ac4169bd3fd8e0ce8b8ded1f8bc566db3cdeb`.
- Workflow head: `71b1e197192c17d0c74e06fe7eb12b9b4b332f60`.
- Authoritative Actions run: `35232311780`, terminal `completed/success`.

The reviewer criteria were frozen before implementation/result. No new physics execution was run.

## Terminal classification

`ITER504T_REPAIR_RERUN_EXACT_RUN_AUTHORITY_VALIDATED_SCOPED`

This is exact-run scoped authority validation for completed repair run `35205054496`. It is not all-1888 closure, D7 closure, model/family closure, or validation of the reusable launch-head validator generally.

## Latest Critic defects repaired

The independent Critic commit `15b323994844fd83dfa0dc71efb977ba4300de97` had invalidated the historical authority-review implementation on two prospectively frozen alternate branches. The repaired reviewer now demonstrates both branches outcome-sensitively:

1. a structurally valid unresolved fixture carrying the original scientific label `ITER504T_LOCAL_D_INCONCLUSIVE_SCOPED` remains exactly that INCONCLUSIVE result and is not converted to authority-restoration FAIL;
2. deleting the required `roots` structural field yields `ITER504T_REPAIR_RERUN_TERMINAL_REVIEW_BLOCKED_SCOPED`, not authority-restoration FAIL.

All eight frozen semantics controls pass:

- valid PASS fixture -> review PASS;
- valid original INCONCLUSIVE -> original scientific INCONCLUSIVE;
- missing required field -> BLOCKED;
- C4 true-leaf/false-rho contradiction -> authority-restoration FAIL;
- per-rho boolean inconsistency -> authority-restoration FAIL;
- `R=6 -> 7` mutation -> authority-restoration FAIL;
- missing required C1 record -> authority-restoration FAIL;
- artifact identity mutation -> `INVALID_IMPLEMENTATION`.

## Exact production replay

Both independent Python 3.11 and Python 3.13 lanes agree exactly and report no review errors.

For immutable repair run `35205054496` at head `10ae6bcc8447d14cecc6e550065504b23f792953`:

- the two terminal assembly payloads are byte-identical, SHA256 `dfaa14d7b07708b9cc59d04413a86661aed37dab662705499893e601ffcb9c24`;
- roots are exactly `13,14,15`;
- R cohort is exactly `[6,8,10,12]`;
- 12 terminal leaves and 48 per-rho rows are present;
- every per-rho serialized certification equals the frozen slope/drift conjunction;
- every actual terminal leaf satisfies `leaf.certified == all(rho.certified for rho in leaf.per_rho)`;
- independently recomputed unresolved leaves = `0`;
- independently recomputed scientific class in both environments is `ITER504T_LOCAL_D_CERTIFIES_THREE_ROOT_CONTINUOUS_DRIFT_SCOPED`;
- C1 contains 18 parent-inclusion records / 70,056 boolean components per lane / 0 false components;
- transported aggregate, independent Critic and repair verdict are consistent with the independently rebound actual decision.

C4 remains historically `CONFIRMED_SCOPED` as a defect of the general reusable launch-head validator path. This result proves only that the exact completed run itself contains no C4 violation and is independently rebound.

## Actions provenance

Jobs:

- source-lock `105239292923`;
- Python 3.11 `105239369708`;
- Python 3.13 `105239369636`;
- aggregate `105239442328`.

Artifacts:

- Python 3.11 `10501567806`, digest `sha256:70f4a0b7b4e2e7ab60c42c5e83abeaa28dd2b55bc45bbace7d448e2ccbbe888e`;
- Python 3.13 `10501033269`, digest `sha256:7ae9953cfc780230007eb326ab8fc5c13532a30bde12b7c41e08d1ed156093ec`;
- aggregate `10501338087`, digest `sha256:cec9f4eaa6192d0a2defc57d117ae5de89cc7e9b5f9c77a2ec9403ea1d545fe4`.

Independent ZIP rehashes match all three GitHub digests.

Decision hashes:

- lane review decision SHA256 `ab197395b971d3dc3c78574d4ae8176df839394ce902b72b126307b2674f604c` in both environments;
- aggregate decision SHA256 `627836dc469c726c280d7b00c3ac46413724683fd05cc8759fbb185735230d61`;
- aggregate JSON SHA256 `345642be3ad316d2c2cd704dce67670b41a364d78129411a1d8475b5a146ba23`;
- aggregate raw-log SHA256 `af7dcc5e9c4badae68b09479af9cd7da10ad837c40ecd68f0160e51a9a06c1c3`.

Green CI is provenance only; the scientific/closure claim comes from the frozen outcome-sensitive replay.

## Claim ceiling

This result validates only exact completed run `35205054496` under the original three-root bounded local-D claim ceiling. It does not validate future executions of the unrepaired reusable launch-head path, does not erase historical `INVALID_IMPLEMENTATION` or C4, and does not establish all 1888 states, D7 closure, model/family failure, a terminal D7 selector, Candidate Gravity, Paper IV authorization, `QUANTUM_GRAVITY_SOLVED`, `ALL_KNOWN_MODELS_FAIL`, `NEW_THEORY_REQUIRED`, or `NEW_PHYSICS_FOUND`.

## Next recommended gate

Do not repeat terminal authority review for this exact run absent a new independent Critic defect. The remaining same-object implementation obligation is the reusable-validator C4 repair: explicitly enforce `leaf.certified == all(rho.certified)` in assembler and independent Critic with the terminal adversarial C4 mutation while leaving the science contract unchanged.

A different scientific frontier may outrank C4 repair if it has higher information gain and does not reuse the defective validator path. Decide from fresh current DAG/recovery state.

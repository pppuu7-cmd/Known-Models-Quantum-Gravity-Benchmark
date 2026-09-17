# ITER504T_IMPLEMENTATION_CONTROL_REPAIR_RERUN_GATE — prospective freeze

Date: 2026-09-17
Status: PROSPECTIVELY_FROZEN_BEFORE_REPAIR_IMPLEMENTATION_OR_RERUN_OUTPUT

## HYPOTHESIS

The terminal Iter504T scientific object can be rerun under its unchanged frozen science/numerics while repairing exactly the two independently verified implementation-control defects: (C1) missing computation/serialization/binding of componentwise child-vs-parent derivative inclusion checks, and (C3) missing independent binding of the exact R cohort `[6,8,10,12]`. The already-valid exact rational dyadic-cell verification must remain unchanged. This gate tests repair validity plus a fresh same-contract rerun; it does not introduce a new physics object or change the original Iter504T scientific classifier.

## exact OBJECT

Exactly the same scientific object as `ITER504T_LOCAL_DERIVATIVE_ENCLOSURE_CONTRACTION` on roots `13,14,15`, with one implementation-only repair layer.

The repair object has two mandatory controls:

1. for every visited non-root child interval `J`, compute and serialize componentwise Arb containment checks `D_i(J) subseteq D_i(parent(J))` for all 243 contracted channel derivatives at every frozen R/rho and for each frozen-R Haar/log derivative; boolean `false` is diagnostic-only and is not a scientific failure;
2. serialize the actual R cohort consumed by the producer and independently require exact identity `[6,8,10,12]` in assembler and Critic, including an adversarial `6 -> 7` mutation that must be rejected.

No other scientific object is admissible in this gate.

## DEPENDENCY

- Original prospective scientific preregistration commit `aa2b0256ce60d605574a18ec86c0bad5b5df1512`.
- Original single-execution authority commit `3a485d34efaa500bbd0276b397c1a2078d18905e`.
- Original exact launch head `d23f34cba57b220dd29474c0651bc727d6d85eae` and terminal Actions run `35181094204`.
- Historical Research classification `ITER504T_LOCAL_D_CERTIFIES_THREE_ROOT_CONTINUOUS_DRIFT_SCOPED` is retained but not downstream-forwardable.
- Terminal independent Critical Review commit `33e2b9818c409843099aa136648a2da010a839a2`, verdict `INVALID_IMPLEMENTATION`.
- Independent defect-binding closure: C1 VERIFIED, dyadic C2 REFUTED, C3 VERIFIED.
- Starting repository main `51b8a95ed009761e542f8c50efaeca3a98bc2891`.

## SOURCE/REALIZATION AUTHORITY

Only the original Iter504T source/scientific chain plus the prospectively committed repair authority ledger `inputs/iter504t_implementation_control_repair_rerun_authority.json` is authoritative.

The repair ledger must lock the pre-repair blobs of:

- `code/iter504t_local_derivative_contraction.py` = `1ae78fc309839da30d1c78fc25c8e5ea3d98693f`;
- `code/iter504t_local_derivative_assemble.py` = `6a886bf6ce8c263e586a6cb25d7441df5273a72d`;
- `code/iter504t_local_derivative_aggregate.py` = `10a4338f5b55485b98cfdb6bfecd1a7e646a130a`;
- `code/iter504t_local_derivative_critic.py` = `950d22e97b1ca2a17b2bb08d4386de6d4fb39445`;
- original workflow `.github/workflows/iter504t-local-d-science.yml` = `8356f1417016f4d084d6b799615e3f096dd99a5d`;
- original scientific preregistration blob = `f648b0e0d6a960bf60c32d5c34694497a50b7e68`.

The only admissible implementation changes are wiring/serialization/validation required to close C1 and C3 plus a fresh workflow/artifact namespace for the rerun. Source equations, local-D construction, interval arithmetic, scientific predicate, partition rule, classifier and claim ceiling may not change.

## FROZEN INPUTS

All original Iter504T scientific/numerical inputs remain exactly frozen:

- `python-flint==0.9.0`;
- Arb/Acb precision 384 bits;
- causal `0to5`, block `0`, path `2`, direction `[1,1,1,-1,-1,-1]`, sign `+1`;
- roots `[13,14,15]`;
- rhos `[0.35,0.9,1.6,2.7]`;
- R grid exactly `[6,8,10,12]`;
- all 243 channels, no pruning;
- exact threshold `1/20`;
- exact robust slope floor `1`;
- deterministic rational dyadic midpoint subdivision;
- `MAX_DEPTH=3`;
- direct local derivative recomputation on every visited interval;
- exact original PASS / INCONCLUSIVE / INVALID scientific labels and original interpretation ceiling.

The componentwise inclusion truth value is not added to the scientific PASS predicate. Its computation/recording/validation is a frozen implementation obligation only.

## REPAIR DATA CONTRACT

For each root producer output:

- emit `r_cohort_consumed=[6,8,10,12]` from the cohort actually iterated by the computation;
- emit one `componentwise_parent_inclusion` record for every visited non-root node;
- each record must identify child interval, parent interval and depths;
- for each frozen R, emit one Haar/log derivative inclusion boolean;
- for each frozen `(R,rho)`, emit exactly 243 channel derivative inclusion booleans in canonical flattened channel order;
- retain false booleans without converting them into INVALID or scientific FAIL.

Assembler and Critic must reject missing/malformed/incomplete inclusion records and missing/extra/wrong R-cohort identity, but must not reject merely because an inclusion boolean is false.

## POSITIVE CONTROLS

1. Exact R cohort `[6,8,10,12]` is accepted.
2. A complete synthetic child inclusion record with the exact frozen R/rho/channel cardinalities and boolean values is accepted regardless of whether individual inclusion booleans are true or false.
3. Existing exact rational dyadic midpoint/cell validation remains accepted unchanged.
4. Original roots/rhos/threshold/floor/channel-count/local-derivative/provenance checks remain accepted.

## NEGATIVE CONTROLS

The repaired independent Critic must reject at least:

1. missing child inclusion record;
2. malformed inclusion record or wrong non-root record count;
3. missing one R/rho/channel inclusion boolean;
4. non-boolean inclusion entry;
5. producer R cohort `[6,8,10,14]` or a `6 -> 7` mutation;
6. missing or extra R entry;
7. any change to roots, rhos, threshold, floor, channel count, MAX_DEPTH, dyadic partition identity, provenance, or scientific decision transport.

The previously refuted dyadic-location defect may not be resurrected as a repair premise; existing exact-rational dyadic validation is retained.

## PASS

`ITER504T_IMPLEMENTATION_CONTROLS_REPAIRED_AND_RERUN_VALID_SCOPED` iff:

1. the fresh rerun uses the unchanged original Iter504T scientific contract;
2. producer, assembler and independent Critic bind exact R cohort `[6,8,10,12]`;
3. every visited non-root node carries a complete componentwise parent-inclusion record with exact frozen cardinalities;
4. false inclusion values, if any, remain diagnostic-only;
5. all prospectively frozen repair positive/negative controls pass;
6. Python 3.11 and 3.13 scientific decisions agree;
7. fresh aggregate and Critic are terminal and the Critic returns no repair-contract error;
8. the fresh original scientific classification is one of the original preregistered Iter504T PASS or INCONCLUSIVE labels and is recorded separately from this repair-gate PASS.

## FAIL

`ITER504T_IMPLEMENTATION_CONTROL_REPAIR_FAILED_SCOPED` iff the prospectively frozen implementation-only repair itself fails its mandatory C1/C3 controls or adversarial fixtures while provenance/authority is otherwise valid. This is a repair-hypothesis failure, not a scientific failure of Iter504T or any model.

## BLOCKED / INVALID

`ITER504T_IMPLEMENTATION_CONTROL_REPAIR_BLOCKED_SCOPED` iff the original frozen computation cannot be rerun with the required control wiring without changing the scientific object/contract, or required durable objects are unavailable.

`INVALID_IMPLEMENTATION` iff source/scientific identity changes, any frozen science/numeric/classifier/ceiling field changes, partial nonterminal substantive output is consumed, a competing authoritative same-object gate is launched, synthetic data enter production, or prospective repair criteria are changed after result.

## INTERPRETATION CEILING

A repair PASS establishes only that the two verified Iter504T implementation-control defects are actually wired and that a fresh same-contract Iter504T run has a Critic-valid implementation record. The original scientific classification of that fresh rerun retains exactly the original three-root bounded local-D claim ceiling. No outcome establishes all 1888 states, D7 closure, model/family failure, terminal selector, Candidate Gravity, Paper IV authorization, `QUANTUM_GRAVITY_SOLVED`, `ALL_KNOWN_MODELS_FAIL`, `NEW_THEORY_REQUIRED`, or `NEW_PHYSICS_FOUND`.

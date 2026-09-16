# ITER504P execution-only terminal-ancestry repair

Date: 2026-09-17
Status: PROSPECTIVELY FROZEN EXECUTION-ONLY REPAIR

## Trigger

The first production execution of `ITER504P_OUT_OF_SAMPLE_POINT_DRIFT_LOCALIZATION_GATE`, Actions run `35151368577` at workflow head `e74ed2e3335fb839c6be722fca0b91e0b8520c81`, failed in `source-lock` before artifact inventory, point-artifact download, drift computation, or aggregate classification.

The failure is provenance-only: the source-lock attempted `git merge-base --is-ancestor 95870d0649d4b8d7b156c3f2b68bd55caa65d9c0 HEAD`, but that SHA is not a valid repository commit. The frozen authority manifest inherited the same erroneous `terminal_record_commit` string.

The actual durable Iter504 records on `main` are:

- canonical result JSON commit `2e1fa7e772185b82387c7bb49da0c4f85bc06df8`;
- terminal result markdown commit `e3816c0437a1f895196d2bbccacfb05e8dd38e74`;
- independent post-terminal Critic commit `2feb5793913ff550b96ea609827da574c2e05056`.

The terminal markdown binds Iter504 to Actions run `34907349374`, workflow head `56362459a826e3e376c529446678f2fbcaa269ae`, summary artifact `10436186009`, artifact digest `sha256:0273394cbd3d0be55589279645c8170a02042178210b145897bc21e721754163`, and classification `ITER504_VALIDATED_CENTERED_INTERVAL_INCONCLUSIVE_SCOPED`.

## Frozen repair

Only the following provenance binding may change:

1. replace the nonexistent `95870d0649d4b8d7b156c3f2b68bd55caa65d9c0` terminal-record reference with the actual Iter504 terminal record `e3816c0437a1f895196d2bbccacfb05e8dd38e74` in the Iter504P frozen authority manifest and source-lock;
2. update the source-lock's expected Git blob SHA for that manifest to the blob produced by exactly this one-field provenance correction;
3. rerun the same frozen Iter504P workflow.

## Scientific immutability

This repair MUST NOT change:

- preregistration `77bac4728401200b226dda16447befce85df0c66`;
- upstream Iter504 run `34907349374` or workflow head `56362459a826e3e376c529446678f2fbcaa269ae`;
- the 11 decisive lanes or any decisive artifact ID/digest;
- control lane `0to5-b0` or its non-decisive status;
- expected decisive count `1584`;
- formula `D_point = abs(actual_slope - early_actual_slope)`;
- threshold `0.05`;
- WITHIN / VIOLATION / INVALID classifier semantics;
- any point value or record.

No substantive decisive point artifact was consumed by the failed run because both `exact-lanes` and `aggregate` were skipped. The repair is therefore execution/provenance-only and preserves the prospective firewall.

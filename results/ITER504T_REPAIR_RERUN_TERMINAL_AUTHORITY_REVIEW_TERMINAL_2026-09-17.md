# ITER504T_REPAIR_RERUN_TERMINAL_AUTHORITY_REVIEW_GATE — terminal result

Date: 2026-09-17
Status: TERMINAL

## Authority

- prospective review preregistration: `a4be2171d5d325ba25b805603a2e9e30e542520b`;
- frozen review authority: `525cea7c03dfae45c668f9fb57b23ad30ac15010`;
- exact review implementation: `cd30ab36e61f4668a73214f603dd018eeb503825`;
- aggregate implementation: `de9596f9fc1297e31ff9f11bbf1d3f30a2f79926`;
- authoritative review workflow head: `8cf5aefa4b15b5a6c7dfaf7f08d1884ba8363658`;
- review Actions run `35225818354`, terminal `completed/success`;
- jobs: source-lock `105217007869`, Python 3.11 `105217073486`, Python 3.13 `105217073481`, aggregate `105217171182`;
- review artifacts: Python 3.11 `10498984379` / `sha256:ecaa42b702fb6e823a90862adca0c6da9869774aa7de673abb8b9c186d6c49f9`; Python 3.13 `10499010539` / `sha256:01ac6aa3746a4b3ada66080188e634fcc116f76b96cbfef9b737fa6ac30d4a24`; aggregate `10499190200` / `sha256:7d2c7181896f396ad476fba2e073d91b04ee776d81d5efb1ebda0f368a278338`;
- lane review decision SHA256 `7db8327005022341541ef0b62df9a87a02e8741d5716ddf2deb397fb1b95e989`;
- aggregate review decision SHA256 `6e764ea10206959a755914279a4dfa67adfcbe0935762377a38606a0b24be9c4`;
- aggregate JSON SHA256 `5cd809948846750e51096ab19a23d8710915859a9f8afcca84bfb6ee32827dc1`;
- aggregate log SHA256 `0c08257847b686994f8782ad89a3d49d62a074f54d0b78d225a480efc692630e`.

Green CI is provenance only; the scientific/authority result below comes from the prospectively frozen independent binding review.

## Terminal classification

`ITER504T_REPAIR_RERUN_EXACT_RUN_AUTHORITY_VALIDATED_SCOPED`

This is an **exact-run authority validation PASS**, not a universal validation of the immutable launch-head workflow.

## Exact result

The completed same-science repair execution reviewed here is Actions run `35205054496` at immutable head `10ae6bcc8447d14cecc6e550065504b23f792953`.

The independent terminal review opened only the prospectively frozen terminal artifact set after review preregistration. Both independent review lanes agree exactly and report no review errors.

The two terminal assembly JSON payloads are byte-identical with SHA256 `dfaa14d7b07708b9cc59d04413a86661aed37dab662705499893e601ffcb9c24`.

For each environment the review independently recomputed the original frozen certification predicate rather than trusting serialized top-level leaf state:

- three roots: `13,14,15`;
- twelve terminal leaves total, four per root;
- four rhos per leaf: `0.35,0.9,1.6,2.7`;
- every one of the 48 per-rho rows satisfies the exact serialized identity `rho.certified == slope_floor_satisfied AND drift_within_tolerance`;
- every one of the 12 actual terminal leaves satisfies `leaf.certified == all(rho.certified for rho in leaf.per_rho)`;
- every independently recomputed leaf certification is `true`;
- independently recomputed unresolved-leaf count is `0` in both environments;
- independently recomputed original scientific classification is `ITER504T_LOCAL_D_CERTIFIES_THREE_ROOT_CONTINUOUS_DRIFT_SCOPED` in both environments.

Thus the actual terminal data do not instantiate the independently verified C4 counterexample, even though the launch-head validators themselves remain unable to enforce that relation generally.

The C1/C3 repair obligations are also independently retained:

- exact R cohort `[6,8,10,12]` is bound;
- 18 non-root componentwise parent-inclusion records per lane are present;
- each lane contains 70,056 componentwise inclusion booleans under the frozen contract;
- zero of those booleans are false in this exact run;
- original exact rational dyadic validation remains in force.

The launch-head aggregate and independent Critic both report the same original scientific classification; Critic errors are empty. The frozen repair verdict is `ITER504T_IMPLEMENTATION_CONTROLS_REPAIRED_AND_RERUN_VALID_SCOPED` with all repair checks true.

All seven prospectively frozen outcome-sensitive review controls pass: both directions of the C4 mismatch are rejected, per-rho boolean inconsistency is rejected, `R=6 -> 7` is rejected, a missing C1 record is rejected, artifact-identity mutation is rejected, and a serialized unresolved-count mismatch is rejected.

## NEW_FACT

The independently confirmed C4 launch-head defect does **not** force this completed run to remain scientifically unusable. A stronger prospectively frozen post-terminal gate can inspect the actual terminal assemblies and independently bind the missing predicate. For run `35205054496`, that independent binding succeeds on all actual terminal leaves and reproduces the original scientific PASS exactly in both environments.

Therefore the exact completed repair run is now admissible as scoped scientific authority for its original three-root bounded local-D claim, despite the fact that the unchanged launch-head validator path remains generally defective and cannot be trusted by itself on future executions.

C4 remains terminally `CONFIRMED_SCOPED`; it is neither erased nor refuted by this result.

## Claim ceiling

The validated scientific result remains exactly the original three-root bounded local-D claim for roots `13,14,15` under the frozen Iter504T contract. It is not an all-1888-state result, not family closure, not D7 closure, not a terminal selector, and does not authorize Candidate Gravity or Paper IV.

No authority exists here for `QUANTUM_GRAVITY_SOLVED`, `ALL_KNOWN_MODELS_FAIL`, `NEW_THEORY_REQUIRED`, or `NEW_PHYSICS_FOUND`.

## Next recommended gate

If this pipeline is to be reused or extended beyond this exact completed run, prospectively freeze a same-science C4 implementation repair that adds explicit assembler and independent-Critic enforcement of

`leaf.certified == all(rho.certified for rho in leaf.per_rho)`

plus the already-terminal adversarial C4 mutation. Do not change roots, rhos, R cohort, 243 channels, local-D construction, threshold `1/20`, floor `1`, `MAX_DEPTH=3`, scientific classifier, or claim ceiling.

This implementation repair is for reusable validator correctness; it is not required to revoke the exact-run authority established by the present terminal review.

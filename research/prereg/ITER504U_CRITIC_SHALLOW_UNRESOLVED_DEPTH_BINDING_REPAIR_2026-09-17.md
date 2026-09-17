# Iter504U Critic shallow-unresolved depth-binding repair — preregistration

Date: 2026-09-17
Status: PROSPECTIVELY_FROZEN_BEFORE_IMPLEMENTATION

## Scope

This gate is methodology / independent-Critic validation only. It MUST NOT consume any scientific payload from active Iter504U production run `35246605860`, MUST NOT rerun producer science, and MUST NOT alter the frozen held-out cohort, source realization, R/rho cohorts, thresholds, precision, channel count, partition, local-D construction, `MAX_DEPTH`, or PASS/INCONCLUSIVE taxonomy.

Parent science gate: `ITER504U_HELDOUT_LOCAL_D_GENERALIZATION_FIREWALL`.
Parent science preregistration: `05b8e9354c9a7805f0fce18b904346a986a0787f`.
Immutable science launch/source head: `102c7f9cafec956f3bc7bed4384ae755c98f761a`.
Authoritative production run: `35246605860`.

Frozen base objects:

- producer blob: `bf457eef08f7df32523c9e22ce3b3713f10d97a0`;
- assembler blob: `5c3b04f25c5fb2523c3788b725ccf84ca23a07f1`;
- original Critic blob: `c2a7ea31ddc151bf02a3995d761cae95bdabd0db`;
- validated C4 repair wrapper blob: `bcea2946a0f9676b50897dc4bbe74fa1122a9965`;
- C4 shared-validator methodology classification: `ITER504U_CRITIC_C4_FIXTURE_REPAIR_VALIDATED_SCOPED`.

Preterminal independent audit commit `97a99cdcfaacec1e87b216e0d3a4282b165ae59b` identified an outcome-independent validator/authority-path defect candidate: the frozen producer recursively bisects every uncertified node while `depth < MAX_DEPTH`, but assembler/Critic validation does not explicitly reject a terminal leaf with `certified == false` at depth 0, 1, or 2.

## Frozen contract rule

For every terminal leaf:

`leaf.certified == false  =>  int(leaf.depth) == MAX_DEPTH`

with frozen `MAX_DEPTH = 3`.

The exact new validator error label is:

`premature_unresolved_leaf_depth`

No other validator semantics are changed by this repair.

## Outcome-independent synthetic counterexample

Use a fully synthetic six-case structurally coherent carrier derived only from frozen metadata and shared-validator structure, not from production science.

Baseline carrier requirements:

- all six frozen H0–H5 case identities;
- one exact full-parent depth-0 leaf per case;
- every baseline leaf certified true;
- four coherent per-rho rows, all true;
- 16 R×rho possible-max records with valid channel index `[0]`;
- exact parent cover;
- zero parent-inclusion records;
- `visited_node_count=1`, `terminal_leaf_count=1`, `unresolved_leaf_count=0`;
- all frozen source/cohort/threshold/floor/precision/depth/tags unchanged.

Synthetic shallow-unresolved mutation for H0 only:

1. keep the exact root cell at `depth=0` and full parent cover;
2. set all four per-rho rows internally coherent true;
3. set the first per-rho row to `slope_floor_satisfied=false`, `drift_within_tolerance=false`, `certified=false`;
4. set the top-level leaf `certified=false`;
5. set case `unresolved_leaf_count=1`;
6. retain `visited_node_count=1`, `terminal_leaf_count=1`, and all other frozen fields unchanged.

This mutation is designed so that the sole intended contract violation under the repaired validator is `H0_AMP_LOW:premature_unresolved_leaf_depth`.

## Required controls

A formal synthetic gate MUST demonstrate all of the following in both Python 3.11 and 3.13:

1. coherent baseline is accepted by the frozen shared validator;
2. the frozen pre-repair shared validator accepts the shallow-unresolved mutation, demonstrating the missing binding rather than relying only on static inspection;
3. the repaired shared validator rejects that same mutation exactly as `['H0_AMP_LOW:premature_unresolved_leaf_depth']`;
4. a depth-3 internally coherent unresolved terminal leaf is accepted by the repaired validator;
5. the already-validated C4 contradiction still rejects exactly as `['H0_AMP_LOW:C4_leaf_binding']`;
6. the full C4 repaired negative-control suite still passes;
7. the successor repaired negative-control suite adds and passes `premature_unresolved_leaf_depth`;
8. original Critic/C4 wrapper identities and production gate/prereg identities remain frozen;
9. no production science is consumed and source run is not classified;
10. Python 3.11 and 3.13 result JSON is byte-identical.

## Repair implementation ceiling

The repair may be implemented only as an independent Critic successor/wrapper. It MUST NOT modify:

- `code/iter504u_heldout_local_d_case.py`;
- `code/iter504u_heldout_assemble.py`;
- `code/iter504u_heldout_aggregate.py`;
- the immutable production run;
- scientific criteria or taxonomy.

The future repaired terminal closure may reject terminal production as `ITER504U_INVALID` if an actual shallow uncertified terminal leaf is present. Such an implementation/provenance invalidity is not a scientific FAIL and does not justify a producer rerun unless a separately prospectively frozen execution-only repair is authorized.

## Frozen methodology classifications

PASS:

`ITER504U_CRITIC_SHALLOW_UNRESOLVED_DEPTH_BINDING_REPAIR_VALIDATED_SCOPED`

FAIL:

`ITER504U_CRITIC_SHALLOW_UNRESOLVED_DEPTH_BINDING_REPAIR_FAIL_SCOPED`

Implementation/provenance defect in this methodology gate:

`INVALID_IMPLEMENTATION`

No Iter504U scientific PASS/INCONCLUSIVE/INVALID result may be issued by this methodology gate.

## Claim ceiling

This gate can establish only that the independent Critic authority path correctly binds unresolved terminal leaves to frozen `MAX_DEPTH=3` while preserving the previously validated C4 control behavior. It does not classify Iter504U science and authorizes no all-domain, D7, model-family, Candidate Gravity, Paper IV, `ALL_KNOWN_MODELS_FAIL`, `NEW_THEORY_REQUIRED`, `QUANTUM_GRAVITY_SOLVED`, or `NEW_PHYSICS_FOUND` claim.

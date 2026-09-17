# ITER504U_CRITIC_C4_SHARED_VALIDATOR_REPAIR_GATE — prospective successor freeze

Date: 2026-09-17
Status: `PROSPECTIVELY_FROZEN_BEFORE_SUCCESSOR_EXECUTION_OR_RESULT`

## Parent terminal defect

Formal parent gate `ITER504U_CRITIC_C4_FIXTURE_REPAIR_GATE` is terminal `INVALID_IMPLEMENTATION`, record commit `77189486ba4db1dd281832b962b1be290e323944`.

The defect is limited to formal validation-path coverage: methodology run `35250717944` proved the local synthetic constructor assertions but did not exercise the shared Critic validator required by formal preregistration `662e1b40c4584a5b1989b821cd7a5c334ef8fc44`.

No held-out scientific payload is needed to repair this defect.

## Exact object

Validate the already-isolated C4 synthetic constructor through the exact shared Iter504U Critic structural validator, using a completely synthetic six-case payload that satisfies the frozen structural contract without representing or importing any held-out scientific result.

Implementation prepared before this successor execution:

- `code/iter504u_critic_c4_fixture_repair_gate.py`;
- implementation commit `151c4ea951c04278811e4c557847e01b32bbb97c`;
- implementation blob `20a854869dbd0a61824b6c7e8a4f829507f5b126`.

No output from this implementation has been consumed before this freeze.

## Frozen dependencies

- source held-out prereg `05b8e9354c9a7805f0fce18b904346a986a0787f`;
- source-run launch head `102c7f9cafec956f3bc7bed4384ae755c98f761a` remains scientifically untouched;
- original Critic blob `c2a7ea31ddc151bf02a3995d761cae95bdabd0db`;
- isolated repair wrapper commit `f5cd17136ddfee8864bb7a46abbdb464f666f518`, blob `bcea2946a0f9676b50897dc4bbe74fa1122a9965`;
- parent formal prereg `662e1b40c4584a5b1989b821cd7a5c334ef8fc44`;
- parent terminal invalid record `77189486ba4db1dd281832b962b1be290e323944`.

Production evaluator, assembler and aggregate classifier remain unchanged:

- evaluator `bf457eef08f7df32523c9e22ce3b3713f10d97a0`;
- assembler `5c3b04f25c5fb2523c3788b725ccf84ca23a07f1`;
- aggregate `23165f9d99ff9a2f90c27a51cb889d5920327f92`.

## Frozen synthetic baseline

The gate constructs all six frozen held-out case identities H0–H5 using only structural constants already encoded by the shared Critic:

- exact causal/block/path/box/direction/sign identities from `base.EXPECTED`;
- exact rational parent intervals from `base.box_interval`;
- one depth-0 leaf spanning the full parent interval per case;
- `visited_node_count=1`, no parent-child inclusion records;
- all four rho rows structurally coherent and certified;
- full 16-entry R×rho possible-max grid, each with a valid channel identity `[0]`;
- 243-channel contract, precision 384, threshold `1/20`, floor `1`, `MAX_DEPTH=3`, exact-decision transport and binding tags unchanged.

The numeric display-only fields in this synthetic fixture are inert placeholders and carry no scientific authority.

## Required shared-validator controls

1. `base.validate_all(coherent_fixture) == []`.
2. Apply only the already-frozen `repair.force_c4_contradiction` to a copy; then:
   `base.validate_all(contradicted_fixture) == ['H0_AMP_LOW:C4_leaf_binding']`.
3. Repeat from a carrier whose H0 first leaf and first rho begin uncertified; after applying the deterministic repair constructor, the same exact shared-validator error must result.
4. `repair.negative_controls(coherent_fixture)` must have every control true.
5. Frozen producer/assembler/aggregate/original-Critic/repair-wrapper identities must match.
6. No source-run science artifact may be read or imported.
7. Independent Python 3.11 and 3.13 executions must emit byte-identical decision JSON/payload SHA.

## PASS

`ITER504U_CRITIC_C4_SHARED_VALIDATOR_REPAIR_VALIDATED_SCOPED`

iff all required controls pass in both Python environments, their outputs are byte-identical, and no held-out science payload is consumed.

## FAIL

`ITER504U_CRITIC_C4_SHARED_VALIDATOR_REPAIR_FAIL_SCOPED`

iff provenance is valid but the coherent synthetic fixture is rejected, the contradiction is not rejected for exactly the C4 binding, false-carrier outcome independence fails, the full repaired negative-control suite fails, or the two environments disagree.

## INVALID

`INVALID_IMPLEMENTATION`

iff any frozen code identity differs, source science is accessed, production science/classifier/cohort/threshold/depth/channel/partition semantics change, or criteria change after execution.

## Interpretation ceiling

PASS validates only the Critic C4 synthetic fixture repair through the shared validator. It does not classify source run `35246605860`, does not modify any held-out value, and does not authorize all-Iter504/D7/model/family/selector/Candidate Gravity/Paper IV/global quantum-gravity conclusions.

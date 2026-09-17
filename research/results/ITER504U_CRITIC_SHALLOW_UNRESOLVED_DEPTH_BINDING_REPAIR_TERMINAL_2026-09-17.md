# Iter504U Critic shallow-unresolved depth-binding repair — terminal methodology result

Date: 2026-09-17
Status: TERMINAL_METHODOLOGY_AUTHORITY

## Gate

`ITER504U_CRITIC_SHALLOW_UNRESOLVED_DEPTH_BINDING_REPAIR_GATE`

## Classification

`ITER504U_CRITIC_SHALLOW_UNRESOLVED_DEPTH_BINDING_REPAIR_VALIDATED_SCOPED`

This is a methodology / independent-Critic authority result only. It does not classify Iter504U science.

## Frozen authority

- preregistration commit: `a2dc229c849f5b15668e984b5947eb45386757f3`
- preregistration blob: `82b9ce891855771f9614ac5bb44581527bcb8136`
- repair wrapper commit: `1ca51a9fa7875509f38c5bed445ce5d1793d26eb`
- repair wrapper blob: `d10bb168e93b3e3b5496a4f40bb0f16a9bd59dd4`
- formal evaluator commit: `0644bc7897ffcbd8842bcf33e63417901fa4ebfd`
- formal evaluator blob: `8f70f7c45b140b72c81f2d8fd158c61e0159d040`
- workflow commit: `d8b7690ff9784d291b9dd23b1f08b435ad4f9d58`
- workflow blob: `023438709dbc9f7f47824a5285d3669899757e27`
- authority commit: `97f3abbce2c4749d8f5ee0bdae7fb6e678fc0379`
- launch/head: `2d1f4e89f6fec1055a45505f58de167ef32b8fd0`
- execution count: 1
- Actions run: `35266020916`

Frozen upstream identities remained unchanged:

- producer blob `bf457eef08f7df32523c9e22ce3b3713f10d97a0`
- assembler blob `5c3b04f25c5fb2523c3788b725ccf84ca23a07f1`
- aggregate blob `23165f9d99ff9a2f90c27a51cb889d5920327f92`
- original Critic blob `c2a7ea31ddc151bf02a3995d761cae95bdabd0db`
- validated C4 wrapper blob `bcea2946a0f9676b50897dc4bbe74fa1122a9965`

## Actions result

Run `35266020916` completed successfully.

Jobs:

- source-lock `105353291617`: success
- replay Python 3.11 `105353329609`: success
- replay Python 3.13 `105353329849`: success
- aggregate `105353392100`: success

Artifacts, all unexpired at terminal read:

- `iter504u-shallow-depth-repair-3.11`: id `10516133819`, digest `sha256:2babfa6d0e0f531f6bec555056d5c556c3bc57669ff5ebd275a5533a6f498c1d`
- `iter504u-shallow-depth-repair-3.13`: id `10517121305`, digest `sha256:efaf017adafb07a981d9dd1024468b439f509261f7d248796af3873bd1cdbae3`
- `iter504u-shallow-depth-repair-aggregate`: id `10517086354`, digest `sha256:383e1a51cdb7142a24ca3f8cad4514bc7165f2801229447f2b6c7fc76b597ab5`

Python 3.11 and 3.13 result JSON and returncode were required byte-identical by the aggregate job and passed.

Formal payload SHA256:

`71766a16b881c0358e2aded5bdf085dc6e4944ca0ffa4db4c2385f6bc3c42bc5`

## Counterexample / repair result

The frozen pre-repair shared validator accepted the outcome-independent synthetic shallow-unresolved counterexample:

`shallow_pre_validation_errors = []`.

The repaired validator rejected the exact same object solely as:

`H0_AMP_LOW:premature_unresolved_leaf_depth`.

The repaired rule is exactly:

`leaf.certified == false => leaf.depth == MAX_DEPTH`

with frozen `MAX_DEPTH = 3`.

A coherent unresolved terminal object at depth 3 remained accepted before and after the repair.

## Regression controls

- coherent baseline accepted before repair: PASS
- coherent baseline accepted after repair: PASS
- pre-repair validator accepts shallow counterexample: CONFIRMED
- repaired validator rejects exact shallow-depth binding: PASS
- coherent depth-3 unresolved terminal leaf accepted: PASS
- C4 contradiction still rejected exactly as `H0_AMP_LOW:C4_leaf_binding`: PASS
- full previously validated C4 negative-control suite preserved: PASS
- successor negative-control suite including `premature_unresolved_leaf_depth`: PASS
- producer gate/prereg unchanged: PASS
- original Critic/C4 wrapper identities frozen: PASS
- `production_science_consumed=false`
- `source_run_classified=false`

## Interpretation

The preterminal audit's depth-binding candidate is a real authority-path validation defect, not a producer-science failure. The immutable producer recursion already bisects uncertified nodes until frozen depth 3. The repair therefore belongs only in the independent Critic successor used for terminal closure.

A future terminal closure must use `code/iter504u_heldout_critic_depth_binding_repair.py`, preserve the validated C4 controls, and accept the frozen Iter504U terminal taxonomy including `ITER504U_INVALID` when actual immutable artifacts violate implementation/provenance constraints.

## Claim ceiling

This result proves only the independent-Critic shallow-unresolved depth-binding repair at scoped methodology level. It does not classify run `35246605860`; does not imply PASS, INCONCLUSIVE, or INVALID science; and authorizes no all-domain, D7, model-family, Candidate Gravity, Paper IV, `ALL_KNOWN_MODELS_FAIL`, `NEW_THEORY_REQUIRED`, `QUANTUM_GRAVITY_SOLVED`, or `NEW_PHYSICS_FOUND` claim.

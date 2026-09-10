# KMQGB Recovery Delta — Iteration 190

Date: 2026-09-10

## Starting authority

- main at Iter189: `a01e30e99a3a27959fdbbd9e299f947a15f5f95c`.
- Iter189 methodology CI run `34431893468`, job `102728958236`: completed SUCCESS; all methodology-self-test steps passed.
- RQIR Core v1.0 remains FROZEN.
- Tier-1 census: 14 required, 1 terminal, 13 nonterminal; Tier-2 unresolved = 0.
- D2/D4/D7 nonterminal; global decision `NOT_YET_AUTHORIZED`; Candidate Gravity R3=24% inactive.

## Iter190 scientific action

Audited the Hořava-Lifshitz family split using primary literature for the projectable scalar sector and the non-projectable/BPS extension.

New authority:
`paper_iv/O_HORAVA_PROJECTABLE_NONPROJECTABLE_FAMILY_FORK_AUDIT_2026-09-10.md`.

New scoped classification:
`PASS_RQIR_GATE__HORAVA_MATERIAL_PROJECTABILITY_FORK_AND_EXTRA_MODE_OBJECT_IDENTIFIED`.

## What is closed

- Projectable and non-projectable Hořava branches are frozen as materially distinct Paper-IV branches because projectability changes the constraint/scalar sector.
- The projectable extra scalar is admitted as a concrete observable target, not merely a taxonomy label.
- The non-projectable/BPS low-energy scalar-tensor sector is admitted as a distinct target.
- A result for one branch cannot be promoted to family-level without branch-by-branch terminal disposition or an explicit reduction/equivalence theorem.

## What remains open

The family remains `PARTIAL_SUBFAMILY_ONLY` because neither branch yet has a complete same-realization UV->IR trajectory with normalized observable, comparator, provenance and controlled error/remainder.

Next gates:
1. `HORAVA_PROJECTABLE_UV_TO_IR_TRAJECTORY_PLUS_EXTRA_SCALAR_NORMALIZED_OBSERVABLE_CERTIFICATE`.
2. `HORAVA_NONPROJECTABLE_BPS_UV_TO_IR_TRAJECTORY_PLUS_SCALAR_TENSOR_COMPARATOR_CERTIFICATE`.

## Global decision impact

No family-level terminal row changed:
- Tier-1 terminal = 1/14.
- Tier-1 nonterminal = 13/14.
- Tier-2 unresolved = 0.
- D2 = NOT_CLOSED.
- D4 = NOT_CLOSED.
- D7 = NOT_CLOSED.
- global decision = `NOT_YET_AUTHORIZED`.
- `NEW_REQUIRED=false`.
- Candidate Gravity R3 = 24%, inactive.

## Compute policy

Heavy compute remains IDLE. The blocker is structural/provenance UV->IR matching, so an IR numerical parameter scan cannot create the missing same-realization ancestry.

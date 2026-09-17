# Iter504U repaired closure — source terminal semantics repair

Date: 2026-09-17
Status: PROSPECTIVELY_FROZEN_BEFORE_CLOSURE_AUTHORITY_AND_BEFORE_TERMINAL_SCIENCE_CONSUMPTION

## Scope

This is an outcome-independent closure/provenance repair only. It does not change producer science, the held-out cohort, scientific criteria, frozen PASS/INCONCLUSIVE/INVALID taxonomy, C4 repair, shallow-unresolved depth-binding repair, or immutable source run `35246605860`.

No partial Iter504U scientific payload has been consumed in deriving this repair.

## Defect

The immutable source workflow `.github/workflows/iter504u-heldout-science.yml` contains, after the required producer/assembly/aggregate DAG, the historical original Critic job. That original Critic predates the terminal C4 and shallow-unresolved depth-binding repairs.

Therefore the overall GitHub Actions run conclusion is not a sufficient admissibility predicate for repaired closure: the run may be terminal `failure` solely because the obsolete original Critic rejects or mishandles its control layer, while all required immutable upstream science artifacts are successfully produced.

Requiring `source_run.conclusion == success` in the prepared repaired-closure workflow would incorrectly convert an already-localized Critic/control defect into a producer-science execution failure and could force an unauthorized producer rerun.

## Frozen repaired source-admissibility rule

The future repaired closure may proceed only when all of the following hold:

1. source run id is exactly `35246605860`;
2. source head is exactly `102c7f9cafec956f3bc7bed4384ae755c98f761a`;
3. run attempt is exactly `1`;
4. run status is exactly `completed`;
5. the actual overall run conclusion is recorded prospectively in closure authority, but is not required to equal `success`;
6. source-lock job completed `success`;
7. all 12 frozen case jobs completed `success`;
8. both frozen assembly jobs completed `success`;
9. the frozen aggregate job completed `success`;
10. exactly the 15 required upstream artifact names are frozen in closure authority with exact IDs, digests, source head and non-expired state: 12 case artifacts + 2 assembly artifacts + 1 aggregate artifact;
11. the historical original source-workflow Critic job and any Critic artifact are explicitly excluded from the repaired closure input authority;
12. the future repaired Critic consumes only the prospectively frozen 15 upstream artifacts and independently reconstructs the frozen science classification.

The closure authority must freeze exact required upstream job names/IDs/conclusions in addition to artifact identities. The closure workflow must re-fetch both run metadata and run jobs and fail closed if any required upstream job identity or success conclusion differs.

## Required upstream jobs

Required job names are exactly:

- `source-lock`;
- `cases (3.11, H0_AMP_LOW)`;
- `cases (3.11, H1_AMP_MID)`;
- `cases (3.11, H2_CAUSAL_1)`;
- `cases (3.11, H3_CAUSAL_2)`;
- `cases (3.11, H4_DIRECTION)`;
- `cases (3.11, H5_SIGN)`;
- `cases (3.13, H0_AMP_LOW)`;
- `cases (3.13, H1_AMP_MID)`;
- `cases (3.13, H2_CAUSAL_1)`;
- `cases (3.13, H3_CAUSAL_2)`;
- `cases (3.13, H4_DIRECTION)`;
- `cases (3.13, H5_SIGN)`;
- `assemble (3.11)`;
- `assemble (3.13)`;
- `aggregate`.

All must be `completed/success` in the exact source run. The historical `critic` job is not in this set.

## Claim ceiling

This repair establishes only source/provenance admissibility for a future repaired independent Critic closure. It does not classify Iter504U science, does not authorize producer rerun, and does not authorize any all-domain, D7, Candidate Gravity, Paper IV, `ALL_KNOWN_MODELS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `QUANTUM_GRAVITY_SOLVED`, `UNIQUE_MECHANISM`, or `NEW_PHYSICS_FOUND` claim.

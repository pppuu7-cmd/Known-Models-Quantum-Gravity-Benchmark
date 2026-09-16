# SOURCE_J1_K5_EQ4_TRIANGLE_WEDGE_GROUP_ARGUMENT_IDENTITY_GATE — execution-only repair freeze

Date: 2026-09-16
Status: PROSPECTIVELY_FROZEN_EXECUTION_REPAIR_ONLY

## Trigger

Authoritative workflow run `35142365235` terminated before any scientific classifier lane executed. The `source-lock` job failed because `actions/checkout@v4` used the default shallow `fetch-depth: 1`, while the frozen provenance control calls `git merge-base --is-ancestor` on preregistration/authority/source/Critic commits. The runner therefore reported `fatal: Not a valid commit name ddf246b861d4e367af409e3ae5b6c97ccfd1ea7e`.

This is an execution/provenance-realization defect. It is not PASS, BLOCKED, FAIL, or INVALID scientific evidence for the frozen wedge-identity object.

## Frozen repair

The only authorized implementation change is to make repository history available to the already-frozen ancestry checks by setting `fetch-depth: 0` on checkout steps in the gate workflow. No source record, source hash, extracted wedge identity, classifier logic, fixture, threshold, identity convention, multiplication order, inversion, orientation, contact argument, PASS/BLOCKED/INVALID criterion, or governance lock may change.

Frozen scientific authority remains:

- gate preregistration `ddf246b861d4e367af409e3ae5b6c97ccfd1ea7e`;
- authority freeze `440c853516c2357029c848c83e48a7f6a39d0c86`;
- source extraction `4a21e9148393ebcefdfbb2a17cfbbf51af82b052`;
- independent Critic `18133e8de9f919960e7100952da3aeee77c0bc06`;
- classifier implementation `1f48955a2f8b15a544121ab07675cdba8830907f`;
- aggregate implementation `a4263330c207b5fdc048fa1996a3e64652490f72`.

## Decision discipline

After repair, both frozen Python 3.11 and Python 3.13 lanes and the frozen aggregate must execute. Only the resulting terminal aggregate may classify the scientific gate. The failed run `35142365235` remains historical execution evidence and must not be reinterpreted as a scientific outcome.

Governance locks remain unchanged: `RQIR Core v1.0 = FROZEN`; `D7-S2 = NOT_CLOSED`; `D7-S3 = NOT_CLOSED`; `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`; Candidate Gravity inactive; terminal selector labels unauthorized; `BLOCKED != FAIL`; missing rank != rank zero.

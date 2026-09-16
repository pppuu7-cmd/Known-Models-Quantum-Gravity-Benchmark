# ITER504P aggregate-only runner fallback

Date: 2026-09-17
Status: PROSPECTIVELY FROZEN EXECUTION-ONLY FALLBACK

## Trigger

Repaired Iter504P production run `35151656186` at head `b7f4f1f94d7668eba22c8bad25050ef632648ec9` has completed successfully through source-lock and both independent point-drift arithmetic lanes, while its aggregate job remains queued. No production lane payload has been consumed for a substantive conclusion.

Immutable completed-lane artifact metadata from GitHub Actions:

- `iter504p-point-drift-decimal`: artifact `10468939725`, digest `sha256:aeeac0ba27efa51bf05b7da1761b799c257d4c94b0c9c7db20bd3e935217fb06`, workflow run `35151656186`, head `b7f4f1f94d7668eba22c8bad25050ef632648ec9`;
- `iter504p-point-drift-float`: artifact `10469641510`, digest `sha256:4034866a04e7221c576ec58da3d6c2ac1429b26081e4814a958f240e7b25d621`, workflow run `35151656186`, head `b7f4f1f94d7668eba22c8bad25050ef632648ec9`.

## Frozen fallback

A separate `windows-latest` job may:

1. verify the two artifact IDs, digests, run ID and workflow head against GitHub metadata;
2. download exactly those two completed artifacts by name from run `35151656186`;
3. execute the already-frozen aggregate implementation `code/iter504p_point_drift_localization_aggregate.py` from implementation commit `e18ed81f33271e3cab66ac8b67119587702eb7d2`;
4. upload the resulting aggregate JSON.

It MUST NOT rerun or modify point computations, inspect the nondecisive control separately, change classifier semantics, modify lane payloads, or choose an outcome-dependent criterion.

## Scientific immutability

Unchanged and authoritative:

- Iter504P preregistration `77bac4728401200b226dda16447befce85df0c66`;
- upstream Iter504 run/head;
- exact 11-lane decisive cohort and 1584-record contract;
- exclusion of `0to5-b0` from the decision;
- formula `D_point = abs(actual_slope - early_actual_slope)`;
- threshold `0.05`;
- classifications WITHIN / VIOLATION / INVALID;
- classifier `37a04752ccee6fd1caa901df36ecfcf5f50dced4`;
- aggregate `e18ed81f33271e3cab66ac8b67119587702eb7d2`.

This fallback changes only runner/orchestration availability. If the original queued aggregate later completes, both aggregate payloads must agree on their scientific fields or Iter504P cannot be terminalized as PASS/VIOLATION without resolving the discrepancy.

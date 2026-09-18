# Iter504V source-lock literal-quote repair — preregistration

Date: 2026-09-18
Status: FROZEN_BEFORE_IMPLEMENTATION_AND_RELAUNCH

## Gate

`ITER504V_SOURCE_LOCK_LITERAL_QUOTE_REPAIR`

The second Iter504V source launch, run `35365231496` at head `99b7613cfba1c7f62838b63d507f8f084e6657ab`, again failed in `source-lock` before any case job executed. No scientific payload was produced or consumed.

## Exact defect

The repaired-U authority blob check in `.github/workflows/iter504v-sentinel-science.yml` was serialized as:

`test \"$(git hash-object <path>)\" = '<sha>'`

The backslash-escaped double quotes are literal shell characters in the first argument, so the predicate compares a quoted string such as `"abc..."` against unquoted `abc...` and fails before later source-lock checks execute.

## Frozen repair

Change only that shell predicate to:

`test "$(git hash-object <path>)" = '<sha>'`

Retain the direct frozen core blob checks introduced by the previous repair. Do not change evaluator, assembler, aggregate, sentinel cohort, precision, channel set, R/rho, threshold, floor, partition, MAX_DEPTH, classifier, or interpretation.

Relaunch exactly one source production under a new prospective execution authority.

Both prior failed runs remain pre-science execution failures, not scientific Iter504V outcomes. Phase B remains unauthorized.

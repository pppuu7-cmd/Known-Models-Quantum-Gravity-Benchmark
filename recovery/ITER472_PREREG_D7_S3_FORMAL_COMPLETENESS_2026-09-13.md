# Iter472 preregistration — D7-S3 formal same-realization completeness matrix

Date: 2026-09-13
Status: FROZEN BEFORE IMPLEMENTATION
Source of requirements: `protocol/PAPER_IV_D7_GLOBAL_DECISION_CONTRACT.json` D7-S3.

## Question
What explicit machine-readable positive/negative declarations currently exist in the repository for the four D7-S3 requirement classes, without inferring missing physics from filenames or prose?

## Frozen requirement classes
1. same-realization physical-object identity;
2. microscopic/effective parameter transport without identity swaps;
3. normalized comparator-ready observable;
4. propagated theory/nuisance/covariance/numerical error certificate.

## Frozen audit rule
Scan tracked UTF-8 JSON/Python/Markdown files for an explicit whitelist of declaration tokens: `same_realization`, `transport_ready`, `parameter_transport`, `normalized_comparator`, `comparator_ready`, `nuisance`, `covariance`, `error_certificate`, `propagated_error`, plus explicit boolean assignments/JSON values in the same local record. Classify only explicit booleans as POSITIVE or NEGATIVE; lexical mentions without a boolean/clear status are MENTION_ONLY. No prose mention can close a gate.

A D7-S3 class can be reported FORMAL_POSITIVE_CANDIDATE only if at least one explicit positive declaration is found and no contradictory negative declaration exists for the same named realization/artifact. Otherwise it remains NOT_FORMALLY_CLOSED. This audit itself never closes S3.

## Controls
- A synthetic positive fixture must be detected in the test logic but must never be written into the repository evidence set.
- A synthetic negative fixture must be detected.
- MENTION_ONLY text must not count as positive.
- Existing known negative declarations in `code/lqg_entropy_observable_common.py` must be recovered if still present.

## PASS label
`ITER472_D7_S3_FORMAL_DECLARATION_MATRIX_COMPLETE_SCOPED` means the frozen audit executed correctly. It is not D7-S3 closure.

## Scope guards
No invented parameter map, no conversion of absence into physical impossibility, no terminal D7 label, and no Candidate Gravity activation.
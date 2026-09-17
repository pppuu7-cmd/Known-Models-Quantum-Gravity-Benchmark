# ITER504U_C4_SHARED_VALIDATOR_DIAGNOSTIC — execution-only freeze

Date: 2026-09-17
Status: `PROSPECTIVELY_FROZEN_BEFORE_DIAGNOSTIC_REPLAY`

## Parent run

Shared-validator repair run `35251855175`, head `fb6a9b4b15219f406d2af7a89de3a6db1f1247c5`, has terminal workflow failure in both Python 3.11 and 3.13 validation lanes after successful source-lock. The evaluator output was redirected to `out/result.json`, then a classification assertion failed before artifact upload, so the exact synthetic validator error set is not recoverable from the terminal logs.

This diagnostic does not repair or alter the evaluator, validator, fixture constructor, criteria or classifications. It exists only to make the already-produced deterministic synthetic evaluator JSON observable.

## Frozen object

Execute exactly the existing evaluator:

- path `code/iter504u_critic_c4_fixture_repair_gate.py`;
- commit `151c4ea951c04278811e4c557847e01b32bbb97c`;
- blob `20a854869dbd0a61824b6c7e8a4f829507f5b126`;

against the exact unchanged dependencies:

- original Critic blob `c2a7ea31ddc151bf02a3995d761cae95bdabd0db`;
- repair wrapper blob `bcea2946a0f9676b50897dc4bbe74fa1122a9965`.

No production/held-out artifact, aggregate or science payload may be downloaded, imported or read.

## Diagnostic execution

Run independently under Python 3.11 and 3.13.

For each lane:

1. execute the frozen evaluator exactly once;
2. capture stdout verbatim to `result.json` with `tee`;
3. preserve the evaluator process return code without aborting before upload;
4. require return code to be either `0` (formal PASS) or `2` (formal frozen FAIL classification), with JSON parseable in either case;
5. record SHA256 of the JSON and return code;
6. upload the diagnostic artifacts regardless of `0/2`;
7. do not reinterpret or modify the JSON.

The aggregate diagnostic must require byte-identical JSON and equal return code across Python 3.11/3.13.

## Allowed inference

This diagnostic may only localize the synthetic methodology mismatch in the already-frozen shared-validator gate. It cannot by itself convert the parent run to PASS, cannot modify the formal preregistration and cannot classify Iter504U held-out science.

After the exact error set is known, any corrective fixture change requires a new prospectively frozen minimal successor before implementation/execution.

## Invalid diagnostic

Any change to the evaluator/dependency blobs, any access to run `35246605860` science payloads, any environment disagreement, unparseable result, or evaluator exit outside `{0,2}` makes this diagnostic invalid.

## Claim ceiling

No scientific, all-domain, D7, model/family, selector, Candidate Gravity, Paper IV or quantum-gravity conclusion is authorized by this diagnostic.

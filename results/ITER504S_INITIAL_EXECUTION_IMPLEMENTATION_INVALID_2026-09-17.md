# Iter504S initial execution — implementation-invalid, non-authoritative for science

Date: 2026-09-17
Status: TERMINAL EXECUTION RECORD

This record does **not** assign any Iter504S scientific terminal class. The frozen scientific classifier remains unchanged and consists only of:

- `ITER504S_ROOT_DERIVATIVE_RADIUS_LOCALIZED_SCOPED`
- `ITER504S_CHANNEL_COMPETITION_NECESSARY_SCOPED`
- `ITER504S_FIXED_CHANNEL_NONSTATIONARITY_REMAINS_SCOPED`
- `ITER504S_MIXED_MECHANISM_SCOPED`
- `ITER504S_INVALID`

The first execution is non-authoritative for scientific classification because it failed at an implementation/type-representation defect that had already been prospectively identified before substantive Iter504S output consumption.

## Frozen authority

- scientific preregistration: `f6367456aa715fe6282ab70c1b2005971a4568c7`
- initial evaluator: `a008d782618ac6a1c397d571ed091138107ac1ee`
- initial assembler: `0ef4a6c8e193eec5294485997e4cfdd60e8c0d19`
- initial aggregate: `3f5c21056d9d701948c918b307f76c67f17eed41`
- initial workflow head: `cb50a107b24232ef1b652baa9443e69fc3fa6ca1`
- initial Actions run: `35173442220`
- run number: `1`
- run attempt: `1`
- terminal workflow state: `completed/failure`

## Root job terminal states

Source-lock job `105049847857` completed/success.

All six root jobs completed/failure in the same workflow step `Execute frozen root mechanism discriminator`:

- Python 3.11 / root 13: job `105049872381`
- Python 3.11 / root 14: job `105049872316`
- Python 3.11 / root 15: job `105049872326`
- Python 3.13 / root 13: job `105049872364`
- Python 3.13 / root 14: job `105049872329`
- Python 3.13 / root 15: job `105049872397`

Assembly was skipped because no successful root cohort existed. Aggregate job `105055614760` also completed/failure after artifact download failed; this is downstream execution fallout and carries no science.

## Exact defect witness

Independent job logs from different Python environments and roots report the same evaluator-invalid signature:

`TypeError("cannot create acb from type <class 'iter503_ad_core.CD'>")`

Verified examples:

- Python 3.11 / root 14 job `105049872316`
- Python 3.11 / root 15 job `105049872326`
- Python 3.11 / root 13 job `105049872381`
- Python 3.13 / root 13 job `105049872364`

Each evaluator wrote only an `invalid=true` root record and exited with code `2`; no valid LOW/MID/HIGH mechanism cases were produced.

This matches the prospectively frozen execution-only derivative representation defect exactly: `iter503_ad_core.dcontract_all()` returns dual `CD` objects, whereas the frozen Iter504R/Iter504S affine derivative object is `ad.as_c(z).d`.

## Partial artifacts

These artifacts are preserved as execution-defect evidence only; they are not scientific evidence.

- `iter504s-3.11-root-13`: artifact `10477569193`, digest `sha256:2b972d8882cc0d5f2b32bf9d9eda0bb4f59b99068c7ef2dfe0eed9f4efd3a0ca`
- `iter504s-3.11-root-14`: artifact `10477818291`, digest `sha256:6b4f57b147bb8e06319b16a83a7edc5603f542b168a7ca9c308195ddd262813c`
- `iter504s-3.11-root-15`: artifact `10478361480`, digest `sha256:84ecf518a4ac8bc1f2146d0bb07e0ca7a82098f267ee3ff44cda4382f17e20e2`
- `iter504s-3.13-root-13`: artifact `10478350909`, digest `sha256:2331c9a900fe0df48b1e95f792eba7f9b1fae1d34fad0550d9b3302cdd9d8005`
- `iter504s-3.13-root-14`: artifact `10478362147`, digest `sha256:c65e2fb503ce3da530e574c13d9c0aff9d3790d24a60ec4e69d27df38467d00f`
- `iter504s-3.13-root-15`: artifact `10478218141`, digest `sha256:450aeaaa8549be1b3a52134fbba533c12427b252421672ece7b1036894da124a`

## Prospectively frozen repairs

Both repairs predate repaired execution and substantive scientific output consumption:

1. derivative-component extraction repair preregistration `88c92f86a765e9d8b441152674fc2c303f3f1ff3`;
2. fixed-channel drift-only competition repair preregistration `4ef41c0f4ceed3082fd4d80930ef5d848f18802b`.

No scientific point, root, rho, R value, threshold, floor, precision, source, channel count, no-pruning rule, mechanism category, or terminal classifier is changed by these repairs.

## Repaired implementation prepared before launch

Non-triggering repaired modules were prepared only after the repairs had been frozen and without launching a second scientific execution:

- repaired evaluator commit `b20077e77b421a68f1a99135ff652e52a0d53227`
- repaired assembler commit `7dc689f9b4d7e4f768a677e2afc80668a15b73d9`
- repaired cross-environment aggregate commit `b0347e225b986b63e079ef6ebf02cd928022eb39`
- repaired adversarial Critic commit `38c705865b0397c7cf664ad142ad232d3b0a312f`

The repaired evaluator explicitly extracts `ad.as_c(z).d`; the fixed-channel competition predicate is reconstructed from `max_fixed_channel_drift_upper <= 0.05` when the competition test is complete. The full-envelope predicate remains `S_lower >= 1.0` and `drift_upper <= 0.05`.

## Claim ceiling

This is an implementation-invalid execution record only. It is not a scientific FAIL, not evidence for or against any Iter504S mechanism, not a full-domain result, and not quantum-gravity evidence.

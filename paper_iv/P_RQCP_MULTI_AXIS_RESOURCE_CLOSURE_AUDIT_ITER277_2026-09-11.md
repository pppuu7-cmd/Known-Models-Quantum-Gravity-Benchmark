# Iter277 — RQCP multi-axis resource-closure audit

Date: 2026-09-11

## Scope

This audit follows the Iter275 promotion of `RELATIONAL_QUANTUM_CAUSAL_PROCESSES` into the frozen Paper-IV Tier-1 census and the Iter276 repair/validation of the 15-row decision stack. It does **not** modify RQIR Core v1.0 and it does **not** treat a scoped numerical result as family-level quantum-gravity closure.

The narrow question is whether the published fixed-band RQCP Einstein-response result remains numerically stable under resource axes that are independent of the already certified spatial-regulator sequence.

Three independent probe classes were executed:

1. local oscillator Hilbert cutoff;
2. quartic-coupling variation around the published point;
3. mixed geometry-matter finite-difference/Richardson step variation.

The probe implementation is independent of the upstream RQCP package: `code/rqcp_fixed_band_probe_common.py` re-implements the declared two-mode Hamiltonian using NumPy and does not import the upstream RQCP code.

## Reproducibility controls

The published cutoff-8 point is reproduced to floating numerical precision:

- published / independently reproduced `Newton_response_G = 23.2002807522111...`;
- published / independently reproduced `mass_gap = 0.48633956724666...`;
- published / independently reproduced `G * gap^2 = 5.48747365758299...`;
- cutoff-8 relative deltas are of order `10^-15`;
- the published mixed response at `sigma_step=10^-3` is reproduced with relative delta about `5.1e-11`.

This establishes that the cutoff study is not caused by a mismatch of the baseline implementation.

## Parallel computation provenance

### First robustness wave

Workflow: `rqcp-scoped-robustness-probes`

Run: `34551324978`

Execution:

- 19 independent jobs;
- up to 8 run concurrently;
- 7 Hilbert cutoffs: `4,6,8,10,12,14,16`;
- 7 quartic factors: `0,0.5,0.75,1,1.25,1.5,2`;
- 5 mixed-response steps: `5e-4,1e-3,2e-3,5e-3,1e-2`;
- then one aggregate job after the dependency barrier.

Result: all 19 independent jobs plus the aggregate job completed successfully.

### High-cutoff extension

Workflow: `rqcp-cutoff-extension`

Run: `34551533448`

Independent parallel cutoffs: `18,20,24,28`.

Result: 4/4 jobs completed successfully.

## Hilbert-cutoff result

| cutoff | Hilbert dimension | G | mass gap | G gap^2 |
|---:|---:|---:|---:|---:|
| 4 | 16 | 59.010995410651084 | 0.2201997863154973 | 2.861321952586775 |
| 6 | 36 | 24.751525667589727 | 0.46069742368521904 | 5.251957449414968 |
| 8 | 64 | 23.200280752211146 | 0.48633956724666694 | 5.487473657582998 |
| 10 | 100 | 21.809484424122982 | 0.499214520584097 | 5.435259236822587 |
| 12 | 144 | 21.5409284181087 | 0.5013796809782525 | 5.41432102821346 |
| 14 | 196 | 21.51013837956672 | 0.501713727090391 | 5.414460274027426 |
| 16 | 256 | 21.50232102803958 | 0.5017421496959152 | 5.413105780434489 |
| 18 | 324 | 21.50115669884191 | 0.5017456279937786 | 5.4128877144348015 |
| 20 | 400 | 21.500993416081617 | 0.501746042954463 | 5.412855561436078 |
| 24 | 576 | 21.500968814791843 | 0.5017460967618718 | 5.412850529035239 |
| 28 | 784 | 21.50096842760798 | 0.5017460974407341 | 5.412850446209202 |

### Quantified shifts

Published cutoff 8 -> cutoff 28:

- `G`: relative shift about `7.3245%`;
- mass gap: relative shift about `3.0706%`;
- `G gap^2`: relative shift about `1.3599%`.

High-cutoff stabilization:

- cutoff 16 -> 18: `G` changes by about `5.41e-5` relative;
- 18 -> 20: about `7.59e-6`;
- 20 -> 24: about `1.14e-6`;
- 24 -> 28: about `1.80e-8`.

At cutoff 24 -> 28:

- `G`: relative change `~1.80e-8`;
- mass gap: relative change `~1.35e-9`;
- `G gap^2`: relative change `~1.53e-8`.

Therefore the cutoff-8 observable is materially displaced relative to the empirically stabilized high-cutoff sequence, while the high-cutoff sequence itself shows rapid numerical stabilization. This is a resource-axis sensitivity result, not evidence of an instability at large cutoff.

No infinite-cutoff theorem is claimed from the finite sequence alone.

## Quartic-coupling probe

Over the finite grid from `0` to `2 * lambda_*` at cutoff 8:

- `G` remains positive;
- `G` ranges approximately `22.9964 ... 23.4104`;
- `G gap^2` ranges approximately `5.45391 ... 5.52197`.

This is modest local parameter sensitivity relative to the much larger cutoff-8 -> high-cutoff shift. It is not a statement about arbitrary coupling or family-level parameter closure.

## Mixed-response step probe

Across `sigma_step = 5e-4 ... 1e-2`:

- mixed response span is about `7.43e-7`;
- relative span is about `5.67e-8`.

The mixed response is therefore strongly stable against the tested numerical derivative step. This does not address the independent physical-domain cutoff.

## Scientific classification

Scoped result:

`PASS_SCOPED_BASE_REPRODUCTION_AND_HIGH_CUTOFF_STABILIZATION__PUBLISHED_CUTOFF8_EINSTEIN_RESPONSE_IS_MATERIALLY_SHIFTED_RELATIVE_TO_THE_HIGH_CUTOFF_PLATEAU`

Family status remains:

`RELATIONAL_QUANTUM_CAUSAL_PROCESSES = PARTIAL_SUBFAMILY_ONLY`

This result does **not** refute the published fixed-band theorem because the upstream construction explicitly treats the finite oscillator cutoff/fixed band as part of the declared physical domain rather than a regulator it claims to remove.

However, KMQGB cannot treat spatial-regulator closure as full resource closure when an orthogonal Hilbert/domain truncation axis changes a normalized gravity observable by percent scale.

## New methodological lesson

The polygon now supplies a concrete counterexample to the following invalid inference:

> convergence on one regulator/refinement axis implies resource closure of the observable.

A stronger general rule is required for benchmark interpretation:

`MULTI_AXIS_RESOURCE_CLOSURE` — every materially independent regulator, truncation, basis/domain, finite-volume, resolution or approximation axis that can change the normalized target observable must either:

1. be removed with a controlled convergence/error certificate; or
2. be justified as a physical input by an autonomous selection principle, with the induced observable uncertainty explicitly propagated.

Closure of one axis does not silently close another.

This is additive benchmark methodology. It does not alter RQIR Core v1.0 and should be considered for Paper III only if Paper III does not already encode the same multi-axis closure requirement.

## Refined RQCP reopen condition

A future family-level RQCP terminalization object must include, in addition to the existing all-band/background-independent/autonomous-gravity requirements, one of:

- a controlled removal/convergence certificate for the local oscillator Hilbert cutoff; or
- an autonomous physical selection principle for the finite cutoff/domain together with propagated uncertainty for normalized gravity observables.

The current finite sequence is strong evidence that this requirement is material rather than cosmetic.

## Global decision effect

None.

- Tier-1: 15 rows;
- strict terminal: 1/15;
- candidate-family terminal: 0/14;
- D2 remains `NOT_CLOSED_COVERAGE_AND_OBJECTS`;
- D3 remains `PARTIAL`;
- D4 remains `PARTIAL_GLOBAL_NOT_CLOSED`;
- D7 remains `NOT_CLOSED / NOT_YET_AUTHORIZED`;
- `NEW_REQUIRED`, `EXISTING_SUFFICIENT`, `ADAPT_EXISTING`, `HYBRID_REQUIRED` remain unauthorized;
- Candidate Gravity remains inactive at canonical R3 = 24%.

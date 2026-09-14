# Iter498 terminal result — continuum-certificate regularity audit

Date: 2026-09-14

## Frozen authority
- Preregistration: `recovery/ITER498_PREREG_CONTINUUM_CERTIFICATE_REGULARITY_AUDIT_2026-09-14.md` (`0bedcbaf7b065b050585f2a3505c8bf0e2a14457`).
- Evaluator: `code/iter498_continuum_certificate_regularity_audit.py` (`2148981be0a808094cd0b4b1b80d2e65fd586807`).
- Aggregate implementation: `code/iter498_aggregate.py` (`432773c916872f6300a2c0e4d56872318eaa03bd`).
- Initial workflow head: `ef8720bbc4cc4e62fa65ca1be5f4cb1c2b460b85`; its source-lock failed on wording only.
- Control-only repair head: `2bc6756dffdbf10b2d70bdf174657f7f2d478864`. Diff changes only the source-lock string predicate `candidate gravity inactive` -> `candidate gravity activation`; no evaluator, preregistration, thresholds, mesh, matrix, or classifier changed.
- Authoritative retry run: `34816799788`.
- Aggregate job: `103890003162`.
- Aggregate artifact: `10337025880`.
- Aggregate digest: `sha256:65851b593dfdc385969e4da67a9e9aa992f328f801521798d2a8c05e349ed814`.

## Terminal classification
`ITER498_MAX_ENVELOPE_NONSMOOTH_BLOCKER_IDENTIFIED_SCOPED`

All 12 frozen jobs are present and valid. There are no missing or invalid job ids and all frozen source/numerical predicates pass.

## Aggregate diagnostics
- total argmax switches: `2`;
- minimum relative top-two gap: `0.0002002130966857187`;
- minimum positive KAK beta: `0.5017347792114244`.

The KAK branch-margin predicate therefore passes by more than five orders of magnitude relative to the frozen `1e-6` floor. The blocker is the max-envelope, not a near-degenerate KAK branch.

Eleven of the twelve jobs are `ITER498_REGULAR_SAMPLED_PATH_QUALIFIED_SCOPED`. The only nonregular sampled job is `0to5-b0`.

## Exact switch localization
Both switches occur on the same frozen path:
- causal class `0to5`;
- direction `[1,1,1,-1,-1,-1]` in active coordinates `[0,1,3,5,6,11]`;
- sign `+1`;
- rho `2.7`;
- amplitude transition `0.00234375 -> 0.00250`.

They occur at:
1. `R=10`: argmax channel index `195 -> 222`; top-two gaps at the two endpoint samples are approximately `2.9244e-4` and `3.3506e-4`.
2. `R=12`: argmax channel index `195 -> 222`; top-two gaps are approximately `2.0021e-4` and `4.2720e-4`.

With the frozen lexicographic `itertools.product(range(3), repeat=5)` channel ordering, these indices are:
- `195 = (2,1,0,2,0)`;
- `222 = (2,2,0,2,0)`.

The crossing is therefore a concrete two-branch competition inside the finite max over genuine five-node intertwiner channels, not an inferred numerical artifact.

## Scientific interpretation
Iter498 does **not** provide a continuum/interval certificate. It prospectively diagnoses why a single-active-channel derivative proof is inadmissible on the frozen amplitude interval: the maximizing channel changes inside the interval.

The preregistered consequence is therefore mandatory: the next continuum attempt must bound the finite max-envelope directly, allowing channel switches, instead of differentiating one selected maximizer. A direct interval treatment may exploit dominance/exclusion of noncompetitive channels only if that dominance is itself validated on the whole interval; sampled dominance is insufficient.

The healthy beta margin means no branch-safe KAK repair is required by Iter498. This does not prove that an interval implementation of the source KAK/network object is available; failure to construct a validated direct envelope must be recorded as a numerical-method blocker.

## Scope ceiling
This result is sampled regularity diagnosis only. It does not establish a uniform angular neighborhood, positive Haar measure, Haar convergence/divergence, the ten source spectral integrations, a physical causal-vertex finiteness/divergence theorem, D7-S2 closure, any terminal D7 label, or Candidate Gravity activation.

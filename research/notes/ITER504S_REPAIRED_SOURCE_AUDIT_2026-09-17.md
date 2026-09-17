# Iter504S repaired implementation — outcome-blind source-level semantics audit

Date: 2026-09-17
Status: COMPLETED WHILE REPAIRED RUN 35175533159 WAS NONTERMINAL

This audit consumed no partial Iter504S mechanism numbers and does not alter the running workflow. It checks the already-frozen repaired source against scientific preregistration `f6367456aa715fe6282ab70c1b2005971a4568c7` and repair authorities `88c92f86a765e9d8b441152674fc2c303f3f1ff3`, `4ef41c0f4ceed3082fd4d80930ef5d848f18802b`.

Audited modules:

- evaluator `b20077e77b421a68f1a99135ff652e52a0d53227`;
- assembler `7dc689f9b4d7e4f768a677e2afc80668a15b73d9`;
- cross-environment aggregate `b0347e225b986b63e079ef6ebf02cd928022eb39`;
- adversarial Critic `38c705865b0397c7cf664ad142ad232d3b0a312f`;
- repaired execution authority `7931e10c31dc8f1db42215117ef2b1b15ac0ed6b`.

## Checks

1. **Derivative representation.** `dcontract_all()` dual channel objects are reduced only by `ad.as_c(z).d`. Full-D retains that Acb derivative ball unchanged. Center-D replaces only that derivative ball by its deterministic real/imaginary midpoint and remains explicitly control-only.

2. **Exact points.** Root intervals and LOW/MID/HIGH points are generated from exact `Fraction` arithmetic and match the preregistered roots 13-15. No fourth point or adaptive point selection exists.

3. **Frozen grids.** Causal/path/sign, roots, rhos, R grid, 384-bit precision, all 243 channels, threshold `0.05` and floor `1.0` remain frozen.

4. **Full-envelope predicate.** `within_tolerance` is reconstructed as `S_lower >= 1.0 AND drift_upper <= 0.05`, unchanged from the science preregistration.

5. **Fixed-channel competition predicate.** A candidate set is complete only when no possible-max candidate is ineligible and eligible count equals candidate count. Competition `all-within` is reconstructed solely from the maximum eligible fixed-channel `drift_upper <= 0.05`. Fixed-channel `S_lower` is not used.

6. **Mechanism flags.** Derivative-radius sensitivity depends on full-D drift `>0.05` and center-D drift `<=0.05`; competition necessary depends on full max-envelope violation plus complete candidate set plus all fixed-channel drifts within threshold; fixed-channel nonstationarity requires center-D max-envelope violation plus complete candidate set plus at least one fixed-channel drift above threshold.

7. **Terminal classifier order.** Derivative-radius localized is tested first; channel-competition necessary second; fixed-channel nonstationarity third; all remaining valid patterns map to MIXED. No fifth post-outcome scientific class exists beyond the preregistered INVALID branch.

8. **Cross-environment authority.** Aggregate compares scientific/discrete projection rather than incidental byte serialization and requires agreement of threshold/floor decisions, possible-max identities, strict-dominance flags, mechanism attribution and final classification.

9. **Critic independence.** Critic recomputes root/case identities, treatment predicates, fixed-channel drift semantics, mechanism flags and final classifier from root/assembly payloads rather than trusting aggregate classification. Its semantic positive control intentionally changes only a fixed-channel witness `S_lower` and requires competition attribution to remain unaffected.

10. **Workflow wiring.** The repaired run executes exactly Python 3.11/3.13 x roots 13/14/15, captures environment before science, assembles each environment independently, then requires aggregate/Critic classification agreement and a non-INVALID Critic result for workflow success.

## Audit conclusion

No additional source-level mismatch with the frozen Iter504S scientific contract was identified in this outcome-blind audit. Therefore no running-code modification is authorized or needed on the basis of this audit.

This is a methodology/source audit only. It is not an Iter504S scientific result and makes no mechanism claim.

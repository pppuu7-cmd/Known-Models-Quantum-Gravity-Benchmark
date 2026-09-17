# Iter504S exact-decision final source-diff audit

Date: 2026-09-17
Status: COMPLETED BEFORE ANY EXACT-DECISION SCIENTIFIC EXECUTION

Scientific preregistration remains:

`f6367456aa715fe6282ab70c1b2005971a4568c7`

Exact-threshold execution-only firewall remains:

`77d42eb58c03eef2356aed7a25795562760de4e3`

This audit is outcome-blind with respect to the exact-decision scientific execution. The earlier float-transport run `35175533159` is treated only as diagnostic/regression evidence; its provisional mechanism class is not used to select, alter, or tune the exact-decision implementation.

## Compared chains

First repaired float-transport chain:

- evaluator `b20077e77b421a68f1a99135ff652e52a0d53227`;
- assembler `7dc689f9b4d7e4f768a677e2afc80668a15b73d9`;
- aggregate `b0347e225b986b63e079ef6ebf02cd928022eb39`;
- adversarial Critic `38c705865b0397c7cf664ad142ad232d3b0a312f`.

Final exact-decision chain:

- evaluator `d6fab0d6a42e79e0d9843c08c453cc0e283cc190`;
- assembler verification hardening `2acf07c0ac5b27e55c90f88a9ffc3af05264cf23`;
- aggregate `d8fac6d451f266df238bd6814eea7ec29fa27dc7`;
- adversarial Critic verification hardening `ecd40392d16f2c936d3d0ff9655a3ff6d390e26d`;
- exact-decision methodology workflow `932866e4be11f0ced241f5e3a1a854bb74dfb637`;
- exact-decision methodology run `35178027196`, completed/success.

## Scientific source invariance

The exact evaluator retains the same frozen scientific construction:

- `python-flint==0.9.0` requirement for production execution;
- Arb/Acb precision 384 bits;
- causal `0to5`, block `0`, path `2`, direction `[1,1,1,-1,-1,-1]`, sign `+1`;
- roots `13,14,15`;
- exact LOW/MID/HIGH rational amplitudes;
- rhos `[0.35,0.9,1.6,2.7]`;
- R grid `[6,8,10,12]`;
- all 243 channels with no pruning;
- the same Iter504R root model and derivative construction;
- the same full-D and derivative-center treatments;
- the same late/early slope formulas;
- exact drift threshold `1/20`;
- exact slope floor `+1`;
- the same four non-INVALID terminal mechanism classes and the same classifier precedence.

No KAK, Toller, intertwiner, contraction, channel-envelope, amplitude, rho, R, root, precision, threshold, floor, or classifier-science parameter was changed by the exact-decision repair.

## Exact-decision-only differences

The evaluator now decides scientifically active inequalities while the values are still Arb objects:

- `slope_floor_satisfied := bool(slo >= arb('1.0'))`;
- `drift_within_tolerance := bool(du <= arb('0.05'))`;
- `within_tolerance := slope_floor_satisfied AND drift_within_tolerance`.

For fixed channels, each candidate's `drift_within_tolerance` is decided from its Arb `du` before serialization. The evaluator serializes deterministic `violating_channel_indices`; fixed-channel all-within is derived from candidate completeness, nonempty candidate set, and those exact producer decisions.

`S_lower`, `drift_upper`, and `max_fixed_channel_drift_upper` remain diagnostic/display metadata. A display-only maximum may still be chosen from serialized values for reporting a witness, but no scientific predicate or terminal class depends on that maximum.

## Consumer firewall

The assembler performs no scientific threshold comparison on binary64 summaries. It validates the producer exact booleans, exact rational identities, cohort structure, possible-max identities, candidate/violating identities, dominance booleans, provenance, and recomputes mechanism flags and the terminal classifier from exact booleans only.

The aggregate compares exact discrete scientific projections across the independent environments. It does not reevaluate threshold inequalities from numeric summaries.

The independent Critic separately reconstructs structural validity, mechanism flags, cross-environment exact-decision projection, and final classification without using serialized `S_lower`, `drift_upper`, or `max_fixed_channel_drift_upper` as threshold authority.

## Adversarial verification

The final Critic and methodology CI explicitly cover all mandatory prelaunch negative controls:

1. threshold comparison after Arb-to-float conversion;
2. floor comparison from serialized float;
3. fixed-channel maximum used as threshold authority;
4. missing exact decision boolean;
5. inconsistent all-within versus violating-channel list;
6. omitted channel;
7. candidate-set incompleteness mislabeled complete;
8. channel pruning;
9. changed threshold;
10. changed floor;
11. changed root/rho/R cohort;
12. changed exact LOW/MID/HIGH amplitude;
13. center-D treated as rigorous enclosure;
14. result-dependent case deletion.

Additional controls cover derivative representation, path/sign, repair provenance and cross-environment disagreement.

The methodology workflow executes a synthetic adversarial self-test rather than merely searching source text. Run `35178027196` completed successfully with syntax, static exact-decision contract, mandatory-control presence, synthetic rejection tests, and frozen-science constants all passing.

## Audit conclusion

The exact-decision chain is an EXECUTION-ONLY rigor repair.

- Science changed: **false**.
- Threshold changed: **false**.
- Cohort changed: **false**.
- Classifier changed: **false**.
- Source physics changed: **false**.
- Decision transport / verification changed: **true**.

The chain is eligible for one prospectively frozen exact-decision scientific execution after the repository's required general methodology/provenance checks on the frozen source head are terminal success and after a separate single-execution authority freezes the exact code/workflow identities.

This audit makes no Iter504S mechanism claim.

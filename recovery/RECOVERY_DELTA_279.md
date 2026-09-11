# Recovery Delta 279 — NSF reduction and claim-boundary audit

Date: 2026-09-11

## What changed

The 2025–2026 Null Surface Formulation quantum/scattering line was audited under the frozen new-parent rule rather than automatically promoted into the Tier-1 census.

Primary classification evidence identifies NSF as a formulation/quantization of General Relativity, and the 2026 Part-III tree construction reproduces the standard Weinberg–DeWitt amplitude.

## Parallel compute

Workflow `nsf-tree-claim-boundary-audit`, run `34553257781`:
- normalization;
- t/u symmetry;
- fixed-angle high-energy scaling;
- forward/collinear scaling;
- 4/4 independent jobs success; aggregate success.

Methodology CI run `34553257768`: preflight + 4/4 methodology shards + aggregate/bundle success.

Aggregate digest: `sha256:f39af3a4ba9c0da0ddf54c53ca5099b3193611cf141f059a380f652e7f2f1a8c`.

## Result

`REDUCED_TO_EXISTING_GR_PARENT__NEW_REALIZATION_NOT_NEW_TIER1_PARENT`

No 16th Tier-1 row is created.

Claim-boundary result:
- normalization error = 0;
- t/u symmetry error = 0;
- fixed-angle amplitude exponent = 1 to floating precision;
- forward/collinear epsilon exponent ≈ -0.9794 on the finite test grid.

Thus UV-finite perturbative/integration behavior must not be rewritten as bounded high-energy amplitude or forward-limit regularity.

## Global state

- Tier-1 = 15.
- strict terminal = 1/15.
- candidate terminal = 0/14.
- D7 = NOT_CLOSED / NOT_YET_AUTHORIZED.
- Candidate Gravity remains inactive at R3 = 24%.

## Publication handoff

- Paper III: `NOT_NEEDED` as a new rule; optional corroboration only.
- Paper IV: `READY`; add the NSF reduction-map/claim-boundary case.

Detailed audit:
`paper_iv/P_NSF_REDUCTION_AND_CLAIM_BOUNDARY_AUDIT_ITER279_2026-09-11.md`

Decision delta:
`paper_iv/PAPER_IV_DECISION_LEDGER_DELTA_279.json`

# Null Surface Formulation reduction and claim-boundary audit — Iter279

Date: 2026-09-11
Candidate object: Null Surface Formulation (NSF) quantum-gravity/scattering line
RQIR Core: `v1.0 FROZEN`

## Question

Does the 2025–2026 NSF quantum/scattering line constitute a new independent Tier-1 quantum-gravity parent, or is it a new realization/formulation of General Relativity that should be reduced to the existing GR benchmark parent? What do the published tree-amplitude claims actually imply about ultraviolet and forward behavior?

## Authority chain

The reduction evidence is unusually explicit:

- the historical literature names NSF as a **Null Surface Formulation of General Relativity**;
- the 2023 nonlinear-scattering paper states that it solves the Einstein equations in NSF;
- the 2025 *Physical Review D* paper constructs a quantum theory of asymptotically flat spacetimes using solutions of the NSF field equations and derives the spacetime metric as a quantum operator;
- the 2026 scattering trilogy develops quantum graviton scattering at null infinity and Part III states that the completed tree contribution reproduces the Weinberg–DeWitt tree amplitude.

Primary 2026 objects used in the bounded numerical audit:

- arXiv:`2605.06961` — Part I / definite-helicity NSF scattering;
- arXiv:`2605.19764` — Part II / third-order exchange channels;
- arXiv:`2605.24512` — Part III / fourth-order Bondi shear and complete tree amplitude.

Part III gives the complete quoted tree formula

`M_tree = -kappa^2 s^3 / (4 t u)`

with the standard gravitational normalization `kappa^2 = 32 pi G`.

## Parallel computational audit

Workflow: `nsf-tree-claim-boundary-audit`
Run: `34553257781`
Head: `7bebcbc81aeae418da180d1fb08be1649a3dd525`

Four independent jobs were executed in parallel and aggregated only after the dependency barrier:

1. normalization consistency;
2. `t <-> u` symmetry of the quoted complete tree formula;
3. fixed-angle high-energy scaling;
4. forward/collinear `t -> 0` scaling.

Result: **4/4 independent jobs SUCCESS + aggregate SUCCESS**.
Aggregate artifact digest: `sha256:f39af3a4ba9c0da0ddf54c53ca5099b3193611cf141f059a380f652e7f2f1a8c`.

The same head passed methodology CI run `34553257768`: preflight + 4/4 methodology shards + aggregate/bundle all `SUCCESS`.

## Numerical result

- Normalization identity between the `kappa` and `G` forms: maximum relative error `0.0` on the test set.
- `t <-> u` exchange of the complete quoted tree formula: maximum relative error `0.0` on the test set.
- Fixed-angle scaling for three independent angle fractions: fitted log-log exponent `1.0000000000000002`, `1.0`, `1.0000000000000002`.
- Forward/collinear scan: fitted log-log exponent with respect to the finite `epsilon = |t|/s` grid is `-0.9793860345408437`, consistent with the expected pole-like `~1/epsilon` approach.

Thus the quoted tree amplitude grows linearly with `s` at fixed scattering angle and retains a forward/collinear pole.

## Claim boundary

This does **not** contradict the NSF authors' ultraviolet-finiteness claim. It clarifies its domain: UV finiteness of the perturbative construction/integrals and absence of the usual UV renormalization divergence is not the same assertion as a bounded fixed-angle tree amplitude, and it is not an infrared/forward-limit regularity statement.

Likewise, reproducing the standard tree amplitude is strong positive evidence for a reduction/equivalence map in that sector, but it does not by itself establish all-order quantum equivalence to every representation of GR or independently validate the authors' all-loop finiteness argument.

## Tier-1 classification

The frozen new-parent rule requires promotion only when a concrete independent parent cannot be reduced/equated to an existing Tier-1 parent by an explicit valid map.

For NSF, the present authority chain points in the opposite direction: the field equations are a formulation of GR and the perturbative quantum scattering construction explicitly reproduces a standard GR tree amplitude.

Therefore the correct current classification is:

`REDUCED_TO_EXISTING_GR_PARENT__NEW_REALIZATION_NOT_NEW_TIER1_PARENT`

No Tier-1 census increase is authorized.

This is **not** a rejection of NSF and **not** a statement that its UV-finiteness claim is false. It is a taxonomy/provenance decision under the KMQGB coverage contract.

## Global consequence

- Tier-1 remains `15`.
- strict terminal remains `1/15`.
- candidate-family terminal remains `0/14`.
- D7 remains `NOT_CLOSED / NOT_YET_AUTHORIZED`.
- Candidate Gravity remains inactive at R3 `24%`.

NSF does not independently terminalize the GR/QG question because the current explicit complete observable is perturbative/asymptotically-flat scattering and the stronger all-loop/full-domain claims are not accompanied here by a same-scope complete independently reproduced observable package.

## Methodological consequence

The audit independently illustrates `MULTI_AXIS_RESOURCE_CLOSURE` and **claim-domain separation**: UV loop finiteness, high-energy amplitude boundedness, forward regularity, and all-order equivalence are different statements and must not be substituted for one another.

No new frozen RQIR rule is needed beyond the Iter277 strengthening; the distinction should be preserved as a Paper-IV example and, at most, as optional corroborating language in Paper III.

## Publication handoff

- Paper III: `NOT_NEEDED` as a new rule. Optional corroboration only for the already-planned multi-axis/claim-domain wording.
- Paper IV: `READY`. Add NSF as a reduction-map case showing why a new-looking quantum-gravity formulation should not automatically create a new Tier-1 family; include the numerical claim-boundary check.

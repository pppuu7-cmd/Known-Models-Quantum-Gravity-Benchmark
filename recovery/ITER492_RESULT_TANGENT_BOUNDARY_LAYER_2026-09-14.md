# Iter492 Result — Tangent Boundary Layer

Date: 2026-09-14

## Authoritative provenance
- Preregistration: `6288e7543f52f714e0887e4cf120f2dd19c4fc7d`
- Evaluator: `35b2a7c44b4c3bc9b6742513ef9fa375d189e2e1`
- Aggregate implementation: `94730270d8b2b900aff270de9e9f0812c902db91`
- Production/workflow head: `65e01fc8bf3b3e090da000501802d27a8d4aaca8`
- Run: `34794279921`
- Source-lock job: `103824262832`
- Aggregate job: `103824804978`
- Aggregate artifact: `10328863006`
- Aggregate digest: `sha256:1821129dbbad0b8f9e4f435235b4d4f2695dbc7326cf899d40b196a989e197c8`

## Terminal classification
`ITER492_TANGENT_BOUNDARY_LAYER_BRACKET_QUALIFIED_SCOPED`

All 15 matrix jobs and all 15 raw artifacts were independently consumed. There are no missing or invalid jobs. All frozen numerical/source controls pass. Aggregate HP KAK reconstruction max is `8.305484669684266e-98`; source-object identity relative max is `3.0356725926950808e-15`.

## Frozen q bracket
For `eps_q(R)=0.02 exp(-q R)` on the prospectively frozen 8 tangent directions, both signs, three causal classes, four rho witnesses and finite R grid:

- `q=0.50`: FULL_NONDECAY = false; 21/24 lanes fail.
- `q=0.75`: FULL_NONDECAY = false; 21/24 lanes fail.
- `q=1.00`: FULL_NONDECAY = true; 24/24 lanes pass and are robust.
- `q=1.25`: FULL_NONDECAY = true; 24/24 lanes pass and are robust.
- `q=1.50`: FULL_NONDECAY = true; 24/24 lanes pass and are robust.

The smallest prospectively frozen full-NONDECAY q is therefore exactly `1.00` on this finite matrix.

## Scientific interpretation
Iter492 materially narrows the angular-Haar blocker: the Iter487/489 center NONDECAY ray is not merely an isolated numerical point under all shrinking perturbations; on the frozen finite tangent matrix it survives perturbations whose radius shrinks at least as fast as `exp(-R)` (with prefactor 0.02), while slower frozen shrinkages `exp(-0.5R)` and `exp(-0.75R)` do not survive.

This is a finite directional/R boundary-layer bracket only. It does **not** establish a fixed open angular neighborhood, positive Haar measure, a Haar divergence theorem, D7-S2 closure, any terminal D7 label, or Candidate Gravity authorization. An analytic/uniform local-response certificate remains mandatory before any positive-measure claim.

## Locks
D7-S2 remains `NOT_CLOSED`; D7-S3 remains `NOT_CLOSED`; D7-S4 remains `PARTIAL_GLOBAL_NOT_CLOSED`. `EXISTING_SUFFICIENT`, `ADAPT_EXISTING`, `HYBRID_REQUIRED`, and `NEW_REQUIRED` remain forbidden. Candidate Gravity remains inactive.

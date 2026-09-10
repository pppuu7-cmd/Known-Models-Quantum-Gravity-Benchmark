# O-LQG EPRL/KKL UV fixed-point scope audit — 2026-09-10

## Frozen benchmark discipline

RQIR Core v1.0 remains FROZEN. This audit does not modify any benchmark criterion. Scoped structural progress is not promoted to family-level PASS. Missing same-realization objects remain BLOCKED rather than FAIL.

## New primary authority

Muxin Han, *Ultraviolet Fixed Point in Covariant Loop Quantum Gravity*, arXiv:2602.18665v1 (21 Feb 2026).

The construction is not merely generic spin-foam language: the stack amplitude uses the Lorentzian EPRL/KKL amplitude on each stacked 2-complex and retains the Barbero–Immirzi parameter through the EPRL simplicity representation, e.g. rho = gamma(k+2). The paper identifies a candidate UV fixed point of the complete covariant-LQG amplitude after summing over 2-complexes. At leading order the amplitude becomes triangulation independent and topological, with the infinite microscopic ambiguity compressed to a finite boundary-block coefficient set. The asymptotic statement carries a stated O(A^-1) remainder in the large-cutoff expansion.

## What this closes

Scoped result:

`PASS_STRUCTURAL_GATE__LQG_EPRL_KKL_COMPLETE_AMPLITUDE_HAS_CANDIDATE_UV_FIXED_POINT_WITH_FINITE_BOUNDARY_DATA_AND_EXPLICIT_LEADING_REMAINDER`

This closes a narrower objection that no concrete EPRL-family continuum/UV object with approximation control exists. It supplies:

- same-realization microscopic object: Lorentzian EPRL/KKL stack amplitudes;
- refinement/sum-over-complexes organization;
- candidate UV fixed-point behavior;
- finite renormalized boundary coefficients `{b_sigma}`;
- leading asymptotic remainder `O(A^-1)`.

## What it does not close

The same authority explicitly leaves the IR flow for future work: relevant deformations away from the topological UV point and the connection of boundary coefficients to physical observables are not derived. The UV regime is small-spin, while the semiclassical large-spin regime needed for Regge/Area-Regge matching is a different regime. No Regge or Area-Regge matching is supplied in the paper.

The Barbero–Immirzi parameter is present in the microscopic amplitude and in the Hessian analysis, but no beta_gamma or same-realization ancestry map is derived from microscopic gamma through the UV boundary coefficients and onward to semiclassical Area-Regge/area-metric parity-sensitive effective couplings.

Therefore the currently required chain remains incomplete:

`EPRL/KKL microscopic gamma -> UV fixed-point boundary data -> relevant deformation / IR crossover -> semiclassical Regge/Area-Regge couplings -> area-metric observable comparator`.

## RQIR disposition

Parent O-LQG remains:

`BLOCKED_MISSING_REQUIRED_OBJECT`

No family-level comparator residual is defined. The new evidence is a scoped structural PASS only and must not be promoted beyond its domain.

## Exact next gate

`EPRL_KKL_UV_FIXED_POINT_TO_SEMICLASSICAL_AREA_REGGE_CROSSOVER_PLUS_GAMMA_ANCESTRY_AND_ERROR_CERTIFICATE`

Required certificate fields:

1. one explicit EPRL/KKL realization continuously connecting the stack UV fixed point to an IR/semiclassical regime;
2. relevant-deformation/RG map from `{b_sigma}` or equivalent UV parameters to the IR gravitational sector;
3. explicit gamma normalization/transport, not name matching;
4. Regge -> Area-Regge/area-metric coupling ancestry in that realization;
5. common-domain normalized observable/comparator map;
6. propagated `O(A^-1)` plus crossover/truncation/refinement remainder.

## Compute decision

Heavy compute remains IDLE. The missing object is a same-realization UV-to-IR matching/provenance certificate. A numerical scan would add assumptions rather than close the frozen gate unless a concrete published or prospectively frozen flow equation is first supplied.

# KMQGB Eighteenth Wave — Minimal E1 Vertex-Seed Specification

**Frozen denominator:** 5 methodology/feasibility targets.  
**Historical waves 1–17:** terminal and immutable.  
**Purpose:** define the first admissible same-spin-2 E1 search skeleton without promoting a Candidate Gravity ansatz.

Canonical specification: `protocol/MINIMAL_E1_VERTEX_SEED_SPECIFICATION.md`.

Machine record v1.1: `eighteenth_wave/records/T18-E1-vertex-skeleton-v1_1.json`.

## Terminal matrix

1. **T18-01 — preserve the GR free spin-2 sector** — `PASS_RQIR_GATE`.
   - A regular cubic-curvature/Weyl deformation begins at `O(h^3)` around Minkowski.
   - The quadratic Einstein-Hilbert action, massless graviton pole and free residue are unchanged by the skeleton itself.
   - This is a gravity/consistency anchor, not novelty.

2. **T18-02 — low-energy C5 containment boundary** — `PASS_RQIR_GATE`.
   - For analytic `Phi_M`, the `E << M` expansion is a tower of local curvature/derivative EFT operators.
   - No finite Taylor/Wilson coefficient may be labelled `DeltaGamma_KG`.
   - Potential novelty, if any, must be an all-orders/cross-regime relation.

3. **T18-03 — on-shell nontrivial search locus** — `PASS_RQIR_GATE` as a search-location statement.
   - Published amplitude analyses distinguish EOM/Ricci-type form-factor classes, often tree-equivalent to Einstein gravity, from Riemann-sector form factors that can alter graviton amplitudes.
   - Therefore the skeleton is placed in a Weyl/Riemann higher-point sector rather than a propagator-only EOM-squared sector.
   - This does **not** authorize a nonzero residual for the specific skeleton.

4. **T18-04 — parent-fixed kernel + Lorentzian/CTP causality** — `BLOCKED_MISSING_REQUIRED_OBJECT`.
   - `Phi_M` has not been derived from a microscopic/parent principle.
   - Exact covariant operator ordering, reality/CTP completion, retarded/no-signalling/global-causality prescription and stability remain missing.
   - Choosing a convenient entire function by hand is forbidden by the rigidity rule.

5. **T18-05 — complete four-graviton cross-regime observable + same-domain quotient** — `BLOCKED_MISSING_REQUIRED_OBJECT`.
   - The first direct physical scattering target is a complete real four-graviton amplitude over several `E/M` and angle/helicity points.
   - At linear order in the new coupling it must include V3-derived quartic contact plus all EH-cubic × V3-cubic exchanges and Ward completion.
   - A same-domain nonlocal/UV comparator at `E~M`, covariance, Jacobian, COR and holdout prediction object are not yet frozen.

## Wave-18 rollup

- `PASS_RQIR_GATE`: 3;
- `BLOCKED_MISSING_REQUIRED_OBJECT`: 2;
- Candidate Gravity ansatz promoted: `false`;
- robust unique-QG residuals: `0`.

**Wave-18 terminal coverage: 5/5 = 100%.**

## Key design consequence

The first surviving architecture is not “nonlocal gravity” generically.  It is much narrower:

- unchanged GR two-point/free pole;
- first possible novelty in a higher-point Weyl/Riemann sector;
- low-energy EFT coefficients explicitly treated as C5;
- one parent-fixed low-parameter cross-regime kernel, not an arbitrary function;
- complete Ward/contact amplitude response;
- Lorentzian/CTP causality;
- same parameters predict multiple kinematic points/channels;
- same-domain nonlocal/UV comparator and global COR separation.

Until T18-04 and T18-05 objects exist, this remains a **pre-ansatz search skeleton**.

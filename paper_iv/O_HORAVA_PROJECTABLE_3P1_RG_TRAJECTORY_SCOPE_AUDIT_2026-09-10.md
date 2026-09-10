# O-HORAVA — projectable 3+1 RG trajectory scope audit

Date: 2026-09-10
Iteration: 191
RQIR Core: v1.0 FROZEN

## Target

Evaluate whether the projectable Hořava branch still lacks any UV->IR trajectory authority, after the Iter190 projectability fork was frozen.

## Primary authorities

### Full one-loop marginal beta functions

Barvinsky, Kurov & Sibiryakov, *Beta functions of (3+1)-dimensional projectable Horava gravity*, arXiv:2110.14688.

The paper derives the full beta functions for the marginal essential couplings of projectable Hořava gravity in 3+1 dimensions and identifies candidate asymptotically free fixed points. Gauge-independent essential beta functions are checked in four gauges and by an independent special-background calculation.

### Numerical RG trajectories

Barvinsky, Kurov & Sibiryakov, *Renormalization group flow of projectable Hořava gravity in (3+1) dimensions*, arXiv:2411.13574.

The paper classifies the fixed points and numerically follows trajectories from asymptotically free points. It reports a unique fixed point whose trajectories span the unitarity-compatible range of the kinetic coupling lambda, including the phenomenologically important region `0 < lambda - 1 << 1`, with a near-universal trajectory for the marginal couplings apart from the gravitational coupling.

## RQIR scope result

The statement "projectable Hořava lacks a 3+1 UV RG trajectory" is no longer admissible.

Scoped classification:

`PASS_RQIR_GATE__HORAVA_PROJECTABLE_3P1_ASYMPTOTICALLY_FREE_MARGINAL_RG_TRAJECTORY_AUTHORITY`

This closes only the UV/marginal-trajectory sub-obligation.

## Why this is not yet a complete projectable branch certificate

The frozen H1 gate requires a single same-realization object connecting the UV theory to a normalized IR observable and GR/EFT comparator with controlled remainder. The 2021/2024 RG results do not by themselves supply all of the following in one certificate:

1. running/matching of the relevant lower-derivative couplings that dominate the deep IR;
2. a quantitative crossover from the z=3 marginal regime to the low-energy scalar-graviton action;
3. propagation of the RG trajectory into a normalized scalar observable (dispersion, cosmological perturbation amplitude/transfer function, PPN-like observable, or another detector-facing quantity);
4. an error/remainder ledger covering truncation, loop order and the UV-to-IR matching region;
5. a same-domain GR/EFT comparator evaluated on the same trajectory.

Accordingly, the family-level status remains `PARTIAL_SUBFAMILY_ONLY` and the projectable branch remains nonterminal.

## Updated projectable gate

The old H1 gate is narrowed from "find a UV trajectory plus observable" to:

`HORAVA_PROJECTABLE_AF_RG_TO_IR_RELEVANT_COUPLING_CROSSOVER_PLUS_EXTRA_SCALAR_OBSERVABLE_MATCHING_CERTIFICATE`

Required object:

`{AF fixed point, marginal trajectory, matching scale, relevant-coupling matching, lambda_IR, scalar kinetic/gradient normalization, observable, error/remainder, GR/EFT comparator}`.

The AF fixed point and marginal trajectory fields now have primary-source authority. The remaining missing object is the controlled crossover/matching into the IR observable sector.

## Negative control

A numerical scan over phenomenological IR lambda values is not equivalent to transporting one UV RG trajectory into that IR point. Such a scan must not be used as a same-realization certificate.

## Global effect

- No new family-level terminal row.
- D2/D4/D7 unchanged.
- `NEW_REQUIRED` remains unauthorized.
- Candidate Gravity remains inactive at R3=24%.
- Heavy compute remains IDLE pending a frozen crossover/matching object.

# Higher-derivative QG DQFT/dual-IHO branch expansion audit — Iter259

Date: 2026-09-11
Family: `PERTURBATIVE_HIGHER_DERIVATIVE`
RQIR Core: `v1.0 FROZEN`

## Question
Is the Iter187 material quantization-branch taxonomy still complete through 2026-09-11, or has a materially distinct quadratic-gravity realization appeared that must be benchmarked separately before family-level disposition?

## Prior branch map
Iter187 separated at least: conventional bare/indefinite-metric ghost interpretation; fakeon/purely-virtual prescription; Lee-Wick/unstable-resonance interpretation; PT-symmetric/modified-inner-product constructions; Euclidean reflection-positive lattice construction.

## New 2026 authority
1. K. Sravan Kumar & João Marto, *Quantum (quadratic) gravity: replacing the massive tensor ghost with an inverted harmonic oscillator-like instability*, arXiv:2603.07150 (2026).
2. K. Sravan Kumar & João Marto, *Unitary Quadratic Quantum Gravity in 4D*, arXiv:2604.19707v3 (2026).

The first authority reinterprets the extra spin-2 sector for a specified sign choice as an inverted-harmonic-oscillator / dual-IHO-like instability and quantizes it in a direct-sum quantum-field-theory framework with geometric superselection sectors. The second sharpens the claim for quadratic gravity with positive Weyl-squared coefficient: the extra pole is spacelike, the Källén-Lehmann spectral density is argued to vanish, the propagator is fixed to principal-value form, the extra spin-2 is excluded from asymptotic states/absorptive cuts, and Landau/Cutkosky analyses are used to argue compatibility of unitarity and renormalizability.

## Material distinctness
The 2026 authority itself distinguishes this construction from fakeon, Lee-Wick and PT-symmetric routes. The distinguishing data are not merely notation:
- sign/kinematic placement of the extra spin-2 pole (spacelike dual-IHO sector rather than a timelike ghost virtualized by prescription);
- direct-sum/geometric-superselection quantization ancestry;
- principal-value propagator claimed to follow from spectral support rather than average continuation or contour prescription;
- absence of physical KL spectral weight/cut support for the extra spin-2;
- a distinct loop/UV argument based on spacelike Landau structure and the full local four-derivative propagator.

Therefore Iter187 B1-B5 is no longer exhaustive through 2026-09-11.

## New material branch
Add:
`B6 = DQFT_DUAL_IHO_SPACELIKE_PURELY_VIRTUAL_BRANCH`

Scoped status:
`SCOPED_CANDIDATE_UNITARITY_RENORMALIZABILITY_CONTROL__INDEPENDENT_TERMINAL_CAUSALITY_OBSERVABLE_AND_ERROR_CERTIFICATE_OPEN`

This status records what the cited preprints claim without promoting the claim to a family-level PASS.

## Why this does not close the family
A terminal KMQGB object still requires, for the same fixed action/parameter/sign domain:
1. exact realization vector and pole/spectral support;
2. physical Hilbert/asymptotic-state rule;
3. optical-theorem/cut certificate;
4. declared causality notion or controlled replacement and its domain;
5. normalized physical observable produced by that same realization;
6. IR/GR map and identical-domain comparator;
7. propagated loop/truncation/scheme/remainder errors;
8. disposition/reduction map relative to other materially distinct quantization branches;
9. preferably independent authority or reproducible external validation before treating a novel 2026 preprint claim as terminal family evidence.

The 2026 DQFT/dual-IHO work materially strengthens items 1-3 and provides phenomenological targets, but the full KMQGB package is not yet closed.

## Governance consequence
`PERTURBATIVE_HIGHER_DERIVATIVE` remains `PARTIAL_SUBFAMILY_ONLY`.
The new branch increases the correctness of the census but does not provide family exclusion evidence and does not authorize `NEW_REQUIRED`.
D2 remains `NOT_CLOSED`; D4 remains `PARTIAL_GLOBAL_NOT_CLOSED`; D7 remains `NOT_CLOSED / NOT_YET_AUTHORIZED`.
Candidate Gravity R3 remains 24%. Heavy compute remains `IDLE`.

## Polygon saturation
Operational polygon saturation is held at approximately 94% rather than increased: a previously missing material branch was discovered, so the census improved but a new finite branch-specific closure task was added. Progress is therefore methodological/coverage progress, not net saturation progress.

## Next gate
`DQFT_DUAL_IHO_SAME_REALIZATION_CAUSALITY_OBSERVABLE_COMPARATOR_AND_ERROR_CERTIFICATE`

The next iteration should determine whether B6 can be parked as a bounded missing-object branch or whether its own papers already contain enough same-realization observable/causality structure for a stronger scoped disposition.

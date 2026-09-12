# KMQGB recovery delta — Iter443 one-leg radial integrability gate

Date: 2026-09-12

## Why this gate exists

Iter304 correctly established that polynomial boundedness of a Toller branch is not by itself enough to infer noncompact Haar integrability. The causal-vertex literature still leaves full causal-vertex finiteness as an open problem: the causal EPRL paper explicitly says finiteness must be investigated again for the causal model because Toller poles could in principle introduce new divergences.

At the same time, Iter438-440 and the currently running Iter442 have substantially tightened the local/source Toller layer. The next useful calculation is therefore not another generic polynomial-boundedness witness, but a source-faithful noncompact radial test.

## Iter443 preregistration and run

Research branch: `research/iter443-one-leg-radial-integrability`
Workflow run: `34716909118`
Frozen contract: `benchmarks/lqg_iter443_one_leg_radial_integrability_contract.json`
Implementation: `code/lqg_iter443_radial_gate.py`

Frozen source matrix:
- gamma: `{7,8}`
- j: `{2,5}`
- all integer m in `[-j,j]`
- both Toller branches
- beta: `{4,6,8,10,12,14}`
- precision: `100 dps`

For one noncompact group variable of the 4-simplex vertex, four incident wedges depend on that variable. The diagnostic constructs the conservative fixed-j source envelope

`M_j(beta) = max_{m, branch} |t_branch(j,m; rho=gamma*j, beta)|`

and tests the radial quantity

`sinh(beta)^2 * M_j(beta)^4`.

The local preregistration sanity calculation found an asymptotic log slope near `-2.00000003` for every frozen `(gamma,j)` channel. The frozen workflow does not use that value as a fitted per-channel threshold; it requires only:
- all source values finite;
- strict radial-envelope decrease;
- late-window fitted log slope `<= -1.8`;
- `M_j(beta)*exp(beta)` relative variation `<= 1e-4` on beta `>=8`.

## Scope guard

A PASS means only `SOURCE_ONE_LEG_RADIAL_ENVELOPE_INTEGRABLE_ON_FROZEN_GRID`.

It must **not** be promoted to:
- simultaneous multi-group noncompact integrability;
- full Haar/angular causal-vertex finiteness;
- generalized EPRL-KKL causal-vertex finiteness or normalization;
- causal-stack cutoff removal;
- D7-S3/S4 closure;
- terminal D7 authorization;
- Candidate Gravity activation.

Frozen post-PASS state remains `D7-S2 = STRENGTHENED_BUT_NOT_CLOSED`.

## Current frontier

Iter441 gap graph remains authoritative for the unresolved S3/S4 targets:
- same-realization parameter / observable / error transport;
- normalized comparator/error certificate;
- finite and normalized physical causal-stack realization;
- lambda_f weighted face-multiplicity transport;
- universal common-domain inclusion;
- causal-stack cutoff removal.

Existing UV-IR guards explicitly show that a published map from the 2017 lambda/delta/mu hierarchy to the causal stack cutoff / UV coordinates is missing, and that a normalized operational observable/comparator bridge is also missing. These are source/definition blockers, not numerical knobs to be silently identified.

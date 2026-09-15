# SOURCE_J1_K5_FOREST_SUBTRACTION_P1 — prospective freeze

Date: 2026-09-15
Parent authoritative head: 36bc03c6886c761ada6257f3ce799584fbb6664c

## Scope
Auxiliary scalar Gaussian K5 witness only. No transfer to Eq.(4), fixed channel 00000, EPRL physical amplitude, terminal D7 classifier, or Candidate Gravity.

## Frozen upstream premises
Use only the Critic-surviving P1 auxiliary Gaussian witness and the exact K5 laminar-forest certificate: connected subsets |S|=2..5; subtraction orders r(S)=0,3,9,18; exhaustive laminar forests (expected upstream census 472, to be independently revalidated by implementation rather than hard-coded as a verdict).

## Question
After applying a genuine nested forest subtraction over all proper connected collision subsets to the same P1 auxiliary Gaussian realization, does the previously surviving P1 growth remain, become bounded/convergent, or remain computationally unresolved?

## Required implementation properties
1. Reconstruct connected subsets and laminar forests algorithmically; do not encode a terminal answer or a table of forest contributions.
2. Implement forest subtraction with inclusion/exclusion/nesting determined from the reconstructed forest poset. Full-collision subtraction must be kept distinct from proper-stratum subtraction.
3. Evaluate at least four successive P1 scale points at high precision; include an independent higher-precision replay.
4. Matrix workflow with fail-fast:false and independent branches (minimum: two Python/precision configurations).
5. Positive control: an intentionally unsubtracted P1 calculation must reproduce the known growing behavior qualitatively.
6. Adversarial control: perturb one frozen subtraction order or omit a required proper stratum; the certificate must detect a changed result/census.
7. Numerical cancellation audit: report absolute terms, residual, working precision, and lost digits; any conclusion dominated by cancellation is COMPUTATION_BLOCKED, not a scientific result.
8. No hard-coded terminal booleans/classifiers based on expected output.

## Frozen outcomes
- FOREST_SUBTRACTED_P1_DIVERGENCE_SURVIVES_SCOPED: stable high-precision evidence of unbounded/growing residual after complete proper-stratum forest subtraction, with controls passing.
- FOREST_SUBTRACTED_P1_STABILIZES_SCOPED: stable high-precision evidence that the residual is bounded/convergent over the preregistered diagnostic and controls pass. This is not a proof of Eq.(4) existence.
- FOREST_SUBTRACTION_COMPUTATION_BLOCKED: precision/cancellation/resource limitations prevent discrimination.
- INVALID_IMPLEMENTATION: any frozen-contract/control/provenance failure.

## Guard
No EXISTING_SUFFICIENT / ADAPT_EXISTING / HYBRID_REQUIRED / NEW_REQUIRED decision is authorized by this gate. Candidate Gravity remains inactive.

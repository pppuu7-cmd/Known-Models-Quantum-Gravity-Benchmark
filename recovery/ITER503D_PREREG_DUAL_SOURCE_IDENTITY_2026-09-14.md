# Iter503D — prospective dual-source identity verifier

**Frozen before Iter503 is terminal.** This is an outcome-blind implementation audit of the derivative path used by Iter503. It does not change the Iter503 gate and carries no DECAY/NONDECAY or D7 conclusion.

## Trigger
The Iter503 AD implementation checks the exact source identity `T^(+) + T^(-) = D` at the interval-value level, but its `source_additive` flag does not separately require the dual derivative residual to contain zero. Because Iter503's scientific purpose depends on derivative enclosures, verify that identity directly in the derivative component before any green Iter503 result is promoted.

## Frozen object
Using Iter503 implementation head `d598f8c20fb6611fefa426bced6c0d4be8260baf`, frozen direction `[1,1,1,-1,-1,-1]`, sign `+1`, amplitude parent boxes `{0,7,15}`, `R={6,8,10,12}`, all ten K5 edges, `rho={0.35,0.9,1.6,2.7}`, and `m={-1,0,1}`:

1. construct the single-common-amplitude dual state;
2. for each edge KAK rapidity `beta(a)`, evaluate the exact Iter503 dual source coefficients `D_m`, `T+_m`, `T-_m`;
3. require both
   - value residual `T+ + T- - D` contains complex zero;
   - derivative residual `d/da(T+ + T- - D)` contains complex zero;
4. require all coefficient and derivative balls finite and all inherited dual-state/KAK construction controls valid.

Frozen count: `3 boxes × 4 R × 10 edges × 4 rho × 3 m = 1440` value identities and 1440 derivative identities.

## Verdicts
- `ITER503D_DUAL_SOURCE_IDENTITY_CONFIRMED`: all 1440 value and all 1440 derivative identities contain zero and all controls are valid.
- `ITER503D_DUAL_SOURCE_IDENTITY_VIOLATION`: object identity is valid but any derivative/value identity excludes zero.
- `ITER503D_INVALID_OR_BLOCKED`: source/KAK construction or verifier implementation cannot be validated.

## Promotion rule
A derivative-identity violation forbids promotion of a green Iter503 result until repaired under a new prospective gate. Confirmation is an independent implementation control only; it does not by itself make Iter503 pass.

## Scope ceiling
No scientific slope classification, no Haar or spectral-integral theorem, no multidimensional-neighborhood result, no D7 closure, no selector label, no Candidate Gravity activation.

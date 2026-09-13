# Iter454 — Toller Feynman projector/kernel qualification

Date: 2026-09-13
Status: TERMINAL FROZEN AGGREGATE = `SCIENTIFIC_FAIL_ITER454_TOLLER_FEYNMAN_PROJECTOR_KERNEL`, with causal audit identifying a preregistered predicate-specification defect rather than evidence against the source kernel.

## Authoritative provenance
- Preregistration: `41281ef2ad95731126465a5089ac0d93e39e56ee`
- Implementation: `47a9ffa12cc924d5567affab5820367245392abb`
- Production head/workflow: `3968d374f4d291c339e52437cee5eccccf3bd524`
- Run: `34736575423`
- Aggregate job: `103669126159`
- Summary artifact: `10311670155`
- Summary digest: `sha256:9c811e7a4abd1398ecb775ba6d8e7a144b745bd4211b4ef7507631fbb50dd339`

All four raw lane artifacts were consumed. All lanes executed validly; frozen aggregate reported 4 valid / 0 pass.

## Frozen-predicate outcome
Across L0–L3:
- `P_jl(rho;rho)=1`: PASS, zero reported error.
- source pole enumeration: PASS.
- local reciprocal-Gamma cancellation predicate: FAIL in all four lanes.
- regulated Sokhotski–Plemelj convergence: PASS in all four lanes.
- wrong-branch negative control: PASS in all four lanes.

The only failing predicate was test 3.

## First causal failure
The frozen test approached each Gamma pole with a fixed real displacement `delta=1e-30` and required
`abs(1/Gamma(-j-i*tilde_rho)) <= 1e-50`.

At a source pole the reciprocal Gamma function has a *simple zero*. If `z=-m+epsilon`, `m` a nonnegative integer,

`1/Gamma(z) = (-1)^m m! epsilon + O(epsilon^2)`.

For the implementation's `tilde_rho=-i*n+delta`, the Gamma argument is a negative integer plus an imaginary displacement of magnitude `delta`, so the expected magnitude is `m! * delta + O(delta^2)`, i.e. O(1e-30), not O(1e-50). The observed lane values were exactly of that form: `1e-30`, `2e-30`, `6e-30`, `2.4e-29`, matching factorial scaling rather than indicating a failure of pole cancellation.

Therefore the historical frozen aggregate classification is retained unchanged, but it is **not interpreted as a scientific refutation of the source Feynman projector/kernel**. The failed predicate was overconstrained by twenty orders relative to its own finite displacement and did not test the actual simple-zero law.

## Scientific interpretation
Iter454 does not qualify the scalar projector layer because its frozen gate failed. However, four independent pieces of evidence survived unchanged: exact diagonal normalization, pole enumeration, regulated branch-difference convergence, and wrong-branch rejection. The next admissible step is a separately preregistered replacement gate that tests the reciprocal-Gamma zero through its mathematically correct first-order scaling coefficient without changing the historical Iter454 record.

No D7-S2 closure, full reduced Toller t-matrix qualification, Eq.(7) magnetic reconstruction, vertex convergence, regulator removal, terminal D7 classifier, or Candidate Gravity activation follows from Iter454.

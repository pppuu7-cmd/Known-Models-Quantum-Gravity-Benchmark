# Iter434 result + Iter435 preregistration

Date: 2026-09-12

## Iter434 terminal scientific result

Frozen gate: `recovery/ITER434_PREREG_MULTI_GROUP_ESCAPE_2026-09-12.md`.

Original production run `34700795644` on head `610d38d95298d6baf0dc57a68b97dfc50f19d106` produced a mixed result because the numerical-validity predicate incorrectly required the fitted log-slopes themselves to be positive. This is incompatible with the prospectively required negative decay slopes. The first causal defect was therefore infrastructure/numerical-control logic, not a scientific result.

Minimal repair commit: `ef5cd29c6d3b8d0d205c6821e59c5929630ac4a3`. The repair changed only numerical finiteness validation: weighted positive amplitudes must remain finite and positive, while fitted slopes need only be finite. The frozen profile set, Toller formulas, analytic discriminator, beta points and tolerance `2e-4` were unchanged.

Authoritative repaired run: `34703928956`.
Aggregate job: `103580532255`.
Aggregate artifact: `10301506751` (`lqg-iter434-summary`).
Artifact digest: `sha256:9e5e8929ace0683f5a8be6fe7233effcd6a96c49907d55198ea34bb5647a7401`.
Raw summary SHA256: `914815933c5a8ebd3e0919f289027e93aa6cc10770c40e1c1b37749a586c1d05`.

All 24/24 profiles are numerically valid after the minimal repair. Worst final-tail slope error is `1.5175517093394235e-08`, far below the frozen `2e-4` tolerance. Eighteen profiles satisfy the strict negative exponential-envelope condition and six fail it. The failing profiles are the prospectively included `worst` family at cluster sizes `s=3` and `s=4` for all three gamma values; the maximum expected weighted tail slope is `+4.0`.

Scientific classification: `FAIL_MULTI_GROUP_EXPONENTIAL_ABSOLUTE_ENVELOPE`.

Scope lock: this is a failure of the tested correlated-collinear K5 absolute exponential convergence envelope only. It is not a physical causal-vertex divergence theorem. Angular/boundary cancellation, source-sector admissibility, magnetic/intertwiner admissibility, finite-beta collision/distributional structure, normalized causal vertex, complete-stack cutoff removal and same-realization UV-to-Regge/GR transport remain open.

Global locks remain unchanged: D2=`NOT_CLOSED_COVERAGE_AND_OBJECTS`; D4=`PARTIAL_GLOBAL_NOT_CLOSED`; D7-S2=`NOT_CLOSED`; D7-S3=`NOT_CLOSED`; D7-S4=`PARTIAL_GLOBAL_NOT_CLOSED`; D7=`NOT_CLOSED / NOT_YET_AUTHORIZED`. Terminal D7 and `EXISTING_SUFFICIENT` / `ADAPT_EXISTING` / `HYBRID_REQUIRED` / `NEW_REQUIRED` remain forbidden. Candidate Gravity remains inactive.

## Iter435 prospectively frozen gate — source-induced K5 causal-support survival audit

### Scientific question
Before spending compute on full angular/intertwiner contractions, does the Iter434 absolute-envelope obstruction survive the exact source-induced K5 causal-sign support already established in Iter301, or was it an artifact of using branch-sign patterns outside the source support?

### Frozen source support
Use exactly the Iter301 source map `kappa_ab = sigma_a sigma_b` on K5. Fix the global-flip redundancy with `sigma_0=+1` and enumerate all `2^4=16` assignments of `(sigma_1,...,sigma_4)`. Every resulting edge-sign pattern must satisfy positive sign product around every K5 triangle; the 16 patterns must be unique.

### Frozen escape geometry
For each source sector and each cluster size `s=1,2,3,4`, boost vertices `1..s` together and use the K5 crossing set of size `s*(5-s)`. Spins on crossing edges cycle deterministically through `{1/2,1,3/2,2}` in lexicographic edge order.

For every crossing edge use its source-induced branch sign `kappa_ab`. Evaluate two preregistered magnetic-label envelopes:

1. `slow-extremal`: choose `m=-j` for `+` and `m=+j` for `-`, so the published Toller branch exponent is `alpha=1` edgewise.
2. `fast-control`: choose the opposite extremal label, so `alpha=1+2j` edgewise.

This gate is deliberately only a sign-support/envelope compatibility audit. It does NOT assert that the simultaneous extremal magnetic labels survive a boundary-intertwiner contraction; that is a later hard gate.

### Frozen discriminator
For each profile compute `lambda = 2*s - sum_crossing alpha_e`. Strict `lambda < 0` is required for the tested absolute exponential envelope. `lambda >= 0` is a scoped envelope FAIL.

### Frozen controls
- exactly 16 unique source-induced K5 sign sectors;
- positive sign product on every K5 triangle for every sector;
- exact K5 cut count `s*(5-s)`;
- every `fast-control` profile must have `lambda < 0`.

Any failure of these structural controls is `CONTROL_INVALID`, not science.

### Aggregate interpretation
- `SOURCE_SUPPORT_REMOVES_MULTI_GROUP_ENVELOPE_OBSTRUCTION` only if every source-supported `slow-extremal` profile has `lambda<0`.
- `SOURCE_SUPPORT_DOES_NOT_REMOVE_MULTI_GROUP_ENVELOPE_OBSTRUCTION` if controls are valid and at least one source-supported `slow-extremal` profile has `lambda>=0`.
- This remains a sign-support-level result only. It cannot promote to physical vertex divergence, D7-S2 PASS/FAIL, or family-level classification.

No threshold, profile, source-support rule or interpretation may be changed after inspecting Iter435 results.

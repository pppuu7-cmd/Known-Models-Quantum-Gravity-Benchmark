# KMQGB Wave 31 — Spectral-Origin Completeness

**Frozen denominator:** 5 methodology targets.  
**Status:** terminal 5/5.  
**Purpose:** determine what must physically support a candidate-specific quartic/higher relation after full-C5 matching.

| # | Target | Terminal result |
|---|---|---|
| T31-01 | local gravitational dispersive UV-origin requirement | `PASS_SCOPED_DISPERSIVE_GATE` |
| T31-02 | gravity-loop/forward-singularity treatment | `PASS_RQIR_GATE_MANDATORY` |
| T31-03 | subtraction-constant caveat | `PASS_FAIL_CLOSED_SCOPE_RULE` |
| T31-04 | nonlocal/exponentially bounded escape branch | `PASS_D_NONLOCAL_SEPARATE_GATE` |
| T31-05 | no-new-spectral-support local identity | `PASS_SCOPED_NO_NEW_DISPERSIVE_SHIFT` |

## Result

For coefficient combinations covered by a valid gravitational dispersion/sum-rule construction, a candidate-specific shift beyond full matched C5 must be sourced by different high-energy spectral/Regge data. This may be new elementary states, composite/multiparticle continuum, modified spectral weights or other UV discontinuity support.

Gravity requires careful IR/forward treatment: naive forward positivity is not accepted because massless graviton exchange and loops affect the sum rules.

If a coefficient is an uncontrolled subtraction constant, its origin remains `BLOCKED`, not inferred.

A genuinely nonlocal/exponentially bounded candidate belongs to a separate `D-nonlocal` branch with modified dispersion relations and its own causality/nonlocality tax.

Authoritative protocol: `protocol/SPECTRAL_ORIGIN_COMPLETENESS.md`.

No KG ansatz is promoted.
# KMQGB Wave 20 — Quartic Helicity and Spectral-Moment Rigidity

**Frozen denominator:** 5 methodology targets.  
**Status:** terminal 5/5.  
**Purpose:** constrain the quartic-first search by four-graviton helicity structure, positivity/moment relations and the correct dispersion class.

| # | Target | Terminal result |
|---|---|---|
| T20-01 | 4D quartic helicity anchor `f2,g2` | `PASS_RQIR_GATE` |
| T20-02 | local positivity ratio `rho4=f2/g2` | `PASS_RQIR_GATE_SCOPED_D_LOCAL` |
| T20-03 | higher-order positive spectral moments / Hankel PSD | `PASS_RQIR_GATE_SCOPED_D_LOCAL` |
| T20-04 | low-rank/saturated moment structure as KG certificate | `OPERATIONALLY_DEGENERATE` |
| T20-05 | local-vs-nonlocal dispersion-class attribution | `PASS_RQIR_GATE_MANDATORY` |

## Core formulas

For quartic-first `C3=0` in 4D GREFT:

`f2=C4,1-C4,2`,

`g2=C4,1+C4,2`,

and in the scoped local/polynomial positivity class

`g2+f2>0`, `g2-f2>0`, hence

`rho4=f2/g2 in (-1,1)`.

The ratio is an IR consistency/anchor coordinate, not KG novelty.

At higher orders, parity-preserving helicity eigenchannels generate positive spectral moment sequences and positive-semidefinite Hankel matrices. This supplies cross-order constraints, but low-rank/extremal moment structure can also arise from ordinary simple spectral support and is not gravity-specific novelty.

For genuinely nonlocal/exponentially bounded amplitudes, standard local polynomial-bounded positivity/moment formulas are not automatically valid. The dispersion/growth class must be declared prospectively before applying bounds.

Authoritative protocol: `protocol/QUARTIC_HELICITY_MOMENT_RIGIDITY.md`.

No KG ansatz is promoted.
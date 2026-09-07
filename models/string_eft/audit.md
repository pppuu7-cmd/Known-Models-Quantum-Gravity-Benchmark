# Model Audit — type-II closed-string four-graviton / low-energy matching control

Benchmark ID: KMQGB-M09-STRING-EFT
Provisional concrete realization ID: TYPEII-T6-GRAV4-TREE-001
Role: string quantum-gravity scattering / UV-completion versus low-energy EFT control
State: ACTIVE / NONTERMINAL

## Why this target is more delicate than M01-M08

A string-theory benchmark cannot be made concrete by writing only the word "string theory". The directly calculable universal object is the closed-string four-graviton amplitude in ten dimensions. RQIR, however, is currently organized around a four-dimensional observable/interface benchmark. A legitimate M09 therefore has to freeze both

1. the exact string scattering object, and
2. the compactification/light-spectrum map that turns it into a four-dimensional source-to-detector observable.

The first object is well defined; the second is the current blocker.

## Frozen ancestor amplitude

Use the tree-level type-II closed-superstring four-graviton amplitude with constant dilaton and external NS-NS gravitons. Up to the standard polarization kinematic factor `K`, the universal Virasoro-Shapiro factor can be written schematically as

`A_tree ~ K * [64/(alpha'^3 s t u)] * Gamma(1-alpha' s/4) Gamma(1-alpha' t/4) Gamma(1-alpha' u/4) / [Gamma(1+alpha' s/4) Gamma(1+alpha' t/4) Gamma(1+alpha' u/4)]`,

with massless external gravitons and `s+t+u=0`.

This fixes an all-orders analytic tree-level scattering object rather than an arbitrary list of Wilson coefficients.

## Low-energy expansion

For `alpha' s, alpha' t, alpha' u << 1`, the amplitude reduces to the supergravity/Einstein massless exchange structure plus a correlated infinite derivative expansion. The first characteristic local type-II correction is at order `alpha'^3 R^4`, with coefficient proportional to `zeta(3)`, followed by higher `D^(2k) R^4` structures with string-fixed relations.

This produces an important comparator lesson already:

- at any **fixed finite low-energy order**, the local analytic string corrections can be represented by ordinary gravitational EFT Wilson coefficients and therefore need not be uniquely string-identifying relative to C5;
- the full string amplitude additionally contains the non-polynomial Gamma-function structure and an infinite tower of massive string poles, which a finite local low-energy C5 truncation is not intended to reproduce once the string threshold is resolved.

A claim of a robust string-specific residual must therefore compare models only in a common domain. It is invalid to call C5 "wrong" merely because it ceases to apply at the string scale.

## Intended 4D projection — not yet fully frozen

The current intended realization is a toroidal compactification to four noncompact dimensions with external graviton momenta and polarizations purely in the noncompact directions and with all external energies below the first KK/winding/string threshold used in the matched low-energy slice.

However, a toroidal type-II compactification also contains additional massless/light fields and moduli. Their exchange/couplings and the exact relation between the ten-dimensional kinematic factor and the four-dimensional observable must be declared before assigning a final RQIR comparator residual.

Therefore the present realization ID is provisional until the compactification/light-spectrum ledger is explicit.

## F0-F7 current map

| Gate | State | Reason |
|---|---|---|
| F0 — dynamics | PASS_ANCESTOR / PARTIAL_4D | exact tree-level closed-string four-graviton amplitude exists; exact 4D compactified observable still to freeze |
| F1 — required limits | PASS_SCOPED | low-energy `alpha' E^2 -> 0` gives the corresponding supergravity/Einstein limit |
| F2 — consistency | PASS_SCOPED_PERTURBATIVE_TREE | tree-level string amplitude has the expected crossing/factorization structure; full compactification/unitarity ledger not yet the active blocker |
| F3 — RQIR hierarchy | BLOCKED_4D_INTERFACE | scattering amplitude is concrete, but source/state/detector mapping and full Q1-Q7 hierarchy are not yet frozen |
| F4 — comparator distinction | PARTIAL | finite-order low-energy local terms are C5-EFT-degenerate; full string pole tower is outside finite C5 truncation but must be compared only in overlapping validity domains |
| F5 | BLOCKED | exact 4D quotient observable not frozen |
| F6 | BLOCKED | identifiability cannot precede the compactification/light-field quotient |
| F7 | BLOCKED | resources forbidden before F5/F6 |

## Current first blocker

`STRING_4D_COMPACTIFICATION_INTERFACE_FREEZE`:

1. choose one explicit 4D compactification point or controlled truncation rather than a program label;
2. list all light fields that can participate in the four-graviton/source-to-detector channel;
3. freeze the external-state normalization and four-dimensional gravitational coupling;
4. decide whether the benchmark observable remains purely low-energy (`E << M_string`) or intentionally resolves the first string threshold;
5. compare only against comparators valid in the same energy domain;
6. then determine whether the terminal result is C5/EFT degeneracy, a robust string-specific amplitude fingerprint, or a protocol/interface blocker.

## Candidate discriminators retained for the next iteration

- correlated low-energy coefficient pattern beginning with `zeta(3) alpha'^3 R^4`;
- absence/presence pattern of lower-order local terms in the supersymmetric type-II four-graviton sector;
- all-orders Gamma-function dependence of the Virasoro-Shapiro factor;
- infinite massive string pole tower and residues/factorization;
- compactification-induced KK/winding/light-moduli contaminants that must not be mistaken for string-specific quantum-gravity evidence.

## Sources

1. M. B. Green and P. Vanhove, low-energy expansion of the type-II four-graviton amplitude: explicit Virasoro-Shapiro tree factor and higher-derivative `R^4`, `D^(2k)R^4` expansion.
2. Type-II effective-action literature: leading tree-level `alpha'^3 zeta(3) R^4` correction.
3. E. Claasen and M. Doroudiani, Phys. Rev. Lett. 134, 201601 (2025): modern one-loop type-II four-graviton low-energy expansion and transcendental structure.
4. External RQIR C5 comparator authority: low-energy perturbative quantum GR/EFT, valid only in its declared low-energy domain.

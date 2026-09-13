# Iteration 451 — PRIMARY-SOURCE CANONICAL CAUSAL VERTEX PINNING

## Dependency
Iter450 is terminal `BLOCKED_SOURCE_CAUSAL_INVARIANT_CONTRACTION_OBJECT_AMBIGUOUS` and durably recorded. Iter451 is a new source-disambiguation gate; it does not revise Iter450.

## Frozen primary authority
Bianchi, Chen, Gamonal, **Causal spinfoam vertex for 4d Lorentzian quantum gravity**, arXiv:`2601.23162v1` (30 Jan 2026). Only the immutable v1 source/HTML is authority for this gate. Repository summaries are controls, not authority.

Canonical source targets frozen before production:
- Eq. (3): Feynman-i-epsilon definition of the Toller `T^(±,rho,k)` matrix.
- Eq. (4): fixed-causal-structure vertex amplitude on the magnetic boundary basis.
- Eq. (5): `T^(+)+T^(-)=D` EPRL control identity.
- Eq. (6): EPRL vertex as unconstrained sum over wedge signs.
- Eq. (7): Cartan/SU(2) decomposition of the Toller matrix.
- Immediately surrounding prose fixing: edges `a=1,...,5`; gamma-simple `(rho,k)=(gamma j_ab,j_ab)`; wedge product `1<=a<b<=5`; boundary state with 10 spins and 5 intertwiners; magnetic numbers; group variables; gauge fixing `g_1=1` and integration over `g_2,...,g_5`.

## Frozen independent lanes
1. `eq4_vertex_object`: Eq.(4), 10 wedge factors, `g_b^{-1}g_a`, gamma-simple labels and integration over four unfixed SL(2,C) group elements are explicitly present.
2. `boundary_contraction_domains`: source prose explicitly identifies 10 spins, 5 intertwiners and magnetic indices; the relation between the magnetic-basis amplitude and a general spin-network boundary state is explicit enough to define the intertwiner contraction without invented coefficients.
3. `toller_source_definition`: Eq.(3) and Eq.(7) explicitly define the source Toller object used in Eq.(4), including the branch sign and finite SU(2) magnetic sum in the Cartan decomposition.
4. `eprl_control`: Eq.(5) and Eq.(6) explicitly provide the additive Toller-to-Wigner identity and the EPRL comparison needed as an exact control.

## Frozen aggregate outcomes
- `PRIMARY_SOURCE_CAUSAL_VERTEX_OBJECT_PINNED` iff all four lanes independently verify the required source statements from arXiv:2601.23162v1.
- `BLOCKED_PRIMARY_SOURCE_CAUSAL_VERTEX_OBJECT_INCOMPLETE` if one or more required scientific statements are absent from the authoritative source.
- `INVALID_ITER451_SOURCE_FETCH_OR_PARSE` only for failed source acquisition/parsing or malformed lane output.

No requirement may be weakened after production output is inspected.

## Scope locks
A PASS pins the canonical source object and authorizes later implementation/audit of the contraction. It is NOT D7-S2 closure, not a finiteness theorem, not a numerical vertex evaluation, and not a terminal D7 result. It does not authorize fitted magnetic weights, arbitrary normalization, preferred sequential contraction order, counterterms, or a replacement of the published spectral i-epsilon prescription.

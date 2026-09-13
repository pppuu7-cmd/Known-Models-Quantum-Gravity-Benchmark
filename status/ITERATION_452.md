# Iteration 452 preregistration — immutable primary-source causal-vertex pin

Status at creation: **PREREGISTERED BEFORE SOURCE SNAPSHOT / SCRIPT / WORKFLOW IMPLEMENTATION**.

## Objective
Resolve the Iter450/451 source-object blocker without modifying any collision-power science. Pin a single immutable published source version and test whether it explicitly supplies the complete mathematical object needed before a coupled magnetic/intertwiner causal-vertex audit can be designed.

## Frozen source identity
- Bianchi, Chen, Gamonal, *Causal spinfoam vertex for 4d Lorentzian quantum gravity*.
- arXiv `2601.23162v1`, submitted 2026-01-30.
- Immutable version URL: `https://arxiv.org/html/2601.23162v1`.
- The production snapshot must identify this exact version. No later version, secondary summary, repository paraphrase, or fitted completion may satisfy a missing predicate.

## Frozen independent lanes
1. `toller_feynman_eq3`
   - explicit Feynman `i epsilon` Toller definition;
   - real `tilde rho` integration from `-infinity` to `+infinity`;
   - branch-dependent denominator/prescription;
   - Wigner `D^(tilde rho,k)` integrand and gamma-function factor recorded.
2. `causal_vertex_eq4`
   - fixed-causal vertex built from `T^(sigma_a sigma_b, gamma j_ab, j_ab)`;
   - product over all ten wedges `1 <= a < b <= 5`;
   - integrations over `g_2,...,g_5`;
   - gauge fix `g_1 = identity`;
   - argument `g_b^{-1} g_a` and magnetic indices `m_ba,m_ab` recorded.
3. `boundary_domains`
   - boundary state has ten spins `j_ab`;
   - five intertwiners `i_a`;
   - magnetic-number contraction domain is explicit enough to connect the boundary coefficients to Eq.(4).
4. `eprl_controls_eq5_eq6`
   - additive identity `T^(+) + T^(-) = D`;
   - EPRL vertex is the unconstrained sum over all wedge signs `kappa_ab = +/-1` of the corresponding Toller-defined vertices;
   - no replacement of the source spectral `i epsilon` prescription is allowed.
5. `cartan_magnetic_eq7`
   - Cartan decomposition into two SU(2) Wigner matrices and one reduced Toller function;
   - finite magnetic summation domain `p=-min(j,l),...,min(j,l)`.

## Frozen aggregate criteria
PASS only if:
- all five lanes are structurally valid;
- all five identify exactly `arXiv:2601.23162v1`;
- every frozen predicate in every lane is true;
- all lanes report the same canonical source-snapshot digest;
- the snapshot contains no fitted weights, counterterms, surrogate vertex, or altered spectral prescription.

Frozen PASS classification:
`PRIMARY_SOURCE_CAUSAL_VERTEX_OBJECT_PINNED_COMPLETE`

If the source identity is valid but one or more scientific/source predicates are absent:
`BLOCKED_PRIMARY_SOURCE_CAUSAL_VERTEX_OBJECT_STILL_INCOMPLETE`

Malformed snapshot, digest disagreement, parser crash, missing artifact or workflow failure is infrastructure/implementation failure and must not be reinterpreted scientifically.

## Interpretation lock
A PASS is **source-object qualification only**. It does not establish causal-vertex convergence, absolute integrability, conditional/PV finiteness, EPRL equality for a fixed causal sector, or D7-S2 closure. It only authorizes prospective design of the next direct coupled magnetic/intertwiner contraction gate.

## Claim locks
D7 terminal classifier remains unauthorized. `EXISTING_SUFFICIENT`, `ADAPT_EXISTING`, `HYBRID_REQUIRED`, `NEW_REQUIRED` remain unauthorized. Candidate Gravity remains inactive.
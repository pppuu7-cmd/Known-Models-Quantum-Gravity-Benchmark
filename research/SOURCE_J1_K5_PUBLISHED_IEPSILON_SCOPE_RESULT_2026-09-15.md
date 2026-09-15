# Terminal source-authority result — published i-epsilon scope / joint-regulator gate

Date: 2026-09-15
Status: `TERMINAL_SOURCE_AUDIT_SCOPED`
Classification: `SOURCE_CAUSAL_VERTEX_PUBLISHED_IEPSILON_IS_ONE_WEDGE_NOT_JOINT_COLLISION_REGULATOR_SCOPED`

## Frozen authority

Prospective source-audit preregistration:

- `research/SOURCE_J1_K5_PUBLISHED_IEPSILON_SCOPE_PREREG_2026-09-15.md`
- frozen prereg commit: `3f022730ec04f27f3f5e65561b38d5e33399d67a`

Primary source:

- E. Bianchi, C. Chen, M. Gamonal, *Causal spinfoam vertex for 4D Lorentzian quantum gravity*, arXiv:2601.23162, Phys. Rev. D 113, 126020 (2026).

Companion source, now published and explicitly consumed in this audit:

- E. Bianchi, C. Chen, M. Gamonal, *Toller matrices and the Feynman i-epsilon in spinfoams*, arXiv:2604.24945, Phys. Rev. D 114, 046014 (2026).

## Primary-source checks

### 1. Eq. (3) is a one-Toller-matrix limit

The primary paper defines

`T^(+/-)(g) = lim_{epsilon->0+} integral d(tilde rho) [ ... /(tilde rho-rho ∓ i epsilon) ... ] D^(tilde rho,k)(g)`.

The regulator therefore appears inside the spectral integral defining a **single** Toller matrix.

Result: `PASS`.

### 2. The regulated variable is the one-wedge spectral variable

The integration variable carrying the pole displacement is `tilde rho`. It is not a K5 group-collision coordinate and Eq. (3) does not display a joint ten-wedge group regulator.

Result: `PASS`.

### 3. One Toller matrix is then assigned to each wedge

Immediately after Eq. (3), the paper states that each wedge `(ab)` is associated with a Toller matrix whose sign is set by `kappa_ab=sigma_a sigma_b`.

Result: `PASS`.

### 4. Eq. (4) uses already-defined Toller matrices under the correlated group integral

The causal vertex is displayed as

`integral prod_{a=2}^5 dg_a  prod_{ab} T_ab(g_b^-1 g_a)`

with the product over the ten K5 wedges. The displayed Eq. (4) contains no common positive `epsilon`, no vector `epsilon_ab`, no regulator-removal path, and no order of ten regulator limits across the group integration.

Result: `PASS`.

### 5. Eq. (4) is the proposed fixed-causal-structure vertex definition

The text following Eq. (4) explicitly says that Eq. (4) defines the vertex amplitude with fixed causal structure.

Result: `PASS`.

### 6. Finiteness is explicitly left open

In the Discussion the authors state that, although the gauge-fixed EPRL vertex is finite, finiteness must be investigated again for the causal model to check whether Toller poles produce new divergences.

Result: `PASS`.

### 7. The one-wedge object is not unspecified

The coherent realization, Eq. (17), contains the one-wedge distributional structure

`theta(kappa B) + kappa delta^(rho,j)(B)`.

Thus this audit does not reinterpret a single Toller matrix as undefined. The remaining issue is the correlated use of the ten source-defined factors at common K5 collision loci.

Result: `PASS`.

## Companion-paper cross-check

The later companion paper was checked because it is now published and could in principle have supplied the missing authority.

Its stated scope is the analytic structure of Toller matrices and three equivalent representations. Its Feynman formula again gives an individual reduced Toller matrix as

`t^(+/-) = lim_{epsilon->0+} I_epsilon^(+/-)[d]`,

with the explicit spectral integral in its Eq. (20).

The paper discusses the causal vertex as an application of those Toller-matrix results, but the inspected published formulation does not supply a ten-wedge correlated positive-regulator family across the four-group vertex integral, nor a regulator path/order-independence theorem resolving K5 collision products. Searches of the published arXiv HTML for a joint `regulator`, `group integral`, ten-wedge construction, or a causal-vertex divergence/finiteness theorem did not reveal such a result.

This cross-check strengthens the source-scope classification but is not used to claim that no such construction can ever exist elsewhere.

## Terminal source classification

`SOURCE_CAUSAL_VERTEX_PUBLISHED_IEPSILON_IS_ONE_WEDGE_NOT_JOINT_COLLISION_REGULATOR_SCOPED`

The published Feynman `i epsilon` prescription is authoritative for the **individual Toller matrices**. The displayed causal-vertex definition then uses their product under the correlated K5 group integral. The source equations inspected do not themselves provide a joint ten-wedge prelimit regulator/removal prescription that can be cited as an already-proved collision-extension theorem.

## Relation to the current KMQGB collision evidence

This source result matters because KMQGB has now independently established, within strict scoped witnesses:

1. ordinary local absolute Haar divergence for a fixed nonzero `j=1`, channel-`00000` full-collision witness;
2. transverse scaling degree `30` versus collision codimension `12`, giving same-scaling extension ambiguity order `18` from off-stratum data alone;
3. failure of the standard Hörmander sufficient multiplication criterion at a source-present coherent-contact triangle witness;
4. a six-dimensional K5 conormal cycle-space obstruction at an aligned-spinor witness;
5. absence of bare constrained-causal-sign cancellation for the formal all-ten-wedge highest `j=1` contact monomial.

The source audit prevents these open collision issues from being dismissed merely by pointing back to the one-wedge `i epsilon` in Eq. (3).

## Claim ceiling

This result does **not** prove:

- that Eq. (4) is mathematically meaningless;
- that the causal vertex diverges as a distribution;
- that no canonical source-compatible extension exists;
- that a common-regulator or independent-regulator construction cannot be built;
- that such an auxiliary construction, if built, is source-equivalent;
- closure of D7-S2, D7-S3 or D7-S4;
- any terminal selector.

Absence of an explicit joint regulator in the displayed source definition is an authority/scope fact, not a nonexistence theorem.

## Authorized split of the next analytical front

The broad joint-regulator question is now split into two prospectively controlled tasks:

### A. `SOURCE_J1_K5_EQ4_IMPROPER_DISTRIBUTIONAL_EXISTENCE_GATE`

Determine whether Eq. (4), using the already source-defined Toller factors, exists at K5 collisions in a mathematically controlled source-compatible sense without adding new model data.

### B. `SOURCE_J1_K5_ADDITIONAL_JOINT_REGULATOR_EQUIVALENCE_GATE`

Only if task A cannot be closed directly, prospectively define any auxiliary common/independent regulator family and prove that its limit is equivalent to the published source object. An auxiliary regulator must not be silently promoted to part of the original model.

## Governance

- `RQIR Core v1.0 = FROZEN`.
- `D7-S2 = NOT_CLOSED`.
- `D7-S3 = NOT_CLOSED`.
- `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`.
- terminal D7 selectors forbidden.
- Candidate Gravity inactive.
- KMQGB remains downstream of pinned DSIR authority.

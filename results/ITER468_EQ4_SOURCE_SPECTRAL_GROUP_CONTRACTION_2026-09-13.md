# Iter468 — EQ4 source spectral/group contraction object

Scientific classification: **PASS (SCOPED)**
Terminal label: `ITER468_EQ4_SOURCE_SPECTRAL_GROUP_CONTRACTION_OBJECT_PINNED_SCOPED`

## Authority
- preregistration commit: `a98992d004fc21996e86b8911b45646c8c288270`
- implementation commit: `f60f590357fdbf7a1f10ffbcd763698f146056d2`
- workflow-definition commit: `084a005ed2fedcfac12bc3374a67af666af75b77`
- PR #20 merge commit on main: `71633a0c916811106c89660264d8884b2f4e4893`
- authoritative production head: `a69d5ef00d085b62b016bede8e217ad042f89938`
- run: `34770144171`
- aggregate job: `103758149621`
- aggregate artifact: `10322025879`
- aggregate digest: `sha256:f45fe3012ed14fa4449554e9cd87edbedbe81a551a694d349adae2211a61a5ff`

Raw artifacts:
- A `10320949799`, digest `sha256:67d8a515c60b7f044db19ecce5dc0eec326ea5d88b6d4f54ce5e6bea28b35a9f`
- B `10322315341`, digest `sha256:086296d62cf2f8658ebe9249c26d8585c55e4d4025b12c702870ee58f50878c7`
- C `10322390585`, digest `sha256:fb953bff56225343f312cbf7ef47749704f63f25a98a41c74a3e47ba6922fb3b`
- D `10321896947`, digest `sha256:b46851926bce922f23112cf84fe4dbb8142acdf4b40e2ac97c50703c1bfb8b2f`

## Frozen result
Direct Eq.(3)->Eq.(4) substitution yields ten independent wedge-local spectral variables and four unfixed SL(2,C) group integrations after `g1=1`. The source-faithful formal object is

`A_sigma = lim eps->0+ int prod_e[d rhot_e/(2*pi*i)] prod_e W_e(rhot_e;eps) C({rhot_e})`,

with one Eq.(3) weight `W_e` per wedge and a single common group-contraction kernel

`C({rhot_e}) = int prod_{a=2}^5 dg_a prod_e D_e^(rhot_e,k_e)(g_b^-1 g_a)`.

Stream A: 10 edges, 10 unique spectral labels, 4 group integrations, wedge locality before group integration all exact.

Stream B: all 120 S5 relabelings preserve the formal contraction structure.

Stream C: the common group kernel depends on all ten spectral variables through the ten Wigner-D factors.

Stream D: all frozen false constructions are rejected: a single shared spectral variable, nine variables, five post-gauge-fix group integrals, one omitted wedge, and an artificial spectral delta/equality constraint.

## Scientific interpretation
The missing D7-S2 object-definition blocker is materially narrowed: the source itself defines a formal correlated spectral/group contraction kernel once Eq.(3) is inserted into Eq.(4). Correlation is mediated by the common group integrations, not by postulating a shared spectral variable.

This does **not** establish existence of the epsilon limit, Fubini/Tonelli interchange, absolute/conditional convergence, a valid non-transversal distributional product, or D7-S2 closure. The next dependent gate must address mathematical validity of the correlated ten-variable distributional boundary value with the source-defined group kernel.

Candidate Gravity remains inactive; terminal D7 labels remain forbidden.
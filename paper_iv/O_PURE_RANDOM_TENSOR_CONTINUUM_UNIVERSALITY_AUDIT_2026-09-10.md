# O-Pure-Random-Tensor continuum-universality audit — 2026-09-10

**KMQGB iteration:** 204  
**RQIR Core:** v1.0 FROZEN  
**Parent:** `GFT_TENSOR_MODELS`  
**Material branch:** `PURE_RANDOM_TENSOR_MODELS`  
**Purpose:** determine which explicitly solved pure/random-tensor continuum classes can receive a scoped terminal disposition under the frozen gravity criterion, without extrapolating the result to unresolved interaction classes.

## Frozen gravity target used by this audit

A pure random-tensor subbranch can count as a viable complete gravity continuum only if its declared continuum limit can support a four-dimensional semiclassical Lorentzian gravitational sector rather than merely a lower-dimensional/statistical random-geometry universality class. A solved continuum with incompatible dimensional/geometric universality is a scoped scientific FAIL for that subbranch. An interaction class without a controlled continuum identification remains BLOCKED and is never zero-filled.

## Primary authorities

1. R. Gurau and J. P. Ryan, *Melons are Branched Polymers*, Annales Henri Poincaré 15 (2014) 2085–2131, arXiv:1302.4386. The leading melonic continuum is shown to be precisely branched-polymer universality, with Hausdorff dimension `d_H=2` and spectral dimension `d_S=4/3`.
2. V. Bonzom, T. Delepouve and V. Rivasseau, *Enhancing non-melonic triangulations: A tensor model mixing melonic and planar maps*, Nucl. Phys. B 895 (2015) 161–191, arXiv:1502.01365. Enhanced nonmelonic interactions produce large-N limits containing a branched-polymer phase, a two-dimensional quantum-gravity planar phase, and a transition between them.
3. *Multi-critical behaviour of 4-dimensional tensor models up to order 6*, Nucl. Phys. B 944 (2019) 114611. For the studied U(N)-invariant rank-3/rank-4 interactions up to order six, enhanced models generically exhibit branched-polymer/planar two-phase structure; the authors explicitly motivate new ingredients/higher order or rank to reach higher-dimensional continuum geometry.
4. A. Eichhorn, J. Lumma, A. D. Pereira and A. Sikandar, *Universal critical behavior in tensor models for four-dimensional quantum gravity*, JHEP 02 (2020) 110, arXiv:1912.05314. A background-independent tensor-size RG analysis finds a candidate fixed point with two relevant directions in a rank-4 tensor model and discusses it as a potential continuum limit. This is a candidate/truncation result, not a demonstrated four-dimensional Lorentzian GR continuum.
5. C. I. Perez-Sanchez, *Twofold universality of large-N melonic random tensors*, arXiv:2607.08677 (2026). Within the declared melonic class, leading large-N observables exhibit strong universality across melonic interaction details and rank `D>=3`. This reinforces that the standard melonic sector is a genuine universality class rather than a single-model accident, but does not extend the branched-polymer theorem to nonmelonic sectors.

## Subbranch A — standard melonic large-N continuum

For standard melonic random tensor models the continuum geometry is not merely “similar to” a branched polymer. Gurau–Ryan prove that melonic graphs are precisely branched polymers in the continuum scaling sense, with

- `d_H = 2`,
- `d_S = 4/3`.

Those invariants are incompatible with the required four-dimensional semiclassical Lorentzian gravity target. The failure is structural and does not depend on fitting an observational nuisance model.

**Scoped terminal disposition:**

`FAIL_RQIR_GATE__PURE_RANDOM_TENSOR_STANDARD_MELONIC_CONTINUUM_IS_BRANCHED_POLYMER_NOT_3P1_LORENTZIAN_GRAVITY`

This is a scientific FAIL of the **standard melonic continuum subbranch only**.

## Subbranch B — solved enhanced nonmelonic BP/planar regimes

The Bonzom–Delepouve–Rivasseau enhanced models explicitly leave the purely melonic class, but the solved continuum phases are still identified as

- branched-polymer random geometry, or
- planar/two-dimensional quantum gravity,

with a transition between them. The order-six multicritical survey finds the same BP/planar structure broadly across the studied small-order rank-3/rank-4 invariant models.

Neither solved phase supplies a four-dimensional Lorentzian GR continuum.

**Scoped terminal disposition:**

`FAIL_RQIR_GATE__PURE_RANDOM_TENSOR_SOLVED_ENHANCED_BP_OR_PLANAR_CONTINUA_ARE_NOT_3P1_LORENTZIAN_GRAVITY`

Again, the scope is the explicitly solved enhanced BP/planar universality sectors, not every possible nonmelonic tensor interaction.

## Subbranch C — unresolved higher-dimensional / RG candidate sectors

The branch cannot be globally failed. There are tensor-model constructions whose continuum behavior is not exhausted by the solved BP/planar classes. In particular, the rank-4 background-independent RG study of Eichhorn et al. finds a candidate interacting fixed point with two relevant directions and explicitly investigates a potential continuum limit for four-dimensional random geometry.

However that object does not yet provide all of the RQIR requirements needed for a gravity PASS:

- fixed-point existence is established within a truncation and requires stability under systematic extension;
- the continuum physical geometry is not demonstrated to be four-dimensional Lorentzian GR;
- no same-realization normalized gravitational observable is transported from the fixed point to a semiclassical regime;
- no complete comparator/error certificate exists.

Therefore the unsolved remainder receives

`BLOCKED_SCOPE_NOT_PROVEN__PURE_RANDOM_TENSOR_NONMELONIC_OR_RG_FIXED_POINT_CANDIDATE_SPACE_LACKS_COMPLETE_3P1_LORENTZIAN_GRAVITY_CONTINUUM_CERTIFICATE`.

This BLOCKED state is not a scientific FAIL and cannot count toward `NEW_REQUIRED`.

## Material-branch disposition after Iter204

`PURE_RANDOM_TENSOR_MODELS` remains **nonterminal as an umbrella material branch**, but two broad, explicitly solved continuum sectors now have terminal scoped FAILs:

1. standard melonic / branched-polymer universality;
2. solved enhanced branched-polymer or planar/2D-gravity universality.

The remaining nonmelonic/higher-order/RG-candidate space stays BLOCKED.

Therefore KMQGB freezes:

**`PARTIAL_BRANCH_DISPOSITION__PURE_RANDOM_TENSOR_STANDARD_MELONIC_AND_SOLVED_BP_PLANAR_ENHANCED_CONTINUA_FAIL_3P1_GRAVITY__UNRESOLVED_NONMELONIC_RG_SPACE_BLOCKED`**.

## Why this does not change family-level D7

The parent `GFT_TENSOR_MODELS` contains geometric GFT/spin-foam-generating branches, generalized graph-completion branches, TGFT RG/phase branches and condensate/relational sectors in addition to pure random tensors. The scoped failures above cannot be promoted across those boundaries.

Even within `PURE_RANDOM_TENSOR_MODELS`, the candidate fixed-point/higher-order interaction remainder prevents terminal family exhaustion. The parent residual remains undefined.

## Refined next gate

For the pure-tensor branch itself:

`PURE_RANDOM_TENSOR_NONMELONIC_RG_FIXED_POINT_TO_3P1_SEMICLASSICAL_GEOMETRY_AND_NORMALIZED_GRAVITY_OBSERVABLE_CERTIFICATE`.

For the overall GFT/tensor family:

`GFT_TENSOR_MATERIAL_BRANCH_TERMINAL_DISPOSITION_PLUS_CONTROLLED_GRAVITY_CONTINUUM_TRAJECTORY_NORMALIZED_OBSERVABLE_COMPARATOR_ERROR_CERTIFICATE`.

## Compute decision

Heavy compute remains `IDLE`. A new numerical scan of tensor couplings would not be admissible until one candidate RG realization, truncation-extension protocol, continuum observable and acceptance thresholds are prospectively frozen. The present result is already determined by published continuum-universality theorems/results for the scoped solved sectors.
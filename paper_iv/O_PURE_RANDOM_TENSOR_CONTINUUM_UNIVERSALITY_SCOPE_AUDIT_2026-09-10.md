# Pure random tensor continuum-universality scope audit — Iter204

Date: 2026-09-10
RQIR Core: v1.0 FROZEN
Parent: GFT_TENSOR_MODELS / PURE_RANDOM_TENSOR_MODELS

## Question

Can the pure-random-tensor branch receive a terminal disposition without importing geometric GFT/TGFT data and without promoting a scoped child result to the whole GFT/tensor family?

## Material subbranches

### B5a — standard melonic / tree-dominated large-N continuum sector

Physical object: colored/unitary-invariant rank-D random tensor ensembles whose standard large-N leading sector is melonic and whose critical continuum limit is obtained by tuning the tensor coupling to criticality.

Primary authority:

1. Bonzom, Gurau, Riello, Rivasseau, *Critical behavior of colored tensor models in the large N limit*, Nucl. Phys. B 853 (2011) 174, arXiv:1105.3122. The leading triangulations proliferate as colored trees and the continuum critical geometry is branched-polymer-like.
2. Gurau and Ryan, *Melons are branched polymers*, Ann. Henri Poincare 15 (2014) 2085, arXiv:1302.4386. The melonic continuum universality class is identified with branched polymers.
3. Dartois, Gurau, Rivasseau, *Double Scaling in Tensor Models with a Quartic Interaction*, JHEP 09 (2013) 088, arXiv:1307.5281. The controlled double-scaling extension resums subleading cherry-tree graphs but does not establish an extended 4D GR continuum geometry.
4. Bonzom, Gurau, Ryan, Tanasa, *The double scaling limit of random tensor models*, JHEP 09 (2014) 051, arXiv:1404.7517. Double scaling exists for broad tensor-model classes but is a combinatorial critical limit, not by itself a Lorentzian GR observable map.

Comparator/domain: the frozen Paper-IV gravity target requires an extended continuum gravity realization admitting a normalized gravitational observable on a common physical domain. A tree/branched-polymer critical geometry is not an extended four-dimensional GR-like continuum geometry.

Disposition:

`FAIL_RQIR_GATE__PURE_RANDOM_TENSOR_STANDARD_MELONIC_LARGE_N_CONTINUUM_IS_BRANCHED_POLYMER_NOT_EXTENDED_4D_GR_GEOMETRY`

Scope restriction: this FAIL applies only to the standard melonic/tree-dominated large-N universality sector and its directly controlled critical limits. It is not a FAIL of enhanced/nonmelonic random tensor models, TGFT, geometric GFT, spin foams, or the full GFT_TENSOR_MODELS family.

Error/remainder statement: the result is a universality-class/geometry mismatch, not a small numerical residual. The relevant control is the proven/controlled large-N and critical/double-scaling expansion in the cited model classes. No claim is made outside those asymptotic domains.

### B5b — enhanced / nonmelonic random tensor sectors

Authority:

- Lionni and Thurigen, *Multi-critical behaviour of 4-dimensional tensor models up to order 6*, arXiv:1707.08931. Proper enhancements generate planar (2D-gravity) phases and branched-polymer/planar mixtures; escaping these lower-dimensional universality classes remained open in the analyzed interactions.
- Castro, Eichhorn and Gurau, *Towards a quantitative characterization of gravitational universality classes for order-4 random tensor models*, JHEP 05 (2026) 117. In an O(N)^4 order-4 truncation, three fixed-point candidates are found; the robust real candidate has two relevant directions and is argued to most likely differ from the Reuter universality class. This is valuable continuum-RG evidence but is truncation/regulator dependent and does not supply a normalized Lorentzian gravity observable/comparator.

Disposition:

`BLOCKED_MISSING_REQUIRED_OBJECT__PURE_RANDOM_TENSOR_ENHANCED_NONMELONIC_CONTINUUM_TO_NORMALIZED_4D_GRAVITY_OBSERVABLE_COMPARATOR`

Reason: enhanced/nonmelonic interactions materially change continuum universality. Existing planar/mixed phases cannot be extrapolated to all enhanced models, while the 2026 pregeometric FRG fixed-point candidates do not yet provide the same-realization continuum-to-observable map demanded by frozen RQIR Core v1.0.

## Branch result

PURE_RANDOM_TENSOR_MODELS is therefore `PARTIAL_SUBBRANCH_TERMINAL`: one material child sector has a scoped scientific FAIL; the enhanced/nonmelonic child remains BLOCKED. The parent GFT_TENSOR_MODELS family stays `PARTIAL_SUBFAMILY_ONLY`, with undefined family residual.

No evidence in this audit authorizes NEW_REQUIRED. D2/D4 remain open and D7 remains NOT_CLOSED.

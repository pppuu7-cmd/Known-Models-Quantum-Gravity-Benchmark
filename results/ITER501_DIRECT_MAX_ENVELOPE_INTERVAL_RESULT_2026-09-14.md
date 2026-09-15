# Iter501 — direct 243-channel max-envelope interval science gate

Date: 2026-09-14
Status: TERMINAL METHOD BLOCKER; NO SCIENCE PROMOTION

## Authority
- preregistration: `a02637a56eab2c9d71641ff5c0c9c7b19bfe1b84`
- evaluator: `6a3571826f2f55b4589daf266abcfc57b1f69022`
- aggregate classifier: `712b1efdb5e151fba697b46bb7590066fa1f83e8`
- production head: `c7888d5f2f75239196deecd010312333c3337b2e`
- workflow run: `34820198677`
- source-lock job: `103899801631` — success
- aggregate job: `103905778710` — success
- aggregate artifact: `10338716481`
- aggregate digest: `sha256:dd0c50998749abf03d7913037d105c7b8ec99f8272788a193a185d60894dc38a`

## Frozen terminal classification
`ITER501_NUMERICAL_METHOD_BLOCKER`

The aggregate is structurally complete: all 12/12 frozen causal×block lane artifacts are present exactly once, with no missing or duplicate job IDs. All 12 lanes return the prospectively frozen numerical-method-blocker classification and all 12 point-regression predicates consequently fail. No interval science state is admissible: `class_counts={}`, `n_direction_boxes=0`, `n_rho_box_states=0`; slope/drift/beta science aggregates are therefore null rather than zero.

## Exact observed blocker
Inspection of completed raw lane artifacts shows the same downstream failure before a science interval can be formed: every attempted frozen amplitude box in inspected lanes raises `ArithmeticError('envelope lower bound not positive')` at the direct 243-channel max-envelope stage. For example `0to5-b2` and `1to4-b2` each have 4 signed-direction paths × 16 boxes = 64/64 box failures with that exact error. This occurs after Iter500 removed the upstream generic interval-KAK blocker; it is therefore a distinct contraction/max-envelope enclosure problem, not a reclassification of Iter499 and not evidence for decay or nondecay.

Because box envelopes never become admissible, point containment is necessarily false and the known Iter498 channel-crossing region is not reached by a valid Iter501 enclosure. The aggregate correctly records `known_crossing_region=[]` and `max_possible_max_channel_count=0`; these are method-blocker outputs and carry no physical-zero interpretation.

## Raw artifact provenance
- `0to5-b0`: artifact `10338701060`, `sha256:b713cbb404ca9d981d595dfa9d3107f436fd7160b75e85cb0ce8af350813b999`
- `0to5-b1`: `10338576885`, `sha256:98a3a4deb254fe69e842fc147e365459dadbb801389191e262c8741afbc0dc53`
- `0to5-b2`: `10338338290`, `sha256:d0850d5b06be9d1213e1fe49abf5e1ac0e88ea7a054a426cdce2faae372d0bf4`
- `0to5-b3`: `10338334141`, `sha256:28c325ebe9699c8dad7d2d69f705ec53dc387d14c441492c8c45379b7b8bce2a`
- `1to4-b0`: `10338362485`, `sha256:8c669e549eac3d2caea20dcbb9c05c62ed64b5380f13429762e1d3fe6fcf047f`
- `1to4-b1`: `10338896111`, `sha256:360b5c4ac663e73c1f44ad4fdf90f91586f551f9d04dcb4afc3e63aa3ded7eef`
- `1to4-b2`: `10338024305`, `sha256:246bd3d04d7dc987a6369084aea0061ebd4fbfa0cda12da1701f5d75ac7f051d`
- `1to4-b3`: `10338571836`, `sha256:291b570742e0264e5c56277832a8b625f32026669fcd2d8f4eff0cf06b75361e`
- `2to3-b0`: `10339235144`, `sha256:1fe5f9f2e4e2f3ae4a4ab26aa3c73d7d76cba6a54db7b644cf1218144befe15a`
- `2to3-b1`: `10338856465`, `sha256:13b17f37b8b4302a595b99a7ee166666154c8daa28e230c80150389478753ee0`
- `2to3-b2`: `10339200116`, `sha256:cba3920c48d0f8e1c425d6b9ec7d43c116fc9f6874278137a5c5db3e7b3bad4c`
- `2to3-b3`: `10339135682`, `sha256:001cd6e37ee216dae03cc4a5e2852546c83a6926890531d4f34f73b1a6bc9d3f`

## Interpretation ceiling
This is not a scientific FAIL of the q=1 NONDECAY hypothesis and not a PASS. It does not establish decay, nondecay, positive measure, absolute Haar convergence/divergence, a ten-spectral causal vertex, or D7-S2 closure. Missing interval lower bounds are not zero residuals. Iter498's real channel crossing and Iter500's enabling KAK qualification remain historically valid in their own scopes.

## Consequence
A fresh science gate is not yet admissible on the same boxes until a prospectively frozen enclosure method can produce a strictly positive certified lower bound for the direct max envelope while retaining all 243 channels and allowing crossings. The next useful step is an enabling, non-science branch-and-bound / subdivision certificate for the max-envelope lower bound with frozen subdivision/termination rules and midpoint/source positive controls. Frozen Iter501 criteria must not be weakened or rewritten.

D7-S2 remains NOT_CLOSED; D7-S3 remains NOT_CLOSED; D7-S4 remains PARTIAL_GLOBAL_NOT_CLOSED. Terminal D7 labels and Candidate Gravity remain forbidden/inactive.
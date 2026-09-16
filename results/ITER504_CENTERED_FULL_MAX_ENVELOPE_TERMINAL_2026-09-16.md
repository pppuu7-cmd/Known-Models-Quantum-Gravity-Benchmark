# Iter504 — terminal centered full max-envelope science result

Date: 2026-09-16  
Status: TERMINAL

## Frozen classification

`ITER504_VALIDATED_CENTERED_INTERVAL_INCONCLUSIVE_SCOPED`

This is a **valid scientific INCONCLUSIVE result**, not a numerical-method blocker and not a scientific FAIL.

## Authority

- preregistration: `1ab46b7add51b36b5499f866eb4579137838bfae`;
- centered-shard implementation: `aeef88e899c2f3900a8735b30610e9adabebbb9d`;
- point-regression implementation: `b5e90ed0568e6ca5eb9657bf49f79c69f56cc369`;
- aggregate classifier: `cf4729040b064f1eb77b651b717f0753cfaaed32`;
- workflow head: `56362459a826e3e376c529446678f2fbcaa269ae`;
- Actions run: `34907349374`, terminal `completed/success`;
- summary artifact: `10436186009`, digest `sha256:0273394cbd3d0be55589279645c8170a02042178210b145897bc21e721754163`;
- summary JSON SHA256: `277971cbd394810c4f4185a203f15f8faddc5b88bde3a671e1801edcd861ae5b`.

Green CI is execution/provenance only. The classification below was independently rederived from the frozen preregistration and terminal aggregate payload.

## Completeness / method validity

The terminal summary satisfies the frozen complete-count contract exactly:

- 12 logical causal×block lanes;
- 96 centered box-shard artifacts;
- 12 point-regression artifacts;
- 768 direction/sign/box records;
- 3072 rho/box science states;
- 1728/1728 mandatory point-containment checks;
- no missing, duplicate or extra shard/point lane;
- `valid_structure=true`;
- `method_blocker=false`.

Thus the outcome is eligible for the scientific classifier.

## Scientific result

Frozen state counts:

- `INTERVAL_ROBUST_NONDECAY = 1184`;
- `INTERVAL_INCONCLUSIVE = 1888`;
- `INTERVAL_NONDECAY = 0`;
- `INTERVAL_UNIFORM_DECAY_WITNESS = 0`.

Global validated bounds:

- minimum late-slope lower bound: `3.704072282326188`;
- maximum late-slope upper bound: `4.315308586737589`;
- maximum drift upper bound: `0.6142148940909335`;
- minimum beta lower bound: `0.5011445004474808`;
- maximum number of simultaneously possible max channels in a validated envelope: `46`.

The frozen ROBUST-NONDECAY slope floor is `+1.0`, and every state has late-slope lower bound above that floor. Under the frozen classifier, the 1888 inconclusive states are therefore localized to failure of the `drift <= 0.05` condition rather than to a negative/zero late-slope interval. No frozen state is a uniform-decay witness.

## Independent artifact check

The aggregate classifier was independently read and its decision tree re-evaluated against the terminal summary. The result must be INCONCLUSIVE because:

1. there is no method blocker;
2. not every state is ROBUST_NONDECAY or NONDECAY;
3. there is no UNIFORM_DECAY_WITNESS.

A known channel-crossing shard was independently consumed after terminalization:

- artifact `10378191574`, digest `sha256:416e374269786a5fae6ec319c45929a2e759ff02b40b06ad038374af1deca653`;
- JSON SHA256 `1f1e27cfb4a5d07dd067c6b66b62cbf8f9a5dcb4a4415aa5556f2bf8e39787d0`.

For lane `0to5-b0`, direction `[1,1,1,-1,-1,-1]`, sign `+1`, boxes 8..15 are valid and all 32 rho-box states are INCONCLUSIVE. At box 13 the late-slope intervals remain strictly positive but the drift upper bounds are approximately `0.104, 0.150, 0.613, 0.475`, exceeding the frozen 0.05 tolerance. The R=10 and R=12 rho=2.7 max-envelope contains 29 and 39 possible channels respectively, consistent with the known nonsmooth crossing mechanism.

The corresponding point artifact `10373506543` (digest `sha256:a70dbfe331738ae6bf560d49410178aea9d9d4e60d487e476514aec7aca1fa40`, JSON SHA256 `6224318d5082cff8e3f575278e4f45744295dda8d3738fc7ffcbd01bfae0d3a1`) is valid and shows point late slopes near `4.0` on the inspected lane. This sampled point evidence is a localization diagnostic only; it is not promoted to a full continuous qualification.

## Meaning

Iter504 removes the Iter501/502 numerical-method blocker on the full frozen q=1 signed-direction domain and provides a valid continuous interval science result. It finds no decay witness and strongly positive late-slope lower bounds everywhere, but the centered first-order max-envelope remains too wide/nonstationary under the frozen drift criterion to certify uniform NONDECAY on all 3072 states.

The immediate information bottleneck is therefore no longer slope sign. It is the validated drift/envelope width in the nonsmooth multi-channel max setting.

## Claim ceiling

This result is restricted to the frozen one-dimensional q=1 signed-direction amplitude intervals and 243-channel max envelope. It is not a 6-D or 20-D positive-measure neighborhood theorem, an absolute-Haar divergence theorem, spectral/collision cutoff removal, a fully contracted ten-spectral causal-vertex theorem, D7-S2 closure, D7 selector authority, model/family failure, Candidate Gravity activation or new physics.

`D7-S2 = NOT_CLOSED`; `D7-S3 = NOT_CLOSED`; `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED` remain unchanged.

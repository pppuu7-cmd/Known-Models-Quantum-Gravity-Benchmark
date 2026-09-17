# ITER504S — root-derivative-width vs channel-competition discriminator

Date: 2026-09-17
Status: PROSPECTIVELY FROZEN BEFORE ITER504S SUBSTANTIVE OUTPUT

Gate:

`ITER504S_ROOT_DERIVATIVE_VS_CHANNEL_COMPETITION_DISCRIMINATOR`

## Parent terminal authority

Iter504R is terminal:

`ITER504R_ROOT_AFFINE_REUSE_INCONCLUSIVE_SCOPED`.

Authority:

- Iter504R preregistration `147d68f26ed3a14ce3cd1fd77fcd96d5fb329ec8`;
- Iter504R implementation `f846820bae39963a48272deccb2e4a539100fce1`;
- Iter504R authoritative run `35154724661`;
- Iter504R terminal record `598ede26e0db448411537e9d5f813aa344f88d0f`;
- Iter504R independent Critic `6e300294e6c9a470099776d1c30357eed3fa4b93`.

Iter504R showed that child-delta subdivision alone leaves `2892` depth-10 unresolved leaves while the late-slope floor remains strongly positive. The frozen residual mechanism space is therefore root derivative enclosure width and/or nonsmooth max-channel competition, with a possible third outcome of fixed-channel nonstationarity.

## Scientific question

At exact zero child width, while keeping the **same full-root validated derivative balls** used by Iter504R, does the continuous drift remain above `0.05` away from the root midpoint? If yes, does a prospectively defined derivative-radius-collapse sensitivity remove that excess, or does max-channel competition / fixed-channel nonstationarity remain?

This is a bounded mechanism-localization gate. It does not reclassify the full Iter504 domain.

## Frozen source and arithmetic

Unchanged from Iter504R:

- `python-flint==0.9.0`;
- Arb/Acb precision `384` bits;
- exact same Iter504 KAK/source/Toller/exact-rational intertwiner/contraction implementation;
- exact same Iter504R `build_root_model` full-root derivative construction;
- all `243` channels retained in every full-envelope computation;
- no channel pruning;
- same causal `0to5`, block `0`, path `2`, direction `[1,1,1,-1,-1,-1]`, sign `+1`;
- same roots `13,14,15`;
- all rhos `[0.35,0.9,1.6,2.7]`;
- R grid `[6,8,10,12]`;
- same late slope `(Y12-Y8)/4` rigorous lower/upper pairing;
- same early slope `(Y10-Y6)/4`;
- same drift-upper construction;
- robust floor `+1.0`;
- drift threshold `0.05`.

## Frozen exact diagnostic points

For each root interval `I=[lo,hi]`, evaluate exactly three degenerate child points:

- `LOW = lo`;
- `MID = (lo+hi)/2`;
- `HIGH = hi`.

Thus the exact amplitudes are:

- root 13: `LOW=29/12800`, `MID=59/25600`, `HIGH=30/12800`;
- root 14: `LOW=30/12800`, `MID=61/25600`, `HIGH=31/12800`;
- root 15: `LOW=31/12800`, `MID=63/25600`, `HIGH=32/12800`.

No point may be added, removed or moved after output.

## Diagnostic A — rigorous zero-width full-D envelope

Build the full Iter504R root model exactly once per root. At an exact point `a`, use the degenerate exact displacement `delta = a-root_midpoint` but retain the unchanged full-root derivative balls `D(I)` and full-root Haar/log derivative ball.

For all `243` channels compute

`f_i(a) in f_i(root_midpoint) + delta * D_i(I)`

and the unchanged 243-channel max envelope. Compute the same `S_lower`, `S_upper`, `E_lower`, `E_upper`, `drift_upper`, possible-max set and strict-dominance gap.

This is rigorous under the same root-superset derivative construction as Iter504R. It answers whether further child-width subdivision can remove the residual while `D(I)` is frozen.

## Diagnostic B — derivative-radius-collapse sensitivity

At the same exact point, replace only each derivative ball `D_i(I)` and the Haar/log derivative ball by its deterministic midpoint value; keep the Iter504R midpoint channel values, source, 243-channel max construction, rho/R grids and formulas unchanged.

This diagnostic is **control-only mechanism sensitivity**, not a validated scientific enclosure and not a replacement classifier for Iter504/Iter504R. It is frozen before output to test whether derivative-ball radius is the source of the excess width.

No threshold is refit.

## Diagnostic C — fixed-channel competition test

For each exact point and rho, compute the zero-width point slopes/drift separately for every channel index `0..242` using the same four R values.

A fixed-channel row is eligible only if its magnitude lower bound is strictly positive at all four R values, so every logarithm is validated.

For the full-D and derivative-center sensitivity separately:

- compute the union of full-envelope `possible_max_indices` over R;
- compute fixed-channel drift for every eligible member of that union;
- record the maximum fixed-channel drift and its witness;
- record whether **all** eligible possible-max channels satisfy drift `<=0.05`;
- if any possible-max candidate is not eligible, record `competition_test_complete=false` rather than silently discard it.

If the full max-envelope drift is `>0.05`, the competition test is complete, and every possible-max fixed channel is individually `<=0.05`, then max-channel competition/switching is necessary for that envelope excess under the corresponding derivative treatment.

No channel is removed from the actual max-envelope calculation.

## Strict dominance diagnostic

For every R/rho/point, let `L_i` and `U_i` be the validated magnitude bounds of all 243 channels. Let `i*` maximize `L_i`. Compute

`dominance_gap = L_i* - max_{j != i*} U_j`.

`dominance_gap > 0` is a rigorous unique-max certificate. Nonpositive gap is only lack of dominance proof; it is not itself proof of crossing.

## Per-case mechanism flags

For each root/location/rho:

- `full_D_within_tolerance := S_lower >= 1.0 and drift_upper <= 0.05`;
- `derivative_radius_sensitivity := full_D drift_upper > 0.05 and derivative-center drift_upper <= 0.05`;
- `competition_necessary_full_D := full_D drift_upper > 0.05 and full-D competition test complete and all eligible possible-max fixed-channel drifts <= 0.05`;
- `competition_necessary_center_D := derivative-center drift_upper > 0.05 and center-D competition test complete and all eligible possible-max fixed-channel drifts <= 0.05`;
- `fixed_channel_nonstationarity_center_D := derivative-center drift_upper > 0.05 and at least one eligible possible-max fixed channel has drift_upper > 0.05`.

These flags are diagnostic only; none changes Iter504R.

## Frozen terminal classifier

After all `3 roots x 3 locations x 4 rhos = 36` cases are present and all source/root controls pass:

### ROOT DERIVATIVE RADIUS LOCALIZED

`ITER504S_ROOT_DERIVATIVE_RADIUS_LOCALIZED_SCOPED`

iff:

1. every MID full-D case is within the frozen tolerance;
2. at least one LOW/HIGH full-D case violates `0.05`;
3. every LOW/HIGH case that violates full-D `0.05` has `derivative_radius_sensitivity=true`;
4. no LOW/HIGH derivative-center case violates `0.05`.

This means the frozen full-root derivative-ball radius is sufficient to explain the residual root-affine enclosure failure on these endpoint diagnostics; it is a mechanism-localization result, not a full-domain theorem.

### CHANNEL COMPETITION NECESSARY

`ITER504S_CHANNEL_COMPETITION_NECESSARY_SCOPED`

iff the previous classifier does not apply, at least one derivative-center case violates `0.05`, every such violating derivative-center case has a complete competition test with `competition_necessary_center_D=true`, and none has fixed-channel nonstationarity.

### FIXED-CHANNEL NONSTATIONARITY REMAINS

`ITER504S_FIXED_CHANNEL_NONSTATIONARITY_REMAINS_SCOPED`

iff the first two classifiers do not apply and at least one derivative-center violating case has `fixed_channel_nonstationarity_center_D=true`, with no incomplete required diagnostics.

### MIXED / UNRESOLVED MECHANISM

`ITER504S_MIXED_MECHANISM_SCOPED`

iff implementation/provenance is valid but the valid cases do not satisfy any of the three classifiers above, including mixtures or incomplete competition attribution.

### INVALID

`ITER504S_INVALID`

iff source/provenance/root identity/precision/channel completeness/formula/threshold/cohort/point identity fails, any required root control fails, or any actual full-envelope calculation prunes channels.

No post-outcome fifth scientific classification may be invented.

## Independent reproduction

Run two independent Ubuntu cohorts with Python `3.11` and `3.13`, both pinning `python-flint==0.9.0`. The final consumer must verify identical discrete classification/mechanism flags and exact rational identities. Byte-identical floating serialization is desirable but is not itself a scientific criterion; any numerical disagreement that changes a frozen inequality or mechanism flag makes the gate INVALID until explained.

## Negative controls

The Critic must reject at least:

- missing root/location/rho;
- wrong exact amplitude;
- threshold other than `0.05`;
- floor other than `+1.0`;
- omitted channel;
- active-channel pruning;
- descendant/point derivative recomputation replacing the frozen root derivative;
- changed root/path/sign/rho/R grid;
- treating derivative-center sensitivity as a rigorous enclosure;
- silently excluding a nonpositive-log possible-max candidate from the competition test.

## Claim ceiling

This gate is restricted to nine exact points inside the three frozen Iter504R diagnostic roots. It does not reclassify the 1888 parent Iter504 inconclusive states, does not prove absolute-Haar divergence or positive-measure behavior, does not close D7, does not authorize selector labels, does not activate Candidate Gravity, and does not establish a quantum-gravity solution or new physics.

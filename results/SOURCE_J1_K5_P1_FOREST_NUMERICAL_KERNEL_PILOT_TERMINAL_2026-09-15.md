# SOURCE_J1_K5_P1_FOREST_NUMERICAL_KERNEL_PILOT — terminal result

Date: 2026-09-15
Status: TERMINAL

## Authority

- Gate: `SOURCE_J1_K5_P1_FOREST_NUMERICAL_KERNEL_PILOT`
- Frozen preregistration: `research/prereg/SOURCE_J1_K5_P1_FOREST_NUMERICAL_KERNEL_PILOT_2026-09-15.md`
- Preregistration commit: `a414760fe676b308db0c0c446f099409867e8407`
- Lane implementation commit: `19acbe95f6d7959983893e0d021cda585e5021ca`
- Aggregate implementation commit: `545f7de5850a455d73921f2db16af10a6921b0b5`
- Workflow head: `dd923b6d4e534caed6ad3cdf6bf561c4457adb01`
- Authoritative run: `34992366470`
- Source-lock job: `104459950823` — success
- dps180 job: `104460016406` — success
- dps260 job: `104460016493` — success
- aggregate job: `104460627505` — success

Artifacts:

- dps180: ID `10406431460`, digest `sha256:81b3880f1aa090ef7fe08c581947565ee94b8d867d5b39fbeed59019c5faa9b4`
- dps260: ID `10406740650`, digest `sha256:b9c07a3256ac525d268e92564d4a1cbf8f111abff49ca75b79538417711ce624`
- aggregate: ID `10406111643`, digest `sha256:d11ecfce8bbf1667c6119984b1e13a0ee1ed921066dcb1ddebefbac2b9a30afd`

## Frozen terminal classification

`P1_FOREST_NUMERICAL_KERNEL_CONFIRMED_SCOPED`

The scientific classification is taken from the prospectively frozen aggregate classifier, not from workflow color.

## Lane-level controls

Both 180-digit and 260-digit lanes independently classified

`P1_FOREST_NUMERICAL_KERNEL_LANE_VALID`.

All frozen lane controls passed:

- exact P1 exponent map `(1,1,1,1,2,2,2,2,2,2)`;
- deliberately broken P1 pattern rejected;
- exact `Gamma_S(1)=I` on all workload subsets;
- historical raw P1 positive lock at `alpha=0.55`, `k=5,6`;
- all outputs finite;
- exact S4 numerical covariance for the four anchor-pair and six internal-pair size-2 orbits;
- deliberately perturbed historical raw authority detected.

The maximum normalized discrepancy from the frozen historical raw P1 values was

`1.7998500053109934504108130845992882626227033836306096084253754496170996243102777e-80`,

well below the frozen `1e-65` raw-lock tolerance.

The measured S4 numerical covariance error was exactly `0.0` in both frozen size-2 orbits in both precision lanes.

## Cross-precision result

The aggregate compared both precision lanes on representatives `{0,1}` and `{1,2}` at `k=5,6` for every frozen field

`raw, F(0), F'(0), F''(0), T2, R2`.

Maximum normalized cross-precision discrepancy:

`2.449852037706867383015719092421846454873239055019858189442548293890036969430474612695575998032290656e-155`.

Frozen tolerance:

`1e-110`.

Thus the numerical kernel clears the required precision margin by roughly 45 decimal orders.

## Scientific meaning

The generalized Gaussian pairing engine and the exact barycentric size-2 Taylor projector can be coupled reproducibly to the stable historical P1 auxiliary Gaussian object. The result validates the numerical building block needed for a later multi-subset forest calculation.

The diagnostic quantity `R2=F(1)-T2` was explicitly non-deciding in this gate. Its sign or scale dependence was not consumed by the classifier.

## What this does NOT establish

This result does not establish:

- stabilization or divergence after proper K5 forest subtraction;
- validity of a 29-orbit multi-subset calculation before its own method/control gate;
- source authorization or uniqueness of the KMQGB-derived forest prescription;
- Eq. (4) existence or nonexistence;
- model/family failure;
- D7-S2/S3/S4 closure;
- any terminal selector;
- Candidate Gravity activation.

## Next admissible gate

Before the 29-orbit production diagnostic, validate the **mixed Taylor-jet composition method** on prospectively frozen laminar forests that exercise:

1. a nested pair with orders `2` and `7`;
2. a disjoint pair;
3. a maximal nested chain with orders `2,7,15`.

The method gate must compare direct multivariate mixed derivatives against sequential Taylor application/order reversal where computationally feasible, use two precision lanes, preserve the exact operator digest, and remain non-scientific. Only a terminal mixed-jet PASS may authorize the full 29-orbit P1 forest-subtraction diagnostic.

Governance remains unchanged: `RQIR Core v1.0 = FROZEN`; `D7-S2 = NOT_CLOSED`; `D7-S3 = NOT_CLOSED`; `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`; terminal selectors forbidden; Candidate Gravity inactive; KMQGB remains downstream of pinned DSIR authority.
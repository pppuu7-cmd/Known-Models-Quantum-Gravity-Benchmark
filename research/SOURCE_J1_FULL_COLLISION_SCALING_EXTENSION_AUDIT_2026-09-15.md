# Source-order j=1 full-collision scaling/extension audit

Date: 2026-09-15
Status: `DERIVED_KMQGB_SCOPED`; no terminal D7 promotion

## Purpose

Sharpen the remaining source-order collision problem after the independently reviewed theorem

`SOURCE_J1_FULL_COLLISION_ABSOLUTE_DIVERGENCE_THEOREM = CONFIRMED_SCOPED`.

The key distinction established here is:

1. the published Feynman `i epsilon` prescription already specifies each **single-wedge Toller object** distributionally;
2. this does **not by itself** prove that the correlated product of ten wedge distributions is canonically defined at the full K5 collision;
3. the already-certified fixed-channel full-collision singularity has scaling degree 30 transverse to a codimension-12 collision stratum, so off-collision data alone admit a local extension ambiguity of normal order at most 18.

This is a scope refinement and an extension-theory theorem. It does not choose a renormalization prescription and does not close D7-S2.

## Authority

### Repository authority

- `research/SOURCE_J1_TOLLER_COLLISION_POLE_LEDGER_2026-09-15.md`.
- `research/SOURCE_J1_FULL_COLLISION_ABSOLUTE_DIVERGENCE_THEOREM_2026-09-15.md`.
- `recovery/CRITICAL_REVIEW_SOURCE_J1_FULL_COLLISION_2026-09-15.md`, verdict `CONFIRMED_SCOPED`.
- Exact same-realization certificate authority: repair head `bcc221b2a77572ace32fcb9dbd84fd78fb90ec03`, run `34910999176`, artifact `10374004571`, digest `sha256:3e378db8f5ac81d5086cbc82f53b2915154bd2d695206154f0220c4ce210fdc3`.

### External mathematical/source authority

Bianchi, Chen and Gamonal, *Causal spinfoam vertex for 4D Lorentzian quantum gravity*, Phys. Rev. D 113, 126020 (2026), arXiv:2601.23162. Their coherent-state formula writes the one-wedge Toller object as a CP1 integral containing

`Theta_{sigma,rho,j}[B] = theta(sigma B) + sigma delta^{(rho,j)}(B)`,

where `delta^{(rho,j)}` is a finite sum of derivatives of the Dirac delta supported at `B=0` (their Eq. (17), Appendix D, Eqs. (D1)-(D5)). Thus the source `i epsilon` prescription is already a distributional one-wedge prescription.

For extension theory use Brunetti and Fredenhagen, *Microlocal Analysis and Interacting Quantum Field Theories: Renormalization on Physical Backgrounds*, Commun. Math. Phys. 208 (2000) 623-661, arXiv:math-ph/9903028, especially the scaling-degree extension theorem at a point and its submanifold version.

## OBJECT

Fix exactly the scope of the reviewed collision theorem:

- gauge-fixed K5 source-order causal vertex;
- fixed `j=1`;
- fixed nonzero real edge `rho_e`;
- any of the three frozen causal signatures `{0to5,1to4,2to3}`;
- allowed intertwiner channel `00000`;
- the full collision stratum `N = K^4`, `K=SU(2)`, inside `G^4`, `G=SL(2,C)`;
- a compact-base/tangent conic neighborhood of the exact rational witness used by the reviewed theorem, chosen away from lower pair-collision subcones.

No claim is made here about all channels, all spins, or lower collision strata.

## Result 1 — one-wedge versus ten-wedge distributional status

The source Feynman representation does **not** leave an unspecified one-wedge object. In the coherent basis the one-wedge Toller matrix contains explicit `theta(B)` and finite `delta^(n)(B)` contact terms. Therefore the correct remaining source-order question is not

> how should a single Toller pole be extended?

but

> is the correlated product/pullback of the ten already-defined wedge distributions well-defined on the common K5 collision set, and if not, what additional source-compatible extension/normalization data select it?

Specifying ten individual distributions is not, by itself, a theorem that their product after pullback to four correlated group variables exists. A product theorem requires a valid multiplication/pullback criterion (for example a wavefront-set transversality statement) or a separate source-defined joint limiting construction.

Classification:

`SINGLE_WEDGE_DISTRIBUTIONAL_PRESCRIPTION = SOURCE_DEFINED`

`TEN_WEDGE_CORRELATED_COLLISION_PRODUCT = NOT_YET_JUSTIFIED`

## Result 2 — transverse scaling degree at the certified full-collision witness

The reviewed theorem establishes in a conic neighborhood away from lower pair-collision directions:

- ten nonzero one-edge cubic poles;
- product leading order `t^(-3*10) = t^-30`;
- full-collision normal codimension `4*(dim SL(2,C)-dim SU(2)) = 4*(6-3) = 12`;
- nonzero exact angular coefficient `11/24` for channel `00000`;
- subleading remainder one power less singular.

After multiplying by smooth compact tangential and angular cutoffs supported inside that witness neighborhood, the punctured normal distribution therefore has exact scaling degree

`sd_N = 30`.

The corresponding degree of divergence relative to the collision submanifold is

`omega = sd_N - codim(N) = 30 - 12 = 18`.

This is the extension-theory counterpart of the previously proved radial absolute-divergence exponent

`t^(12-1) * t^-30 = t^-19`.

## Result 3 — local extension ambiguity

The standard finite-scaling-degree extension theorem implies that extensions across the full-collision submanifold with the same scaling degree exist locally, but are not unique when `sd_N >= codim(N)`.

For the conically localized fixed-channel object here,

`sd_N = 30 > 12 = codim(N)`.

Hence off-collision data alone do not select a unique local extension. The difference between two same-scaling-degree extensions is supported on the collision submanifold and has bounded normal order. Locally its normal derivative order is at most

`18`.

On a fixed tangential slice this reduces to the familiar finite jet

`sum_{|alpha| <= 18} c_alpha partial^alpha delta(normal)`.

Along the full submanifold the coefficients may carry tangential dependence; this note does not impose symmetry reductions on that ambiguity.

Classification:

`FULL_COLLISION_OFF_STRATUM_EXTENSION_UNIQUENESS = FALSE_WITHOUT_ADDITIONAL_CONDITIONS_SCOPED`

This statement is deliberately narrower than saying that no canonical source extension exists.

## What the source i-epsilon may still do

A stronger source-defined theorem remains possible. The published one-wedge `i epsilon` prescription could select a particular **joint** K5 distribution if one proves, for the correlated ten-wedge object, an appropriate limit/pullback/product theorem.

To promote such a result one must establish at least one source-faithful route such as:

1. a common-regulator family whose ten-wedge correlated product exists before the regulator is removed and converges in `D'` across the full collision;
2. a microlocal product theorem showing that the required wedge distributions satisfy an admissible wavefront-set condition after correlated pullback;
3. an explicit extension prescription plus normalization/symmetry identities that fixes the allowed collision-supported ambiguity and is shown to be the limit of the source Feynman construction.

If independent regulators `epsilon_e` are used, path/order independence must be proved rather than assumed.

## Nested-stratum guard

The conic witness used above is chosen away from lower pair-collision subcones. Therefore the scaling-degree result isolates the full-collision obstruction cleanly, but it does **not** classify all nested K5 collision strata. Iter461 remains the registered independent collision-partition stream and must not be duplicated.

Nested strata may add compatibility conditions or additional extension problems; they cannot be declared resolved by this full-collision result alone.

## Relation to reordered ten-spectral representation

The ten independent spectral boundary-value distributions remain a legitimate tensor product in spectral variables before correlated group integration. That fact does not automatically identify a reordered pairing `<W,C>` with the primary source-order product at the collision.

The two open statements remain distinct:

- source order: joint group-variable product/extension at K5 collisions;
- reordered representation: spectral pairing plus exchange/Fubini/microlocal justification.

Neither can be used to silently define the other.

## Immediate next admissible analytical gate

`SOURCE_J1_K5_JOINT_FEYNMAN_PRODUCT_MICROLOCAL_GATE`

Target question:

> Does the source-defined ten-wedge Feynman construction determine a unique correlated distribution across the full K5 collision for the reviewed fixed `j=1`, channel-`00000` scope?

Required subchecks:

1. write the exact one-wedge coherent distribution `theta(sigma B)+sigma delta^{(rho,1)}(B)` in the same source conventions as the collision theorem;
2. compute/pin the conormal covectors of the pulled-back wedge hypersurfaces at the full collision;
3. test the Hörmander multiplication criterion for all contact-term combinations relevant to the frozen causal signatures;
4. if the criterion fails, distinguish `criterion not applicable` from an actual nonexistence proof;
5. if a regulator family is used instead, freeze common versus independent regulator paths prospectively and prove path/order independence or record the ambiguity;
6. preserve the exact source identity `T+ + T- = D` at the distributional/joint level as a mandatory control;
7. do not infer any conclusion for lower collision strata before consuming Iter461.

## Claim ceiling

This audit proves only:

- the source already fixes each one-wedge Toller distribution;
- the correlated ten-wedge collision product still needs a joint product/extension theorem;
- the certified fixed-channel full-collision singularity has transverse scaling degree 30 in codimension 12;
- same-scaling local extensions based only on off-collision data have normal ambiguity order at most 18.

It does **not** prove:

- that the source Feynman prescription fails to define a unique joint vertex;
- that every channel/spin sector diverges;
- that principal-value, conditional or distributional amplitudes fail;
- that the reordered spectral representation is equivalent to the source-order vertex;
- closure of D7-S2, D7-S3 or D7-S4;
- any terminal selector `EXISTING_SUFFICIENT / ADAPT_EXISTING / HYBRID_REQUIRED / NEW_REQUIRED`.

## Governance

- `RQIR Core v1.0 = FROZEN`.
- `D7-S2 = NOT_CLOSED`.
- `D7-S3 = NOT_CLOSED`.
- `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`.
- Candidate Gravity remains inactive.
- KMQGB remains downstream of the pinned DSIR authority; this audit changes no DSIR object or normalization.

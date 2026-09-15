# Terminal result — Eq. (4) local full-collision extension existence versus uniqueness

Date: 2026-09-15
Status: `TERMINAL_SCOPED`
Classification: `SOURCE_J1_K5_EQ4_LOCAL_EXTENSION_EXISTS_UNIQUENESS_OPEN_SCOPED`

## Frozen authority

- preregistration: `research/SOURCE_J1_K5_EQ4_LOCAL_EXTENSION_EXISTENCE_PREREG_2026-09-15.md`
- frozen prereg commit: `43a4cb12289509a2b4f74192aa709e0c0c6c240e`
- exact premise certificate: `code/source_j1_k5_eq4_local_extension_existence_certificate.py`
- implementation commit: `6a503bacbabd36ac81a69e091f4322be651418cc`
- workflow head: `1c7d20683414844d4ccf4387245e80db9d303698`

## Authoritative run

- workflow run: `34916570152`
- source-lock job: `104215364399`, success
- exact-premise-certificate job: `104215410266`, success
- artifact: `10375929193`
- artifact name: `source-j1-k5-eq4-local-extension-existence`
- artifact digest: `sha256:644dc49c98952a9158326bef9af1633d99dc654cc06ef47ca44145ea54193eab`

## Certified premises

The exact certificate revalidated the frozen local full-collision ledger:

- transverse scaling degree `sd_N = 30`;
- normal codimension `codim(N) = 12`;
- singular order `30-12 = 18`;
- ordinary radial absolute-integrability exponent `-19`;
- therefore ordinary local absolute Haar integrability fails in the frozen witness;
- zeroth-order collision term `delta_N` has scaling degree `12 <= 30`;
- the exact EPRL-preserving counterterm witness has full independent-sign shift `0` but causal-sector shift `1008`.

The certificate also records the scope controls:

- fixed `j=1`;
- channel `00000`;
- conic full-collision patch away from lower pair-collision subcones;
- lower collision strata not consumed;
- no global Eq. (4) definition claimed.

## Theorem-level conclusion

The substantive existence conclusion is not produced by Python. It follows from the cited finite-scaling-degree extension theorem applied to the already established punctured distribution on the frozen conic patch:

> finite transverse scaling degree implies that a distribution defined off the collision submanifold admits a local extension across that submanifold preserving the scaling degree.

Because the frozen scaling degree is finite (`30`), at least one local distributional extension across the full-collision submanifold exists on this scoped patch.

Because `30 >= 12`, the same theorem does not provide automatic uniqueness. The allowed same-scaling extension freedom is collision-supported and has normal order through `18` in the frozen integer ledger.

Thus the correct conclusion is explicitly two-sided:

`LOCAL DISTRIBUTIONAL EXISTENCE = CERTIFIED_SCOPED`

`SOURCE-CANONICAL UNIQUENESS = NOT_YET_CERTIFIED`

## Relation to ordinary divergence

The previously certified radial behavior `t^-19` proves failure of ordinary local absolute Haar integration for the frozen source-order witness. It does **not** imply that no distributional continuation exists.

This gate therefore removes an important false dichotomy from D7-S2:

- ordinary absolute integral: fails in the scoped witness;
- local distributional extension: exists;
- source-canonical selection of that extension: remains open.

## Why uniqueness is still open

The already terminal collision-counterterm gate gives an explicit local `delta_N` coefficient family which simultaneously preserves:

- off-collision agreement;
- the same scaling-degree ceiling;
- K5 permutation covariance;
- the exact full EPRL independent-sign sum rule;

while shifting the constrained causal sector nontrivially.

Therefore those conditions, even taken together, do not select a unique causal full-collision extension.

The published one-wedge Feynman `i epsilon` prescription also cannot simply be cited as an already-proved joint ten-wedge collision normalization: the separate source-authority audit established that the displayed Eq. (3) regulates individual Toller matrices, whereas Eq. (4) then uses their product under the correlated K5 group integral.

## Claim ceiling

This result does **not** prove:

- that the published Eq. (4) is globally well-defined;
- that Eq. (4) is globally ambiguous;
- that every channel or spin admits the same extension statement;
- that lower/nested K5 collision strata are resolved;
- that a source-faithful normalization condition cannot uniquely select one extension;
- closure of D7-S2, D7-S3 or D7-S4;
- any terminal selector.

## Frontier consequence

The full-collision analytical question is now narrowed from existence to **source-canonical selection**.

Authorized next analytical gate:

`SOURCE_J1_K5_EQ4_SOURCE_NORMALIZATION_SELECTION_GATE`

It must identify a source-derived condition stronger than the already-insufficient set

- off-collision agreement;
- same scaling degree;
- K5 permutation covariance;
- EPRL independent-sign sum rule,

and test whether that condition eliminates the explicit collision-supported counterterm witness.

Lower collision strata remain independent and depend on unresolved Iter461.

## Governance

- `RQIR Core v1.0 = FROZEN`.
- `D7-S2 = NOT_CLOSED`.
- `D7-S3 = NOT_CLOSED`.
- `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`.
- terminal D7 selectors remain forbidden.
- Candidate Gravity remains inactive.
- KMQGB remains downstream of pinned DSIR authority.

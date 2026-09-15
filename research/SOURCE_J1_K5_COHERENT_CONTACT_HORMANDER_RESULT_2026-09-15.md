# Terminal result — source j=1 K5 coherent-contact Hörmander gate

Date: 2026-09-15
Status: `TERMINAL_SCOPED`
Classification: `SOURCE_J1_K5_COHERENT_CONTACT_HORMANDER_CRITERION_FAILS_SCOPED`

## Frozen authority

Prospective preregistration:

- `research/SOURCE_J1_K5_COHERENT_CONTACT_HORMANDER_PREREG_2026-09-15.md`
- frozen prereg commit: `d13c6672125c022dce6b645a4efa1f25cc31aff4`

Exact certificate implementation:

- `code/source_j1_k5_coherent_contact_hormander_certificate.py`

Workflow:

- `.github/workflows/source-j1-k5-coherent-contact-hormander.yml`

The workflow required the preregistration file to remain exactly at the frozen prereg commit. Two earlier runs failed before scientific execution because of source-lock orchestration only. The first issue was shell quoting of `delta''(B)`; the second was shallow checkout preventing the frozen prereg commit from being present locally. Neither failure executed the exact certificate or changed the preregistered scientific contract.

Final provenance-only repair head:

- `9d1ac7710987b1b3eb077b3eebc5afcd59dfac8e`

## Authoritative run

- workflow run: `34915343800`
- workflow conclusion: `success`
- source-lock job: `104211642816`, `success`
- exact-certificate job: `104211669941`, `success`
- artifact: `10376205845`
- artifact name: `source-j1-k5-coherent-contact-hormander`
- artifact digest: `sha256:d94ebec1a747afc17e7a7b86553cfc8153d736dc8f7796b9853b345b28883ff2`

## Exact certified controls

The dependency-free exact certificate produced the preregistered classification and verified:

1. frozen coherent spinor `z0=(1,0)^T` has Bloch vector `(0,0,1)`;
2. the three source-linearized K5 conormals `dB_12`, `dB_23`, `dB_13` are all nonzero;
3. the exact triangle relation is identically zero in all 12 normal coordinates:

   `dB_12 + dB_23 - dB_13 = 0`;

4. exact rank of `{dB_12,dB_23,dB_13}` is `2`;
5. forest control `{dB_12,dB_13}` has rank `2`;
6. non-cycle control `{dB_12,dB_23,dB_14}` has rank `3`, and the analogous frozen relation is nonzero;
7. exact source `j=1` polynomial coefficients are

   - `c1=(3 rho^2+1)/(rho(1+rho^2))`,
   - `c2=6/(1+rho^2)`,
   - `c3=6/(rho(1+rho^2))`;

8. the `delta''(B)` contact coefficient is

   `i/[rho(1+rho^2)]`,

   hence nonzero for frozen real `rho != 0`.

The workflow output therefore records:

`hormander_sufficient_criterion_at_frozen_witness = false`.

## Scientific interpretation

At the frozen full-K5 compact collision witness, the source-present three-contact subproduct on triangle `(12),(23),(13)` admits nonzero conormal wavefront covectors whose signed sum vanishes exactly.

Therefore the standard Hörmander sufficient criterion for distribution multiplication cannot be used to justify this coherent-contact subproduct at that witness. A fortiori, that sufficient criterion alone cannot certify the full correlated ten-wedge coherent contact product through the same collision.

This materially sharpens the remaining source-order problem:

- the one-wedge distributions are source-defined;
- ordinary local absolute Haar integrability already fails in the independently reviewed fixed `j=1`, channel-`00000` full-collision scope;
- off-stratum same-scaling extensions have collision-supported ambiguity at the previously certified scaling degree `30` versus codimension `12`;
- and now the elementary Hörmander sufficient product theorem is explicitly unavailable at a source-present contact witness.

The next admissible analytical question is therefore not another ordinary convergence estimate. It is whether the **source Feynman regulator itself** defines a unique correlated joint distributional limit across the collision, with regulator path/order independence and the exact identity `T+ + T- = D` preserved jointly.

## Claim ceiling

This result does **not** prove:

- that the correlated product does not exist;
- that the source Feynman prescription fails;
- that no canonical extension exists;
- non-uniqueness of the final source-defined vertex;
- divergence of every channel or spin sector;
- failure of conditional/PV/distributional amplitudes;
- closure of lower K5 collision strata;
- closure of D7-S2, D7-S3 or D7-S4;
- any terminal selector `EXISTING_SUFFICIENT / ADAPT_EXISTING / HYBRID_REQUIRED / NEW_REQUIRED`.

## Frontier consequence

Authorized next analytical gate:

`SOURCE_J1_K5_JOINT_FEYNMAN_REGULATOR_EXTENSION_GATE`

It must be prospectively frozen before any substantive calculation and must separately classify:

1. existence of a joint regulated distribution for positive regulator(s);
2. existence of the regulator-removal limit in `D'`;
3. common-regulator versus independent-regulator path/order dependence;
4. collision-supported extension ambiguity;
5. preservation of the exact source identity `T+ + T- = D` at the joint level;
6. scope relative to unresolved lower collision strata / Iter461.

## Governance

- `RQIR Core v1.0 = FROZEN`.
- `D7-S2 = NOT_CLOSED`.
- `D7-S3 = NOT_CLOSED`.
- `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`.
- terminal D7 selectors remain forbidden.
- Candidate Gravity remains inactive.
- KMQGB remains downstream of pinned DSIR authority.

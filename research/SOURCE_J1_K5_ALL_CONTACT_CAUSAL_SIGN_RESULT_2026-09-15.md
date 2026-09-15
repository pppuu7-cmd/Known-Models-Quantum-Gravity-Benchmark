# Terminal result — source j=1 K5 all-contact causal-sign gate

Date: 2026-09-15
Status: `TERMINAL_SCOPED`
Classification: `SOURCE_J1_K5_ALL_CONTACT_CAUSAL_SIGN_NONCANCELLATION_SCOPED`

## Frozen authority

Prospective preregistration:

- `research/SOURCE_J1_K5_ALL_CONTACT_CAUSAL_SIGN_PREREG_2026-09-15.md`
- frozen prereg commit: `d22d456e3f978f5cbb99c76ea20df0b583eaa57c`

Exact exhaustive certificate:

- `code/source_j1_k5_all_contact_causal_sign_certificate.py`
- implementation commit: `a0dc18758c577c40550611ee28af29262615c588`

Workflow:

- `.github/workflows/source-j1-k5-all-contact-causal-sign.yml`
- launch head: `a32a741b1924186c5b65176c8b05ca5d1f99f11b`

## Authoritative run

- workflow run: `34915662486`
- source-lock job: `104212602878`, success
- exact-certificate job: `104212625339`, success
- artifact: `10376226278`
- artifact name: `source-j1-k5-all-contact-causal-sign`
- artifact digest: `sha256:00ff1b8375f8a4ef6f8553ab783b940d5786908fc4307ca835b16a142170534c`

## Exact certified result

For K5 with vertices `{1,2,3,4,5}` and all ten edges `(ab)`, every vertex has degree four. With the source causal constraint

`kappa_ab = sigma_a sigma_b`, `sigma_a in {+1,-1}`,

the exact graph identity is

`prod_{a<b} kappa_ab = prod_a sigma_a^4 = +1`.

The exhaustive certificate verified:

- exactly `10` K5 edges;
- degree vector `(4,4,4,4,4)`;
- all `32/32` vertex-sign assignments have all-edge product `+1`;
- global reversal `sigma -> -sigma` leaves the induced edge-sign pattern unchanged;
- the 32 vertex assignments induce exactly `16` distinct constrained `kappa` patterns, each with multiplicity `2`;
- all `16/16` distinct constrained patterns have edge-sign product `+1`;
- signed sum over all 32 vertex assignments = `32`;
- signed sum over the 16 distinct constrained patterns = `16`.

The frozen source `j=1` control remains nonzero for real `rho != 0`:

`delta''(B)` coefficient = `i/[rho(1+rho^2)]`.

Therefore the formal highest-contact ten-wedge `j=1` monomial cannot cancel by constrained causal signs alone.

## Adversarial independent-wedge control

For all `2^10 = 1024` independent edge-sign assignments:

- `512` have `prod_e kappa_e = +1`;
- `512` have `prod_e kappa_e = -1`;
- exact signed sum = `0`.

Thus the independent-wedge sign algebra behaves differently from the constrained causal K5 sign algebra, as required by the preregistration.

## Scientific interpretation

The result excludes one possible cancellation mechanism for the formal all-contact component:

> constrained causal-sign summation by itself cannot remove the all-ten-wedge highest `j=1` contact monomial.

Any removal, canonical definition, or cancellation of the collision contact sector must therefore arise from some other source-faithful mechanism, such as:

- the joint Feynman-regulator/extension prescription;
- channel/intertwiner contraction;
- integration identities;
- collision-supported normalization conditions;
- or another explicitly proved structural cancellation.

This complements the already terminal scoped facts that ordinary local absolute Haar integrability fails for a fixed nonzero channel witness and that the standard Hörmander sufficient multiplication criterion fails at an explicit source-present contact triangle witness.

## Claim ceiling

This result is exact **sign combinatorics only**. It does not prove:

- that the formal ten-fold product `prod_e delta''(B_e)` exists as a distribution;
- that this formal contact monomial survives every channel contraction;
- that the full vertex diverges as a distribution;
- that the source Feynman prescription fails to select a canonical joint extension;
- failure of conditional/PV/distributional amplitudes;
- closure of lower K5 collision strata;
- closure of D7-S2, D7-S3 or D7-S4;
- any terminal selector `EXISTING_SUFFICIENT / ADAPT_EXISTING / HYBRID_REQUIRED / NEW_REQUIRED`.

## Frontier consequence

The authorized analytical frontier remains:

`SOURCE_J1_K5_JOINT_FEYNMAN_REGULATOR_EXTENSION_GATE`.

The bare constrained sign sum is no longer an admissible explanation for removing the frozen all-contact component. The joint-regulator gate must instead determine whether the source Feynman construction supplies a well-defined correlated distributional extension and whether that construction is unique/path-independent.

## Governance

- `RQIR Core v1.0 = FROZEN`.
- `D7-S2 = NOT_CLOSED`.
- `D7-S3 = NOT_CLOSED`.
- `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`.
- terminal D7 selectors remain forbidden.
- Candidate Gravity remains inactive.
- KMQGB remains downstream of pinned DSIR authority.

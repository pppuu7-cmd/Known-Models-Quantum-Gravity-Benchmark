# SOURCE_J1_K5_SCALAR_FOREST_OPERATOR_PILOT — terminal result

Date: 2026-09-15
Status: TERMINAL

## Authority

- Gate: `SOURCE_J1_K5_SCALAR_FOREST_OPERATOR_PILOT`
- Frozen preregistration: `research/prereg/SOURCE_J1_K5_SCALAR_FOREST_OPERATOR_PILOT_2026-09-15.md`
- Preregistration commit: `1bd587addf78876675ca8260900a8c1735943989`
- Implementation commit: `198728e432162a8304348bc2df9e9b7a65ab8fb1`
- Workflow head: `fd8124c54864d67d1762e3309215ae4706268b2e`
- Authoritative run: `34991261044`
- Source-lock job: `104456207169` — success
- Python 3.11 job: `104456369046` — success
- Python 3.12 job: `104456369018` — success
- Python 3.11 artifact: ID `10405443732`, digest `sha256:e1e97f0b38792dc4fd70ac4e8951012a768b547a8e60bdfae95711ce875afdb1`
- Python 3.12 artifact: ID `10405468629`, digest `sha256:1d06670df19fe42b835f21c9dbfd743159f2890e7873829ccb57ddaf07aba97a`

## Frozen terminal classification

`SCALAR_K5_FOREST_OPERATOR_PILOT_CONFIRMED_SCOPED`

Both independent Python lanes emitted the same exact scientific payload and the same deterministic operator-specification digest:

`sha256:c3e0ca0c5a5357887db79b7b0a1c5a0a1042c450ca13f7e2599c7e3801ef8a9c`.

## Exact operator certificate

The KMQGB-derived auxiliary scalar operator is now fully defined:

- gauge: `q_0=0`, `x=(q_1,q_2,q_3,q_4)`;
- `C_S`: full-coordinate barycentric collapse on `S`, followed by re-gauging;
- `N_S=I-C_S`;
- `Gamma_S(lambda)=C_S+lambda N_S`;
- `T_S^r`: Taylor projector through order `r` in the normal-scaling parameter at `lambda=0`;
- scalar proper-stratum orders `{2:2,3:7,4:15}`;
- separate full-root order `26`;
- proper forest operator `W_prop=sum_F (-1)^|F| T_F` over the exact 236 proper-only forests;
- full operator `W_full=(I-T_V^26) W_prop`.

This is a KMQGB-derived barycentric Taylor forest prescription for the auxiliary scalar Gaussian witness only. It is not claimed source-authorized or unique.

## Exact controls

All frozen controls passed.

### Geometry / gauge

- every collapse matrix is exactly idempotent;
- exact ranks are `rank(C_S)=5-|S|`, so normal dimensions are `|S|-1`;
- full collision has `C_V=0`, `N_V=I`;
- all 120 S5 covariance checks pass modulo the fixed gauge;
- deliberately label-dependent anchored collapse fails S5 covariance as required.

### Laminar algebra

- proper subsets: `25`;
- laminar unordered subset pairs: `105`;
- all 105 have commuting collapse and symbolic `Gamma` coefficient matrices;
- overlapping nonnested pairs: `195`;
- all 195 fail the commutation condition and are excluded;
- nested collapses satisfy exact parent absorption `C_T C_S=C_S C_T=C_T` for `S proper subset T`.

### Taylor-order controls

For every internal vertex pair `a,b in S`, the exact normal linear form `ell_ab=q_a-q_b` satisfies

`ell_ab C_S=0`, `ell_ab N_S=ell_ab`,

hence `ell_ab(Gamma_S(lambda)x)=lambda ell_ab(x)`.

This was checked over 80 subset/internal-pair records and used for 320 exact Taylor fixtures. Degree `m<=r` normal monomials are captured by `T_S^r`, while degree `r+1` survives `(I-T_S^r)` as required.

### Forest topology

- proper-only forests including empty: `236`;
- histogram `{0:1,1:25,2:105,3:105}`;
- S5 orbits: `12`;
- orbit-size histogram `{1:1,5:1,10:3,15:2,20:1,30:3,60:1}`.

## Consequence

The operator-definition blocker is closed. A corrected numerical P1 forest-subtraction gate is now authorized, provided it consumes this exact operator digest and does not reuse the superseded three-normal-dimensional order table or the invalidated historical P3 divergence premise.

## Interpretation ceiling

This gate defines and validates the operator algebra only. It does not establish post-subtraction convergence/divergence, Eq. (4) existence/nonexistence, source authorization, uniqueness, model/family failure, D7 closure, a terminal selector, or Candidate Gravity activation.

## Next admissible gate

Prospectively freeze an optimized numerical P1 witness gate on the robust Critic-confirmed P1 realization. The efficient first diagnostic should:

- use the exact operator spec digest above;
- use the stable P1 test point `alpha=0.55` as a frozen divergence/stabilization witness;
- use at least four successive P1 scale points;
- exploit the exact S4 symmetry of P1 only after independently certifying orbit reduction against the full 236-forest formula on a cheap fixture;
- include two precision lanes and explicit lost-digit/cancellation accounting;
- classify numerical/resource failure as BLOCKED rather than scientific FAIL.

Governance remains unchanged: RQIR Core v1.0 frozen; D7-S2/S3 not closed; D7-S4 partial; terminal selectors forbidden; Candidate Gravity inactive; KMQGB downstream of pinned DSIR authority.
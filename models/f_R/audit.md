# Model Audit — metric f(R) / R+R^2 Minkowski scalaron control

Benchmark ID: KMQGB-M05-FR
Concrete realization ID: FR-R2-MINK-001
Role: extra-scalar / modified-gravity control
State: TERMINAL
Terminal status: OPERATIONALLY_DEGENERATE

## Frozen action

Use four-dimensional metric f(R) gravity

`S = (M_Pl^2/2) ∫ d^4x sqrt(-g) [ R + R^2/(6 M^2) ] + S_m[g,psi]`,

with `M^2 > 0`, expanded about Minkowski spacetime and coupled minimally to a conserved matter stress tensor.

For `f(R)=R+R^2/(6M^2)`, `F=df/dR=1+R/(3M^2)` and `f_RR=1/(3M^2)>0`. At Minkowski, `F(0)=1>0`. The declared weak-field spectrum is the usual massless GR spin-2 sector plus one scalaron of mass `M`; pure `R^2` adds no massive spin-2 ghost pole.

## Frozen calibration-resistant C0 observable

Use weak-field potentials

`ds^2=-(1+2Phi)dt^2+(1-2Psi)dx^2`.

For a localized nonrelativistic traceful source,

`Phi(r)=-G m_s/r [1+(1/3)e^{-Mr}]`,

`Psi(r)=-G m_s/r [1-(1/3)e^{-Mr}]`.

Therefore

`gamma_fR(r)=Psi/Phi=(3-e^{-Mr})/(3+e^{-Mr})`.

C0/GR predicts `gamma_GR=1`, so

`Delta_gamma^C0(r)=-2e^{-Mr}/(3+e^{-Mr})`.

Common source mass, Newton constant and `1/r` normalization cancel exactly. The residual is nonzero for finite `Mr`, tends to zero for `Mr -> infinity`, and tends to `-1/2` for `Mr -> 0`.

The radial shape obeys

`ln[3(1-gamma)/(1+gamma)]=-Mr`.

Thus the raw C0/source-amplitude quotient is passed analytically.

## Broader scalar/Yukawa quotient — exact degeneracy

Define the admissible one-scalar Yukawa comparator family in the same weak-field observable by

`Phi_Y(r)=-G_N m_s/r [1+alpha exp(-m r)]`,

`Psi_Y(r)=-G_N m_s/r [1-alpha exp(-m r)]`,

so

`gamma_Y(r)=[1-alpha exp(-m r)]/[1+alpha exp(-m r)]`.

Massive scalar-tensor gravity generically produces distance-dependent PPN gamma/Yukawa behavior. The metric-f(R) realization is the exact special point

`alpha = 1/3`, `m = M`.

Hence for every radius in the frozen weak-field domain,

`gamma_Y(r; alpha=1/3,m=M) = gamma_fR(r;M)`.

Consequently the comparator-profiled residual in this observable is exactly

`Delta_gamma^(scalar/Yukawa quotient)(r)=0`.

This is stronger than a one-radius amplitude degeneracy: the entire multi-radius exponential shape is absorbed by the two-parameter scalar/Yukawa family.

## Representation identity versus operational degeneracy

Two facts are kept separate:

1. Metric f(R) is dynamically equivalent to a scalar-tensor representation with `omega_BD=0` plus the mapped scalar potential. That is an exact field/representation identity.
2. A broader scalar/Yukawa model can reproduce the frozen `gamma(r)` response by parameter matching. That is an operational observable degeneracy even when the underlying theory is not literally the same f(R) action.

KMQGB therefore assigns `OPERATIONALLY_DEGENERATE`, not `EXACT_COMPARATOR_IDENTITY` and not `FAIL_RQIR_CONSISTENCY`.

## F0–F7 terminal map

| Gate | State | Reason |
|---|---|---|
| F0 — dynamics | PASS_SCOPED | exact local metric action frozen |
| F1 — required limits | PASS_SCOPED | GR recovered for scalaron decoupling / `Mr >> 1` |
| F2 — consistency | PASS_SCOPED_AROUND_MINKOWSKI | `F(0)>0`, `f_RR>0`, `M^2>0`; no extra massive spin-2 ghost from pure `R^2` |
| F3 — RQIR hierarchy | CLASSICAL_PARTIAL | classical mean/retarded response exists; no independent QG operator/noise hierarchy |
| F4 — comparator distinction | FAIL_TO_DISTINGUISH_AFTER_BROADER_QUOTIENT | nonzero versus C0, exact degeneracy with scalar/Yukawa family in frozen observable |
| F5 — hard discriminator | NOT_PROMOTED | F4 uniqueness fails for the frozen gamma channel |
| F6 — statistical identifiability | NOT_PROMOTED | exact comparator shape degeneracy leaves no unique model direction in this channel |
| F7 — physical resources | NOT_PROMOTED | forbidden after earlier non-identifiability |

## Q1–Q7 fingerprint

- Q1: modified classical proper-time/metric response only.
- Q2: no branch-resolved quantum geometry.
- Q3: classical trace-source/backreaction modification through the scalaron.
- Q4: no quantum-mediator certificate.
- Q5: extra classical scalar curvature degree of freedom, not intrinsic quantum metric noise.
- Q6: causal classical retarded response in the declared weak-field theory.
- Q7: not standard C5 quantized-GR EFT; low-q expansion overlaps higher-curvature structures, but uniqueness already fails at the scalar/Yukawa quotient.

## Scientific interpretation

`FR-R2-MINK-001` is healthy in the declared weak-field Minkowski domain and gives a genuine finite deviation from GR. The benchmark nevertheless refuses to promote that deviation as a unique model discriminator because a broader scalar/Yukawa class reproduces the entire frozen `gamma(r)` shape exactly.

This is not evidence that f(R) gravity is inconsistent. It is evidence that `gamma(r)` alone cannot identify this f(R) realization uniquely.

## Sources

1. A. De Felice and S. Tsujikawa, *f(R) Theories*, Living Reviews in Relativity 13, 3 (2010).
2. M. Hohmann et al., *Post-Newtonian parameter gamma for multiscalar-tensor gravity with a general potential*, arXiv:1607.02356 — distance-dependent exponential gamma in massive scalar-tensor theories.
3. Standard scalar-tensor/Brans-Dicke PPN relation and coupling normalization `alpha_0^2=1/(2 omega_BD+3)` as summarized in Living Reviews tests of gravity.
4. External RQIR comparator authority: `candidate_gravity/BASELINE_COMPARATORS.md`, blob `a2b45188710c885f979123f77fa7aad2273b9983`.
5. External RQIR funnel authority: `candidate_gravity/landscape/RQIR_FUNNEL_AUDIT_ITERATION137.md`, blob `2757e8fe1004b5c0caef51d6d9fee6f982ac81d4`.

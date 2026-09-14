# Iter499 preregistration — direct Arb max-envelope interval gate

Date frozen: 2026-09-14
Status: **FROZEN BEFORE IMPLEMENTATION / PRODUCTION**

## Parent authority and reason for this gate
Iter498 is terminal `ITER498_MAX_ENVELOPE_NONSMOOTH_BLOCKER_IDENTIFIED_SCOPED`.

Authoritative parent provenance:
- Iter498 prereg `0bedcbaf7b065b050585f2a3505c8bf0e2a14457`;
- evaluator `2148981be0a808094cd0b4b1b80d2e65fd586807`;
- aggregate `432773c916872f6300a2c0e4d56872318eaa03bd`;
- wording-only source-lock repair head `2bc6756dffdbf10b2d70bdf174657f7f2d478864`;
- authoritative run `34816799788`;
- aggregate job `103890003162`;
- aggregate artifact `10337025880`;
- digest `sha256:65851b593dfdc385969e4da67a9e9aa992f328f801521798d2a8c05e349ed814`.

Iter498 found exactly two maximizing-channel switches in the frozen sampled audit. Both are in `0to5-b0`, direction `[1,1,1,-1,-1,-1]`, sign `+1`, rho `2.7`, between amplitudes `0.00234375` and `0.00250`, at R=10 and R=12; channel `195=(2,1,0,2,0)` switches to `222=(2,2,0,2,0)`. The minimum positive KAK beta is `0.5017347792114244`, so the diagnosed blocker is the finite max-envelope, not a near-degenerate KAK branch.

Therefore Iter499 must **not** differentiate one selected argmax channel and must **not** substitute a denser point mesh for a continuum certificate. It will evaluate a validated ball enclosure of the full finite max over all 243 genuine intertwiner channels.

## Frozen mathematical target
For every frozen causal class, direction, sign and rho, define amplitude `a` and q=1 perturbation

`eps_R(a) = a * exp(-R)`

with `R in {6,8,10,12}` and the same source-faithful shared-node geometry as Iter492-498.

Let `C_I(R,a,rho)` be the **unnormalized** fully contracted ten-edge j=1 magnetic/intertwiner network for channel `I in {0,1,2}^5`, using the source Toller branch on every edge. The existing normalized implementation satisfies identically

`(product_e n_e) * Contract_I(M_e/n_e) = Contract_I(M_e)`,

so Iter499 uses the raw Toller matrices directly and introduces no new amplitude or weight.

Define

`Cmax(R,a,rho) = max_I |C_I(R,a,rho)|`,

`Y_R(a,rho) = log H_R(a) + log Cmax(R,a,rho)`,

where `H_R` is the same source radial Haar density used in Iter486 onward.

Because the R grids are equally spaced, the frozen least-squares slopes reduce exactly to

`S(a,rho) = [Y_12(a,rho)-Y_8(a,rho)]/4`,

`E(a,rho) = [Y_10(a,rho)-Y_6(a,rho)]/4`,

and drift is `D(a,rho)=|S-E|`.

The continuum target on this gate is:

`S >= 0` and `D <= 0.05`

for every amplitude in the frozen interval and every frozen state. Robust margin `S >= 1` is recorded separately but is not required for the base NONDECAY certificate.

## Frozen state space
Exactly the Iter495-498 q=1 state space is retained:
- active coordinates `[0,1,3,5,6,11]` in the 20-D chart;
- directions
  1. `[1,1,1,1,1,1]`
  2. `[1,1,1,-1,-1,-1]`
  3. `[1,-1,-1,1,1,-1]`
  4. `[1,-1,1,-1,1,-1]`
  5. `[1,1,-1,1,-1,-1]`
  6. `[1,-1,1,1,-1,1]`
  7. `[1,1,-1,-1,1,1]`
  8. `[1,-1,-1,-1,-1,1]`;
- both signs `+1,-1`;
- causal classes `0to5`, `1to4`, `2to3`;
- rho witnesses `{0.35,0.9,1.6,2.7}`;
- `R={6,8,10,12}`;
- j=1 and the exact five-node intertwiner basis inherited from Iter481 onward.

No direction, rho, R value, sign or causal class may be removed after production.

## Frozen interval cover
The full amplitude interval is exactly

`A=[0.00125,0.00250]=[1/800,1/400]`.

It is covered by exactly **16 closed rational boxes**

`A_k=[(16+k)/12800,(17+k)/12800]`, `k=0,...,15`.

Adjacent endpoint overlap is intentional and the union is exactly A. No adaptive subdivision, endpoint shift, box deletion or box insertion is allowed after production evidence is observed.

The 16-box choice is fixed prospectively after the Iter498 diagnosis: each box has half the width of the final Iter498 mesh spacing, so the known crossing region is covered by multiple validated boxes while the method remains a continuum enclosure, not a sample grid.

## Frozen validated arithmetic backend
Production arithmetic is pinned to:
- CPython 3.12;
- `python-flint==0.9.0`;
- Arb/Acb ball arithmetic at exactly `ctx.prec=384` bits for the scientific enclosure.

No higher precision may be used to tighten a scientifically inconclusive interval in this iteration. Failure of the 384-bit validated construction is a numerical-method outcome, not permission to alter boxes or thresholds.

All decimal constants inherited from previous frozen Python objects are lifted from `repr(float_value)` strings. Rational interval endpoints and rational intertwiner coefficients are constructed exactly as rationals, not through binary floats.

## Frozen 2x2 KAK ball construction
No SVD black box is required. For each node/edge ball matrix `h`, form the Hermitian positive matrix `H=h^dagger h` in explicit 2x2 Hermitian form

`H=[[a,c],[conj(c),d]]`.

Define using Arb/Acb operations

`t=(a+d)/2`, `delta=(a-d)/2`, `r=sqrt(delta^2+|c|^2)`,
`lambda_plus=t+r`, `lambda_minus=t-r`.

Required whole-box predicates:
1. `lower(lambda_minus)>0`;
2. `lower(lambda_plus-lambda_minus)>0`;
3. the selected eigenvector chart has norm lower bound `>1e-30`.

Two algebraically equivalent high-eigenvector charts are allowed and frozen:
- `w_A=(c, lambda_plus-a)`;
- `w_B=(lambda_plus-d, conj(c))`.

For each box choose the chart whose validated norm lower bound is larger. This deterministic chart selection uses only interval conditioning and is not a science-result-dependent branch. If both norm lower bounds are `<=1e-30`, the box is numerical-method invalid.

Normalize the selected vector to `v`; construct its SU(2) complement exactly as `(-conj(v_2),conj(v_1))`; set `V=[v,Jv]`, `U2=V^dagger`,

`beta=(log(lambda_plus)-log(lambda_minus))/2`,
`A=diag(exp(beta/2),exp(-beta/2))`,
`U1=h V A^{-1}`.

The production record must validate by ball containment:
- KAK reconstruction `0 in U1*A*U2-h` entrywise;
- `0 in U1^dagger U1-I` and `0 in U2^dagger U2-I` entrywise;
- `1 in det(U1)` and `1 in det(U2)`;
- `lower(beta)>0`.

A failure is `ITER499_NUMERICAL_METHOD_BLOCKER`, not scientific FAIL.

## Frozen source Toller ball object
Use the exact j=1 Appendix-B/Ruehl branch formulas already source-locked by Iter456 and propagated through Iter484-498, evaluated with Arb/Acb functions at ball beta and exact frozen rho.

For each m in `{-1,0,+1}` compute `D_m,T+_m,T-_m`; require the reduced additive identity `0 in T+_m+T-_m-D_m` for every edge/box/rho.

Lift to the full magnetic matrix with the same canonical spin-1 symmetric-square convention as Iter484:

`T_branch(h)=D^1(U1) diag(T_branch,m(beta,rho)) D^1(U2)`.

No polar replacement, representation-composition law, determinant projection, fitted rescaling, contour change or extra damping is allowed.

## Exact intertwiner arithmetic
The five-node intertwiner tensors must be built from exact rational coefficients, not the prior floating SymPy evaluation. The nonzero coefficient sets are exactly those of the existing `intertwiner(i)` definitions; for j=1 they reduce to rationals:
- i=0: only `+/- 1/3`;
- i=1: only `+/- 1/6`;
- i=2: only `1/5,-1/10,1/30,1/15,2/15` with the existing magnetic supports/signs.

An initialization control must compare all 3x81 exact-rational tensor entries against the existing floating tensors and require maximum absolute difference `<1e-15`.

## Direct 243-channel contraction
The network must retain **all 243** channels. Implementation may stack the three intertwiner tensors at each node and contract once to a `3x3x3x3x3` Acb tensor, but it may not drop a channel based on point samples.

For every R/rho/box:
- obtain an Acb enclosure for every `C_I`;
- define `L_I=abs_lower(C_I)` and `U_I=abs_upper(C_I)`;
- define envelope bounds `L=max_I L_I`, `U=max_I U_I`;
- require `L>0` and all balls finite;
- record the validated possible-max set `{I: U_I >= L}`. Channels with `U_I<L` are whole-box excluded from being maximizers; this is diagnostic only because the envelope itself always uses all 243 channels.

Then `log Cmax` is enclosed by `[log L,log U]`. Combine with the Arb Haar log-density ball to obtain `[Y_R^L,Y_R^U]`.

Frozen slope bounds for each amplitude box are

`S_L=(Y12_L-Y8_U)/4`, `S_U=(Y12_U-Y8_L)/4`,
`E_L=(Y10_L-Y6_U)/4`, `E_U=(Y10_U-Y6_L)/4`.

The rigorous drift upper bound is

`D_U=max(|S_L-E_U|,|S_U-E_L|)`.

No covariance/correlation cancellation between R values is assumed; this intentionally conservative interval combination remains valid when dependencies are lost.

## Frozen implementation controls
Every production lane must pass:
1. exact 16-box cover endpoints and adjacency;
2. finite Arb/Acb values;
3. positive/separated KAK eigenvalues and selected eigenvector norm margin;
4. KAK reconstruction/unitarity/determinant containment predicates above;
5. source reduced additive identity containment;
6. exact-rational intertwiner regression `<1e-15`;
7. direct full 243-channel envelope with `L>0`;
8. center/source regression at the nine already-frozen Iter498 amplitudes `{0.00125,0.00140625,0.0015625,0.00171875,0.001875,0.00203125,0.0021875,0.00234375,0.00250}`: point slopes from the existing high-precision q=1 evaluator must lie inside the corresponding adjacent validated box slope enclosures, with endpoint membership accepted in either/both adjacent boxes;
9. the known Iter498 crossing anchor (`0to5`, direction 2, sign +, rho 2.7) must not be forced into a single argmax branch; the possible-max diagnostics in boxes intersecting `[0.00234375,0.00250]` must remain computed from all 243 channels.

No control threshold may be weakened after production.

## Frozen matrix
Exactly `3 causal classes x 4 direction blocks = 12` independent GitHub Actions jobs, `fail-fast:false`, `max-parallel:12`.

Each job covers its two directions, both signs, all 16 boxes, four rho witnesses and four R values. Aggregate must consume all 12 raw artifacts and verify all expected job ids are present exactly once.

## Frozen classifier
Per amplitude box and state:
- `INTERVAL_ROBUST_NONDECAY` iff all controls pass, `S_L>=+1.0` and `D_U<=0.05`;
- `INTERVAL_NONDECAY` iff all controls pass, `S_L>=0.0` and `D_U<=0.05` but robust margin is not certified;
- `INTERVAL_UNIFORM_DECAY_WITNESS` iff all controls pass, `S_U<=-0.10` and `D_U<=0.05`;
- otherwise `INTERVAL_INCONCLUSIVE` if the validated construction is finite but the frozen science predicates cannot be decided;
- any arithmetic/source/KAK/containment failure -> `ITER499_NUMERICAL_METHOD_BLOCKER`.

Aggregate:
1. `ITER499_DIRECT_MAX_ENVELOPE_INTERVAL_ROBUST_QUALIFIED_SCOPED` iff every frozen box/state is `INTERVAL_ROBUST_NONDECAY`;
2. `ITER499_DIRECT_MAX_ENVELOPE_INTERVAL_NONDECAY_QUALIFIED_SCOPED` iff every box/state is at least `INTERVAL_NONDECAY` and at least one misses robust margin;
3. `SCIENTIFIC_FAIL_ITER499_UNIFORM_NONDECAY_INTERVAL` iff controls are valid and at least one box is a validated `INTERVAL_UNIFORM_DECAY_WITNESS`;
4. `ITER499_VALIDATED_INTERVAL_INCONCLUSIVE_SCOPED` iff all arithmetic/source controls are valid but neither PASS nor uniform-decay witness is certified because at least one box straddles a frozen threshold;
5. `ITER499_NUMERICAL_METHOD_BLOCKER` iff any required validated construction/control fails.

A PASS is a continuum certificate **only along the 16 frozen one-dimensional signed direction intervals**. It does not prove a six-dimensional angular box, a 20-D positive-measure neighborhood, or an absolute Haar theorem.

## Interpretation ceiling and next-step lock
- PASS authorizes a subsequent prospectively frozen multidimensional angular-box certificate attempt.
- VALIDATED_INTERVAL_INCONCLUSIVE authorizes only a new numerical-analysis gate; no post-hoc box refinement belongs to Iter499.
- NUMERICAL_METHOD_BLOCKER authorizes only the minimal enabling validated-arithmetic repair.
- SCIENTIFIC_FAIL means the q=1 frozen uniform-NONDECAY interval claim is false on at least one validated subinterval; do not rescue by changing q, amplitudes, directions or thresholds inside this iteration.

Ten source spectral integrations, Iter461 K5 collision geometry, PV/conditional/distributional boundary values, D7-S3/S4, terminal D7 labels and Candidate Gravity remain separate and unpromoted.

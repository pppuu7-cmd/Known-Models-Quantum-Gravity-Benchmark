# Iter491 preregistration — high-precision source-group re-evaluation of frozen Iter490 angular thickening

Date frozen: 2026-09-14
Status: FROZEN BEFORE IMPLEMENTATION/PRODUCTION

## Parent authority
- One-dimensional parent science authority: `SCIENTIFIC_FAIL_ITER487_HAAR_ESCAPE_ACTUAL_ENVELOPE_REVALIDATED_BY_ITER489`.
- Iter490 terminal result: `INFRASTRUCTURE_OR_NUMERICAL_FAIL_ITER490`.
- Iter490 result note: `results/ITER490_ANGULAR_NEIGHBORHOOD_THICKENING_RESULT_2026-09-14.md`.
- Iter490 aggregate artifact `10328343195`, digest `sha256:a45c55bd93095f61e0aaa9b79f4ea4810e7f54b8fb07c9a13c895fe8dffc9d58`.

Iter490 produced all 12 frozen angular lanes but every lane was invalid because an absolute KAK reconstruction test was applied after large, ill-conditioned relative edge matrices had already been rounded to double precision. Post-verdict diagnostics show max-entry scales up to about `1e4`, edge determinant drift of order `1e-9`, and absolute KAK residuals of order `1e-5` while relative matrix error remains of order `1e-9`. Those diagnostics do not validate Iter490 and do not authorize use of its raw slopes.

## Target hypothesis
The frozen Iter490 angular object can be evaluated without the double-conditioning ambiguity if the **same frozen group parameters** are lifted to high precision before constructing the `SL(2,C)` node/edge matrices and before KAK decomposition. If this source-object reconstruction is valid and precision-stable, then the unchanged Iter490 sampled-thickening science classifier may be applied prospectively to the newly evaluated lanes.

This gate is allowed to return a genuine angular-thickening scientific FAIL. It is not a rescue gate for the one-dimensional NONDECAY witness.

## Frozen scientific object — unchanged from Iter490
- panel `C`, strong regime;
- cluster size `s=4`, nodes 1..4 escaped together;
- `j=k=l=1` full ten-edge Toller/intertwiner network;
- rho witnesses `{0.35,0.9,1.6,2.7}`;
- causal patterns `{0to5,1to4,2to3}`;
- radial grid `R={6,8,10,12}`;
- angular radii `eps={0.0025,0.005,0.01,0.02}`;
- exact same 16 deterministic 20-D perturbation vectors per radius as Iter490, with RNG seed `490000 + 1000*radius_index + sample_index` and the same Rademacher/interior split;
- same 20-D chart `g_a(delta;R)=L_a(delta_L) g_a^0(R) R_a(delta_R)` with `L=Rx Ry Rz`, `R=Rx Ry`;
- all 243 genuine `3^5` four-valent intertwiner channels;
- same source radial Haar factor;
- 12 lanes = 3 causal patterns x 4 radii, `fail-fast:false`.

No radius, sample, seed, causal pattern, rho, R point, boundary channel or slope threshold may be changed after production.

## Frozen parameter-lift rule
The mathematical source object is fixed by the already-committed Iter490 numeric parameters. High precision must not reinterpret those numbers.

For every scalar parameter used by the original double implementation:
1. first form any composite parameter in the same double operation as Iter490/Iter483 (for example `-0.37*g`, `0.73*t`, `0.41*a`, and `v_i*eps`);
2. freeze that resulting Python float by `repr(float(x))`;
3. lift that decimal string to `mpmath.mpf`;
4. evaluate trigonometric/exponential functions and all node products/inverses at the requested high precision.

This rule makes high precision a re-evaluation of the same frozen parameter point, not a new chart or a new sample.

## Frozen numerical realization
Primary production precision: **100 decimal digits**.

For each sample and R:
1. construct all five node matrices at 100 digits;
2. construct all ten relative edges `h_ab=g_b^{-1}g_a` at 100 digits;
3. perform KAK/SVD at 100 digits on those high-precision edge matrices;
4. only after KAK is obtained may the bounded SU(2) factors and beta be converted to double for the already-qualified Iter484/485 spin-1 Toller magnetic evaluation and the existing normalized 243-channel contraction;
5. source Haar rapidities are taken from the high-precision node KAK values.

No determinant projection, scalar renormalization, fitted phase adjustment, polar-factor substitution or post-hoc matrix repair is allowed.

## Frozen source-object and precision controls
Every lane is invalid if any required control fails.

A. high-precision node determinant residual `<1e-50` for every node/sample/R.

B. high-precision relative-edge determinant residual `<1e-50` for every edge/sample/R.

C. high-precision KAK absolute reconstruction residual `<1e-50` for every edge/sample/R.

D. high-precision KAK SU(2) controls: unitarity and determinant residuals `<1e-50` for both compact factors.

E. high-precision shared-node K5 cycle residual `<1e-50` for every sample/R.

F. frozen source-object identity: after converting the 100-digit edge matrix to complex128, compare it with the original Iter490 double-constructed edge matrix at the same frozen parameters. Require
`max|h_hp_to_double-h_iter490| / max(1,max|h_hp_to_double|) < 1e-9`
for every edge/sample/R. This is an identity/control check, not the KAK validation metric.

G. independent precision convergence anchor: for sample 0 at `R=12` in every radius lane, reconstruct all ten edge matrices and KAK betas independently at 80 and 120 decimal digits. Require maximum relative edge-matrix difference `<1e-20` and maximum absolute beta difference `<1e-20`.

H. chart tangent ranks remain exactly `[5,5,5,5]` under the unchanged Iter490 finite-difference chart-rank control.

I. center regression: the unperturbed center must reproduce the four frozen parent C-s4 slopes for the selected causal pattern within absolute error `<5e-3`.

J. full scientific-evaluation regressions: all contractions finite and strictly positive; source additive residual `<1e-9`; Haar slope within `0.05` of `+8`; Haar bookkeeping residual `<1e-8`.

## Frozen observables and classifier — unchanged from Iter490
For every valid perturbed `(sample,rho)`:
- `C_max(R,rho)=max_I |C_I|` over all 243 channels;
- `log H(R)` from actual high-precision KAK node rapidities;
- `log E=log C_max+log H`;
- network/Haar/actual slopes on `R={8,10,12}`;
- early actual slope on `{6,8,10}`;
- slope drift = absolute difference of those actual-slope fits.

State predicates:
- `NONDECAY` iff `actual_slope >= 0.00` and drift `<=0.05`;
- `ROBUST` iff `actual_slope >= +1.00` and drift `<=0.05`.

Per lane:
1. `ITER491_SAMPLED_ROBUST_THICKENING_LANE` iff all 16 perturbed samples x 4 rho witnesses are ROBUST;
2. `ITER491_SAMPLED_NONDECAY_THICKENING_LANE` iff all 64 points are NONDECAY but at least one misses the +1 robust margin;
3. `SCIENTIFIC_FAIL_ITER491_ANGULAR_THICKENING_HP` iff the lane is valid and at least one point is not NONDECAY;
4. `INFRASTRUCTURE_OR_NUMERICAL_FAIL_ITER491` iff any required control fails.

Aggregate:
- `ITER491_FULL_ANGULAR_SAMPLED_ROBUST_THICKENING_QUALIFIED_SCOPED` iff at least one frozen radius has all three causal lanes classified ROBUST;
- else `ITER491_FULL_ANGULAR_SAMPLED_NONDECAY_THICKENING_QUALIFIED_SCOPED` iff at least one frozen radius has all three causal lanes NONDECAY, reporting the largest such frozen radius;
- else `SCIENTIFIC_FAIL_ITER491_ANGULAR_THICKENING_HP` iff all 12 lanes are valid and no frozen radius has all three causal lanes NONDECAY;
- else `INFRASTRUCTURE_OR_NUMERICAL_FAIL_ITER491`.

## Interpretation ceiling
A ROBUST/NONDECAY aggregate is still a **finite deterministic sampled** result in a locally full-rank 20-D chart. It does not prove a uniform lower bound over an open neighborhood and does not establish an absolute Haar-divergence theorem. It would only authorize a later prospective boundary/interval/Lipschitz-style neighborhood certificate.

A scientific FAIL means the four prospectively frozen radii and samples do not support the sampled-thickening hypothesis. It does not prove that no smaller nonzero neighborhood exists; shrinking the radius below `0.0025` after seeing the result is forbidden within Iter491 and would require a new separately motivated prospective gate.

Ten source spectral integrations, conditional/PV cancellations, correlated boundary-value/distributional amplitudes, and the physical causal vertex remain separate. D7-S2 remains NOT_CLOSED. No terminal D7 label or Candidate Gravity authorization is permitted.
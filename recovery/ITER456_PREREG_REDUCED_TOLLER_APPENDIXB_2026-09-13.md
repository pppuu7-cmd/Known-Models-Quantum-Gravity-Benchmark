# Iter456 preregistration — source-faithful reduced Toller Appendix-B qualification

Date frozen: 2026-09-13
Status: preregistered before implementation/production.

## Scientific objective
Qualify a first source-faithful reduced Toller `t`-matrix implementation under the published Rühl phase convention using only the explicit closed forms in Bianchi–Chen–Gamonal, arXiv:2601.23162v1, Appendix B, for the pure boost sector `k=j=l=1`, `m=-1,0,+1`.

This is a prerequisite to an Eq.(7) magnetic reconstruction gate. It is not a full causal-vertex or convergence gate.

## Frozen source objects
For each `m in {-1,0,+1}` implement independently the published analytic expressions for
- `d^(rho,1)_{11m}(beta)`,
- `t^(+,rho,1)_{11m}(beta)`,
- `t^(-,rho,1)_{11m}(beta)`,
with `beta>0` and the Rühl phase convention stated in Appendix A/B.

No coefficient fitting, interpolation, learned correction, or phase retuning is permitted.

## Frozen numerical panels
- precision: 80 decimal digits
- beta panel: `[0.35, 0.8, 1.2, pi/2, 2.1]`
- real-rho panel: `[-3.4,-2.3,-1.7,-0.6,0.35,0.9,1.6,2.7,3.8]`
- pole displacement scales: `[1e-8,1e-12,1e-16,1e-20,1e-24]`
- source pole locations determined by `i*rho in {-1,0,+1}`.
- matrix lanes: one lane per magnetic index `m=-1,0,+1`, plus one independent cross-check lane that evaluates all three with an algebraically separate formula organization.

## Frozen predicates
A lane is scientifically valid only if all evaluations are finite away from the source poles and the negative controls are active.

1. **Additive recovery**: for every real-panel point, `t_plus + t_minus = d`. Frozen tolerance: absolute residual `<= 1e-45 + 1e-40*|d|`.
2. **Independent formula agreement**: direct transcription and independently reorganized evaluation must agree for each of `d,t+,t-` within `1e-42 + 1e-38*|value|`.
3. **Source pole locations**: no off-source singularity is permitted on the preregistered imaginary-axis scan; candidate singularities must map to `i*rho=-1,0,+1` within `1e-30`.
4. **Simple-pole scaling**: for every branch/magnetic/source-pole pair whose analytic numerator is nonzero at the pole, `(rho-rho0)*t` must converge to a finite nonzero residue and the local log-log divergence slope of `|t|` versus displacement must converge to `-1`. Frozen slope error `<=5e-6`; relative residue drift across the last three scales `<=5e-6`. Pairs with an analytically vanishing numerator are recorded as removable cancellations and are not relabeled as failures.
5. **Branch-sum stability near poles**: at symmetric off-pole points, cancellation in `t+ + t-` must recover finite `d` with relative/absolute residual `<=1e-30` for the last three displacement scales where conditioning permits 80-dps evaluation.
6. **Wrong-phase negative control**: flip the source phase factor in exactly one Toller branch. It must violate additive recovery by `>1e-8` at at least 80% of the real-panel points in every affected magnetic lane.
7. **Wrong-pole negative control**: shift one denominator factor so the nominal pole set is displaced by `0.1 i`; the source-pole-location predicate must reject it.

## Aggregate rule
PASS only if all four lanes are valid and every applicable frozen predicate passes:
`ITER456_REDUCED_TOLLER_APPENDIXB_RUHL_PHASE_QUALIFIED_SCOPED`.

If lanes are valid but any scientific predicate fails:
`SCIENTIFIC_FAIL_ITER456_REDUCED_TOLLER_APPENDIXB`.

If evaluation/artifact plumbing fails before the predicates are meaningfully evaluated:
`INFRASTRUCTURE_OR_NUMERICAL_FAIL`.

## Interpretation lock
A PASS qualifies only the explicit `k=j=l=1`, pure-boost Appendix-B reduced Toller layer and the Rühl-phase/additive/pole implementation. It does **not** establish Eq.(7) magnetic reconstruction, arbitrary spins, group-element reconstruction, noncompact integration convergence, causal-vertex finiteness, D7-S2 closure, or any terminal D7 classifier.

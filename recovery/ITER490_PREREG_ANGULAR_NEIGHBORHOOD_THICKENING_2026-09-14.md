# Iter490 preregistration — full-angular sampled thickening of a valid Haar NONDECAY witness

Date frozen: 2026-09-14
Status: FROZEN BEFORE IMPLEMENTATION/PRODUCTION

## Parent authority
- Promoted parent classification: `SCIENTIFIC_FAIL_ITER487_HAAR_ESCAPE_ACTUAL_ENVELOPE_REVALIDATED_BY_ITER489`.
- Parent result note: `results/ITER487_ITER489_HAAR_ESCAPE_REVALIDATED_RESULT_2026-09-14.md`.
- Iter489 aggregate artifact `10328187668`, digest `sha256:897f4c4f9dc8927c3872f01ba6e678552367819f70aee342192f904b850b78fb`.

Iter487/489 establishes stable one-dimensional s=4 NONDECAY escape witnesses but cannot support an absolute Haar-divergence claim because one path has zero angular measure. Iter490 is the first prospective angular-thickening gate. It is deliberately a **sampled robustness gate**, not a uniform-neighborhood theorem.

## Frozen center witness
- panel `C`, strong regime;
- cluster size `s=4`, so nodes 1..4 escape together;
- `j=k=l=1` and the exact Iter487 full ten-edge/intertwiner network;
- all four source rho witnesses `{0.35,0.9,1.6,2.7}`;
- causal patterns `{0to5,1to4,2to3}`;
- radial grid `R={6,8,10,12}`;
- exact source Haar radial factor and exact Iter487 slope/drift classifier.

The center was frozen because all three C-panel s=4 causal lanes contain stable NONDECAY points with actual slopes approximately +4, leaving a large prospective margin to the NONDECAY floor 0.

## Frozen 20-dimensional angular chart
For each escaped node `a=1..4`, perturb the central escaped node element by

`g_a(delta;R) = L_a(delta_L) g_a^0(R) R_a(delta_R)`

where `L_a = Rx(dx) Ry(dy) Rz(dz)` and `R_a = Rx(rx) Ry(ry)`. This gives five independent compact angular coordinates per node, 20 total. Node 0 remains identity. The omitted right-z coordinate fixes the local axial KAK redundancy.

At the center and R=10, a finite-difference tangent-rank control must find rank 5 for each node's five chart directions. Failure blocks the lane.

## Frozen radii and deterministic samples
Neighborhood radii: `eps in {0.0025,0.005,0.01,0.02}` radians.

Each `(causal,eps)` lane evaluates exactly 16 deterministic 20-D perturbation vectors plus the unperturbed center:
- samples 0..7 are seeded Rademacher corners in `{−1,+1}^20`;
- samples 8..15 are seeded uniform interior points in `[−1,+1]^20`;
- RNG seed is exactly `490000 + 1000*radius_index + sample_index`; the same perturbation vector is held fixed across R and rho.

This is 12 independent lanes = 3 causal patterns x 4 radii, `fail-fast:false`.

## Frozen observables
For each perturbation sample and rho, compute the same Iter487 quantities:
- `C_max(R,rho)=max_I |C_I|` over all 243 genuine four-valent intertwiner channels;
- source radial Haar log density from the actual node KAK rapidities;
- `log E=log C_max + log H`;
- network, Haar and actual slopes on R={8,10,12};
- early actual slope on {6,8,10};
- slope drift.

## Frozen validity controls
For every sample/R/rho:
A. shared-node K5 cycle residual `<1e-8`;
B. source KAK reconstruction uses the Iter489-qualified two-tier numerical rule: accept double reconstruction if `<1e-8`; if it exceeds that threshold, independently re-evaluate that edge matrix with the 100-digit KAK method and require the same unchanged absolute threshold `<1e-8`;
C. all contractions finite and strictly positive;
D. Haar slope within 0.05 of +8 for s=4;
E. Haar bookkeeping residual `<1e-8`;
F. source additive regression `<1e-9`;
G. chart tangent rank exactly 5 at each of nodes 1..4;
H. center regression must reproduce the parent C-s4 causal-lane states within slope absolute error `<5e-3`.

No threshold may be changed after production.

## Frozen sampled-thickening classifier
For each valid perturbed `(sample,rho)`:
- parent NONDECAY condition: `actual_slope >= 0.00` and drift `<=0.05`;
- robust-margin condition: `actual_slope >= +1.00` and drift `<=0.05`.

Per `(causal,eps)` lane:
1. `ITER490_SAMPLED_ROBUST_THICKENING_LANE` iff every one of the 16 perturbed samples and all four rho values satisfies the robust-margin condition;
2. `ITER490_SAMPLED_NONDECAY_THICKENING_LANE` iff every sample/rho is NONDECAY but at least one misses +1 margin;
3. `SCIENTIFIC_FAIL_ITER490_ANGULAR_THICKENING` iff the lane is valid and any sample/rho is DECAY or asymptotically inconclusive;
4. invalid/control failure -> `INFRASTRUCTURE_OR_NUMERICAL_FAIL_ITER490`.

Aggregate:
- `ITER490_FULL_ANGULAR_SAMPLED_ROBUST_THICKENING_QUALIFIED_SCOPED` iff there exists at least one frozen eps for which all three causal lanes are robust-margin PASS;
- otherwise report the exact largest all-causal sampled-NONDECAY radius if present, or scoped scientific fail/inconclusive according to raw lanes.

## Interpretation ceiling
Even aggregate PASS establishes only **finite deterministic sampled robustness in a locally full-rank 20-D angular chart**. It does not by itself prove a uniform lower bound over every point of an open neighborhood. Therefore no absolute Haar-divergence theorem is authorized by Iter490. A PASS authorizes the next prospective gate: boundary/interval/Lipschitz-style certification of a nonzero-radius neighborhood. A FAIL must not be repaired by shrinking eps post hoc; the four frozen radii already define the prospective radius scan.

Ten source spectral integrations, conditional/PV cancellations and distributional boundary values remain separate. D7-S2 stays NOT_CLOSED. Terminal D7 labels and Candidate Gravity remain forbidden/inactive.
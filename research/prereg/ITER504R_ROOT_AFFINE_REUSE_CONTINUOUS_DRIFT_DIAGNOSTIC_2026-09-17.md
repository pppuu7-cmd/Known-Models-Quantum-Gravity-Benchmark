# ITER504R — root-affine reuse continuous-drift diagnostic

Date: 2026-09-17  
Status: PROSPECTIVELY FROZEN BEFORE ITER504R SUBSTANTIVE OUTCOME

Gate:

`ITER504R_ROOT_AFFINE_REUSE_CONTINUOUS_DRIFT_DIAGNOSTIC_GATE`

## Scientific question

Terminal Iter504P established that the frozen sampled point grid satisfies `D_point <= 0.05`, while terminal Iter504 remains continuous-interval INCONCLUSIVE in the known nonsmooth max-channel region. Iter504Q prospectively selected full recomputation on every adaptive subbox, but historical terminal Iter504 runtime shows that one eight-box centered shard required about 3 h 12 min, making repeated full geometry/source recomputation at every adaptive node inappropriate for a cheap localization gate.

ITER504R asks a narrower and cheaper rigorous question:

**Does narrowing only the amplitude displacement interval `delta`, while retaining the full-root validated derivative enclosure as a rigorous superset derivative bound, reduce the continuous max-envelope drift below the unchanged `0.05` criterion on the same known crossing diagnostic?**

A PASS localizes the dominant overestimation to amplitude-displacement / max-envelope dependency that can be removed without recomputing geometry at every child. An INCONCLUSIVE result localizes a residual bottleneck to root derivative width and/or channel competition that does not disappear under delta refinement alone.

## Mathematical validity of root-affine reuse

For every contraction channel `f(a)` on an original root amplitude interval `I` with midpoint `m`, Iter504 centered AD computes a validated derivative enclosure `D(I)` such that `f'(a) in D(I)` for all `a in I`, together with the validated center value `f(m)`.

For any child interval `J subset I` and any `a in J`, the segment from `m` to `a` lies inside `I`. Therefore the mean-value/integral enclosure

`f(a) in f(m) + (J - m) * D(I)`

is rigorous even when `m` is outside `J`.

The same argument applies to the Haar/log prefactor derivative used by the centered Iter504 construction. Reusing `D(I)` is conservative: the derivative enclosure is not narrowed post hoc. No channel is discarded.

## Parent terminal authority

- Iter504 terminal continuous result: `e3816c0437a1f895196d2bbccacfb05e8dd38e74`.
- Iter504P terminal point localization: `162014c7566afa4828e646f77e52d91140dc8388`.
- Iter504P independent Critic: `f0844237cbf6ba1e042399d5a76dec8a4ab8b248`.
- Parent centered implementation: `aeef88e899c2f3900a8735b30610e9adabebbb9d`.

## Frozen diagnostic cohort

Exactly the same outcome-blind crossing diagnostic preregistered for Iter504Q:

- causal `0to5`;
- block `0`;
- path `2`;
- direction `[1,1,1,-1,-1,-1]`;
- sign `+1`;
- original boxes `13,14,15`;
- all rhos `[0.35,0.9,1.6,2.7]`;
- R grid `[6,8,10,12]`.

Exact root intervals:

- box 13: `[29/12800,30/12800]`;
- box 14: `[30/12800,31/12800]`;
- box 15: `[31/12800,32/12800]`.

## Frozen arithmetic / source contract

- `python-flint==0.9.0`;
- Arb/Acb precision `384` bits;
- same Iter504 KAK, source, Toller, exact-rational intertwiner and 243-channel contraction code;
- all `243` channels retained on every child interval;
- same center regression and source-additive controls;
- same late slope definition `(Y12-Y8)/4` with rigorous lower/upper pairing;
- same early slope definition `(Y10-Y6)/4`;
- same continuous drift upper definition;
- robust NONDECAY floor `+1.0`;
- drift threshold `0.05`.

## Frozen algorithm

For each root box independently:

1. construct the validated dual state once on the **entire root box** with derivative seed 1;
2. construct the validated raw source realization once at the exact root midpoint;
3. for each R and rho, compute and retain in memory all 243 midpoint channel values and all 243 derivative enclosures over the full root box;
4. retain the full-root Haar/log derivative enclosure;
5. evaluate any child interval `J` only through the rigorous root-affine formula using `delta_J = J - root_midpoint`;
6. recompute the 243-channel max-envelope bounds from these child affine enclosures; `possible_max_indices` are diagnostic only and never prune channels;
7. compute the unchanged slope/drift classifier.

A child is `CERTIFIED` iff every rho has `S_lower >= +1.0`, `drift_upper <= 0.05`, and all finite-envelope/root controls pass.

If not certified and depth `< 10`, split exactly at the rational midpoint. If not certified at depth `10`, retain as `UNRESOLVED_DEPTH10`.

Maximum depth is frozen to `10`. The derivative enclosure itself is never recomputed or narrowed on descendants.

## Exact-cover requirements

For each root box independently:

- leaf union equals the full original root box;
- first/last endpoints equal root endpoints exactly;
- adjacent leaves meet exactly;
- no gap;
- no interior overlap;
- no missing or outcome-dependent removed leaf.

## Terminal classifier

### PASS

`ITER504R_ROOT_AFFINE_REUSE_NARROWED_WITHIN_TOLERANCE_SCOPED`

iff all three exact covers and all root/source controls are valid and every terminal leaf is `CERTIFIED` by depth 10.

### Valid scientific INCONCLUSIVE

`ITER504R_ROOT_AFFINE_REUSE_INCONCLUSIVE_SCOPED`

iff all exact-cover/root/source controls are valid but at least one depth-10 leaf remains classifier-inconclusive without a numerical/provenance defect.

This is not FAIL and not a decay witness.

### INVALID

`ITER504R_ROOT_AFFINE_REUSE_INVALID`

iff provenance/source/control/coverage fails, a root box or channel is missing, the cohort/formula/threshold changes, or the affine-reuse implementation is not the frozen root-superset derivative construction.

## Required evidence

Persist per root box and aggregate:

- root controls and minimum beta;
- root model build count exactly one per root box;
- total nodes/leaves and depth histogram;
- certified/unresolved leaves;
- exact coverage certificate;
- root and terminal-leaf possible-max-channel counts;
- maximum terminal-leaf drift and witness;
- minimum terminal-leaf late-slope lower;
- per-rho worst leaf;
- implementation/workflow/run/artifact hashes;
- independent Python-environment reproduction;
- adversarial Critic recomputation of cover/classifier from terminal leaf records.

## Relation to Iter504Q

Iter504Q remains a valid prospectively frozen but computationally expensive method. No Iter504Q substantive artifact/value was consumed before ITER504R was frozen. If Iter504Q later completes, it is an independent stricter full-recompute comparator; ITER504R does not overwrite or reinterpret it.

## Scaling firewall / claim ceiling

Neither PASS nor INCONCLUSIVE on this three-box diagnostic authorizes a full-domain continuous theorem or automatic 1888-state campaign. No positive-measure Haar theorem, absolute-Haar divergence theorem, cutoff removal, D7 closure, selector authorization, model/family failure, Candidate Gravity activation, quantum-gravity solution or new-physics claim follows.

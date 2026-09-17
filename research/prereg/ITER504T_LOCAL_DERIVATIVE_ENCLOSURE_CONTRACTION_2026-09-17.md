# Iter504T — validated local derivative enclosure contraction

Date: 2026-09-17
Status: PROSPECTIVELY FROZEN BEFORE ITER504T SUBSTANTIVE OUTPUT

Gate:

`ITER504T_LOCAL_DERIVATIVE_ENCLOSURE_CONTRACTION`

## Parent authority

Terminal parent:

`ITER504S_ROOT_DERIVATIVE_RADIUS_LOCALIZED_SCOPED`

Authoritative Iter504S run:

`35178186905`

Terminal record commit:

`1b0004064575f046210383dc7b1ee22d4f25e66b`

Outcome-blind successor toolkit:

`81e0e94649a50cccc510dc2630456af45fd98e46`.

## Scientific question

Does recomputing a validated derivative enclosure directly on deterministic local subintervals `J subset I` contract the rigorous continuous envelope enough to certify the frozen slope/drift criterion on the three Iter504S diagnostic roots?

This gate tests the mechanism localized by Iter504S. It does not reclassify all 1888 Iter504 parent states.

## Frozen science and source

Preserve exactly:

- `python-flint==0.9.0`;
- Arb/Acb precision 384 bits;
- causal `0to5`, block `0`, path `2`, direction `[1,1,1,-1,-1,-1]`, sign `+1`;
- root boxes `13,14,15`;
- rhos `[0.35,0.9,1.6,2.7]`;
- R grid `[6,8,10,12]`;
- all 243 channels;
- no channel pruning;
- exact drift threshold `1/20`;
- exact robust slope floor `1`;
- same source-faithful KAK/Toller/exact-rational intertwiner/contraction route used by the parent chain.

No threshold, floor, rho, R, root, channel or source parameter may change after output.

## Frozen local partition

For each root interval `I=[lo,hi]`, use deterministic dyadic subdivision.

Maximum local depth:

`MAX_DEPTH = 3`.

Depth 0 is the full root. Every unresolved node `[a,b]` at depth `<3` is split exactly at rational midpoint `(a+b)/2` into left then right children.

No adaptive split location is allowed.

Early stopping is allowed only when a node is already scientifically certified by the frozen criterion below. Uncertified nodes must split until depth 3.

No post-outcome depth extension is permitted. A depth-3 unresolved result is INCONCLUSIVE, not permission to continue automatically.

## Validated local derivative construction

For every visited interval `J=[j_lo,j_hi]`, construct the dual state directly with the interval amplitude `J` and derivative seed `1`.

For every retained channel `f_i`, extract the derivative object from the dual contraction and treat it as a validated enclosure `D_i(J)` satisfying the source construction's interval semantics over all amplitudes in `J`.

Likewise construct the validated local Haar/log derivative enclosure `D_logH(J)`.

The derivative midpoint, sampled derivatives, finite differences, or the Iter504S center-D control are forbidden as scientific substitutes.

## Local midpoint values

Let `m_J=(j_lo+j_hi)/2` be the exact rational midpoint.

Construct the source-faithful ordinary Arb state directly at `m_J`.

For each channel use the rigorous mean-value enclosure

`f_i(J) subset f_i(m_J) + (J-m_J) D_i(J)`.

For the Haar/log factor use

`logH(J) subset logH(m_J) + (J-m_J) D_logH(J)`.

Then compute the full 243-channel max envelope with no pruning.

## Frozen scientific predicate

For each node and rho, construct the same four R-value rigorous Y bounds as the parent chain.

Late slope:

`S = (Y12-Y8)/4`.

Early slope:

`E = (Y10-Y6)/4`.

Use the same rigorous lower/upper pairing as Iter504R/S.

Define in Arb before serialization:

`slope_floor_satisfied := S_lower >= arb('1.0')`.

`drift_within_tolerance := drift_upper <= arb('0.05')`.

`rho_certified := slope_floor_satisfied AND drift_within_tolerance`.

A node is certified iff all four rhos are certified.

Binary64 summaries are display-only and may not determine any scientific branch.

## Local derivative contraction controls

At depth 0 construct the parent-root derivative enclosure `D(I)` by the same local construction.

For every child `J`, record componentwise Arb containment checks where the direct interval objects make this comparison meaningful:

`D_i(J) subseteq D_i(parent(J))`

for all 243 channel derivatives at every R/rho and for the Haar/log derivative.

Containment failure does not by itself invalidate the science because dependency inflation can make two independently valid interval constructions non-nested. Therefore distinguish:

- `validated_local_derivative = true`: local construction itself passed all source/finite controls;
- `componentwise_parent_inclusion = true/false`: optional contraction certificate;
- never infer validity from nominal radius reduction.

Any claimed derivative contraction must be supported by actual componentwise inclusion, not only smaller serialized widths.

## Terminal classifier

After complete deterministic coverage of roots 13-15:

### PASS

`ITER504T_LOCAL_D_CERTIFIES_THREE_ROOT_CONTINUOUS_DRIFT_SCOPED`

iff:

1. every root has an exact gap-free dyadic terminal cover;
2. every terminal leaf is scientifically certified;
3. every visited local construction is valid;
4. all 243 channels are retained everywhere;
5. exact decision transport/provenance controls pass;
6. independent Python 3.11 and 3.13 scientific decisions agree;
7. independent Critic returns no errors.

### INCONCLUSIVE

`ITER504T_LOCAL_D_INCONCLUSIVE_SCOPED`

iff implementation/provenance is valid and at least one depth-3 terminal leaf remains uncertified.

This means the bounded local-D mechanism test did not close the three-root obstruction at the prospectively frozen depth. It is not a scientific FAIL and does not authorize automatic deeper search.

### INVALID

`ITER504T_INVALID`

iff source/provenance/root/rho/R/channel/precision/partition/exact-threshold/exact-floor/decision-transport/cover validity fails, a derivative midpoint or sampled derivative is used as truth, channels are pruned, or cross-environment/Critic scientific decisions disagree.

No fourth terminal class may be invented after output.

## Independent reproduction

Run independent Python 3.11 and 3.13 cohorts, both with `python-flint==0.9.0` and 384-bit precision.

Require equality of:

- root and dyadic interval identities;
- terminal cover identities;
- exact scientific booleans;
- certified/unresolved status;
- possible-max identities;
- channel completeness;
- final classifier.

Incidental binary64 display text need not be byte-identical.

## Negative controls

The Critic must reject at least:

- omitted channel;
- wrong threshold or floor;
- scientific decision reconstructed from float;
- outcome-dependent split location;
- depth beyond 3;
- missing required child;
- gap/overlap in terminal cover;
- derivative midpoint substituted for `D(J)`;
- sampled/finite-difference derivative substituted for `D(J)`;
- reusing full-root `D(I)` instead of recomputing on a child;
- changed root/rho/R cohort;
- center-D treated as rigorous;
- favorable channel selection;
- missing provenance authority.

## Held-out firewall

Even a PASS here is restricted to roots 13-15. Before any full-domain expansion, freeze a representative held-out cohort prospectively and apply the same local-D mechanism with no refit.

## Claim ceiling

A PASS establishes only that the validated local derivative enclosure mechanism closes the frozen continuous-drift obstruction on these three roots at this bounded partition. It does not establish all 1888 states, D7 closure, quantum gravity, Candidate Gravity validity, NEW_REQUIRED, new physics, or experiment.

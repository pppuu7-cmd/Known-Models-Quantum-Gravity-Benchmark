# P4 BCFW Infinity Boundary Origin-Data Gate

**Status:** scoped hard-amplitude origin prefilter.  
**KMQGB iteration:** 108.  
**Purpose:** identify when large-complex-momentum boundary data are genuine new hard information rather than ordinary factorization data, local EFT contacts, or a restatement of Einstein-gravity constructibility.

## 1. Control from ordinary gravity

For a complex momentum deformation parameter `z`, a tree amplitude may be reconstructed from its finite poles only when the contour at infinity gives no boundary contribution.

Ordinary gravity provides a strong positive control: under the standard two-line BCFW shift, the improved large-`z` behavior allows tree amplitudes to be reconstructed from pole factorization in the familiar constructible sectors.

Therefore, if a candidate has

- the same asymptotic states as GR;
- the same physical three-point amplitudes/residues;
- no boundary contribution at infinity;

then BCFW reconstruction does not create a new hard datum. It reconstructs the comparator tree hierarchy.

Classification:

`NO_INFINITY_BOUNDARY_PLUS_GR_LOWER_DATA__GR_FACTORISATION_CONTAINED`.

## 2. Boundary data are a legitimate location for new hard information

For more general multi-line shifts, gravity amplitudes can have nonzero poles/boundary contributions at infinity. Recent work emphasizes that general principles do not in general determine these residues.

Reference:

Justin Lemmon and Jaroslav Trnka, *Tree-Level Gravity Amplitudes at Infinity*, arXiv:2512.11787.

The same work finds special classes of shifts for which the leading infinity data exhibit factorization-like relations to lower-point gravity amplitudes or evaluate the same amplitude on special shifted/collinear kinematics.

Thus infinity data can be highly structured, but that structure is not automatically a new parent principle.

## 3. KMQGB trichotomy

Let `B_n` denote the boundary-at-infinity datum needed in a chosen recursion.

### Case A — `B_n = 0`

With the same lower-point GR data, ordinary constructibility returns GR. No new P4 datum.

### Case B — `B_n` is a finite local polynomial/contact datum

Then the same-factorization contact theorem applies: the boundary contribution belongs to local analytic higher-derivative/contact freedom, i.e. full C5 after matching.

Classification:

`LOCAL_INFINITY_BOUNDARY__FULL_C5_CONTACT`.

### Case C — `B_n` is non-polynomial/nonlocal/nonperturbative

This can in principle carry comparator-orthogonal hard information, but the boundary function/sequence must itself be derived from a finite gravity-native law. Merely specifying `B_n` is equivalent to specifying the missing hard seed.

It must pass

- functional-freedom / finite-data tests;
- growth and singularity classification;
- crossing and physical factorization;
- causality/unitarity;
- string/q-string/nonlocal/matrix/discrete comparators;
- same-parent CTP/retarded completion.

## 4. Factorization at infinity is transport/compression, not automatically origin

Suppose a family of amplitudes satisfies a relation schematically

`B_n = K_n * A_{n-1}`

for a prospectively fixed kinematic operator `K_n`.

This is powerful compression: once the seed and `K_n` are fixed, higher boundary data can be generated recursively.

However two possibilities remain:

1. `K_n` is the known Einstein-gravity infinity law -> comparator-contained positive control;
2. `K_n` is deformed -> the physical origin of that deformation becomes the first hard datum and must be derived independently.

Therefore

`boundary recursion completeness != origin of boundary law`.

## 5. Relation to hidden-zero rigidity

Large-`z` behavior and hidden-zero constraints are closely related forms of hard amplitude rigidity. Both can strongly compress a rational amplitude.

But neither can earn P4 credit unless the candidate prospectively derives

- the relevant shift/domain;
- zero/boundary law;
- degree/growth behavior;
- normalization;
- all-helicity/multiplicity completion.

Otherwise the UV/hard boundary condition is chosen rather than predicted.

## 6. P4 rule

For any amplitude-recursion candidate, explicitly record

`B0` chosen complex deformation and why it is physical/parent-derived;

`B1` whether the infinity boundary vanishes;

`B2` if nonzero, its finite-data origin law;

`B3` local-polynomial versus nonlocal/nonperturbative classification;

`B4` comparator survival;

`B5` linked all-point and CTP/retarded continuation.

An unspecified infinity boundary gives

`BLOCKED__HARD_BOUNDARY_DATA_NOT_SELECTED`.

## 7. Score consequence

This gate identifies a legitimate possible location of the first hard datum, but supplies no novel datum itself. R4 remains 45%.
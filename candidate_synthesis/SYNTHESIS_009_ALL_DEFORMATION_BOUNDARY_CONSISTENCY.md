# SYNTHESIS-009 — All-Deformation Boundary Consistency Parent

**Status:** REJECTED as standalone P4 parent / retained boundary-data control.  
**KMQGB iteration:** 109.  
**Purpose:** test whether mutual consistency of all complex momentum deformations can select the first irreducible gravity hard datum.

## 1. Proposed parent law

For a physical tree-level graviton amplitude, consider a sufficiently rich web of two-line and multi-line complex deformations. Require that

1. every finite residue factorizes correctly;
2. every nonzero boundary-at-infinity term agrees with the same undeformed amplitude;
3. hard-to-soft maps and crossing relations between different shifts are mutually consistent;
4. no shift-dependent extra datum is allowed.

Tempting principle:

> the quantum-gravity hard amplitude is the unique crossing-symmetric object compatible with the complete web of factorization and infinity-boundary reconstructions.

This is more gravity-specific than choosing a single form factor and uses genuine on-shell consistency across representations of the same amplitude.

## 2. A1 — explicit consistency law

The deformation web is finite in rule form even though it generates many constraints. Known gravity results provide strong positive controls: ordinary two-line BCFW reconstruction has vanishing boundary, while other shifts can expose nontrivial infinity data with factorization-like or soft-related structure.

Thus

`A1 PASS_AS_ON_SHELL_CONSISTENCY_PRINCIPLE`.

## 3. A2 — global contact nullspace survives every shift

Let `C_n` be any crossing/helicity-allowed local contact amplitude.

`C_n` is one globally defined amplitude. Therefore its values and its boundary terms under **all** complex shifts are automatically mutually consistent: they are simply different deformations of the same polynomial function.

It has no finite factorization poles, so factorization conditions cannot determine its coefficient. Changing shifts moves the information between different residues/boundary terms but does not eliminate the underlying contact freedom.

With increasing derivative order there is a tower of allowed local gravitational contacts unless a separate degree/growth/UV law fixes them.

Therefore

`A2 FAIL__ALL_SHIFT_CONSISTENCY_LEAVES_GLOBAL_CONTACT_NULLSPACE`.

This is the boundary-at-infinity version of the earlier transport-vs-origin theorem.

## 4. A3 — comparator containment

If the contact nullspace is restricted to local analytic gravity operators, it is full C5.

If a nonlocal boundary function is introduced, its origin/growth/singularity data must independently pass the nonlocal/Hadamard/CDD/string/AS comparator gates.

If the ordinary GR boundary behavior is chosen, the construction returns GR.

Hence all-deformation consistency by itself does not produce a comparator-orthogonal parent.

## 5. A4 — no normalized new hard datum

The proposal supplies relations among representations of an amplitude, but it does not select the first new irreducible hard coefficient/function. No new normalized `K4` exists before extra UV/growth data are specified.

Classification:

`A4 BLOCKED__BOUNDARY_WEB_TRANSPORTS_BUT_DOES_NOT_ORIGINATE_CONTACT_DATA`.

## 6. Positive lesson

Boundary-at-infinity information can be highly structured and can even be related to lower-point amplitudes or soft limits. This proves that boundary data need not be arbitrary **once a theory is given**.

But for parent selection the direction of inference matters:

`given theory -> structured boundary web`

is not equivalent to

`structured boundary web -> unique new theory`.

The missing selector is a physical **degree/growth/singularity law** that removes the common contact/null sector before inspecting the desired answer.

## 7. Next synthesis requirement

SYNTHESIS-010 should test a prospective gravity-native rule for the allowed asymptotic growth class itself. A viable rule must

- remove the local contact tower;
- not merely select ordinary GR minimal growth;
- not collapse to string/minimal-zero or weakly-nonlocal exponential comparator;
- fix normalization and all-point/CTP continuation from the same parent.

## 8. Score consequence

No P4 credit. R4 remains 45%.

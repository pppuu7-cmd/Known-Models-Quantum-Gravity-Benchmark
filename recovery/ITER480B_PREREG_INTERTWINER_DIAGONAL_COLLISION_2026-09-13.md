# Iter480B preregistration — source-backed four-valent intertwiner contraction of Toller leading coefficients

Date: 2026-09-13
Status: FROZEN BEFORE IMPLEMENTATION
Parent authority: newest main through Iter479 plus transparent pre-production invalidation of Iter480.

## Source authority
The 2026 causal-vertex source defines a boundary spin-network state with 10 spins and 5 intertwiners and Eq.(4) contracts the Toller magnetic indices with those boundary data. Dona–Frisoni (2022), Appendix A Eq.(90), gives the explicit four-valent SU(2) recoupling-basis intertwiner in terms of two Wigner 3jm symbols. This gate combines only those published ingredients with already-qualified Iter477/479 leading Toller coefficients.

## Scientific question
Does contraction with genuine four-valent SU(2)-invariant boundary intertwiners force the leading individual-branch Toller coefficient to cancel identically in the minimal equal-spin j=1 diagonal-collision control, or do source-compatible invariant contractions with nonzero leading coefficient exist?

## Frozen model
- K5, 10 wedges, all j=1.
- Five four-valent boundary intertwiners from Dona–Frisoni Eq.(90), recoupling channel i in {0,1,2}.
- For every wedge e=(ab), use the Iter477 leading reduced-Toller coefficient vector C_e(m), m in {-1,0,+1}, branch fixed by kappa_ab=sigma_a sigma_b. The diagonal-collision control identifies the row/column magnetic label on that wedge. No angular U1/U2 matrices are inserted.
- gamma in {7,8}.
- canonical causal representatives: 0<->5 sigma=(+,+,+,+,+), 1<->4 sigma=(-,+,+,+,+), 2<->3 sigma=(-,-,+,+,+).
- Exhaust all 3^5=243 boundary recoupling-channel assignments for every gamma x causal representative.

## Dimensionless normalization
For each gamma x causal panel define
`S = product_e max_m |C_e(m)|`.
S must be finite and strictly positive.
For each contraction A define dimensionless witness ratio `R=|A|/S`.
The frozen nonzero threshold is `R > 1e-12`.
This threshold is not fitted to any desired physical conclusion; it is a numerical zero-discrimination threshold on a dimensionless normalized tensor contraction.

## Frozen checks
A. Reconstruct i=0,1,2 intertwiners directly from Eq.(90); verify support m1+m2+m3+m4=0, mutual orthogonality, and norm 1/(2i+1), each to 1e-12.
B. Evaluate all 243 K5 contractions in every frozen panel.
C. Require at least one finite contraction with R>1e-12 in every gamma x causal panel. Individual channel assignments may vanish by symmetry.
D. Pure reindexing control: simultaneously relabel every edge m->-m in both coefficient vectors and all incident intertwiner tensor axes; the sorted multiset of |A| values must agree to relative 1e-10.
E. Negative control: replace all wedge coefficient vectors by zero vectors; all 243 contractions must have |A|<1e-14.
F. Report number of nonzero witnesses, maximum R, channel tuple attaining maximum R, and the full zero/nonzero support count for every panel.

## PASS rule
PASS iff A-E all pass. PASS label:
`ITER480B_SOURCE_INTERTWINER_CONTRACTION_NONZERO_WITNESS_SCOPED`.

A valid-control failure of C is a SCIENTIFIC FAIL for this frozen minimal diagnostic. Infrastructure/dependency failures are not scientific results.

## Scope guards
PASS excludes only universal cancellation caused solely by the five boundary SU(2) four-valent intertwiner contractions in this equal-spin j=1 diagonal-collision control. It does not exclude angular U1/U2 cancellation, shared-group constraints, Haar/group integration, non-diagonal magnetic mixing, spectral integration, Jacobians, or full K5 collision-stratum cancellation. It does not close D7-S2/D7-S3/D7-S4, does not authorize terminal D7 labels, and does not activate Candidate Gravity.

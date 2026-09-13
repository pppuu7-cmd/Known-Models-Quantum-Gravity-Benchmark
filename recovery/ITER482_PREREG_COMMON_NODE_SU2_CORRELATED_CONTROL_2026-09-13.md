# Iter482 preregistration — common-node SU(2) correlated control

Date: 2026-09-13
Status: FROZEN BEFORE IMPLEMENTATION
Parent authority: terminal Iter481.

## Scientific question
Does the nonzero leading magnetic/intertwiner witness found in Iter481 survive a first genuinely correlated common-node control in which all ten K5 edge rotations are generated from only five node rotations, rather than chosen independently edge by edge? Separately, are the old Iter481 P0/P1 edge-angle panels correctly identified as local controls rather than common-node-compatible panels?

## Scope lock
This is a compact SU(2) common-node/control-slice diagnostic only. It is **not** the full source `SL(2,C)` KAK decomposition, boost sector, Haar integration or causal vertex. The pure-SU(2) slice has KAK degeneracy, so no claim that one chosen factorization is the unique source Eq.(7) factorization is allowed. Its purpose is to impose exact shared-node correlation/cycle consistency before the later noncompact gate.

## Frozen construction
- K5, all face spins j=1.
- gamma in `{7,8}`.
- causal representatives `0to5`, `1to4`, `2to3` exactly as Iter481.
- Reuse Iter481/Iter479 coefficient, Wigner-j=1 and Eq.(90) intertwiner conventions unchanged.
- Three prospectively fixed node-rotation panels Q0,Q1,Q2. Node 0 is identity (gauge root); nodes 1..4 use deterministic Euler triples frozen in the implementation from this prereg only.
- For every edge `(a,b)`, define the correlated compact relative rotation `R_ab = Q_b^† Q_a` in the qualified j=1 representation. The leading control matrix is `L_ab = R_ab diag(C_ab)` in basis `[1,0,-1]`, then reordered exactly as Iter481 for the intertwiner basis. This is a compact correlated control, not a unique full Toller KAK choice.
- Total production matrix: 2 gamma x 3 causal representatives x 3 common-node panels = 18 independent lanes, `fail-fast:false`.

## Frozen exact/shared-node checks
A. Every node matrix is unitary to max residual `<1e-12`.
B. Every edge matrix `R_ab` is unitary to max residual `<1e-12`.
C. Triangle cycle consistency: for every ordered triangle `a<b<c`, require `R_bc R_ab = R_ac` to max residual `<1e-12` under the frozen orientation convention.
D. Common-left gauge control: multiply all five node matrices by the same frozen nontrivial unitary G and recompute all `R_ab`; every edge must agree with the original to max residual `<1e-12`.
E. Deliberate corrupted-edge negative control: replace one edge relative matrix by a fixed noncommuting Wigner rotation times that edge; at least one triangle closure residual must exceed `1e-6`.
F. Diagnose the prior Iter481 P0/P1 independent-edge rotation products using the same triangle-cycle criterion; they are expected not to satisfy common-node closure. This is diagnostic only and cannot retroactively invalidate Iter481, whose prereg explicitly scoped them as local controls.

## Frozen network checks
G. Reconstruct Eq.(90) intertwiners and require the existing support/Gram controls `<1e-12`.
H. For each of the 18 lanes, evaluate all `3^5=243` intertwiner channels with the ten correlated `L_ab`. Normalize by the same dimensionless coefficient scale `S=product_e max_m|C_e(m)|`; require at least one finite witness `R=|A|/S > 1e-12`.
I. Magnetic-basis simultaneous reindex control: sorted magnitude multiset residual `<1e-10`.
J. Zero-edge-matrix negative control: all channels `<1e-14`.

## PASS rule
PASS iff A-E and G-J pass in all 18 lanes and F is reported. PASS label:
`ITER482_COMMON_NODE_SU2_CORRELATED_NETWORK_NONZERO_WITNESS_SCOPED`.

A valid-control failure of H is a SCIENTIFIC FAIL for this compact common-node control. Dependency/runtime/serialization failure is infrastructure/numerical. Frozen thresholds, panels and interpretation may not be weakened after viewing production results.

## Interpretation lock
PASS would show only that exact common-node/cycle correlation on a compact SU(2) control slice does not itself force universal cancellation on the frozen j=1 panels. It would not establish the noncompact `SL(2,C)` boost/KAK/Haar result, convergence, distributional validity, D7-S2 closure, any terminal D7 label or Candidate Gravity authorization.

## Next if PASS
A subsequent prospectively frozen gate must introduce noncompact `SL(2,C)` node variables / boost dependence and source-faithful Haar or controlled quadrature structure. Do not repeat independent-edge angular panels.
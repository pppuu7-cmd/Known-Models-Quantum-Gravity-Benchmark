# Iter480 preregistration — source-backed four-valent intertwiner contraction of Toller leading coefficients

Date: 2026-09-13
Status: FROZEN BEFORE IMPLEMENTATION
Parent authority: newest main through Iter479.

## Source authority
The 2026 causal-vertex source defines the boundary spin-network state with 10 spins and 5 intertwiners and Eq.(4) contracts the Toller magnetic indices with those boundary data. The computational EPRL reference Dona–Frisoni (2022), Appendix A Eq.(90), gives an explicit four-valent SU(2) recoupling-basis intertwiner in terms of two Wigner 3jm symbols. This gate combines only those published ingredients with the already-qualified Iter477/479 leading Toller coefficients.

## Scientific question
Does contraction with genuine four-valent SU(2)-invariant boundary intertwiners force the leading individual-branch Toller coefficient to cancel identically in the minimal equal-spin j=1 diagonal-collision control, or do source-compatible invariant contractions with nonzero leading coefficient exist?

This is a boundary magnetic-tensor diagnostic only. It is not the full group-integrated causal vertex and is not a divergence theorem.

## Frozen model
- Complete graph K5, 10 wedges, all face spins j=1.
- At each of the five four-valent boundary nodes use the Dona–Frisoni Eq.(90) recoupling tensor for channel i in {0,1,2}; use the source normalization implied by Eq.(90), while separately checking its exact norm 1/(2i+1).
- For each wedge e=(ab), use the Iter477 leading reduced-Toller coefficient C_m(gamma, branch) with m in {-1,0,+1}; diagonal collision identifies the two edge magnetic labels on that wedge. No U1/U2 angular matrices are inserted in this gate.
- gamma in {7,8}.
- Three canonical causal edge-orientation representatives: 0<->5 sigma=(+,+,+,+,+), 1<->4 sigma=(-,+,+,+,+), 2<->3 sigma=(-,-,+,+,+), with wedge branch kappa_ab=sigma_a sigma_b.
- Exhaust all 3^5=243 boundary recoupling-channel assignments for each gamma and causal representative.

## Frozen checks
A. Reconstruct all three j=1 four-valent intertwiners directly from the published Eq.(90) 3jm formula; verify exact/near-exact support rule m1+m2+m3+m4=0, mutual orthogonality, and norm 1/(2i+1).
B. Contract the full K5 diagonal leading-coefficient tensor network for all 243 channel assignments for each gamma and each of the three causal representatives.
C. Require at least one finite nonzero contraction in every frozen gamma x causal-representative panel. Nonzero means |A| > 1e-12 * max(1, product_e max_m |C_e(m)|); this threshold is frozen prospectively.
D. Held-out convention control: reverse every edge magnetic label m->-m and simultaneously use the corresponding transformed intertwiner tensor; the multiset of contraction magnitudes must agree within relative 1e-10.
E. Negative control: replace every Toller leading coefficient vector by an all-zero vector and require every one of the 243 contractions to vanish exactly/numerically below 1e-14.
F. Sparsity is allowed: individual recoupling assignments may vanish by symmetry. The gate tests universal forced cancellation, not nonvanishing of every boundary channel.

## PASS rule
PASS iff A-E all pass. PASS label:
`ITER480_SOURCE_INTERTWINER_CONTRACTION_NONZERO_WITNESS_SCOPED`.

FAIL is scientific if the implementation/control layer is valid but any gamma x causal representative has no nonzero invariant-contraction witness under the frozen threshold.

## Scope guards
A PASS only excludes **universal cancellation caused solely by the five boundary SU(2) four-valent intertwiner contractions in this j=1 diagonal-collision control**. It does not exclude cancellation from angular U1/U2 structure, shared group variables, group/Haar integration, multi-wedge non-diagonal magnetic mixing, spectral integration, Jacobians, or full K5 collision geometry. It does not close D7-S2/D7-S3/D7-S4, does not authorize a terminal D7 classifier, and does not activate Candidate Gravity.

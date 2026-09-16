# Independent Critic — D7-S2 Eq.(4) K5 group-variable tangent pushforward

Date: 2026-09-16
Verdict: `CRITIC_CONFIRMS_SCOPED_RAW_K5_TANGENT_PASS_NO_PHYSICAL_PROMOTION`

## Adversarial checks

1. **Preregistration ordering.** The earlier mainline preregistration `bc9aa01263df1172206eb211b456bf5d78fe1b1b` predates the later compatible preregistration. The canonical result correctly treats the older document as governing. The first production run omitted two explicit older-prereg checks and is correctly retained as noncanonical partial evidence rather than silently promoted.

2. **Source identity.** The map is the literal already-authorized Eq.(4) tangent identity `Y_ab=X_a-X_b` obtained from `g_ab=g_b^{-1}g_a`; no physical quotient, V8 relation, guessed contact projection or Toller composition enters.

3. **Triangle consistency.** The `(12,23,13)` restriction with root 1 reproduces exactly `[[-1,0],[1,-1],[0,-1]]`, hence `(-X2,X2-X3,-X3)`. There is no sign/order drift between triangle and K5 conventions.

4. **Rank is raw, not physical.** Per generator `rank=4`, domain nullity `0`, left-nullity `6`; full real `sl(2,C)` block lift has `24->60`, rank `24`, domain nullity `0`, left-nullity `36`. The result never calls these values a physical transverse rank.

5. **Cycle basis.** The six frozen triangle-cycle vectors `(1,i,j)`, `2<=i<j<=5`, are integer, have exact rank 6, and annihilate every root-reduced incidence matrix. The six edge-space relations are graph cycles, not physical zero modes.

6. **No cherry-picked Jacobian.** The independent tree lane enumerates all 125 spanning trees for each of five roots and checks all 625 corresponding `4x4` minors. Every determinant is exactly `+1` or `-1`. No favorable tree or root is selected after outcome.

7. **Gauge-root transport.** All 20 ordered root-to-root tangent-coordinate changes are checked and have determinant `+/-1`. Root choice is therefore an exact unimodular coordinate change at this raw linear level, not an additional physical assumption.

8. **Orientation/S5 transport.** All 120 vertex permutations times five roots are checked with the sign induced by restoring the source ordering `a<b`; all 600 exact comparisons pass. Orientation was not silently discarded.

9. **Independent methods.** Rational RREF/cycle/root/S5 verification and graph spanning-tree/fraction-free-minor verification are structurally different proof paths and agree on rank/cycle invariants. The tree JSON is byte-identical in substantive content to the prior run, while the repaired RREF lane adds the previously missing checks.

10. **Iter466 comparison.** The comparison is limited to Iter466's topology scope (rank 4, cycle dimension 6 per root). No distributional or convergence content is imported from Iter466.

11. **Jacobian hygiene.** Unit tree minors authorize an integral raw tangent coordinate chart only. They do not imply Haar-measure invariance, contact-distribution normalization, physical transversality, or a source-authorized physical quotient.

## Conclusion

No defect was found in the repaired terminal PASS within its frozen scope. The result closes the raw full-K5 group-variable tangent-pushforward prerequisite and nothing downstream: D7-S2 remains `NOT_CLOSED`, and the physical quotient authority blocker remains intact.

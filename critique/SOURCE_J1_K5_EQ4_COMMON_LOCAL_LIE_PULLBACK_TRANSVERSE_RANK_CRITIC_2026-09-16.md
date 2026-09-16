# Independent Critic — SOURCE_J1_K5_EQ4_COMMON_LOCAL_LIE_PULLBACK_TRANSVERSE_RANK_GATE

Date: 2026-09-16
Verdict: `CRITIC_CONFIRMS_RAW_RANK_AND_PHYSICAL_BLOCKER_SEPARATION`

The Critic independently checked the source-authorized maps, the generator-level differential, exact-rank arithmetic, basis controls, S3 raw relabeling controls and the authority boundary.

- From `G12=g2^{-1}`, `G23=g3^{-1}g2`, `G13=g3^{-1}`, the identity-point differential is `(-X2, X2-X3, -X3)`.
- The generator matrix `[[-1,0],[1,-1],[0,-1]]` has exact rank 2 and exact left relation `(1,1,-1)`.
- For real `sl(2,C)` dimension 6 the block map has domain 12, codomain 18, rank 12, domain nullity 0 and left-nullity 6.
- RREF and independent minor proof agree; the fixed invertible rational basis replacements and all six raw relabelings preserve rank.
- No frozen source record defines the physical transverse quotient/projection, simultaneous contact pullback to that quotient, Jacobian/Haar/contact-normalization transport, or S3/orientation transport on it.

Therefore the raw differential result is valid, while `physical_transverse_rank=null` is mandatory. Calling it 0 would be false; calling it 12 would silently identify raw coordinate rank with a physical quotient rank and would also be invalid.

No defect requiring reinterpretation of the terminal `BLOCKED_SCOPED` result was found. The next source question should be only the minimal quotient/projection authority object; downstream normalization/S3 transport should not be guessed before that object exists.

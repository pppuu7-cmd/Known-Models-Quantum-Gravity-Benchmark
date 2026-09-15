# Preregistration — source j=1 K5 vertex-level conjugation derivation / counterterm decision

Date: 2026-09-15
Status: `PROSPECTIVELY_FROZEN`
Gate: `SOURCE_J1_K5_VERTEX_LEVEL_CONJUGATION_DERIVATION_AND_COUNTERTERM_ELIMINATION_GATE`

## HYPOTHESIS

The repository-pinned one-wedge reduced Toller formulas and Eq. (7) magnetic reconstruction may determine a unique anti-linear causal/co-causal transformation at the full j=1 one-wedge matrix level. This gate tests that derivability prospectively and then asks a separate question: whether the derived one-wedge transformation, without adding new model data, uniquely determines the action on the already frozen K5 full-collision counterterm witness.

The gate is deliberately allowed to terminate `BLOCKED_SCOPED` if the source-derived one-wedge map is uniquely recoverable but the correlated joint collision-supported extension action is not derivable from the frozen source chain. Such a blocker is not scientific falsification.

## EXACT OBJECT

Fixed source-order EPRL/FK causal/co-causal vertex sector at:

- `j=1`;
- boundary intertwiner channel `(0,0,0,0,0)`;
- ten K5 wedge signs `kappa_ab`;
- source-defined one-wedge Toller matrices reconstructed from the reduced magnetic entries in the frozen Eq. (7) convention;
- the previously frozen real collision-supported distribution `delta_N` with coefficient witness `c(kappa)=+i` on `C_+`, `-i` on `C_-=-C_+`, and `0` otherwise.

No reordered ten-spectral surrogate, independent-edge approximation, fitted KAK object, or different spin/channel is admissible.

## DEPENDENCY

Frozen upstream chain:

1. `research/SOURCE_J1_K5_PUBLISHED_IEPSILON_SCOPE_RESULT_2026-09-15.md`, blob `9a5531b6dbecc367c2869c6e9d873071a6444a66`.
2. `research/SOURCE_J1_K5_CAUSAL_COCAUSAL_CONJUGATION_AMBIGUITY_PREREG_2026-09-15.md`, blob `de8916bb0444d54249ffa7ffc33553ff39d5db0f`.
3. `research/SOURCE_J1_K5_VERTEX_LEVEL_CONJUGATION_AUTHORITY_RESULT_2026-09-15.md`, blob `839f0ed038b60eb73dfbdc4738872d13fea2a352`.
4. independent Critic `recovery/CRITICAL_REVIEW_SOURCE_J1_K5_VERTEX_LEVEL_CONJUGATION_AUTHORITY_2026-09-15.md`, blob `87a95edccb41ca2115ad0918b590d948bf4b9338`, verdict `CONFIRMED_SCOPED`.
5. source-formula transcription `code/iter456_reduced_toller_appendixb.py`, blob `9626d52307763bc84c348110ed26db4a2b57b211`.
6. Eq. (7) magnetic reconstruction/convention control `code/iter457_toller_eq7_magnetic_reconstruction.py`, blob `23d7108cd697012b2d9bb9ce3b2651d36b561e2b`.

Concurrent Iter504 run `34907349374` and Iter461 run `34748503239` are non-terminal and excluded from this gate.

## SOURCE / REALIZATION AUTHORITY

The authority hierarchy is frozen as follows:

- published one-wedge Toller/Feynman structure is authoritative only through repository records already validated and explicitly frozen above;
- the Iter456 formulas are treated as the repository-pinned transcription of the reduced j=1 source formulas;
- Iter457 fixes the magnetic basis ordering `m=(+1,0,-1)` and the full-matrix reconstruction `T = D^1(U1) diag(t_m) D^1(U2)` used in this gate;
- the coefficient witness remains only the previously frozen adversarial collision-supported perturbation; it is not source-selected.

No external formula may be imported after this preregistration to rescue or defeat the gate.

## FROZEN INPUTS

### Candidate reduced anti-linear maps

For each reduced magnetic component and real nonzero rho, search only the finite candidate family

`conj(t_plus_m(rho,beta)) = q_m * t_minus_{s_m m}(s_r rho,beta)`

with:

- common `s_r in {+1,-1}`;
- common `s_m in {+1,-1}` acting as `m -> s_m m`;
- component phases `q_m in {+1,-1,+i,-i}` for `m=+1,0,-1`.

A candidate is accepted only if it holds across every frozen control point and then admits an algebraic identity check directly against the explicit Iter456 formulas. Multiple surviving candidates invalidate uniqueness.

### Magnetic reconstruction

Freeze the Iter457 convention:

`T_plus/minus(U1,beta,U2;rho) = D^1(U1) diag(t_plus/minus_{+1,0,-1}) D^1(U2)`.

The SU(2) j=1 conjugation matrix in the same basis is frozen to the candidate

`C_{m n}=(-1)^(1-m) delta_{m,-n}`

in ordering `(+1,0,-1)`, i.e.

`C = [[0,0,1],[0,-1,0],[1,0,0]]`.

The gate must verify rather than assume the corresponding Wigner-matrix conjugation identity on the Iter457 closed-form realization.

### Control grid

Use exactly:

- `rho = {-2.3,-1.7,-0.6,0.35,0.9,1.6,2.7}`;
- `beta = {0.35,0.8,1.2,pi/2,2.1}`;
- the four Iter457 frozen `U1,U2` angle lanes `L0..L3`;
- 80 decimal-digit arithmetic for numerical discrimination;
- acceptance tolerance `1e-35` relative/absolute envelope, followed by algebraic formula verification for any numerical survivor.

### Frozen joint witness

Retain exactly the prior coefficient family:

- `c(kappa)=+i` for `kappa in C_+`;
- `c(kappa)=-i` for `kappa in C_-=-C_+`;
- `c(kappa)=0` otherwise;
- `delta_N` real under scalar complex conjugation;
- no new regulator or counterterm coefficient may be introduced.

## POSITIVE CONTROLS

1. All 3x7x5 reduced source values are finite at the frozen real nonzero rho grid.
2. Exactly one candidate reduced anti-linear map survives the finite search and algebraic formula verification.
3. The frozen j=1 Wigner conjugation matrix `C` satisfies the Iter457 closed-form identity over all frozen angle lanes to `1e-35`.
4. The reduced map and Wigner identity compose to one explicit full one-wedge matrix anti-linear relation; matrix residuals over all frozen rho/beta/lane points are `<=1e-35`.
5. A deliberately wrong rho sign, magnetic reversal, or phase table is rejected at at least one frozen point.
6. The previously frozen coefficient witness still satisfies `c(-kappa)=conj(c(kappa))`; this is only an adversarial control and not by itself the vertex-level decision.

## NEGATIVE / ADVERSARIAL CONTROLS

- Do not infer a joint K5 collision-extension action merely from a one-wedge identity.
- Do not identify the real scalar `delta_N` assumption with a source theorem about the representation-valued joint distribution.
- Do not use semiclassical phase reversal as a substitute for the exact matrix transformation.
- Do not import an auxiliary common regulator, order of limits, boundary-state transformation, or new normalization after preregistration.
- Do not classify a missing joint action as elimination of the witness.

## PASS

Classify

`SOURCE_J1_K5_VERTEX_LEVEL_CONJUGATION_DERIVED_AND_COUNTERTERM_DECIDED_SCOPED`

iff all positive controls pass **and** the frozen source chain plus the derived full one-wedge map uniquely determines the action on the collision-supported joint distribution sufficiently to decide the frozen witness, with no added model data.

The result must state explicitly whether the witness is excluded or preserved.

## FAIL

Classify

`SOURCE_J1_K5_VERTEX_LEVEL_CONJUGATION_DERIVATION_CONTRADICTS_FROZEN_SOURCE_SCOPED`

iff the frozen source formulas or magnetic reconstruction are internally inconsistent with every candidate map while all input/provenance checks remain valid, or if a uniquely source-derived complete map exists and the preregistered algebraic controls demonstrate that the previously claimed coefficient covariance was false in the same realization.

A scientific FAIL requires an actual contradiction, not missing authority.

## BLOCKED / INVALID

Classify

`SOURCE_J1_K5_VERTEX_LEVEL_CONJUGATION_JOINT_EXTENSION_ACTION_BLOCKED_SCOPED`

iff the one-wedge representation-valued map is uniquely derived and verified but the frozen source chain does not determine a unique action on collision-supported **joint** K5 extension terms without an additional joint limiting/normalization/boundary-transformation prescription.

Classify `INVALID_DERIVATION_GATE` if source blobs do not match, the candidate family is changed after seeing outputs, multiple reduced candidates survive without resolution, the algebraic verification is skipped, or any non-terminal Iter504/Iter461 substantive value is consumed.

## INTERPRETATION CEILING

Any PASS/BLOCKED/FAIL is limited to the fixed `j=1`, channel-`00000`, full-collision conjugation question and the frozen repository/source realization. It does not prove or disprove the full EPRL/FK model, all spins/channels/collision strata, source-order distributional existence, D7-S2/S3/S4 closure, any terminal D7 selector, Candidate Gravity, or any global quantum-gravity claim.

In particular, `BLOCKED_SCOPED` means the source-derived one-wedge map is insufficient to select the joint collision extension from the frozen data; it is not physical nonuniqueness and not scientific falsification.

## OUTPUT / PROVENANCE CONTRACT

The gate must durably record:

- prereg commit SHA;
- exact code and workflow SHAs if computation is used;
- raw canonical JSON with candidate counts, map, residuals/controls and joint-decision audit;
- Actions run/job/artifact IDs and artifact digest when Actions is used;
- terminal result and recovery handoff;
- all claim ceilings and governance locks.

## GOVERNANCE

- `RQIR Core v1.0 = FROZEN`.
- `D7-S2 = NOT_CLOSED`.
- `D7-S3 = NOT_CLOSED`.
- `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`.
- terminal D7 selectors and `EXISTING_SUFFICIENT / ADAPT_EXISTING / HYBRID_REQUIRED / NEW_REQUIRED` forbidden.
- Candidate Gravity inactive.

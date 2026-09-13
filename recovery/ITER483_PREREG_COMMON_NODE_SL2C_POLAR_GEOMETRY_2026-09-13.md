# Iter483 preregistration — common-node SL(2,C) polar geometry

Date: 2026-09-13
Status: FROZEN BEFORE IMPLEMENTATION
Parent authority: terminal Iter482.

## Scientific question
Can the next D7-S2 layer be equipped with a numerically stable, gauge-consistent common-node noncompact `SL(2,C)` geometry in which all ten K5 relative group elements come from five shared node elements and each relative element admits a controlled positive-polar decomposition with a well-defined boost rapidity? This gate qualifies decomposition machinery only; it does not insert a guessed boost dependence into the Toller kernel.

## Scope lock
This is a kinematic/decomposition prerequisite. PASS does not establish Eq.(7) boost coefficients, Haar convergence, spectral convergence, a physical causal-vertex value, D7-S2 closure, a terminal D7 classifier or Candidate Gravity authorization.

## Frozen construction
- K5 with five node matrices `g_a in SL(2,C)` and node 0 identity.
- Each nontrivial node is deterministically constructed as `g = U_L diag(exp(eta/2), exp(-eta/2)) U_R` from fixed SU(2) Euler rotations and a positive rapidity.
- Four deterministic angular panels crossed with two boost regimes `{mild,strong}` = 8 independent lanes, `fail-fast:false`.
- All ten oriented relative elements use one frozen convention `h_ab = g_b^{-1} g_a` for `a<b`.
- Left polar decomposition uses `h = H U`, `H = sqrt(h h^†)`, `U=H^{-1}h`; eigenvalues of positive Hermitian `H` define `eta_edge = log(lambda_max/lambda_min) >= 0`.

## Frozen checks
A. Node determinants: `max |det(g_a)-1| < 1e-11`.
B. Relative determinants: `max |det(h_ab)-1| < 1e-11`.
C. Shared-node triangle-cycle consistency: `h_bc h_ab = h_ac` for all ten K5 triangles, max residual `<1e-11`.
D. Common-left gauge covariance: for a fixed nontrivial `G in SL(2,C)`, replacing all nodes by `G g_a` leaves every `h_ab` unchanged, max residual `<1e-11`.
E. Polar Hermiticity: `max ||H-H^†||_max <1e-11`.
F. Positive definiteness: all polar eigenvalues strictly `>1e-10`.
G. Polar determinant: `max |det(H)-1| <1e-10`.
H. Unitary factor: `max ||U^†U-I||_max <1e-10` and `max |det(U)-1| <1e-10`.
I. Reconstruction: `max ||H U-h||_max <1e-10`.
J. Rapidity consistency: every extracted `eta_edge` finite/nonnegative; additionally singular values of `h` must match polar eigenvalues to relative error `<1e-10`.
K. Inversion consistency: the unordered rapidity extracted from `h_ab^{-1}` agrees with `eta_edge` to `<1e-10`.
L. Deliberate corrupted-relative-element control: left-multiply exactly one edge by a fixed noncommuting `SL(2,C)` boost while leaving all other edges untouched; at least one triangle closure residual must exceed `1e-4`.
M. Compact-limit regression: with all input node rapidities set to zero on the same angular panels, every edge rapidity must be `<1e-10` and the relative matrices must be unitary to `<1e-10`.

## PASS rule
PASS iff A-M pass in all 8 production lanes. Frozen PASS label:
`ITER483_COMMON_NODE_SL2C_POLAR_GEOMETRY_QUALIFIED_SCOPED`.

A valid-control failure is a SCIENTIFIC/NUMERICAL QUALIFICATION FAIL for this decomposition method and must not be repaired by weakening thresholds. Dependency/runtime/serialization failure is infrastructure failure; only a minimal causal repair is allowed with frozen science unchanged.

## Interpretation lock
Even full PASS qualifies only common-node noncompact group geometry and polar/rapidity extraction. It does not identify the source Toller KAK factors uniquely and does not authorize replacing published source formulas with the polar factors. A later gate must explicitly map the qualified shared-node `SL(2,C)` elements to the source-defined Toller/KAK magnetic kernel before any network or Haar conclusion.

## Next if PASS
Prospectively derive/test the source-faithful one-edge Toller factor on these noncompact shared-node elements, with explicit convention/reconstruction controls, before evaluating the ten-edge intertwiner network or Haar integral.
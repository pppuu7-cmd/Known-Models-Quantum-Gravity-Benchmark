# SYNTHESIS-002 — Physical-Helicity Parquet Closure

**Status:** REJECTED as P4 parent / retained gravity-sensitive synthesis control.  
**KMQGB iteration:** 085.  
**Purpose:** test a nonlinear recursion whose rule uses physical graviton helicities and channel unitarity, rather than scalar combinatorics.

## 1. Proposed parent idea

Take as finite seed the ordinary massless graviton propagator and the GR on-shell three-point amplitudes. Define a crossing-symmetric four-point object by coupled channel equations of schematic parquet/Bethe-Salpeter form

`M4 = K4 + Phi_s[M4,K4] + Phi_t[M4,K4] + Phi_u[M4,K4]`,

where each `Phi_c` sews two lower kernels through the corresponding channel using only physical intermediate graviton helicities and the parent-fixed Lorentzian prescription.

The intended physical principle was:

> the hard four-graviton amplitude is the minimal crossing-symmetric fixed point of its own physical two-graviton factorization channels.

Unlike SYNTHESIS-001, the nonlinear map is explicitly tied to gravitational helicity/factorization data.

## 2. A1 — explicit but not fundamental

Once `K4`, the propagator and the sewing prescription are specified, the coupled integral equations define a concrete nonlinear object.

However `K4` is the two-particle-irreducible / channel-irreducible kernel. Standard factorization does not determine its hard contact/nonlocal content from the GR three-point amplitude.

Thus the proposal has moved the missing first hard datum into `K4` rather than deriving it.

Classification:

`A1 BLOCKED__IRREDUCIBLE_HARD_KERNEL_NOT_SELECTED_BY_FACTORISATION`.

## 3. Same-factorization theorem

If one chooses `K4` so that no new hard datum is introduced beyond two-derivative GR, the fixed-point resummation is a reorganization/resummation of ordinary GR quantum-field-theory diagrams.

It does not become a new parent because its bookkeeping is self-consistent.

If one adds a new local analytic irreducible contact term to `K4`, the term lies in full C5.

If one adds a nonlocal/nonanalytic `K4`, that function must independently pass O1/O3 functional-freedom and comparator gates.

Therefore the parquet closure cannot manufacture the first comparator-orthogonal hard datum.

## 4. A2 — renormalization freedom returns

Four-dimensional quantum GR loop sewing is nonrenormalizable as a finite-coupling QFT. Repeated channel iteration requires the ordinary higher-derivative counterterm/Wilson tower unless a separate UV parent fixes it.

Hence choosing only the Einstein seed does not close the functional data of the full hard solution.

Classification:

`A2 FAIL_AS_UV_PARENT__FULL_C5_RENORMALIZATION_DATA_NOT_DERIVED`.

A finite numerical discretization or cutoff would not solve this scientific freedom; it would only regularize it.

## 5. A3 — standard QFT/resummation comparator

Bethe-Salpeter/parquet/Dyson-Schwinger/self-consistent channel equations are standard QFT resummation architectures. Applying them to GR with the GR kernel is a nonperturbative/reorganized GR calculation, not an architecture-orthogonal quantum-gravity parent.

Classification:

`A3 FAIL__STANDARD_QFT_SELF_CONSISTENT_RESUMMATION_OF_GR`.

## 6. Positive lesson

SYNTHESIS-002 does improve one thing over SYNTHESIS-001: the nonlinearity is physically gravity-sensitive and its imaginary parts/factorization channels are tied to physical helicities.

But this reveals the exact missing object:

`irreducible hard kernel / boundary datum`.

Standard unitarity determines how an irreducible datum propagates through cuts; it does not select that datum.

Thus

`unitarity sewing = propagation of hard information, not origin of hard information`.

## 7. CTP lesson

A Schwinger-Keldysh version of the same self-consistent equations can provide retarded/advanced/Keldysh components. That is useful representation completeness, but it does not repair the missing UV kernel selection. A same-parent CTP formulation is necessary, not sufficient.

## 8. Requirement for SYNTHESIS-003

The next parent attempt must derive the **irreducible hard datum itself** from a finite gravity-specific law.

It cannot use as its sole principle

- factorization;
- unitarity;
- crossing;
- Ward identities;
- CTP closure;
- or self-consistent resummation,

because these constrain/transport a hard kernel but do not uniquely choose it.

The first new datum must be prospective and independently normalized before any recursion is applied.

## 9. Score consequence

No P4 credit. R4 remains 45%.

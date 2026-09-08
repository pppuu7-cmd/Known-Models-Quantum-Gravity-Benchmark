# Parent-Principle Audit for a Future Candidate Gravity Kernel

**Status:** frozen design audit / no Candidate Gravity promotion.  
**Purpose:** distinguish principles that actually determine a momentum/tensor hierarchy from consistency conditions that merely constrain an arbitrary function.

## 1. Required standard

A viable parent principle must do more than say that a form factor is ghost-free, positive or smooth. It should prospectively determine or strongly restrict

- which tensor/helicity structures occur;
- their relative coefficients across orders;
- the momentum/cross-regime dependence;
- the Lorentzian/CTP prescription;
- the spectrum/pole/cut structure;
- the renormalization/radiative completion;
- the source-to-observable mapping.

The resulting freedom should be finite or very low dimensional before residual inspection.

## 2. P1 — S-matrix bootstrap / crossing-unitarity-Regge-softness

**Result:** `STRONG_RIGIDITY_PRECEDENT__STRING_STRUCTURAL_COMPARATOR`.

Modern bootstrap work shows that high-energy/Regge/spin/softness assumptions can strongly constrain graviton amplitudes and, in sufficiently rigid setups, can select string-like spectra/amplitudes. Recent 2026 work argues that string structure can emerge from very few amplitude assumptions.

Positive lesson: amplitude consistency can genuinely determine a hierarchy rather than fit a function.

Negative lesson for KG: a parent principle of this type must be quotiented against string/Virasoro-Shapiro and broader dual-resonance/bootstrap families. Re-deriving a string-like amplitude is not a new KG residual.

## 3. P2 — supersymmetry / duality / protected operator hierarchy

**Result:** `STRONG_PROTECTION_PRECEDENT__EXTRA_STRUCTURE_COMPARATOR`.

Type-II string gives the key example: parent symmetry/worldsheet/duality structure protects the absence of lower alpha-prime pure-gravity corrections and fixes an `R4` completion.

Positive lesson: a symmetry principle can make a quartic-first hierarchy radiatively/structurally meaningful.

Cost: extra fields/symmetries/spectrum and direct overlap with known supergravity/string comparator space. A future KG may use a different protection principle, but must state its additional structure explicitly.

## 4. P3 — nonperturbative RG fixed point / functional flow

**Result:** `KERNEL_GENERATION_PRECEDENT__ASYMPTOTIC_SAFETY_COMPARATOR`.

Asymptotic-safety calculations reconstruct momentum-dependent quantum effective actions from multi-graviton correlation functions and functional RG flows, including physical-limit momentum dependence of three- and four-graviton vertices.

Positive lesson: RG dynamics can generate momentum-dependent form factors instead of choosing them by hand.

Negative lesson for KG: this is already an existing comparator class and carries truncation/scheme/continuation questions. A candidate using a fixed-point principle must demonstrate a residual beyond the corresponding asymptotic-safety prediction in the same physical observable/domain.

## 5. P4 — causal/discrete microstructure

**Result:** `STRUCTURAL_PRECEDENT__BLOCKED_COMPLETE_SPIN2_PARENT`.

Causal/discrete microstructure can generate Lorentz-compatible or retarded nonlocal operators with few scales, showing that a kernel can in principle descend from microscopic structure.

Current blocker: no sufficiently complete, stable, Lorentzian quantum spin-2 CTP/four-graviton parent with the full Ward/observable apparatus has been established for the KMQGB use case. Scalar/nonlocal kinematic precedents are not enough.

## 6. P5 — positivity/spectral density/extremality alone

**Result:** `INSUFFICIENT_KERNEL_SELECTION_PRINCIPLE`.

Positive spectral density, ghost freedom, Hankel positivity, positivity-cone extremality or good UV falloff constrain theory space but generally leave families of allowed kernels/amplitudes.

They are consistency/geometry tools, not by themselves a parent derivation.

## 7. Current conclusion

Every presently tested strong kernel-selection mechanism falls into one of three categories:

1. **strong enough but already a known comparator architecture** — string/bootstrap, asymptotic safety;
2. **strong enough only with substantial extra structure/spectrum** — supersymmetry/duality/string-like protection;
3. **not yet complete enough for the required spin-2 observable** — causal/discrete microstructure;
4. **too weak to select a unique hierarchy** — positivity/ghost-freedom/spectral constraints alone.

Therefore the future KG parent principle must satisfy two simultaneous requirements:

`RIGIDITY`: fix a low-dimensional tensor/momentum hierarchy before data;

`NOVELTY`: generate a common-domain relation not contained in string-like, asymptotic-safety, full-C5 or other registered comparator manifolds.

## 8. Machine-record consequence

Add parent-principle metadata to future exploratory records:

- `parent_principle_id`;
- `principle_assumptions`;
- `predicted_free_parameters/functions`;
- `protection_or_RG_closure_ref`;
- `known_architecture_comparator_refs`;
- `derived_tensor_hierarchy_ref`;
- `derived_momentum_kernel_ref`;
- `Lorentzian_CTP_ref`.

If the kernel is still chosen by hand, `G0=BLOCKED_ARBITRARY_FUNCTIONAL_FREEDOM`.

## 9. Promotion status

No tested parent principle currently gives a new comparator-surviving Candidate Gravity residual. No ansatz is promoted.

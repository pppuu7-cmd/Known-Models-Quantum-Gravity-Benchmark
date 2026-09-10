# PF2-01 — Nonlocal Quantum Gravity / Ricci-sector field-redefinition subclass

**KMQGB iteration:** 184  
**RQIR Core:** v1.0 FROZEN  
**Coverage parent:** `NONLOCAL_QG`  
**Benchmark scope:** weakly nonlocal Ricci-sector gravity and gravity+matter theories whose nonlocal deformation is proportional to the local equations of motion and is related to the local theory by an analytic/nonlocal field redefinition; no independent Riemann/Weyl-sector deformation is admitted in the closed subbenchmark.

## Question

Does this controlled nonlocal-QG subclass generate a tree-level on-shell scattering residual that survives the full GR comparator, or is the apparent UV-modified theory scattering-equivalent to Einstein gravity in the declared domain?

## Declared realization

A representative gravitational action can be written schematically as

`S = (1/2 kappa^2) ∫ sqrt(|g|) [R + R gamma_0(Box) R + R_mn gamma_2(Box) R^mn + V(R,R_mn)]`,

with analytic weakly-nonlocal form factors chosen for perturbative unitarity and super-renormalizability/finiteness, and with the potential arranged so that the deformation belongs to the equation-of-motion-squared class covered by the field-redefinition theorem.

The closed benchmark specifically excludes an independent term

`R_mnrs gamma_4(Box) R^mnrs`

(or an equivalent Weyl-basis deformation) unless separately shown to be reducible to the same field-redefinition class.

## Primary authority

1. L. Modesto, G. Calcagni, *Tree-level scattering amplitudes in nonlocal field theories*, JHEP 10 (2021) 169, arXiv:2107.04558v2.
2. P. Donà, S. Giaccari, L. Modesto, L. Rachwał, Y. Zhu, *Scattering amplitudes in super-renormalizable gravity*, JHEP 08 (2015) 038, arXiv:1506.04589.
3. L. Modesto, *Nonlocal Spacetime-Matter*, arXiv:2103.04936.
4. S. Giaccari, *Causality and Scattering Amplitudes in Nonlocal Gravity*, Handbook of Quantum Gravity (Springer, 2024), DOI 10.1007/978-981-99-7681-2_33.

## RQIR object

Observable vector:

`O_tree = {A_n(on-shell external gravitons/matter; fixed asymptotic states)}`

for arbitrary tree-level multiplicity inside the theorem's action class.

Comparator:

`C_GR = {A_n^Einstein for identical external states, masses/couplings and asymptotic normalization}`.

Published field-redefinition result:

`A_n^NLQG(tree) = A_n^GR(tree)`

throughout the theorem's declared class.

Therefore the comparator-subtracted residual is

`R_NLQG(tree) = A_n^NLQG - A_n^GR = 0`.

This zero is **not** a zero-fill for missing information: it is a theorem-backed exact comparator identity for the scoped tree-level S-matrix.

## Structural gates

### Physical normalization — PASS

The comparison is performed on on-shell scattering amplitudes with the same asymptotic local-theory states and couplings; no arbitrary rescaling is used to manufacture equality.

### GR infrared map — PASS in declared observable

The entire closed tree-level S-matrix equals the Einstein comparator, which is stronger than merely approaching GR at low energy for this observable.

### Perturbative unitarity / UV consistency — SCOPED PASS

The admitted form-factor class is constructed to preserve perturbative unitarity and improve renormalizability, with finite subclasses available. This is a consistency control, not a proof that every nonlocal gravity action is unitary.

### Macro-causality — SCOPED PASS

For the same weakly nonlocal Ricci-sector class, the scattering/field-redefinition structure supports absence of the Shapiro time advance in the stated high-energy weak-coupling regime. This cannot be transferred automatically to Weyl/Riemann-basis variants.

### Comparator quotient — EXACT IDENTITY

The complete tree-level on-shell amplitude vector lies in the GR comparator identity class. It supplies **no unique tree-level residual direction** for RQIR.

## Negative control / family-boundary test

The 2015 four-graviton analysis and the 2021 theorem both make the boundary important: once an independent Riemann-squared form factor is added (apart from the four-dimensional Gauss-Bonnet exception), the scattering amplitudes need not equal GR and can depend on the new form factor. The 2024 Handbook chapter similarly warns that nonlocal gravity in a Weyl basis can have different causality properties.

Therefore it would be scientifically invalid to promote the exact identity of this Ricci/EOM-squared subclass to a family-level statement `NONLOCAL_QG = GR`.

## RQIR classification

Scoped child benchmark:

`PASS_RQIR_GATE__EXACT_COMPARATOR_IDENTITY__TREE_S_MATRIX`

Interpretation:

`SCOPED_NONLOCAL_RICCI_EOM_SQUARED_SUBCLASS_HAS_NO_TREE_LEVEL_SCATTERING_RESIDUAL_BEYOND_GR`

This is **not** a scientific FAIL of nonlocal quantum gravity. The theory may differ in loop observables, off-shell quantities, cosmology, singularity structure, or in materially distinct Riemann/Weyl-sector subclasses.

## Parent-family status

`NONLOCAL_QG = PARTIAL_SUBFAMILY_ONLY`

The parent cannot become terminal until materially distinct nonlocal subclasses are resolved, minimally including:

1. Ricci/EOM-squared weakly nonlocal finite class — closed here at tree S-matrix identity;
2. Riemann/Weyl-sector nonlocal class — requires its own normalized amplitude/causality comparator;
3. if retained as independent, nonlocal matter-coupled or cosmological sectors whose physical observables are not covered by the field-redefinition S-matrix theorem;
4. family-level proof showing whether those branches exhaust the materially independent RQIR directions.

## Exact next gate inside NONLOCAL_QG

`PF2_01B_NONLOCAL_RIEMANN_WEYL_SCATTERING_CAUSALITY_CERTIFICATE`

Required payload:

`{declared Riemann/Weyl nonlocal action, entire/form-factor prescription, physical pole/unitarity prescription, normalized on-shell amplitude or eikonal observable, GR/local-EFT comparator, causality/time-delay observable, approximation/error authority, proof of material independence from the Ricci field-redefinition class}`.

## Global impact

- D2A remains open: major-school census is not resolved.
- D2B remains open: parent `NONLOCAL_QG` is only partial.
- D4 gains one additional **defined scoped child residual**, exactly zero after GR subtraction.
- No family-level exclusion evidence is produced.
- D7 remains `NOT_CLOSED`.
- `NEW_REQUIRED` remains forbidden.
- Candidate Gravity remains inactive.

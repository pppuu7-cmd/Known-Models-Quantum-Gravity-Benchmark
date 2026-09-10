# IIB / IKKT matrix model — GR-emergence to observable closure audit (Iter236)

**Date:** 2026-09-10  
**RQIR Core:** v1.0 FROZEN  
**Parent family:** `STRING_MTHEORY_HOLOGRAPHY`  
**Branch:** `IIB_IKKT_MATRIX_MODEL`  
**Gate:** `IIB_IKKT_MATRIX_MODEL_GR_EMERGENCE_TO_NORMALIZED_OBSERVABLE_COMPARATOR_ERROR_AUDIT`

## Question

Do the 2026 IIB/IKKT results now close a same-realization chain

`matrix path integral / large-N realization -> selected 3+1 Lorentzian spacetime -> massless spin-2 / GR dynamics -> normalized physical gravity observable -> GR/EFT comparator -> large-N/truncation/state error ledger`?

## A. Direct low-energy gravity bridge — major positive control

Ho, Kawai and Steinacker, JHEP 2026, *General Relativity in IIB matrix model* (arXiv:2509.06646), treat matrices as bilocal fields around a Lorentz-invariant vacuum. They show that the low-energy bilocal sector reduces to local fields containing finitely many massless fields and infinitely many massive fields, formulate unitarity conditions, and explain the emergence of diffeomorphism invariance and the gravitational field.

Classification:

`PASS_SCOPED_IIB_MATRIX_LOW_ENERGY_LOCAL_FIELD_GRAVITY_DIFFEO_UNITARITY_BRIDGE`.

This retires an obsolete blocker of the form `no explicit GR/graviton bridge from IKKT`.

## B. Four-dimensional supersymmetry constraints — positive dimensional-selection information, not a cosmological closure

Muramatsu, Nucl. Phys. B 1030 (2026) 117610, analyzes the leading low-energy effective action subject to supersymmetry closure and Ward identities. Generic 10D leading-order fluctuations are frozen by a non-renormalization theorem. In 4D, Hodge duality opens a special algebraic route, but the nontrivial solutions in that analysis are restricted to Euclidean (anti-)self-dual configurations and are interpreted as primordial/nonperturbative vacuum-like configurations rather than a macroscopic time-evolving universe.

Classification:

`PASS_SCOPED_4D_ALGEBRAIC_SELECTION_CONSTRAINT__BLOCKED_DIRECT_Lorentzian_DYNAMICAL_IDENTIFICATION`.

## C. Lorentzian kappa-Minkowski-like sector — genuine but kinematic

Muramatsu, Nucl. Phys. B 1031 (2026) 117638 / arXiv:2606.03496, obtains a Lorentzian four-dimensional kappa-Minkowski-like algebra from restricted off-shell supersymmetry closure and spatial isotropy. A nontrivial realization requires an `N -> infinity` or unbounded-operator limit. The paper explicitly treats the expansion/internal-static pattern as algebraic/kinematic rather than physical time evolution or demonstrated dynamical compactification.

Classification:

`PASS_SCOPED_Lorentzian_4D_KINEMATIC_ALGEBRAIC_SECTOR__BLOCKED_DYNAMICAL_SELECTION_AND_OBSERVABLE_TRANSPORT`.

## D. Same-realization composition gate

The three 2026 controls above cannot be automatically spliced into one terminal object:

- Ho–Kawai–Steinacker use a bilocal low-energy realization and derive a gravity/diffeomorphism/unitarity structure;
- the Euclidean self-dual analysis and the Lorentzian kappa-Minkowski-like analysis impose different low-order algebraic ansatze/branches;
- neither Muramatsu result supplies a demonstrated dynamical probability/selection weight showing that its branch is the same vacuum used by the GR-emergence construction;
- no audited source closes a common parameter map, large-N limit, vacuum-selection rule and detector-facing observable across these ingredients.

Therefore D6 forbids treating

`GR bridge + 4D selection + Lorentzian algebra`

as a single proven same-realization chain without an explicit equivalence map.

## E. Missing physical observable object

A normalized low-energy gravitational observable tied to the same nonperturbative matrix realization is still required. The minimum useful object would contain:

1. a fixed IKKT integration prescription / vacuum sector;
2. a demonstrated large-N or continuum selection of a 3+1 Lorentzian geometry;
3. the same-sector graviton/metric effective action and coupling normalization;
4. one normalized scattering, response, cosmological, black-hole or propagation observable;
5. a same-domain GR/EFT prediction;
6. finite-N, effective-action truncation, vacuum/state and numerical/systematic uncertainties.

No such complete object was located in the bounded 2025–2026 primary-authority sweep.

## Branch disposition

The IIB/IKKT branch is materially stronger than the previous first-pass family label, but remains nonterminal:

`PARTIAL_SUBFAMILY_ONLY__DIRECT_LOW_ENERGY_GRAVITY_DIFFEO_UNITARITY_BRIDGE_PASS__4D_ALGEBRAIC_SECTORS_EXIST__SAME_REALIZATION_Lorentzian_DYNAMICAL_SELECTION_TO_NORMALIZED_GRAVITY_OBSERVABLE_ERROR_CHAIN_BLOCKED`.

Exact missing certificate:

`IKKT_FIXED_MATRIX_REALIZATION_TO_DYNAMICAL_3P1_LORENTZIAN_VACUUM_PLUS_NORMALIZED_GRAVITY_OBSERVABLE_GR_COMPARATOR_FINITE_N_ERROR_CERTIFICATE`.

This is **not** a scientific FAIL and contributes zero exclusion evidence toward `NEW_REQUIRED`.

## Paper-III impact

No new transferable Paper-III failure class appears. The apparent ability to assemble complementary ingredients from nearby IKKT papers is another instance of the already-frozen same-realization/provenance rule.

`PAPER_III_REOPEN = NO`.

## Heavy compute

`CONDITIONAL_HIGH_VALUE`.

IKKT is now one of the branches where numerical large-N vacuum selection could become decision-relevant, but only if tied prospectively to the same observable/effective-gravity extraction. A generic matrix simulation without the frozen observable cannot close the RQIR object.

## Next gate

The next highest-information String-family branch is holography, because it offers an exact boundary quantum theory in fixed AdS sectors but the family-level question hinges on the scope and errors of bulk observable reconstruction:

`ADSCFT_FIXED_BOUNDARY_NONPERTURBATIVE_DEFINITION_TO_FINITE_N_BULK_OBSERVABLE_COMPARATOR_AUDIT`

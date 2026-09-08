# Spectral-Origin Completeness for Beyond-C5 Quartic/Higher Structure

**Status:** frozen pre-ansatz methodology / no Candidate Gravity promotion.  
**Purpose:** require every claimed candidate-specific quartic/higher contribution to identify the UV spectral/growth origin that supports it, rather than treating a Wilson coefficient or nonlocal form factor as unexplained input.

## 1. Scoped local dispersive setup

For amplitudes in a declared local/polynomially or appropriately Regge-bounded class, suitably subtracted/smeared/crossing-symmetric dispersion relations relate covered low-energy amplitude coefficients to high-energy discontinuities or positive spectral averages.

Schematically,

`c_IR = c_known,IR + integral_(UV) dmu rho(mu) W(mu)`

for those coefficient combinations that genuinely obey the chosen gravitational sum rule.

The exact kernel `W`, subtraction structure and helicity projection are observable-specific.

## 2. Spectral-origin tax

After the full matched C5 low-energy/loop contribution is removed, a genuinely new dispersively controlled coefficient or linked coefficient relation requires a difference in the high-energy data that feeds the sum rule, for example

- additional massive states;
- a new multiparticle continuum/composite sector;
- altered spectral weights or Regge residues/trajectories;
- other UV discontinuity support allowed by the declared parent.

Therefore a candidate cannot simply postulate a new `R4` coefficient and simultaneously claim “no new UV spectral information” under the same dispersive assumptions.

This does not require the new support to be a new elementary particle; strongly coupled/composite/continuum support also counts.

## 3. Gravity-loop caveat

Naive forward positivity is unreliable in gravity because massless graviton exchange and graviton loops generate forward singularities and low-energy contributions to dispersion sum rules.

Therefore before applying the spectral-origin tax, the candidate/comparator must freeze an admissible gravitational prescription, e.g.

- crossing-symmetric dispersion relations;
- appropriate momentum-transfer smearing;
- explicit subtraction of known low-energy graviton contributions;
- a demonstrably finite helicity/eigenchannel sum rule.

A naive forward-limit sign argument is not authority.

## 4. Subtraction-constant caveat

Not every low-order polynomial coefficient is necessarily determined by a given dispersion relation; some may remain subtraction constants.

If a candidate-specific coefficient lies outside the controlled dispersive moment set, classify its spectral origin as

`BLOCKED_NOT_FIXED_BY_CURRENT_SUM_RULE`

rather than infer new spectral support.

Such a coefficient still does not become KG novelty: the parent principle must explain why its value/relation is fixed and comparator-resistant.

## 5. Nonlocal dispersion class

For exponentially bounded/nonlocal amplitudes, standard polynomial-bounded local positivity/sum-rule formulas need not apply.

Use the `D-nonlocal` branch frozen in `QUARTIC_HELICITY_MOMENT_RIGIDITY.md` and the appropriate modified dispersion relations.

Recent nonlocal positivity analyses show that exponentially bounded, unitary and causal amplitudes can occupy EFT regions not reachable by local UV completions.

Thus a future KG may escape the local spectral-origin relation only by explicitly paying the **nonlocal dispersion-class tax**: the nonlocality/growth assumption becomes part of the parent claim and requires its own UV causality and comparator audit.

## 6. Spectral-origin dichotomy

For a candidate-specific quartic/higher relation that survives full-C5 matching, prospectively classify:

### S-local

A valid local gravitational sum rule exists. Record the additional/modified high-energy spectral or Regge support responsible for the residual.

### S-nonlocal

The amplitude belongs to a nonlocal/exponentially bounded class. Record the modified dispersion relation, nonlocality scale/growth parameters and UV-causality assumptions.

### S-unresolved

No applicable sum rule or nonlocal dispersion authority is available. The origin is `BLOCKED`, never inferred.

## 7. No-new-spectrum consequence

A “minimal KG with no additional UV spectral support whatsoever” is strongly constrained in the local dispersive branch.

If

- the light spectrum and all high-energy discontinuity data are identical to full C5 in the relevant sum rule;
- the asymptotic/Regge assumptions and subtraction data are also identical;

then the covered dispersive coefficient combinations cannot acquire an independent candidate-specific shift.

This is a scoped dispersive identity, not a global theorem about every conceivable nonlocal/nonperturbative gravity theory.

## 8. Cross-representation use

The same spectral data should consistently control, where the parent allows,

- in-out discontinuities/cross sections;
- retarded/ordered real-time spectral functions;
- induced detector/response kernels.

This creates a natural bridge to `CROSS_REPRESENTATION_RIGIDITY.md`, but generic spectral/dispersion consistency remains ordinary QFT/C5 structure. KG novelty requires a specific spectral relation that survives comparator profiling.

## 9. Candidate record additions

Future candidate blocks should record

- `dispersion_class`;
- `sum_rule_ref`;
- `low_energy_known_subtraction_ref`;
- `candidate_specific_coefficient_set`;
- `spectral_origin_class` (`S-local`, `S-nonlocal`, `S-unresolved`);
- `spectral_support_or_nonlocal_growth_ref`;
- `gravity_loop_IR_treatment_ref`;
- `subtraction_constant_status`.

Missing origin authority blocks the relevant novelty gate.

## 10. Promotion status

This protocol narrows the possible origin of a future `DeltaGamma_KG`. It does not identify such a residual and does not promote a Candidate Gravity ansatz.
# Projectable Hořava gravity — UV RG to IR GR/extra-scalar closure audit (Iter220)

**Date:** 2026-09-10  
**RQIR Core:** v1.0 FROZEN  
**Family:** `HORAVA_LIFSHITZ`  
**Branch:** projectable 3+1 theory  
**Gate:** `HORAVA_PROJECTABLE_UV_RG_TO_IR_GR_EXTRA_SCALAR_NORMALIZED_OBSERVABLE_CLOSURE`

## Question

Does the strongest current 3+1 projectable Hořava result close one same-realization chain

`asymptotically-free UV trajectory -> relevant-operator completion -> stable/weakly-coupled IR near-GR regime -> extra-scalar disposition -> normalized physical observable -> same-domain GR/EFT comparator -> propagated RG/phenomenology errors`?

## A. UV renormalization and RG control — strong positive result

Projectable Hořava gravity is perturbatively renormalizable, and the full one-loop beta functions for the marginal essential couplings in 3+1 dimensions have been computed. Barvinsky, Kurov and Sibiryakov then mapped the fixed points and global marginal-coupling trajectories.

The 2024 global-flow analysis identifies a unique asymptotically-free fixed-point family whose trajectories span the unitary kinetic-coupling region and can reach `0 < lambda - 1 << 1`, the regime used in GR-like phenomenology. The trajectories follow an almost universal path in the essential marginal couplings, differing mainly through the gravitational coupling.

Classification:

`PASS_SCOPED_PROJECTABLE_3PLUS1_UV_RENORMALIZATION_AND_MARGINAL_RG_TRAJECTORY`.

## B. Near-GR running is necessary but explicitly not sufficient

The same 2024 authority states that reaching a phenomenologically interesting IR region is only a necessary condition. Its computed flow retains the marginal operators dominating above the Lorentz-violation scale but omits the relevant operators that control the true low-energy completion.

Those relevant operators can change the flow before the trajectory reaches the strong-coupling region. Their effect is expected to be decisive for matching to low-energy gravity, but that matching is outside the calculation.

Therefore the existing RG curve cannot be promoted to a complete UV-to-observable trajectory.

Classification:

`BLOCKED_PROJECTABLE_RELEVANT_OPERATOR_IR_MATCHING`.

## C. Extra scalar / IR stability and strong coupling

The projectable theory contains an additional scalar mode. The literature has long identified an instability/strong-coupling tension in the naive IR treatment near the GR point. Nonlinear gradient-expansion work shows that some apparent singular behavior of perturbation theory can be avoided and that a continuous GR-like limit can exist in a declared cosmological long-wavelength regime, so the correct classification is not a blanket failure of the scalar sector.

However the 2024 RG paper itself emphasizes that the full IR theory including relevant operators has an instability that can only be suppressed at the cost of strong coupling in the standard projectable setup, and it deliberately does not resolve this issue. It treats the projectable model as a useful RG toy model for more complicated stable versions.

Thus the decisive projectable same-realization IR stability/strong-coupling disposition remains open.

Classification:

`BLOCKED_PROJECTABLE_SAME_TRAJECTORY_EXTRA_SCALAR_IR_STABILITY_STRONG_COUPLING_DISPOSITION`.

## D. Physical observable layer

High-energy projectable graviton scattering amplitudes are known and provide a useful UV physical-observable control. Low-energy/cosmological solutions and phenomenological constraints also exist in various projectable extensions/parameter regimes.

But the RQIR family object requires the *same* fixed UV trajectory to be transported through the relevant-operator crossover into a viable IR realization and then into a normalized observable. No audited object was located that binds all these stages with one parameter ancestry and one uncertainty ledger.

Using an observable from a U(1)-extended, differently coupled, or otherwise modified Hořava realization without an explicit mapping would violate same-realization discipline.

## E. Comparator/error closure

A projectable family residual cannot be defined until the chain fixes:

- where the marginal RG flow is cut off by relevant operators;
- the resulting IR values of `lambda`, Newton coupling and Lorentz-violation scale;
- scalar-mode stability/strong-coupling status in that same realization;
- matter coupling prescription;
- normalized observable and GR/EFT comparator;
- RG truncation, matching, observational and approximation uncertainties.

Those ingredients are not jointly frozen by current authority.

## Projectable branch result

The projectable branch is substantially stronger than a generic `PARTIAL` row because its UV/marginal RG structure is explicit and unusually constrained. Nevertheless it remains nonterminal:

`PARTIAL_SUBFAMILY_ONLY__PROJECTABLE_UV_RG_STRONG_PASS__IR_RELEVANT_OPERATOR_SCALAR_OBSERVABLE_CLOSURE_BLOCKED`.

Exact missing certificate:

`HORAVA_PROJECTABLE_SAME_REALIZATION_RELEVANT_OPERATOR_MATCHED_UV_TO_IR_STABLE_EXTRA_SCALAR_NORMALIZED_OBSERVABLE_COMPARATOR_ERROR_CERTIFICATE`.

This is **not** a scientific FAIL of projectable Hořava gravity and contributes zero exclusion evidence toward `NEW_REQUIRED`.

## Important update to family census

The old family note that non-projectable renormalization remained only an unresolved obstacle is now stale. Bellorín, Borquez and Droguett (2024) explicitly present a proof of renormalization for the non-projectable Hořava theory using a BRST/background-field construction after cancellation of irregular-loop divergences.

Therefore the non-projectable branch must now receive its own fresh audit rather than being left as an old unresolved-renormalization placeholder.

## Paper-III impact

No new transferable Paper-III failure mode appears. The new lesson is still an instance of end-to-end resource closure: a strong UV calculation cannot substitute for missing IR matching, nuisance/extra-mode disposition and observable normalization.

`PAPER_III_REOPEN = NO`.

## Heavy compute

`IDLE_FOR_PROJECTABLE_GLOBAL_CLASSIFICATION`.

The current blocker is not lack of numerical precision in the marginal RG system. A decision-changing computation would require a controlled inclusion of the relevant operators and same-realization IR matching; merely integrating the already-frozen marginal beta functions more accurately cannot close the branch.

## Next Hořava gate

Advance immediately to the materially distinct non-projectable branch:

`HORAVA_NONPROJECTABLE_RENORMALIZATION_TO_IR_VIABLE_OBSERVABLE_COMPARATOR_AUDIT`.

The audit must verify the scope of the 2024 renormalization proof, identify whether a usable RG trajectory/fixed-point structure exists, bind it to the low-energy stable parameter region and then test for a normalized observable/comparator/error chain. Only after projectable and non-projectable branches have explicit dispositions can the Hořava family approach family-level closure.

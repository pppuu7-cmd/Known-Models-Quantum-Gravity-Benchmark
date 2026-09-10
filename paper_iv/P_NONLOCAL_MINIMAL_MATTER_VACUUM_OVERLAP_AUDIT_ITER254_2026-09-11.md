# NONLOCAL_QG minimal-matter / vacuum form-factor overlap audit — Iter254

**Date:** 2026-09-11  
**RQIR Core:** v1.0 FROZEN  
**Family:** `NONLOCAL_QG`

## Gate
Resolve the Iter253 saturation question: does the 2026 vacuum Gödel-CTC realization lie outside the minimally-coupled super-renormalizable class studied in 2023, or is it a vacuum sector of the same Ricci–Weyl gravitational family with overlapping admissible form factors?

## Authorities
1. Z. Zhao & L. Modesto, *Quantum avoidance of Gödel’s closed timelike curves*, Eur. Phys. J. C 83, 517 (2023), arXiv:2304.10318.
2. Z. Zhao, L. Modesto & C. Bambi, *Acausal exact vacuum solutions in nonlocal gravity*, Eur. Phys. J. C 86, 713 (2026), arXiv:2605.01413.
3. L. Modesto, *Nonlocal Spacetime-Matter*, arXiv:2103.04936.

## Result 1 — gravitational action overlap is explicit
The 2023 minimally-coupled analysis uses the Ricci–Weyl gravitational action

`EH + R gamma0(Box) R + Ric gamma2(Box) Ric + Weyl gamma4(Box) Weyl + S_m`

with a cosmological term allowed. The 2026 vacuum paper studies the same Ricci–Weyl gravitational sector with `S_m=0` and zero cosmological constant in the vacuum equations. Its Appendix B explicitly writes the corresponding general equations with both `Lambda_cc` and `S_m` restored.

Therefore the 2026 theory is not a disjoint gravitational architecture; it is a vacuum specialization of the same broad minimally-coupled Ricci–Weyl class.

## Result 2 — renormalizable form-factor classes overlap
The 2023 analysis characterizes unitary/super-renormalizable realizations by nonzero entire functions `H0,H2` with `H0(0)=H2(0)=0` and asymptotically polynomial/Kuzmin-type behavior.

The 2026 paper uses the same type of entire-function form factors and explicitly imposes the super-renormalizable relation

`gamma2 + 2 gamma4 = tilde_gamma2 + 4 tilde_gamma4 = (exp(H2)-1)/Box`,

with `H2(0)=0`. It then identifies a special but large subfamily satisfying the extra infrared condition `H2'(0)=0` and constructs explicit polynomials `p(x)` for which an `m^2=0` Gödel-type CTC vacuum is an exact solution.

Hence the vacuum CTC branch overlaps the admissible super-renormalizable form-factor family rather than escaping it by becoming non-renormalizable.

## Result 3 — no contradiction with the 2023 matter-sourced PASS
The 2023 exclusion theorem is scoped to homogeneous Gödel metrics that already solve Einstein equations with their matter source/cosmological term. The authors explicitly state that they do not exclude other Gödel-type solutions solving the full higher-derivative/nonlocal equations but not Einstein's equations.

The 2026 `m^2=0` vacuum CTC solution is exactly such a different sector. Thus the two results coexist:

- nonzero matter-sourced Einstein-Gödel CTC sector: scoped exclusion in the declared super-renormalizable minimal class;
- vacuum `m^2=0` non-Einstein/full-NLG sector: scoped CTC existence for a special but large super-renormalizable form-factor subclass.

Therefore `presence of a matter sector` is not equivalent to `global chronology protection`; the actual background/source sector matters.

## Result 4 — conditional full-action inheritance
For a minimally-coupled matter theory whose matter equations admit a zero-field configuration with vanishing stress tensor and no residual vacuum-energy term, the 2026 solution is inherited by the full matter-coupled action in that zero-matter sector. This statement is conditional on the chosen matter action admitting that vacuum configuration and is not promoted beyond that scope.

## Scoped disposition
`FAIL_SCOPED_VACUUM_GLOBAL_CHRONOLOGY_GATE__SUPERRENORMALIZABLE_RICCI_WEYL_FORM_FACTOR_SUBCLASS_ADMITS_M2_ZERO_GODEL_CTC_VACUUM`.

This is stronger than a mere missing-certificate blocker, but still not a family-level `NONLOCAL_QG` fail because the 2026 paper itself shows branch dependence: e.g. some form-factor classes do not satisfy the CTC solution conditions.

## Saturation decision for the causality branch
The specific literature question opened at Iter250 is now sufficiently resolved for benchmark purposes:

1. eikonal/Shapiro causality and global chronology are distinct;
2. nonminimal spacetime-matter gives an explicit same-action split;
3. minimal Ricci–Weyl gravity has both matter-sourced scoped causal branches and vacuum scoped acausal branches within overlapping super-renormalizable form-factor families;
4. no family-level global chronology theorem is available.

Therefore repeated generic causality searching is now parked. Reopen only on a new global solution-space chronology theorem, a complete classification of the relevant fixed-action solution space, or a same-realization observable certificate that materially changes the family disposition.

## Family/global consequence
- `NONLOCAL_QG = PARTIAL_SUBFAMILY_ONLY`
- family residual = `UNDEFINED`
- `D2 = NOT_CLOSED`
- `D4 = PARTIAL_GLOBAL_NOT_CLOSED`
- `D7 = NOT_CLOSED`
- Paper IV = `NOT_YET_AUTHORIZED`
- Candidate Gravity activation = false
- canonical R3 = 24%
- heavy compute = `IDLE`

## Paper III consequence
No new resource-closure failure mode is generated for Paper III. Paper III remains `FROZEN_CLOSED`.

## Exact next gate
Return the family front from generic causality searching to the unresolved discriminator required by the coverage contract:

`NONLOCAL_QG_CROSS_ORDER_FUNCTIONAL_RIGIDITY_OR_FULL_MOMENTUM_SHAPE_CERTIFICATE__WITH_CAUSALITY_BRANCH_PARKED`.

# Iter499 diagnostic preregistration — interval dependency localization

Date frozen: 2026-09-14
Status: FROZEN DIAGNOSTIC ONLY; NO SCIENCE VERDICT

Iter499 production remains authoritative and unchanged. Early raw artifacts from `0to5-b0`, `0to5-b1`, and `1to4-b3` all return `ITER499_NUMERICAL_METHOD_BLOCKER`; in each inspected artifact every one of the 64 signed-direction/box attempts fails before contraction with `KAK eigenvalue positivity/separation not certified`.

This diagnostic localizes the numerical mechanism only. It cannot promote, repair, reinterpret, or replace Iter499.

## Frozen representative object
Use exactly:
- Iter499 direction 1 `[1,1,1,1,1,1]`;
- sign `+1`;
- amplitude box `A_0=[16/12800,17/12800]`;
- R grid `{6,8,10,12}`;
- panel C / strong shared-node geometry already frozen in Iter499.

Causal/rho data are irrelevant because the diagnostic stops before Toller branches.

## Two algebraically identical relative-matrix constructions
For escaped node `a>=1`, write the frozen node exactly as

`g_a = L_a B G_a R_a`,

where `B=boost(R)`, `G_a` is the fixed panel-C strong base element, and `L_a,R_a` are the frozen amplitude-dependent compact perturbations.

Construction N (naive, exactly the Iter499 production implementation):

`h_ab^N = inverse(ball(g_b)) ball(g_a)`.

Construction F (factorized dependency-preserving identity):
- for edge `(0,b)`,
  `h_0b^F = R_b^{-1} G_b^{-1} B^{-1} L_b^{-1}`;
- for `1<=a<b<=4`,
  `h_ab^F = R_b^{-1} G_b^{-1} B^{-1} L_b^{-1} L_a B G_a R_a`.

All inverses of compact SU(2) factors are represented by Hermitian conjugation. `G_a^{-1}` is built analytically by reversing its frozen `UL * boost(eta) * UR` factors. No determinant projection, midpoint substitution, subdivision, or threshold change is allowed.

## Frozen tests
For every R:
1. the four naive node balls must individually pass the frozen Iter499 `kak_ball` predicate;
2. record exactly which of the ten naive relative balls pass/fail `kak_ball`;
3. record exactly which of the ten factorized relative balls pass/fail `kak_ball`;
4. at the exact midpoint amplitude of A0, zero-radius N and F relative constructions must be algebraically equivalent entrywise by ball containment of zero in their difference.

## Diagnostic classifier
`ITER499_INTERVAL_DEPENDENCY_BLOWUP_CONFIRMED_SCOPED` iff:
- all four node KAK checks pass for every R;
- at least one naive relative KAK check fails;
- all factorized relative KAK checks pass;
- midpoint N/F algebraic equivalence passes on all ten edges and all four R values.

`ITER499_DEPENDENCY_DIAGNOSTIC_UNRESOLVED` otherwise.

Either classification is diagnostic only. If confirmed, the next prospective iteration after terminal Iter499 may test the factorized relative construction across the entire frozen 16-box state space as a **validated-arithmetic enabling gate**, before any repeat of the direct max-envelope science classifier.

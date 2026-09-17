# Iter504T pre-execution source audit

Date: 2026-09-17
Status: OUTCOME-BLIND PRE-EXECUTION AUDIT

This audit is performed after preregistration `aa2b0256ce60d605574a18ec86c0bad5b5df1512` and before any Iter504T scientific output.

Parent terminal authority: `1b0004064575f046210383dc7b1ee22d4f25e66b`.
Outcome-blind successor toolkit: `81e0e94649a50cccc510dc2630456af45fd98e46`.

## Source-level checks

1. Each visited interval `J` is passed directly as an Arb interval amplitude with derivative seed 1 into `iter503_ad_core.construct_dual_state`; the full-root derivative enclosure is not reused for descendants.
2. Ordinary channel values are recomputed source-faithfully at the exact rational midpoint `m_J`.
3. Channel enclosures use midpoint value plus the full local interval derivative ball times exact child displacement; no derivative midpoint, sampled derivative, fitted derivative, or finite-difference derivative is used as scientific truth.
4. Haar/log contribution is treated analogously from the local dual node KAK construction.
5. All 243 contracted channels are retained in the envelope calculation; no pruning path exists.
6. Scientific slope-floor and drift decisions are made as Arb predicates before display serialization.
7. Deterministic partition is dyadic with frozen `MAX_DEPTH=3`; assembler and Critic independently verify each terminal interval is an exact rational dyadic cell of its declared depth, not merely that the union covers the root.
8. Aggregate compares complete cross-environment scientific projections rather than float summaries.
9. Critic includes negative controls for non-dyadic/outcome-dependent partition, depth increase, root-derivative reuse, float-reconstructed predicates, channel omission/pruning, wrong threshold/floor/cohort, missing cover and missing provenance.

## Parent-inclusion diagnostic scope

The preregistered scientific validity of Iter504T rests on the direct validated local construction `D(J)`, not on an assumption that independently constructed interval derivatives must be nested componentwise inside `D(parent(J))`.

This first bounded gate therefore makes **no scientific contraction claim from serialized interval widths and no terminal decision depends on parent-inclusion nesting**. Componentwise nesting is an optional diagnostic/certificate where algebraically meaningful, but lack of such a certificate is not used as evidence against validity because independent interval dependency inflation can make valid local constructions non-nested.

The mechanism tested is operational and rigorous: whether direct local validated derivative enclosures, used in the mean-value enclosure on the prospectively frozen dyadic partition, certify the same frozen continuous-drift predicate.

## Audit conclusion

No source-level change to threshold, floor, roots, rho/R grid, precision, channel set, source route, terminal classes or maximum depth is authorized. The implementation is suitable for methodology CI and, only after that CI is terminal success and exact source hashes are frozen, one bounded scientific execution.

This audit contains no Iter504T numerical result and selects no favorable leaf, depth, channel or outcome.

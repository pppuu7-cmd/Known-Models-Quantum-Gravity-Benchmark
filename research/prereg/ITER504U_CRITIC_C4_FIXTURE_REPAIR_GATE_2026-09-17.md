# ITER504U_CRITIC_C4_FIXTURE_REPAIR_GATE — prospective formal closure freeze

Date: 2026-09-17
Status: PROSPECTIVELY_FROZEN_BEFORE_CONSUMING_ANY_REPAIR_RUN_RESULT

This formal gate incorporates without alteration the earlier outcome-blind repair freeze at commit `5ad9664e88e517cd64bd9971bac5c4c239ba4672`. At this freeze, methodology run `35250717944` is nonterminal (`queued`, `conclusion=null`) and source science run `35246605860` remains nonterminal. No held-out scientific value and no result from `35250717944` has been consumed.

## HYPOTHESIS

The Iter504U independent-Critic C4 adversarial fixture can be repaired, without changing any production science or scientific classifier, so that it deterministically constructs and rejects a structurally valid per-rho payload whose top-level leaf certification contradicts `all(rho.certified)` independently of unknown held-out scientific outcomes.

## exact OBJECT

Exactly the synthetic negative-control constructor and its isolated outcome-independent self-test in `code/iter504u_heldout_critic_c4_fixture_repair.py`, bound to the frozen Critic implementation and unchanged Iter504U production chain. This gate does not classify source run `35246605860` and does not inspect its scientific payloads.

## DEPENDENCY

- original Iter504U held-out preregistration `05b8e9354c9a7805f0fce18b904346a986a0787f`;
- immutable source-run launch head `102c7f9cafec956f3bc7bed4384ae755c98f761a`;
- original Critic blob `c2a7ea31ddc151bf02a3995d761cae95bdabd0db`;
- initial repair freeze `5ad9664e88e517cd64bd9971bac5c4c239ba4672`;
- structurally isolated repair wrapper commit `f5cd17136ddfee8864bb7a46abbdb464f666f518`, blob `bcea2946a0f9676b50897dc4bbe74fa1122a9965`;
- methodology workflow binding head `9793843843b53c1616af6fbfc72f7a8fa56a28ef`.

## SOURCE / REALIZATION AUTHORITY

Only the repository objects named above and the exact Actions execution of `.github/workflows/iter504u-critic-c4-fixture-repair-methodology.yml` at head `9793843843b53c1616af6fbfc72f7a8fa56a28ef` are authoritative for this repair gate. The active held-out science artifacts are explicitly outside this gate's decision authority.

## FROZEN INPUTS

- production evaluator blob `bf457eef08f7df32523c9e22ce3b3713f10d97a0` unchanged;
- environment assembler blob `5c3b04f25c5fb2523c3788b725ccf84ca23a07f1` unchanged;
- aggregate classifier blob `23165f9d99ff9a2f90c27a51cb889d5920327f92` unchanged;
- original Critic blob `c2a7ea31ddc151bf02a3995d761cae95bdabd0db` imported, not edited;
- repaired wrapper blob `bcea2946a0f9676b50897dc4bbe74fa1122a9965`;
- no change to held-out cohort, source realization, precision 384, 243 channels, R `[6,8,10,12]`, rho `[0.35,0.9,1.6,2.7]`, threshold `1/20`, floor `1`, `MAX_DEPTH=3`, partition/local-D rule or PASS/INCONCLUSIVE scientific semantics.

## POSITIVE CONTROLS

The isolated self-test must demonstrate, for structural carrier variants independent of unknown science, that the deterministic constructor creates internally coherent per-rho rows and that the repaired Critic rejects the intentionally contradictory top-level leaf binding. The wrapper must execute the same shared validation path used by the Critic rather than merely assert a disconnected predicate.

## NEGATIVE CONTROLS

1. A structurally coherent non-contradictory synthetic leaf must not be rejected as C4.
2. The contradictory fixture must be rejected even when the carrier baseline leaf or selected rho would originally have been uncertified.
3. Any mutation to the frozen producer/assembler/aggregate/original-Critic identities is INVALID_IMPLEMENTATION.
4. Any use of active held-out scientific payloads to choose or modify the fixture is INVALID_IMPLEMENTATION.

## PASS

`ITER504U_CRITIC_C4_FIXTURE_REPAIR_VALIDATED_SCOPED` iff the exact frozen repair identities match, the isolated outcome-independent self-test passes, the shared Critic validation path deterministically rejects the C4 contradiction, non-contradictory control remains accepted, and no production-science object or scientific criterion changes.

## FAIL

`ITER504U_CRITIC_C4_FIXTURE_REPAIR_FAIL_SCOPED` iff all provenance/implementation controls are valid but the repaired synthetic fixture does not deterministically exercise the intended C4 contradiction through the shared Critic validation path, or a coherent non-contradictory control is incorrectly rejected.

## BLOCKED / INVALID

`ITER504U_CRITIC_C4_FIXTURE_REPAIR_BLOCKED_SCOPED` iff the exact required repository/workflow object cannot be evaluated for a non-scientific infrastructure reason without establishing PASS or FAIL.

`INVALID_IMPLEMENTATION` iff any frozen object identity differs, production science/classifier changes, active held-out science influences fixture construction, the self-test bypasses the shared Critic validation path, or frozen criteria are changed after result.

## INTERPRETATION CEILING

PASS validates only the outcome-independent synthetic C4 Critic control repair. It does not classify run `35246605860`, convert its future INCONCLUSIVE to PASS, alter any held-out scientific value, authorize all-Iter504 closure, D7 closure, model/family conclusions, Candidate Gravity, Paper IV, `QUANTUM_GRAVITY_SOLVED`, `ALL_KNOWN_MODELS_FAIL`, `NEW_THEORY_REQUIRED`, or `NEW_PHYSICS_FOUND`.

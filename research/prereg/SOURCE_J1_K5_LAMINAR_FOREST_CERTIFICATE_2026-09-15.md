# SOURCE J1 K5 — exact laminar-forest certificate gate

Date: 2026-09-15
Status: PROSPECTIVELY FROZEN BEFORE IMPLEMENTATION

## Upstream premises
Use only Critic-confirmed scoped premises: K5 scalar auxiliary power count with all 50 proper collision strata superficially divergent; full-collision-only subtraction is structurally insufficient for that auxiliary witness. This gate does not transfer conclusions to Eq. (4), channel 00000, or physical EPRL without a separately proved same-object bridge.

## Frozen object
Vertex set V={0,1,2,3,4}. Because K5 is complete, every subset S with 2<=|S|<=5 is connected. A collision forest is a family F of such subsets that is laminar: for every A,B in F, A subset B, B subset A, or A intersection B is empty.

## Required exact outputs
1. Enumerate all connected collision subsets and census by |S|.
2. Enumerate every laminar family F (including empty family) exactly, with no sampling.
3. Report total forest count, maximal forest cardinality/depth, cardinality histogram, and orbit/type census under all 120 S5 vertex relabelings.
4. For each subset S compute E_int=C(|S|,2), d_perp=3(|S|-1), omega=3 E_int-d_perp, and frozen superficial subtraction order r(S)=max(0, floor(omega)).
5. For every forest report its maximal required r and nested-chain depth.
6. Verify invariance under all 120 relabelings.

## Controls
Positive: singleton forest {0,1} is valid; nested chain {0,1} subset {0,1,2} subset {0,1,2,3} subset V is valid.
Adversarial: overlapping nonnested pair {0,1} and {1,2} must be rejected. Disjoint pair {0,1},{2,3} must be accepted.
Changed-scaling control: replacing edge scaling coefficient 3 by 2 must alter at least one omega/order census entry; otherwise INVALID_IMPLEMENTATION.

## Outcome ladder
- FOREST_CERTIFIED_SCOPED: exact enumeration completes, all controls/invariance pass.
- FOREST_IMPLEMENTATION_INVALID: any required control or exact census consistency fails.
- FOREST_COMPUTATION_BLOCKED: exhaustive enumeration cannot complete for an identified computational reason; not scientific FAIL.

No terminal D7 classifier is authorized. EXISTING_SUFFICIENT / ADAPT_EXISTING / HYBRID_REQUIRED / NEW_REQUIRED remain forbidden. Candidate Gravity remains inactive.
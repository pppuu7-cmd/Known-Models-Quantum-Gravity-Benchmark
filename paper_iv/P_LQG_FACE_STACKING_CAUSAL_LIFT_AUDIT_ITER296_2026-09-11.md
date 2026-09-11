# Iter296 — LQG face-stacking causal-orientation lift audit

## Authorities and derivation status
- Muxin Han, *Summation and triangulation independence of Lorentzian spinfoam amplitudes for all LQG*, Phys. Rev. D 113, 084034 (2026), DOI `10.1103/n76f-31gf`, arXiv:2510.26926.
- Carlos E. Beltrán, *Causal Structure for Generalized Spinfoams*, arXiv:2603.22661v2 (2026).
- The Iter296 lift theorem is a source-grounded algebraic inference from the published definitions; it is not claimed verbatim by either source.

## Source-grounded algebraic bridge
Han's face-stacking operation holds the vertex/edge skeleton fixed while increasing the multiplicity of faces bounded by the same root loop. At a vertex, Beltrán encodes causal consistency by a GF(2) incidence system whose rows are wedge/face constraints and whose columns are edge-orientation variables.

Therefore stacking a root face duplicates the associated incidence row. If every duplicate inherits the same causal wedge bit as the root face (the diagonal lift), the stacked right-hand side duplicates the corresponding bit as well. Repeating identical equations cannot change the row space, rank, or solution set for the edge-orientation variables. Thus every causally solvable root assignment has an orientation-level lift to every positive face-multiplicity vector in the Han family. Independent conflicting causal bits on duplicate faces are not guaranteed to lift.

## Frozen machine audit
- Scientific run: `34593061657` on head `079f94c11c0c222b5c8759b316538cfd12664c33`.
- Four independent guards in parallel with `fail-fast:false`, `max-parallel:4`.
- Exhaustive guard: 1,885 three-link-connected simple graphs with 4–6 vertices; all preserve GF(2) rank/diagonal solution lift after deterministic face-row duplication.
- Multiplicity stress: K5 rank 4; 512 positive multiplicity vectors up to multiplicity 16; 32 edge-orientation assignments per vector; all lifts preserve the equations.
- Negative control: two copies of one incidence row with opposite causal bits have zero solutions.
- Aggregate = SUCCESS.
- Methodology run `34593061667`: preflight + 4/4 shards + aggregate/bundle SUCCESS.
- Summary artifact `10196412595`; artifact digest `sha256:7d1d4387def6de4921532e78d31f098c49f72e37a178619eeb4e2dc2ba9fab0b`; raw summary digest `sha256:c80bb2d1d5fc7fe58f8bbe059c6e1e3bba0cac1ab1819b5c54ab8286d829cd67`.

## Classification
`PASS_SCOPED_ORIENTATION_LEVEL_CAUSAL_LIFT_ACROSS_HAN_FACE_MULTIPLICITY_STACKS_BY_ROW_DUPLICATION__NO_CAUSAL_AMPLITUDE_SUM_FINITE_LAMBDA_TRANSPORT_OR_UV_IR_OBSERVABLE_CERTIFICATE`

## Fail-closed boundary
This closes only existence/consistency of a diagonal causal-orientation lift across Han's face-multiplicity family. It does not establish finiteness or normalization of Beltrán's generalized causal vertex, insertion of that causal vertex into Han's `lambda_f`-weighted stack sum, removal/control of Han area cutoffs for the causal amplitude, or same-realization UV-to-Regge/GR parameter/observable/error transport. Beltrán explicitly leaves finiteness of the generalized causal vertex open. LQG/spinfoam remains `PARTIAL/BLOCKED`, not terminal; D7 remains unauthorized.

Refined active blocker:
`BLOCKED_MISSING_FINITE_NORMALIZED_GENERALIZED_CAUSAL_VERTEX_INSERTION_AND_LAMBDA_F_WEIGHTED_COMPLETE_STACK_AMPLITUDE_SUM_WITH_AREA_CUTOFF_CONTROL_PLUS_SAME_REALIZATION_UV_TO_CAUSAL_LARGE_SPIN_REGGE_GR_TRANSPORT_WITH_GAMMA_SPIN_SCALE_IDENTITY_NORMALIZED_OBSERVABLE_COMMON_DOMAIN_COMPARATOR_AND_PROPAGATED_ERROR`

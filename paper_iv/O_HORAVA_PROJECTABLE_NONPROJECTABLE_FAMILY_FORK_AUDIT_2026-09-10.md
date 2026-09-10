# O-HORAVA — projectable/non-projectable family fork audit

Date: 2026-09-10
Iteration: 190
RQIR Core: v1.0 FROZEN

## Question

Can the Hořava-Lifshitz Tier-1 row be represented by one projectable realization, or must projectable and non-projectable branches receive separate terminal disposition before a family-level Paper-IV result is allowed?

## Primary literature authorities

1. Cerioni & Brandenberger, *Cosmological Perturbations in the Projectable Version of Horava-Lifshitz Gravity*, arXiv:1007.1006.
   - In the projectable theory the extra scalar cosmological perturbation is dynamical already at linear order.
   - The paper finds ghost/tachyon behavior in complementary lambda ranges around the GR value and therefore a nontrivial extra-mode/IR problem for that realization.

2. Koyama & Arroja, *Pathological behaviour of the scalar graviton in Hořava-Lifshitz gravity*, arXiv:0910.1998.
   - The projectable IR scalar becomes pathological near the GR limit and nonlinear interactions become important as the sound speed is driven small.
   - This blocks any inference that a formal lambda -> 1 limit by itself supplies a controlled same-realization GR observable map.

3. Blas, Pujolas & Sibiryakov, *A healthy extension of Horava gravity*, arXiv:0909.3525.
   - The non-projectable extension changes the scalar sector: it has a regular quadratic scalar action and a low-energy Lorentz-violating scalar-tensor limit.
   - Its extra operators/constraint structure are therefore materially different from the projectable branch.

4. Papazoglou & Sotiriou, *Strong coupling in extended Horava-Lifshitz gravity*, arXiv:0911.1299, together with the BPS comment arXiv:0912.0550.
   - These papers demonstrate that even the status of strong coupling in the extended branch depends on the precise UV completion/operator content and cannot be inherited from the projectable realization by family label alone.

## Frozen RQIR interpretation

The projectability condition is not a cosmetic parameter choice. It changes the constraint structure and the physical scalar sector. Consequently:

- `PROJECTABLE_HORAVA` and `NONPROJECTABLE_HORAVA/BPS` are materially distinct branches for Paper-IV coverage.
- A scoped PASS/FAIL/BLOCKED result in one branch cannot be promoted to the full `HORAVA_LIFSHITZ` family without an explicit reduction/equivalence theorem.
- The projectable branch does provide a concrete normalized candidate observable class: the scalar cosmological perturbation/dispersion and its ghost/tachyon/strong-coupling behavior in a fixed background and parameter regime.
- However, the literature inspected here does **not** provide one frozen UV->IR trajectory with all of: same microscopic action, renormalization/coarse-graining map, controlled remainder, IR GR comparison, and normalized detector/cosmological observable.
- The non-projectable BPS branch likewise has a concrete low-energy scalar-tensor limit, but the inspected sources do not establish a complete same-realization UV fixed trajectory plus normalized RQIR comparator package.

## New scoped result

Classification:

`PASS_RQIR_GATE__HORAVA_MATERIAL_PROJECTABILITY_FORK_AND_EXTRA_MODE_OBJECT_IDENTIFIED`

This is a family-structure/coverage PASS, not a terminal physical-family PASS.

### Exact consequences

1. The old requirement to "separately disposition the materially distinct non-projectable theory" is now justified by primary-source physical differences rather than only taxonomy.
2. `PROJECTABLE_HORAVA_EXTRA_SCALAR` is admitted as a concrete same-branch observable target.
3. `NONPROJECTABLE_BPS_SCALAR_TENSOR_IR_LIMIT` is admitted as a distinct comparator target.
4. No family-level residual is defined yet because the required same-realization UV->IR maps and error/remainder ledgers are absent.
5. Therefore `HORAVA_LIFSHITZ` remains `PARTIAL_SUBFAMILY_ONLY`; D2/D4/D7 do not advance.

## Narrow next gates

### H1 — projectable branch

`HORAVA_PROJECTABLE_UV_TO_IR_TRAJECTORY_PLUS_EXTRA_SCALAR_NORMALIZED_OBSERVABLE_CERTIFICATE`

Required fields:
- exact projectable action/operator basis and parameter convention;
- UV authority/trajectory or prospectively frozen running law;
- map to the IR lambda/background point;
- scalar-mode dispersion/normalization;
- strong-coupling/stability domain;
- explicit theoretical error/remainder;
- same-domain GR/EFT comparator.

### H2 — non-projectable branch

`HORAVA_NONPROJECTABLE_BPS_UV_TO_IR_TRAJECTORY_PLUS_SCALAR_TENSOR_COMPARATOR_CERTIFICATE`

Required fields:
- exact non-projectable action/operator basis;
- status of lapse-gradient operators and scalar mode;
- UV-to-IR running/coarse-graining authority;
- normalized low-energy scalar-tensor observable;
- error/remainder ledger;
- same-domain GR/EFT comparator.

## Family terminal rule

`HORAVA_LIFSHITZ` may become family-terminal only after H1 and H2 are independently terminal, or after a theorem proves that one branch reduces to the other in the exact Paper-IV observable domain. No such theorem is established here.

## Heavy compute disposition

IDLE. The present blocker is missing same-realization RG/UV->IR ancestry and error-controlled matching, not numerical precision. A scan over IR parameters would not close that provenance object.

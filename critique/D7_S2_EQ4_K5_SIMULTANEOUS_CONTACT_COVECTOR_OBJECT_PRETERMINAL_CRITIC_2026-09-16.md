# Independent preterminal Critic — D7-S2 K5 simultaneous contact-covector object

Date: 2026-09-16
Scope: source/object identity only; no outcome criterion changes.

## Adversarial review

The preregistered question asks for a simultaneous **group-only** contact-covector object on the gauge-fixed Eq.(4) group tangent domain, while explicitly forbidding an unstated `dz_ab=0` restriction.

Independent rereading of the locked primary source gives:

1. Eq.(4) fixes the group realization and uses `g_ab=g_b^{-1}g_a`.
2. In the coherent-state/spinor realization, Eq.(12) integrates both the four group variables and one `CP1` auxiliary variable per wedge.
3. Appendix C Eq.(31)-Eq.(32) explicitly defines `B(z,g)=log(<g^dagger z|g^dagger z>/<z|z>)`; its natural differential therefore has both auxiliary-spinor and group components on the product domain.
4. Appendix D Eq.(35)-Eq.(36) composes the step/contact distribution with the full scalar `B(z,g)`. It does not rewrite that object as a function of `g` alone.
5. No statement in the audited v1 primary source was found that conditions the contact distribution on fixed `z`, sets `dz=0`, integrates out `z` to an equivalent group-only defining function, or supplies a canonical restriction/projection from the full contact covector to the group-only tangent domain.
6. `CP1` projectivization is a quotient of the auxiliary spinor representation, not a projection of the Eq.(4) group tangent variables, and cannot fill the missing map.
7. The terminal raw K5 incidence map can pull back the **group component** of `dB` once such a component is selected, but it cannot source-authorize the selection itself.

## Adversarial alternatives rejected

- Treating `z` as an external boundary label is inconsistent with Eq.(12), where `z_ab` is integrated.
- Calling a partial derivative `d_g B` mathematically available does not by itself prove that the source contact distribution is the pullback of a distribution on group space alone.
- The saddle-point value of `B` at critical points does not define the exact distributional contact object away from the saddle.
- Raw K5 unit tree minors do not supply contact normalization or a missing restriction map.

## Critic verdict

`CRITIC_SUPPORTS_BLOCKED_UNLESS_SOURCE_AUTHORIZED_GROUP_ONLY_CONTACT_RESTRICTION_EXISTS`

The source explicitly defines the full `B(z,g)` contact object, so this is not a missing-contact-formula blocker. The narrow missing authority is the map/restriction that would turn the full contact covector on the joint `CP1 x SL(2,C)` variables into the group-only covector required by the preregistered child of the raw K5 tangent gate.

This remains `BLOCKED`, not `FAIL`, if the classifier confirms the frozen ledger. No rank, transversality or distribution-product conclusion is authorized.

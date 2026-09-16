# D7-S2 K5 contact-covector gate — classifier normalization repair freeze

Date: 2026-09-16
Status: EXECUTION/REPRESENTATION-ONLY REPAIR FROZEN BEFORE REPAIRED RUN

The first terminal workflow run `35149976729` produced the frozen scientific classification `D7_S2_EQ4_K5_SIMULTANEOUS_CONTACT_COVECTOR_OBJECT_BLOCKED_SCOPED`, but its aggregate payload contains one internally inconsistent derived boolean:

- frozen source ledger value: `ten_wedge_group_only_contact_covectors = NOT_ESTABLISHED_WITHOUT_AUXILIARY_SPINOR_RESTRICTION`;
- classifier boolean: `ten_wedge_group_only_contact_covectors_authorized = true`.

Cause: implementation compared the ledger string only to exact `NOT_ESTABLISHED`, instead of treating the prospectively frozen `NOT_ESTABLISHED_*` refinement as non-authorized.

This is not a new scientific criterion and does not authorize changing the classification, source extraction, missing object or claim ceiling.

## Frozen repair

For all authority-status fields, define `authorized(status)` as false iff the status string begins with `NOT_ESTABLISHED`; otherwise retain the existing positive/explicit semantics.

The repaired classifier must therefore report:

- group-only `dz=0` restriction authorized = false;
- fixed-z conditioning authorized = false;
- ten-wedge group-only contact covectors authorized = false;
- the ten-wedge field must also appear in `blocked_fields`;
- classification remains determined by the original preregistration and source ledger, with no post-hoc change.

All source hashes, preregistration, negative controls and PASS/BLOCKED/INVALID criteria remain unchanged.

The first run is retained as noncanonical execution evidence because its classification is usable but its derived diagnostic payload is internally inconsistent. Only a repaired terminal aggregate may become canonical.

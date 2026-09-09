# KMQGB Recovery Delta 152

Created `code/post_freeze_paper_iv_governance_validator.py`.

The validator makes the post-freeze governance executable:

- every PF1 result must declare RQIR Core v1.0;
- any `BLOCKED...` result with `counts_as_new_required_evidence=true` is an error;
- `core_change_requested=true` requires `rqir_core_defect=true`;
- individual model records may not authorize the global Paper-IV decision;
- the global ledger may not authorize `NEW_REQUIRED` while missing-object blocks remain;
- the PF1 denominator remains frozen at five.

This is methodology enforcement, not a physics decision and does not change readiness scores.
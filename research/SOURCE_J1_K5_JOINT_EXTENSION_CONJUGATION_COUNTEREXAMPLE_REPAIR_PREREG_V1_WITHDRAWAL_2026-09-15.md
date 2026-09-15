# Prospective preregistration withdrawal — v1 negative-control defect

Date: 2026-09-15
Status: `WITHDRAWN_BEFORE_SUBSTANTIVE_COMPUTATION`

The preregistration committed at `b194a6d4b56f93eabb982fd3af7f7da93d0a068b` is withdrawn prospectively before any certificate code, workflow, or substantive result is executed.

Reason: its frozen negative control `C_bad=[[0,0,1],[0,+1,0],[1,0,0]]` is not guaranteed to be adversarial for the channel-0 four-valent tensor. The channel-0 tensor factors through spin-1 singlet structures whose signs are invariant under simultaneous magnetic reversal; changing only the middle sign in the reversal matrix can therefore remain invisible after a four-leg action. A negative control whose failure is not structurally guaranteed cannot validate the implementation.

No scientific predicate has been evaluated and no terminal classification is attached to v1. Historical v1 remains immutable. A complete v2 preregistration must be committed before code/workflow execution, changing only this pre-compute validation defect and explicitly identifying v1 as superseded.

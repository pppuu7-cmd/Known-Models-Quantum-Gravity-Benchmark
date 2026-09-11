# Publication Impact Ledger

Purpose: preserve, for final manuscript preparation, every benchmark result that requires a change, check, or explicit non-change in an RQIR paper. This ledger is additive and does not modify frozen RQIR Core criteria.

Status vocabulary:
- `TODO` — manuscript change/check still required.
- `READY` — wording/evidence is sufficiently defined to be applied at final preparation.
- `APPLIED` — change has been incorporated into the manuscript and re-audited.
- `NOT_NEEDED` — checked and no manuscript change is warranted.

## Iter277 — RQCP multi-axis resource closure

### Paper III
- **Status:** `READY`
- **Impact:** methodological correction/strengthening is warranted.
- **What to add:** an explicit general rule that resource closure is axis-complete rather than single-axis. If a result depends on multiple independent regulator/truncation/domain/finite-volume/approximation axes, convergence or calibration along one axis cannot certify closure of the others. Every materially active independent axis must either (a) be taken to a controlled limit with uncertainty propagated into the normalized observable, or (b) be fixed by an independently justified physical principle with the induced uncertainty propagated.
- **Why:** Iter277 provides a concrete counterexample to single-axis closure. RQCP spatial refinement can be well controlled while an independent Hilbert-space cutoff materially shifts normalized quantities. In the independent audit, cutoff 8 -> 28 changes G_eff by about 7.32%, the gap by about 3.07%, and G_eff*gap^2 by about 1.36%, while the high-cutoff sequence 24 -> 28 is already extremely stable.
- **Where to apply:** methodology/resource-closure definition and the discussion/checklist for claiming apparatus/model closure. Keep the wording theory-agnostic; do not turn Paper III into an RQCP case study.
- **Do not change:** frozen RQIR Core criteria or previously certified detector-side nuisance/noise/calibration logic unless manuscript audit finds a direct contradiction.

### Paper IV
- **Status:** `READY`
- **Impact:** detailed benchmark evidence should be included.
- **What to add:** RQCP as a distinct nonterminal Tier-1 parent; four-environment semantic reproducibility result; the zero-frequency diagnostic defect as an implementation artifact; the 19-job robustness scan; extended Hilbert-cutoff scan through 28; and the refined blocker requiring independent closure/control of the Hilbert/domain truncation axis before any broader family-level sufficiency claim.
- **Interpretation constraint:** this is neither a family-level PASS nor a family-level FAIL. It is a scoped positive fixed-band result plus a newly quantified independent resource axis.

## Standing rule for subsequent iterations
For every scientifically relevant benchmark iteration, record here:
1. affected paper(s),
2. exact manuscript correction/addition/check required,
3. whether the change is methodological, numerical, evidentiary, or editorial,
4. status (`TODO/READY/APPLIED/NOT_NEEDED`),
5. an explicit note when no paper change is warranted.

This ledger is the manuscript handoff authority for final article preparation; chat-only reminders are not sufficient.

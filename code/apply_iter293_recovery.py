#!/usr/bin/env python3
from pathlib import Path

run_id = "34584685590"
scientific_head = "3edcaf9feb3a308750fd6a84a25056f9f105c61d"
summary_artifact = "10193076711"
artifact_digest = "sha256:d14df68d7b1c98464bacd38644d75271ab5c75745e75bf69c6a6d048bc04cd42"
raw_summary_digest = "sha256:a0521f16d90f393376d7899556a3c452123025baa172f1248f7bcbad6eb1b277"
classification = "HIGH_VALUE_GENERALIZED_EPRL_KKL_CAUSAL_SCOPE_EXTENSION__NO_COMPLETE_STACK_EQUIVALENCE_OR_UV_TO_IR_TRANSPORT"

audit = Path("paper_iv/P_LQG_GENERALIZED_CAUSAL_SCOPE_AUDIT_ITER293_2026-09-11.md")
if not audit.exists():
    audit.write_text(f'''# Iter293 — LQG generalized EPRL-KKL causal-scope audit\n\n## Authority\nCarlos E. Beltrán, *Causal Structure for Generalized Spinfoams*, arXiv:2603.22661v2 (2026). Public preprint authority; no peer-reviewed journal publication was located in the Iter293 authority check.\n\n## Frozen machine audit\n- Scientific run: `{run_id}` on head `{scientific_head}`.\n- Four independent guards ran in parallel with fail-fast disabled: authority, generalized-scope, asymptotic-scope, and transport-scope.\n- Aggregate ran only after the explicit dependency barrier.\n- Summary artifact: `{summary_artifact}`.\n- Artifact digest: `{artifact_digest}`.\n- Raw summary digest: `{raw_summary_digest}`.\n\n## Scoped result\nThe source defines causal structure for generalized EPRL-KKL spinfoams on arbitrary 2-complexes, supplies a consistency criterion relating 2-skeleton and 1-skeleton orientations, and introduces a causal vertex amplitude that explicitly generalizes earlier Bianchi–Chen–Gamonal-type proposals. This materially broadens the scope of the Iter290 causal endpoint beyond a single simplicial EPRL vertex.\n\nClassification: `{classification}`.\n\n## Fail-closed boundary\nThis is not an explicit equivalence/reduction map to the active Han spinfoam-stack realization. It does not provide continuous same-realization stack-coupling/Immirzi/spin-scale transport from the Iter287 UV sector to the causal large-spin Regge/Einstein endpoint, nor a normalized same-realization observable/comparator/propagated-error certificate. Therefore LQG/spinfoam remains `PARTIAL/BLOCKED`; family terminality remains false; D7 remains unauthorized.\n''')

ledger = Path("recovery/PUBLICATION_IMPACT_LEDGER.md")
text = ledger.read_text()
if "## Iter293 — LQG generalized EPRL-KKL causal scope" not in text:
    marker = "\n## Standing rule\n"
    if marker not in text:
        raise SystemExit("fail-closed: standing-rule marker absent")
    block = f'''\n## Iter293 — LQG generalized EPRL-KKL causal scope\n### Paper III — `NOT_NEEDED`\n- **Type:** theory-specific causal-scope extension; no new general methodology rule.\n### Paper IV — `READY`\n- Add Beltrán, *Causal Structure for Generalized Spinfoams*, arXiv:2603.22661v2 (2026), as a scoped public-preprint extension of causal-spinfoam structure to generalized EPRL-KKL arbitrary 2-complexes.\n- Record the orientation-consistency criterion and the causal vertex construction that generalizes the earlier Bianchi–Chen–Gamonal causal proposal.\n- **Required boundary:** this broadens the causal endpoint's model scope but is not an explicit reduction/equivalence to the active Han complete-stack realization and does not supply same-realization UV→IR parameter transport, normalized comparator-ready observable, or propagated uncertainty. Keep LQG `PARTIAL/BLOCKED` and D7 unauthorized.\n- Result: `{classification}`.\n- Provenance: scientific `{run_id}`; scientific head `{scientific_head}`; summary artifact `{summary_artifact}`; artifact digest `{artifact_digest}`; raw summary digest `{raw_summary_digest}`.\n'''
    ledger.write_text(text.replace(marker, block + marker))

front = Path("recovery/CURRENT_BENCHMARK_FRONT.md")
text = front.read_text()
old = "Iteration: Iter292 LQG external refinement-flow authority scoped; Iter291 gamma-duality bridge and Iter290 causal Lorentzian Regge endpoint retained"
new = "Iteration: Iter293 generalized EPRL-KKL causal scope integrated; Iter292 refinement-flow authority, Iter291 gamma-duality bridge and Iter290 causal Regge endpoint retained"
if old in text:
    text = text.replace(old, new, 1)
elif new not in text:
    raise SystemExit("fail-closed: unexpected front iteration header")

if "### Iter293 — generalized EPRL-KKL causal scope" not in text:
    marker = "\n## CFS front\n"
    if marker not in text:
        raise SystemExit("fail-closed: CFS marker absent")
    block = f'''\n### Iter293 — generalized EPRL-KKL causal scope\nPrimary object: Beltrán, *Causal Structure for Generalized Spinfoams*, arXiv:2603.22661v2 (2026), public preprint.\nScientific run `{run_id}`: four independent guards in parallel + aggregate SUCCESS on head `{scientific_head}`.\nSummary artifact `{summary_artifact}`; artifact digest `{artifact_digest}`; raw summary digest `{raw_summary_digest}`.\n\nAggregate:\n- public-preprint authority identity = PASS;\n- generalized EPRL-KKL arbitrary-2-complex causal structure / orientation consistency = PASS;\n- causal vertex generalizing Bianchi–Chen–Gamonal plus semiclassical asymptotic analysis = PASS;\n- explicit Han-stack equivalence = false;\n- complete-stack same-realization UV→IR transport = false;\n- normalized observable/comparator/error certificate = false;\n- family terminal = false;\n- D7 authorized = false.\n\nClassification:\n`{classification}`\n\nInterpretation: the Iter290 causal endpoint is no longer confined to a single simplicial EPRL-vertex construction; a generalized EPRL-KKL causal framework on arbitrary 2-complexes exists. This is a meaningful scope extension, but it does not establish identity with the active Han stack or close the decisive UV→IR transport blocker.\n'''
    text = text.replace(marker, block + marker)
front.write_text(text)

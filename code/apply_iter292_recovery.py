#!/usr/bin/env python3
# Deterministic one-shot recovery handoff; scientific interpretation already frozen in Iter292 audit.
from pathlib import Path

run_id = "34575046143"
artifact_id = "10189283134"
digest = "sha256:3dfa5deb1bab46bfcb7c32f199969dcc8a1588a69937d408483ff202a48002f5"
head = "eb6ba509773ac50697b4c6c683b2f3638ea7ad71"

ledger = Path("recovery/PUBLICATION_IMPACT_LEDGER.md")
text = ledger.read_text()
if "## Iter292 — LQG ER=EPR refinement-flow scope audit" not in text:
    marker = "\n## Standing rule\n"
    if marker not in text:
        raise SystemExit("fail-closed: standing-rule marker absent")
    block = f'''\n## Iter292 — LQG ER=EPR refinement-flow scope audit\n### Paper III — `NOT_NEEDED`\n- **Type:** theory-specific refinement/continuum authority; no new general methodology rule.\n### Paper IV — `READY`\n- Add Tamburini, *ER = EPR in Loop Quantum Gravity: the Immirzi Parameter and the Continuum Limit*, arXiv:2508.18324v2 (2025), as a scoped public-preprint refinement-flow authority.\n- Record the explicit claim of a spin-foam refinement-renormalization flow and a conditional regulator-independent continuum limit.\n- **Required boundary:** no explicit equivalence/reduction map to the active Han complete-stack realization was located; no continuous stack-coupling/`gamma`/spin-scale identity transport to the Iter290 causal Regge endpoint is demonstrated; no normalized same-realization observable/comparator/error certificate is supplied. Do not promote preprint-scoped evidence to family terminal status.\n- Result: `HIGH_VALUE_EXTERNAL_REFINEMENT_FLOW_AUTHORITY__NO_EXPLICIT_EQUIVALENCE_TO_THE_ACTIVE_COMPLETE_STACK_OR_CAUSAL_REGGE_CHAIN`.\n- Provenance: scientific `{run_id}`; scientific head `{head}`; summary artifact `{artifact_id}`; artifact digest `{digest}`.\n'''
    text = text.replace(marker, block + marker)
    ledger.write_text(text)

front = Path("recovery/CURRENT_BENCHMARK_FRONT.md")
text = front.read_text()
old = "Iteration: Iter291 LQG gamma-duality semiclassical observable/parameter bridge integrated; Iter290 causal Lorentzian Regge endpoint retained"
new = "Iteration: Iter292 LQG external refinement-flow authority scoped; Iter291 gamma-duality bridge and Iter290 causal Lorentzian Regge endpoint retained"
if old in text:
    text = text.replace(old, new, 1)
elif new not in text:
    raise SystemExit("fail-closed: unexpected front iteration header")

if "### Iter292 — external refinement-flow authority" not in text:
    marker = "\n## CFS front\n"
    if marker not in text:
        raise SystemExit("fail-closed: CFS marker absent")
    block = f'''\n### Iter292 — external refinement-flow authority\nPrimary object: Tamburini, *ER = EPR in Loop Quantum Gravity: the Immirzi Parameter and the Continuum Limit*, arXiv:2508.18324v2 (2025). Public preprint; no peer-reviewed journal version located in the Iter292 authority check.\nScientific run `{run_id}`: four independent guards in parallel + aggregate SUCCESS on head `{head}`.\nSummary artifact `{artifact_id}`; artifact digest `{digest}`.\n\nRaw aggregate:\n- public preprint identity = PASS;\n- explicit refinement-renormalization / conditional regulator-independent continuum claim = PASS;\n- explicit equivalence map to active Han complete-stack = false;\n- continuous `gamma` / stack-coupling / spin-scale transport to Iter290 = false;\n- normalized same-realization observable/comparator/error certificate = false;\n- family terminal = false;\n- D7 authorized = false.\n\nClassification:\n`HIGH_VALUE_EXTERNAL_REFINEMENT_FLOW_AUTHORITY__NO_EXPLICIT_EQUIVALENCE_TO_THE_ACTIVE_COMPLETE_STACK_OR_CAUSAL_REGGE_CHAIN`\n\nThis removes only the weak sub-blocker that no explicit LQG refinement-flow proposal exists. The decisive family-scope blocker remains the same-realization/equivalence transport into the active complete-stack + causal-Regge chain.\n'''
    text = text.replace(marker, block + marker)
front.write_text(text)

"""Fail-closed governance validator for post-freeze Paper-IV benchmark records.

This code does not decide physics. It enforces the frozen methodological rules:
- every post-freeze record uses RQIR Core v1.0;
- a missing-object BLOCKED result never counts as NEW_REQUIRED evidence;
- a requested core change requires an explicit core defect;
- one model-level record cannot silently authorize the global Paper-IV decision;
- the machine-readable decision ledger cannot authorize NEW_REQUIRED while
  missing-object benchmark records remain in the active evidence set.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WAVE = ROOT / "post_freeze_paper_iv_wave_01"
LEDGER = ROOT / "paper_iv" / "PAPER_IV_FROZEN_CORE_DECISION_LEDGER.json"


def load(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def validate_record(path: Path, record: dict) -> list[str]:
    errors: list[str] = []
    if str(record.get("rqir_core_version")) != "1.0":
        errors.append(f"{path}: post-freeze record must use frozen RQIR Core v1.0")

    status = str(record.get("terminal_status", ""))
    if status.startswith("BLOCKED") and bool(record.get("counts_as_new_required_evidence", False)):
        errors.append(f"{path}: BLOCKED result cannot count as NEW_REQUIRED evidence")

    if bool(record.get("core_change_requested", False)) and not bool(record.get("rqir_core_defect", False)):
        errors.append(f"{path}: core change requested without rqir_core_defect=true")

    if bool(record.get("paper_iv_decision_authorized", False)):
        errors.append(f"{path}: model-level record may not authorize the global Paper-IV decision")

    return errors


def validate_ledger(ledger: dict, records: list[dict]) -> list[str]:
    errors: list[str] = []
    if str(ledger.get("rqir_core_version")) != "1.0" or ledger.get("rqir_core_status") != "FROZEN":
        errors.append("decision ledger must be locked to RQIR Core v1.0 FROZEN")

    auth = ledger.get("terminal_authorization", {})
    blocked = [r for r in records if str(r.get("terminal_status", "")).startswith("BLOCKED")]
    if blocked and bool(auth.get("NEW_REQUIRED", False)):
        errors.append("NEW_REQUIRED cannot be authorized while active major-framework evidence contains missing-object BLOCKED records")

    if ledger.get("global_decision") == "NEW_REQUIRED" and blocked:
        errors.append("global_decision NEW_REQUIRED conflicts with missing-object quarantine")

    wave = ledger.get("post_freeze_wave_01", {})
    if wave.get("terminal") != len(records):
        errors.append("ledger terminal count does not match discovered result records")
    if wave.get("denominator") != 5 or len(records) != 5:
        errors.append("post-freeze wave denominator/result count must remain frozen at five")

    return errors


def main() -> None:
    paths = sorted(WAVE.glob("PF1_*/result.json"))
    if len(paths) != 5:
        raise SystemExit(f"expected 5 PF1 result records, found {len(paths)}")

    records = [load(p) for p in paths]
    errors: list[str] = []
    for path, record in zip(paths, records):
        errors.extend(validate_record(path, record))
    errors.extend(validate_ledger(load(LEDGER), records))

    if errors:
        raise SystemExit("\n".join(errors))

    print("post_freeze_paper_iv_governance=PASS")
    print(f"validated_records={len(records)}")
    print("rqir_core_version=1.0")
    print("missing_object_quarantine=PASS")
    print("global_decision=NOT_YET_AUTHORIZED")


if __name__ == "__main__":
    main()

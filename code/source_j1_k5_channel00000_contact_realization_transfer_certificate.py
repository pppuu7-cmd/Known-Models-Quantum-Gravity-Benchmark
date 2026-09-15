#!/usr/bin/env python3
"""Exact/bounded certificate for the channel-00000 coherent-contact realization bridge.

The physical outcome is source-authority sensitive.  The exact cubic-pole channel
contraction is recomputed only as a positive survival control; it is never
substituted for the coherent contact tensor.
"""
from __future__ import annotations

from fractions import Fraction as F
import hashlib
import json
import pathlib

import numpy as np

import source_j1_full_collision_leading_certificate as leading
import iter499_arb_core as core

ROOT = pathlib.Path(__file__).resolve().parents[1]
LEDGER = ROOT / "inputs/source_j1_k5_channel00000_contact_transfer_authority_2026-09-15.json"
OUT = ROOT / "artifacts/source_j1_k5_channel00000_contact_realization_transfer.json"

PASS = "SOURCE_J1_K5_CHANNEL00000_COHERENT_CONTACT_SURVIVES_EXACT_CONTRACTION_SCOPED"
FAIL = "SOURCE_J1_K5_CHANNEL00000_COHERENT_CONTACT_CANCELS_EXACTLY_SCOPED"
BLOCKED = "SOURCE_J1_K5_CHANNEL00000_CONTACT_REALIZATION_TRANSFER_BLOCKED_SCOPED"
INVALID = "SOURCE_J1_K5_CHANNEL00000_CONTACT_REALIZATION_TRANSFER_INVALID"


def git_blob_sha(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode()
    return hashlib.sha1(header + data).hexdigest()


def classify(*, source_locks_ok: bool, controls_ok: bool, map_pinned: bool,
             conventions_match: bool, coefficient):
    if not source_locks_ok or not controls_ok or (map_pinned and not conventions_match):
        return INVALID
    if not map_pinned or coefficient is None:
        return BLOCKED
    return PASS if coefficient != 0 else FAIL


def exact_leading_control():
    cart = leading.cartesian_intertwiners()
    X = [
        (F(0), F(0), F(0)),
        (F(1), F(0), F(0)),
        (F(0), F(1), F(0)),
        (F(0), F(0), F(1)),
        (F(1), F(1), F(1)),
    ]
    mats = []
    for a, b in core.EDGES:
        v = tuple(X[a][q] - X[b][q] for q in range(3))
        mats.append(leading.Q(v))
    path = leading.build_path(cart)
    return leading.contract(cart, mats, (0, 0, 0, 0, 0), path)


def main():
    ledger = json.loads(LEDGER.read_text())
    record_checks = []
    for rec in ledger["records"]:
        p = ROOT / rec["path"]
        data = p.read_bytes()
        text = data.decode("utf-8")
        blob_ok = git_blob_sha(data) == rec["blob_sha"]
        markers = {m: (m in text) for m in rec.get("required_markers", [])}
        record_checks.append({
            "id": rec["id"],
            "path": rec["path"],
            "blob_sha_expected": rec["blob_sha"],
            "blob_sha_actual": git_blob_sha(data),
            "blob_ok": blob_ok,
            "markers": markers,
            "markers_ok": all(markers.values()),
        })

    source_locks_ok = all(r["blob_ok"] and r["markers_ok"] for r in record_checks)

    leading_coeff = exact_leading_control()
    leading_control_ok = leading_coeff == F(11, 24)
    cancellation_coeff = leading_coeff + (-leading_coeff)
    cancellation_control_ok = cancellation_coeff == 0

    # Generic outcome-sensitivity controls through exactly the same classifier.
    fixture_outputs = {
        "positive_nonzero_survival": classify(
            source_locks_ok=True, controls_ok=True, map_pinned=True,
            conventions_match=True, coefficient=F(11, 24)),
        "adversarial_exact_cancellation": classify(
            source_locks_ok=True, controls_ok=True, map_pinned=True,
            conventions_match=True, coefficient=F(0)),
        "missing_transfer": classify(
            source_locks_ok=True, controls_ok=True, map_pinned=False,
            conventions_match=True, coefficient=None),
        "convention_mismatch": classify(
            source_locks_ok=True, controls_ok=True, map_pinned=True,
            conventions_match=False, coefficient=F(11, 24)),
    }
    expected = {
        "positive_nonzero_survival": PASS,
        "adversarial_exact_cancellation": FAIL,
        "missing_transfer": BLOCKED,
        "convention_mismatch": INVALID,
    }
    fixtures_ok = fixture_outputs == expected
    controls_ok = leading_control_ok and cancellation_control_ok and fixtures_ok

    amap = ledger.get("actual_contact_map")
    map_pinned = bool(amap and amap.get("source_pinned"))
    conventions_match = bool(amap and amap.get("conventions_match")) if map_pinned else True
    coeff_raw = ledger.get("actual_contact_channel00000_exact_coefficient")
    coefficient = None if coeff_raw is None else F(coeff_raw)

    classification = classify(
        source_locks_ok=source_locks_ok,
        controls_ok=controls_ok,
        map_pinned=map_pinned,
        conventions_match=conventions_match,
        coefficient=coefficient,
    )

    out = {
        "gate": ledger["gate"],
        "classification": classification,
        "source_locks_ok": source_locks_ok,
        "record_checks": record_checks,
        "exact_positive_control": {
            "object": "independent cubic-pole Q contraction only",
            "channel_00000_coefficient": str(leading_coeff),
            "expected": "11/24",
            "pass": leading_control_ok,
            "physical_contact_evidence": False,
        },
        "exact_cancellation_control": {
            "construction": "C + (-C)",
            "coefficient": str(cancellation_coeff),
            "pass": cancellation_control_ok,
            "physical_contact_evidence": False,
        },
        "classifier_fixtures": fixture_outputs,
        "classifier_fixtures_expected": expected,
        "classifier_outcome_sensitive": fixtures_ok,
        "actual_contact_map_source_pinned": map_pinned,
        "actual_contact_map_conventions_match": conventions_match if map_pinned else None,
        "actual_contact_channel00000_exact_coefficient": None if coefficient is None else str(coefficient),
        "controls_ok": controls_ok,
        "new_fact": (
            "The frozen repository authority contains nonzero coherent contact evidence and an independent "
            "nonzero fixed-channel cubic-pole contraction, but no source-pinned coherent-contact-to-magnetic "
            "map sufficient to execute the physical channel-00000 contact contraction."
            if classification == BLOCKED else
            "See classification and exact coefficient."
        ),
        "claim_ceiling": (
            "Same-realization transfer gate only; the independent Q=diag(1,-2,1), 11/24 control is not the "
            "coherent contact tensor. No Eq4 distributional existence/nonexistence, uniqueness, family, D7, "
            "or terminal-selector conclusion."
        ),
    }
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(json.dumps(out, indent=2, sort_keys=True))
    # BLOCKED is a valid scientific terminal outcome; only INVALID is an execution-contract failure.
    raise SystemExit(2 if classification == INVALID else 0)


if __name__ == "__main__":
    main()

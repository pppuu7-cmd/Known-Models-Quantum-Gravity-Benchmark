#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

GATE = "SOURCE_J1_K5_EQ4_PHYSICAL_TRANSVERSE_QUOTIENT_PRIMARY_AUTHORITY_ESCALATION_GATE"
PASS = "EQ4_PHYSICAL_TRANSVERSE_QUOTIENT_PRIMARY_AUTHORITY_PASS_SCOPED"
BLOCKED = "EQ4_PHYSICAL_TRANSVERSE_QUOTIENT_PRIMARY_AUTHORITY_BLOCKED_SCOPED"
INVALID = "EQ4_PHYSICAL_TRANSVERSE_QUOTIENT_PRIMARY_AUTHORITY_INVALID"
PREREG = "b0c40b0c8c65f8eec9eecb4e9e25ee2eb05f1d88"
ARXIV_SHA = "cc533af3c84de8c0de57523a795ba4357523712f1746ce55fa78eb521cd51713"
REQ = [
    "PHYSICAL_TRANSVERSE_QUOTIENT_OBJECT",
    "QUOTIENT_OR_PROJECTION_MAP_FROM_EQ4_LOCAL_TANGENT_VARIABLES",
    "CONTACT_CONSTRAINT_PULLBACK_TO_QUOTIENT",
]
BLOCKER = "PUBLISHED_VERSION_FULLTEXT_AUTHORITY_ACCESS_CEILING"


def canonical_sha(obj):
    raw = json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def classify_fixture(fields, source_boundary_ok=True, variable_class_ok=True, forbidden_used=False):
    if not source_boundary_ok or not variable_class_ok or forbidden_used:
        return INVALID
    return PASS if all(fields.get(k) == "EXPLICIT_PRESENT" for k in REQ) else BLOCKED


def primary_lane(auth):
    sources = auth.get("sources", [])
    arxiv = next((s for s in sources if s.get("source_id") == "arXiv:2601.23162v1"), None)
    prd = next((s for s in sources if s.get("source_id") == "PhysRevD.113.126020"), None)
    author = next((s for s in sources if s.get("source_id") == "author_linked_material_search"), None)
    provenance_ok = bool(
        auth.get("gate") == GATE
        and auth.get("preregistration_commit") == PREREG
        and auth.get("source_boundary_frozen") is True
        and arxiv
        and arxiv.get("pdf_sha256") == ARXIV_SHA
        and arxiv.get("retrieval_status") == "COMPLETE_HTML_AND_PDF_AUDITABLE"
        and prd
        and prd.get("doi") == "10.1103/fwql-t4yr"
        and prd.get("published") == "2026-06-15"
        and author
    )
    v1_absent = bool(arxiv and all(str(arxiv.get("required_field_status", {}).get(k, "")).startswith("ABSENT_FROM_COMPLETE_AUDITABLE_V1_RECORD") for k in REQ))
    prd_access_ceiling = bool(prd and prd.get("retrieval_status") == "PUBLIC_METADATA_AND_ABSTRACT_ONLY__FULLTEXT_NOT_AUDITABLE_IN_CURRENT_AUTHORITY_ENVIRONMENT")
    no_extra_primary = bool(
        prd
        and prd.get("publisher_linked_supplement_search") == "NO_EXPLICIT_OFFICIAL_SUPPLEMENTARY_MATERIAL_LINK_DISCOVERED_IN_PUBLIC_RECORD_OR_EXACT_TITLE_DOI_SEARCH"
        and author
        and author.get("retrieval_status") == "NO_ADMISSIBLE_EXPLICITLY_PAPER_LINKED_DERIVATION_OR_CODE_DISCOVERED"
    )
    normalized = {k: "NOT_ESTABLISHED" for k in REQ}
    cls = BLOCKED if provenance_ok and v1_absent and prd_access_ceiling and no_extra_primary else INVALID
    return cls, provenance_ok, v1_absent, prd_access_ceiling, no_extra_primary, normalized


def critic_lane(critic):
    challenges = critic.get("challenges", [])
    verdicts = {c.get("question"): c.get("verdict") for c in challenges}
    fields = critic.get("required_field_assessment", {})
    required_not_established = all(fields.get(k) == "NOT_ESTABLISHED" for k in REQ)
    has_cp1_rejection = any(c.get("verdict") == "NO" and "CP1" in c.get("question", "") for c in challenges)
    has_gauge_rejection = any(c.get("verdict") == "NO" and "gauge fixing" in c.get("question", "") for c in challenges)
    has_access_ceiling = any(c.get("verdict") == "NO_STRONG_ABSENCE_CLAIM" for c in challenges)
    provenance_ok = bool(
        critic.get("gate") == GATE
        and critic.get("preregistration_commit") == PREREG
        and critic.get("minimal_blocker") == BLOCKER
        and critic.get("production_classification_recommendation") == BLOCKED
    )
    cls = BLOCKED if provenance_ok and required_not_established and has_cp1_rejection and has_gauge_rejection and has_access_ceiling else INVALID
    return cls, provenance_ok, required_not_established, has_access_ceiling, {k: "NOT_ESTABLISHED" for k in REQ}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--authority", required=True)
    ap.add_argument("--critic", required=True)
    ap.add_argument("--lane", choices=["primary", "critic"], required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    auth = json.loads(Path(a.authority).read_text())
    critic = json.loads(Path(a.critic).read_text())

    fixtures = {
        "positive_all_three_explicit_pass": classify_fixture({k: "EXPLICIT_PRESENT" for k in REQ}) == PASS,
        "negative_missing_projection_blocked": classify_fixture({REQ[0]: "EXPLICIT_PRESENT", REQ[1]: "MISSING", REQ[2]: "EXPLICIT_PRESENT"}) == BLOCKED,
        "negative_cp1_variable_class_substitution_invalid": classify_fixture({k: "EXPLICIT_PRESENT" for k in REQ}, variable_class_ok=False) == INVALID,
        "negative_textbook_or_v8_substitution_invalid": classify_fixture({k: "EXPLICIT_PRESENT" for k in REQ}, forbidden_used=True) == INVALID,
        "negative_posthoc_source_expansion_invalid": classify_fixture({k: "EXPLICIT_PRESENT" for k in REQ}, source_boundary_ok=False) == INVALID,
        "access_ceiling_is_blocked_not_fail": classify_fixture({k: "NOT_ESTABLISHED" for k in REQ}) == BLOCKED,
    }

    if a.lane == "primary":
        cls, provenance_ok, v1_absent, access_ceiling, no_extra_primary, fields = primary_lane(auth)
        lane_checks = {
            "auditable_v1_required_fields_absent": v1_absent,
            "published_version_fulltext_access_ceiling": access_ceiling,
            "no_admissible_official_supplement_or_author_code_found": no_extra_primary,
        }
    else:
        cls, provenance_ok, required_not_established, access_ceiling, fields = critic_lane(critic)
        lane_checks = {
            "critic_required_fields_not_established": required_not_established,
            "critic_preserves_strong_absence_claim_ceiling": access_ceiling,
            "critic_rejects_variable_class_and_gauge_conflation": cls != INVALID,
        }

    if not all(fixtures.values()) or not provenance_ok or not all(lane_checks.values()):
        cls = INVALID

    scientific_core = {
        "gate": GATE,
        "classification": cls,
        "required_fields": fields,
        "minimal_blocker": BLOCKER if cls == BLOCKED else None,
        "source_search_status": "FROZEN_PRIMARY_BOUNDARY_EXHAUSTED_TO_PUBLISHED_FULLTEXT_ACCESS_CEILING",
        "published_version_fulltext_auditable": False,
        "strong_absence_claim_authorized": False,
        "physical_transverse_rank": None,
        "downstream_physical_projection_authorized": cls == PASS,
        "claim_ceiling": "BLOCKED means the auditable frozen primary authority does not establish the physical quotient/projection; it is not a transversality FAIL and does not prove the inaccessible version of record lacks the object.",
        "fixtures": fixtures,
    }
    out = dict(scientific_core)
    out.update({
        "lane": a.lane,
        "source_provenance_ok": provenance_ok,
        "lane_checks": lane_checks,
        "authority_record_sha256": hashlib.sha256(Path(a.authority).read_bytes()).hexdigest(),
        "critic_record_sha256": hashlib.sha256(Path(a.critic).read_bytes()).hexdigest(),
        "scientific_payload_sha256": canonical_sha(scientific_core),
    })
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0 if cls in (PASS, BLOCKED) else 2


if __name__ == "__main__":
    raise SystemExit(main())

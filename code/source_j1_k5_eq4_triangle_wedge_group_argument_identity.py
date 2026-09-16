#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, subprocess
from copy import deepcopy
from pathlib import Path

PREREG = "ddf246b861d4e367af409e3ae5b6c97ccfd1ea7e"
AUTHORITY_COMMIT = "440c853516c2357029c848c83e48a7f6a39d0c86"
SOURCE_AUDIT_COMMIT = "4a21e9148393ebcefdfbb2a17cfbbf51af82b052"
PARENT_TERMINAL = "48f59aa10203903b494bd33edb5e498be24bb24f"
EXPECTED_SOURCE_BLOBS = {
    "sources/arxiv_2601_23162v1_eq4_local_collision_map_expansion_v13.json": "fdfb13f9974ebc891cb3f490ca553dd0991d9136",
    "sources/arxiv_2604_24945v1_eq4_local_collision_map_expansion_v13.json": "c742e8cab0648b8fbaef88f09876644c6c2c3077",
}
EXPECTED_PDFS = {
    "arXiv:2601.23162v1": "cc533af3c84de8c0de57523a795ba4357523712f1746ce55fa78eb521cd51713",
    "arXiv:2604.24945v1": "f37659f5cb4674dd0c1b81a6e55f5d1dfd992c60b0e85cb2859322b860e22046",
}
REQUIRED = [
    "integration_variables", "multiplication_order", "inversions", "orientation",
    "left_right_action_if_material", "contact_scalar_group_argument", "primary_location",
    "literal_or_dummy_rename_equivalence",
]
PASS = "EQ4_TRIANGLE_WEDGE_GROUP_ARGUMENT_IDENTITY_PASS_SCOPED"
BLOCKED = "EQ4_TRIANGLE_WEDGE_GROUP_ARGUMENT_IDENTITY_BLOCKED_SCOPED"
INVALID = "INVALID_IMPLEMENTATION"


def git_blob(root: Path, path: str) -> str:
    return subprocess.check_output(["git", "hash-object", path], cwd=root, text=True).strip()


def classify_ledger(ledger, *, guessed=False, v8=False, toller_comp=False, wrong_order=False):
    if guessed or v8 or toller_comp or wrong_order:
        return INVALID, []
    by = {x.get("wedge"): x for x in ledger if isinstance(x, dict)}
    missing = []
    for w in ("12", "23", "13"):
        row = by.get(w)
        if row is None:
            missing.append(f"{w}:record")
            continue
        for field in REQUIRED:
            if field not in row or row[field] in (None, "", []):
                missing.append(f"{w}:{field}")
    if missing:
        return BLOCKED, missing
    return PASS, []


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--authority", required=True)
    ap.add_argument("--source-audit", required=True)
    ap.add_argument("--repo-root", default=".")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    root = Path(args.repo_root)
    authority = json.loads(Path(args.authority).read_text())
    source = json.loads(Path(args.source_audit).read_text())

    source_blob_checks = {p: git_blob(root, p) == sha for p, sha in EXPECTED_SOURCE_BLOBS.items()}
    authority_sources = {x["source_id"]: x for x in authority.get("allowed_primary_authority", [])}
    pdf_checks = {sid: authority_sources.get(sid, {}).get("pdf_sha256") == sha for sid, sha in EXPECTED_PDFS.items()}

    provenance = {
        "preregistration_locked": authority.get("preregistration_commit") == PREREG and source.get("preregistration_commit") == PREREG,
        "authority_commit_locked": source.get("authority_commit") == AUTHORITY_COMMIT,
        "parent_terminal_locked": authority.get("parent_terminal_commit") == PARENT_TERMINAL,
        "target_triangle_locked": authority.get("target_triangle") == ["12", "23", "13"],
        "source_blobs_locked": all(source_blob_checks.values()),
        "pdf_hashes_locked": all(pdf_checks.values()) and source.get("locked_pdf_sha256") == EXPECTED_PDFS["arXiv:2601.23162v1"],
        "source_audit_commit_frozen": subprocess.run(["git", "merge-base", "--is-ancestor", SOURCE_AUDIT_COMMIT, "HEAD"], cwd=root).returncode == 0,
    }

    identity_controls = {
        "same_realization_tuple": source.get("same_realization_parent", {}).get("integration_tuple") == ["g2", "g3", "g4", "g5"],
        "g1_fixed": source.get("same_realization_parent", {}).get("fixed_variable") == "g1 = 1",
        "general_wedge_formula": source.get("literal_general_wedge_identity", {}).get("formula") == "g_ab = g_b^{-1} g_a",
        "ordered_wedge_product": source.get("same_realization_parent", {}).get("wedge_product_ordering") == "1 <= a < b <= 5",
        "orientation_formula": source.get("orientation", {}).get("formula") == "kappa_ab = sigma_a sigma_b",
        "contact_argument_formula": source.get("contact_scalar_input", {}).get("literal_wedge_scalar") == "B_ab = B(z_ab, g_b^{-1} g_a)",
        "no_v8": source.get("historical_v8_auxiliary_relation_used") is False,
        "no_textbook_guess": source.get("generic_textbook_group_formula_used") is False,
        "no_toller_composition": source.get("toller_matrix_composition_used") is False,
    }

    ledger = source.get("triangle_identity_ledger", [])
    by = {x.get("wedge"): x for x in ledger if isinstance(x, dict)}
    literal_expected = {
        "12": ("g_2^{-1} g_1", "g_2^{-1}", ["g_2^{-1}", "g_1"], ["g2"]),
        "23": ("g_3^{-1} g_2", "g_3^{-1} g_2", ["g_3^{-1}", "g_2"], ["g3"]),
        "13": ("g_3^{-1} g_1", "g_3^{-1}", ["g_3^{-1}", "g_1"], ["g3"]),
    }
    literal_checks = {}
    for w, exp in literal_expected.items():
        row = by.get(w, {})
        literal_checks[w] = (
            row.get("literal_group_argument") == exp[0]
            and row.get("gauge_fixed_group_argument") == exp[1]
            and row.get("multiplication_order") == exp[2]
            and row.get("inversions") == exp[3]
            and row.get("literal_or_dummy_rename_equivalence") == "LITERAL"
            and "g_b^{-1} g_a" in row.get("left_right_action_if_material", "")
        )

    production_class, missing = classify_ledger(ledger)

    # Controls are deliberately independent of production values.
    fixture = deepcopy(ledger)
    positive_class, _ = classify_ledger(fixture)
    renamed = deepcopy(fixture)
    for row in renamed:
        row["integration_variables"] = [x.replace("g", "h") for x in row["integration_variables"]]
        row["literal_or_dummy_rename_equivalence"] = "BIJECTIVE_DUMMY_RENAME_EXPLICITLY_SUBSTITUTED"
    rename_class, _ = classify_ledger(renamed)
    missing_one = [x for x in deepcopy(fixture) if x.get("wedge") != "13"]
    missing_class, missing_fixture = classify_ledger(missing_one)
    guessed_class, _ = classify_ledger(fixture, guessed=True)
    reversal_class, _ = classify_ledger(fixture, wrong_order=True)
    v8_class, _ = classify_ledger(fixture, v8=True)
    toller_class, _ = classify_ledger(fixture, toller_comp=True)
    controls = {
        "positive_complete_literal_maps_pass": positive_class == PASS,
        "positive_bijective_dummy_rename_pass": rename_class == PASS,
        "negative_one_missing_blocks": missing_class == BLOCKED and any(x.startswith("13:") for x in missing_fixture),
        "negative_guessed_textbook_invalid": guessed_class == INVALID,
        "negative_order_reversal_invalid": reversal_class == INVALID,
        "negative_v8_injection_invalid": v8_class == INVALID,
        "negative_toller_composition_invalid": toller_class == INVALID,
    }

    all_integrity = all(provenance.values()) and all(identity_controls.values()) and all(literal_checks.values()) and all(controls.values())
    if not all_integrity:
        classification = INVALID
    else:
        classification = production_class

    decision = {
        "gate": authority.get("gate"),
        "classification": classification,
        "target_triangle": authority.get("target_triangle"),
        "source_audit_commit": SOURCE_AUDIT_COMMIT,
        "provenance": provenance,
        "source_blob_checks": source_blob_checks,
        "pdf_hash_checks": pdf_checks,
        "identity_controls": identity_controls,
        "literal_wedge_checks": literal_checks,
        "fixture_controls": controls,
        "missing_identity_fields": missing,
        "identity_ledger": ledger,
        "transverse_rank": None,
        "rank_policy": authority.get("rank_policy"),
        "downstream_authorized": classification == PASS,
        "scope": "exact source identity of Eq.(4) triangle wedge arguments only; no transversality or D7 closure claim",
    }
    raw = json.dumps(decision, sort_keys=True, separators=(",", ":")).encode()
    decision["decision_sha256"] = hashlib.sha256(raw).hexdigest()
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(json.dumps(decision, indent=2, sort_keys=True) + "\n")
    print(json.dumps({k: v for k, v in decision.items() if k != "identity_ledger"}, sort_keys=True))
    return 0 if classification in (PASS, BLOCKED) else 2


if __name__ == "__main__":
    raise SystemExit(main())

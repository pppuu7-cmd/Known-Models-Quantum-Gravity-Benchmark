"""Cross-file validator for KMQGB repository/methodology completion.

R1/R2 declarations are no longer accepted as sufficient evidence.  This
validator imports the independent evidence scorer and requires its atomically
computed values to equal the declarations. Scientific readiness remains
separate from repository/methodology readiness.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from kg_candidate_record_v13_validator import validate_v13
from readiness_score import compute as compute_readiness

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_COMPLETION_FILES = [
    "protocol/READINESS_100_COMPLETION_CONTRACT.md",
    "protocol/READINESS_RUBRIC_V2.json",
    "protocol/BEYOND_C5_PARENT_PRINCIPLE_DECISION_PROCEDURE.md",
    "protocol/EXECUTABLE_TEST_REGISTRY.json",
    "schemas/candidate_gravity_record_v1_3.schema.json",
    "templates/candidate_gravity_record_v1_3.template.json",
    "code/kg_candidate_record_v13_validator.py",
    "code/schema_validation.py",
    "code/readiness_score.py",
    "code/methodology_orchestrator.py",
    "code/build_release_bundle.py",
    "release/BUNDLE_CONTENTS.json",
    "release/RELEASE_VERSION",
    "requirements-ci.txt",
    "reproducibility/ENVIRONMENT_LOCK.json",
    ".github/workflows/methodology-ci.yml",
    ".github/workflows/release.yml",
    ".github/CODEOWNERS",
    "LICENSE",
    "CITATION.cff",
    "publication/KMQGB_METHODS_EVIDENCE_MATRIX.md",
    "publication/claim_evidence_matrix.json",
]

ALLOWED_PAPER_IV = {
    "NOT_YET_AUTHORIZED",
    "EXISTING_SUFFICIENT",
    "ADAPT_EXISTING",
    "HYBRID_REQUIRED",
    "NEW_REQUIRED",
}


def load_json(rel: str):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def validate(require_100: bool = False) -> dict:
    errors: list[str] = []
    warnings: list[str] = []

    for rel in REQUIRED_COMPLETION_FILES:
        if not (ROOT / rel).is_file():
            errors.append(f"missing completion artifact: {rel}")

    state = load_json("recovery/state.json")
    metrics = state.get("readiness_metrics", {})
    r1 = metrics.get("repository_readiness_R1_percent")
    r2 = metrics.get("kmqgb_methodology_material_readiness_R2_percent")
    r3 = metrics.get("candidate_gravity_scientific_readiness_R3_percent")
    r4 = metrics.get("legacy_parent_search_R4_percent")
    if not all(isinstance(x, int) and 0 <= x <= 100 for x in (r1, r2, r3, r4)):
        errors.append("readiness metrics must be integer percentages in [0,100]")

    independent = compute_readiness()
    computed_r1 = independent["metrics"]["R1"]["score"]
    computed_r2 = independent["metrics"]["R2"]["score"]
    if computed_r1 != r1 or computed_r2 != r2:
        errors.append(
            f"declared/computed readiness mismatch: declared R1/R2={r1}/{r2}, "
            f"computed={computed_r1}/{computed_r2}"
        )
    if require_100 and (computed_r1 != 100 or computed_r2 != 100):
        errors.append(
            f"completion mode requires independently computed R1=R2=100, "
            f"got {computed_r1}/{computed_r2}"
        )

    rqir = state.get("rqir_core", {})
    if rqir.get("version") != "1.0" or rqir.get("status") != "FROZEN":
        errors.append("RQIR Core v1.0 frozen invariant violated")

    candidate = state.get("candidate_gravity", {})
    if candidate.get("readiness_percent") != r3:
        errors.append("R3 does not match candidate_gravity.readiness_percent")
    if r1 == 100 and r2 == 100 and r3 == 100 and not candidate.get("promotable_ansatz", False):
        warnings.append("R3=100 without explicit promotable_ansatz marker would require external scientific audit")

    paper = state.get("paper_iv", {})
    decision = paper.get("global_decision")
    if decision not in ALLOWED_PAPER_IV:
        errors.append(f"invalid Paper-IV global decision {decision!r}")
    if decision == "NOT_YET_AUTHORIZED" and paper.get("new_required_authorized", False):
        errors.append("NEW_REQUIRED cannot be authorized while Paper IV is NOT_YET_AUTHORIZED")

    cw = paper.get("closure_wave_02", {})
    terminal = cw.get("terminal")
    denominator = cw.get("denominator")
    completion = cw.get("completion_percent")
    if isinstance(terminal, int) and isinstance(denominator, int) and denominator > 0:
        expected = int(round(100 * terminal / denominator))
        if completion != expected:
            errors.append(
                f"Closure Wave 02 percentage inconsistent: {terminal}/{denominator} -> {expected}, stored={completion}"
            )
    else:
        errors.append("Closure Wave 02 terminal/denominator malformed")

    template = load_json("templates/candidate_gravity_record_v1_3.template.json")
    template_result = validate_v13(template)
    if not template_result["valid"]:
        errors.append(f"v1.3 candidate template invalid: {template_result['errors']}")
    if template.get("promotion", {}).get("ansatz_promoted", False):
        errors.append("prospective template must not promote an ansatz")
    if template.get("compute_authorization", {}).get("heavy_compute_authorized", False):
        errors.append("prospective structural-blocked template must not authorize heavy compute")

    registry = load_json("protocol/EXECUTABLE_TEST_REGISTRY.json")
    tests = registry.get("tests", [])
    ids = [item.get("id") for item in tests if isinstance(item, dict)]
    for required_id in {
        "paper_iv_governance",
        "candidate_record_v13",
        "schema_validation",
        "readiness_independent_score",
        "p4_functional_freedom",
        "lqg_gamma_rg_tangency",
        "lqg_multiscale_rg_transport",
    }:
        if required_id not in ids:
            errors.append(f"critical executable registry id missing: {required_id}")
    if len(ids) != len(set(ids)):
        errors.append("duplicate executable registry IDs")

    bundle = load_json("release/BUNDLE_CONTENTS.json")
    bundle_paths = bundle.get("paths", [])
    if len(bundle_paths) != len(set(bundle_paths)):
        errors.append("release bundle policy contains duplicate paths")
    for rel in bundle_paths:
        if not (ROOT / rel).is_file():
            errors.append(f"release bundle references missing file: {rel}")
    for must_bundle in {
        "recovery/state.json",
        "protocol/READINESS_100_COMPLETION_CONTRACT.md",
        "protocol/READINESS_RUBRIC_V2.json",
        "protocol/EXECUTABLE_TEST_REGISTRY.json",
        "publication/claim_evidence_matrix.json",
        "templates/candidate_gravity_record_v1_3.template.json",
        "requirements-ci.txt",
        "reproducibility/ENVIRONMENT_LOCK.json",
        "LICENSE",
        "CITATION.cff",
    }:
        if must_bundle not in bundle_paths:
            errors.append(f"release bundle omits critical authority: {must_bundle}")

    env_lock = load_json("reproducibility/ENVIRONMENT_LOCK.json")
    workflow = (ROOT / ".github/workflows/methodology-ci.yml").read_text(encoding="utf-8")
    release_workflow = (ROOT / ".github/workflows/release.yml").read_text(encoding="utf-8")
    if env_lock.get("runner") not in workflow or env_lock.get("python") not in workflow:
        errors.append("methodology CI does not match frozen runner/Python environment lock")
    for action, sha in env_lock.get("actions", {}).items():
        token = f"{action}@{sha}"
        if token not in workflow and token not in release_workflow:
            errors.append(f"pinned action absent from workflows: {token}")
    if "--require-hashes -r requirements-ci.txt" not in workflow:
        errors.append("methodology CI does not enforce the hashed dependency lock")

    claims = load_json("publication/claim_evidence_matrix.json")
    claim_map = {c.get("id"): c for c in claims.get("claims", []) if isinstance(c, dict)}
    if claim_map.get("FORBID_SOLVED_QG", {}).get("status") != "FORBIDDEN_OVERCLAIM":
        errors.append("publication matrix must preserve FORBID_SOLVED_QG overclaim guard")
    if claim_map.get("REPOSITORY_COMPLETE_NOT_SCIENCE_COMPLETE", {}).get("status") != "DERIVED_KMQGB":
        errors.append("repository/science separation claim is missing or misclassified")

    metrics_text = (ROOT / "protocol" / "READINESS_METRICS.md").read_text(encoding="utf-8")
    readme_text = (ROOT / "README.md").read_text(encoding="utf-8")
    if require_100:
        if "**R1 = 100%.**" not in metrics_text or "**R2 = 100%.**" not in metrics_text:
            errors.append("READINESS_METRICS.md does not advertise the completed R1/R2 values")
        if "R1 repository readiness: **100%**" not in readme_text:
            errors.append("README does not report R1=100%")
        if "R2 KMQGB methodology/material readiness: **100%**" not in readme_text:
            errors.append("README does not report R2=100%")

    compute_policy = state.get("compute_policy", {})
    if "STRUCTURAL" in str(compute_policy.get("current_reason", "")).upper() and "IDLE" not in str(compute_policy.get("heavy_compute_status", "")).upper():
        errors.append("structural compute blocker must keep heavy compute IDLE")

    return {
        "valid": not errors,
        "require_100": require_100,
        "errors": errors,
        "warnings": warnings,
        "declared_readiness": {"R1": r1, "R2": r2, "R3": r3, "R4": r4},
        "independent_readiness": {"R1": computed_r1, "R2": computed_r2},
        "independent_rubric_valid": independent["valid"],
        "paper_iv": decision,
        "closure_wave_02": {"terminal": terminal, "denominator": denominator, "completion_percent": completion},
        "candidate_template_valid_blocked": template_result["valid"] and not template_result["promotion_allowed"],
        "registered_critical_tests": len(tests),
        "bundle_file_count": len(bundle_paths),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--require-100", action="store_true")
    args = parser.parse_args()
    result = validate(require_100=args.require_100)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

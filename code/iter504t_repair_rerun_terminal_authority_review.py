#!/usr/bin/env python3
from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path
from typing import Any

EXPECTED_ROOTS = [13, 14, 15]
EXPECTED_RHOS = [0.35, 0.9, 1.6, 2.7]
EXPECTED_R = [6, 8, 10, 12]
EXPECTED_CHANNELS = 243
EXPECTED_SCIENCE_PASS = "ITER504T_LOCAL_D_CERTIFIES_THREE_ROOT_CONTINUOUS_DRIFT_SCOPED"
EXPECTED_SCIENCE_INCONCLUSIVE = "ITER504T_LOCAL_D_THREE_ROOT_CONTINUOUS_DRIFT_INCONCLUSIVE_SCOPED"
EXPECTED_REPAIR_PASS = "ITER504T_IMPLEMENTATION_CONTROLS_REPAIRED_AND_RERUN_VALID_SCOPED"
REVIEW_PASS = "ITER504T_REPAIR_RERUN_EXACT_RUN_AUTHORITY_VALIDATED_SCOPED"
REVIEW_FAIL = "ITER504T_REPAIR_RERUN_AUTHORITY_RESTORATION_FAILED_SCOPED"
REVIEW_BLOCKED = "ITER504T_REPAIR_RERUN_TERMINAL_REVIEW_BLOCKED_SCOPED"
INVALID = "INVALID_IMPLEMENTATION"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def expected_pairs() -> list[tuple[int, float]]:
    return [(R, rho) for R in EXPECTED_R for rho in EXPECTED_RHOS]


def validate_lane(payload: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    leaves_summary: list[dict[str, Any]] = []
    total_unresolved = 0
    c1_record_count = 0
    c1_component_count = 0
    c1_false_component_count = 0

    roots = payload.get("roots")
    if not isinstance(roots, list):
        return {"errors": ["missing_roots"], "blocked": True}

    root_ids = [r.get("root_box") for r in roots]
    if root_ids != EXPECTED_ROOTS:
        errors.append(f"roots_identity:{root_ids!r}")

    for root in roots:
        root_id = root.get("root_box")
        if root.get("r_cohort_consumed") != EXPECTED_R:
            errors.append(f"R_cohort_root_{root_id}")
        if root.get("rho_cohort_consumed") != EXPECTED_RHOS:
            errors.append(f"rho_cohort_root_{root_id}")
        if root.get("full_channel_count") != EXPECTED_CHANNELS:
            errors.append(f"channel_count_root_{root_id}")
        if root.get("threshold_exact") != "1/20":
            errors.append(f"threshold_root_{root_id}")
        if root.get("robust_floor_exact") != "1":
            errors.append(f"floor_root_{root_id}")
        if root.get("max_depth") != 3:
            errors.append(f"max_depth_root_{root_id}")
        if root.get("partition_rule") != "deterministic_dyadic_midpoint":
            errors.append(f"partition_rule_root_{root_id}")
        if root.get("channel_pruning_used") is not False:
            errors.append(f"channel_pruning_root_{root_id}")
        if root.get("local_derivative_recomputed_each_visited_node") is not True:
            errors.append(f"local_D_recompute_root_{root_id}")

        leaves = root.get("leaves")
        if not isinstance(leaves, list):
            errors.append(f"missing_leaves_root_{root_id}")
            continue
        if len(leaves) != root.get("terminal_leaf_count"):
            errors.append(f"terminal_leaf_count_root_{root_id}")

        recomputed_unresolved = 0
        for leaf_index, leaf in enumerate(leaves):
            per_rho = leaf.get("per_rho")
            if not isinstance(per_rho, list):
                errors.append(f"missing_per_rho_root_{root_id}_leaf_{leaf_index}")
                continue
            if [row.get("rho") for row in per_rho] != EXPECTED_RHOS:
                errors.append(f"per_rho_identity_root_{root_id}_leaf_{leaf_index}")

            recomputed_rho: list[bool] = []
            serialized_rho: list[Any] = []
            for row in per_rho:
                recomputed = bool(row.get("slope_floor_satisfied")) and bool(row.get("drift_within_tolerance"))
                recomputed_rho.append(recomputed)
                serialized_rho.append(row.get("certified"))
                if row.get("certified") is not recomputed:
                    errors.append(
                        f"rho_boolean_consistency_root_{root_id}_leaf_{leaf_index}_rho_{row.get('rho')}"
                    )

            recomputed_leaf = len(recomputed_rho) == len(EXPECTED_RHOS) and all(recomputed_rho)
            if leaf.get("certified") is not recomputed_leaf:
                errors.append(f"C4_leaf_binding_root_{root_id}_leaf_{leaf_index}")
            if not recomputed_leaf:
                recomputed_unresolved += 1

            possible_max = leaf.get("possible_max")
            if not isinstance(possible_max, list):
                errors.append(f"missing_possible_max_root_{root_id}_leaf_{leaf_index}")
            else:
                got_pairs = [(row.get("R"), row.get("rho")) for row in possible_max]
                if got_pairs != expected_pairs():
                    errors.append(f"possible_max_R_rho_cohort_root_{root_id}_leaf_{leaf_index}")

            leaves_summary.append(
                {
                    "root": root_id,
                    "leaf_index": leaf_index,
                    "depth": leaf.get("depth"),
                    "serialized_certified": leaf.get("certified"),
                    "recomputed_certified": recomputed_leaf,
                    "per_rho_serialized": serialized_rho,
                    "per_rho_recomputed": recomputed_rho,
                }
            )

        if root.get("unresolved_leaf_count") != recomputed_unresolved:
            errors.append(
                f"unresolved_leaf_count_root_{root_id}:{root.get('unresolved_leaf_count')}!={recomputed_unresolved}"
            )
        total_unresolved += recomputed_unresolved

        records = root.get("componentwise_parent_inclusion_records")
        if not isinstance(records, list):
            errors.append(f"missing_C1_records_root_{root_id}")
            records = []
        if len(records) != root.get("componentwise_parent_inclusion_record_count"):
            errors.append(f"C1_record_count_field_root_{root_id}")
        expected_record_count = root.get("visited_node_count", 0) - 1
        if len(records) != expected_record_count:
            errors.append(f"C1_nonroot_record_count_root_{root_id}")
        c1_record_count += len(records)

        for record_index, record in enumerate(records):
            haar = record.get("haar_log_inclusion_by_R")
            if not isinstance(haar, dict):
                errors.append(f"C1_missing_haar_root_{root_id}_record_{record_index}")
                haar = {}
            try:
                haar_keys = sorted(int(k) for k in haar.keys())
            except Exception:
                haar_keys = []
            if haar_keys != EXPECTED_R:
                errors.append(f"C1_haar_R_root_{root_id}_record_{record_index}")
            if not all(isinstance(v, bool) for v in haar.values()):
                errors.append(f"C1_haar_boolean_root_{root_id}_record_{record_index}")

            rows = record.get("channel_inclusion_rows")
            if not isinstance(rows, list):
                errors.append(f"C1_missing_channel_rows_root_{root_id}_record_{record_index}")
                rows = []
            got_pairs = [(row.get("R"), row.get("rho")) for row in rows]
            if got_pairs != expected_pairs():
                errors.append(f"C1_R_rho_rows_root_{root_id}_record_{record_index}")

            component_values: list[bool] = []
            for row_index, row in enumerate(rows):
                values = row.get("componentwise_inclusion")
                if not isinstance(values, list) or len(values) != EXPECTED_CHANNELS:
                    errors.append(f"C1_channel_cardinality_root_{root_id}_record_{record_index}_row_{row_index}")
                    continue
                if not all(isinstance(v, bool) for v in values):
                    errors.append(f"C1_channel_boolean_root_{root_id}_record_{record_index}_row_{row_index}")
                component_values.extend(values)

            all_values = component_values + list(haar.values())
            c1_component_count += len(all_values)
            c1_false_component_count += sum(value is False for value in all_values)
            if all_values and record.get("all_componentwise_parent_inclusion") is not all(all_values):
                errors.append(f"C1_all_flag_root_{root_id}_record_{record_index}")

    if payload.get("total_unresolved_leaves") != total_unresolved:
        errors.append(f"total_unresolved_leaves:{payload.get('total_unresolved_leaves')}!={total_unresolved}")
    if payload.get("total_terminal_leaves") != len(leaves_summary):
        errors.append(f"total_terminal_leaves:{payload.get('total_terminal_leaves')}!={len(leaves_summary)}")

    recomputed_classification = (
        EXPECTED_SCIENCE_PASS if total_unresolved == 0 else EXPECTED_SCIENCE_INCONCLUSIVE
    )
    if payload.get("classification") != recomputed_classification:
        errors.append(
            f"science_classification:{payload.get('classification')}!={recomputed_classification}"
        )

    return {
        "errors": errors,
        "blocked": False,
        "root_count": len(roots),
        "terminal_leaf_count": len(leaves_summary),
        "recomputed_unresolved_leaves": total_unresolved,
        "recomputed_scientific_classification": recomputed_classification,
        "c1_record_count": c1_record_count,
        "c1_component_count": c1_component_count,
        "c1_false_component_count": c1_false_component_count,
        "leaf_rows": leaves_summary,
    }


def identity_matches(expected: dict[str, Any], observed: dict[str, Any]) -> bool:
    return (
        expected.get("id") == observed.get("id")
        and expected.get("name") == observed.get("name")
        and expected.get("digest") == observed.get("digest")
    )


def run_negative_controls(base: dict[str, Any], authority: dict[str, Any]) -> dict[str, bool]:
    controls: dict[str, bool] = {}

    mutant = copy.deepcopy(base)
    row = mutant["roots"][0]["leaves"][0]["per_rho"][0]
    row["slope_floor_satisfied"] = False
    row["certified"] = False
    controls["C4_true_leaf_with_false_rho_rejected"] = any(
        err.startswith("C4_leaf_binding_") for err in validate_lane(mutant)["errors"]
    )

    mutant = copy.deepcopy(base)
    mutant["roots"][0]["leaves"][0]["certified"] = False
    controls["C4_false_leaf_with_all_true_rhos_rejected"] = any(
        err.startswith("C4_leaf_binding_") for err in validate_lane(mutant)["errors"]
    )

    mutant = copy.deepcopy(base)
    mutant["roots"][0]["leaves"][0]["per_rho"][0]["certified"] = False
    controls["per_rho_boolean_inconsistency_rejected"] = any(
        err.startswith("rho_boolean_consistency_") for err in validate_lane(mutant)["errors"]
    )

    mutant = copy.deepcopy(base)
    mutant["roots"][0]["r_cohort_consumed"][0] = 7
    controls["R_6_to_7_rejected"] = any(
        err.startswith("R_cohort_root_") for err in validate_lane(mutant)["errors"]
    )

    mutant = copy.deepcopy(base)
    mutant["roots"][0]["componentwise_parent_inclusion_records"].pop()
    controls["missing_C1_record_rejected"] = any(
        err.startswith("C1_record_count_field_") or err.startswith("C1_nonroot_record_count_")
        for err in validate_lane(mutant)["errors"]
    )

    first = authority["required_terminal_artifacts"][0]
    wrong = dict(first)
    wrong["id"] = int(first["id"]) + 1
    controls["artifact_identity_mutation_rejected"] = not identity_matches(first, wrong)

    mutant = copy.deepcopy(base)
    mutant["roots"][0]["unresolved_leaf_count"] = 1
    controls["serialized_unresolved_count_mismatch_rejected"] = any(
        err.startswith("unresolved_leaf_count_root_") for err in validate_lane(mutant)["errors"]
    )

    return controls


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--authority", required=True)
    ap.add_argument("--assembly-a", required=True)
    ap.add_argument("--assembly-b", required=True)
    ap.add_argument("--aggregate", required=True)
    ap.add_argument("--critic", required=True)
    ap.add_argument("--verdict", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    paths = {
        "assembly_a": Path(args.assembly_a),
        "assembly_b": Path(args.assembly_b),
        "aggregate": Path(args.aggregate),
        "critic": Path(args.critic),
        "verdict": Path(args.verdict),
    }
    authority = load_json(Path(args.authority))

    missing = [name for name, path in paths.items() if not path.exists()]
    if missing:
        result = {
            "gate": authority.get("gate"),
            "classification": REVIEW_BLOCKED,
            "missing_terminal_objects": missing,
            "claim_ceiling": authority.get("interpretation_ceiling"),
        }
        canonical = json.dumps(result, sort_keys=True, separators=(",", ":"))
        result["review_decision_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()
        Path(args.out).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
        return

    a = load_json(paths["assembly_a"])
    b = load_json(paths["assembly_b"])
    aggregate = load_json(paths["aggregate"])
    critic = load_json(paths["critic"])
    verdict = load_json(paths["verdict"])

    lane_a = validate_lane(a)
    lane_b = validate_lane(b)
    review_errors = list(lane_a["errors"]) + list(lane_b["errors"])

    if lane_a.get("recomputed_scientific_classification") != lane_b.get("recomputed_scientific_classification"):
        review_errors.append("cross_environment_recomputed_scientific_disagreement")
    science = lane_a.get("recomputed_scientific_classification")

    if aggregate.get("classification") != science:
        review_errors.append("aggregate_classification_mismatch")
    if critic.get("classification") != science:
        review_errors.append("critic_classification_mismatch")
    if verdict.get("scientific_classification") != science:
        review_errors.append("repair_verdict_scientific_classification_mismatch")
    if verdict.get("classification") != EXPECTED_REPAIR_PASS:
        review_errors.append("repair_verdict_not_original_repair_PASS")
    if critic.get("critic_errors") != []:
        review_errors.append("critic_errors_nonempty")
    if aggregate.get("cross_environment_exact_decision_agreement") is not True:
        review_errors.append("aggregate_cross_environment_agreement_missing")
    if critic.get("cross_environment_exact_decision_agreement") is not True:
        review_errors.append("critic_cross_environment_agreement_missing")
    if not isinstance(verdict.get("checks"), dict) or not all(verdict["checks"].values()):
        review_errors.append("repair_verdict_checks_not_all_true")

    file_hashes = {name: sha256_file(path) for name, path in paths.items()}
    assembly_byte_identical = file_hashes["assembly_a"] == file_hashes["assembly_b"]
    if not assembly_byte_identical:
        review_errors.append("assembly_bytes_not_identical")

    controls = run_negative_controls(a, authority)
    if not all(controls.values()):
        review_errors.append("outcome_sensitive_control_failure")

    authority_identity = {
        "terminal_run_id": authority.get("terminal_run", {}).get("id") == 35205054496,
        "terminal_run_status": authority.get("terminal_run", {}).get("status") == "completed",
        "terminal_run_conclusion": authority.get("terminal_run", {}).get("conclusion") == "success",
        "terminal_run_head": authority.get("terminal_run", {}).get("head_sha")
        == "10ae6bcc8447d14cecc6e550065504b23f792953",
        "c4_confirmed": authority.get("terminal_c4_authority", {}).get("independent_critic_verdict")
        == "CONFIRMED_SCOPED",
    }
    if not all(authority_identity.values()):
        classification = INVALID
    elif review_errors:
        classification = REVIEW_FAIL
    else:
        classification = REVIEW_PASS

    result = {
        "gate": authority["gate"],
        "classification": classification,
        "exact_run": authority["terminal_run"],
        "terminal_c4_retained": authority["terminal_c4_authority"],
        "authority_identity": authority_identity,
        "artifact_internal_file_sha256": file_hashes,
        "assembly_byte_identical": assembly_byte_identical,
        "lanes": {"3.11": lane_a, "3.13": lane_b},
        "aggregate_observed": aggregate,
        "critic_observed": critic,
        "repair_verdict_observed": verdict,
        "negative_controls": controls,
        "review_errors": review_errors,
        "claim_ceiling": authority["interpretation_ceiling"],
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":"))
    result["review_decision_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "classification": classification,
        "review_decision_sha256": result["review_decision_sha256"],
        "review_errors": review_errors,
        "negative_controls": controls,
        "science": science,
        "leaf_count": lane_a.get("terminal_leaf_count"),
        "recomputed_unresolved": lane_a.get("recomputed_unresolved_leaves"),
    }, sort_keys=True))


if __name__ == "__main__":
    main()

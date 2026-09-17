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
EXPECTED_SCIENCE_INCONCLUSIVE = "ITER504T_LOCAL_D_INCONCLUSIVE_SCOPED"
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


def blocked_result(reason: str) -> dict[str, Any]:
    return {
        "errors": [],
        "blocked": True,
        "blocked_reasons": [reason],
        "recomputed_scientific_classification": None,
    }


def validate_lane(payload: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    blocked_reasons: list[str] = []
    leaves_summary: list[dict[str, Any]] = []
    total_unresolved = 0
    c1_record_count = 0
    c1_component_count = 0
    c1_false_component_count = 0

    roots = payload.get("roots")
    if not isinstance(roots, list):
        return blocked_result("missing_roots")

    if any(not isinstance(root, dict) for root in roots):
        return blocked_result("malformed_root_object")

    root_ids = [root.get("root_box") for root in roots]
    if root_ids != EXPECTED_ROOTS:
        errors.append(f"roots_identity:{root_ids!r}")

    required_root_fields = [
        "root_box", "r_cohort_consumed", "rho_cohort_consumed", "full_channel_count",
        "threshold_exact", "robust_floor_exact", "max_depth", "partition_rule",
        "channel_pruning_used", "local_derivative_recomputed_each_visited_node",
        "leaves", "terminal_leaf_count", "unresolved_leaf_count", "visited_node_count",
        "componentwise_parent_inclusion_records", "componentwise_parent_inclusion_record_count",
    ]

    for root in roots:
        root_id = root.get("root_box")
        missing_root = [field for field in required_root_fields if field not in root]
        if missing_root:
            blocked_reasons.append(f"missing_root_fields_{root_id}:{','.join(sorted(missing_root))}")
            continue

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
            blocked_reasons.append(f"missing_leaves_root_{root_id}")
            continue
        if len(leaves) != root.get("terminal_leaf_count"):
            errors.append(f"terminal_leaf_count_root_{root_id}")

        recomputed_unresolved = 0
        for leaf_index, leaf in enumerate(leaves):
            if not isinstance(leaf, dict):
                blocked_reasons.append(f"malformed_leaf_root_{root_id}_leaf_{leaf_index}")
                continue
            if "certified" not in leaf or "per_rho" not in leaf or "possible_max" not in leaf:
                blocked_reasons.append(f"missing_leaf_fields_root_{root_id}_leaf_{leaf_index}")
                continue

            per_rho = leaf.get("per_rho")
            if not isinstance(per_rho, list):
                blocked_reasons.append(f"missing_per_rho_root_{root_id}_leaf_{leaf_index}")
                continue
            if len(per_rho) != len(EXPECTED_RHOS):
                errors.append(f"per_rho_cardinality_root_{root_id}_leaf_{leaf_index}")
            if any(not isinstance(row, dict) for row in per_rho):
                blocked_reasons.append(f"malformed_per_rho_root_{root_id}_leaf_{leaf_index}")
                continue
            for row in per_rho:
                missing_row = [field for field in ("rho", "slope_floor_satisfied", "drift_within_tolerance", "certified") if field not in row]
                if missing_row:
                    blocked_reasons.append(
                        f"missing_per_rho_fields_root_{root_id}_leaf_{leaf_index}:{','.join(sorted(missing_row))}"
                    )
            if blocked_reasons:
                continue

            if [row.get("rho") for row in per_rho] != EXPECTED_RHOS:
                errors.append(f"per_rho_identity_root_{root_id}_leaf_{leaf_index}")

            recomputed_rho: list[bool] = []
            serialized_rho: list[Any] = []
            for row in per_rho:
                if not isinstance(row.get("slope_floor_satisfied"), bool) or not isinstance(row.get("drift_within_tolerance"), bool):
                    errors.append(f"rho_predicate_not_boolean_root_{root_id}_leaf_{leaf_index}_rho_{row.get('rho')}")
                recomputed = (row.get("slope_floor_satisfied") is True) and (row.get("drift_within_tolerance") is True)
                recomputed_rho.append(recomputed)
                serialized_rho.append(row.get("certified"))
                if not isinstance(row.get("certified"), bool) or row.get("certified") is not recomputed:
                    errors.append(
                        f"rho_boolean_consistency_root_{root_id}_leaf_{leaf_index}_rho_{row.get('rho')}"
                    )

            recomputed_leaf = len(recomputed_rho) == len(EXPECTED_RHOS) and all(recomputed_rho)
            if not isinstance(leaf.get("certified"), bool) or leaf.get("certified") is not recomputed_leaf:
                errors.append(f"C4_leaf_binding_root_{root_id}_leaf_{leaf_index}")
            if not recomputed_leaf:
                recomputed_unresolved += 1

            possible_max = leaf.get("possible_max")
            if not isinstance(possible_max, list):
                blocked_reasons.append(f"missing_possible_max_root_{root_id}_leaf_{leaf_index}")
            elif any(not isinstance(row, dict) for row in possible_max):
                blocked_reasons.append(f"malformed_possible_max_root_{root_id}_leaf_{leaf_index}")
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
            blocked_reasons.append(f"missing_C1_records_root_{root_id}")
            continue
        if len(records) != root.get("componentwise_parent_inclusion_record_count"):
            errors.append(f"C1_record_count_field_root_{root_id}")
        expected_record_count = root.get("visited_node_count", 0) - 1
        if len(records) != expected_record_count:
            errors.append(f"C1_nonroot_record_count_root_{root_id}")
        c1_record_count += len(records)

        for record_index, record in enumerate(records):
            if not isinstance(record, dict):
                blocked_reasons.append(f"malformed_C1_record_root_{root_id}_record_{record_index}")
                continue
            if "haar_log_inclusion_by_R" not in record or "channel_inclusion_rows" not in record:
                blocked_reasons.append(f"missing_C1_fields_root_{root_id}_record_{record_index}")
                continue
            haar = record.get("haar_log_inclusion_by_R")
            if not isinstance(haar, dict):
                blocked_reasons.append(f"C1_missing_haar_root_{root_id}_record_{record_index}")
                continue
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
                blocked_reasons.append(f"C1_missing_channel_rows_root_{root_id}_record_{record_index}")
                continue
            got_pairs = [(row.get("R"), row.get("rho")) for row in rows if isinstance(row, dict)]
            if len(got_pairs) != len(rows) or got_pairs != expected_pairs():
                errors.append(f"C1_R_rho_rows_root_{root_id}_record_{record_index}")

            component_values: list[bool] = []
            for row_index, row in enumerate(rows):
                if not isinstance(row, dict) or "componentwise_inclusion" not in row:
                    blocked_reasons.append(f"C1_missing_components_root_{root_id}_record_{record_index}_row_{row_index}")
                    continue
                values = row.get("componentwise_inclusion")
                if not isinstance(values, list) or len(values) != EXPECTED_CHANNELS:
                    errors.append(f"C1_channel_cardinality_root_{root_id}_record_{record_index}_row_{row_index}")
                    continue
                if not all(isinstance(v, bool) for v in values):
                    errors.append(f"C1_channel_boolean_root_{root_id}_record_{record_index}_row_{row_index}")
                component_values.extend(v for v in values if isinstance(v, bool))

            all_values = component_values + [v for v in haar.values() if isinstance(v, bool)]
            c1_component_count += len(all_values)
            c1_false_component_count += sum(value is False for value in all_values)
            if all_values and record.get("all_componentwise_parent_inclusion") is not all(all_values):
                errors.append(f"C1_all_flag_root_{root_id}_record_{record_index}")

    if blocked_reasons:
        return {
            "errors": errors,
            "blocked": True,
            "blocked_reasons": blocked_reasons,
            "root_count": len(roots),
            "terminal_leaf_count": len(leaves_summary),
            "recomputed_unresolved_leaves": None,
            "recomputed_scientific_classification": None,
            "c1_record_count": c1_record_count,
            "c1_component_count": c1_component_count,
            "c1_false_component_count": c1_false_component_count,
            "leaf_rows": leaves_summary,
        }

    if "total_unresolved_leaves" not in payload or "total_terminal_leaves" not in payload or "classification" not in payload:
        return blocked_result("missing_top_level_science_fields")

    if payload.get("total_unresolved_leaves") != total_unresolved:
        errors.append(f"total_unresolved_leaves:{payload.get('total_unresolved_leaves')}!={total_unresolved}")
    if payload.get("total_terminal_leaves") != len(leaves_summary):
        errors.append(f"total_terminal_leaves:{payload.get('total_terminal_leaves')}!={len(leaves_summary)}")

    recomputed_classification = EXPECTED_SCIENCE_PASS if total_unresolved == 0 else EXPECTED_SCIENCE_INCONCLUSIVE
    if payload.get("classification") != recomputed_classification:
        errors.append(f"science_classification:{payload.get('classification')}!={recomputed_classification}")

    return {
        "errors": errors,
        "blocked": False,
        "blocked_reasons": [],
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


def classify_review(authority_identity_ok: bool, lane_a: dict[str, Any], lane_b: dict[str, Any], review_errors: list[str], controls_ok: bool) -> str:
    if not authority_identity_ok or not controls_ok:
        return INVALID
    if lane_a.get("blocked") or lane_b.get("blocked"):
        return REVIEW_BLOCKED
    if review_errors:
        return REVIEW_FAIL
    science_a = lane_a.get("recomputed_scientific_classification")
    science_b = lane_b.get("recomputed_scientific_classification")
    if science_a != science_b:
        return REVIEW_FAIL
    if science_a == EXPECTED_SCIENCE_PASS:
        return REVIEW_PASS
    if science_a == EXPECTED_SCIENCE_INCONCLUSIVE:
        return EXPECTED_SCIENCE_INCONCLUSIVE
    return INVALID


def make_consistent_inconclusive_fixture(base: dict[str, Any]) -> dict[str, Any]:
    fixture = copy.deepcopy(base)
    root = fixture["roots"][0]
    leaf = root["leaves"][0]
    row = leaf["per_rho"][0]
    row["slope_floor_satisfied"] = False
    row["certified"] = False
    leaf["certified"] = False
    root["unresolved_leaf_count"] = 1
    fixture["total_unresolved_leaves"] = 1
    fixture["classification"] = EXPECTED_SCIENCE_INCONCLUSIVE
    return fixture


def run_semantics_controls(base: dict[str, Any], authority: dict[str, Any]) -> dict[str, bool]:
    controls: dict[str, bool] = {}

    base_state = validate_lane(base)
    controls["valid_pass_fixture_maps_to_review_pass"] = (
        not base_state.get("blocked")
        and not base_state.get("errors")
        and classify_review(True, base_state, copy.deepcopy(base_state), [], True) == REVIEW_PASS
    )

    inconclusive_fixture = make_consistent_inconclusive_fixture(base)
    inconclusive_state = validate_lane(inconclusive_fixture)
    controls["valid_original_inconclusive_preserved"] = (
        not inconclusive_state.get("blocked")
        and not inconclusive_state.get("errors")
        and inconclusive_state.get("recomputed_scientific_classification") == EXPECTED_SCIENCE_INCONCLUSIVE
        and classify_review(True, inconclusive_state, copy.deepcopy(inconclusive_state), [], True)
        == EXPECTED_SCIENCE_INCONCLUSIVE
    )

    missing_roots = copy.deepcopy(base)
    missing_roots.pop("roots", None)
    blocked_state = validate_lane(missing_roots)
    controls["missing_required_field_maps_to_blocked"] = (
        blocked_state.get("blocked") is True
        and classify_review(True, blocked_state, copy.deepcopy(blocked_state), [], True) == REVIEW_BLOCKED
    )

    mutant = copy.deepcopy(base)
    row = mutant["roots"][0]["leaves"][0]["per_rho"][0]
    row["slope_floor_satisfied"] = False
    row["certified"] = False
    c4_state = validate_lane(mutant)
    controls["C4_true_leaf_with_false_rho_maps_to_fail"] = (
        not c4_state.get("blocked")
        and any(err.startswith("C4_leaf_binding_") for err in c4_state.get("errors", []))
        and classify_review(True, c4_state, copy.deepcopy(c4_state), list(c4_state.get("errors", [])), True) == REVIEW_FAIL
    )

    mutant = copy.deepcopy(base)
    mutant["roots"][0]["leaves"][0]["per_rho"][0]["certified"] = False
    rho_state = validate_lane(mutant)
    controls["per_rho_boolean_inconsistency_maps_to_fail"] = (
        not rho_state.get("blocked")
        and any(err.startswith("rho_boolean_consistency_") for err in rho_state.get("errors", []))
        and classify_review(True, rho_state, copy.deepcopy(rho_state), list(rho_state.get("errors", [])), True) == REVIEW_FAIL
    )

    mutant = copy.deepcopy(base)
    mutant["roots"][0]["r_cohort_consumed"][0] = 7
    r_state = validate_lane(mutant)
    controls["R_6_to_7_maps_to_fail"] = (
        not r_state.get("blocked")
        and any(err.startswith("R_cohort_root_") for err in r_state.get("errors", []))
        and classify_review(True, r_state, copy.deepcopy(r_state), list(r_state.get("errors", [])), True) == REVIEW_FAIL
    )

    mutant = copy.deepcopy(base)
    mutant["roots"][0]["componentwise_parent_inclusion_records"].pop()
    c1_state = validate_lane(mutant)
    controls["missing_C1_record_maps_to_fail"] = (
        not c1_state.get("blocked")
        and any(
            err.startswith("C1_record_count_field_") or err.startswith("C1_nonroot_record_count_")
            for err in c1_state.get("errors", [])
        )
        and classify_review(True, c1_state, copy.deepcopy(c1_state), list(c1_state.get("errors", [])), True) == REVIEW_FAIL
    )

    first = authority["required_terminal_artifacts"][0]
    wrong = dict(first)
    wrong["id"] = int(first["id"]) + 1
    controls["artifact_identity_mutation_is_invalid"] = (
        not identity_matches(first, wrong)
        and classify_review(False, base_state, copy.deepcopy(base_state), [], True) == INVALID
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
            "semantics_controls": {},
            "claim_ceiling": authority.get("interpretation_ceiling"),
        }
        canonical = json.dumps(result, sort_keys=True, separators=(",", ":"))
        result["review_decision_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()
        Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        Path(args.out).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(json.dumps({"classification": REVIEW_BLOCKED, "missing": missing}, sort_keys=True))
        return

    a = load_json(paths["assembly_a"])
    b = load_json(paths["assembly_b"])
    aggregate = load_json(paths["aggregate"])
    critic = load_json(paths["critic"])
    verdict = load_json(paths["verdict"])

    lane_a = validate_lane(a)
    lane_b = validate_lane(b)
    review_errors: list[str] = []

    if not lane_a.get("blocked") and not lane_b.get("blocked"):
        review_errors.extend(lane_a.get("errors", []))
        review_errors.extend(lane_b.get("errors", []))
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
    else:
        science = None

    file_hashes = {name: sha256_file(path) for name, path in paths.items()}
    assembly_byte_identical = file_hashes["assembly_a"] == file_hashes["assembly_b"]
    if not (lane_a.get("blocked") or lane_b.get("blocked")) and not assembly_byte_identical:
        review_errors.append("assembly_bytes_not_identical")

    semantics_controls = run_semantics_controls(a, authority)
    controls_ok = all(semantics_controls.values())

    authority_identity = {
        "terminal_run_id": authority.get("terminal_run", {}).get("id") == 35205054496,
        "terminal_run_status": authority.get("terminal_run", {}).get("status") == "completed",
        "terminal_run_conclusion": authority.get("terminal_run", {}).get("conclusion") == "success",
        "terminal_run_head": authority.get("terminal_run", {}).get("head_sha")
        == "10ae6bcc8447d14cecc6e550065504b23f792953",
        "critic_verdict_locked": authority.get("latest_critic", {}).get("verdict") == "INVALID_IMPLEMENTATION",
        "c4_confirmed": authority.get("terminal_c4_authority", {}).get("independent_critic_verdict") == "CONFIRMED_SCOPED",
        "original_inconclusive_label_locked": authority.get("frozen_science", {}).get("INCONCLUSIVE")
        == EXPECTED_SCIENCE_INCONCLUSIVE,
        "blocked_label_locked": authority.get("review_outcomes", {}).get("BLOCKED") == REVIEW_BLOCKED,
    }
    authority_identity_ok = all(authority_identity.values())

    classification = classify_review(
        authority_identity_ok,
        lane_a,
        lane_b,
        review_errors,
        controls_ok,
    )

    result = {
        "gate": authority["gate"],
        "classification": classification,
        "exact_run": authority["terminal_run"],
        "terminal_c4_retained": authority["terminal_c4_authority"],
        "latest_critic_repaired": authority["latest_critic"],
        "authority_identity": authority_identity,
        "artifact_internal_file_sha256": file_hashes,
        "assembly_byte_identical": assembly_byte_identical,
        "lanes": {"3.11": lane_a, "3.13": lane_b},
        "aggregate_observed": aggregate,
        "critic_observed": critic,
        "repair_verdict_observed": verdict,
        "semantics_controls": semantics_controls,
        "semantics_controls_all_pass": controls_ok,
        "review_errors": review_errors,
        "science": science,
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
        "semantics_controls": semantics_controls,
        "science": science,
        "leaf_count": lane_a.get("terminal_leaf_count"),
        "recomputed_unresolved": lane_a.get("recomputed_unresolved_leaves"),
    }, sort_keys=True))


if __name__ == "__main__":
    main()

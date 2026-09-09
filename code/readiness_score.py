"""Independent evidence-based R1/R2 scorer for KMQGB.

Unlike repository_completion_validator.py, this module does not use declared
R1/R2 percentages as scoring inputs.  It evaluates the machine-readable rubric
in protocol/READINESS_RUBRIC_V2.json from atomic repository evidence.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUBRIC = ROOT / "protocol" / "READINESS_RUBRIC_V2.json"
REGISTRY = ROOT / "protocol" / "EXECUTABLE_TEST_REGISTRY.json"


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def dotted_get(obj, path: str):
    cur = obj
    for part in path.split("."):
        if not isinstance(cur, dict) or part not in cur:
            raise KeyError(path)
        cur = cur[part]
    return cur


def evaluate_component(component: dict, registry_ids: set[str]) -> dict:
    failures: list[str] = []
    for rel in component.get("files", []):
        if not (ROOT / rel).is_file():
            failures.append(f"missing file: {rel}")

    for required_id in component.get("registry_ids", []):
        if required_id not in registry_ids:
            failures.append(f"missing registry id: {required_id}")

    cache: dict[str, object] = {}
    for pred in component.get("json_equals", []):
        rel = pred["file"]
        if rel not in cache:
            try:
                cache[rel] = load_json(ROOT / rel)
            except Exception as exc:  # fail closed
                failures.append(f"cannot read JSON {rel}: {exc}")
                continue
        try:
            observed = dotted_get(cache[rel], pred["path"])
        except KeyError:
            failures.append(f"missing JSON path: {rel}:{pred['path']}")
            continue
        if observed != pred["value"]:
            failures.append(
                f"JSON mismatch {rel}:{pred['path']} observed={observed!r} expected={pred['value']!r}"
            )

    weight = int(component["weight"])
    passed = not failures
    return {
        "id": component["id"],
        "weight": weight,
        "earned": weight if passed else 0,
        "status": "PASS" if passed else "FAIL",
        "failures": failures,
    }


def compute() -> dict:
    rubric = load_json(RUBRIC)
    registry = load_json(REGISTRY)
    registry_ids = {
        item.get("id") for item in registry.get("tests", []) if isinstance(item, dict)
    }

    result = {"rubric_version": rubric["rubric_version"], "metrics": {}}
    for metric_name, metric in rubric["metrics"].items():
        components = [evaluate_component(c, registry_ids) for c in metric["components"]]
        declared_total = int(metric["total"])
        weight_total = sum(c["weight"] for c in components)
        if weight_total != declared_total:
            raise ValueError(
                f"{metric_name} rubric weights sum to {weight_total}, expected {declared_total}"
            )
        earned = sum(c["earned"] for c in components)
        result["metrics"][metric_name] = {
            "score": earned,
            "total": declared_total,
            "status": "PASS" if earned == declared_total else "FAIL",
            "components": components,
        }
    result["valid"] = all(
        metric["status"] == "PASS" for metric in result["metrics"].values()
    )
    return result


def main() -> int:
    out = compute()
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0 if out["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

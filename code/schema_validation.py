"""Standards-compliant JSON Schema validation for Candidate Gravity v1.3.

This is intentionally independent of the repository's semantic v1.3 validator.
Both must pass: JSON Schema catches structural/schema drift; the semantic
validator enforces scientific/governance invariants not expressible cleanly in
JSON Schema alone.
"""
from __future__ import annotations

import copy
import json
from pathlib import Path

from jsonschema import Draft202012Validator
from jsonschema.exceptions import SchemaError, ValidationError

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas" / "candidate_gravity_record_v1_3.schema.json"
TEMPLATE = ROOT / "templates" / "candidate_gravity_record_v1_3.template.json"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def run() -> dict:
    schema = load(SCHEMA)
    template = load(TEMPLATE)

    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema)
    validator.validate(template)

    invalid_missing = copy.deepcopy(template)
    invalid_missing.pop("same_realization", None)
    rejected_missing = False
    try:
        validator.validate(invalid_missing)
    except ValidationError:
        rejected_missing = True

    invalid_version = copy.deepcopy(template)
    invalid_version["record_schema_version"] = "9.9"
    rejected_version = False
    try:
        validator.validate(invalid_version)
    except ValidationError:
        rejected_version = True

    if not rejected_missing or not rejected_version:
        raise AssertionError("negative JSON-Schema controls were not rejected")

    return {
        "status": "PASS",
        "draft": "2020-12",
        "schema": str(SCHEMA.relative_to(ROOT)),
        "template": str(TEMPLATE.relative_to(ROOT)),
        "valid_template_accepted": True,
        "missing_required_rejected": rejected_missing,
        "wrong_version_rejected": rejected_version,
    }


def main() -> int:
    try:
        print(json.dumps(run(), indent=2, sort_keys=True))
        return 0
    except (SchemaError, ValidationError, AssertionError) as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc)}, indent=2))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

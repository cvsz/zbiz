#!/usr/bin/env python3
"""Validate a ZBiz company registration package.

This validator performs structural and cross-field checks. It does not replace
DBD review, legal advice, accounting advice, or verification of official forms.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "company.schema.json"
PLACEHOLDER_MARKERS = ("REPLACE_WITH", "REDACTED", "TODO", "TBD")


def load_data(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise ValueError("Top-level YAML value must be an object.")
    return data


def load_schema() -> dict[str, Any]:
    with SCHEMA_PATH.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def find_placeholders(value: Any, path: str = "$") -> list[str]:
    findings: list[str] = []
    if isinstance(value, dict):
        for key, child in value.items():
            findings.extend(find_placeholders(child, f"{path}.{key}"))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            findings.extend(find_placeholders(child, f"{path}[{index}]"))
    elif isinstance(value, str) and any(marker in value.upper() for marker in PLACEHOLDER_MARKERS):
        findings.append(path)
    return findings


def cross_field_errors(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    capital = data.get("capital", {})
    total_shares = capital.get("total_shares")
    par_value = capital.get("par_value_thb")
    registered_capital = capital.get("registered_capital_thb")

    if all(isinstance(v, int) for v in (total_shares, par_value, registered_capital)):
        expected = total_shares * par_value
        if expected != registered_capital:
            errors.append(
                f"capital.registered_capital_thb must equal total_shares × par_value_thb "
                f"({expected:,} expected)."
            )

    shareholders = data.get("shareholders", [])
    if isinstance(shareholders, list) and isinstance(total_shares, int):
        allocated = sum(
            item.get("share_count", 0)
            for item in shareholders
            if isinstance(item, dict) and isinstance(item.get("share_count"), int)
        )
        if allocated != total_shares:
            errors.append(
                f"Allocated shareholder shares total {allocated:,}; expected {total_shares:,}."
            )

    founder_ids = {
        item.get("id") for item in data.get("founders", []) if isinstance(item, dict)
    }
    for group_name in ("shareholders", "directors"):
        for index, item in enumerate(data.get(group_name, [])):
            if isinstance(item, dict) and item.get("founder_id") not in founder_ids:
                errors.append(
                    f"{group_name}[{index}].founder_id does not reference an existing founder."
                )

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a ZBiz company YAML package")
    parser.add_argument("file", type=Path, help="Path to company YAML file")
    parser.add_argument(
        "--allow-placeholders",
        action="store_true",
        help="Do not fail when placeholder values remain",
    )
    args = parser.parse_args()

    try:
        data = load_data(args.file)
        schema = load_schema()
    except (OSError, ValueError, yaml.YAMLError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    validation_errors = sorted(validator.iter_errors(data), key=lambda error: list(error.path))
    errors = [
        f"{'.'.join(str(part) for part in error.absolute_path) or '$'}: {error.message}"
        for error in validation_errors
    ]
    errors.extend(cross_field_errors(data))

    placeholders = find_placeholders(data)
    if placeholders and not args.allow_placeholders:
        errors.append("Placeholder values remain at: " + ", ".join(placeholders))

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

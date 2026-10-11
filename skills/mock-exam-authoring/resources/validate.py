#!/usr/bin/env python3
"""Validate exam YAML files: JSON Schema + semantic checks.

Usage: python3 validate.py exam1.exam.yaml [exam2.exam.yaml ...]
Requires: pip install pyyaml jsonschema
"""
import json, sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

SCHEMA = json.loads((Path(__file__).parent / "exam.schema.json").read_text(encoding="utf-8"))


def check(path):
    errors = []
    data = yaml.safe_load(Path(path).read_text(encoding="utf-8"))
    for e in sorted(Draft202012Validator(SCHEMA).iter_errors(data), key=lambda e: list(e.path)):
        errors.append("/".join(map(str, e.path)) + ": " + e.message)
    if errors:
        return errors

    domains = {d["id"]: {t["id"] for t in d.get("topics", [])} for d in data["domains"]}
    seen = set()
    for q in data["questions"]:
        n = f"Q{q['id']}"
        if q["id"] in seen:
            errors.append(f"{n}: duplicate id")
        seen.add(q["id"])
        if q["domain"] not in domains:
            errors.append(f"{n}: unknown domain '{q['domain']}'")
        elif q.get("topic") and q["topic"] not in domains[q["domain"]]:
            errors.append(f"{n}: unknown topic '{q['topic']}' in domain '{q['domain']}'")
        ids = [o["id"] for o in q["options"]]
        if len(set(ids)) != len(ids):
            errors.append(f"{n}: duplicate option ids")
        if not set(q["correct"]) <= set(ids):
            errors.append(f"{n}: correct {q['correct']} not in options {ids}")
        if q.get("type", "single") == "single" and len(q["correct"]) != 1:
            errors.append(f"{n}: type 'single' needs exactly one correct answer")
        if q.get("type") == "multiple" and len(q["correct"]) < 2:
            errors.append(f"{n}: type 'multiple' needs 2+ correct answers")
        texts = [o["text"].strip().lower() for o in q["options"]]
        if len(set(texts)) != len(texts):
            errors.append(f"{n}: duplicate option text")
    return errors


if __name__ == "__main__":
    bad = 0
    for p in sys.argv[1:]:
        errs = check(p)
        print(("FAIL " if errs else "OK   ") + p)
        for e in errs:
            print("  -", e)
        bad += bool(errs)
    sys.exit(1 if bad else 0)

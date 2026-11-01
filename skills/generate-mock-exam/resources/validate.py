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

def dup_ids(n, label, ids):
    return [f"{n}: duplicate {label} ids"] if len(set(ids)) != len(ids) else []


def check_question(q, n):
    errors = []
    t = q.get("type", "single")
    if t in ("single", "multiple"):
        ids = [o["id"] for o in q["options"]]
        errors += dup_ids(n, "option", ids)
        if not set(q["correct"]) <= set(ids):
            errors.append(f"{n}: correct {q['correct']} not in options {ids}")
        if t == "single" and len(q["correct"]) != 1:
            errors.append(f"{n}: type 'single' needs exactly one correct answer")
        if t == "multiple" and len(q["correct"]) < 2:
            errors.append(f"{n}: type 'multiple' needs 2+ correct answers")
        texts = [o["text"].strip().lower() for o in q["options"]]
        if len(set(texts)) != len(texts):
            errors.append(f"{n}: duplicate option text")
    elif t == "ordering":
        ids = [i["id"] for i in q["items"]]
        errors += dup_ids(n, "item", ids)
        if sorted(q["correct_order"]) != sorted(ids):
            errors.append(f"{n}: correct_order must use every item id exactly once")
        elif q["correct_order"] == ids:
            errors.append(f"{n}: items are listed already in the correct order; shuffle them")
    elif t == "matching":
        pids = [p["id"] for p in q["prompts"]]
        cids = [c["id"] for c in q["choices"]]
        errors += dup_ids(n, "prompt", pids) + dup_ids(n, "choice", cids)
        paired = [p["prompt"] for p in q["correct_pairs"]]
        if sorted(paired) != sorted(pids):
            errors.append(f"{n}: correct_pairs needs exactly one pair per prompt")
        if not {p["choice"] for p in q["correct_pairs"]} <= set(cids):
            errors.append(f"{n}: correct_pairs references unknown choice")
    elif t == "yesno-series":
        errors += dup_ids(n, "statement", [s["id"] for s in q["statements"]])
        if len({s["answer"] for s in q["statements"]}) < 2:
            errors.append(f"{n}: statements should include both true and false answers")
    elif t == "hotspot":
        errors += dup_ids(n, "slot", [s["id"] for s in q["slots"]])
        for s in q["slots"]:
            oids = [o["id"] for o in s["options"]]
            errors += dup_ids(f"{n}/{s['id']}", "option", oids)
            if s["correct"] not in oids:
                errors.append(f"{n}/{s['id']}: correct '{s['correct']}' not in options")
    elif t == "command":
        c = q["command"]
        norm = [" ".join(x.split()).lower() for x in c["accepted"]]
        if len(set(norm)) != len(norm):
            errors.append(f"{n}: duplicate accepted commands")
    return errors


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
        errors += check_question(q, n)
    return errors


def check_coverage(exam_path, cov_path):
    """Cross-check objective:<id> tags against a textbook coverage.md."""
    import re
    errors = []
    tagged = {}
    for q in yaml.safe_load(Path(exam_path).read_text()).get("questions", []):
        for t in q.get("tags", []):
            if t.startswith("objective:"):
                tagged.setdefault(t[10:], set()).add(str(q["id"]))
    mapped = {}
    for line in Path(cov_path).read_text().splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 5 and re.fullmatch(r"`[^`]+`", cells[0]):
            ids = {x.strip() for x in cells[4].split(",") if x.strip() and x.strip() != "—"}
            mapped[cells[0].strip("`")] = ids
    for o, qs in tagged.items():
        if o not in mapped:
            errors.append(f"tag objective:{o} (questions {sorted(qs)}) not in coverage map")
        elif mapped[o] != qs:
            errors.append(f"{o}: tags say {sorted(qs)}, coverage map says {sorted(mapped[o])}")
    for o, qs in mapped.items():
        if qs and o not in tagged:
            errors.append(f"coverage map lists questions for {o} but none are tagged")
    return errors


if __name__ == "__main__":
    args = sys.argv[1:]
    cov = None
    if "--coverage" in args:
        i = args.index("--coverage")
        cov = args[i + 1]
        del args[i:i + 2]
    bad = 0
    for p in args:
        errs = check(p)
        if cov:
            errs += check_coverage(p, cov)
        print(("FAIL " if errs else "OK   ") + p)
        for e in errs:
            print("  -", e)
        bad += bool(errs)
    sys.exit(1 if bad else 0)

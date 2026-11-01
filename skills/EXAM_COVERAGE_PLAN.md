# Exam coverage expansion plan

Status: implemented (steps 1–4).

## Decisions

- **Scope:** Microsoft/Azure exams only (AZ-900, AZ-104, similar). Keep the design generic so other vendors can be added later.
- **Labs and workshops:** link out to official Microsoft Learn labs, sandboxes, Applied Skills, and challenges. Do not author original labs.
- **Placement:** inline "Hands-on" pointers at the end of each topic, plus a per-book `LABS.md` appendix index.
- **Exam format guide:** a per-book `EXAM-FORMAT.md` covering question types, timing, case studies, lab sections, the official exam sandbox and practice assessment, and retake policy.
- **Non-multiple-choice formats:** support in the mock exam schema and quiz app, plus approach tips in the textbook.
- **CLI/shell tasks:** free-text answer checked against accepted command variants (normalise whitespace, quoting, and short vs long flags).

## Gap analysis

Today the textbook skill produces prose chapters and a coverage map. The mock exam schema (`exam.schema.json`) only allows `single` and `multiple`.

| Resource type | Current | Target |
|---|---|---|
| Learn labs, sandboxes | none | inline pointers and `LABS.md` |
| Workshops, Applied Skills | none | `LABS.md` |
| Exam format guide | none | `EXAM-FORMAT.md` |
| Ordering, matching, yes/no series, hotspot | none | new question types and textbook tips |
| CLI/PowerShell tasks | none | `command` question type and tips |
| Cheat sheets, comparison tables | partial | chapter summaries |

## Proposed question types

`single`, `multiple`, `ordering`, `matching`, `yesno-series`, `hotspot` (a pick-from-list per slot), `command` (free text with `accepted` variants).

## Steps

1. Update `textbook-structure.md` and the `generate-textbook` skill: "Hands-on" section, `LABS.md`, `EXAM-FORMAT.md`, and a coverage column.
2. Extend `exam.schema.json`, `validate.py`, and the `generate-mock-exam` skill with the new types.
3. Add rendering and grading for the new types to the quiz app.
4. Backfill AZ-900 and AZ-104 with lab links, exam-format guides, and sample questions of each type.

## Open items

- Link rot: decide how to verify and refresh Learn URLs (for example, a link check in the build).
- Exact `command` normalisation rules and partial-credit behaviour.
- Scoring rules for multi-part types (all-or-nothing vs partial).

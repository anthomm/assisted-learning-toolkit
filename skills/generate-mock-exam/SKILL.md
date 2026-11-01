---
name: generate-mock-exam
description: Generate and validate original mock exams from a local textbook and its source curriculum. Enrich claims with authoritative lookups and stop for review if there is conflict or drift.
---

# Generate mock exams

Use a generated textbook and its associated study guide or curriculum source as inputs. The book and source may use any structure; do not assume or impose a study-guide format. Store produced exams in one directory per subject (`mock_exams/<subject>/<id>.exam.yaml`). The schema and validator are packaged with this skill:

```
pip install pyyaml jsonschema
python3 skills/generate-mock-exam/resources/validate.py mock_exams/<subject>/<id>.exam.yaml
```

When the exam comes from a textbook, also check tag/coverage alignment:

```
python3 skills/generate-mock-exam/resources/validate.py --coverage textbooks/<subject>/coverage.md mock_exams/<subject>/<id>.exam.yaml
```

Read the textbook's `metadata.yaml` for domains, topics, and source-stated weights. Questions should carry `references` once verified; unreviewed questions should say so in `source_note`.

Then run `python3 apps/quiz_app/serve.py` and open http://localhost:8000/ to pick any exam under `mock_exams/` (or open `apps/quiz_app/index.html` directly and load a file).

## Workflow

1. **Read both inputs.** Inspect the local textbook, its `coverage.md`, and the associated source guide/curriculum in its native form. The guide defines scope where it is explicit; the book supplies the organized teaching material. Record source version/as-of date and official domain weights when available.
2. **Compare for drift.** Compare the source's intent and available scope information with the textbook's extracted outcomes and content. Do not assume a textual or structural diff is sufficient. Note missing, added, changed, ambiguous, or stale coverage.
3. **Verify claims with lookups.** Prefer current official/primary documentation. Use reputable secondary sources when primary material does not sufficiently resolve a claim. Public official practice assessments or sample questions may inform exam style, but write original questions; do not use exam-ripping sites, dumps, or reproduce their questions.
4. **Stop on conflict.** If a material claim in the textbook, source guide, or current authoritative references conflicts or appears to have drifted, do not silently choose a version or generate questions from the disputed claim. Report the conflicting statements with links, explain why they matter, and ask the user how to proceed. Continue only after resolution.
5. **Create original questions.** Generate scenarios and distractors from resolved textbook content and extracted learning outcomes. Preserve official domain weights when available; do not invent weights if they are absent. Use source-appropriate domains/topics without requiring the guide to expose them in a particular format.
6. **Maintain traceability.** Use project-local learning-outcome IDs from `textbooks/<subject>/coverage.md` as question tags (`objective:<id>`). Update the map with question IDs. Track outcome coverage across the mock-exam set; an individual exam form may sample outcomes proportionally.
7. **Review and validate.** Check question claims, correct answers, explanations, distractor quality, objective mapping, weight distribution, and references. Run the packaged validator before use.

## Structure

```yaml
schema_version: 1
id: kubernetes-basics          # lowercase, digits, hyphens
title: Kubernetes Basics Mock Exam
description: ...               # optional
source_note: ...               # optional
pass_score_percent: 70         # optional
time_limit_minutes: 60         # optional (used by exam mode)
domains:
- id: core-concepts
  title: Core concepts
  weight: 20-25%               # optional free text
  topics:
  - {id: pods, title: Pods}
questions:
- id: 1                        # unique integer
  domain: core-concepts        # domains[].id
  topic: pods                  # optional, topics[].id of that domain
  type: single                 # single (default) | multiple | ordering | matching | yesno-series | hotspot | command
  text: Which object ...?
  options:                     # 2-8 options, ids A-H
  - {id: A, text: ..., explanation: why wrong}
  - {id: B, text: ..., explanation: why right/wrong}
  correct: [B]                 # list of option ids
  explanation: Why B is correct.
  difficulty: medium           # optional: easy | medium | hard
  tags: [optional]
  references: [https://...]    # optional
```

## Non-multiple-choice question types

`single` and `multiple` use `options` + `correct`. The other types replace them (they are not allowed to be mixed in, except that `text`, `explanation`, `tags`, etc. always apply). Match the formats described in the book's `EXAM-FORMAT.md`.

```yaml
# ordering: list items shuffled; correct_order is the right sequence
- id: 101
  domain: ...
  type: ordering
  text: Arrange the steps to ...
  items: [{id: A, text: ...}, {id: B, text: ...}, {id: C, text: ...}]
  correct_order: [B, C, A]

# matching: one correct choice per prompt; a choice may be reused
- id: 102
  type: matching
  text: Match each service to its description.
  prompts: [{id: "1", text: Azure Policy}, {id: "2", text: Azure RBAC}]
  choices: [{id: A, text: Controls who can act}, {id: B, text: Enforces resource rules}]
  correct_pairs: [{prompt: "1", choice: B}, {prompt: "2", choice: A}]

# yesno-series: each statement is true/false (include both)
- id: 103
  type: yesno-series
  text: For each statement, select Yes or No.
  statements: [{id: S1, text: ..., answer: true, explanation: ...}, {id: S2, text: ..., answer: false}]

# hotspot: one dropdown (slot) per blank, one correct option each
- id: 104
  type: hotspot
  text: Complete the command.
  slots:
  - id: H1
    text: "az ___ create"
    options: [{id: A, text: group}, {id: B, text: vm}]
    correct: A

# command: free text graded against accepted variants
- id: 105
  type: command
  text: Type the command that lists all resource groups.
  command:
    shell: azure-cli             # azure-cli | powershell | bash | cmd
    accepted: ["az group list"]  # list every valid variant, including short flags
    ignore_flag_order: true      # default
    case_sensitive: false        # default
    hint: optional
```

Rules: ordering items must not be listed in the correct order; ids for matching prompts are `1`-`8`, statements `S1`-`S8`, slots `H1`-`H6`; every question still needs an `explanation` and `references`. `command` answers should only cover what the exam expects (do not accept commands that fail or change different resources). The quiz app renders and grades all of these types.

## Quality rules
- Exactly one correct answer for `single`; 2+ for `multiple`, and the question text should say "Choose N".
- Every option has an `explanation`; the question has an `explanation`.
- Distractors are plausible; avoid "all/none of the above".
- Balance correct answer positions across A-D.
- Questions are self-contained (no references to other questions).
- Domain question counts roughly follow the exam's official weights.
- Tag each question with `objective:<id>` for every extracted learning outcome it assesses. IDs come from that textbook's `coverage.md`; they are internal traceability IDs, not identifiers required by the source guide.
- Choose domains/topics to reflect the exam scope and material; do not assume the source guide has a fixed hierarchy or format.
- Track coverage across the mock-exam set in `coverage.md`; each individual form may sample outcomes proportionally rather than test every outcome.
- Add authoritative source URLs in `references` for version-sensitive or product-specific answers.

## LLM prompt template

> Generate a mock-exam set on **{TOPIC}** targeting **{AUDIENCE/LEVEL}** from `textbooks/{subject}/` and its associated source curriculum. Before writing questions, compare scope and claims, look up current official documentation first and reputable secondary sources if needed, and stop to report conflicts or drift rather than choosing silently. Do not consult exam-ripping sites or reproduce leaked questions; write original questions. Conform each exam to `skills/generate-mock-exam/resources/exam.schema.json`. Preserve source-provided domain weights; do not invent them. Tag questions with internal `objective:<id>` values from `coverage.md` and update its question mapping. Include explanations and authoritative references.

Always run `python3 skills/generate-mock-exam/resources/validate.py <exam-file>` on generated output before use.

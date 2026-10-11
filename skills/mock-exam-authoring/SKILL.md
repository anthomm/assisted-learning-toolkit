---
name: mock-exam-authoring
description: Create and validate mock exam YAMLs that conform to the Study/mock_exams exam schema. Use when authoring, reviewing, or converting mock exams.
---

# Authoring mock exams

Store produced exams in one directory per subject (`mock_exams/<subject>/<id>.exam.yaml`). The schema and validator are packaged with this skill:

```
pip install pyyaml jsonschema
python3 skills/mock-exam-authoring/resources/validate.py mock_exams/<subject>/<id>.exam.yaml
```

Then open `apps/quiz_app/index.html` and load the file.

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
  type: single                 # single (default) | multiple
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

## Quality rules
- Exactly one correct answer for `single`; 2+ for `multiple`, and the question text should say "Choose N".
- Every option has an `explanation`; the question has an `explanation`.
- Distractors are plausible; avoid "all/none of the above".
- Balance correct answer positions across A-D.
- Questions are self-contained (no references to other questions).
- Domain question counts roughly follow the exam's official weights.

## LLM prompt template

> Generate a mock exam on **{TOPIC}** targeting **{AUDIENCE/LEVEL}** with **{N}** questions, as a single YAML document conforming to `skills/mock-exam-authoring/resources/exam.schema.json`. Use these domains and approximate weights: {DOMAINS}. Each question must have 4 options (A-D), a `correct` list, a per-option `explanation` (why right or wrong), and a general `explanation`. Include `topic` ids declared under each domain. Distribute correct answers evenly across A-D. Output only the YAML.

Always run `python3 skills/mock-exam-authoring/resources/validate.py <exam-file>` on generated output before use.

## Converting existing Markdown
`resources/legacy/legacy_md_to_yaml.py` converted `resources/legacy/AZ-900-mock-exam.md`; it is specific to that file's layout and kept only as a historical reference.

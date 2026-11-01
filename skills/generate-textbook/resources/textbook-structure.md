# Textbook structure

The reusable **output** contract for generated textbooks. Curriculum inputs are never standardized; only the output below is. `textbooks/` stores produced books only; this contract lives with the skill that produces them.

## Hierarchy

```
Domain / chapter   -> one numbered file (01-<slug>.md); carries its exam weight when the source gives one
  Topic            -> one H2 section inside the chapter file
    Teaching pattern (H3s, see below)
```

Chapters and topics are chosen from the extracted intent and pedagogy, not copied from source headings. Their number is not fixed.

## Book directory

```
textbooks/<book>/
  metadata.yaml       # structured facts the mock-exam skill reads (see below)
  CURRICULUM.md       # source record + extraction notes (no verbatim outline)
  00-intro.md         # scope, audience, weights, how to use, edition
  01-<chapter>.md ... # chapters with topics
  coverage.md         # traceability map (see below)
  EXAM-FORMAT.md      # exam-day guide (see below), for certification exams
  LABS.md             # index of linked labs and workshops (see below)
  CHANGELOG.md        # one entry per edition
  build/              # generated PDF/HTML from apps/textbook_pdf, gitignored, never hand-edited
```

## `metadata.yaml`

```yaml
title: ...
subject: ...
exam_code: ...            # optional
source:
  url: ...                # or file/manual description
  retrieved: YYYY-MM-DD
  as_of: YYYY-MM-DD       # the source's own version date, when it has one
  language: en
edition: ...
chapters:
- id: cloud-concepts
  title: ...
  weight: 25-30%          # only when the source states one; never invented
  file: 01-cloud-concepts.md
  topics:
  - {id: ..., title: ...}
```

The mock-exam skill derives domains, topics, and weights from this file.

## `CURRICULUM.md`

Records where the curriculum came from, when it was captured, its version/as-of date, and extraction notes (ambiguities, assumptions). Link to the source rather than reproducing its outline verbatim.

## `coverage.md` (working traceability map)

One table per topic, preceded by `Source locator: <where in the source>`. Columns:

| Outcome ID | Learning outcome (interpreted) | Confidence / note | Book section | Exam questions | Textbook | Exam |
|---|---|---|---|---|---|---|

- Outcome IDs are internal, stable, lower-case, hyphenated, in backticks. They are not source identifiers.
- Outcomes are interpretations in the author's words; they may split, merge, or add enrichment. Note `direct`, `inferred`, or `broad - consider splitting`.
- `Exam questions` lists question IDs (`—` if none). Questions carry the matching `objective:<id>` tag; `validate.py --coverage` checks both directions.
- Statuses: `todo`/`drafted`/`reviewed`. `reviewed` means a human checked the mapped material against the source and references; it never claims the source was exhaustive.
- Record known gaps in a closing section.

## `EXAM-FORMAT.md` (certification exams)

How the exam is delivered, from the official exam page, skills-measured document, and Microsoft's exam sandbox / practice assessment. Cover: question types (multiple choice, multiple response, ordering, matching, yes/no series, hotspot/dropdown, case studies, command or performance-based labs if present), number of questions and time, passing score, whether questions can be revisited (case studies and some sections lock), retake policy, and per question type an approach tip with a short original example. State only what the sources state; mark anything unconfirmed with `> **Verify:**` and record the retrieval date. Skip for non-exam books.

## `LABS.md` (linked hands-on resources)

An index of official external labs and workshops (Microsoft Learn modules with sandboxes, Learn challenge projects, Applied Skills, MS Learn/GitHub workshop repos). Do not copy lab content; link and describe. Table columns: Resource, Type (`sandbox` / `lab` / `workshop` / `applied-skill`), Link, Needs own subscription (yes/no), Chapter/topic, Outcome IDs (from `coverage.md`), Link checked (date). Only list resources that were actually opened and verified; mark cost or subscription needs.

## Teaching pattern for each topic

Learning intent, core concepts, how it works / distinctions / limits, example or worked scenario, hands-on activity (when applicable), official labs (linked, when available), exam or practical application (when applicable), self-check questions with answers, sources. Omit parts that do not fit. Mark uncertain or version-sensitive facts with `> **Verify:**`.

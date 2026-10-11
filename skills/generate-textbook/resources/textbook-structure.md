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
  CHANGELOG.md        # one entry per edition
  style.css, Makefile # only when a PDF build is wanted; book-local until a second book needs them
  build/              # generated, never hand-edited
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

## Teaching pattern for each topic

Learning intent, core concepts, how it works / distinctions / limits, example or worked scenario, hands-on activity (when applicable), exam or practical application (when applicable), self-check questions with answers, sources. Omit parts that do not fit. Mark uncertain or version-sensitive facts with `> **Verify:**`.

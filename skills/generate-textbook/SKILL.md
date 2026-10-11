---
name: generate-textbook
description: Turn a study guide, curriculum source, syllabus, or learning intent into an original textbook organized with a reusable teaching template. Accept unstructured inputs; extract intent rather than assuming a source format.
---

# Generate textbook

Create an editable textbook from the intent in a source curriculum. The source can be a URL, attached/local document, syllabus, or a manual description. Do not assume it has headings, bullets, domain percentages, or any other standardized structure. The generated book has a consistent pedagogical pattern; its chapter organization is chosen from the extracted material, not imposed on the source.

## Workflow

1. **Inspect and record the source.** Read the source in its native form. Record its URL or file/manual origin, retrieval date, exam or course identifier, locale, and any publication or "as of" date that is available. For web sources, use `web_fetch` and continue pagination when needed. Do not infer missing metadata.
2. **Extract intent with evidence.** Use AI to identify candidate domains, learning outcomes, important distinctions, scope, and any explicit weighting. For each candidate, record a locator or concise source cue and note whether it is directly stated, inferred, ambiguous, or absent. Source headings/bullets are evidence, not a required data model. Preserve explicit exam weights; do not invent percentages when none are supplied.
3. **Resolve important ambiguity.** If the intended audience, learning scope, source interpretation, or material conflict would significantly change the book, ask the user before writing that material. Keep competing interpretations visible rather than silently choosing.
4. **Design learning units and confirm.** Propose a Domain/chapter → Topic hierarchy that partitions the extracted intent, carrying source-stated percentages onto domains. Combine or split source material where pedagogically useful; do not force one-to-one source-to-heading mapping. Present the proposed organization to the user and get confirmation before drafting content (in autopilot, record it as an assumption in `CURRICULUM.md`).
5. **Create the book workspace.** One directory per book under `textbooks/`, following `resources/textbook-structure.md` (the output contract: `metadata.yaml`, `CURRICULUM.md`, `00-intro.md`, numbered chapters, `coverage.md`, `CHANGELOG.md`). PDF styling is shared in `apps/textbook_pdf/`; add book-local build assets only if a book needs a custom look.
6. **Write original teaching material.** Use the common topic pattern below, adapting or omitting parts that do not fit the subject. Ground factual claims in authoritative primary sources, using reputable secondary references when primary documentation is insufficient. Link sources; do not copy source material at length.
7. **Review traceability and uncertainty.** Check that each extracted outcome is addressed by one or more real book sections, and that every section's scope is explainable from the source or is explicitly marked as enrichment. Record omissions, uncertainty, and unresolved interpretation. A coverage map supports human review; it is not a formal schema or a guarantee that the source intent was exhaustively captured.
8. **Build and inspect if requested.** Keep Markdown as the editable source. If PDF output is needed and Pandoc/WeasyPrint are available, build from the Markdown and inspect the rendered TOC, code, tables, diagrams, and page breaks. Never hand-edit generated files in `build/`.

## Reusable topic pattern

```markdown
## Topic title

### Learning intent
### Core concepts
### How it works, distinctions, limits, and defaults
### Example or worked scenario
### Hands-on activity (when applicable)
### Exam or practical application (when applicable)
### Self-check questions (3–5, with answers)
### Sources
```

Group related outcomes when it improves understanding; split a broad area when it needs separate explanations. Use `> **Verify:**` for uncertain or version-sensitive facts.

## Coverage map

Use a human-readable `coverage.md` rather than a schema for arbitrary source curricula. Use the columns defined in `resources/textbook-structure.md` (outcome, confidence/note, book section, exam questions, statuses), with a source locator per topic. Interpret outcomes in your own words; do not copy source bullets verbatim.

Use stable project-local IDs for later mock-exam tags such as `objective:<id>`. Statuses may be `todo`, `drafted`, or `reviewed`; `reviewed` means a human checked the interpretation and material against available sources, not that the input source was guaranteed complete.

## Optional PDF build

When a PDF is wanted, use the shared app: `python3 apps/textbook_pdf/build_pdf.py <book>` (see `apps/README.md` for dependencies). It reads `metadata.yaml` and the chapter files, and writes to the book's gitignored `build/`. Never hand-edit generated output.

## Extending or revising a book

- If the curriculum source changes, inspect the new source and compare its intent with the existing extraction map; do not assume the same structure or merely diff heading text.
- Update affected learning outcomes, sections, question mappings, metadata, and `CHANGELOG.md`.
- Preserve prior edition context and identify uncertain or unresolved changes instead of silently overwriting it.

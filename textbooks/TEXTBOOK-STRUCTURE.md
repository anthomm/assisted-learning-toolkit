# Textbook structure

Formalizes the *output* (not the curriculum input, which is free-form; see README).

- One directory per textbook under `textbooks/`.
- `CURRICULUM.md` must exist and point to the source (URL or "manual") plus the verbatim outline.
- `00-intro.md`, then one numbered file per outline domain/section, in outline order.
- `coverage.md`: one row per outline bullet (verbatim) -> target heading -> status (`todo`/`drafted`/`reviewed`).
- `CHANGELOG.md`: one entry per edition.
- Chapter template: Learning objectives, then per bullet: Concepts, How it works / limits, Hands-on, Exam tips, Self-check questions.
- Mark uncertain or version-sensitive facts with `> **Verify:**`.
- `build/` is generated and never hand-edited.

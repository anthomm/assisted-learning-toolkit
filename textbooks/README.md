# textbooks

Parent of all generated textbooks. One directory per textbook, named `<subject>` in snake_case (e.g. `az_104`).

## Shared contract (lives here)
- `TEXTBOOK-STRUCTURE.md` – required layout, per-chapter template, coverage rules
- Shared build assets (`style.css`, Makefile template) go here when first needed, so textbooks don't duplicate them.
- Generation workflow: the `course-curriculum` skill.

## Per-textbook directory
```
<subject>/
  CURRICULUM.md     # pointer to the curriculum source (see below)
  00-intro.md  01-<chapter>.md ...
  coverage.md  CHANGELOG.md  metadata.yaml
  build/            # generated output, not edited
```

## Curriculum sources are NOT formalized
Study guides (e.g. https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-104),
syllabi and outlines have no guaranteed format, so no schema is imposed. `CURRICULUM.md` only records:
- **Source**: URL, or "manual" if hand-written
- **Retrieved / as-of date**
- **Outline**: the verbatim outline (copied or hand-defined) in whatever shape the source uses

Chapters and `coverage.md` are derived from that outline by the author/agent, not validated against a schema.

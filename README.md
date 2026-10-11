# Assisted Learning Toolkit (ALT)

Each top-level directory owns one responsibility. Output directories (`mock_exams/`, `textbooks/`)
hold only produced content, one subdirectory per subject. The contracts, schemas and tooling for
producing them live with the skills in `skills/`.

| Directory | Responsibility |
|---|---|
| `mock_exams/` | Produced mock exams only. One subdirectory per subject, containing exam files. |
| `textbooks/` | Generated reading material only. One subdirectory per textbook. |
| `apps/` | Standalone applications (one subdirectory each), e.g. `quiz_app/` for taking mock exams. |
| `skills/` | Study-specific agent skills, flat, one directory per skill. |
| `mock_maker/` | Reserved (empty). |

Mock-exam generation instructions, schema, and validation tools live with `skills/generate-mock-exam/`, not in `mock_exams/`.

Licensing, third-party notices, trademark disclaimer and content provenance: see `LICENSE` and `NOTICE.md`.

Textbook structure contract: `skills/generate-textbook/resources/textbook-structure.md`.

Rule: formal, shared definitions live in skills; subject-specific produced content lives in the output directories.

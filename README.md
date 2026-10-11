# Assisted Learning Toolkit (ALT)

Each top-level directory owns one responsibility. A **parent directory** holds the
shared contract (schema, tooling, authoring rules) for its artifact type; each
**child directory** holds one subject and conforms to that contract.

| Directory | Responsibility |
|---|---|
| `mock_exams/` | Produced mock exams only. One subdirectory per subject, containing exam files. |
| `textbooks/` | Generated reading material. One subdirectory per textbook. Contract at this level. |
| `apps/` | Standalone applications (one subdirectory each), e.g. `quiz_app/` for taking mock exams. |
| `skills/` | Study-specific agent skills, flat, one directory per skill. |
| `mock_maker/` | Reserved (empty). |

Authoring instructions, schema, validation tools, and legacy source/converter files for mock exams live with `skills/mock-exam-authoring/`, not in `mock_exams/`.

Licensing, third-party notices, trademark disclaimer and content provenance: see `LICENSE` and `NOTICE.md`.

Rule: formal, shared definitions live outside the artifact directory; subject-specific produced content lives in it.

# apps

Standalone applications that consume study artifacts. One directory per app; apps never store exams or textbooks themselves.

- `quiz_app/` – offline single-file quiz viewer for `mock_exams/**/*.exam.yaml`. Rebuild: `python3 apps/quiz_app/build_app.py apps/quiz_app/vendor/js-yaml.min.js`

# apps

Standalone applications that consume study artifacts. One directory per app; apps never store exams or textbooks themselves.

- `quiz_app/` – quiz viewer for `mock_exams/**/*.exam.yaml`. Fast start: `python3 apps/quiz_app/serve.py` then open http://localhost:8000/ (lists every exam in `mock_exams/`; localhost-only, read-only). The single-file `index.html` also works offline via file drop. Rebuild: `python3 apps/quiz_app/build_app.py apps/quiz_app/vendor/js-yaml.min.js`

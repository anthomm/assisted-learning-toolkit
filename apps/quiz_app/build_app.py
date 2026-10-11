"""Inline js-yaml into index.src.html -> index.html (single file, works offline).

Usage: python3 build_app.py vendor/js-yaml.min.js
"""
import sys
from pathlib import Path

root = Path(__file__).resolve().parent
lib = Path(sys.argv[1]).read_text(encoding="utf-8").replace("</script", "<\\/script")
src = (root / "index.src.html").read_text(encoding="utf-8")
(root / "index.html").write_text(src.replace("/*JSYAML*/", lib, 1), encoding="utf-8")
print("built", root / "index.html")

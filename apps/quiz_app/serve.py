"""Serve the quiz app and list every exam under mock_exams/.

Usage: python3 apps/quiz_app/serve.py [port]
Then open http://localhost:8000/ (default port 8000).
Only the app and mock_exams/ are exposed; everything is read-only and bound to localhost.
"""
import json
import sys
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

APP = Path(__file__).resolve().parent
ROOT = APP.parent.parent
EXAMS = ROOT / "mock_exams"


def list_exams():
    out = []
    for p in sorted(EXAMS.glob("*/*.exam.y*ml")) + sorted(EXAMS.glob("*/*.exam.json")):
        out.append({"subject": p.parent.name, "name": p.name, "path": "/mock_exams/" + p.relative_to(EXAMS).as_posix()})
    return out


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *a, **k):
        super().__init__(*a, directory=str(ROOT), **k)

    def do_GET(self):
        path = self.path.split("?", 1)[0]
        if path == "/api/exams":
            body = json.dumps(list_exams()).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        elif path in ("/", "/index.html"):
            self.path = "/apps/quiz_app/index.html" + ("?" + self.path.split("?", 1)[1] if "?" in self.path else "")
            super().do_GET()
        elif path.startswith(("/mock_exams/", "/apps/quiz_app/")):
            super().do_GET()
        else:
            self.send_error(404)

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    print(f"Quiz app: http://localhost:{port}/  (exams from {EXAMS})")
    ThreadingHTTPServer(("127.0.0.1", port), Handler).serve_forever()

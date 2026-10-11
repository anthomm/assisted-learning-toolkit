"""Turn a textbook's Markdown sources into a readable PDF.

Usage:
  python3 apps/textbook_pdf/build_pdf.py <book> [-o OUT.pdf]
  python3 apps/textbook_pdf/build_pdf.py --all
  python3 apps/textbook_pdf/build_pdf.py <book> --html     # also keep the intermediate HTML

<book> is a directory name under textbooks/ (for example az_900). Output defaults to
textbooks/<book>/build/<book>.pdf (build/ is generated and gitignored).

Requires: python3 -m pip install markdown-it-py pygments weasyprint pyyaml
On macOS, WeasyPrint also needs Pango: brew install pango
"""
import argparse
import html
import os
import re
import sys
from datetime import date
from pathlib import Path

if sys.platform == "darwin":
    for lib in ("/opt/homebrew/lib", "/usr/local/lib"):
        if Path(lib).is_dir():
            os.environ["DYLD_FALLBACK_LIBRARY_PATH"] = lib + ":" + os.environ.get("DYLD_FALLBACK_LIBRARY_PATH", "")

try:
    import yaml
    from markdown_it import MarkdownIt
    from pygments import highlight
    from pygments.formatters import HtmlFormatter
    from pygments.lexers import TextLexer, get_lexer_by_name
    from pygments.util import ClassNotFound
    from weasyprint import HTML
except ImportError as e:
    sys.exit(f"Missing dependency ({e.name}). Run: python3 -m pip install markdown-it-py pygments weasyprint pyyaml"
             "\nOn macOS also: brew install pango")

APP = Path(__file__).resolve().parent
ROOT = APP.parent.parent
BOOKS = ROOT / "textbooks"


def highlight_code(code, lang, _attrs):
    try:
        lexer = get_lexer_by_name(lang) if lang else TextLexer()
    except ClassNotFound:
        lexer = TextLexer()
    return '<pre class="hl"><code>' + highlight(code, lexer, HtmlFormatter(nowrap=True)) + "</code></pre>"


MD = MarkdownIt("commonmark", {"highlight": highlight_code}).enable("table")


def book_files(book_dir, meta):
    files = []
    intro = book_dir / "00-intro.md"
    if intro.exists():
        files.append(("front", intro))
    listed = [book_dir / c["file"] for c in meta.get("chapters", []) if c.get("file")]
    chapters = listed or sorted(p for p in book_dir.glob("[0-9][0-9]-*.md") if p.name != "00-intro.md")
    files += [("chapter", p) for p in chapters if p.exists()]
    return files


def render_md(text):
    return MD.render(text)


def add_ids(body, counter):
    """Give every h1/h2 a unique id; return the new html and the outline entries."""
    outline = []

    def sub(m):
        level, inner = int(m.group(1)), m.group(2)
        counter[0] += 1
        hid = f"s{counter[0]}"
        outline.append((level, hid, re.sub(r"<[^>]+>", "", html.unescape(inner))))
        return f'<h{level} id="{hid}">{inner}</h{level}>'

    return re.sub(r"<h([12])(?: [^>]*)?>(.*?)</h\1>", sub, body, flags=re.S), outline


def build_html(book_dir, meta):
    title = meta.get("title") or book_dir.name
    parts, toc, counter = [], [], [0]
    for kind, path in book_files(book_dir, meta):
        body, outline = add_ids(render_md(path.read_text(encoding="utf-8")), counter)
        parts.append(f'<section class="{kind}">{body}</section>')
        toc += [(kind, *o) for o in outline]

    toc_html, chap, sec = [], 0, 0
    for kind, level, hid, text in toc:
        label = ""
        if level == 1 and kind == "chapter":
            chap, sec = chap + 1, 0
            label = f"{chap}. "
        elif level == 2 and kind == "chapter":
            sec += 1
            label = f"{chap}.{sec} "
        toc_html.append(f'<li class="l{level}"><a href="#{hid}">{html.escape(label + text)}</a></li>')

    src = meta.get("source") or {}
    facts = [f"Edition {meta['edition']}" if meta.get("edition") else None,
             f"Skills measured as of {src['as_of']}" if src.get("as_of") else None]
    cover = (f'<section class="cover"><p class="code">{html.escape(str(meta.get("exam_code", "")))}</p>'
             f'<h1 class="cover-title">{html.escape(title)}</h1>'
             f'<p class="facts">{html.escape(" · ".join(f for f in facts if f))}</p>'
             f'<p class="small">Source: {html.escape(str(src.get("url", "")))}</p>'
             f'<p class="small">Built {date.today().isoformat()}. An independent study aid, not Microsoft material.</p></section>')
    css = (APP / "style.css").read_text(encoding="utf-8") + HtmlFormatter(style="friendly").get_style_defs(".hl")
    css += "\n@page { @bottom-left { content: \"%s\"; } }" % title.replace('"', "'")
    return (f'<!doctype html><html lang="{src.get("language", "en")}"><head><meta charset="utf-8">'
            f"<title>{html.escape(title)}</title><style>{css}</style></head><body>{cover}"
            f'<section class="toc"><h1 class="plain">Contents</h1><ul>{"".join(toc_html)}</ul></section>'
            f'{"".join(parts)}</body></html>')


def build(book, out=None, keep_html=False):
    book_dir = BOOKS / book
    if not book_dir.is_dir():
        sys.exit(f"No such textbook: {book_dir}")
    meta_path = book_dir / "metadata.yaml"
    meta = yaml.safe_load(meta_path.read_text(encoding="utf-8")) if meta_path.exists() else {}
    page = build_html(book_dir, meta or {})
    out = Path(out) if out else book_dir / "build" / f"{book}.pdf"
    out.parent.mkdir(parents=True, exist_ok=True)
    if keep_html:
        out.with_suffix(".html").write_text(page, encoding="utf-8")
    HTML(string=page, base_url=str(book_dir)).write_pdf(out)
    print(f"built {out}")
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("book", nargs="?", help="directory name under textbooks/")
    ap.add_argument("-o", "--output")
    ap.add_argument("--all", action="store_true", help="build every textbook")
    ap.add_argument("--html", action="store_true", help="also write the intermediate HTML")
    a = ap.parse_args()
    if a.all:
        for d in sorted(p for p in BOOKS.iterdir() if p.is_dir()):
            build(d.name, keep_html=a.html)
    elif a.book:
        build(a.book, a.output, a.html)
    else:
        ap.error("give a textbook name or --all")

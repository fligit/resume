#!/usr/bin/env python3
"""Bundle slides/*.html + styles.css into a self-contained dist/index.html.

The bundled file inlines every slide and the stylesheet, and drops the fetch
loader, so it works when opened directly via file:// (double-click).

Usage: ./build.sh  (or: python3 build.py)
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).parent
DIST = ROOT / "dist"

manifest = json.loads((ROOT / "slides.json").read_text())
slides_html = "\n\n".join((ROOT / p).read_text().rstrip() for p in manifest)
styles = (ROOT / "styles.css").read_text()

HTML = f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
    <title>Fan Li — Self Introduction</title>

    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/dist/reset.css" />
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/dist/reveal.css" />
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/dist/theme/black.css" id="theme" />
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/plugin/highlight/monokai.css" />
    <style>
{styles}
    </style>
  </head>
  <body>
    <div class="reveal">
      <div class="slides">
{slides_html}
      </div>
    </div>

    <div class="footer-note">Fan Li · Self Introduction · Built with reveal.js</div>

    <script src="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/dist/reveal.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/plugin/notes/notes.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/plugin/highlight/highlight.js"></script>
    <script>
      Reveal.initialize({{
        hash: true,
        slideNumber: "c/t",
        controls: true,
        progress: true,
        center: false,
        width: 1280,
        height: 800,
        margin: 0.04,
        transition: "slide",
        backgroundTransition: "fade",
        plugins: [RevealHighlight, RevealNotes],
      }});
    </script>
  </body>
</html>
"""

DIST.mkdir(exist_ok=True)
(DIST / "index.html").write_text(HTML)
print(f"Bundled {len(manifest)} slides → {DIST / 'index.html'}")

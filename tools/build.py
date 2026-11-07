#!/usr/bin/env python3
"""Build index.html from src/index.html.

Subsets Mitad's fonts to the characters on the page, embeds them as base64
between the /* fonts:start */ and /* fonts:end */ markers, and minifies the
result into index.html, the one file that gets uploaded.

Every trim here was checked against screenshots of the unminified page with
Mitad's original fonts: 41 renders, pixel-identical. Narrowing a variable axis
away from its default re-rounds outlines and moves edge pixels, so only
Literata's weight, which the page uses at its default (400), is pinned.

    pip install fonttools brotli minify-html     # and Node, for npx esbuild
    python3 tools/build.py [path/to/design-system/fonts]

The source fonts default to ../design-system/fonts. After changing any text
the fonts draw, update the "text" entries below and rebuild.
"""

import base64
import io
import re
import subprocess
import sys
from pathlib import Path

import minify_html
from fontTools import subset
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer

ROOT = Path(__file__).resolve().parent.parent
SRC = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT.parent / "design-system" / "fonts"

FONTS = [
    {
        "family": "Archivo",
        "file": "archivo-var.woff2",
        "pin": None,
        "weight": "100 900",
        "style": "normal",
        "text": "Hola Salut Hi Salü, I’m José.",  # greetings, name, hidden heading
    },
    {
        "family": "Literata",
        "file": "literata-italic-var.woff2",
        "pin": {"wght": 400},
        "weight": "400",
        "style": "italic",
        "text": "hello@josemanosalvas.ch",
    },
    {
        "family": "B612 Mono",
        "file": "b612mono-400.woff2",
        "pin": None,
        "weight": "400",
        "style": "normal",
        "text": "GITHUB",  # uppercased in CSS
    },
]


# font-display: block, not swap. The fonts are in the page, so they cannot be
# slow or fail to arrive; they only need decoding. Under swap a slow CPU paints
# one frame in Helvetica and Georgia first (measured at 10x CPU throttling).

def font_face(font):
    tt = TTFont(SRC / font["file"])
    if font["pin"]:
        tt = instancer.instantiateVariableFont(tt, font["pin"])
    opts = subset.Options()
    opts.layout_features = ["kern"]   # nothing else applies to this text
    opts.name_IDs = []                # family names come from @font-face
    opts.name_languages = []
    opts.name_legacy = False
    opts.drop_tables += ["STAT"]
    opts.flavor = "woff2"             # hinting is kept: B612 needs it at 12px on Windows
    sub = subset.Subsetter(opts)
    sub.populate(text=font["text"])
    sub.subset(tt)
    buf = io.BytesIO()
    tt.flavor = "woff2"
    tt.recalcTimestamp = False        # same input, same bytes
    tt.save(buf)
    data = buf.getvalue()
    css = (
        f"@font-face{{font-family:'{font['family']}';"
        f"src:url(data:font/woff2;base64,{base64.b64encode(data).decode()}) format('woff2');"
        f"font-weight:{font['weight']};font-style:{font['style']};font-display:block;"
        "ascent-override:80%;descent-override:20%;line-gap-override:0%}"
    )
    return css, len(data)


def minify_js(code):
    # esbuild shortens local names and drops comments; minify-html's JS pass does neither.
    run = subprocess.run(
        ["npx", "--yes", "esbuild@0.25.10", "--minify", "--charset=utf8", "--loader=js"],
        input=code, capture_output=True, text=True, check=True,
    )
    return run.stdout.strip()


def main():
    html = (ROOT / "src" / "index.html").read_text(encoding="utf-8")
    faces, fonts = [], 0
    for font in FONTS:
        css, size = font_face(font)
        faces.append(css)
        fonts += size
    marker = re.compile(r"/\* fonts:start \*/.*?/\* fonts:end \*/", re.S)
    if not marker.search(html):
        sys.exit("src/index.html has no /* fonts:start */ … /* fonts:end */ markers")
    html = marker.sub(lambda _: "\n".join(faces), html)
    html = re.sub(r"(?s)<script>(.*?)</script>", lambda m: f"<script>{minify_js(m[1])}</script>", html)
    out = minify_html.minify(html, minify_css=True)
    (ROOT / "index.html").write_text(out, encoding="utf-8")
    print(f"fonts {fonts} B, index.html {len(out.encode())} B")


if __name__ == "__main__":
    main()

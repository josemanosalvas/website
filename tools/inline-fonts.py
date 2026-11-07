#!/usr/bin/env python3
"""Subset Mitad's fonts to the characters on the page and embed them.

Each face is cut down to the exact characters it draws, then written into
index.html as base64
@font-face rules between the /* fonts:start */ and /* fonts:end */ markers.

Run it again after changing any text the fonts draw (the greetings, the
name, the email, the GitHub label), and update the "text" entries below.

    pip install fonttools brotli
    python3 tools/inline-fonts.py [path/to/design-system/fonts]

The source fonts default to ../design-system/fonts (the Mitad repo checked
out next to this one).
"""

import base64
import io
import re
import sys
from pathlib import Path

from fontTools import subset
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer

ROOT = Path(__file__).resolve().parent.parent
SRC = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT.parent / "design-system" / "fonts"

# "axes" can pin or narrow variable axes ({"wght": 400} or {"wght": (200, 800)}),
# but it is off for both variable faces: narrowing re-rounds the outlines and
# moves edge pixels (measured: ~5,000 anti-aliasing pixels per screen differed
# from Mitad's originals). Whole axes cost 7.6 KB more and render identically.
FONTS = [
    {
        "family": "Archivo",
        "file": "archivo-var.woff2",
        "axes": None,
        "weight": "100 900",
        "style": "normal",
        # Greetings (index.html script), the name, and the hidden heading text.
        "text": "Hola Salut Hi Salü, I’m José.",
    },
    {
        "family": "Literata",
        "file": "literata-italic-var.woff2",
        "axes": None,
        "weight": "200 900",
        "style": "italic",
        "text": "hello@josemanosalvas.ch",
    },
    {
        "family": "B612 Mono",
        "file": "b612mono-400.woff2",
        "axes": None,
        "weight": "400",
        "style": "normal",
        "text": "GITHUB",  # the label is uppercased in CSS
    },
]


def build(font):
    tt = TTFont(SRC / font["file"])
    if font["axes"]:
        # A number pins an axis; a (min, max) pair narrows it.
        tt = instancer.instantiateVariableFont(tt, font["axes"])
    opts = subset.Options()
    opts.layout_features = ["*"]
    opts.flavor = "woff2"
    sub = subset.Subsetter(opts)
    sub.populate(text=font["text"])
    sub.subset(tt)
    buf = io.BytesIO()
    tt.flavor = "woff2"
    tt.save(buf)
    data = buf.getvalue()
    b64 = base64.b64encode(data).decode("ascii")
    css = (
        "  @font-face {\n"
        f"    font-family: '{font['family']}';\n"
        f"    src: url(data:font/woff2;base64,{b64}) format('woff2');\n"
        f"    font-weight: {font['weight']};\n"
        f"    font-style: {font['style']};\n"
        "    font-display: swap;\n"
        "    ascent-override: 80%;\n"
        "    descent-override: 20%;\n"
        "    line-gap-override: 0%;\n"
        "  }"
    )
    return css, len(data)


def main():
    page = ROOT / "index.html"
    html = page.read_text(encoding="utf-8")
    blocks, total = [], 0
    for font in FONTS:
        css, size = build(font)
        blocks.append(f"  /* {font['family']} {font['style']} — {font['text']!r} */\n{css}")
        total += size
        print(f"{font['family']:<10} {font['style']:<7} {size:>6} bytes")
    pattern = re.compile(r"/\* fonts:start \*/.*?/\* fonts:end \*/", re.S)
    if not pattern.search(html):
        sys.exit("index.html has no /* fonts:start */ … /* fonts:end */ markers")
    html = pattern.sub(lambda _: "/* fonts:start */\n" + "\n".join(blocks) + "\n  /* fonts:end */", html)
    page.write_text(html, encoding="utf-8")
    print(f"{'total':<18} {total:>6} bytes embedded in index.html")


if __name__ == "__main__":
    main()

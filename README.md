# josemanosalvas.ch

The homepage at [josemanosalvas.ch](https://josemanosalvas.ch). Set in Mitad, my personal
design system: its faces and colours, with a composition of its own.

## What's here

```
index.html        built and minified: the only file visitors load (25 KB, 16 KB gzipped)
src/index.html    the readable source
tools/build.py    builds index.html from src/
OFL.txt           licence for the embedded fonts
```

A visit is one request. Markup, CSS, script, favicon and fonts are all inside `index.html`.
The fonts are subset to the characters they draw and embedded as base64.

## Editing

Edit `src/index.html`, never `index.html`. Then build, with the Mitad repo checked out next
to this one:

```sh
pip install fonttools brotli minify-html     # Node is also needed, for esbuild
python3 tools/build.py                       # or pass the path to design-system/fonts
```

The fonts only contain the characters on the page. If you change the greetings, the name,
the email or the GitHub label, or the glyphs the greeting cuts through, update the `text` entries
in `tools/build.py` first, or new letters will fall back to Helvetica, Georgia or Courier.

The build is deterministic: the same source gives the same bytes.

## The greeting

Only the greeting moves, alternating between Hola and Salü. On load, Hola's letters cut through
Mitad's three faces, then each greeting breaks up in place and the other resolves out of symbols
and stickers. Its last letter lands as a sticker for a moment. When the word is whole, its flag
hops on top to say where the word is from, and leaves about a second later while the word stays.
What goes with each word is the `greetings` list at the foot of `src/index.html`, and the first
greeting's timing is the `intro` score beside it.

Everything keeps to one 90 ms beat and one 36-beat bar, whatever the word's length. While a word
is in pieces each letter holds its resting width, so only the last letter's mark can add to the
title, and the widest state stays inside the page margin down to 320 px. Anything wider than a
letter needs room checked first, and `l` only takes the slim symbols.

Flags are the visitor's own emoji, so they look different on each system, and Chrome and Edge on
Windows show letters instead (EC, CH). Everything else is inline SVG in the sprite at the top of
`<body>`. Without JS or with reduced motion, the page simply stands still.

## Deploying to Infomaniak

The site is hosted on Infomaniak's free Starter web hosting. Upload `index.html` and
`OFL.txt` to the web root using Web FTP in the Infomaniak Manager or any FTP client.

The Starter plan has no IPv6, so make sure the domain has no AAAA record, or SSL may not
activate.

## Fonts

Archivo, Literata and B612 Mono are licensed under the SIL Open Font License 1.1, see
`OFL.txt`.

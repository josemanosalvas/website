# josemanosalvas.ch

The homepage at [josemanosalvas.ch](https://josemanosalvas.ch). Set in Mitad, my personal
design system: its faces and colours, with a composition of its own.

## What's here

```
index.html        built and minified: the only file visitors load (17 KB, 12 KB gzipped)
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

The fonts only contain the characters on the page. If you change the greeting, the name,
the email or the GitHub label, update the `text` entries in `tools/build.py` first, or new
letters will fall back to Helvetica, Georgia or Courier.

The build is deterministic: the same source gives the same bytes.

## Deploying to Infomaniak

The site is hosted on Infomaniak's free Starter web hosting. Upload `index.html` and
`OFL.txt` to the web root using Web FTP in the Infomaniak Manager or any FTP client.

The Starter plan has no IPv6, so make sure the domain has no AAAA record, or SSL may not
activate.

## Fonts

Archivo, Literata and B612 Mono are licensed under the SIL Open Font License 1.1, see
`OFL.txt`.

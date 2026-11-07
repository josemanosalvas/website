# josemanosalvas.ch

The homepage at [josemanosalvas.ch](https://josemanosalvas.ch). Set in Mitad, my personal
design system: its faces and colours, with a composition of its own.

## What's here

```
index.html        built and minified: the only file visitors load (36 KB, 24 KB gzipped)
src/index.html    the readable source
src/shepherd.avif the white Swiss shepherd, embedded by the build
tools/build.py    builds index.html from src/
tools/shepherd.html  the 3D model the shepherd is rendered from
OFL.txt           licence for the embedded fonts
```

A visit is one request. Markup, CSS, script, favicon and fonts are all inside `index.html`.
The fonts are subset to the characters they draw and embedded as base64, like the shepherd.

## Editing

Edit `src/index.html`, never `index.html`. Then build, with the Mitad repo checked out next
to this one:

```sh
pip install fonttools brotli minify-html     # Node is also needed, for esbuild
python3 tools/build.py                       # or pass the path to design-system/fonts
```

The fonts only contain the characters on the page. If you change the greetings, the name,
the email or the GitHub label, or the greeting's symbol, update the `text` entries
in `tools/build.py` first, or new letters will fall back to Helvetica, Georgia or Courier.

The build is deterministic: the same source gives the same bytes.

## The greeting

Only the greeting moves, alternating between Hola and Salü. The `l` never changes: it's the
third letter of both words, so the word never leaves. Around it, the last letter cuts to a
sparkle for Hola or the white Swiss shepherd for Salü, the second to a slash, and the first
inflates into liquid silver and sets back into ink. New letters grow from hairline to heavy,
and the word is whole in under a second. Then the `l` grows into a flagpole and the word's
flag opens from it, to say where the word is from. It closes a little over a second later,
the `l` comes back down, and the word rests.

What goes with each word is the `greetings` list at the foot of `src/index.html`, and all the
timing is the block under it, on one clock. Letters are placed by transforms, so nothing
reflows and the title can't grow. They stay in their slots after the first change, so nothing
is re-rendered when a word comes to rest.

The silver letter isn't an image or a video. It comes from Archivo's own outline: the page
draws the letter, solves the shape a balloon would take and lights it in WebGL. Anything wider
or taller than today's needs checking: `--hello` is what keeps the flag on screen, and the
`nudge` values are set by eye for these two words.

The flags and the sparkle are the visitor's own emoji, so Apple devices show Apple's. Each is
drawn once to a canvas and cropped to its ink, which puts it in the same place on every
system. Chrome and Edge on Windows have no flag emoji, so there the flag is drawn from the
rectangles in `greetings`. No system has a white Swiss shepherd, so that one is a small render:
`tools/shepherd.html` is the model and says how to make a new `src/shepherd.avif`.

Without WebGL the letters still change, with no silver, shepherd or flag. Without JS or with
reduced motion, the page simply stands still.

## Deploying to Infomaniak

The site is hosted on Infomaniak's free Starter web hosting. Upload `index.html` and
`OFL.txt` to the web root using Web FTP in the Infomaniak Manager or any FTP client.

The Starter plan has no IPv6, so make sure the domain has no AAAA record, or SSL may not
activate.

## Fonts

Archivo, Literata and B612 Mono are licensed under the SIL Open Font License 1.1, see
`OFL.txt`.

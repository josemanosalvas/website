# josemanosalvas.ch

The homepage at [josemanosalvas.ch](https://josemanosalvas.ch). Set in Mitad, my personal
design system: its faces and colours, with a composition of its own.

## What's here

```
index.html        built and minified: the only file visitors load (44 KB, 30 KB gzipped)
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
the email or the GitHub label, or the glyphs the greeting passes through, update the `text` entries
in `tools/build.py` first, or new letters will fall back to Helvetica, Georgia or Courier.

The build is deterministic: the same source gives the same bytes.

## The greeting

Only the greeting moves, alternating between Hola and Salü every 2.8 s, and each change is
one quick gesture of about 1.3 s. The `l` never changes: it's the third letter of both words,
so the word never leaves.

It's two bursts and an accent. First a run of hard cuts two frames apart: the second letter
passes through glyphs from its own language (ñ, á, ó on the way to Hola; the Swiss cross, ö, ä
on the way to Salü) in the page's other two faces, the first letter goes to Literata italic
and is then poured in lacquer of its flag's colour, and an animal lands in the last slot, the
Galápagos tortoise or the white Swiss shepherd. Then the `l` shoots up into a flagpole and
knocks the animal out, the first letter cuts to ink and the last letter drops in. Only then,
over the whole word, the flag comes out of the pole. It stays a moment, goes back in, and the
pole drops.

What goes with each word is the `greetings` list at the foot of `src/index.html`, and all the
timing is the score under it, on one clock of 60 fps frames, so a display at any rate lands on
the same beats. Letters are placed by transforms, so nothing reflows. Each state of the word is
set tight from the widths of the glyphs it shows, so the word stays one block on the way, and
comes to rest exactly where plain text would set it. The letters stay in their slots after the
first change, so nothing is re-rendered when a word comes to rest.

The liquid letter isn't an image or a video. It comes from Archivo's own outline: the page draws
the letter, solves the shape a balloon would take inside that outline and lights it in WebGL,
in the page's own Azul or Ají, so dark mode gets Guayas and its lighter red. Anything wider or
taller than today's needs checking: `--hello` keeps the word on screen, the pole measures the
room above the word so the flag can't reach the top of the window, and the `nudge` values are
set by eye for these two words.

The flags and the tortoise are the visitor's own emoji, so Apple devices show Apple's. Each is
drawn once to a canvas and cropped to its ink, which puts it in the same place on every system.
Chrome and Edge on Windows have no flag emoji, so there the flag is drawn from the rectangles in
`greetings`. No system has a white Swiss shepherd, so that one is a small render:
`tools/shepherd.html` is the model and says how to make a new `src/shepherd.avif`.

Without WebGL the letters still change, with no liquid, animal or flag. Without JS or with
reduced motion, the page simply stands still.

## Deploying to Infomaniak

The site is hosted on Infomaniak's free Starter web hosting. Upload `index.html` and
`OFL.txt` to the web root using Web FTP in the Infomaniak Manager or any FTP client.

The Starter plan has no IPv6, so make sure the domain has no AAAA record, or SSL may not
activate.

## Fonts

Archivo, Literata and B612 Mono are licensed under the SIL Open Font License 1.1, see
`OFL.txt`.

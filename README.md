# josemanosalvas.ch

The homepage at [josemanosalvas.ch](https://josemanosalvas.ch). Set in Mitad, my personal
design system: its faces and colours, with a composition of its own.

## What's here

```
index.html        built and minified: the only file visitors load (64 KB, 43 KB gzipped)
src/index.html    the readable source
src/shepherd.avif the white Swiss shepherd, four poses in a strip, embedded by the build
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

Only the greeting moves. A visit opens with two changes, to Salü and back to Hola, a change and
a rest apart, and then the word stays: it's all over within five seconds of the first move.
Pointing at the word, or tapping it, plays one more. The `l` never changes and never moves: it's
the third letter of both words, so the word never leaves.

Each change takes about 1.7 s and runs fast and then slower, the way a thrown thing settles,
like the title of Apple's Mac mini page. First a burst of hard cuts, one letter at a time, two
frames apart. The second letter passes through glyphs from its own language (ñ, á, ó on the way
to Hola; the Swiss cross, ä, ö on the way to Salü) in the page's other two faces, at the word's
own weight, and the first letter turns italic. Then the first letter becomes its own 3D model:
it inflates in clay, in a pastel of the word's colour, turns to glossy lacquer on a beat, and is
un-built along its own strokes, a wireframe running ahead of the ink letter it uncovers. When a
glyph on the way needs more room, the first letter steps aside to make it. Glyphs change on a
cut, but the spacing slides to its new places over a few frames. The animal slides out from
behind the `l`, brakes and waits in the last letter's place: the Galápagos tortoise, or the
white Swiss shepherd, which acts through four poses rendered from its 3D model. The second
letter comes back with a halo in the word's colour. Then the `l` shoots up into a flagpole and
flings the animal away, the last letter lands, and the flag unfurls from behind the pole. The
halo fades, the flag goes back in, and the pole drops.

What goes with each word is the `greetings` list at the foot of `src/index.html`, and all the
timing is the score under it, on one clock of 60 fps frames counted from each change's first
frame, so a display at any rate lands on the same beats. Successive changes to the same word
take turns between two sets of glyphs, so the fourth change isn't the second again. Letters are
placed by transforms, so nothing reflows. Each glyph on the way is sized to fill the letter it
stands in for, never larger than its face's own size, and set by its ink at the finished word's
own gaps, so every state of the word keeps the word's spacing. The animal takes the last
letter's place and size, standing on the baseline. The `nudge` values kern the two words and set
their `l` in the same place.

The 3D letter isn't an image or a video. It comes from Archivo's own outline: the page draws the
letter, inflates it like a balloon (the square root of the steady pressure inside its outline,
so every stroke is a round tube as wide as the stroke), and lights it in WebGL in the page's own
blue and red, the same as the flat letters in either theme. The path it's un-built along is the
distance through the letter from its lowest leftmost point. Anything wider or taller than
today's needs checking: `--hello` keeps the word on screen, and the pole measures the room above
the word so the flag stays out of the page's top margin.

The flags and the tortoise are the visitor's own emoji, so Apple devices show Apple's. Each is
drawn once to a canvas and cropped to its ink, which puts it in the same place on every system.
Chrome and Edge on Windows have no flag emoji, so there the flag is drawn from the rectangles in
`greetings`. No system has a white Swiss shepherd, so that one is a strip of renders:
`tools/shepherd.html` is the model and says how to make a new `src/shepherd.avif`.

Without WebGL the letters still change, with no 3D letter, animal or flag. Without JS or with
reduced motion, the page simply stands still.

## Deploying to Infomaniak

The site is hosted on Infomaniak's free Starter web hosting. Upload `index.html` and
`OFL.txt` to the web root using Web FTP in the Infomaniak Manager or any FTP client.

The Starter plan has no IPv6, so make sure the domain has no AAAA record, or SSL may not
activate.

## Fonts

Archivo, Literata and B612 Mono are licensed under the SIL Open Font License 1.1, see
`OFL.txt`.
